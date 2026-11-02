"""Read-only source/control and Ren'Py statement-ID audit for editorial builds.

Usage: python tools/readability_ast_audit.py Q:/b0 Q:/p1 --output Q:/p1/editorial_ast.json
Both arguments may also be the private cs_scripts_5ea2d086 directories.
No compiled Python, game, builder or authoring generator is executed.
"""
from pathlib import Path
from collections import Counter
import argparse
import io
import json
import re

from rpyc_audit import DataUnpickler, payload

ROOT = Path(__file__).resolve().parent.parent
NAMESPACE = 'cs_scripts_5ea2d086'
GROUPS = ('prologue', 'day01', 'day02', 'day03', 'day04')
SAY = re.compile(r'^\s*(?:cs_\w+|el)\s+"')
FROZEN = 'days/day03/part03/95_scene.rpy'


def compiled_root(path):
    path = Path(path)
    candidates = (path / 'content' / NAMESPACE, path / NAMESPACE, path)
    for candidate in candidates:
        if (candidate / 'scriot.rpyc').is_file():
            return candidate
    raise ValueError('Cannot find private compiled scripts under ' + str(path))


def source_root(path, fallback=None):
    path = Path(path)
    for candidate in (path / 'source_snapshot', path):
        if (candidate / 'scriot.rpy').is_file():
            return candidate
    if fallback is not None:
        return Path(fallback)
    raise ValueError('Pass a build with source_snapshot or --before-source/--after-source')


def ast_nodes(path, slot=1):
    """Return data-only AST records, preserving separate nodes with equal IDs."""
    root = DataUnpickler(io.BytesIO(payload(path, slot)), encoding='utf8', errors='replace').load()
    result, seen, stack = [], set(), [root]
    while stack:
        item = stack.pop()
        if id(item) in seen:
            continue
        seen.add(id(item))
        if isinstance(item, dict):
            stack.extend(item.values())
        elif isinstance(item, (list, tuple, set, frozenset)):
            stack.extend(item)
        elif hasattr(item, '__dict__'):
            attributes = vars(item)
            stack.extend(attributes.values())
            if getattr(item, 'audit_module', '') == 'renpy.ast' and 'name' in attributes:
                result.append(dict(id=repr(attributes['name']), kind=type(item).__name__,
                                   line=attributes.get('linenumber'), filename=attributes.get('filename'),
                                   who=attributes.get('who'), what=attributes.get('what')))
    return sorted(result, key=lambda n: (n['line'] or 0, n['id']))


def control_signature(text, rel, permit_document_fix=False):
    lines = text.splitlines()
    if permit_document_fix and rel == 'days/day04/01_scene.rpy':
        # The author's explicitly approved exception: no magnified reuse of the
        # dated 1963 photo for the first undated photograph on the wall.
        pairs = [('    show cs_d4_document photo1963 at cs_d4_document_center zorder 40',
                  '    with dissolve'), ('    hide cs_d4_document', '    with dissolve')]
        for first, second in pairs:
            hits = [i for i in range(len(lines) - 1) if lines[i:i + 2] == [first, second]]
            if hits:
                if len(hits) != 1:
                    raise AssertionError('Nonunique permitted document operation: ' + rel)
                del lines[hits[0]:hits[0] + 2]
    return [line for line in lines if line.strip() and not line.lstrip().startswith('#') and not SAY.match(line)]


