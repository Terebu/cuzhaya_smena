"""Load real saves made by the preceding ADV release into the POV revision."""
from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
old=Path('Q:/day05_adv_20261105/validation/steamapps/common/Everlasting Summer')
stage=Path(sys.argv[1]);new=stage/'validation/steamapps/common/Everlasting Summer'
for e in (old,new):
    for name in ('day05_adv_test','day05_adv_save'):
        shutil.copy2(R/('tools/'+name+'.rpy.txt'),e/('game/cs_release_checks/'+name+'.rpy'))
for case in ('awake','mid'):
    engine_run(old,['test','cs_adv_save_'+case],stage/('pov_create_'+case+'.log'),timeout=180)
    for p in (old/'isolated_saves').glob('*adv_previous_'+case+'*'):shutil.copy2(p,new/'isolated_saves'/p.name)
    marker=new/('adv_old_'+case+'_PASS.txt')
    if marker.exists():marker.unlink()
    engine_run(new,['test','cs_adv_load_'+case],stage/('pov_load_'+case+'.log'),timeout=180)
    assert marker.is_file()
    print('PRE_POV_SAVE_PASS',case,flush=True)
engine_run(new,['test','cs_day05_adv_clicks'],stage/'pov_clicks.log',timeout=180)
assert (new/'adv_clicks_PASS.txt').is_file()
(stage/'POV_CHECKS_PASS.json').write_text(json.dumps(dict(old_awake=True,old_mid=True,manual_adv_clicks=6),indent=2),encoding='utf-8')
print('DAY05_POV_CHECKS_PASS',flush=True)
