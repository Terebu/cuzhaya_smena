from pathlib import Path
import sys,shutil,json
from build_release import engine_run
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
    q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for name in ('day03_part06_test','lunch_revision_test'):
    shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
dest=stage/'lunch_revision_results.json'
results=json.loads(dest.read_text()) if dest.exists() else []
for case in (sys.argv[2:] or [str(i) for i in range(8)]+['guard']):
    print('Native lunch:',case,flush=True)
    marker=engine/('lunch_revision_'+case+'_PASS.txt')
    if marker.exists():marker.unlink()
    engine_run(engine,['test','cs_lunch_revision_'+case],stage/('lunch_revision_'+case+'.log'),timeout=400)
    assert marker.is_file(),case
    results=[r for r in results if r['case']!=case]+[dict(case=case,status='PASS')]
    dest.write_text(json.dumps(results,indent=2),encoding='utf8')
print('LUNCH_REVISION_NATIVE_PASS',flush=True)
