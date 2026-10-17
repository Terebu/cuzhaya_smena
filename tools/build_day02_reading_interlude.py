"""A quiet library visit between 59 and 60. Full PNGs, explicit viewpoint changes."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_reading_interlude.md').read_text(encoding='utf8').split('**[КОНЕЦ ИНТЕРЛЮДИИ.]**')[0]
parts=re.split(r'### Сцена 59\.(\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz'}
tags=['cs_darya','cs_zhenya','cs_semen','mz','un','mi','dv','sl','us','mt','sh','el','cs','cs_dasha_winter','cs_dasha_pioneer']
folder=R/'days/day02/reading_interlude';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
def build(n,title,body,branch=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_reading_%02d%s:'%(n,branch),'    $ save_name = '+q('Чужая смена — Тишина на троих: '+title),'    $ cs_part08_live = False','    $ cs_reading_live = True']
 indent='    ';group=['cs_darya'] if n in (1,6,8,9) else ['cs_zhenya'] if n in (4,) else ['cs_zhenya','cs_darya'] if n==7 else []
 poses={'cs_darya':'neutral','cs_zhenya':'normal'}
 def emit(s):lines.append(indent+s)
 def show():
  for t in tags:
   if t not in group:emit('hide '+t)
  for t in group:emit('show '+t+' '+poses[t]+' pioneer normal at '+('cs_darya_normal_right' if t=='cs_darya' else 'cs_darya_normal_left'))
  emit('$ cs_reading_cast = '+q(group))
 def remove(t):
  if t in group:group.remove(t)
  emit('hide '+t);emit('$ cs_reading_cast = '+q(group))
 def bg(name):emit('scene '+name);show();emit('with Dissolve(0.8)')
 if n==1:
  show();emit('play music "sound/music/my_daily_life.ogg" fadein 2.0');emit('$ renpy.music.set_volume(0.11, channel="music", delay=1.0)')
 elif n==2:
  bg('bg int_library_day');emit('stop music fadeout 2.0');emit('play ambience "sound/ambiences/library_day.ogg" fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume(0.055, channel="ambience", delay=1.0)')
 elif n==9:
  bg('bg ext_library_day');emit('$ cs_reading_book_location = "lena_hand"');emit('play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)');emit('play music "sound/music/a_promise_from_distant_days.ogg" fadein 2.5');emit('$ renpy.music.set_volume(0.12, channel="music", delay=1.0)')
 else:show()
 emit('label cs_check_reading_%02d%s:'%(n,branch))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if p.startswith('**[ЕСЛИ `'):indent='    ';emit('if '+re.search(r'`([^`]+)`',p)[1]+':');indent='        ';continue
  if p.startswith('**[ИНАЧЕ ЕСЛИ'):indent='    ';emit('elif '+re.search(r'`([^`]+)`',p)[1]+':');indent='        ';continue
  if p.startswith('**[ИНАЧЕ'):indent='    ';emit('else:');indent='        ';continue
  if p.startswith('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):indent='    ';continue
  if not p or p=='---' or p.startswith(('#','**[')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if n==8 and text=='Мы направились к выходу.':indent='    '
  if n==1 and text=='Впереди виднелась библиотека.':bg('bg ext_library_day')
  if n==1 and text=='Дарья направилась к домикам.':remove('cs_darya');emit('label cs_check_reading_darya_left:')
  if n==2 and text=='Я осторожно достала второй.':emit('$ cs_reading_book_id = "zhenya_second_copy"');emit('$ cs_reading_book_location = "reading_room"')
  if n==3 and text=='Женя стояла напротив.':group=['cs_zhenya'];show();emit('label cs_check_reading_zhenya_approached:')
  if n==4 and ((branch=='a' and text=='Она направилась к своему столу.') or (branch=='b' and text=='И вернулась за стол.') or (branch=='c' and text=='И вернулась к работе.')):remove('cs_zhenya')
  if n==5 and text=='На пороге стояла Дарья.':group=['cs_darya'];show();emit('label cs_check_reading_darya_returned:')
  if n==5 and text=='Даша подошла к библиотекарше.':remove('cs_darya')
  if n==5 and text=='Вернулась ко мне.':group=['cs_darya'];show()
  if n==6 and text=='И услышала голос Жени.':group=['cs_zhenya','cs_darya'];show();emit('label cs_check_reading_three:')
  if n==7 and ((branch=='a' and text=='И вернулась к своему столу.') or (branch=='b' and text=='Она вернулась к работе.') or (branch=='c' and text=='Женя вернулась за свой стол.')):remove('cs_zhenya')
  if n==8 and text=='Я подошла к столу библиотекарши.':group=['cs_zhenya','cs_darya'];show();emit('label cs_check_reading_checkout:')
  if speaker=='cs_da' and 'cs_darya' in group:
   pose=reaction(text,speaker=speaker)
   if pose and pose!=poses['cs_darya']:poses['cs_darya']=pose;show()
  if speaker=='cs_mz' and 'cs_zhenya' in group:
   pose='glasses_touch' if any(w in text for w in ('книг','читай','заклад')) else 'thinking' if '?' in text else 'explaining' if len(text)>95 else 'thoughtful' if n in (6,7,8) else 'normal'
   if pose!=poses['cs_zhenya']:poses['cs_zhenya']=pose;show()
  emit(speaker+' '+q(text));catalog.append(dict(scene=n,branch=branch,speaker=speaker,text=text))
  if n==2 and text=='Я осторожно достала второй.':emit('cs_narrator '+q('Между страницами лежала бумажная полоска. Я оставила её для закладки.'))
  if n==3 and text=='Но я снова опустила глаза к книге.':emit('$ cs_mz_quiet_visit_seen = True')
  if n==7 and branch=='c' and text=='И, пожалуй, именно от Жени оно значило особенно много.':emit('$ cs_mz_reading_invite = True');emit('label cs_check_reading_invited:')
  if n==8 and text=='Женя внесла их в журнал.':emit('$ cs_reading_book_borrowed = True');emit('$ cs_reading_book_location = "lena_hand"');emit('label cs_check_reading_borrowed:')
 indent='    '
 if n in (4,7):emit('label cs_check_reading_desk_%02d%s:'%(n,branch));emit('pause 0.5')
 if n==9:emit('stop music fadeout 2.0');emit('label cs_check_reading_walk_done:');emit('pause 0.5')
 emit('return');(folder/('59_%02d%s_scene.rpy'%(n,branch))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1];body=parts[i+2]
 if n in (4,7):
  branches=re.split(r'#### Если `[^`]+`\s*',body)
  for branch,b in zip(('a','b','c'),branches[1:]):build(n,title,b,branch)
 else:build(n,title,body)
(R/'source/day02_reading_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Reading interlude:',len(catalog),'source blocks, thirteen files')
