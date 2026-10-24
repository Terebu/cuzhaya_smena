"""Manuscript integration with three independent choices and explicit scene focus."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parent.parent;D=R/'days/day03/part06';D.mkdir(parents=True,exist_ok=True)
s=(R/'source/day03_part06.md').read_text(encoding='utf8');s=s[s.index('### Сцена 113.'):s.index('## Техническое задание')]
p=re.split(r'### Сцена (\d+[А-Я]?)\. ([^\n]+)\n',s);parts={p[i]:(p[i+1],p[i+2]) for i in range(1,len(p),3)};transcript={}
def parse(t):
 out=[]
 for t in re.split(r'\n\s*\n',t):
  t=t.strip()
  if not t or t=='---' or t.startswith(('#','**[','- ')):continue
  m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
  if m:
   n,w=m.groups();who={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz','Мику':'cs_mi','Алиса':'cs_dv','Лена Тихонова':'cs_un','Славя':'cs_sl','Семён':'cs_sy'}[n]
  elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
  else:who,w='cs_narrator',t
  out.append((who,w.replace('\n',' ')))
 return out
def pose(tag,p):
 attrs=' '+p+' pioneer'+(' normal' if tag in ('cs_darya','cs_zhenya') else '')
 return ['if renpy.showing("'+tag+'"):', '    show '+tag+attrs,'    $ cs_presence_stage()','    with cs_sprite_change']
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
reflect=['$ cs_reflective_focus()','with cs_sprite_leave']
def frame(bg,actors=()):
 a=['$ cs_director_scene("'+bg+'")','scene '+bg,'show cs_darya neutral pioneer normal at cs_darya_normal_right']
 for tag,expression in actors:
  attrs=' '+expression+' pioneer'+(' normal' if tag=='cs_zhenya' else '')
  a+=['show '+tag+attrs+' at '+('cs_darya_normal_left' if tag=='cs_zhenya' else 'cs_actor_left')]
 return a+['$ cs_presence_stage()','with Dissolve(0.8)']
def enter(tag,expression):
 return focus(['cs_darya',tag])+pose(tag,expression)
hooks={
 '113a':{'Мы аккуратно вернули карточки на места.':['$ cs_mz_catalog_checked_day3 = True','$ cs_day03_library_visit_time = "after_lunch" if cs_mz_book_requested_day3 else None','label cs_check_day03_113_catalog_done:'],'Вышли на улицу.':['$ cs_actor_exit(["cs_zhenya"])']+frame('bg ext_library_day')+['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0','label cs_check_day03_113_library_left:']},
 '114':{'Мы открыли дверь.':frame('bg int_musclub_day',[('mi','normal'),('dv','normal')])+['$ renpy.music.set_volume(0.07,delay=1.0,channel="ambience")','label cs_check_day03_114_cast:'],'Дарья подошла к пианино.':['if cs_sl_poster_collected_day3 and cs_day03_poster_location == "darya_folder":','    cs_narrator "Перед тем как подойти к клавишам, Дарья положила папку с плакатом на свободный чистый стул."','    $ cs_day03_poster_location = "music_club_chair"'],'И осторожно коснулась клавиш.':['label cs_check_day03_114_darya_piano:'],'Дарья закончила короткую мелодию.':['label cs_check_day03_114_darya_finished:']},
 '115a':{'Она сыграла короткое вступление.':['label cs_check_day03_115_first:'],'Она сыграла почти ту же последовательность.':['label cs_check_day03_115_second:']},
 '115b':{'Она сыграла оба вступления.':['label cs_check_day03_115_both:']},
 '116':{'Мику вернулась к нотам.':focus(['dv'])+['label cs_check_day03_116_alice_focus:']},
 '118':{'Мы вышли из клуба.':['if cs_day03_poster_location == "music_club_chair":','    cs_narrator "Дарья забрала со стула папку с плакатом и прижала её к боку."','    $ cs_day03_poster_location = "darya_folder"','$ cs_actor_exit(["mi","dv"])']+frame('bg ext_musclub_day')+['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0','play music "sound/music/my_daily_life.ogg" fadein 2.0','$ renpy.music.set_volume(0.15,delay=1.0,channel="music")','label cs_check_day03_118_music_left:'],'Лена Тихонова сидела, чуть наклонившись над альбомом.':enter('un','normal')+['label cs_check_day03_118_un:'],'Она посмотрела на меня внимательнее.':pose('un','normal')},
 '119a':{'А ты не хочешь как-нибудь порисовать вместе?':pose('un','shy')+['label cs_check_day03_119_invitation:']},
 '120':{'Мы отошли от скамейки.':['$ cs_actor_exit(["un"])']+frame('cs_camp_path_day')+['label cs_check_day03_120_bench_left:'],'И в этот момент над лагерем раздался горн.':['$ renpy.music.set_volume(0.06,delay=1.0,channel="music")','if not cs_day03_lunch_horn_played:','    play sound "sound/sfx/dinner_horn_processed.ogg"','    $ cs_day03_lunch_horn_played = True','label cs_check_day03_120_horn:'],'Возле столовой уже собирались пионеры.':frame('bg ext_dining_hall_away_day')+['$ renpy.music.set_volume(0.13,delay=1.0,channel="music")','label cs_check_day03_120_dining:'],'О, вы уже здесь!':enter('sl','smile')+['label cs_check_day03_120_sl:'],'Я подошла к Жене.':focus(['cs_darya','cs_zhenya'])+pose('cs_zhenya','normal')+['label cs_check_day03_120_mz:'],'И мы вместе направились внутрь.':frame('bg int_dining_hall_people_day',[('cs_zhenya','normal')])+['play ambience "sound/ambiences/dining_hall_full.ogg" fadein 1.5','$ renpy.music.set_volume(0.20,delay=1.0,channel="ambience")','$ cs_day03_lunch_arrived = True','label cs_check_day03_120_inside:']}
}
main={'113a':('cs_zhenya','normal'),'115':('mi','happy'),'115a':('mi','happy'),'115b':('mi','smile'),'116':('dv','grin'),'117':('dv','normal'),'117a':('dv','smile'),'117b':('dv','grin'),'118':('un','shy'),'119':('un','normal'),'119a':('un','smile'),'119b':('un','shy')}
for k in ('113','113a','114','115','115a','115b','116','117','117a','117b','118','119','119a','119b','120'):
 h=hooks.setdefault(k,{})
 for w,p in [('Дарья улыбнулась.','shy_smile'),('Дарья рассмеялась.','amused'),('Дарья немного смутилась.','shy_smile'),('Дарья приподняла бровь.','thinking')]:h.setdefault(w,pose('cs_darya',p))
 for w,tag,p in [('Мику улыбнулась.','mi','smile'),('Мику рассмеялась.','mi','laugh'),('Мику задумалась.','mi','normal'),('Мику обрадовалась.','mi','happy'),('Алиса усмехнулась.','dv','grin'),('Алиса прищурилась.','dv','normal'),('Алиса рассмеялась.','dv','laugh'),('Алиса чуть улыбнулась.','dv','smile'),('Тихонова смутилась.','un','shy'),('Тихонова задумалась.','un','normal'),('Тихонова тихо улыбнулась.','un','smile'),('Женя приподняла бровь.','cs_zhenya','thinking'),('Она поправила очки.','cs_zhenya','glasses_touch')]:h.setdefault(w,pose(tag,p))
 if k in main:
  tag,p=main[k]
  for w in ('Она улыбнулась.','Она немного улыбнулась.','Потом улыбнулась.'):h.setdefault(w,pose(tag,p))
changes={
 'Даша, хочешь попробовать? Ты ведь вчера говорила, что раньше играла.':'Даша, хочешь ещё поиграть? Вчера у тебя хорошо получилось.',
 'Сегодня меня впервые за долгое время пустили в музыкальный клуб без обязательства уметь играть. Потом ещё и выяснилось, что здесь есть человек, с которым можно нормально поговорить о рисунках.':'Сегодня мы снова зашли в музыкальный клуб без обязательства уметь играть. А потом ещё и поговорили о рисунках.',
 'Я и правда уже почти забыла, как это приятно.':'После долгого перерыва приятно снова привыкать к клавишам.'}
def write(k,segments,pre=(),post=()):
 b=list(pre);transcript[k]=[]
 for x in segments:
  if isinstance(x,list):b+=x;continue
  text,depth=x;indent='    '*depth
  for who,w in parse(text):
   transcript[k].append((who,w));b += [indent+y for y in hooks.get(k,{}).get(w,[])]
   if k=='113' and w=='Славя не осталась один на один с бесконечными списками.':
    b+=['if cs_helped_sl_day3:','    cs_th '+json.dumps(w,ensure_ascii=False),'else:','    cs_th "К Славе заглянули и честно сказали, что у нас ещё есть свои дела."'];continue
   if k=='118' and who=='cs_da' and w=='Лена?':
    b+=['if cs_un_name_known:','    cs_da "Лена?"','else:','    cs_da "Та девушка тоже рисует?"'];continue
   if k=='118' and w=='Именно. Та, которую не нужно отличать от меня исключительно по фамилии, пока мы не оказались в одной комнате.':
    b+=['if cs_un_name_known:','    cs_ls '+json.dumps(w,ensure_ascii=False),'else:','    cs_ls "Да. Давай подойдём и познакомимся."'];continue
   if k=='118' and w=='Привет, тёзка.':
    b+=['if cs_un_name_known:','    cs_ls "Привет, тёзка."','else:','    cs_ls "Привет. Я Лена Соколова, а это Даша."','    cs_un "Лена. Тихонова."','    $ cs_un_name_known = True','    $ cs_met_un = True'];continue
   if k=='118' and w=='На рисунке была вчерашняя концертная площадка.':
    b+=['if cs_un_concert_sketch_seen:','    cs_narrator "Вчера Лена показала мне лишь быстрый набросок музыкантов. Теперь вокруг них появились сцена, скамейки и зрители."']
   if k=='118' and w=='Она тоже решила сохранить вчерашний вечер.':
    b+=['if cs_un_concert_sketch_seen:','    cs_th "Вчерашний быстрый набросок превращался в целую сцену."','else:','    cs_th '+json.dumps(w,ensure_ascii=False)];continue
   b.append(indent+who+' '+json.dumps(changes.get(w,w),ensure_ascii=False))
 b+=list(post)+['return'];title=parts[k.replace('a','А').replace('b','Б')][0]
 (D/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n',encoding='utf8')
def one(k,pre=(),post=()):write(k,[(parts[k][1],0)],pre,post)
t=parts['113'][1];base,t=t.split('**[ЕСЛИ `cs_mz_map_lead == True` И встреча по каталогам ещё не выполнена:]**');yes,no=t.split('**[ИНАЧЕ:]**')
write('113',[(base,0),['if cs_mz_map_lead and not cs_mz_catalog_checked_day3:'],(yes,1),['else:'],(no,1)],pre=frame('cs_camp_path_day')+['if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":','    play music "sound/music/my_daily_life.ogg" fadein 2.0','play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0','label cs_check_day03_113:'])
t=parts['113А'][1];base,t=t.split('**[ЕСЛИ `cs_mz_book_requested_day3 == True`:]**');yes,t=t.split('**[ИНАЧЕ:]**');no,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('113a',[(base,0),['if cs_mz_book_requested_day3:'],(yes,1),['else:'],(no,1),(tail,0)],pre=frame('bg ext_library_day')+['label cs_check_day03_113_library_exterior:','cs_narrator "Мы поднялись на библиотечное крыльцо."']+frame('bg int_library_day',[('cs_zhenya','normal')])+['$ renpy.music.set_volume(0.05,delay=1.0,channel="ambience")','$ renpy.music.set_volume(0.08,delay=1.0,channel="music")','label cs_check_day03_113_catalog:'])
t=parts['114'][1];base,t=t.split('**[ЕСЛИ `cs_mi_intro_revised == True`:]**');yes,t=t.split('**[ИНАЧЕ:]**');no,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('114',[(base,0),['if cs_mi_intro_revised:'],(yes,1),['else:'],(no,1),(tail,0)],pre=frame('bg ext_musclub_day')+['stop music fadeout 1.5','stop cs_piano fadeout 0.5','label cs_check_day03_114_exterior:'])
for n in ('115','117','119'):
 write(n,[(parts[n][1].split('**[ВЫБОР ИГРОКА:]**')[0],0)],post=['call cs_day03_'+{'115':'miku_arrangement_choice','117':'alice_music_choice','119':'un_art_choice'}[n]])
for n in ('115a','115b','116','117a','117b','119b'):
 write(n,[(parts[n.replace('a','А').replace('b','Б')][1],0)])
t=parts['118'][1];base,t=t.split('**[ЕСЛИ `cs_friend_un >= 2`:]**');high,t=t.split('**[ИНАЧЕ ЕСЛИ `cs_friend_un == 1`:]**');mid,t=t.split('**[ИНАЧЕ:]**');low,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('118',[(base,0),['if cs_friend_un >= 2:'],(high,1),['elif cs_friend_un == 1:'],(mid,1),['else:'],(low,1),(tail,0)],pre=focus(['mi','dv','cs_darya']))
t=parts['119А'][1];base,t=t.split('**[ЕСЛИ `cs_friend_un >= 2` ПОСЛЕ начисления нового очка:]**');yes,t=t.split('**[ИНАЧЕ:]**');no,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ ВЕТВИ.]**')
write('119a',[(base,0),['if cs_friend_un >= 2:'],(yes,1),['    $ cs_un_sketch_invite_day3 = True'],['else:'],(no,1),(tail,0)])
t=parts['120'][1];base,t=t.split('**[ЕСЛИ `cs_friend_sl >= 2`:]**');sl,t=t.split('**[ИНАЧЕ:]**',1);no,t=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**',1);middle,t=t.split('**[ЕСЛИ `cs_mz_map_lead == True` И `cs_mz_catalog_checked_day3 == True`:]**');cat,t=t.split('**[ИНАЧЕ ЕСЛИ `cs_mz_book_requested_day3 == True`:]**');book,t=t.split('**[ИНАЧЕ:]**');other,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('120',[(base,0),['if cs_friend_sl >= 2 and cs_helped_sl_day3:'],(sl,1),['else:'],(no,1),(middle,0),['if cs_mz_map_lead and cs_mz_catalog_checked_day3:'],(cat,1),['elif cs_mz_book_requested_day3:'],(book,1),['else:'],(other,1),(tail,0)])
flags=['cs_day03_part06_done','cs_day03_part06_started','cs_mz_catalog_checked_day3','cs_mi_day3_arrangement_help','cs_dv_music_talk_day3','cs_un_day3_art_talk','cs_un_sketch_invite_day3','cs_mi_day3_awarded','cs_dv_day3_awarded','cs_un_day3_awarded','cs_day03_lunch_horn_played','cs_day03_lunch_arrived']
(D/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+n+' = False\n' for n in flags)+'init -9 python:\n    cs_state_defaults.update('+', '.join(n+'=False' for n in flags)+')\n',encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day03_part06:
    if cs_day03_part06_done:
        jump cs_day03_part07_pending
    hide screen cs_day03_part05_wait_screen
    $ cs_day03_part05_done = True
    $ cs_day03_part06_started = True
    if cs_mz_catalog_checked_day3:
        $ cs_day03_library_visit_time = "after_lunch" if cs_mz_book_requested_day3 else None
    $ cs_day03_part06_route = "library_then_music" if cs_mz_map_lead and not cs_mz_catalog_checked_day3 else "music"
    call cs_day03_113
    if cs_mz_map_lead and not cs_mz_catalog_checked_day3:
        call cs_day03_113a
    call cs_day03_114
    call cs_day03_115
    call cs_day03_116
    call cs_day03_117
    call cs_day03_118
    call cs_day03_119
    call cs_day03_120
    $ cs_day03_part06_done = True
    jump cs_day03_part07_pending

'''
for who,number,positive,negative,event in [('mi','115','Послушать оба варианта и обсудить их с Мику','Не мешать репетиции и просто послушать','arrangement_help'),('dv','117','Спросить Алису о её игре и честно обсудить звучание','Сказать, что звучит хорошо, и не отвлекать','music_talk'),('un','119','Спросить Лену о её рисунке и поделиться опытом','Не мешать Лене заканчивать рисунок','art_talk')]:
 label={'mi':'miku_arrangement_choice','dv':'alice_music_choice','un':'un_art_choice'}[who]
 flag={'mi':'cs_mi_day3_arrangement_help','dv':'cs_dv_music_talk_day3','un':'cs_un_day3_art_talk'}[who]
 flow+='label cs_day03_'+label+':\n    label cs_check_day03_'+number+'_menu:\n    menu:\n        '+json.dumps(positive,ensure_ascii=False)+':\n            if not cs_'+who+'_day3_awarded:\n                $ cs_friend_'+who+' += 1\n                $ cs_'+who+'_day3_awarded = True\n            call cs_day03_'+number+'a\n            $ '+flag+' = True\n        '+json.dumps(negative,ensure_ascii=False)+':\n            call cs_day03_'+number+'b\n    label cs_check_day03_'+number+'_result:\n    return\n\n'
flow+='''label cs_day03_part07_pending:
    label cs_check_day03_part06_complete:
    jump cs_day03_part07

screen cs_day03_part06_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Три творческие натуры и одна Соколова" size 26
            text "Дальше — обед и разговоры в столовой." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
(D/'00_flow.rpy').write_text(flow,encoding='utf8')
(R/'source/day03_part06_transcript.json').write_text(json.dumps(transcript,ensure_ascii=False,indent=2),encoding='utf8')
print('Part6:',sum(map(len,transcript.values())),'manuscript blocks in',len(transcript),'scene files')
import runpy
runpy.run_path(str(R/'tools/apply_medpoint_continuity.py'))
