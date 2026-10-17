"""Collect literal stage references from every active production RPY for engine QA."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
refs={};audio={}
for p in R.rglob('*.rpy'):
 if 'qa' in p.relative_to(R).parts:continue
 for i,line in enumerate(p.read_text(encoding='utf8').splitlines(),1):
  m=re.match(r'^\s*(?:show|scene)\s+(.+?)(?::)?$',line)
  if m:
   name=re.split(r'\s+(?:at|as|onlayer|zorder|behind|with)\s+',m[1])[0].rstrip(':')
   if not name.startswith(('screen ','expression ')):
    refs.setdefault(name,[]).append(p.relative_to(R).as_posix()+':'+str(i))
  m=re.match(r'^\s*play\s+(?:music|sound|ambience|cs_piano)\s+(".*?")',line)
  if m:
   path=re.sub(r'^<[^>]*>','',json.loads(m[1]))
   audio.setdefault(path,[]).append(p.relative_to(R).as_posix()+':'+str(i))
(R/'qa/mod_literal_stage_references.json').write_text(json.dumps(dict(images=refs,audio=audio),ensure_ascii=False,indent=2),encoding='utf8')
print(len(refs),'literal image names;',len(audio),'sound paths across all production RPY')
