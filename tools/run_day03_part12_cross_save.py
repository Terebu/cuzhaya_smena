from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1])
old=Path('D:/stean/release_chuzaya_smena/day03_part11_20261025_final')
suffix=Path('validation/steamapps/common/Everlasting Summer')
for release in (old,stage):
 for name in ('day03_part06_test','day03_part12_test','day03_part12_cross_save'):
  shutil.copy2(R/('tools/'+name+'.rpy.txt'),release/suffix/('game/cs_release_checks/'+name+'.rpy'))
dest=stage/'part12_cross_save_results.json'
results=json.loads(dest.read_text()) if dest.exists() else []
for kind in sys.argv[2:] or ('help','nohelp','work','audio'):
 print('Native old-save migration:',kind,flush=True)
 engine_run(old/suffix,['test','cs_p12_make_'+kind],stage/('p12_cross_old_'+kind+'.log'),timeout=200)
 saves=list((old/suffix/'isolated_saves').glob('*p12_old_'+kind+'*'));assert saves,kind
 for p in saves:shutil.copy2(p,stage/suffix/'isolated_saves'/p.name)
 marker=stage/suffix/('p12_cross_'+kind+'_PASS.txt')
 if marker.exists():marker.unlink()
 for p in (stage/suffix).glob('p6_p12_cross_'+kind+'*.png'):
  assert p.resolve().parent==(stage/suffix).resolve();p.unlink()
 engine_run(stage/suffix,['test','cs_p12_load_'+kind],stage/('p12_cross_new_'+kind+'.log'),timeout=220)
 assert marker.is_file(),kind
 shutil.copy2(old/suffix/('p12_old_'+kind+'.png'),stage/suffix/('p6_p12_cross_'+kind+'_old.png'))
 results=[r for r in results if r['case']!=kind]+[dict(case=kind,status='PASS')]
 dest.write_text(json.dumps(results,indent=2),encoding='utf8')
print('PART12_CROSS_SAVE_PASS')
