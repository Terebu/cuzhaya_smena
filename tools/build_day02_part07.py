"""A second, distinct injury and clinic visit; no repeat first meeting."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part07.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧАСТИ 7 ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Виола':'cs_vi'}
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
folder=R/'days/day02/part07';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part06_live = False','    $ cs_part07_live = True']
 def emit(s):lines.append('    '+s)
 group=['cs','cs_darya'] if n in (50,51) else ['cs_darya'];pose='smile' if n in (47,53) else 'worried';viola=None;vpose='normal';seated=n in (50,51)
 def actor(t):
  if t=='cs_darya':return 'cs_darya '+pose+' pioneer normal at cs_darya_normal_right'
  return 'cs custom '+viola+' medical normal at cs_viola_normal_left zorder 10' if viola else 'cs '+vpose+' stethoscope at cs_actor_left zorder 10'
 def show():
  for t in tags:
   if t not in group:emit('hide '+t)
  for t in group:emit('show '+actor(t))
  emit('$ cs_part07_cast = '+q(group))
 def bg(name):emit('scene '+name);show();emit('with Dissolve(0.8)')
 def amb(name,volume=.13):
  p='sound/ambiences/'+name+'.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(p)+':');lines.append('        play ambience '+q(p)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 def music(name,volume=.17):
  p='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(p)+':');lines.append('        play music '+q(p)+' fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="music", delay=1.0)')
 if n==47:
  show();amb('camp_center_day');music('my_daily_life')
  emit('if cs_met_viola and cs_lena_elbow_injury_day2 == 0:');lines+=['        $ cs_lena_elbow_bandaged = True','        $ cs_lena_elbow_injury_day2 = 1']
 elif n==48:show()
 elif n==49:bg('bg ext_aidpost_day');amb('camp_center_day');emit('stop music fadeout 0.5')
 elif n==50:viola='warm_smile';show();music('my_daily_life',.13)
 elif n==51:viola='thoughtful';show();emit('with cs_sprite_change')
 elif n==52:bg('bg ext_aidpost_day');amb('camp_center_day');music('a_promise_from_distant_days',.15)
 else:show()
 emit('label cs_check_part07_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if n==48 and text=='В следующую секунду земля внезапно оказалась значительно ближе, чем предполагалось.':emit('stop music fadeout 0.5');emit('play sound "sound/sfx/bodyfall_1.ogg"');pose='worried';show();emit('$ cs_lena_elbow_injury_day2 = 2');emit('$ cs_lena_bandage_damaged = True');emit('label cs_check_part07_fall:')
  if n==48 and text=='Присела рядом.':seated=True;show();emit('label cs_check_part07_injury_focus:')
  if n==48 and text=='Я осторожно поднялась с её помощью.':seated=False;show();emit('label cs_check_part07_standing:')
  if n==49 and text=='Дарья постучала.':emit('play sound "sound/sfx/knock_door7_polite.ogg"')
  if n==49 and text=='Она открыла дверь.':group=['cs','cs_darya'];bg('bg int_aidpost_day');amb('medstation_inside_day',.10);emit('label cs_check_part07_clinic:')
  if n==49 and text=='Виола вздохнула.':viola='eyes_closed';emit('show '+actor('cs'));emit('$ cs_part07_cast = '+q(group))
  if n==49 and text=='Виола начала осторожно промывать ссадину.':viola='serious';emit('show '+actor('cs'));emit('$ cs_part07_cast = '+q(group));emit('label cs_check_part07_treatment:')
  if n==49 and text=='Дарья села рядом, не мешая Виоле работать.':seated=True;show();emit('label cs_check_part07_seated:')
  if n==50 and text=='Повреждённый участок закрывала свежая повязка.':emit('$ cs_lena_elbow_bandaged = True');emit('$ cs_lena_bandage_damaged = False');emit('$ cs_lena_no_sport_day2 = True');pose='neutral';show();emit('label cs_check_part07_bandaged:')
  if n==51 and suffix=='b' and text=='Я осторожно поднялась с кушетки.':seated=False;show()
  if n==52 and text=='Мы медленно спустились с крыльца.':bg('cs_camp_path_day')
  # Authorial cues, not a speaker-hiding callback. Darya stays worried until care.
  newpose=None
  if speaker=='cs_da' or (speaker=='cs_narrator' and text.startswith('Дарья')):newpose=reaction(text,speaker=speaker)
  if n in (48,49) and newpose not in ('serious','reaching'):newpose='worried' if newpose else None
  if newpose and pose!=newpose and 'cs_darya' in group:pose=newpose;emit('show '+actor('cs_darya'));emit('$ cs_part07_cast = '+q(group))
  if speaker=='cs_vi' and 'cs' in group:
   if n==49:
    newvi='surprised' if text=='Лена?' else 'serious' if any(w in text.lower() for w in ('круж','сознание','удар','ссадин','терпи')) else 'explaining' if len(text)>75 else 'thoughtful'
   else:
    newvi='arms_crossed' if 'пробежек' in text else 'stern' if 'с повязкой' in text or 'на сегодня' in text.lower() else 'amused' if any(w in text.lower() for w in ('разговорчив','правда','дважды','бегать')) else 'warm_smile' if any(w in text.lower() for w in ('люблю','работаю','замечательно','люблю','не за что','спасибо')) else 'explaining' if len(text)>80 else 'thoughtful'
   if viola!=newvi:viola=newvi;emit('show '+actor('cs'));emit('$ cs_part07_cast = '+q(group))
  if n==49 and text=='Удивительно. Женя, Славя, теперь Виола. У Даши стремительно растёт профессиональная репутация.':
   emit('if cs_met_mz:');lines.append('        '+speaker+' '+q(text));emit('else:');lines.append('        '+speaker+' '+q('Удивительно. Славя, теперь Виола. У Даши стремительно растёт профессиональная репутация.'))
  else:emit(speaker+' '+q(text))
  catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==53:emit('stop music fadeout 3.0');amb('camp_center_day',.18);emit('$ cs_day02_part07_complete = True');emit('label cs_check_part07_ready:');emit('pause 0.5')
 emit('return')
 (folder/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2]
 if n==51:
  intro,a=body.split('#### Сцена 51А. Не только пациенты',1);a,b=a.split('#### Сцена 51Б. Хватит приключений',1)
  build(n,title,intro);build(n,'Не только пациенты',a,'a');build(n,'Хватит приключений',b,'b')
 else:build(n,title,body)
(R/'source/day02_part07_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 7:',len(catalog),'source blocks, nine scene/branch files')
