"""Author the supplied first musical meeting as independent scenes and branches."""
import re,json,hashlib
from pathlib import Path
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part02.md').read_text(encoding='utf8').split('## Инструкция для Codex')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda text:json.dumps(text,ensure_ascii=False)
tags=['cs_darya','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
catalog=[]
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title)]
 def emit(text):lines.append('    '+text)
 group=['cs_darya'] if n in (15,20) else ['mi','cs_darya'];visible=[];private=False;cg=False;poses={'mi':'normal','cs_darya':'shrug'};japanese_checkpoint=False;miku_checkpoint=False
 def clear():
  for tag in tags:emit('hide '+tag)
  emit('$ cs_part02_cast = []');visible.clear()
 def show():
  clear()
  if cg or private:return
  for tag in group:
   emit('show '+('mi '+poses[tag]+' pioneer at cs_actor_left zorder 10' if tag=='mi' else 'cs_darya '+poses[tag]+' pioneer normal at '+('cs_darya_normal_center' if len(group)==1 else 'cs_darya_normal_right')))
  emit('$ cs_part02_cast = '+q(group));visible[:]=group
 def bg(target):
  emit('scene '+target);emit('$ cs_part02_cg = False');show();emit('with Dissolve(0.8)')
 def music():
  emit('if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":');lines.append('        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0');emit('$ renpy.music.set_volume(0.22, channel="music", delay=1.0)')
 def amb(name,volume):
  file='sound/ambiences/'+name+'.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(file)+':');lines.append('        play ambience '+q(file)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 def piano(kind,again=False):
  nonlocal cg
  cg=True;emit('scene cs_cg_'+kind+'_piano_day');clear();emit('$ cs_part02_cg = True');emit('with Dissolve(0.8)');emit('stop music fadeout 1.0');emit('$ renpy.music.set_volume(0.58, channel="cs_piano", delay=0.3)');emit('play cs_piano '+('"<from 12>sound/music/miku_song_voice.ogg"' if again else 'cs_'+kind+'_piano_track')+' noloop fadein 1.0');emit('label cs_check_d2_piano_'+kind+('_again' if again else '')+':');emit('pause 1.5')
 def end_piano():
  nonlocal cg
  emit('stop cs_piano fadeout 0.8');cg=False;bg('bg int_musclub_day')
 if n==15:
  emit('$ cs_part02_live = True');emit('hide screen cs_day02_continue_screen');bg('bg ext_dining_hall_near_day');amb('camp_center_day',.22);music()
 elif n==17:
  bg('bg ext_musclub_day');emit('play sound "sound/sfx/open_door_2.ogg"');bg('bg int_musclub_day');amb('music_club_day',.12);emit('stop music fadeout 2.0')
 elif n==18:
  group=['mi'];show();emit('stop music fadeout 1.0');amb('music_club_day',.08)
 elif n==20:
  emit('stop cs_piano fadeout 1.0');bg('bg ext_musclub_day');amb('camp_center_day',.22);music()
 else:show()
 emit('label cs_check_part02_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:
   who=m[1].split(' (')[0];speaker={'Лена Соколова':'cs_ls','Дарья':'cs_da','Мику':'cs_mi','Ольга Дмитриевна':'cs_mt'}[who];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p
  if n==15 and text.startswith('Семён задержался на крыльце,'):bg('cs_camp_path_day')
  if n==15 and text=='Девушка заметила нас и приветливо улыбнулась.':group=['mi','cs_darya'];show()
  if n==15 and text=='Ой, простите, я же даже не представилась! Меня Мику зовут.':emit('$ cs_met_mi = True');emit('$ cs_mi_name_known = True')
  if n==17 and text=='Подошла к инструменту и села.':group=['mi'];show()
  if n==18 and text=='И начала играть.':piano('darya')
  if n==18 and text=='Мелодия закончилась негромким аккордом.':end_piano();group=['mi'];show()
  if n==18 and text=='Дарья поднялась, освобождая место.':group=['mi','cs_darya'];show()
  if n==19 and suffix=='a' and text=='И начала играть.':piano('miku')
  if n==19 and suffix=='a' and text=='И неожиданно остановилась.':end_piano()
  if n==19 and suffix=='a' and text=='Потом сыграла фрагмент ещё раз.':piano('miku',True)
  if n==19 and suffix=='a' and text=='Вот так мне нравится больше.':end_piano()
  if n==20 and text=='На дорожках становилось заметно оживлённее.':bg('cs_camp_path_day')
  if n==20 and text=='Мы подошли к площади.':bg('bg ext_square_day');emit('label cs_check_part02_square:')
  if speaker=='cs_th':
   if not cg and visible:clear()
   private=True
  elif speaker in ('cs_ls','cs_da','cs_mi','cs_mt'):
   if private:private=False;show()
   if speaker=='cs_da' and not cg and 'cs_darya' in group:
    pose=reaction(text) or 'shrug'
    if pose!=poses['cs_darya']:poses['cs_darya']=pose;show()
   if speaker=='cs_mi' and not cg and 'mi' in group:
    t=text.lower();pose='shy' if any(w in t for w in ('извини','опять','увлеклась')) else 'happy' if '!' in text else 'surprise' if '?' in text else 'smile'
    if pose!=poses['mi']:poses['mi']=pose;show()
  # Use a licensed Japanese font only for Japanese runs; Russian stays in the game font.
  display=re.sub(r'[\u3040-\u30ff\u3400-\u9fff\uff00-\uffef\u3000-\u303f]+',lambda m:'{font=mods/chuzaya_smena/fonts/NotoSansCJKjp-Regular.otf}'+m[0]+'{/font}',text)
  if not japanese_checkpoint and speaker=='cs_ls' and 'おはよう' in text:emit('label cs_check_part02_japanese:');japanese_checkpoint=True
  if not miku_checkpoint and speaker=='cs_mi':emit('label cs_check_part02_miku_'+str(n)+suffix+':');miku_checkpoint=True
  emit(speaker+' '+q(display));catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==19 and suffix=='a' and (R/'source/day02_part03.md').exists():emit('call cs_day02_21')
 if n==20:clear();emit('$ cs_part02_live = False')
 emit('return')
 (R/'days/day02/part02'/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2]
 if n==19:
  a,b=re.split(r'#### Сцена 19Б\. До следующего раза',body,1)
  a=a.split('#### Сцена 19А. Внимательные слушатели',1)[1]
  if (R/'source/day02_part03.md').exists():a=a.split('Мику захлопнула папку.',1)[0]
  build(n,'Внимательные слушатели',a,'a');build(n,'До следующего раза',b,'b')
 else:build(n,title,body)
(R/'source/day02_part02_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
assets=['cg/music_club/cg_darya_piano_day.png','cg/music_club/cg_miku_piano_day.png','audio/music/music_club/The_Unfinished_Lullaby.mp3','fonts/NotoSansCJKjp-Regular.otf']
(R/'source/day02_part02_assets.json').write_text(json.dumps([dict(path=p,sha256=hashlib.sha256((R/p).read_bytes()).hexdigest()) for p in assets],indent=2),encoding='utf8')
print('Part 2:',len(catalog),'source blocks, seven scene/branch files')