def audit(before, after, groups=GROUPS, before_source=None, after_source=None):
    old_compiled, new_compiled = compiled_root(before), compiled_root(after)
    old_source = source_root(before, before_source)
    new_source = source_root(after, after_source)
    errors, files, absent, added = [], [], [], []
    old_global, new_global = {}, {}
    for group in groups:
        relatives = sorted(p.relative_to(old_source).as_posix() for p in (old_source / 'days' / group).rglob('*.rpy'))
        current = {p.relative_to(new_source).as_posix() for p in (new_source / 'days' / group).rglob('*.rpy')}
        if set(relatives) != current:
            errors.append('Source file set changed in ' + group)
        for rel in relatives:
            old_path, new_path = old_source / rel, new_source / rel
            if not new_path.is_file():
                continue
            old_text, new_text = old_path.read_text(encoding='utf-8-sig'), new_path.read_text(encoding='utf-8-sig')
            a = control_signature(old_text, rel, True)
            b = control_signature(new_text, rel, True)
            if a != b:
                errors.append('Control/menu/state/staging signature changed: ' + rel)
            old_cache, new_cache = old_compiled / Path(rel).with_suffix('.rpyc'), new_compiled / Path(rel).with_suffix('.rpyc')
            if not old_cache.is_file() or not new_cache.is_file():
                errors.append('Missing compiled file: ' + rel)
                continue
            old_nodes, new_nodes = ast_nodes(old_cache), ast_nodes(new_cache)
            old_ids, new_ids = {n['id'] for n in old_nodes}, {n['id'] for n in new_nodes}
            for side, cache, global_ids in [('before', old_cache, old_global), ('after', new_cache, new_global)]:
                for slot in (1, 2):
                    try:
                        nodes = ast_nodes(cache, slot)
                    except ValueError:
                        if slot == 2:
                            continue
                        raise
                    counts = Counter(n['id'] for n in nodes)
                    for ident, number in counts.items():
                        if number > 1:
                            errors.append('%s slot%s duplicate ID inside %s: %s' % (side, slot, rel, ident))
                        key = (slot, ident)
                        if key in global_ids and global_ids[key] != rel:
                            errors.append('%s slot%s ID collision: %s and %s' % (side, slot, global_ids[key], rel))
                        global_ids[key] = rel
            for node in old_nodes:
                if node['id'] not in new_ids:
                    absent.append(dict(file=rel, **node))
            for node in new_nodes:
                if node['id'] not in old_ids:
                    added.append(dict(file=rel, **node))
            files.append(dict(file=rel, old=len(old_ids), retained=len(old_ids & new_ids), lost=len(old_ids - new_ids),
                              new=len(new_ids - old_ids), control_signature_equal=a == b))
    frozen = None
    if 'day03' in groups:
        a, b = old_source / FROZEN, new_source / FROZEN
        ca, cb = old_compiled / Path(FROZEN).with_suffix('.rpyc'), new_compiled / Path(FROZEN).with_suffix('.rpyc')
        source_equal = a.read_bytes() == b.read_bytes()
        old_nodes, new_nodes = ast_nodes(ca), ast_nodes(cb)
        # Location fields may differ in otherwise identical serialized caches.
        canonical = lambda ns: [(n['id'], n['kind'], n['who'], n['what']) for n in ns]
        ast_equal = canonical(old_nodes) == canonical(new_nodes)
        frozen = dict(source_byte_identity=source_equal, statement_identity=ast_equal,
                      compiled_byte_identity=ca.read_bytes() == cb.read_bytes())
        if not source_equal or not ast_equal:
            errors.append('Protected day3 scene95 changed')
    return dict(status='FAIL' if errors else 'PASS', groups=list(groups), files=files,
                totals={key: sum(f[key] for f in files) for key in ('old', 'retained', 'lost', 'new')},
                absent_by_kind=dict(Counter(n['kind'] for n in absent)), absent_ids=absent, new_ids=added,
                protected95=frozen, errors=errors,
                scope='Static data-only audit. Lost Say IDs require native old-save rollback tests; ID loss alone is not a load failure.')


def main():
    p = argparse.ArgumentParser(__doc__)
    p.add_argument('before'); p.add_argument('after')
    p.add_argument('--groups', nargs='+', choices=GROUPS, default=list(GROUPS))
    p.add_argument('--before-source'); p.add_argument('--after-source'); p.add_argument('--output')
    a = p.parse_args()
    result = audit(a.before, a.after, a.groups, a.before_source, a.after_source)
    if a.output:
        Path(a.output).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('absent_ids', 'new_ids', 'files')}, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))


if __name__ == '__main__':
    main()
