"""Stable named call returns and data-only migration from published snapshots."""
from pathlib import Path
from collections import defaultdict
import re,hashlib,io,json,ast
from rpyc_audit import DataUnpickler,payload
R=Path(__file__).resolve().parent.parent
call=re.compile(r'^(\s*)call (cs_\w+)(?: from (cs_return_\w+))?\s*$')
def sites(text,rel):
 owner='file';counts=defaultdict(int);result={}
 for number,line in enumerate(text.splitlines(),1):
  m=re.match(r'^\s*label (\w+)',line)
  if m:owner=m[1]
  m=call.match(line)
  if not m:continue
  indent,target,existing=m.groups()
  # The renamed branch has the same role as the old 101a/101b menu call.
  logical={'cs_day03_100a':'cs_day03_101a','cs_day03_100b':'cs_day03_101b'}.get(target,target) if rel=='days/day03/part04/00_flow.rpy' else target
  key=(rel,owner,logical);counts[key]+=1
  label=existing or 'cs_return_'+hashlib.sha256(('|'.join(key)+'|'+str(counts[key])).encode()).hexdigest()[:20]
  result[number]=(indent,target,label)
 return result
paths=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'));anchors=set()
for p in paths:
 rel=p.relative_to(R).as_posix();s=p.read_text(encoding='utf-8-sig');mapping=sites(s,rel);lines=s.splitlines()
 for number,(indent,target,label) in mapping.items():lines[number-1]=indent+'call '+target+' from '+label;anchors.add(label)
 if mapping:p.write_text('\n'.join(lines)+'\n',encoding='utf8')
legacy={};skipped=[]
existing=R/'save_return_compat.rpy'
if existing.exists():
 match=re.search(r'^    cs_legacy_call_returns = (.+)$',existing.read_text(encoding='utf8'),re.M)
 if match:legacy.update(ast.literal_eval(match.group(1)))
for name in ('day03_part07_20261024_final','day03_part06_20261023_final','day03_medpoint_revision_20261024_final','day03_part07_revision_20261024_final','day03_part08_09_20261025_final','day03_part10_20261025_final','day03_part11_20261025_final','day03_part12_20261025_final','day03_part13_20261026_final'):
 release=Path('D:/stean/release_chuzaya_smena')/name
 for src in (release/'source_snapshot').rglob('*.rpy'):
  rel=src.relative_to(release/'source_snapshot').as_posix();mapping=sites(src.read_text(encoding='utf-8-sig'),rel)
  if not mapping:continue
  compiled=release/'content/cs_scripts_5ea2d086'/Path(rel).with_suffix('.rpyc')
  root=DataUnpickler(io.BytesIO(payload(compiled)),encoding='utf8',errors='replace').load()
  seen=set();stack=[root];nodes={};calls=[]
  while stack:
   obj=stack.pop()
   if id(obj) in seen:continue
   seen.add(id(obj))
   if isinstance(obj,dict):stack.extend(obj.values())
   elif isinstance(obj,(tuple,list,set)):stack.extend(obj)
   elif hasattr(obj,'__dict__'):
    a=vars(obj);stack.extend(a.values())
    if getattr(obj,'audit_module','')=='renpy.ast' and 'name' in a:
     nodes[a['name']]=obj
     if type(obj).__name__=='Call':calls.append(obj)
  for obj in calls:
   a=vars(obj);entry=mapping.get(a.get('linenumber'))
   if not entry or entry[2] not in anchors:continue
   ident=a['name']
   if not isinstance(ident,tuple):continue
   ret=ident[:-1]+(ident[-1]+1,)
   if ret not in nodes or type(nodes[ret]).__name__!='Pass':
    skipped.append((name,rel,a.get('linenumber')));continue
   legacy[ret]=entry[2]
assert not skipped,skipped
body='''# -*- coding: utf-8 -*-
# Only invalid return addresses from this mod's known previous releases.
# Do not redirect other mods, current saves, or the loaded statement itself.
init 40 python:
    cs_legacy_call_returns = '''+repr(legacy)+'''
    def cs_migrate_call_returns():
        if not getattr(store,"cs_active",False):
            return
        stack=renpy.get_return_stack()
        fixed=[]
        changed=False
        for old in stack:
            target=cs_legacy_call_returns.get(old) if isinstance(old,tuple) else None
            if target and not renpy.has_label(old) and renpy.has_label(target):
                fixed.append(target)
                changed=True
            else:
                fixed.append(old)
        if changed:
            renpy.set_return_stack(fixed)
            renpy.block_rollback()
    config.after_load_callbacks.append(cs_migrate_call_returns)
'''
(R/'save_return_compat.rpy').write_text(body,encoding='utf8')
(R/'source/save_return_compat_audit.json').write_text(json.dumps(dict(stable_sites=len(anchors),legacy_addresses=len(legacy),skipped=skipped),indent=2),encoding='utf8')
print('STABLE_CALL_RETURNS',len(anchors),'anchors;',len(legacy),'verified old addresses')
