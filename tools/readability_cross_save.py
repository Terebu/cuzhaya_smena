"""Create genuine pre-edit saves and load them in an isolated edited build.

Examples (root invokes inside its temporary Q: mapping):
  python tools/readability_cross_save.py Q:/b0 --mode prepare
  python tools/readability_cross_save.py Q:/b0 --mode create --groups prologue day01
  python tools/readability_cross_save.py Q:/p1 --mode load --groups prologue day01

The fixture never uses interact=False: every preceding Say is clicked normally.
Only QA files, isolated saves and QA evidence are written. Product packages are
hashed before/after each run. Baseline and edited phases share the SAME fixture.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import shutil
import sys
import textwrap

from readability_ast_audit import ast_nodes, compiled_root

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'source/readability_save_cases.json'
FIXTURE = ROOT / 'tools/readability_cross_save.rpy.txt'
GROUPS = ('prologue', 'day01', 'day02', 'day03', 'day04')
SUFFIX = Path('validation/steamapps/common/Everlasting Summer')
STATE_FIELDS = [
    'cs_readability_probe_sentinel', 'cs_active', 'cs_darya_known',
    'cs_friend_da', 'cs_friend_mz', 'cs_friend_sl', 'cs_friend_un', 'cs_friend_mi',
    'cs_friend_dv', 'cs_friend_se', 'cs_friend_viola',
    'cs_day01_done', 'cs_day02_done', 'cs_day03_started', 'cs_day03_completed', 'cs_day04_started',
    'cs_lena_elbow_injury_day2', 'cs_lena_elbow_bandaged', 'cs_lena_no_sport_day2',
    'cs_day03_hint_album_seen', 'cs_day03_poster_location', 'cs_day03_reading_book_location',
    'cs_day03_lunch_horn_played', 'cs_day03_lunch_arrived',
    'cs_da_shared_bed_day3', 'cs_da_love_confession_day3',
    'cs_d4_choice_01_done', 'cs_d4_left_note', 'cs_d4_first_photo_seen', 'save_name',
]

# A line is supplied only to disambiguate repeated identical source remarks.
SPECS = [
    ('prologue_removed', 'prologue', 'days/prologue/03_stranger.rpy', 'cs_scene_03', 'cs_narrator', 'Очень красные.', 31, 'deleted'),
    ('prologue_surviving', 'prologue', 'days/prologue/03_stranger.rpy', 'cs_scene_03', 'cs_narrator', 'Она сидела со стороны прохода, чуть откинувшись на спинку кресла.', 37, 'surviving'),
    ('day01_removed', 'day01', 'days/day01/02_recognition.rpy', 'cs_day01_02', 'cs_narrator', 'Музыка.', 83, 'deleted'),
    ('day01_surviving', 'day01', 'days/day01/02_recognition.rpy', 'cs_day01_02', 'cs_ls', 'К сожалению, значительно лучше, чем хотелось бы.', 171, 'surviving'),
    ('day02_removed', 'day02', 'days/day02/part01/07_scene.rpy', 'cs_day02_07', 'cs_narrator', 'Я замолчала.', 125, 'deleted'),
    ('day02_surviving', 'day02', 'days/day02/part01/07_scene.rpy', 'cs_day02_07', 'cs_ls', 'Семён предложил сходить к воротам вместе после завтрака.', 163, 'surviving'),
    ('day03_removed', 'day03', 'days/day03/part06/120_scene.rpy', 'cs_day03_120', 'cs_narrator', 'Я задумалась.', 33, 'deleted'),
    ('day03_surviving', 'day03', 'days/day03/part06/120_scene.rpy', 'cs_day03_120', 'cs_da', 'После долгого перерыва приятно снова привыкать к клавишам.', 53, 'surviving'),
    ('day04_removed', 'day04', 'days/day04/01_scene.rpy', 'cs_day04_01', 'cs_narrator', 'Я перечитала написанное.', 102, 'deleted'),
    ('day04_surviving', 'day04', 'days/day04/01_scene.rpy', 'cs_day04_01', 'cs_ls', 'Так. Напоминаю себе, что в оригинальной истории здесь было слишком много мистики.', 163, 'surviving'),
    ('day03_frozen95', 'day03', 'days/day03/part03/95_scene.rpy', 'cs_day03_95', 'cs_narrator', 'Она направилась к библиотеке.', 29, 'protected'),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stage_and_engine(path):
    path = Path(path)
    if (path / 'lib/windows-x86_64/python.exe').is_file():
        return path.parents[3], path
    engine = path / SUFFIX
    if not (engine / 'lib/windows-x86_64/python.exe').is_file():
        raise ValueError('Not an isolated editorial build or engine: ' + str(path))
    return path, engine


def seed_for(group):
    day = 0 if group == 'prologue' else int(group[-2:])
    return dict(cs_active=True, cs_darya_known=day > 0, cs_slavya_known=day > 0,
                cs_olga_seen=day > 0, cs_friend_da=2, cs_friend_mz=3, cs_friend_sl=2,
                cs_friend_un=1, cs_friend_mi=1, cs_friend_dv=2, cs_friend_se=1, cs_friend_viola=1,
                cs_day01_done=day >= 2, cs_day02_done=day >= 3, cs_day03_started=day >= 3,
                cs_day03_completed=day >= 4, cs_day04_started=day >= 4,
                cs_lena_elbow_injury_day2=2 if day >= 3 else 0,
                cs_lena_elbow_bandaged=day >= 3, cs_lena_no_sport_day2=day >= 3,
                cs_day03_hint_album_seen=day >= 3,
                cs_day03_poster_location='house_table' if day >= 3 else None,
                cs_day03_reading_book_location='library' if day >= 3 else None,
                cs_day03_lunch_horn_played=False, cs_day03_lunch_arrived=False,
                cs_da_shared_bed_day3=False, cs_da_love_confession_day3=False,
                cs_d4_choice_01_done=False, cs_d4_left_note=False)


def prepare_manifest(baseline_stage):
    session = json.loads((ROOT / 'source/readability_session.json').read_text(encoding='utf-8'))
    baseline_source = Path(session['baseline'])
    caches = compiled_root(baseline_stage)
    cases = []
    for index, (ident, group, rel, label, who, text, line, expect) in enumerate(SPECS):
        nodes = [n for n in ast_nodes(caches / Path(rel).with_suffix('.rpyc'))
                 if n['kind'] == 'Say' and n['who'] == who and n['what'] == text]
        exact = [n for n in nodes if n['line'] == line]
        if exact:
            nodes = exact
        if len(nodes) != 1:
            raise AssertionError((ident, 'Baseline target must identify one actual Say', nodes))
        node = nodes[0]
        cases.append(dict(id=ident, group=group, file=rel, scene_label=label, who=who, old_text=text,
                          old_source_line=node['line'], old_id=node['id'], expect=expect,
                          slot='readability_' + ident, sentinel=74100 + index,
                          seed=seed_for(group), state_fields=STATE_FIELDS,
                          baseline_source_sha256=sha(baseline_source / rel)))
    result = dict(format=1, fixture_sha256=sha(FIXTURE), cases=cases,
                  baseline_source=str(baseline_source),
                  engine_fallback='renpy/python.py:2157 unfreeze -> rollback(on_load=True); rollback walks prior checkpoints until context.current exists; no migration is added.')
    MANIFEST.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    return result


def fixture_static_check():
    text = FIXTURE.read_text(encoding='utf-8-sig')
    start = text.index('init 98 python:\n') + len('init 98 python:\n')
    end = text.index('\nlabel cs_readability_probe_setup:')
    ast.parse(textwrap.dedent(text[start:end]))
    assert 'interact=False' not in text and 'interact = False' not in text
    assert 'click until run CSReadabilityReady("target")' in text
    assert 'cs_rb_builtin' in text
    assert 'renpy.python.RollbackLog.load_failed = cs_readability_failed' in text
    return True


def identity(stage):
    root = compiled_root(stage)
    return {p.relative_to(root).as_posix(): sha(p) for p in root.rglob('*.rpyc')}


def run(stage, engine, mode, cases, shared, timeout):
    from build_release import engine_run
    before = identity(stage)
    checks = engine / 'game/cs_release_checks'
    checks.mkdir(parents=True, exist_ok=True)
    shutil.copy2(FIXTURE, checks / 'readability_cross_save.rpy')
    shared.mkdir(parents=True, exist_ok=True)
    evidence = stage / 'readability_cross_save'
    evidence.mkdir(exist_ok=True)
    results = []
    for case in cases:
        ident = case['id']
        request = dict(mode=mode, case=case)
        request['fixture_sha256'] = sha(FIXTURE)
        if mode == 'load':
            baseline_json = shared / (ident + '_baseline.json')
            if not baseline_json.is_file():
                raise AssertionError('Create the genuine baseline save first: ' + ident)
            baseline = json.loads(baseline_json.read_text(encoding='utf-8'))
            assert baseline['status'] == 'PASS' and baseline['saved']['node']['id'] == case['old_id']
            assert baseline['fixture_sha256'] == sha(FIXTURE), 'Old save requires its exact original QA fixture'
            request['baseline'] = baseline
            old_saves = list(shared.glob(case['slot'] + '-*.save'))
            assert old_saves, 'Missing old native save: ' + ident
            for old_save in old_saves:
                shutil.copy2(old_save, engine / 'isolated_saves' / old_save.name)
        (engine / 'readability_case_request.json').write_text(json.dumps(request, ensure_ascii=True, indent=2), encoding='utf-8')
        result_path = engine / ('readability_' + ident + '_' + mode + '.json')
        if result_path.exists():
            result_path.unlink()
        print('Native editorial save probe:', mode, ident, flush=True)
        engine_run(engine, ['test', 'cs_readability_' + mode], evidence / (ident + '_' + mode + '.log'), timeout=timeout)
        result = json.loads(result_path.read_text(encoding='utf-8'))
        assert result.get('status') == 'PASS' and not result.get('load_failed'), result
        if mode == 'create':
            assert result['saved']['node']['id'] == case['old_id']
            assert len(result['saved']['genuine_scene_checkpoints']) >= 2
            shutil.copy2(result_path, shared / (ident + '_baseline.json'))
            saves = list((engine / 'isolated_saves').glob(case['slot'] + '-*.save'))
            assert saves, ident
            for save in saves:
                shutil.copy2(save, shared / save.name)
        else:
            assert 'resumed' in result and 'roundtrip' in result
        shutil.copy2(result_path, evidence / result_path.name)
        debug = engine / ('readability_' + ident + '_debug.jsonl')
        if debug.is_file():
            shutil.copy2(debug, evidence / debug.name)
        for screenshot in engine.glob('readability_' + ident + '_*.png'):
            shutil.copy2(screenshot, evidence / screenshot.name)
        results.append(result)
        (evidence / (mode + '_results.json')).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
        assert identity(stage) == before, 'Immutable product RPYC package changed during QA'
    return results


def main():
    p = argparse.ArgumentParser(__doc__)
    p.add_argument('stage')
    p.add_argument('--mode', choices=('prepare', 'create', 'load'), required=True)
    p.add_argument('--groups', nargs='+', choices=GROUPS, default=list(GROUPS))
    p.add_argument('--cases', nargs='+', help='Optional exact case IDs')
    p.add_argument('--baseline-stage')
    p.add_argument('--save-root')
    p.add_argument('--timeout', type=int, default=240)
    a = p.parse_args()
    fixture_static_check()
    stage, engine = stage_and_engine(a.stage)
    baseline_stage = Path(a.baseline_stage) if a.baseline_stage else stage.parent / 'b0'
    if a.mode == 'prepare' or not MANIFEST.is_file():
        manifest = prepare_manifest(baseline_stage)
    else:
        manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    assert manifest['fixture_sha256'] == sha(FIXTURE), 'Fixture changed: regenerate manifest before making new baseline saves'
    cases = [c for c in manifest['cases'] if c['group'] in a.groups and (not a.cases or c['id'] in a.cases)]
    assert cases, 'No matching save cases'
    if a.mode == 'prepare':
        print('PREPARED', len(manifest['cases']), 'baseline Say probes; fixture Python syntax PASS; no native game launched')
        return
    shared = Path(a.save_root) if a.save_root else stage.parent / 'readability_save_evidence'
    results = run(stage, engine, a.mode, cases, shared, a.timeout)
    print('READABILITY_CROSS_SAVE_PASS', a.mode, len(results), flush=True)


if __name__ == '__main__':
    main()
