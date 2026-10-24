"""Final native checks use one engine at a time and isolated save directories."""
from pathlib import Path
import sys,subprocess
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part07_revision_20261024')
def run(name,*args):
    subprocess.run([sys.executable,str(R/'tools'/name)]+list(map(str,args)),cwd=R,check=True)
run('verify_lunch_revision.py')
run('run_lunch_revision_qa.py',stage)
run('run_full_render_walkthrough_qa.py',stage)
run('run_medpoint_revision_qa.py',stage,'camera')
run('run_day03_part07_qa.py',stage,'attention','camera')
run('run_day03_part06_qa.py',stage,'costume')
run('run_lunch_cross_save.py','D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024_final',stage)
engine_run(stage/'validation/steamapps/common/Everlasting Summer',['lint'],stage/'lint.log')
run('build_release.py',str(stage)+'_final')
print('LUNCH_FINAL_CHECKS_PASS',flush=True)
