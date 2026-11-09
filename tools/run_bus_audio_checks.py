from pathlib import Path
import json,shutil,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);e=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
    d=work/p.relative_to(R);d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,d)
for p in list((R/'audio/sfx/bus').glob('*.ogg'))+[R/'audio/ambience/sports_court_day.ogg',R/'audio/stock_sound_credits.txt']:
    d=work.parent/p.relative_to(R);d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,d)
    # Remove the seven temporary base-game fallback files from the first probe.
    fallback=e/'game'/p.relative_to(R)
    if fallback.is_file():fallback.unlink()
shutil.copy2(R/'tools/bus_audio_test.rpy.txt',e/'game/cs_release_checks/bus_audio_test.rpy')
proofs={'cs_bus_audio':'BUS_AUDIO_PASS.json','cs_bus_credits':'BUS_CREDITS_PASS.txt','cs_female_chuckle':'FEMALE_CHUCKLE_PASS.json','cs_sports_court':'SPORTS_COURT_PASS.json','cs_meal_horns':'MEAL_HORNS_PASS.json'}
for profile in (sys.argv[2:] or tuple(proofs)):
    proof={'cs_cabin_audio':'CABIN_AUDIO_PASS.json','cs_prologue_visuals':'PROLOGUE_VISUALS_PASS.json','cs_dialogue_window':'DIALOGUE_WINDOW_PASS.json'}.get(profile) or proofs[profile]
    (e/proof).unlink(missing_ok=True)
    engine_run(e,['test',profile],stage/(profile+'.log'),timeout=180)
    assert (e/proof).is_file()
    print(profile,'PASS',flush=True)
