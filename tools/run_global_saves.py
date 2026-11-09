from pathlib import Path
import json,os,shutil,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1])
new=stage/'validation/steamapps/common/Everlasting Summer'
old=Path('Q:/day05_corrected_20261106/validation/steamapps/common/Everlasting Summer')
for e in (old,new):
    shutil.copy2(R/'tools/global_revision_saves.rpy.txt',e/'game/cs_release_checks/global_revision_saves.rpy')
# Define every old serialized test callback in the receiving test environment.
for p in (old/'game/cs_release_checks').glob('*.rpy'):
    target=new/'game/cs_release_checks'/p.name
    if not target.exists():shutil.copy2(p,target)
cases=('day1','injury','interlude','frozen95','day4')
for case in cases:
    os.environ['CS_LEGACY_CASE']=case
    if not list((old/'isolated_saves').glob('*global_legacy_'+case+'*')):
        engine_run(old,['test','cs_global_create_legacy'],stage/('legacy_create_'+case+'.log'),timeout=120)
    for p in (old/'isolated_saves').glob('*global_legacy_'+case+'*'):shutil.copy2(p,new/'isolated_saves'/p.name)
    engine_run(new,['test','cs_global_load_legacy'],stage/('legacy_load_'+case+'.log'),timeout=120)
    assert (new/('legacy_'+case+'_PASS.txt')).is_file()
    print('GLOBAL_LEGACY_PASS',case,flush=True)
(stage/'GLOBAL_LEGACY_PASS.json').write_text(json.dumps(dict(status='PASS',cases=cases),indent=2),encoding='utf-8')
