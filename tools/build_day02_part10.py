"""Author's finale, split into scene files; source is preserved separately."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part10.md').read_text(encoding='utf8').split('## Техническое задание для Codex')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
folder=R/'days/day02/part10';folder.mkdir(parents=True,exist_ok=True)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz'}
catalog=[]
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part09_live = False','    $ cs_reading_live = False','    $ cs_part10_live = True']
 ind='    '
 def e(s):lines.append(ind+s)
 def d(pose='shrug'):e('show cs_darya '+pose+' pioneer normal at cs_darya_normal_right')
 def z(pose='normal'):e('show cs_zhenya '+pose+' pioneer normal at cs_darya_normal_left')
 def scene(bg):e('scene '+bg);d();e('with Dissolve(0.8)')
 if n==66:
  e('$ sunset_time()');e('$ persistent.sprite_time = "sunset"');scene('bg ext_dining_hall_near_sunset');e('play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0');e('$ renpy.music.set_volume(0.12, channel="music")')
 elif n==67:
  scene('cs_library_exterior_sunset');e('stop music fadeout 2.0');scene('bg int_library_day');z();e('play ambience "sound/ambiences/library_day.ogg" fadeout 1.5 fadein 1.5');e('$ renpy.music.set_volume(0.055, channel="ambience")')
 elif n in (68,69):d();z('thoughtful')
 elif n==70:
  e('$ night_time()');e('$ persistent.sprite_time = "night"');scene('bg ext_square_night');e('stop cs_piano fadeout 3.0');e('play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0');e('$ renpy.music.set_volume(0.12, channel="music")');e('play ambience "sound/ambiences/camp_center_night.ogg" fadeout 2.0 fadein 2.0');e('$ renpy.music.set_volume(0.10, channel="ambience")')
 elif n==71:
  scene('cs_house_lena_darya_ext_night');e('play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 3.0');e('$ renpy.music.set_volume(0.12, channel="music")')
 elif n>=72:d('thinking')
 e('label cs_check_finale_%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if p.startswith('**[ЕСЛИ `'):
   ind='    ';e('if '+re.search(r'`([^`]+)`',p)[1]+':');ind='        ';continue
  if p.startswith('**[ИНАЧЕ'):ind='    ';e('else:');ind='        ';continue
  if p.startswith('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):ind='    ';continue
  if p.startswith('**[УСЛОВНОЕ ДОПОЛНЕНИЕ'):
   ind='    ';e('if cs_mz_map_lead:');ind='        ';continue
  if p.startswith('**[КОНЕЦ УСЛОВНЫХ'):ind='    ';continue
  if not p or p=='---' or p.startswith(('#','**[','Использовать существующую','В ней должны','В ней','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  # The montage instruction belongs to neither scene 69 nor spoken narration.
  if n==69 and text.startswith(('Использовать существующую','В ней должны')):continue
  if n==66 and text=='Внутри я сразу подошла к тумбочке.':scene('cs_house_lena_darya_int_day at cs_house_full_frame')
  if n==66 and text=='Мы вышли.':scene('cs_house_lena_darya_ext_day')
  if n==69 and text=='На крыльце я ненадолго остановилась.':scene('cs_library_exterior_sunset')
  if n==71 and text=='Внутри горел тёплый свет.':scene('cs_house_lena_darya_int_night at cs_house_full_frame')
  if speaker=='cs_da':
   pose=reaction(text,speaker=speaker) or 'shrug';d(pose)
  if speaker=='cs_mz':z('thinking' if '?' in text else 'explaining' if len(text)>90 else 'thoughtful')
  if n==70 and text=='Она направилась к нашему домику.':e('# Presence rule: keep Darya until the next location, per user request.')
  if n==72 and text=='Семёна, который сам предложил помощь после концерта.':
   e('if cs_friend_se >= 2:');lines.append(ind+'    '+speaker+' '+q(text));e('else:');lines.append(ind+'    '+speaker+' '+q('Семёна, который выслушал нас и прошёл с нами дорогу.'));catalog.append(text);continue
  if n==69 and text=='И, кажется, именно второй визит оказался для нас гораздо важнее.':text='И, кажется, этот визит оказался для нас гораздо важнее.'
  if n==74 and text.startswith('Утром бегала. Днём исследовала'):
   e('if cs_lena_book_returned:');lines.append(ind+'    '+speaker+' '+q(text));e('else:');lines.append(ind+'    '+speaker+' '+q('Утром бегала. Днём исследовала пространственную петлю. Потом познакомилась с землёй поближе, чем планировала. Вечером послушала концерт.'));catalog.append(text);continue
  e(speaker+' '+q(text));catalog.append(text)
  if n==66 and text=='Я взяла свой экземпляр, проверила закладку и осторожно прижала его к боку здоровой рукой.':e('$ cs_reading_book_location = "lena_hand"')
  if n==74 and text=='Комната погрузилась в мягкую темноту.':e('# Keep the same portrait height through bedtime, per user request.')
 ind='    '
 if n==68 and suffix:
  e('$ cs_reading_book_borrowed = False');e('$ cs_lena_book_returned = True');e('$ cs_reading_book_location = "library_shelf"');e('label cs_check_finale_returned_'+suffix+':')
 if n==69:e('scene cs_camp_path_sunset');d();e('with Dissolve(0.8)')
 if n==74:e('stop music fadeout 4.0');e('stop ambience fadeout 4.0')
 e('return');(folder/('%02d%s_scene.rpy'%(n,suffix))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);body=parts[i+2].split('### Монтажная граница')[0];title=parts[i+1]
 if n==68:
  b=re.split(r'#### Если `[^`]+`\s*',body)
  build(n,title,b[0]);
  for suffix,section in zip(('a','b','c'),b[1:]):build(n,title,section,suffix)
 else:build(n,title,body)
(R/'source/day02_part10_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Finale:',len(catalog),'source blocks')
