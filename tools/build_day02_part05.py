"""Poster completion and a shared walk; original source remains separate."""
from pathlib import Path
import re,json,hashlib
from darya_emotions import reaction
R=Path(__file__).resolve().parent.parent
raw=(R/'source/day02_part05.md').read_text(encoding='utf8').split('**[КОНЕЦ ПЯТОЙ ЧАСТИ ВТОРОГО ДНЯ.]**')[0]
parts=re.split(r'### Сцена (\d+)\. (.+)\n',raw)
q=lambda s:json.dumps(s,ensure_ascii=False)
voices={'Лена Соколова':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Славя':'cs_sl','Виола':'cs_vi'}
tags=['cs_darya','cs_dasha_winter','cs_dasha_pioneer','cs_semen','cs_zhenya','mz','un','mi','dv','sl','us','mt','sh','el','cs']
folder=R/'days/day02/part05';folder.mkdir(parents=True,exist_ok=True)
catalog=[]
alternatives={'Вспомнила высокую лавку в музыкальном кружке.':'Вспомнила утренний спор с карандашом.',
 'Да. Сначала советская мебель, теперь ты.':'Да. Сначала бумага без Ctrl+Z, теперь ты.'}
def build(n,title,body,suffix=''):
 lines=['# -*- coding: utf-8 -*-','label cs_day02_%02d%s:'%(n,suffix),'    $ save_name = '+q('Чужая смена — День 2: '+title),'    $ cs_part04_live = False','    $ cs_part05_live = True']
 indent='    ';cg=n in (34,35,36);group=[] if cg else ['sl','cs_semen','cs_darya'] if n==37 else ['cs_darya']
 poses={'cs_darya':'shrug','cs_semen':'neutral','sl':'normal','cs':'normal'}
 def emit(s):lines.append(indent+s)
 def actor(t):
  if len(group)==3:
   if t=='cs_darya':return t+' '+poses[t]+' pioneer far at cs_darya_far_right'
   if t=='cs_semen':return t+' '+poses[t]+' pioneer far at cs_semen_far_center'
   return 'sl '+poses[t]+' pioneer far at cs_actor_far_left zorder 10'
  if t=='cs_darya':return t+' '+poses[t]+' pioneer normal at cs_darya_normal_right'
  if t=='cs_semen':return t+' '+poses[t]+' pioneer normal at cs_semen_normal_left'
  return t+' '+poses[t]+(' pioneer' if t=='sl' else '')+' at cs_actor_left zorder 10'
 def show():
  for t in tags:
   if t not in group:emit('hide '+t)
  for t in group:emit('show '+actor(t))
  emit('$ cs_part05_cast = '+q(group))
 def bg(name):
  nonlocal cg
  cg=False;emit('scene '+name);emit('$ cs_part05_cg = False');show();emit('with Dissolve(0.8)')
 def amb(volume=.15):
  p='sound/ambiences/camp_center_day.ogg';emit('if renpy.music.get_playing(channel="ambience") != '+q(p)+':');lines.append(indent+'    play ambience '+q(p)+' fadeout 1.0 fadein 1.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="ambience", delay=1.0)')
 def music(name,volume=.18):
  p='sound/music/'+name+'.ogg';emit('if renpy.music.get_playing() != '+q(p)+':');lines.append(indent+'    play music '+q(p)+' fadeout 2.0 fadein 2.5');emit('$ renpy.music.set_volume('+str(volume)+', channel="music", delay=1.0)')
 if n in (34,35,36):
  emit('if not renpy.showing("cs_cg_poster_planning_day"):');lines.append(indent+'    scene cs_cg_poster_planning_day')
  emit('$ cs_part05_cg = True');show();amb()
  emit('if renpy.music.get_playing() is None:');lines.append(indent+'    play music "sound/music/my_daily_life.ogg" fadein 2.0')
 elif n==37:bg('bg ext_square_day');amb();music('lets_be_friends')
 elif n==38:bg('cs_camp_path_day');amb(.10);music('get_to_know_me_better',.16)
 else:show();emit('$ cs_part05_cg = False');amb(.10)
 emit('label cs_check_part05_s%02d%s:'%(n,suffix))
 for p in re.split(r'\n\s*\n',body):
  p=p.strip()
  if p.startswith('**[ЕСЛИ `cs_helped_sl_day2 == True`'):
   emit('if cs_helped_sl_day2:');indent='        ';emit('label cs_check_part05_sl_helped:');continue
  if p.startswith('**[ЕСЛИ `cs_helped_sl_day2 == False`'):
   indent='    ';emit('else:');indent='        ';emit('label cs_check_part05_sl_neutral:');continue
  if p.startswith('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.'):indent='    ';continue
  if not p or p=='---' or p.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*([^:*]+):\*\*\\?\s*\n?\s*[—–]\s*(.+)',p,re.S)
  if m:speaker=voices[m[1].split(' (')[0]];text=m[2].strip()
  elif p.startswith('*') and p.endswith('*') and not p.startswith('**'):speaker='cs_th';text=p.strip('*')
  else:speaker='cs_narrator';text=p.strip('*')
  if n==36 and text=='Семён поднял объявление.':group=['cs_semen','cs_darya'];bg('bg ext_clubs_day');emit('$ cs_day02_poster_finished = True');emit('label cs_check_part05_poster_finished:')
  if n==36 and text=='И тут со стороны площади появилась Славя.':group=['sl','cs_semen','cs_darya'];show();emit('label cs_check_part05_sl_arrived:')
  if n==37 and text=='Тогда официально считаю работу завершённой.':emit('$ cs_day02_poster_posted = True')
  if n==37 and text=='В этот момент мимо площади проходила Виола.':group=['cs','cs_darya'];show();emit('label cs_check_part05_viola_arrived:')
  if n==37 and text=='Она попрощалась и продолжила путь.':group=['sl','cs_semen','cs_darya'];show();emit('label cs_check_part05_viola_left:')
  if n==37 and text=='Семён и Славя направились в сторону клубов.':group=['cs_darya'];show();emit('label cs_check_part05_companions_left:')
  if n==39 and text=='Она протянула мне руку.':music('a_promise_from_distant_days',.17)
  if n==39 and text=='Потом осторожно взяла.':
   cg=True;group=[];emit('scene cs_cg_lena_darya_hand_in_hand_day');emit('$ cs_part05_cg = True');show();emit('with Dissolve(1.0)');emit('label cs_check_part05_hand_in_hand:')
  target={'cs_da':'cs_darya','cs_sy':'cs_semen','cs_sl':'sl','cs_vi':'cs'}.get(speaker)
  if speaker=='cs_narrator' and text.startswith('Дарья'):target='cs_darya'
  pose=None
  if target=='cs_darya':pose=reaction(text,speaker=speaker)
  elif target=='cs_semen':
   pose='thinking' if '?' in text else 'awkward' if any(w in text.lower() for w in ('не помещ','поддержку','почерка')) else 'smile' if any(w in text.lower() for w in ('согласен','хорошо','справился','наконец')) else None
  elif target in ('sl','cs'):pose='smile' if any(w in text.lower() for w in ('спасибо','красиво','понятно','заметила','неплохо','хорошо')) else 'normal'
  if not cg and target in group and pose and poses[target]!=pose:poses[target]=pose;emit('show '+actor(target));emit('$ cs_part05_cast = '+q(group))
  if n==39 and text in alternatives:
   emit('if cs_day02_miku_listened:');lines.append(indent+'    '+speaker+' '+q(text));emit('else:');lines.append(indent+'    '+speaker+' '+q(alternatives[text]))
  else:emit(speaker+' '+q(text))
  catalog.append(dict(scene=n,suffix=suffix,speaker=speaker,text=text))
 if n==39:emit('stop music fadeout 3.0');amb(.18);emit('$ cs_day02_part05_complete = True');emit('label cs_check_part05_walk_ready:');emit('pause 0.5')
 emit('return')
 (folder/('%02d_%sscene.rpy'%(n,suffix+'_' if suffix else ''))).write_text('\n'.join(lines)+'\n',encoding='utf8')
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1].strip();body=parts[i+2]
 if n==35:
  intro,a=body.split('### Сцена 35А. Совместное производство',1);a,b=a.split('### Сцена 35Б. Разделение труда',1)
  build(n,title,intro);build(n,'Совместное производство',a,'a');build(n,'Разделение труда',b,'b')
 else:build(n,title,body)
(R/'source/day02_part05_dialogue.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
asset='cg/lena_n_dasha/cg_lena_darya_hand_in_hand_day.png'
(R/'source/day02_part05_assets.json').write_text(json.dumps([dict(path=asset,original='cg/lena_n_dasha/6830b449-cd57-46b6-8607-652ad156f96e.png',sha256=hashlib.sha256((R/asset).read_bytes()).hexdigest())],indent=2),encoding='utf8')
print('Part 5:',len(catalog),'source blocks, eight files')
