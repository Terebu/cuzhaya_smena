"""Replace dinner 64, preserving the scene label and friendship consequences."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part09_dinner_revised.md').read_text(encoding='utf8').split('**[КОНЕЦ ЗАМЕНЯЮЩЕЙ СЦЕНЫ 64.]**')[0]
parts=re.split(r'### Сцена 64([АБВГД]?)(-[12])?\. (.+)\n',raw)
suffixes={'':'','А':'a','Б':'b','В':'c','Г':'d','Д':'e'}
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz','Семён':'cs_sy'}
tags=['cs_darya','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs','cs_dasha_winter','cs_dasha_pioneer']
catalog=[]
for i in range(1,len(parts),4):
 suffix=suffixes[parts[i]]+(parts[i+1] or '').replace('-','');title=parts[i+2];body=parts[i+3]
 lines=['# -*- coding: utf-8 -*-','label cs_day02_64'+suffix+':','    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part09_live = True'];indent='    '
 poses={'cs_darya':'shrug','cs_zhenya':'normal','cs_semen':'neutral'}
 group=['cs_darya'] if suffix=='' else ['cs_zhenya','cs_darya'];mode='conditional' if suffix=='e' else 'plain'
 def emit(s):lines.append(indent+s)
 def actor(t,g):
  far=len(g)>2;pose=poses[t]
  pos=('cs_darya_far_right' if far else 'cs_darya_normal_right') if t=='cs_darya' else ('cs_semen_far_center' if far else 'cs_semen_normal_left') if t=='cs_semen' else ('cs_darya_far_left' if far else 'cs_darya_normal_left')
  return t+' '+pose+' pioneer '+('far' if far else 'normal')+' at '+pos
 def stage(g):
  for t in tags:
   if t not in g:emit('hide '+t)
  for t in g:emit('show '+actor(t,g))
  emit('$ cs_part09_cast = '+q(g))
 def show():
  global indent
  if mode in ('conditional','semen'):
   old=indent;emit('if cs_friend_mz >= 1:');indent+='    ';stage(['cs_zhenya']+(['cs_semen'] if mode=='semen' else [])+['cs_darya']);indent=old;emit('else:');indent+='    ';stage((['cs_semen'] if mode=='semen' else [])+['cs_darya']);indent=old
  else:stage(group)
 show()
 if suffix=='':emit('$ renpy.music.set_volume(0.14, channel="music", delay=1.0)');emit('label cs_check_part09_s64:')
 if suffix=='d1':emit('$ renpy.music.set_volume(0.09, channel="music", delay=1.0)')
 elif suffix=='e':emit('$ renpy.music.set_volume(0.14, channel="music", delay=1.0)')
 emit('label cs_check_dinner64'+(suffix or '_start')+':')
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if p.startswith('**[ЕСЛИ `'):indent='    ';emit('if '+re.search(r'`([^`]+)`',p)[1]+':');indent='        ';continue
  if p.startswith('**[ИНАЧЕ:'):indent='    ';emit('else:');indent='        ';continue
  if p.startswith('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):indent='    ';continue
  if not p or p=='---' or p.startswith(('#','**[')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if suffix=='d' and text=='Потом Женя осторожно отодвинула книгу подальше от тарелки.':
   emit('if cs_mz_quiet_visit_seen:');lines.append('        cs_narrator '+q('Мы снова ненадолго заговорили о той самой книге — без пересказов и спойлеров.'));emit('else:');indent='        '
  if suffix=='d' and text=='А ты вообще всегда читаешь во время еды?':indent='    '
  if suffix=='' and text=='Женя заметила нас ещё до того, как мы подошли.':group=['cs_zhenya','cs_darya'];show();emit('label cs_check_dinner64_greeting:')
  if suffix=='c' and text=='Мы отошли к свободному столику возле окна.':group=['cs_darya'];show();emit('label cs_check_dinner64_separate:')
  if suffix=='e' and text=='Увидев нас, остановился.':mode='semen';show();emit('label cs_check_part09_semen:')
  if suffix=='e' and text=='Семён попрощался и отправился к выходу.':mode='conditional';show();emit('label cs_check_part09_semen_left:')
  if suffix=='e' and text=='Женя направилась к выходу.':mode='plain';group=['cs_darya'];show();emit('label cs_check_dinner64_zhenya_left:')
  if suffix=='e' and text=='Мы вышли из столовой.':
   mode='plain';group=['cs_darya'];emit('$ sunset_time()');emit('$ persistent.sprite_time = "sunset"');emit('scene bg ext_dining_hall_near_sunset');show();emit('with Dissolve(0.8)');emit('play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)');emit('play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 2.0');emit('$ renpy.music.set_volume(0.14, channel="music", delay=1.0)')
  if suffix=='e' and text=='На площади постепенно собирались зрители.':emit('scene bg ext_square_sunset');show();emit('with Dissolve(0.8)');emit('label cs_check_dinner64_exit:')
  if speaker=='cs_da':
   pose=reaction(text,speaker=speaker)
   if pose and pose!=poses['cs_darya']:poses['cs_darya']=pose;show()
  if speaker=='cs_mz':
   pose='glasses_touch' if 'каталог' in text or 'книгам' in text else 'thinking' if '?' in text else 'explaining' if len(text)>85 else 'thoughtful' if suffix in ('d','d1','d2') else 'normal'
   if pose!=poses['cs_zhenya']:poses['cs_zhenya']=pose;show()
  if speaker=='cs_sy':
   pose='explaining' if len(text)>85 else 'thinking' if '?' in text else 'smile'
   if pose!=poses['cs_semen']:poses['cs_semen']=pose;show()
  emit(speaker+' '+q(text));catalog.append(dict(suffix=suffix,speaker=speaker,text=text))
 indent='    '
 if suffix=='':emit('call cs_day02_dinner_branches')
 emit('return')
 file='64_'+(suffix+'_' if suffix else '')+'scene.rpy';(R/'days/day02/part09'/file).write_text('\n'.join(lines)+'\n',encoding='utf8')
(R/'source/day02_dinner_revised_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Replacement dinner:',len(catalog),'source blocks, eight files')

if (R/'source/day02_part10.md').exists():
 p=R/'days/day02/part09/64_e_scene.rpy'
 p.write_text(p.read_text(encoding='utf8').replace('scene bg ext_square_sunset','scene bg ext_dining_hall_near_sunset'),encoding='utf8')
