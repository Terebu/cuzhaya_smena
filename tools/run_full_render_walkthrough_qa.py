from pathlib import Path
import sys,shutil,json
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;rel=Path(sys.argv[1]);engine=rel/'validation/steamapps/common/Everlasting Summer'
for name in ('day03_part06_test','full_render_walkthrough_test'):
 shutil.copy2(R/('tools/'+name+'.rpy.txt'),engine/('game/cs_release_checks/'+name+'.rpy'))
results=[]
for route in (sys.argv[2:] or ['high','low']):
 marker=engine/('rw_'+route+'_PASS.txt')
 if marker.exists():marker.unlink()
 choices=engine/('rw_'+route+'_choices.txt')
 if choices.exists():choices.unlink()
 print('Native render walkthrough:',route,flush=True)
 engine_run(engine,['test','cs_render_walk_'+route],rel/('render_walk_'+route+'.log'),timeout=900)
 assert marker.is_file(),route
 state=json.loads((engine/('rw_'+route+'_state.json')).read_text())
 assert set(state['visited']) >= {'cs_scene_01','cs_scene_07','cs_day01_01','cs_day01_64','cs_day02_01','cs_day02_74','cs_day03_75','cs_day03_83','cs_day03_96','cs_day03_104','cs_day03_113','cs_day03_114','cs_day03_115','cs_day03_117','cs_day03_119','cs_day03_120','cs_day03_121','cs_day03_122','cs_day03_123','cs_day03_124','cs_day03_126','cs_day03_127','cs_day03_128'}
 results.append(dict(route=route,**state))
 (rel/'full_render_walkthrough_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print('FULL_RENDER_WALKTHROUGH_PASS',flush=True)
