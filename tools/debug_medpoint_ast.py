from pathlib import Path
import io,sys
from rpyc_audit import DataUnpickler,payload
for filename in sys.argv[1:]:
 root=DataUnpickler(io.BytesIO(payload(Path(filename))),encoding='utf8',errors='replace').load()
 seen=set();stack=[root];nodes=[]
 while stack:
  obj=stack.pop()
  if id(obj) in seen:continue
  seen.add(id(obj))
  if isinstance(obj,dict):stack.extend(obj.values())
  elif isinstance(obj,(tuple,list,set)):stack.extend(obj)
  elif hasattr(obj,'__dict__'):
   a=vars(obj);stack.extend(a.values())
   if getattr(obj,'audit_module','')=='renpy.ast' and type(obj).__name__ in ('Call','Label','Return'):
    nodes.append((a.get('linenumber'),type(obj).__name__,a.get('name'),a.get('label'),getattr(a.get('next'),'name',None)))
 print(filename)
 for n in sorted(nodes,key=lambda x:x[0] or 0):print(n)
