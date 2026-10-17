"""New second day: only the supplied ten-scene first instalment."""
import re,json
from pathlib import Path
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_new_part01.md').read_text(encoding='utf8').split('## Что передать Codex')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
tags=['cs_darya','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
q=lambda t:json.dumps(t,ensure_ascii=False)
catalog=[]
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2].split('### Продолжение первой части')[0]
 if n==10 and (R/'source/day02_breakfast.md').exists():continue
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d:'%n,'    $ save_name = '+q('Чужая смена — День 2: '+title)]
 def emit(s):lines.append('    '+s)
 visible=[];group=[];poses={};private=False;uniform=n>=9;portrait_checkpoint=False
 def clear():
  for tag in tags:emit('hide '+tag)
  visible.clear()
 def show():
  clear()
  for tag in group:
   pose=poses.get(tag,'shrug' if tag=='cs_darya' else 'neutral' if tag=='cs_semen' else 'normal')
   if tag=='mt':emit('show mt '+pose+' pioneer at cs_actor_right')
   else:emit('show '+tag+' '+pose+' pioneer normal at '+('cs_darya_normal_center' if len(group)==1 and tag=='cs_darya' else 'cs_darya_normal_right' if tag=='cs_darya' else 'cs_semen_normal_left'))
  visible[:]=group
 def bg(name,morning=False):
  emit('scene '+name+(' at cs_early_morning' if morning else ''));show();emit('with Dissolve(0.8)')
 def music(name):emit('play music "sound/music/'+name+'.ogg" fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume(0.22, channel="music", delay=1.0)')
 def amb(name):emit('play ambience "sound/ambiences/'+name+'.ogg" fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)')
 starts={1:'cs_house_lena_darya_int_day',2:'cs_house_lena_darya_int_day',3:'cs_house_lena_darya_ext_day',4:'cs_camp_path_day',5:'cs_camp_path_day',6:'bg ext_house_of_mt_day',7:'cs_house_lena_darya_ext_day',8:'cs_house_lena_darya_int_day',9:'cs_camp_path_day',10:'bg ext_dining_hall_near_day'}
 bg(starts[n],n<=5)
 amb('forest_day' if n<=5 else 'int_cabin_day' if n in (7,8) else 'camp_center_day')
 if n==1:emit('stop music fadeout 1.0')
 if n in (2,6,7):music('my_daily_life')
 if n in (3,9,10):music('feeling_good')
 if n in (5,8):emit('stop music fadeout 2.0')
 emit('label cs_check_new_d2_s%02d:'%n)
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('**[','###')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:
   who=m[1].split(' (')[0];text=m[2].strip();speaker={'Лена':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Ольга Дмитриевна':'cs_mt'}[who]
  elif p.startswith('*') and p.endswith('*'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p
  # Explicit entrances and geography; a sleeping or undressed Darya stays off camera.
  if n==4 and text=='Я пробежала мимо площади.':bg('bg ext_square_day',True)
  if n==4 and text=='Затем свернула к столовой.':bg('bg ext_dining_hall_near_day',True)
  if n==4 and text=='Дальше показались клубы.':bg('bg ext_clubs_day',True)
  if n==4 and text=='И через несколько минут увидела турники.':bg('bg ext_playground_day',True);emit('label cs_check_new_d2_sport:')
  if n==5 and text=='И остановилась.':bg('bg ext_camp_entrance_day',True);music('into_the_unknown');emit('label cs_check_new_d2_gate:')
  if n==5 and text=='Передо мной лежала дорога.':bg('bg ext_no_bus',True)
  if n==7 and text=='Я осторожно вошла в домик.':bg('cs_house_lena_darya_int_day')
  if n==8 and text=='В этот момент снаружи раздался горн.':emit('play sound "sound/sfx/dinner_horn_processed.ogg"')
  if n==8 and text=='Мы вышли на крыльцо.':bg('cs_house_lena_darya_ext_day');amb('camp_center_day');music('feeling_good')
  if n==9 and text=='Умывальники нашлись без особых приключений.':group[:]=['cs_darya'];bg('bg ext_washstand_day');emit('label cs_check_new_d2_wash:')
  if n==10 and text=='Мы взяли подносы и нашли свободный столик.':group[:]=['cs_semen','cs_darya'];bg('bg int_dining_hall_people_day');amb('dining_hall_full');emit('label cs_check_new_d2_breakfast:')
  if n==4 and text=='На дорожке стояла Ольга Дмитриевна.':emit('$ cs_olga_seen = True');group[:]=['mt'];show()
  if n==6 and text=='И почти сразу увидела Семёна.':group[:]=['cs_semen'];show()
  if n==8 and text=='Дарья взяла полотенце.':
   emit('cs_narrator '+q('Даша уже переоделась в пионерскую форму. Я пока осталась в спортивной одежде: чистую рубашку решила надеть после умывания.'))
   uniform=True;group[:]=['cs_darya'];show()
  if n==6 and speaker=='cs_sy' and group!=['cs_semen']:group[:]=['cs_semen'];show()
  if n==10 and speaker=='cs_sy' and not group:group[:]=['cs_semen','cs_darya'];show()
  if text in ('Она пошла дальше по дорожке.','Я продолжила путь.') and n in (4,6):group.clear();clear();emit('with Dissolve(0.4)')
  if speaker=='cs_th':
   if visible:clear()
   private=True
  elif speaker in ('cs_ls','cs_da','cs_sy','cs_mt'):
   if private:show();private=False
   if speaker=='cs_mt':
    pose='smile' if any(w in text.lower() for w in ('молодец','хорошо','работа','как думала')) else 'surprise' if '?' in text else 'normal'
    if poses.get('mt')!=pose:poses['mt']=pose;show()
   if speaker=='cs_sy' and 'cs_semen' in group:
    pose='smile' if any(w in text.lower() for w in ('отлично','заметил','увидимся','пробеж')) else 'thinking' if '?' in text else 'neutral'
    if poses.get('cs_semen')!=pose:poses['cs_semen']=pose;show()
   if speaker=='cs_da' and uniform and 'cs_darya' in group:
    pose=reaction(text) or 'shrug'
    if poses.get('cs_darya')!=pose:poses['cs_darya']=pose;show()
  if not portrait_checkpoint and ((n==4 and speaker=='cs_mt' and group==['mt']) or (n==6 and speaker=='cs_sy')):
   emit('label cs_check_new_d2_'+('olga' if n==4 else 'semen')+':');portrait_checkpoint=True
  emit(speaker+' '+q(text));catalog.append(dict(scene=n,speaker=speaker,text=text))
 if n==2:emit('play sound "sound/sfx/close_door_1.ogg"');emit('stop music fadeout 2.0')
 if n==5:emit('stop music fadeout 3.0')
 if n==9:
  clear();emit('window hide dissolve');emit('scene black with dissolve');emit('pause 0.5');emit('window show dissolve');emit('cs_narrator '+q('Вернувшись в домик, мы переоделись в пионерскую форму и убрали полотенца. Потом вместе пошли к столовой.'))
  music('my_daily_life')
 if n==10:emit('stop music fadeout 2.0');clear()
 emit('return')
 (R/'days/day02/part01'/('%02d_scene.rpy'%n)).write_text('\n'.join(lines)+'\n',encoding='utf8')
(R/'source/day02_new_part01_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Ten new scenes:',len(catalog),'source blocks')
if (R/'source/day02_breakfast.md').exists():
 import runpy
 runpy.run_path(str(R/'tools/build_day02_breakfast.py'))
