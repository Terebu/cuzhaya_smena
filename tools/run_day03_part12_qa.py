from pathlib import Path
import sys,shutil,json
from build_release import engine_run
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for name in ('day03_part06_test','day03_part12_test'):
 shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
dest=stage/'part12_native_results.json';results=json.loads(dest.read_text()) if dest.exists() else []
for case in sys.argv[2:] or [str(i) for i in range(18)]+['guard']:
 print('Native part12:',case,flush=True)
 marker=engine/('p12_'+case+'_PASS.txt')
 if marker.exists():marker.unlink()
 for p in engine.glob('p6_p12_'+case+'_*.png'):
  assert p.resolve().parent==engine.resolve();p.unlink()
 engine_run(engine,['test','cs_p12_'+case],stage/('part12_'+case+'.log'),timeout=220)
 assert marker.exists(),case
 results=[r for r in results if r['case']!=case]+[dict(case=case,status='PASS')]
 dest.write_text(json.dumps(results,indent=2),encoding='utf8')
print('PART12_NATIVE_PASS')
