from pathlib import Path
import subprocess,sys,json,hashlib,textwrap,re,shutil
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
def run(name,*args):subprocess.run([sys.executable,str(R/'tools'/name)]+list(map(str,args)),cwd=R,check=True)
def identity():return {p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))}
before=identity();run('build_day04.py');assert identity()==before,'Day04 generator changed frozen sources'
(stage/'day04_generator_identity.json').write_text(json.dumps(dict(status='PASS',sources=before),indent=2),encoding='utf8')
s=(R/'day03_location_audio.rpy').read_text(encoding='utf8');a=s.index('    def cs_day03_audio_target(');b=s.index('    def cs_day03_location_audio(',a)
space={};exec(textwrap.dedent(s[a:b]),space);target=space['cs_day03_audio_target'];rooms={}
for p in (R/'days/day04').glob('*.rpy'):
 for im in re.findall(r'cs_director_scene\("([^"]+)"\)',p.read_text(encoding='utf8')):
  sound=target(im);assert sound is not False or im.startswith('cs_cg_'),im;rooms[im]=sound
(stage/'day04_audio_audit.json').write_text(json.dumps(dict(status='PASS',rooms=rooms),indent=2),encoding='utf8')
work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
run('run_day04_qa.py',stage)
if not (stage/'day04_cross_save_results.json').exists():
 run('run_day04_cross_save.py',stage)
run('run_full_render_walkthrough_qa.py',stage)
engine_run(engine,['lint'],stage/'lint.log')
assert identity()==before,'Sources changed while testing'
run('build_release.py',str(stage)+'_final')
for prefix in ('p6_render_reviewed_high_','p6_render_reviewed_low_')+tuple('p6_day04_matrix_'+str(i)+'_' for i in range(4)):
 run('build_qa_contact_sheets.py',engine,prefix,'64')
 # Remove obsolete sheets from the earlier exploratory capture, by exact names.
 folder=engine/(prefix.rstrip('_')+'_contacts');keep={v['sheet'] for v in json.loads((folder/'index.json').read_text())}
 for p in folder.glob('*.png'):
  if p.name not in keep:
   assert p.resolve().parent==folder.resolve();p.unlink()
print('DAY04_FINAL_CHECKS_PASS',flush=True)
