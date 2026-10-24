"""Attach native QA only after checking source and asset identity with release."""
from pathlib import Path
import sys,json,hashlib,shutil
from validate_release import NAMESPACE
stage,final=map(Path,sys.argv[1:3]);work=stage/'validation/steamapps/workshop/content/331470/3822308228'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
 rel=p.relative_to(final/'source_snapshot');observed=work/NAMESPACE/rel
 assert observed.is_file() and sha(p)==sha(observed),str(rel)
 sources.append(dict(path=rel.as_posix(),sha256=sha(p)))
assets=0
for rel,entry in json.loads((final/'release_manifest.json').read_text(encoding='utf8'))['files'].items():
 if rel.endswith('.rpyc'):continue
 assert sha(work/rel)==entry['sha256'],rel
 assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for name in ('full_render_walkthrough_results.json','part07_native_results.json','part06_native_results.json','p7_cross_save_result.json','render_walk_high.log','render_walk_low.log','lint.log','lint_diagnostics.json'):
 shutil.copy2(stage/name,out/name)
for p in stage.glob('p7_*.log'):shutil.copy2(p,out/p.name)
engine=stage/'validation/steamapps/common/Everlasting Summer';images=out/'native_frames';images.mkdir(exist_ok=True)
for p in engine.glob('rw_*_choices.txt'):shutil.copy2(p,out/p.name)
frames=[]
for prefix in ('p6_render_reviewed_high_','p6_render_reviewed_low_','p6_p7_','p6_costume_'):
 for p in sorted(engine.glob(prefix+'*.png')):
  shutil.copy2(p,images/p.name);frames.append(p.name)
 contacts=engine/(prefix.rstrip('_')+'_contacts')
 if contacts.exists():
  target=out/contacts.name;target.mkdir(exist_ok=True)
  shutil.copy2(contacts/'index.json',target/'index.json')
  for entry in json.loads((contacts/'index.json').read_text(encoding='utf8')):
   p=contacts/entry['sheet'];shutil.copy2(p,target/p.name)
for p in engine.glob('p7_cross_version*.png'):shutil.copy2(p,images/p.name);frames.append(p.name)
summary=dict(status='PASS',matching_sources=len(sources),matching_assets=assets,frames=len(frames),sources=sources,images=frames,scope='Two complete native accelerated routes, 8 targeted native cases, actual previous-build save migration. Every scene, CG and cast change rendered. Transitions disabled for full routes, retained in targeted checks. Contact sheets and key full-size frames reviewed.')
(out/'tested_source_identity.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print('PART07_EVIDENCE_PASS',len(sources),'matching scripts;',assets,'assets;',len(frames),'frames')
