from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;old=Path(sys.argv[1]);new=Path(sys.argv[2]);suffix=Path('validation/steamapps/common/Everlasting Summer')
for release in (old,new):shutil.copy2(R/'tools/day03_part05_cross_save.rpy.txt',release/suffix/'game/cs_release_checks/day03_part05_cross_save.rpy')
print('Creating previous-build save',flush=True)
engine_run(old/suffix,['test','cs_p5_make_old_save'],new/'cross_save_old.log')
assert (old/suffix/'p5_old_save_PASS.txt').is_file()
saved=list((old/suffix/'isolated_saves').glob('*p5_cross_version*'));assert saved
for p in saved:shutil.copy2(p,new/suffix/'isolated_saves'/p.name)
print('Loading previous-build save',flush=True)
engine_run(new/suffix,['test','cs_p5_load_old_save'],new/'cross_save_new.log')
assert (new/suffix/'p5_cross_save_PASS.txt').is_file()
(new/'cross_save_result.json').write_text(json.dumps(dict(status='PASS',old_build=str(old),new_build=str(new),save_files=[p.name for p in saved],scope='Old part4 waiting screen -> new errands; defaults, poster, injury, inventory and library appointment retained.'),indent=2),encoding='utf8')
print('CROSS_VERSION_SAVE_PASS',flush=True)
