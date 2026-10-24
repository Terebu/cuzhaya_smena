from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;old,new=map(Path,sys.argv[1:3]);suffix=Path('validation/steamapps/common/Everlasting Summer')
for rel in (old,new):shutil.copy2(R/'tools/medpoint_revision_cross_save.rpy.txt',rel/suffix/'game/cs_release_checks/medpoint_revision_cross_save.rpy')
print('Creating actual previous-build Viola menu save',flush=True)
engine_run(old/suffix,['test','cs_revision_make_old_menu'],new/'revision_cross_old.log',timeout=360)
assert (old/suffix/'revision_old_menu_PASS.txt').is_file()
saved=list((old/suffix/'isolated_saves').glob('*revision_previous_menu*'));assert saved
for p in saved:shutil.copy2(p,new/suffix/'isolated_saves'/p.name)
print('Loading old menu into revised medical scene',flush=True)
engine_run(new/suffix,['test','cs_revision_load_old_menu'],new/'revision_cross_new.log',timeout=360)
assert (new/suffix/'revision_cross_save_PASS.txt').is_file()
(new/'revision_cross_save_result.json').write_text(json.dumps(dict(status='PASS',old_build=str(old),new_build=str(new),save_files=[p.name for p in saved]),indent=2),encoding='utf8')
print('REVISION_CROSS_SAVE_PASS',flush=True)
