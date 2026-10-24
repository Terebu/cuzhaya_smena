from pathlib import Path
import sys,json,shutil
from build_release import engine_run
R=Path(__file__).resolve().parent.parent;rel=Path(sys.argv[1]).resolve();engine=rel/'validation/steamapps/common/Everlasting Summer'
shutil.copy2(R/'tools/day03_part06_test.rpy.txt',engine/'game/cs_release_checks/day03_part06_test.rpy')
result=rel/'part06_native_results.json';results=json.loads(result.read_text()) if result.exists() else []
for suffix in (sys.argv[2:] or ['costume','0','1','2','3','guard','phone','credits','legacy_book']):
 case='cs_day03_p6_'+suffix
 if any(x['test']==case for x in results):continue
 marker=engine/('p6_'+suffix+'_PASS.txt')
 if marker.exists():marker.unlink()
 print('Native:',case,flush=True);engine_run(engine,['test',case],rel/(case+'.log'))
 assert marker.is_file(),case
 results.append(dict(test=case,status='PASS'));result.write_text(json.dumps(results,indent=2),encoding='utf8')
print('PART06_NATIVE_PASS',flush=True)
