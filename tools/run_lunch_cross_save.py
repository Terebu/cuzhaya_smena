from pathlib import Path
import shutil,sys,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
old=Path(sys.argv[1]);new=Path(sys.argv[2]);suffix=Path('validation/steamapps/common/Everlasting Summer')
for folder in (old,new):
    for name in ('lunch_revision_cross_save','day03_part06_test'):
        shutil.copy2(R/('tools/'+name+'.rpy.txt'),folder/suffix/('game/cs_release_checks/'+name+'.rpy'))
engine_run(old/suffix,['test','cs_lunch_old_save'],new/'lunch_cross_old.log',timeout=300)
assert (old/suffix/'lunch_old_save_PASS.txt').is_file()
saves=list((old/suffix/'isolated_saves').glob('*lunch_old_menu*'));assert saves
for src in saves:shutil.copy2(src,new/suffix/'isolated_saves'/src.name)
engine_run(new/suffix,['test','cs_lunch_new_load'],new/'lunch_cross_new.log',timeout=400)
assert (new/suffix/'lunch_new_load_PASS.txt').is_file()
(new/'lunch_cross_save_result.json').write_text(json.dumps(dict(status='PASS',old=str(old),new=str(new),files=[s.name for s in saves]),indent=2),encoding='utf8')
print('REAL_OLD_LUNCH_MENU_SAVE_PASS')
