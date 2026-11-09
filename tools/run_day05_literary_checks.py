from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
    q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
shutil.copy2(R/'tools/day05_literary_test.rpy.txt',engine/'game/cs_release_checks/day05_test.rpy')
engine_run(engine,['test','cs_day05_matrix'],stage/'day05_matrix.log',timeout=1200)
result=json.loads((engine/'day05_matrix_PASS.json').read_text())
assert len(result)==16 and len({x['route'] for x in result})==16
print('LITERARY_MATRIX_PASS',len(result),flush=True)
shutil.copy2(R/'tools/day05_compat.rpy.txt',engine/'game/cs_release_checks/day05_compat.rpy')
old=Path('Q:/release_20261102/validation/steamapps/common/Everlasting Summer/isolated_saves')
for p in old.glob('*d5_old_wait*'):shutil.copy2(p,engine/'isolated_saves'/p.name)
engine_run(engine,['test','cs_d5_load_old'],stage/'day05_old_load.log',timeout=180)
assert (engine/'day05_old_save_PASS.txt').is_file()
engine_run(engine,['test','cs_release_smoke'],stage/'day05_final_smoke.log')
engine_run(engine,['lint'],stage/'day05_lint.log')
(stage/'DAY05_CHECKS_PASS.json').write_text(json.dumps(dict(native_routes=16,save_load=True,old_wait_save=True,smoke=True,lint_exit=0),indent=2),encoding='utf-8')
print('LITERARY_FINAL_CHECKS_PASS',flush=True)
