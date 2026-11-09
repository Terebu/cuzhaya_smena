from pathlib import Path
import sys,subprocess,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent; stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
subprocess.run([sys.executable,str(R/'tools/run_day05_qa.py'),str(stage)],check=True,cwd=R)
for fixture in ('day05_visual','day05_compat'):
 shutil.copy2(R/('tools/'+fixture+'.rpy.txt'),engine/('game/cs_release_checks/'+fixture+'.rpy'))
engine_run(engine,['test','cs_day05_visual'],stage/'day05_visual.log',timeout=240)
assert (engine/'day05_visual_PASS.txt').is_file()
old=Path('Q:/release_20261102/validation/steamapps/common/Everlasting Summer/isolated_saves')
for p in old.glob('*d5_old_wait*'):shutil.copy2(p,engine/'isolated_saves'/p.name)
engine_run(engine,['test','cs_d5_load_old'],stage/'day05_old_load.log',timeout=180)
assert (engine/'day05_old_save_PASS.txt').is_file()
engine_run(engine,['test','cs_release_smoke'],stage/'day05_final_smoke.log')
engine_run(engine,['lint'],stage/'day05_lint.log')
(stage/'DAY05_CHECKS_PASS.json').write_text(json.dumps(dict(native_routes=12,save_load=True,old_wait_save=True,visual=True,smoke=True,lint_exit=0),indent=2),encoding='utf-8')
print('DAY05_FINAL_CHECKS_PASS',flush=True)
