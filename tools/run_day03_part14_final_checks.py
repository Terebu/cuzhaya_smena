from pathlib import Path
import subprocess,sys,json,hashlib
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_part14_20261026')
def run(name,*args):subprocess.run([sys.executable,str(R/'tools'/name)]+list(map(str,args)),cwd=R,check=True)
def identity():return {p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))}
before=identity()
run('build_day03_part11.py');run('build_day03_audio_compat.py');run('stabilize_mod_calls.py')
after=identity();assert before==after,[k for k in after if before.get(k)!=after[k]]
(stage/'generator_idempotence.json').write_text(json.dumps(dict(status='PASS',scripts=len(after),sources=after),indent=2),encoding='utf8')
run('verify_day03_part14.py');run('verify_day03_location_audio.py',stage)
run('run_day03_part14_cross_save.py',stage)
run('build_full_render_walkthrough_qa.py');run('run_full_render_walkthrough_qa.py',stage)
engine=stage/'validation/steamapps/common/Everlasting Summer'
engine_run(engine,['lint'],stage/'lint.log')
run('build_release.py',str(stage)+'_final')
for prefix in ('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_p14_'):
 run('build_qa_contact_sheets.py',engine,prefix,'64')
print('PART14_FINAL_CHECKS_PASS',flush=True)
