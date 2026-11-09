from pathlib import Path
import json,sys,shutil,os
from build_release import engine_run
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]);engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228/cs_scripts_5ea2d086'
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
    dest=work/p.relative_to(R);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
shutil.copy2(R/'tools/global_revision_test.rpy.txt',engine/'game/cs_release_checks/global_revision_test.rpy')
routes=sys.argv[2:] or ('a','b','higha','highb')
result=[]
for route in routes:
    os.environ['CS_GLOBAL_ROUTE']=route
    engine_run(engine,['test','cs_global_revision'],stage/('global_'+route+'.log'),timeout=1800)
    data=json.loads((engine/('global_'+route+'_PASS.json')).read_text());result.append(data)
    assert data.get('save_roundtrip'),data
    print('GLOBAL_ROUTE_PASS',route,data['say_count'],flush=True)
(stage/'GLOBAL_ROUTES_PASS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
