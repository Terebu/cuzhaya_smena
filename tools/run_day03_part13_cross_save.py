from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1]);suffix=Path('validation/steamapps/common/Everlasting Summer');engine=stage/suffix
old=Path('D:/stean/release_chuzaya_smena/day03_part12_20261025')/suffix
# These genuine automated saves serialize QA callback functions by name.
# Preserve their original QA environment, never add helpers to mod runtime.
for p in (old/'game/cs_release_checks').glob('*.rpy'):
 shutil.copy2(p,engine/'game/cs_release_checks'/p.name)
shutil.copy2(R/'tools/day03_part13_cross_save.rpy.txt',engine/'game/cs_release_checks/day03_part13_cross_save.rpy')
results=[]
for case in (0,12,15):
 print('Native actual part12 save:',case,flush=True)
 saves=list((old/'isolated_saves').glob('p12_'+str(case)+'_end*'));assert saves
 for p in saves:shutil.copy2(p,engine/'isolated_saves'/p.name)
 marker=engine/('p13_cross_'+str(case)+'_PASS.txt')
 if marker.exists():marker.unlink()
 for p in engine.glob('p6_p13_cross_'+str(case)+'_*.png'):
  assert p.resolve().parent==engine.resolve();p.unlink()
 engine_run(engine,['test','cs_p13_cross_'+str(case)],stage/('p13_cross_'+str(case)+'.log'),timeout=220)
 assert marker.exists(),case
 results.append(dict(case=case,status='PASS',previous='day03_part12_20261025',save=saves[0].name))
 (stage/'part13_cross_save_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('PART13_CROSS_SAVE_PASS')
