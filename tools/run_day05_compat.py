from pathlib import Path
import sys,shutil
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
old=Path('Q:/release_20261102/validation/steamapps/common/Everlasting Summer')
new=Path(sys.argv[1])/'validation/steamapps/common/Everlasting Summer'
for engine in (old,new):
 p=engine/'game/cs_release_checks/day05_compat.rpy';p.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(R/'tools/day05_compat.rpy.txt',p)
engine_run(old,['test','cs_d5_create_old'],new/'day05_old_create.log',timeout=180)
for p in (old/'isolated_saves').glob('*d5_old_wait*'):
 shutil.copy2(p,new/'isolated_saves'/p.name)
engine_run(new,['test','cs_d5_load_old'],new/'day05_old_load.log',timeout=180)
assert (new/'day05_old_save_PASS.txt').is_file()
print('DAY05_OLD_WAIT_SAVE_PASS',flush=True)
