"""Square reunion after the second clinic visit; intact user CG and full PNGs."""
from pathlib import Path
import re,json
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part08.md').read_text(encoding='utf8').split('**[КОНЕЦ ЧАСТИ 8 ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)([АБ]?)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Женя':'cs_mz'}
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
folder=R/'days/day02/part08';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
for i in range(1,len(parts),4):
 n=int(parts[i]);suffix={'А':'a','Б':'b','':''}[parts[i+1]];title=parts[i+2];body=parts[i+3]
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part07_live = False','    $ cs_part08_live = True']
 def emit(s):lines.append('    '+s)
 group=['cs_darya'] if n==54 else [] if n==55 else ['cs_semen','cs_darya']
 poses={'cs_darya':'shrug','cs_semen':'neutral','cs_zhenya':'normal'}
 seated=n in (56,57)
 def actor(t):
  if t=='cs_darya':pos='cs_darya_normal_right'
  elif t=='cs_semen':pos='cs_semen_normal_left'
  else:pos='cs_darya_normal_left'
  return t+' '+poses[t]+' pioneer normal at '+pos
 def show():
  for t in tags:
   if t not in group:emit('hide '+t)
  for t in group:emit('show '+actor(t))
  emit('$ cs_part08_cast = '+q(group))
 def bg(name):emit('scene '+name);show();emit('with Dissolve(0.8)')
 def music(name):
  p='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(p)+':');lines.append('        play music '+q(p)+' fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume(0.16, channel="music", delay=1.0)')
 if n==54:
  show();music('my_daily_life');emit('$ renpy.music.set_volume(0.14, channel="ambience", delay=1.0)')
 elif n==56:show();music('lets_be_friends')
 elif n in (58,59):show();music('my_daily_life')
 else:show()
 emit('label cs_check_part08_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if n==54 and text=='Мы прошли мимо доски объявлений.':bg('bg ext_square_day');emit('label cs_check_part08_square:')
  if n==55 and text=='Осторожно прикрыла ему глаза ладонью здоровой руки.':bg('cs_cg_lena_semen_guess_who_day');emit('$ cs_part08_cg = True');emit('label cs_check_part08_guess_cg:')
  if n==55 and text=='Он повернулся.':group=['cs_semen'];bg('bg ext_square_day');emit('$ cs_part08_cg = False');emit('label cs_check_part08_turned:')
  if n==55 and text=='В этот момент подошла Дарья.':group=['cs_semen','cs_darya'];poses['cs_darya']='smile';show();emit('label cs_check_part08_darya_returns:')
  if n==55 and text=='Дарья заняла свободное место.':seated=True;show();emit('label cs_check_part08_seated:')
  if n==58 and suffix=='a' and text=='И направилась к Жене.':group=[];show()
  if n==58 and suffix=='a' and text=='Она подняла взгляд.':group=['cs_zhenya'];show();emit('label cs_check_part08_zhenya:')
  if n==58 and suffix=='a' and text=='Женя пошла дальше.':group=[];show();emit('label cs_check_part08_zhenya_left:')
  if n==58 and suffix=='a' and text=='Я вернулась к лавочке.':group=['cs_semen','cs_darya'];seated=True;show();emit('label cs_check_part08_rejoined:')
  if n==59 and text=='Он махнул рукой и направился к клубам.':group=['cs_darya'];show();emit('label cs_check_part08_semen_left:')
  if n==59 and text=='Мы пошли по дорожке.':bg('cs_camp_path_day');emit('label cs_check_part08_walk:')
  if n==56 and text=='И почему-то после этого мне стало немного легче.':
   emit('if cs_friend_se >= 2:');lines.append('        show cs_semen relaxed pioneer normal at cs_semen_normal_left');emit('else:');lines.append('        show cs_semen neutral pioneer normal at cs_semen_normal_left');emit('label cs_check_part08_trust:')
  if speaker=='cs_narrator' and 'cs_semen' in group:
   pose='smile' if text in ('Он рассмеялся.','Семён рассмеялся.','Он начал смеяться.','Он усмехнулся.') else 'surprised' if text=='Он удивился.' else 'serious' if text=='Он нахмурился.' else None
   if pose and pose!=poses['cs_semen']:poses['cs_semen']=pose;emit('show '+actor('cs_semen'));emit('$ cs_part08_cast = '+q(group))
  if speaker=='cs_da' or (speaker=='cs_narrator' and text.startswith('Дарья')):
   pose=reaction(text,speaker=speaker)
   if pose and pose!=poses['cs_darya'] and 'cs_darya' in group:poses['cs_darya']=pose;emit('show '+actor('cs_darya'));emit('$ cs_part08_cast = '+q(group))
  if speaker=='cs_sy' and 'cs_semen' in group:
   low=text.lower()
   pose='serious' if any(w in low for w in ('рукой','разозли','странно отреаг','не понимаю')) else 'thinking' if '?' in text else 'smile' if any(w in low for w in ('скучно','ждать','победил','соколова','прости')) else 'neutral'
   if pose!=poses['cs_semen']:poses['cs_semen']=pose;emit('show '+actor('cs_semen'));emit('$ cs_part08_cast = '+q(group))
  if speaker=='cs_mz' and 'cs_zhenya' in group:
   pose='glasses_touch' if 'каталогу' in text else 'thinking' if '?' in text else 'arms_crossed' if 'доказательств' in text or 'не поверила' in text else 'explaining' if len(text)>75 else 'normal'
   if pose!=poses['cs_zhenya']:poses['cs_zhenya']=pose;emit('show '+actor('cs_zhenya'));emit('$ cs_part08_cast = '+q(group))
  emit(speaker+' '+q(text));catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==59:emit('stop music fadeout 3.0');emit('$ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)');emit('$ cs_day02_part08_complete = True');emit('label cs_check_part08_ready:');emit('pause 0.5')
 emit('return');(folder/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
(R/'source/day02_part08_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 8:',len(catalog),'source blocks, eight scene/branch files')
