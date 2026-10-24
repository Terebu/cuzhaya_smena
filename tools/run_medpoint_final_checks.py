from pathlib import Path
import subprocess,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024')
def run(name,*args):subprocess.run([sys.executable,str(R/'tools'/name)]+list(map(str,args)),check=True,cwd=R)
run('build_medpoint_revision_qa.py')
run('run_medpoint_revision_qa.py',stage,*[str(i) for i in range(10)],'camera','guard')
run('run_medpoint_revision_qa.py',stage,'legacy')
run('run_full_render_walkthrough_qa.py',stage)
run('run_day03_part07_qa.py',stage,'attention','camera','guard')
run('run_day03_part06_qa.py',stage,'costume')
run('run_medpoint_cross_save.py','D:/stean/release_chuzaya_smena/day03_part07_20261024_final',stage)
run('run_day03_part07_cross_save.py','D:/stean/release_chuzaya_smena/day03_part06_20261023_final',stage)
engine_run(stage/'validation/steamapps/common/Everlasting Summer',['lint'],stage/'lint.log')
run('build_release.py','D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024_final')
print('REVISION_FINAL_NATIVE_AND_BUILD_PASS',flush=True)
