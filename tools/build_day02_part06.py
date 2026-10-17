"""A road experiment, two independently guarded trust choices, no supernatural reveal."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part06.md').read_text(encoding='utf8').split('**[КОНЕЦ ШЕСТОЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Ольга Дмитриевна':'cs_mt'}
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
folder=R/'days/day02/part06';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part05_live = False','    $ cs_part06_live = True']
 def emit(s):lines.append('    '+s)
 group=['cs_darya'] if n==40 else ['cs_semen','cs_darya'];poses={'cs_darya':'shrug','cs_semen':'neutral','mt':'normal'}
 road=n in (43,44);focus=False
 def actor(t):
  if len(group)==3:
   if t=='mt':return 'mt '+poses[t]+' pioneer far at cs_actor_far_left zorder 10'
   if t=='cs_semen':return t+' '+poses[t]+' pioneer far at cs_semen_far_center'
   return t+' '+poses[t]+' pioneer far at cs_darya_far_right'
  if t=='cs_darya':return t+' '+poses[t]+' pioneer '+('far at cs_darya_far_left' if road else 'normal at cs_darya_normal_right')
  return t+' '+poses[t]+' pioneer '+('far at cs_semen_far_center' if road else 'normal at cs_semen_normal_left')
 def show():
  for t in tags:
   if t not in group:emit('hide '+t)
  for t in group:emit('show '+actor(t))
  emit('$ cs_part06_cast = '+q(group))
 def bg(name):
  emit('scene '+name);show();emit('with Dissolve(0.8)')
 def route(name,key):
  # A background-only substitution preserves both companions and their scale.
  emit('hide cs_road_powerlines_day');emit('hide cs_road_right_bend_day');emit('hide cs_road_marked_verge_day');emit('hide cs_road_left_bend_day')
  emit('show '+name+' behind cs_darya, cs_semen');emit('with Dissolve(0.8)')
  emit('$ cs_road_visual_trace.append('+q(key)+')');emit('label cs_check_part06_'+key+':')
 def amb(name,volume=.15):
  p='sound/ambiences/'+name+'.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(p)+':');lines.append('        play ambience '+q(p)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 def music(name,volume=.16):
  p='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(p)+':');lines.append('        play music '+q(p)+' fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="music", delay=1.0)')
 if n==40:bg('bg ext_dining_hall_near_day');amb('camp_center_day');music('my_daily_life')
 elif n==41:show();music('just_think')
 elif n==42:bg('cs_camp_path_day');amb('camp_center_day');emit('stop music fadeout 2.0');emit('$ cs_road_visual_trace = []');emit('$ cs_road_loop_observations = 0')
 elif n==43:show();amb('forest_day',.15);music('into_the_unknown',.11)
 elif n==44:show();music('waltz_of_doubts',.12);amb('forest_day',.10)
 elif n==45:bg('bg ext_camp_entrance_day');amb('camp_center_day');emit('stop music fadeout 2.0')
 else:bg('cs_camp_path_day');amb('camp_center_day');music('just_think')
 emit('label cs_check_part06_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if n==40 and text=='Мы вошли внутрь.':bg('bg int_dining_hall_people_day');amb('dining_hall_full',.20)
  if n==40 and text=='В этот момент возле столика появился Семён с подносом.':group=['cs_semen','cs_darya'];show();emit('label cs_check_part06_semen_arrived:')
  if n==42 and text=='Я и Дарья зашли в наш домик за водой.':group=['cs_darya'];bg('cs_house_lena_darya_int_day');amb('int_cabin_day',.12)
  if n==42 and text=='Через несколько минут мы дошли до ворот.':group=['cs_semen','cs_darya'];bg('bg ext_camp_entrance_day');amb('camp_entrance_day',.15)
  if n==42 and text=='Никакого автобуса.':bg('bg ext_no_bus');emit('label cs_check_part06_empty_bus_stop:')
  if n==42 and text=='Мы прошли под вывеской «Совёнок».':bg('bg ext_no_bus')
  if n==42 and text=='Мы продолжили путь.':
   road=True;bg('bg ext_road_day');amb('forest_day',.15)
  if n==42 and text=='Только дорога.':
   emit('cs_narrator '+q('Лес у дороги начал редеть. Впереди открылись поля, а над асфальтом тянулись провода ЛЭП.'))
   bg('cs_road_powerlines_day');emit('$ cs_road_visual_trace.append("approach")')
  if n==43 and text=='Аккуратно закрепила её на тонкой ветке.':route('cs_road_marked_verge_day','control_created')
  if n==43 and text=='Мы отправились дальше.':route('cs_road_powerlines_day','lap1_a')
  if n==43 and text=='Иногда слегка изгибалась, но крупных поворотов не было.':route('cs_road_left_bend_day','lap1_b')
  if n==43 and text=='Через несколько минут он произнёс:':route('cs_road_right_bend_day','lap1_c')
  if n==43 and text=='На ветке висела моя резинка.':route('cs_road_marked_verge_day','lap1_return');emit('$ cs_road_loop_observations = 1');emit('$ renpy.music.set_volume(0.18, channel="music", delay=1.5)')
  if n==44 and text=='Мы снова пошли вперёд.':route('cs_road_powerlines_day','lap2_a')
  if n==44 and text=='На одном участке дорога слегка изгибалась влево.':route('cs_road_left_bend_day','lap2_b')
  if n==44 and text=='Небольшая неровность асфальта.':route('cs_road_right_bend_day','lap2_c')
  if n==44 and text=='Яркая резинка.':route('cs_road_marked_verge_day','lap2_return');emit('$ cs_road_loop_observations = 2');emit('pause 1.0')
  if n==44 and text=='И пошли в противоположную сторону.':route('cs_road_right_bend_day','back_c')
  if n==44 and text=='Снова асфальт.':route('cs_road_left_bend_day','back_b')
  if n==44 and text=='Дорога сделала небольшой изгиб.':route('cs_road_powerlines_day','back_a')
  if n==44 and text=='И между деревьями показалась знакомая вывеска.':road=False;bg('bg ext_no_bus');emit('label cs_check_part06_gate_return:')
  if n==45 and text=='Ольга Дмитриевна шла по дорожке в нашу сторону.':group=['mt','cs_semen','cs_darya'];poses['mt']='angry';show();emit('label cs_check_part06_olga_arrived:')
  if n==45 and text=='Ольга Дмитриевна немного смягчилась.':poses['mt']='normal';emit('show '+actor('mt'))
  if n==45 and text=='Она направилась обратно к площади.':group=['cs_semen','cs_darya'];show();emit('label cs_check_part06_olga_left:')
  if n==46 and text=='Затем сложила лист.':emit('$ cs_road_notes_written = True')
  if n==46 and text=='Он попрощался и пошёл своей дорогой.':group=['cs_darya'];show();emit('label cs_check_part06_semen_left:')
  if n==46 and text=='Тебе страшно?':music('a_promise_from_distant_days',.14)
  target={'cs_da':'cs_darya','cs_sy':'cs_semen','cs_mt':'mt'}.get(speaker)
  if speaker=='cs_narrator' and text.startswith('Дарья'):target='cs_darya'
  pose=None
  if target=='cs_darya':pose=reaction(text,speaker=speaker)
  elif target=='cs_semen':pose='thinking' if '?' in text else 'serious' if any(w in text.lower() for w in ('вместе','ни разу','думал','пришли','провер')) else 'smile' if any(w in text.lower() for w in ('хорошо','согласен','договорились')) else None
  if target in group and pose and poses[target]!=pose:poses[target]=pose;emit('show '+actor(target));emit('$ cs_part06_cast = '+q(group))
  emit(speaker+' '+q(text));catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==46:emit('stop music fadeout 3.0');emit('$ cs_day02_part06_complete = True');emit('label cs_check_part06_ready:');emit('pause 0.5')
 emit('return')
 (folder/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2]
 if n==41:
  intro,a=body.split('### Сцена 41А. Без шуток',1);a,b=a.split('### Сцена 41Б. Только факты',1)
  build(n,title,intro);build(n,'Без шуток',a,'a');build(n,'Только факты',b,'b')
 else:build(n,title,body)
(R/'source/day02_part06_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 6:',len(catalog),'source blocks, nine scene/branch files')
