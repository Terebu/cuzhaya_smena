"""Load the last published Day 5 edition using its actual dialogue anchors."""
from pathlib import Path
import json,os,shutil,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);new=stage/'validation/steamapps/common/Everlasting Summer'
old=Path('Q:/day05_corrected_20261106/validation/steamapps/common/Everlasting Summer')
text=(R/'tools/day05_corrected_saves.rpy.txt').read_text(encoding='utf-8')
text=text.replace('Мне опять снился автобус.','Мне сегодня сон приснился. Про автобус.')
text=text.replace('И впервые за весь день даже не попыталась пошутить.','А мы продолжали писать.')
text=text.replace('literary_previous_','global_day5_previous_').replace('literary_old_','global_day5_old_')
for e in (old,new):
    (e/'game/cs_release_checks/day05_corrected_saves.rpy').write_text(text,encoding='utf-8')
    shutil.copy2(R/'tools/day05_corrected_clicks.rpy.txt',e/'game/cs_release_checks/day05_corrected_clicks.rpy')
for p in (old/'game/cs_release_checks').glob('*.rpy'):
    target=new/'game/cs_release_checks'/p.name
    if not target.exists():shutil.copy2(p,target)
for case in ('awake','mid','final'):
    os.environ['CS_LIT_SAVE_CASE']=case
    engine_run(old,['test','cs_lit_save_previous'],stage/('day5_legacy_create_'+case+'.log'),timeout=240)
    for p in (old/'isolated_saves').glob('*global_day5_previous_'+case+'*'):shutil.copy2(p,new/'isolated_saves'/p.name)
    engine_run(new,['test','cs_lit_load_previous'],stage/('day5_legacy_load_'+case+'.log'),timeout=180)
    assert (new/('global_day5_old_'+case+'_PASS.txt')).is_file()
    print('GLOBAL_DAY5_LEGACY_PASS',case,flush=True)
(stage/'GLOBAL_DAY5_LEGACY_PASS.json').write_text(json.dumps(dict(status='PASS',previous_edition_saves=3),indent=2),encoding='utf-8')
