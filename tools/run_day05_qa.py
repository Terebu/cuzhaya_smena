from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]); engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
fixture=engine/'game/cs_release_checks/day05_test.rpy'; fixture.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(R/'tools/day05_test.rpy.txt',fixture)
engine_run(engine,['test','cs_day05_matrix'],stage/'day05_matrix.log',timeout=1200)
result=json.loads((engine/'day05_matrix_PASS.json').read_text())
assert len(result)==12 and len({x['route'] for x in result})==12
print('DAY05_MATRIX_PASS',len(result),'full routes',flush=True)
