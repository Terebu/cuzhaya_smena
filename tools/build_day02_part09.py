"""Automatic friendship consequences, no menus or score mutations."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part09.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧАСТИ 9 ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Женя':'cs_mz','Славя':'cs_sl','Мику':'cs_mi'}
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
folder=R/'days/day02/part09';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1];body=parts[i+2]
 if n==64 and (R/'source/day02_part09_dinner_revised.md').exists():continue
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d:'%n,'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part08_live = False','    $ cs_part09_live = True']
 indent='    ';group=['cs_zhenya','cs_darya'] if n in (62,63) else ['cs_darya'];mode='pair';poses={'cs_darya':'shrug','cs_zhenya':'normal','cs_semen':'neutral','sl':'normal','mi':'normal'}
 def emit(s):lines.append(indent+s)
 def actor(t,g):
  triple=len(g)==3
  if t=='cs_darya':return 'cs_darya '+poses[t]+' pioneer '+('far at cs_darya_far_right' if triple else 'normal at cs_darya_normal_right')
  if t=='cs_zhenya':return 'cs_zhenya '+poses[t]+' pioneer '+('far at cs_darya_far_left' if triple else 'normal at cs_darya_normal_left')
  if t=='cs_semen':return 'cs_semen '+poses[t]+' pioneer '+('far at cs_semen_far_center' if triple else 'normal at cs_semen_normal_left')
  return t+' '+poses[t]+' pioneer at cs_actor_left'
 def stage(g):
  for t in tags:
   if t not in g:emit('hide '+t)
  for t in g:emit('show '+actor(t,g))
  emit('$ cs_part09_cast = '+q(g))
 def show():
  global indent
  if mode in ('dinner','semen'):
   emit('if cs_friend_mz >= 1:');old=indent;indent+='    ';stage(['cs_zhenya']+(['cs_semen'] if mode=='semen' else [])+['cs_darya']);indent=old;emit('else:');indent+='    ';stage((['cs_semen'] if mode=='semen' else [])+['cs_darya']);indent=old
  else:stage(group)
 def bg(name):emit('scene '+name);show();emit('with Dissolve(0.8)')
 def music(name):
  emit('if renpy.music.get_playing() != '+q('sound/music/'+name+'.ogg')+':');lines.append(indent+'    play music '+q('sound/music/'+name+'.ogg')+' fadeout 2.0 fadein 2.0');emit('$ renpy.music.set_volume(0.14, channel="music", delay=1.0)')
 def amb(name,vol=.15):emit('play ambience '+q('sound/ambiences/'+name+'.ogg')+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(vol)+', channel="ambience", delay=1.0)')
 if n==60:show();music('my_daily_life');emit('play sound "sound/sfx/dinner_horn_processed.ogg"')
 elif n==61:bg('bg ext_dining_hall_near_day')
 elif n==62:bg('bg int_dining_hall_people_day');amb('dining_hall_full',.16);music('just_think')
 elif n==63:bg('bg int_dining_hall_people_day');amb('dining_hall_full',.18);music('my_daily_life')
 elif n==64:mode='dinner';show();emit('stop music fadeout 2.0')
 elif (R/'source/day02_part09_dinner_revised.md').exists():emit('$ sunset_time()');emit('$ persistent.sprite_time = "sunset"');show();music('lets_be_friends')
 else:emit('$ sunset_time()');emit('$ persistent.sprite_time = "sunset"');bg('bg ext_dining_hall_near_sunset');amb('camp_center_evening',.13);music('lets_be_friends')
 emit('label cs_check_part09_s%02d:'%n)
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if p.startswith('**[ЕСЛИ `'):
   cond=re.search(r'`([^`]+)`',p)[1];indent='    ';emit('if '+cond+':');indent='        '
   continue
  if p.startswith('**[ИНАЧЕ ЕСЛИ'):
   cond=re.search(r'`([^`]+)`',p)[1];indent='    ';emit('elif '+cond+':');indent='        ';continue
  if p.startswith('**[ИНАЧЕ'):
   indent='    ';emit('else:');indent='        ';continue
  if p.startswith('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):indent='    ';continue
  if p.startswith('**[ТЕХНИЧЕСКИЙ ФЛАГ:') and 'cs_sl_good_seats' in p:emit('$ cs_sl_good_seats = '+('False' if 'False' in p else 'True'));continue
  if p.startswith('**[УСЛОВНЫЙ ФЛАГ:'):emit('$ cs_mi_intro_revised = '+('False' if 'False' in p else 'True'));continue
  if not p or p=='---' or p.startswith(('#','**[','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if n==61 and text=='Затем Женя заметила мой локоть.':
   emit('if cs_mz_quiet_visit_seen:');lines.append('        cs_narrator '+q('Женя посмотрела на повязку и снова напомнила беречь локоть.'));lines.append('        cs_ls '+q('Помню. Смотрю под ноги.'));emit('else:');indent='        '
  if n==61 and text=='Изнутри столовой донёсся голос, приглашавший проходить к раздаче.':indent='    '
  if n==61 and text=='Женя подняла взгляд от книги.':group=['cs_zhenya','cs_darya'];show();emit('label cs_check_part09_zhenya_greeting:')
  if n==64 and text=='Женя направилась к знакомым за дальний стол.':mode='pair';group=['cs_darya'];show()
  if n==64 and text=='Я принялась за ужин.':mode='dinner';show();emit('label cs_check_part09_dinner:')
  if n==64 and text=='В этот момент мимо нашего столика проходил Семён.':mode='semen';show();emit('label cs_check_part09_semen:')
  if n==64 and text=='Семён попрощался и направился к выходу.':mode='dinner';show();emit('label cs_check_part09_semen_left:')
  if n==65 and text=='На площади заметно прибавилось народу.':
   if not (R/'source/day02_part09_dinner_revised.md').exists():bg('bg ext_square_sunset')
   emit('label cs_check_part09_square:')
  if n==65 and text=='В этот момент к нам подошла Славя.':group=['sl','cs_darya'];show();emit('label cs_check_part09_slavya:')
  if n==65 and text=='Славя отправилась помогать остальным.':group=['cs_darya'];show();emit('label cs_check_part09_seats:')
  if n==65 and text=='Увидев нас, Мику сразу оживилась.':group=['mi','cs_darya'];poses['mi']='smile';show();emit('label cs_check_part09_miku:')
  if n==65 and text=='Она помахала нам и поспешила обратно.':group=['cs_darya'];show()
  if speaker=='cs_da':
   pose=reaction(text,speaker=speaker)
   if pose and pose!=poses['cs_darya']:poses['cs_darya']=pose;show()
  if speaker=='cs_mz':poses['cs_zhenya']='glasses_touch' if 'каталог' in text else 'thinking' if '?' in text else 'arms_crossed' if 'не говорю' in text or 'не знаю' in text else 'explaining' if len(text)>85 else 'normal';show()
  if speaker=='cs_sy':poses['cs_semen']='grateful' if 'увидимся' in text else 'explaining' if len(text)>85 else 'thinking' if '?' in text else 'smile';show()
  if speaker=='cs_sl':poses['sl']='shy' if 'решила' in text else 'smile';show()
  if speaker=='cs_mi':poses['mi']='shy' if 'волнуюсь' in text else 'smile';show()
  if n==65 and text=='Когда мы вышли из столовой, солнце уже клонилось к деревьям.' and (R/'source/day02_part09_dinner_revised.md').exists():emit(speaker+' '+q('К этому времени солнце уже клонилось к деревьям.'))
  elif n==65 and text=='Ну, вы ведь утром помогли с материалами. Да и ты сегодня поранилась. Я решила, что так будет удобнее.':
   emit('if cs_helped_sl_day2:');lines.append(indent+'    '+speaker+' '+q(text));emit('else:');lines.append(indent+'    '+speaker+' '+q('Мы ведь уже успели познакомиться. А сегодня ты поранилась. Я решила, что так будет удобнее.'))
  else:emit(speaker+' '+q(text))
  catalog.append(dict(scene=n,speaker=speaker,text=text))
  if n==64 and text=='Мы доели ужин.':
   emit('if cs_friend_mz >= 1:');lines.append(indent+'    cs_mz '+q('До завтра.'));lines.append(indent+'    cs_narrator '+q('Женя взяла книгу и, попрощавшись с нами, направилась к выходу.'));mode='pair';group=['cs_darya'];show()
 indent='    '
 if n==62:emit('$ cs_mz_map_lead = True');emit('label cs_check_part09_map_lead:');emit('pause 0.5')
 if n==65:emit('stop music fadeout 3.0');emit('$ cs_day02_part09_complete = True');emit('label cs_check_part09_ready:');emit('pause 0.5')
 emit('return');(folder/('%02d_scene.rpy'%n)).write_text('\n'.join(lines)+'\n',encoding='utf8')
(R/'source/day02_part09_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 9:',len(catalog),'source blocks in six scene files')

# Finale starts at the dining-hall exit; seating is called after the book return.
if (R/'source/day02_part10.md').exists():
 p=R/'days/day02/part09/65_scene.rpy'
 s=p.read_text(encoding='utf8').replace('    $ cs_part09_live = True','    $ cs_part09_live = True\n    $ cs_day02_seating_done = True\n    scene bg ext_square_sunset\n    with Dissolve(0.8)',1)
 p.write_text(s,encoding='utf8')
