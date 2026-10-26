from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;old=Path(sys.argv[1]);new=Path(sys.argv[2]);suffix=Path('validation/steamapps/common/Everlasting Summer')
for d in (old,new):
    for name in ('day03_late_cross_save','day03_part06_test'):
        shutil.copy2(R/('tools/'+name+'.rpy.txt'),d/suffix/('game/cs_release_checks/'+name+'.rpy'))
engine_run(old/suffix,['test','cs_late_make_old'],new/'late_cross_old.log')
assert (old/suffix/'late_old_save_PASS.txt').is_file()
saves=list((old/suffix/'isolated_saves').glob('*late_old_wait*'));assert saves
for p in saves:shutil.copy2(p,new/suffix/'isolated_saves'/p.name)
engine_run(new/suffix,['test','cs_late_load_old'],new/'late_cross_new.log',timeout=600)
assert (new/suffix/'late_cross_save_PASS.txt').is_file()
shutil.copy2(old/suffix/'late_old_wait.png',new/suffix/'p6_late_cross_old_wait.png')
(new/'late_cross_save_result.json').write_text(json.dumps(dict(status='PASS',old=str(old),new=str(new),scope='Actual old part7 waiting-screen save, legacy Paustovsky bridge -> novel, loan, square and drawing; no repeated lunch.'),indent=2),encoding='utf8')
print('LATE_REAL_CROSS_VERSION_SAVE_PASS')
