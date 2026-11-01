from pathlib import Path
import sys,shutil,json
from build_release import engine_run
from validate_release import NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for name in ('day03_part06_test','day04_test'):
 shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
results=[]
for case in sys.argv[2:] or ['0','1','2','3']:
 print('Native day04 matrix:',case,flush=True)
 for p in engine.glob('p6_day04_matrix_'+case+'_*.png'):
  assert p.resolve().parent==engine.resolve();p.unlink()
 engine_run(engine,['test','cs_day04_matrix_'+case],stage/('day04_matrix_'+case+'.log'),timeout=600)
 assert (engine/('day04_matrix_'+case+'_PASS.txt')).exists()
 results.append(dict(case=case,status='PASS'))
 (stage/'day04_native_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('DAY04_MATRIX_PASS',flush=True)
