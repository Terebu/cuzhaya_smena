from pathlib import Path
import shutil,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
old=Path('Q:/day05_final_20261105/validation/steamapps/common/Everlasting Summer')
new=Path(sys.argv[1])/'validation/steamapps/common/Everlasting Summer'
for engine in (old,new):shutil.copy2(R/'tools/day05_expanded_save.rpy.txt',engine/'game/cs_release_checks/day05_expanded_save.rpy')
for case in ('awake','sport'):
 engine_run(old,['test','cs_d5_probe_create_'+case],new/('expanded_create_'+case+'.log'),timeout=120)
 for p in (old/'isolated_saves').glob('*d5_pre_expanded_'+case+'*'):shutil.copy2(p,new/'isolated_saves'/p.name)
 engine_run(new,['test','cs_d5_probe_load_'+case],new/('expanded_load_'+case+'.log'),timeout=120)
 assert (new/('expanded_old_'+case+'_PASS.txt')).is_file()
 print('PRE_EXPANDED_SAVE_PASS',case,flush=True)
