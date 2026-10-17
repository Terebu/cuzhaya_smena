"""Apply reviewed exact-paragraph shot plans. No runtime text classification."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
plans=json.loads((R/'source/scene_frame_plan.json').read_text(encoding='utf8'))
q=lambda x:json.dumps(x,ensure_ascii=False)
missing=[];applied=[]
for relative,plan in plans.items():
 p=R/relative;lines=p.read_text(encoding='utf8').splitlines()
 # Normalise only legacy original/custom sprite references, retaining one tag.
 for i,line in enumerate(lines):
  m=re.match(r'^(\s*)show (cs|mz) (?!custom\b)(\w+)(.*)$',line)
  if not m:continue
  indent,tag,emotion,tail=m.groups();distance='far' if re.search(r'\bfar\b',tail) else 'close' if re.search(r'\bclose\b',tail) else 'normal'
  side='right' if re.search(r' at \w*right',tail) else 'center' if re.search(r' at \w*center',tail) else 'left'
  z=re.search(r' zorder (-?\d+)',tail);zorder=' zorder '+z[1] if z else ''
  if tag=='cs':
   pose={'normal':'serious','smile':'warm_smile','shy':'amused','angry':'angry','laugh':'amused'}.get(emotion,'thoughtful')
   lines[i]=indent+'show cs custom '+pose+' medical '+distance+' at cs_viola_'+distance+'_'+side+zorder
  else:
   pose={'normal':'normal','shy':'shy','rage':'angry','angry':'angry','laugh':'explaining','smile':'thoughtful'}.get(emotion,'thinking')
   lines[i]=indent+'show cs_zhenya '+pose+' pioneer '+distance+' at cs_darya_'+distance+'_'+side+zorder
 first=True;occ={};out=[];reflective=False
 def block(indent,commands,reason):
  return [indent+'# cs_director_begin: '+reason]+[indent+c for c in commands]+[indent+'# cs_director_end']
 for line in lines:
  # An authored REFLECTIVE_SHOT owns the whole block, including legacy
  # emotion cues inside its narration. Background changes remain untouched.
  if re.match(r'\s*scene ',line):reflective=False
  if reflective and re.match(r'\s*show (cs_darya|cs_dasha_winter|cs_semen|cs_zhenya|mz|un|mi|dv|us|sl|mt|el|sh|cs)\b',line):
   out.append(line[:len(line)-len(line.lstrip())]+'# cs_reflective_suppressed: '+line.strip())
   continue
  m=re.match(r'^(\s+)(cs_\w+) (".*")$',line)
  if not m:out.append(line);continue
  indent,speaker,literal=m.groups();text=json.loads(literal);occ[text]=occ.get(text,0)+1
  if first:
   initial=q(plan['initial'])
   if plan.get('initial_if'):
    initial+=' if '+plan['initial_if']+' else '+q(plan['initial_else'])
   out+=block(indent,['$ cs_frame_focus('+initial+')','with cs_sprite_change'],'entry frame; explicit scene plan')
   first=False
  events=[e for e in plan['events'] if e['anchor']==text and e.get('occurrence',1)==occ[text]]
  def emit(e):
   command='$ cs_actor_exit('+q(e['tags'])+')' if e['kind']=='absent' else '$ cs_frame_focus('+q(e['tags'])+')'
   if e['kind']=='reflective':command='$ cs_reflective_focus()'
   cues=[command]
   if e.get('images'):
    cues+=['show '+name for name in e['images']]
    cues+=['$ cs_presence_stage()']
   out.extend(block(indent,cues+['with cs_sprite_leave' if e['kind']=='absent' else 'with cs_sprite_change','label cs_director_check_'+e['id']+':'],e['reason']))
   applied.append(dict(file=relative,**e))
  for e in events:
   if e['when']=='before':
    emit(e);reflective=e['kind']=='reflective'
  out.append(line)
  for e in events:
   if e['when']=='after':
    emit(e);reflective=e['kind']=='reflective'
 for e in plan['events']:
  if occ.get(e['anchor'],0)<e.get('occurrence',1):missing.append(dict(file=relative,**e))
 p.write_text('\n'.join(out)+'\n',encoding='utf8')
(R/'qa/director_frame_audit.json').write_text(json.dumps(dict(files=len(plans),events=applied,missing_anchors=missing),ensure_ascii=False,indent=2),encoding='utf8')
print('Explicit staging:',len(plans),'scene frames;',len(applied),'reviewed events;',len(missing),'missing anchors')
if missing:
 for e in missing:print(e['file'],repr(e['anchor']))
 raise SystemExit(1)
