"""Refresh a verified isolated build after the final authored camera corrections."""
from pathlib import Path
import sys,json,shutil,zipfile
from build_release import engine_run,sha
from validate_release import validate,NAMESPACE
R=Path(__file__).resolve().parent.parent
stage=Path(sys.argv[1]); engine=stage/'validation/steamapps/common/Everlasting Summer'
work=stage/'validation/steamapps/workshop/content/331470/3822308228'/NAMESPACE
sources=sorted(R.glob('*.rpy'))+sorted((R/'days').rglob('*.rpy'))
for p in sources:
 q=work/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
engine_run(engine,['compile','--keep-orphan-rpyc'],stage/'day05_final_compile.log')
manifest=json.loads((stage/'release_manifest.json').read_text(encoding='utf-8'))
for p in sources:
 rel=p.relative_to(R);compiled=work/rel.with_suffix('.rpyc');dest=stage/'content'/NAMESPACE/rel.with_suffix('.rpyc')
 shutil.copy2(compiled,dest)
 snap=stage/'source_snapshot'/rel;snap.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,snap)
 manifest['files'][(Path(NAMESPACE)/rel.with_suffix('.rpyc')).as_posix()]=dict(sha256=sha(dest),source=rel.as_posix(),source_sha256=sha(p))
 (work/rel).unlink()
(stage/'release_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
result=validate(stage/'content',stage/'release_manifest.json',engine/'game',stage/'day05_final_validation.json')
assert not result['errors'],result['errors']
with zipfile.ZipFile(stage/'Chuzhaya_Smena_Vertical_Slice.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted((stage/'content').rglob('*')):
  if p.is_file(): z.write(p,'chuzaya_smena/'+p.relative_to(stage/'content').as_posix())
with zipfile.ZipFile(stage/'Chuzhaya_Smena_Vertical_Slice.zip') as z: assert z.testzip() is None
print('DAY05_FINAL_PACKAGE_PASS',len(sources),flush=True)
