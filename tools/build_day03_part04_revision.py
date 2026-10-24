"""Replace the morning visit, preserve old named entries and later continuity."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent;D=R/'days/day03/part04'
s=(R/'source/day03_part04_revision.md').read_text(encoding='utf8')
s=s[s.index('### Сцена 96.'):s.index('## Задание для Codex')]
p=re.split(r'### Сцена (\d+[А-Я]?)\. ([^\n]+)\n',s)
parts={p[i]:(p[i+1],p[i+2]) for i in range(1,len(p),3)}
transcript={}
def parse(text):
 out=[]
 for t in re.split(r'\n\s*\n',text):
  t=t.strip()
  if not t or t=='---' or t.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
  if m:
   n,w=m.groups();who={'Лена Соколова':'cs_ls','Дарья':'cs_da','Виола':'cs_vi','Семён':'cs_sy','Алиса':'cs_dv','Алиса (за дверью)':'cs_dv'}[n]
  elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
  else:who,w='cs_narrator',t
  out.append((who,w.replace('\n',' ')))
 return out
def pose(tag,emotion):
 attrs=' custom '+emotion+' medical normal' if tag=='cs' else ' '+emotion+' pioneer'+(' normal' if tag.startswith('cs_') else '')
 return ['if renpy.showing("'+tag+'"):', '    show '+tag+attrs,'    $ cs_presence_stage()','    with cs_sprite_change']
def frame(bg,actors):
 b=['$ cs_director_scene("'+bg+'")','scene '+bg]
 for tag,emotion in actors:
  attrs=' custom '+emotion+' medical normal' if tag=='cs' else ' '+emotion+' pioneer'+(' normal' if tag.startswith('cs_') else '')
  b+=['show '+tag+attrs+' at '+({'cs':'cs_viola_normal_left','cs_semen':'cs_semen_normal_right'}.get(tag,'cs_darya_normal_right' if tag=='cs_darya' else 'cs_actor_left'))]
 return b+['$ cs_presence_stage()','with Dissolve(0.8)']
da=[('cs_darya','shy_smile')];medical=[('cs','warm_smile')]+da
hooks={
 '96':{'Он покачал головой и направился по дорожке.':['$ cs_actor_exit(["cs_semen"])','with cs_sprite_leave','label cs_check_day03_96_semen_left:']},
 '97':{'Впереди показался медпункт.':frame('bg ext_aidpost_day',da)+['label cs_check_day03_97_aidpost:']},
 '99':{'Виола сняла старый бинт.':pose('cs','serious')+['label cs_check_day03_99_examination:'],'Наложила новую повязку.':['$ cs_day03_viola_check_done = True','$ cs_lena_elbow_bandaged = True','label cs_check_day03_99_dressed:']},
 '100a':{'Работа оказалась совершенно обычной.':['$ cs_director_scene("cs_cg_lena_darya_medical_inventory_day")','scene cs_cg_lena_darya_medical_inventory_day','with Dissolve(0.8)','label cs_check_day03_101_inventory_cg:'],'Наконец Дарья поставила последнюю отметку.':frame('bg int_aidpost_day',medical)+['label cs_check_day03_101_inventory_return:']},
 '101':{'На пороге появилась Алиса Двачевская.':['show dv normal pioneer at cs_actor_left','$ cs_presence_stage()','with cs_sprite_change','label cs_check_day03_101_alice:'],'Мы вышли.':frame('bg ext_aidpost_day',da+[('dv','normal')])+['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.5','label cs_check_day03_102_outside:']},
 '102a':{'Алиса вернулась внутрь.':['$ cs_actor_exit(["dv"])','with cs_sprite_leave','label cs_check_day03_102_alice_left_a:']},
 '102b':{'Она вернулась в медпункт.':['$ cs_actor_exit(["dv"])','with cs_sprite_leave','label cs_check_day03_102_alice_left_b:']},
 '103':{'Мы пошли по дорожке.':frame('cs_camp_path_day',da),'Я смотрела на деревья.':['$ cs_pov_begin()','with cs_sprite_leave','label cs_check_day03_103_reflection:'],'Дарья:':[], 'Лен.':[],'Ты сегодня действительно как-то спокойнее.':[], 'Я немного улыбнулась.':['$ cs_pov_end()','with cs_sprite_change','label cs_check_day03_103_dialogue:']}
}
for k in ('96','97','98','99','100','100a','100b','101','102a','102b','103'):
 h=hooks.setdefault(k,{})
 for w,e in [('Дарья рассмеялась.','amused'),('Дарья тихо рассмеялась.','amused'),('Дарья улыбнулась.','shy_smile'),('Дарья пожала плечами.','shrug'),('Дарья закрыла глаза.','thinking')]:h.setdefault(w,pose('cs_darya',e))
 for w,e in [('Виола улыбнулась.','warm_smile'),('Виола усмехнулась.','amused'),('Виола рассмеялась.','amused'),('Она начала обработку.','serious')]:h.setdefault(w,pose('cs',e))
 for w,e in [('Алиса усмехнулась.','grin'),('Алиса рассмеялась.','laugh'),('Алиса улыбнулась.','smile'),('Она прищурилась.','normal')]:
  if k in ('101','102a','102b'):h.setdefault(w,pose('dv',e))
 for w,e in [('Семён рассмеялся.','smile'),('Семён усмехнулся.','smile'),('Он вздохнул.','awkward')]:
  if k=='96':h.setdefault(w,pose('cs_semen',e))
changes={
 'Кстати, это ты там что-то кричала возле столовой?':'Кстати, это ты возле столовой очередь ко мне распределяла?',
 'Третий визит к местной медицине.':'Плановый осмотр после вчерашних приключений.',
 'Удивительно. Стоит дважды поранить локоть, и люди уже начинают считать тебя постоянным клиентом.':'Удивительно. Стоит вернуться на перевязку, и люди уже начинают считать тебя постоянным клиентом.',
 'Так. Бинты. Шесть упаковок.':'Так. Бинты. Шесть упаковок.',
}
def write(k,blocks,pre=(),post=()):
 b=list(pre);transcript[k]=[]
 for text,depth in blocks:
  indent='    '*depth
  if isinstance(text,list):b += [indent+x for x in text];continue
  for who,w in parse(text):
   transcript[k].append((who,w));b += [indent+x for x in hooks.get(k,{}).get(w,[])]
   b.append(indent+who+' '+json.dumps(changes.get(w,w),ensure_ascii=False))
 b+=list(post)+['return']
 title=parts.get(k.replace('a','А').replace('b','Б'),('',))[0]
 (D/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n',encoding='utf8')
def one(k,pre=(),post=()):write(k,[(parts[k.replace('a','А').replace('b','Б')][1],0)],pre,post)
one('96',frame('bg ext_dining_hall_away_day',da+[('cs_semen','smile')])+['label cs_check_day03_96:','label cs_check_day03_96_semen:','play music "sound/music/my_daily_life.ogg" fadein 2.0'])
one('97',frame('cs_camp_path_day',da)+['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0'])
one('98',frame('bg int_aidpost_day',medical)+['stop music fadeout 2.0','play ambience "sound/ambiences/medstation_inside_day.ogg" fadein 1.5','label cs_check_day03_98:'])
one('99');one('100');one('100a');one('100b')
# Move the optional gift before Alice arrives, following the task's chronology.
t=parts['101'][1];base,t=t.split('**[ЕСЛИ ранее было как минимум 2 очка');condition,t=t.split('**',1)
gift,t=t.split('**[ИНАЧЕ:]**');low,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
giftcode=['if cs_viola_friend_before_day3 >= 2 and not cs_viola_day3_bonus_seen:','    if not cs_viola_spare_bandage:']
write('101',[(giftcode,0),(gift,2),(['        $ cs_viola_spare_bandage = True','        label cs_check_day03_102_spare_given:','        cs_narrator "Я убрала запечатанный пакет в сумку, чтобы не потерять его по дороге."','    else:','        cs_vi "Запасная повязка ещё у тебя? Пусть остаётся в сумке. Если рука будет беспокоить, приходи."','        cs_ls "Да, она со мной. Спасибо."','    $ cs_viola_day3_bonus_seen = True','else:'],0),(low,1),(base,0),(tail,0)])
one('102a');one('102b')
write('102',[],pre=['call cs_day03_alice_medpoint_choice'])
one('103',pre=['label cs_check_day03_103_outside:','play music "sound/music/my_daily_life.ogg" fadein 2.0','$ renpy.music.set_volume(0.15,delay=1.0,channel="music")'],post=['$ cs_day03_medpoint_revision_done = True'])
flow=(D/'00_flow.rpy').read_text(encoding='utf8')
if '    call cs_day03_101\n    call cs_day03_102\n' not in flow:
 flow=flow.replace('    call cs_day03_102\n','    call cs_day03_101\n    call cs_day03_102\n')
flow=flow.replace('call cs_day03_101a','call cs_day03_100a').replace('call cs_day03_101b','call cs_day03_100b')
# These are now real checkpoints inside 103, not the old placeholder jumps.
flow=re.sub(r'label cs_check_day03_103_(reflection|dialogue):\n    jump cs_day03_part05_legacy\n','',flow)
if 'label cs_day03_alice_medpoint_choice:' not in flow:flow+='''
label cs_day03_alice_medpoint_choice:
    label cs_check_day03_102_menu:
    menu:
        "Спросить, всё ли в порядке, и не делать из этого представление":
            if not cs_dv_medpoint_day3:
                $ cs_friend_dv += 1
                $ cs_dv_medpoint_day3 = True
            call cs_day03_102a
        "Не вмешиваться и пожелать Алисе удачи":
            call cs_day03_102b
    label cs_check_day03_102_result:
    return
'''
(D/'00_flow.rpy').write_text(flow,encoding='utf8')
if 'label cs_check_day03_102_viola_left:' not in flow:
 flow+='\n# Compatibility with a save at the former end of the medical visit.\nlabel cs_check_day03_102_viola_left:\n    $ cs_actor_exit(["cs"])\n    return\n'
 (D/'00_flow.rpy').write_text(flow,encoding='utf8')
for old,new in [('101a','100a'),('101b','100b')]:
 (D/(old+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+old+':\n    call cs_day03_'+new+'\n    return\n',encoding='utf8')
p=D/'resources.rpy';t=p.read_text(encoding='utf8')
if 'default cs_dv_medpoint_day3' not in t:t+='\ndefault cs_dv_medpoint_day3 = False\ndefault cs_day03_medpoint_revision_done = False\ninit -9 python:\n    cs_state_defaults.update(cs_dv_medpoint_day3=False,cs_day03_medpoint_revision_done=False)\n'
p.write_text(t,encoding='utf8')
(R/'source/day03_part04_revision_transcript.json').write_text(json.dumps(transcript,ensure_ascii=False,indent=2),encoding='utf8')
print('Revised morning visit:',sum(map(len,transcript.values())),'blocks')
