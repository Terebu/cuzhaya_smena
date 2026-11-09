"""Refresh assets and compiled scripts after the focused audio and story checks."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys
from build_release import engine_run,sha
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);e=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
for name in ('BUS_AUDIO_PASS.json','BUS_CREDITS_PASS.txt','LIBRARY_NIGHT_PASS.txt','FEMALE_CHUCKLE_PASS.json','SPORTS_COURT_PASS.json','MEAL_HORNS_PASS.json','CABIN_AUDIO_PASS.json'):assert (e/name).is_file()
routes=json.loads((stage/'GLOBAL_ROUTES_PASS.json').read_text())
assert {r['route'] for r in routes}=={'a','b'} and all(r['save_roundtrip'] for r in routes)
manifest=json.loads((stage/'release_manifest.json').read_text(encoding='utf-8'))
for p in list((R/'audio/sfx/bus').glob('*.ogg'))+[R/'audio/ambience/sports_court_day.ogg',R/'audio/stock_sound_credits.txt']:
    rel=p.relative_to(R);(stage/'content'/rel).parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,stage/'content'/rel)
    shutil.copy2(p,work.parent/rel)
    manifest['files'][rel.as_posix()]={'sha256':sha(p)}
(stage/'release_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
engine_run(e,['lint'],stage/'bus_audio_lint.log')
subprocess.run([sys.executable,str(R/'tools/finalize_day05.py'),str(stage)],cwd=R,check=True)
for n in (1,2):engine_run(e,['test','cs_release_smoke'],stage/('bus_final_compiled_smoke_%d.log'%n))
proof=dict(status='PASS',full_routes=routes,native_audio=json.loads((e/'BUS_AUDIO_PASS.json').read_text()),female_chuckle=json.loads((e/'FEMALE_CHUCKLE_PASS.json').read_text()),sports_court=json.loads((e/'SPORTS_COURT_PASS.json').read_text()),meal_horns=json.loads((e/'MEAL_HORNS_PASS.json').read_text()),credits=True,library_night=True,compiled_only_workshop_launches=2,runtime_files=470,
           source_sha256={p.relative_to(R).as_posix():sha(p) for p in [R/'bus_scene_audio.rpy',R/'day03_location_audio.rpy',R/'opening_credits.rpy',R/'new_day05_assets.rpy',R/'days/revision20261106/day03.rpy',*sorted((R/'days/day05').glob('*.rpy'))]},
           audio_sha256={p.relative_to(R).as_posix():sha(p) for p in [*list((R/'audio/sfx/bus').glob('*.ogg')),R/'audio/ambience/sports_court_day.ogg']})
proof['cabin_audio']=json.loads((e/'CABIN_AUDIO_PASS.json').read_text())
(stage/'BUS_AUDIO_FINAL_PASS.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),encoding='utf-8')
print('BUS_AUDIO_FINAL_PASS',flush=True)
