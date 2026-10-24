from pathlib import Path
import sys,json,shutil
from build_release import engine_run
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for name in ('day03_part06_test','medpoint_revision_test'):
 shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
result_path=stage/'revision_native_results.json'
results=json.loads(result_path.read_text()) if result_path.exists() else []
for case in (sys.argv[2:] or [str(i) for i in range(10)]+['camera','guard']):
 print('Native revision:',case,flush=True)
 marker=engine/('revision_'+case+'_PASS.txt')
 if marker.exists():marker.unlink()
 engine_run(engine,['test','cs_revision_'+case],stage/('revision_'+case+'.log'),timeout=400)
 assert marker.is_file(),case
 results=[x for x in results if x['case']!=case]+[dict(case=case,status='PASS')]
 (stage/'revision_native_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('MEDPOINT_REVISION_NATIVE_PASS',flush=True)
