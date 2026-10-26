from pathlib import Path
import subprocess,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part10_20261025')
def run(name,*args):subprocess.run([sys.executable,str(R/'tools'/name)]+list(map(str,args)),cwd=R,check=True)
if '--tail' not in sys.argv:
    run('build_day03_part10.py')
    run('stabilize_mod_calls.py')
    run('verify_day03_part10.py')
    run('build_day03_part10_qa.py')
    run('run_day03_part10_qa.py',stage)
    run('run_day03_part10_cross_save.py',stage)
run('run_full_render_walkthrough_qa.py',stage)
run('run_medpoint_revision_qa.py',stage,'camera')
run('run_day03_part07_qa.py',stage,'attention','camera')
engine_run(stage/'validation/steamapps/common/Everlasting Summer',['lint'],stage/'lint.log')
run('build_release.py',str(stage)+'_final')
print('PART10_FINAL_CHECKS_PASS',flush=True)
