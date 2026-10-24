"""Native isolated story QA; never installs test scripts into the mod."""
from pathlib import Path
import sys,json,shutil
from build_release import engine_run
release=Path(sys.argv[1]).resolve();root=Path(__file__).resolve().parent.parent
engine=release/'validation/steamapps/common/Everlasting Summer'
checks=engine/'game/cs_release_checks'
for name in ('day03_part02_test','day03_part01_test','day03_assets_test','day03_entry_frames','poster_cg_test'):
 shutil.copy2(root/('tools/'+name+'.rpy.txt'),checks/(name+'.rpy'))
results=json.loads((release/'story_qa_results.json').read_text()) if (release/'story_qa_results.json').is_file() else []
selected=sys.argv[2:] or (['cs_day03_p2_'+str(n) for n in range(9)]+['cs_day03_p2_guard','cs_day03_after_night_load','cs_day03_assets','cs_day03_entry_frames','cs_poster_25','cs_poster_33'])
for case in selected:
 if any(x['test']==case for x in results):continue
 print('Native test:',case,flush=True)
 engine_run(engine,['test',case],release/(case+'.log'))
 marker=('p2_'+case.rsplit('_',1)[1]+'_PASS.txt') if case.startswith('cs_day03_p2_') else ('poster_'+case.rsplit('_',1)[1]+'_PASS.txt') if case.startswith('cs_poster_') else 'entry_PASS.txt' if case=='cs_day03_entry_frames' else 'day03_after_night_PASS.txt' if case=='cs_day03_after_night_load' else 'day03_assets_PASS.txt'
 assert (engine/marker).is_file(),case
 results.append(dict(test=case,exit=0))
 (release/'story_qa_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('Native lint.',flush=True)
engine_run(engine,['lint'],release/'lint.log')
print('ALL_NATIVE_QA_PASS',flush=True)
