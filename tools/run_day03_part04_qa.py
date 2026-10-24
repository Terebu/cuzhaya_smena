"""Run part four in the isolated compiled-only Workshop build."""
from pathlib import Path
import sys,json,shutil
from build_release import engine_run
root=Path(__file__).resolve().parent.parent;rel=Path(sys.argv[1]).resolve();engine=rel/'validation/steamapps/common/Everlasting Summer'
checks=engine/'game/cs_release_checks'
shutil.copy2(root/'tools/day03_part04_test.rpy.txt',checks/'day03_part04_test.rpy')
results=json.loads((rel/'part04_native_results.json').read_text()) if (rel/'part04_native_results.json').exists() else []
for case in (sys.argv[2:] or ['cs_day03_p4_'+str(n) for n in range(9)]+['cs_day03_p4_guard']):
 if any(x['test']==case for x in results):continue
 marker=engine/('p4_'+case.rsplit('_',1)[1]+'_PASS.txt')
 if marker.exists():marker.unlink()
 print('Native:',case,flush=True);engine_run(engine,['test',case],rel/(case+'.log'))
 assert marker.is_file(),case
 results.append(dict(test=case,exit=0));(rel/'part04_native_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
engine_run(engine,['lint'],rel/'lint.log')
print('PART04_NATIVE_PASS',flush=True)
