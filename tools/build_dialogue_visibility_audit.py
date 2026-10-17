"""Build native QA source lookup. This tool never modifies scenario staging."""
from pathlib import Path
import ast
import json
import re

ROOT = Path(__file__).resolve().parent.parent
SPEAKERS = dict(cs_da=['cs_darya', 'cs_dasha_winter'], cs_sy=['cs_semen'],
    cs_sl=['sl'], cs_mt=['mt'], cs_dv=['dv'], cs_us=['us'], cs_sh=['sh'],
    cs_el=['el'], cs_un=['un'], cs_mz=['cs_zhenya'], cs_vi=['cs'], cs_mi=['mi'])
ACTORS = {tag for tags in SPEAKERS.values() for tag in tags}
lookup, candidates, crowded = {}, [], []
for path in sorted((ROOT / 'days').rglob('*.rpy')):
    relative = path.relative_to(ROOT).as_posix()
    statements, visible, cg = {}, set(), False
    for number, raw in enumerate(path.read_text(encoding='utf8').splitlines(), 1):
        line = raw.strip()
        if line.startswith('scene '):
            image = line.split()[1]
            visible = set()
            cg = image.startswith('cs_cg_') or image in ('cs_sleep_winter', 'cs_sleep_summer', 'cs_lena_pioneer_mirror')
        match = re.match(r'\$ cs_frame_focus\((\[.*?\])\)', line)
        if match:
            node = ast.parse(match[1], mode='eval').body
            # Diagnostic union only; the native branch test checks the actual
            # existing friendship condition and each resulting composition.
            choices = (node.body, node.orelse) if isinstance(node, ast.IfExp) else (node,)
            visible = set().union(*(set(ast.literal_eval(choice)) for choice in choices)) if not cg else set()
        match = re.match(r'\$ cs_actor_exit\((\[.*?\])\)', line)
        if match:
            visible -= set(ast.literal_eval(match[1]))
        if line == '$ cs_reflective_focus()':
            visible = set()
        match = re.match(r'(show|hide) (\w+)\b', line)
        if match and match[2] in ACTORS:
            visible.add(match[2]) if match[1] == 'show' else visible.discard(match[2])
        match = re.match(r'(cs_\w+) (".*")$', line)
        if not match:
            continue
        speaker, text = match[1], json.loads(match[2])
        statements[str(number)] = dict(speaker=speaker, text=text)
        if speaker in SPEAKERS and not cg and not set(SPEAKERS[speaker]) & visible:
            candidates.append(dict(file=relative, line=number, speaker=speaker, text=text))
        if len(visible) > 3:
            crowded.append(dict(file=relative, line=number, tags=sorted(visible)))
    if statements:
        lookup[relative] = statements
voices = json.loads((ROOT / 'source/offscreen_dialogue.json').read_text(encoding='utf8'))
unexpected = [row for row in candidates if not any(all(row[k] == voice[k] for k in ('file', 'speaker', 'text')) for voice in voices)]
for name, data in [('dialogue_statement_lookup', lookup), ('dialogue_visibility_audit',
    dict(files=len(lookup), reviewed_voices=voices, unexpected_candidates=unexpected, crowded_candidates=crowded))]:
    (ROOT / 'qa' / (name + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf8')
print('Dialogue audit:', len(lookup), 'files;', len(unexpected), 'unreviewed missing-speaker candidates;', len(crowded), 'crowded candidates')
