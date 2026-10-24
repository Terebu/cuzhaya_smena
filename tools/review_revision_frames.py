"""Record reviewed frames; only unchanged image bytes inherit that review."""
from pathlib import Path
import hashlib,json,sys,shutil
R=Path(__file__).resolve().parent.parent
stage=Path('D:/stean/release_chuzaya_smena/day03_medpoint_revision_20261024')
engine=stage/'validation/steamapps/common/Everlasting Summer'
record=stage/'reviewed_before_call_fix.json'
frames=sorted(engine.glob('p6_render_reviewed_*.png'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if sys.argv[1]=='record':
 record.write_text(json.dumps({p.name:sha(p) for p in frames},indent=2),encoding='utf8')
 print('Previously inspected:',len(frames))
else:
 old=json.loads(record.read_text());changed=[];same=[]
 target=engine/'final_changed_frames';target.mkdir(exist_ok=True)
 for p in frames:
  if old.get(p.name)==sha(p):same.append(p.name)
  else:changed.append(p.name);shutil.copy2(p,target/p.name)
 result=dict(total=len(frames),identical_to_reviewed=len(same),changed=len(changed),changed_frames=changed)
 (stage/'final_visual_comparison.json').write_text(json.dumps(result,indent=2),encoding='utf8')
 print('VISUAL COMPARISON:',result['total'],'frames;',len(same),'identical;',len(changed),'need renewed review')
