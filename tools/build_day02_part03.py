"""Part 3: optional bench before leaving, then lineup and materials."""
import re,json,hashlib
from pathlib import Path
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part03.md').read_text(encoding='utf8').split('## Глобальные')[0].split('## Готовое')[0]
# The staging appendix starts after the end marker and is not spoken story.
raw=raw.split('**[КОНЕЦ ТРЕТЬЕЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Мику':'cs_mi','Славя':'cs_sl','Ольга Дмитриевна':'cs_mt'}
catalog=[]
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part03_live = True']
 def emit(text):lines.append('    '+text)
 group=['cs_darya'] if n in (21,22) else ['sl','cs_darya'] if n in (23,24) else ['cs_semen','cs_darya'];cg=False;poses={'cs_darya':'shrug','cs_semen':'neutral','sl':'normal','mt':'normal','mi':'normal'};seated=False
 def clear():
  for t in tags:emit('hide '+t)
  emit('$ cs_part03_cast = []')
 def show():
  clear()
  if cg:return
  for t in group:
   emit('show '+(t+' '+poses[t]+' pioneer at cs_actor_left zorder 10' if t in ('sl','mt','mi') else t+' '+poses[t]+' pioneer normal at '+('cs_darya_normal_right' if t=='cs_darya' else 'cs_semen_normal_left')))
  emit('$ cs_part03_cast = '+q(group))
 def bg(name):
  nonlocal cg
  cg=False;emit('scene '+name);emit('$ cs_part03_cg = False');show();emit('with Dissolve(0.8)')
 def illustration(name,checkpoint):
  nonlocal cg
  cg=True;emit('scene '+name);clear();emit('$ cs_part03_cg = True');emit('with Dissolve(0.8)');emit('label '+checkpoint+':')
 def amb(name,volume=.22):
  path='sound/ambiences/'+name+'.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(path)+':');lines.append('        play ambience '+q(path)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 def music(name='my_daily_life'):
  path='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(path)+':');lines.append('        play music '+q(path)+' fadeout 1.5 fadein 2.0');emit('$ renpy.music.set_volume(0.22, channel="music", delay=1.0)')
 if n==21:
  emit('if cs_day02_miku_listened is not True:');lines.append('        return');emit('$ cs_part02_live = False');bg('bg int_musclub_day');emit('stop music fadeout 1.0');amb('music_club_day',.10);emit('play cs_piano cs_miku_piano_track noloop fadein 0.5')
 else:
  emit('$ cs_part02_live = False');bg('bg ext_square_day' if n==22 else 'cs_camp_path_day');amb('camp_center_day');music()
 emit('label cs_check_part03_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p
  if n==21 and text=='Затем присела рядом.':group=[];show();seated=True
  if n==21 and text=='Мику закончила мелодию и подняла голову.':emit('stop cs_piano fadeout 0.8');group=['mi'];show()
  if n==21 and text=='Я наконец слезла с лавки.':group=['mi','cs_darya'];show()
  if n==22 and text=='Семён заметил нас и махнул рукой.':group=['cs_semen','cs_darya'];poses['cs_semen']='wave';show()
  if n==22 and text=='В этот момент Ольга Дмитриевна попросила всех перестать разговаривать.':illustration('cs_cg_morning_lineup_day','cs_check_cg_lineup')
  if n==22 and text=='Через несколько минут линейка закончилась.':group=['cs_darya'];bg('bg ext_square_day')
  if n==22 and text=='Семён подошёл к нам.':group=['cs_semen','cs_darya'];poses['cs_semen']='neutral';show()
  if n==24 and suffix=='a' and text=='Мы дошли до небольшой кладовой.':bg('cs_storage_ext_day')
  if n==24 and suffix=='a' and text=='Славя открыла дверь.':emit('play sound "sound/sfx/open_door_2.ogg"');bg('cs_storage_int_day');amb('int_cabin_day',.15);emit('label cs_check_part03_storage:')
  if n==24 and suffix=='a' and text=='Мы направились обратно к дорожке.':group=['cs_semen','cs_darya'];bg('cs_camp_path_day');amb('camp_center_day')
  if n==24 and suffix=='b' and text=='Она направилась к кладовой.':group=['cs_semen','cs_darya'];show()
  if n==25 and text=='Возле клубов мы нашли стол под навесом.':bg('bg ext_clubs_day')
  if n==25 and text=='Дарья разложила бумагу, прижав края ладонями.':illustration('cs_cg_poster_planning_day','cs_check_cg_poster_planning')
  if n==25 and text=='Семён подошёл к двери.':bg('bg ext_clubs_day')
  # Stable companions, occasional deliberate focus for a third speaker.
  if not cg and n in (23,24) and speaker in ('cs_sy','cs_sl'):
   target='cs_semen' if speaker=='cs_sy' else 'sl'
   if group and group[0]!=target:group=[target,'cs_darya'];show()
  target={'cs_da':'cs_darya','cs_sy':'cs_semen','cs_sl':'sl','cs_mi':'mi'}.get(speaker)
  if not cg and target in group:
   if target=='cs_darya':pose=reaction(text) or 'shrug'
   elif target=='cs_semen':pose='smile' if any(w in text.lower() for w in ('удобно','пожалуйста','поддерж','понят')) else 'thinking' if '?' in text else 'neutral'
   else:pose='surprise' if '?' in text else 'smile'
   if poses[target]!=pose:poses[target]=pose;show()
  alternatives={
   'С Мику мы уже познакомились. Она как раз репетировала утром.':'С Мику мы уже познакомились. Она готовилась к утренней репетиции.',
   'Да. Мы немного послушали.':'Да. Она показала нам кружок.'}
  if n==24 and suffix=='a' and text in alternatives:
   emit('if cs_day02_miku_listened:');lines.append('        '+speaker+' '+q(text));emit('else:');lines.append('        '+speaker+' '+q(alternatives[text]))
  else:emit(speaker+' '+q(text))
  catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==21:emit('stop cs_piano fadeout 1.0');emit('$ cs_part03_live = False');emit('$ cs_part02_live = True')
 if n==25:group=['cs_semen','cs_darya'];bg('bg int_clubs_male_day');amb('clubs_inside_day',.18);music('smooth_machine');emit('label cs_check_part03_clubs:');emit('pause 0.5');emit('$ cs_part03_live = False')
 emit('return')
 (R/'days/day02/part03'/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2]
 if n==24:
  a,b=body.split('#### Сцена 24Б. У каждого свои дела',1);a=a.split('#### Сцена 24А. Вместе быстрее',1)[1];build(n,'Вместе быстрее',a,'a');build(n,'У каждого свои дела',b,'b')
 else:build(n,title,body)
(R/'source/day02_part03_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
assets=['bg/storage/ext_storage_day.png','bg/storage/int_storage_day.png','cg/square/cg_morning_lineup_day.png','cg/event/cg_poster_planning_day.png']
(R/'source/day02_part03_assets.json').write_text(json.dumps([dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest()) for p in assets],indent=2),encoding='utf8')
print('Part 3:',len(catalog),'blocks, six scene/branch files')
