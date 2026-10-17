"""Offline, explicit scene staging. Never a runtime speaker-hiding callback."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
TAGS={'cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_dasha_full','cs_dasha','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs'}
CMD=re.compile(r'^(\s*)(show|hide) ('+'|'.join(sorted(TAGS,key=len,reverse=True))+r')(?:\s.*)?$')
SAY=re.compile(r'^\s+(cs_\w+) (".*")$')
CAST=re.compile(r'^\s*\$ cs_(?:breakfast|part02|part03|part04|part05|part06|part07|part08|part09|part10|reading|d2_visible)_cast\s*=')
def is_cast(line):return bool(CAST.match(line) or re.match(r'^\s*\$ cs_d2_visible_cast\s*=',line))
def next_say(lines,i):
 for line in lines[i:]:
  if SAY.match(line):return SAY.match(line)
  if line.strip().startswith(('scene ','return','call ','menu:','if ')):return None
 return None
reports=[]
for path in sorted((R/'days').rglob('*.rpy')):
 raw=path.read_text(encoding='utf8').splitlines()
 if not any(SAY.match(line) or CMD.match(line) or line.strip().startswith('scene ') for line in raw):continue
 # Remove only old/generated camera directives, retaining phone and CG staging.
 lines=[];i=0
 while i<len(raw):
  s=raw[i].strip()
  if s.startswith('# cs_director_begin:'):
   i+=1
   while i<len(raw) and raw[i].strip()!='# cs_director_end':i+=1
   i+=1;continue
  if s in ('# cs_global_transition','# cs_focus: camera'):
   i+=2;continue
  if s=='# cs_global_private':
   i+=1
   while i<len(raw) and raw[i].strip()!='# cs_global_private_end':i+=1
   i+=1;continue
  if '# cs_global_hidden: ' in raw[i]:lines.append(raw[i].replace('# cs_global_hidden: ',''))
  elif '# cs_reflective_suppressed: ' in raw[i]:lines.append(raw[i].replace('# cs_reflective_suppressed: ',''))
  elif '# cs_focus_suppressed: ' in raw[i]:lines.append(raw[i].replace('# cs_focus_suppressed: ',''))
  elif raw[i].strip() == '$ cs_presence_stage()' or raw[i].strip().startswith(('$ cs_presence_saved = cs_presence_snapshot(', '$ cs_presence_restore(', '$ cs_director_scene(')):pass
  else:lines.append(raw[i])
  i+=1
 # Compact an atomic staging block: a same-tag emotion never has hide->show.
 prepared=[];i=0;changes=0;redundant=0;brief_clears=0
 while i<len(lines):
  m=CMD.match(lines[i])
  if not m or lines[i].rstrip().endswith(':'):prepared.append(lines[i]);i+=1;continue
  indent=m[1];j=i;batch=[]
  while j<len(lines):
   t=lines[j];c=CMD.match(t)
   if (c and c[1]==indent and not t.rstrip().endswith(':')) or (is_cast(t) and t.startswith(indent+'$')) or (t.startswith(indent+'#') and 'cs_' in t):batch.append(t);j+=1
   else:break
  commands=[CMD.match(t) for t in batch if CMD.match(t)]
  shown={c[3] for c in commands if c[2]=='show'}
  upcoming=next_say(lines,j)
  camera_clear=len({c[3] for c in commands if c[2]=='hide'})>=10 and not shown and upcoming and upcoming[1]=='cs_th'
  if camera_clear:
   # The new private-pass below distinguishes brief thoughts from long POV shots.
   prepared.extend(t for t in batch if not CMD.match(t) and not is_cast(t));brief_clears+=1;i=j;continue
  output=[];last_show={}
  for k,t in enumerate(batch):
   c=CMD.match(t)
   if c and c[2]=='show':last_show[c[3]]=k
  for k,t in enumerate(batch):
   c=CMD.match(t)
   if c and ((c[2]=='hide' and c[3] in shown) or (c[2]=='show' and last_show[c[3]]!=k)):
    redundant+=1;continue
   if c:t=re.sub(r' with .*$','',t)
   output.append(t)
  # Preserve every actor until scene clears the location (user's explicit rule).
  if sum(c[2]=='hide' for c in commands)>=5:
   output=[t for t in output if not (CMD.match(t) and CMD.match(t)[2]=='hide')]
  prepared+=output
  if any(c[2]=='show' for c in commands):prepared.append(indent+'$ cs_presence_stage()')
  # Respect an existing scene transition that follows the whole block.
  nextline=lines[j].strip() if j<len(lines) else ''
  if commands and not nextline.startswith('with '):
   transition='cs_sprite_change' if shown else 'cs_sprite_leave'
   prepared+=[indent+'# cs_global_transition',indent+'with '+transition];changes+=1
  i=j
 # Part 6's global presence rule supersedes automatic thought-camera cuts.
 # Only the author's explicit exits, CGs and staged reverse shots hide actors.
 long_starts=set()
 physical={};hidden=False;out=[];private_count=0
 def camera(lines_to_emit,indent):
  return [indent+'# cs_global_private']+[indent+t for t in lines_to_emit]+[indent+'# cs_global_private_end']
 def cast_updates(values):
  return ['$ '+name+' = '+repr(values) for name in ('cs_breakfast_cast','cs_part02_cast','cs_part03_cast','cs_part04_cast','cs_part05_cast','cs_part06_cast','cs_d2_visible_cast')]
 for i,line in enumerate(prepared):
  s=line.strip();indent=line[:len(line)-len(line.lstrip())];say=SAY.match(line);cmd=CMD.match(line)
  if s.startswith('scene '):physical={};hidden=False
  if i in long_starts and physical and not hidden:
   out+=camera(['hide '+tag for tag in physical]+cast_updates([])+['with cs_sprite_leave'],indent);hidden=True;private_count+=1
  if say and say[1] not in ('cs_th','cs_narrator') and hidden:
   out+=camera(list(physical.values())+cast_updates(list(physical))+['with cs_sprite_enter'],indent);hidden=False
  if cmd:
   tag=cmd[3]
   if cmd[2]=='show':physical[tag]=re.sub(r' with .*$','',s)
   else:physical.pop(tag,None)
   if hidden:
    out.append(indent+'# cs_global_hidden: '+s);continue
  if hidden and is_cast(line):out.append(indent+'# cs_global_hidden: '+s);continue
  out.append(line)
 # A scene clears the frame; only explicit following shows/focus restore actors.
 framed=[]
 for line in out:
  m=re.match(r'^(\s*)scene (.+)$',line)
  if not m:framed.append(line);continue
  indent,spec=m.groups();pieces=spec.split(' with ',1)
  name=re.split(r' at | onlayer | zorder ',pieces[0])[0].strip()
  framed.append(indent+'$ cs_director_scene('+json.dumps(name)+')')
  framed.append(indent+'scene '+pieces[0])
  if len(pieces)>1:framed.append(indent+'with '+pieces[1])
 path.write_text('\n'.join(framed)+'\n',encoding='utf8')
 reports.append(dict(file=path.relative_to(R).as_posix(),transitions=changes,redundant_commands_removed=redundant,thought_clear_blocks_replaced=brief_clears,long_private_shots=private_count))
(R/'qa/global_sprite_staging.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf8')
print('Global staging:',len(reports),'files;',sum(x['transitions'] for x in reports),'transitions;',sum(x['redundant_commands_removed'] for x in reports),'redundant commands removed')

# New reviewed story-frame plans supersede the historical keep-everyone policy.
import runpy
runpy.run_path(str(R/"tools/direct_scene_frames.py"), run_name="__main__")
runpy.run_path(str(R/"tools/build_dialogue_visibility_audit.py"), run_name="__main__")
