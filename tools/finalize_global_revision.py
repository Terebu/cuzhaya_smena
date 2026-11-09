"""Finish the isolated, verified package without publishing to Workshop."""
from pathlib import Path
import json,shutil,subprocess,sys
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
shutil.copy2(R/'tools/global_revision_credits.rpy.txt',engine/'game/cs_release_checks/global_revision_credits.rpy')
if not (engine/'global_credits_PASS.txt').is_file():
    engine_run(engine,['test','cs_global_credits'],stage/'global_credits.log')
assert (engine/'global_credits_PASS.txt').is_file()
engine_run(engine,['lint'],stage/'global_lint.log')
subprocess.run([sys.executable,str(R/'tools/finalize_day05.py'),str(stage)],check=True,cwd=R)
for n in (1,2):
    engine_run(engine,['test','cs_release_smoke'],stage/('global_compiled_smoke_%d.log'%n))
proof={name:json.loads((stage/name).read_text(encoding='utf-8')) for name in ('GLOBAL_ROUTES_PASS.json','GLOBAL_LEGACY_PASS.json','GLOBAL_DAY5_LEGACY_PASS.json')}
assert all(x['status']=='PASS' and x.get('save_roundtrip') for x in proof['GLOBAL_ROUTES_PASS.json'])
proof.update(status='PASS',compiled_only_workshop_smokes=2,credits=True,lint_exit=0)
(stage/'GLOBAL_FINAL_PASS.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),encoding='utf-8')
print('GLOBAL_FINAL_PASS',flush=True)
