"""Replace breakfast in part 1, never append a second breakfast."""
import re,json
from pathlib import Path
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_breakfast.md').read_text(encoding='utf8').split('## Техническое задание')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda text:json.dumps(text,ensure_ascii=False)
tags=['cs_darya','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
catalog=[]
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d:'%n,'    $ save_name = '+q('Чужая смена — День 2: '+title)]
 emit=lambda text:lines.append('    '+text)
 group=['cs_darya'] if n==10 else ['un','cs_darya'] if n==12 else ['cs_semen','cs_darya']
 visible=[];private=False;poses={'cs_darya':'shrug','cs_semen':'neutral','un':'normal'};arrived=False;un_departed=False;first_un=False;first_sy=False
 def clear():
  for tag in tags:emit('hide '+tag)
  visible.clear();emit('$ cs_breakfast_cast = []')
 def show():
  clear()
  for tag in group:
   if tag=='un':emit('show un '+poses[tag]+' pioneer at cs_actor_left zorder 10')
   else:emit('show '+tag+' '+poses[tag]+' pioneer normal at '+('cs_darya_normal_right' if tag=='cs_darya' else 'cs_semen_normal_left'))
  visible[:]=group;emit('$ cs_breakfast_cast = '+q(group))
 def bg(name):emit('scene '+name);show();emit('with Dissolve(0.8)')
 def music(name):
  path='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(path)+':');lines.append('        play music '+q(path)+' fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume(0.22, channel="music", delay=1.0)')
 def amb(name,volume=.22):
  path='sound/ambiences/'+name+'.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(path)+':');lines.append('        play ambience '+q(path)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 if n==12:
  emit('if not (cs_met_un and cs_friend_un >= 1):');lines.append('        return');emit('$ cs_un_name_known = True')
 if n==10:
  emit('$ cs_breakfast_live = True');emit('$ day_time()');emit('$ persistent.sprite_time = "day"');bg('bg ext_dining_hall_near_day');amb('camp_center_day',.18);music('my_daily_life')
 else:
  show()
  if n==13:emit('$ cs_breakfast_un_here = False');music('just_think');amb('dining_hall_full',.12)
  if n==14:music('my_daily_life');amb('dining_hall_full')
 emit('label cs_check_breakfast_s%02d:'%n)
 for p in re.split(r'\n\s*\n',parts[i+2]):
  p=p.strip()
  if not p or p=='---' or p.startswith(('**[','###')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Лена Тихонова':'cs_un'}[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p
  if n==10 and text=='Мы вошли.':emit('play sound "sound/sfx/open_door_1.ogg"');bg('bg int_dining_hall_people_day');amb('dining_hall_full');music('feeling_good');emit('label cs_check_new_d2_breakfast:')
  if n==10 and text=='И почти сразу увидела Семёна.':
   group[:]=['cs_semen','cs_darya'];show();arrived=True;emit('$ cs_breakfast_un_here = cs_met_un and cs_friend_un >= 1');emit('if cs_breakfast_un_here:');lines.append('        cs_narrator '+q('Рядом с Семёном сидела Лена Тихонова. Она подняла взгляд и приветственно кивнула нам.'))
  if n==10 and text=='Я устроилась рядом с ней.':emit('label cs_check_breakfast_table:')
  if n==12 and text=='Тёзка попрощалась и направилась к выходу.':
   group[:]=['cs_semen','cs_darya'];show();emit('with Dissolve(0.7)');emit('$ cs_breakfast_un_here = False');un_departed=True
  if n==14 and text=='Затем направились к выходу.':bg('bg ext_dining_hall_near_day');amb('camp_center_day')
  if n==14 and text=='На площади постепенно собирались пионеры.':
   if not (R/'source/day02_part02.md').exists():bg('bg ext_square_day')
   emit('label cs_check_breakfast_square:')
  if speaker=='cs_th':
   if visible:clear()
   private=True
  elif speaker in ('cs_ls','cs_da','cs_sy','cs_un'):
   if n==12 and not un_departed:
    focus='cs_semen' if speaker=='cs_sy' else 'un' if speaker=='cs_un' else group[0]
    if group[0]!=focus:group[:]=[focus,'cs_darya'];show()
   if private:show();private=False
   if speaker=='cs_da':
    pose=reaction(text) or 'shrug'
    if poses['cs_darya']!=pose:poses['cs_darya']=pose;show()
   if speaker=='cs_sy':
    t=text.lower();pose='smile' if any(w in t for w in ('спасибо','почти','неплохо','отлично','усмех','проверим')) else 'thinking' if '?' in t else 'serious' if any(w in t for w in ('автобус','исчез','ворот','неизвестно')) else 'neutral'
    if poses['cs_semen']!=pose:poses['cs_semen']=pose;show()
   if speaker=='cs_un':
    pose='shy' if any(w in text.lower() for w in ('немного','наверное','да нет')) else 'surprise' if '?' in text else 'smile'
    if poses['un']!=pose:poses['un']=pose;show()
  if speaker=='cs_un' and not first_un:emit('label cs_check_breakfast_un:');first_un=True
  if n==13 and speaker=='cs_sy' and not first_sy:emit('label cs_check_breakfast_private:');first_sy=True
  emit(speaker+' '+q(text));catalog.append(dict(scene=n,speaker=speaker,text=text))
 if n==14:clear();emit('$ cs_breakfast_live = False')
 emit('return')
 (R/'days/day02/part01'/('%02d_scene.rpy'%n)).write_text('\n'.join(lines)+'\n',encoding='utf8')
(R/'source/day02_breakfast_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Breakfast replacement:',len(catalog),'source blocks in five scenes')
