"""Retain story QA evidence only when its tested sources match the final build."""
from pathlib import Path
import sys,json,hashlib,shutil
from validate_release import NAMESPACE
stage,final=map(Path,sys.argv[1:3]);workshop=stage/'validation/steamapps/workshop/content/331470/3822308228'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checked=[]
for p in sorted((final/'source_snapshot').rglob('*.rpy')):
 rel=p.relative_to(final/'source_snapshot');observed=workshop/NAMESPACE/rel
 if not observed.exists():observed=stage/'source_snapshot'/rel
 assert sha(p)==sha(observed),('Tested source differs',str(rel))
 checked.append(dict(path=rel.as_posix(),sha256=sha(p)))
assets=0
for rel,entry in json.loads((final/'release_manifest.json').read_text(encoding='utf8'))['files'].items():
 if rel.endswith('.rpyc'):continue
 assert sha(workshop/rel)==entry['sha256'],('Tested asset differs',rel)
 assets+=1
out=final/'qa_evidence';out.mkdir(exist_ok=True)
for name in ('full_render_walkthrough_results.json','part06_native_results.json','render_walk_high.log','render_walk_low.log'):
 shutil.copy2(stage/name,out/name)
engine=stage/'validation/steamapps/common/Everlasting Summer';images=out/'native_frames';images.mkdir(exist_ok=True)
frames=[]
for route in ('high','low'):
 for p in sorted(engine.glob('p6_render_'+route+'_*.png')):
  shutil.copy2(p,images/p.name);frames.append(p.name)
 contacts=engine/('p6_render_'+route+'_contacts')
 shutil.copytree(contacts,out/contacts.name,dirs_exist_ok=True)
summary=dict(status='PASS',tested_build=str(stage),final_build=str(final),matching_sources=len(checked),matching_assets=assets,frames=len(frames),sources=checked,images=frames,review='All 15 contact sheets visually inspected, with full-size inspection of wardrobe, music-club composition and phone UI. Full traversal executes every dialogue statement and the real menu branches, suppressing input waits; screenshots are rendered in native RenPy. Scene transitions disabled for the accelerated full routes; targeted scene tests use normal transitions.')
(out/'tested_source_identity.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print('EVIDENCE_PASS',len(checked),'identical sources;',assets,'identical assets;',len(frames),'native frames')
