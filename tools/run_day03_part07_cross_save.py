from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;old=Path(sys.argv[1]);new=Path(sys.argv[2]);suffix=Path('validation/steamapps/common/Everlasting Summer')
for rel in (old,new):shutil.copy2(R/'tools/day03_part07_cross_save.rpy.txt',rel/suffix/'game/cs_release_checks/day03_part07_cross_save.rpy')
print('Creating actual part6-build save',flush=True)
engine_run(old/suffix,['test','cs_p7_make_old_save'],new/'p7_cross_save_old.log')
assert (old/suffix/'p7_old_save_PASS.txt').is_file()
saved=list((old/suffix/'isolated_saves').glob('*p7_cross_version*'));assert saved
for p in saved:shutil.copy2(p,new/suffix/'isolated_saves'/p.name)
print('Loading part6 save into part7',flush=True)
engine_run(new/suffix,['test','cs_p7_load_old_save'],new/'p7_cross_save_new.log',timeout=480)
assert (new/suffix/'p7_cross_save_PASS.txt').is_file()
(new/'p7_cross_save_result.json').write_text(json.dumps(dict(status='PASS',old_build=str(old),new_build=str(new),save_files=[p.name for p in saved],scope='Actual part6 waiting-screen save -> part7 lunch choice and library; poster, injury, documents, friendship retained.'),indent=2),encoding='utf8')
print('PART07_CROSS_VERSION_SAVE_PASS',flush=True)
