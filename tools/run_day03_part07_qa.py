from pathlib import Path
import sys,json,shutil
from build_release import engine_run
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent;rel=Path(sys.argv[1]);engine=rel/'validation/steamapps/common/Everlasting Summer'
work=rel/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 target=work/p.relative_to(R);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_bytes(p.read_bytes())
for name in ('day03_part06_test','day03_part07_test'):
 shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
result_path=rel/'part07_native_results.json'
results=json.loads(result_path.read_text()) if result_path.exists() else []
for name in (sys.argv[2:] or ['attention','0','1','2','3','4','camera','guard']):
 print('Native part7:',name,flush=True)
 marker=engine/('p7_'+name+'_PASS.txt')
 if marker.exists():marker.unlink()
 engine_run(engine,['test','cs_day03_p7_'+name],rel/('p7_'+name+'.log'),timeout=300)
 assert marker.is_file(),name
 results=[x for x in results if x['case']!=name]+[dict(case=name,status='PASS')]
 result_path.write_text(json.dumps(results,indent=2),encoding='utf8')
print('PART07_NATIVE_PASS',flush=True)
