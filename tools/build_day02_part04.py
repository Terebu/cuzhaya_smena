"""Part 4: power supply, ordinary medical visit, optional help, poster work."""
import re, json
from pathlib import Path
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part04.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧЕТВЁРТОЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Шурик':'cs_sh','Электроник':'cs_el','Виола':'cs_vi'}
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
folder=R/'days/day02/part04';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part03_live = False','    $ cs_part04_live = True']
 def emit(s):lines.append('    '+s)
 group=['sh','el'] if n==26 else ['cs_semen','cs_darya'] if n in (27,33) else ['cs','cs_darya'] if n in (29,30,31) else ['cs_darya']
 poses={'sh':'normal','el':'normal','cs':'normal','cs_semen':'neutral','cs_darya':'shrug'};cg=False
 def actor(t):
  if t in ('cs_darya','cs_semen'):return t+' '+poses[t]+' pioneer normal at '+('cs_darya_normal_right' if t=='cs_darya' else 'cs_semen_normal_left')
  return t+' '+poses[t]+(' pioneer' if t in ('sh','el') else ' stethoscope')+' at '+('cs_actor_right' if t=='el' else 'cs_actor_left')+' zorder 10'
 def show():
  for t in tags:
   if t not in group:emit('hide '+t)
  for t in group:emit('show '+actor(t))
  emit('$ cs_part04_cast = '+q(group))
 def bg(name):
  nonlocal cg
  cg=False;emit('scene '+name);emit('$ cs_part04_cg = False');show();emit('with Dissolve(0.8)')
 def amb(name,volume=.18):
  p='sound/ambiences/'+name+'.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(p)+':');lines.append('        play ambience '+q(p)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 def music(name,volume=.20):
  p='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(p)+':');lines.append('        play music '+q(p)+' fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="music", delay=1.0)')
 # Preserve the room and music at the part boundary; no repeated entry.
 if n==26:
  emit('if not renpy.showing("bg int_clubs_male_day"):');lines.append('        scene bg int_clubs_male_day')
  show();amb('clubs_inside_day')
  # Part 3 already queued smooth_machine with a fade. get_playing() may still
  # name the outgoing track; do not enqueue the incoming music a second time.
  emit('if renpy.music.get_playing() is None:');lines.append('        play music "sound/music/smooth_machine.ogg" fadein 2.5')
  emit('$ renpy.music.set_volume(0.20, channel="music", delay=1.0)')
 elif n==27:bg('bg ext_clubs_day');amb('camp_center_day');music('my_daily_life')
 elif n==28:bg('cs_camp_path_day');amb('camp_center_day',.13);music('my_daily_life')
 elif n==29:bg('bg int_aidpost_day');amb('medstation_inside_day',.10);music('get_to_know_me_better',.16)
 elif n==30:show();music('just_think',.14);amb('medstation_inside_day',.08)
 elif n==31:show();music('my_daily_life',.16)
 elif n==32:bg('bg ext_aidpost_day');amb('camp_center_day',.15);music('just_think',.14)
 else:bg('cs_camp_path_day');amb('camp_center_day',.18);music('my_daily_life',.20);bg('bg ext_clubs_day')
 emit('label cs_check_part04_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p
  # A few sustained reverse shots rather than a cut for every speaker.
  if n==26 and text in ('Дарья подошла к столу.','Дарья посмотрела на меня.'):group=['cs_semen','cs_darya'];show()
  if n==26 and text in ('Шурик нахмурился.','Мы ещё немного поговорили об инструментах, после чего стало ясно, что сегодня нам больше нечего здесь делать.'):group=['sh','el'];show()
  if n==27 and text=='Он кивнул и направился к площади.':group=['cs_darya'];show();emit('label cs_check_part04_semen_left:')
  if n==28 and text=='За деревьями показалось небольшое здание.':bg('bg ext_aidpost_day')
  if n==28 and text=='Я постучала.':emit('play sound "sound/sfx/knock_door7_polite.ogg"')
  if n==28 and text=='Я открыла дверь.':emit('play sound "sound/sfx/open_door_2.ogg"')
  if n==29 and text=='Виола. Можно просто по имени.':emit('$ cs_met_viola = True')
  if n==29 and text=='Через некоторое время она закончила.':emit('cs_narrator '+q('Виола закрыла царапину лёгкой повязкой.'));emit('$ cs_lena_elbow_bandaged = True')
  if n==31 and suffix=='a' and text=='Я взяла коробку.':
   cg=True;group=[];emit('scene cs_cg_lena_darya_help_viola_day');emit('$ cs_part04_cg = True');show();emit('with Dissolve(0.8)');emit('label cs_check_cg_help_viola:')
  if n==30 and text=='На стене висел анатомический плакат.':group=[];show();emit('label cs_check_part04_poster_observation:')
  if n==30 and text=='Виола заметила наш интерес.':group=['cs','cs_darya'];poses['cs_darya']='thinking';show();emit('label cs_check_part04_viola_restored:')
  if n==32 and text=='Мы спустились с крыльца.':bg('cs_camp_path_day')
  if n==33 and text=='Я села.':
   cg=True;group=[];emit('scene cs_cg_poster_planning_day');emit('$ cs_part04_cg = True');show();emit('with Dissolve(0.8)');emit('label cs_check_part04_poster_work:')
  # Narrative emotion cues as well as spoken ones; do not reset every line.
  target={'cs_da':'cs_darya','cs_sy':'cs_semen','cs_sh':'sh','cs_el':'el','cs_vi':'cs'}.get(speaker)
  if speaker=='cs_narrator' and text.startswith('Дарья'):target='cs_darya'
  pose=None
  if target=='cs_darya':pose=reaction(text,speaker=speaker)
  elif target=='cs_semen':pose='smile' if any(w in text.lower() for w in ('страшно','прекрасно','хорошо','понял','работу')) else 'thinking' if '?' in text else None
  elif target=='sh':pose='normal_smile' if text in ('Вот именно.','Договорились.') else 'serious' if 'решение' in text or 'подключить' in text else 'normal'
  elif target=='el':pose='surprise' if '?' in text else 'laugh' if 'придумаем' in text else 'grin' if 'собрали' in text else 'normal'
  elif target=='cs':pose='smile' if any(w in text.lower() for w in ('победил','спасибо','насыщенная','разумнее','разговариваешь','несколько пачек','смотри сама','до обеда')) else 'normal'
  if not cg and target in group and pose and poses[target]!=pose:poses[target]=pose;emit('show '+actor(target));emit('$ cs_part04_cast = '+q(group))
  emit(speaker+' '+q(text));catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==33:emit('$ cs_day02_part04_complete = True');emit('label cs_check_part04_work_ready:');emit('pause 0.5')
 emit('return')
 (folder/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2]
 if n==31:
  intro,a=body.split('#### Сцена 31А. Врачебная помощь наоборот',1);a,b=a.split('#### Сцена 31Б. Не будем мешать',1)
  build(n,title,intro);build(n,'Врачебная помощь наоборот',a,'a');build(n,'Не будем мешать',b,'b')
 else:build(n,title,body)
(R/'source/day02_part04_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 4:',len(catalog),'source blocks, ten files')
