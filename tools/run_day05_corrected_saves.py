from pathlib import Path
import sys,shutil,json,os
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);new=stage/'validation/steamapps/common/Everlasting Summer'
old=Path('Q:/day05_literary_20261106/validation/steamapps/common/Everlasting Summer')
for e in (old,new):
    for stale in ('day05_literary_saves','day05_literary_clicks'):
        for ext in ('.rpy','.rpyc'):
            p=e/('game/cs_release_checks/'+stale+ext)
            if p.exists():p.unlink()
    for fixture in ('day05_corrected_saves','day05_corrected_clicks'):
        shutil.copy2(R/('tools/'+fixture+'.rpy.txt'),e/('game/cs_release_checks/'+fixture+'.rpy'))
# Saved QA contexts can retain callbacks from earlier, isolated test fixtures.
for p in (old/'game/cs_release_checks').glob('*.rpy'):
    dest=new/'game/cs_release_checks'/p.name
    if not dest.exists():shutil.copy2(p,dest)
for case in ('awake','mid','final'):
    os.environ['CS_LIT_SAVE_CASE']=case
    if (new/('literary_old_'+case+'_PASS.txt')).is_file():
        print('PREVIOUS_LITERARY_SAVE_ALREADY_PASS',case,flush=True)
        continue
    if not list((new/'isolated_saves').glob('*literary_previous_'+case+'*')):
        engine_run(old,['test','cs_lit_save_previous'],stage/('literary_create_'+case+'.log'),timeout=240)
        for p in (old/'isolated_saves').glob('*literary_previous_'+case+'*'):shutil.copy2(p,new/'isolated_saves'/p.name)
    engine_run(new,['test','cs_lit_load_previous'],stage/('literary_load_'+case+'.log'),timeout=180)
    assert (new/('literary_old_'+case+'_PASS.txt')).is_file()
    print('PREVIOUS_LITERARY_SAVE_PASS',case,flush=True)
engine_run(new,['test','cs_literary_clicks'],stage/'literary_clicks.log',timeout=120)
assert (new/'literary_clicks_PASS.txt').is_file()
(stage/'CORRECTED_SAVES_PASS.json').write_text(json.dumps(dict(previous_literary_saves=3,manual_adv_windows=7),indent=2),encoding='utf-8')
print('LITERARY_SAVE_CHECKS_PASS',flush=True)
