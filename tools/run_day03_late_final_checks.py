from pathlib import Path
import subprocess,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part08_09_20261025')
def run(name,*args):subprocess.run([sys.executable,str(R/'tools'/name)]+list(map(str,args)),cwd=R,check=True)
if '--tail' not in sys.argv:
    run('verify_day03_part08_09.py')
    run('run_day03_late_qa.py',stage,'0','1')
    run('run_day03_late_cross_save.py','D:/stean/release_chuzaya_smena/day03_part07_revision_20261024_final',stage)
run('run_full_render_walkthrough_qa.py',stage)
run('run_medpoint_revision_qa.py',stage,'camera')
run('run_day03_part07_qa.py',stage,'attention','camera')
engine_run(stage/'validation/steamapps/common/Everlasting Summer',['lint'],stage/'lint.log')
run('build_release.py',str(stage)+'_final')
print('DAY03_LATE_FINAL_CHECKS_PASS',flush=True)
