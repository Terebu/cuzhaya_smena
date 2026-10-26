from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1])
old=Path('D:/stean/release_chuzaya_smena/day03_part10_20261025_final')
suffix=Path('validation/steamapps/common/Everlasting Summer')
for release in (old,stage):
    for name in ('day03_part06_test','day03_part11_test','day03_part11_cross_save'):
        shutil.copy2(R/('tools/'+name+'.rpy.txt'),release/suffix/('game/cs_release_checks/'+name+'.rpy'))
engine_run(old/suffix,['test','cs_p11_make_old'],stage/'p11_cross_old.log')
assert (old/suffix/'p11_old_save_PASS.txt').is_file()
saves=list((old/suffix/'isolated_saves').glob('*p11_old_pending*'));assert saves
for p in saves:shutil.copy2(p,stage/suffix/'isolated_saves'/p.name)
for p in (stage/suffix).glob('p6_p11_cross_*.png'):
    assert p.resolve().parent==(stage/suffix).resolve();p.unlink()
engine_run(stage/suffix,['test','cs_p11_load_old'],stage/'p11_cross_new.log',timeout=200)
assert (stage/suffix/'p11_cross_save_PASS.txt').is_file()
shutil.copy2(old/suffix/'p11_old_pending.png',stage/suffix/'p6_p11_cross_old_pending.png')
(stage/'part11_cross_save_result.json').write_text(json.dumps(dict(status='PASS',old=str(old),scope='Actual previous-release modal save -> part11, with no replay of reading/drawing/library and preserved inventory/invitations.'),indent=2),encoding='utf8')
print('PART11_CROSS_SAVE_PASS')

