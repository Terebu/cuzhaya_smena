from pathlib import Path
from build_release import engine_run,build
stage=Path('D:/stean/release_chuzaya_smena/day03_part07_revision_20261024')
engine_run(stage/'validation/steamapps/common/Everlasting Summer',['lint'],stage/'lint.log')
build(str(stage)+'_final')
print('LUNCH_RELEASE_TAIL_PASS',flush=True)
