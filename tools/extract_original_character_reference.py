"""Read original dialogue as data, without executing compiled game scripts."""
from pathlib import Path
import io,json
from rpyc_audit import DataUnpickler,payload
R=Path(__file__).resolve().parent.parent
game=R.parents[1]
result={k:[] for k in ('cs','mz','dv','mi','un','sl','us','mt','sh','el','me')}
for p in sorted((game/'scenario').glob('day[12].rpyc')):
 root=DataUnpickler(io.BytesIO(payload(p)),encoding='utf8',errors='replace').load()
 seen=set();stack=[root];nodes=[]
 while stack:
  obj=stack.pop()
  if id(obj) in seen:continue
  seen.add(id(obj))
  if isinstance(obj,dict):stack.extend(obj.values())
  elif isinstance(obj,(tuple,list,set)):stack.extend(obj)
  elif hasattr(obj,'__dict__'):
   a=vars(obj);stack.extend(a.values())
   if type(obj).__name__=='Say' and a.get('who') in result:nodes.append(a)
 for a in sorted(nodes,key=lambda a:a.get('linenumber',0)):
  bucket=result[a['who']]
  if len(bucket)<12:bucket.append(dict(file=p.relative_to(game).as_posix(),line=a.get('linenumber'),text=a.get('what')))
(R/'source/original_character_reference.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
