"""Compile the reviewed, indexed Day 5 manuscript; never rewrite earlier days."""
from pathlib import Path
import json,re,hashlib
from global_text_paging import page_source
ROOT=Path(__file__).resolve().parent.parent
P=(ROOT/'source/day05/manuscript.txt').read_text(encoding='utf-8').splitlines()
OUT=ROOT/'days/day05'; OUT.mkdir(parents=True,exist_ok=True)
def q(s): return json.dumps(s,ensure_ascii=False)
def write(name,s):
 (OUT/name).write_text(s,encoding='utf-8')
 if name.endswith('_scene.rpy'):page_source(ROOT,OUT/name)
# Explicit speaker attribution: two Lenas never share a character identifier.
speakers={}
speaker_indices={
'da':'51 55 59 63 67 72 74 79 82 86 101 181 214 222 244 259 291 341 355 359 361 363 365 370 373 377 379 383 385 387 392 470 491 506 532 538 554 578 592 594 604 632 646 680 700 792 797 840 899',
'sy':'90 95 99 102 105 109 111 113 116 118 122 127 162 184 233 242 262 268 271 277 279 282 286 288 292 345 442 467 495 524 541 575 598 628 638 661 686 703 766 768 773 779 782 786 794 843 861 865 870 877 895',
'mz':'134 136 140 147 149 152 156 158 164 166 206 212 217 236 238 303 305 310 313 316 321 324 329 332 335 452 550 559 563 599 665 669 672 708 862 886 905 919',
'mt':'171 175 177 180 182 185 189 191 193 195 200 296 620 627 629 693 699 701 704 723 731 809 833 871 890',
'un':'401 403 410 415 417 424 426 428 431 445 451 549 601 603 607 609 875 878 881 909 913 918',
'sl':'458 461 463 469 472 475 479 481 485 731 733 737',
'dv':'498 503 509 511 513 515 742 745',
'mi':'505 520 523 525 527 531 534 572 754',
'vi':'650 652 694 697 706 712 716 828 851',
'voice':'240 243 249 252 582 584 836 838 841 845 848 897 900 903 907',
}
for who,ids in speaker_indices.items():
 for i in map(int,ids.split()):
  assert P[i].startswith('—'),(i,P[i]); speakers[i]=who
# sl's arrival dialogue supersedes the generic adult map.
speakers[731]='sl'
speakers[640]='sy'
ROM='cs_da_shared_bed_day3 and cs_da_love_confession_day3'
# (exclusive branches, first index AFTER the complete conditional group)
B={}
def branch(start,end,*parts): B[start]=(end,parts)
branch(49,58,(ROM,50,53),(None,54,57))
branch(108,126,('cs_friend_se >= 4',109,117),('cs_friend_se >= 1',118,121),(None,122,125))
branch(187,198,('cs_d4_od_trust_approach',188,192),(None,193,197))
branch(308,338,('cs_friend_mz >= 4 and cs_d5_asked_address',309,319),('cs_friend_mz >= 4',320,327),(None,328,337))
branch(358,368,('cs_d5_shared_pace',359,362),(None,363,367))
branch(375,391,(ROM,376,381),('cs_friend_da >= 4',382,386),(None,387,390))
branch(422,435,('cs_friend_un >= 4',423,429),(None,430,434))
branch(448,455,('cs_friend_un >= 4',449,450),(None,451,454))
branch(478,490,('cs_friend_sl >= 4',479,484),(None,485,489))
branch(508,519,('cs_friend_dv >= 4',509,514),(None,515,518))
branch(521,537,('cs_friend_mi >= 4',522,529),(None,530,536))
branch(557,566,('cs_friend_mz >= 4',558,561),(None,562,565))
branch(570,577,('cs_d5_miku_volunteer',571,573),(None,574,576))
branch(605,617,('cs_friend_un >= 4',606,613),(None,614,616))
branch(663,676,('cs_d5_zhenya_address',664,670),(None,671,675))
branch(710,719,('cs_friend_viola >= 4',711,714),(None,715,718))
branch(729,740,('cs_friend_sl >= 4',730,735),(None,736,740))
branch(740,752,('cs_friend_dv >= 4',741,748),(None,749,752))
branch(752,761,('cs_friend_mi >= 4',753,757),(None,758,760))
branch(763,777,('cs_d5_semyon_agency',764,769),(None,770,776))
branch(777,781,('cs_friend_se >= 4 and not cs_d5_semyon_address',778,781))
branch(781,790,('cs_friend_se >= 4',782,785),(None,786,789))
branch(791,801,('cs_d5_shared_fear',792,796),(None,797,800))
branch(812,819,(ROM,813,814),('cs_friend_da >= 4',815,816),(None,817,818))
for a,b,cond in [(819,821,'cs_d5_slavya_present'),(821,823,'cs_d5_alisa_present'),(823,825,'cs_d5_miku_present')]: branch(a,b,(cond,a+1,b))
branch(864,874,('cs_friend_se >= 4',865,868),(None,869,873))
branch(879,889,('cs_d5_lena_private_memory',880,884),(None,885,888))
branch(911,922,('cs_d5_lena_respected',912,916),(None,917,921))
M={68:(85,[(69,71,77,['cs_friend_da += 1','cs_d5_shared_pace = True']),(77,79,84,['cs_d5_shared_pace = False'])]),
142:(160,[(143,145,153,['cs_friend_mz += 1','cs_d5_asked_address = True']),(153,155,159,['cs_d5_asked_address = False'])]),
274:(295,[(275,277,284,['cs_friend_se += 1','cs_d5_semyon_agency = True']),(284,286,294,['cs_friend_se -= 1','cs_d5_semyon_agency = False'])]),
405:(422,[(406,408,413,['cs_friend_un += 1','cs_d5_lena_respected = True']),(413,415,421,['cs_friend_un -= 1','cs_d5_lena_respected = False'])]),
633:(649,[(634,636,642,['cs_friend_da += 1','cs_friend_se += 1','cs_d5_shared_fear = True']),(642,644,648,['cs_d5_shared_fear = False'])])}
A={114:['cs_d5_semyon_address = True'],318:['cs_d5_zhenya_address = True'],325:['cs_d5_zhenya_address = True'],483:['cs_d5_slavya_volunteer = True'],488:['cs_d5_slavya_volunteer = False'],528:['cs_d5_miku_volunteer = True'],535:['cs_d5_miku_volunteer = False'],612:['cs_d5_lena_private_memory = True'],615:['cs_d5_lena_private_memory = False'],734:['cs_d5_slavya_present = True'],739:['cs_d5_slavya_present = False'],747:['cs_d5_alisa_present = True'],751:['cs_d5_alisa_present = False'],756:['cs_d5_miku_present = True'],759:['cs_d5_miku_present = False'],780:['cs_d5_semyon_address = True']}
SKIP={326,336,760,825,855,856,857}
# In-world paper inserts are screens over the scene, never a missing image name.
before={65:['$ cs_d5_costume("sport")','$ cs_d5_room("bg ext_square_day")'],66:['$ cs_d5_room("bg ext_playground_day")'],88:['$ cs_d5_room("bg ext_house_of_mt_day")'],186:['$ cs_d5_documents_location = "lena"'],198:['$ cs_d5_documents_location = "olga"'],213:['show screen cs_d5_insert("НЕ ОГЛЯДЫВАЙСЯ", "Обратная сторона таблички")'],218:['hide screen cs_d5_insert'],219:['$ cs_d5_room("bg ext_bus")'],226:['stop music fadeout 1.0'],435:['$ cs_d5_room("bg int_library_day")'],497:['$ cs_d5_room("bg ext_dining_hall_near_day")'],547:['$ cs_d5_documents_location = "library"'],566:['play sound cs_d5_seven_knocks'],595:['$ cs_d5_room("bg ext_library_day")'],597:['show screen cs_d5_insert("│ │ │ │ │ │ ╳", "Отметки на косяке")'],600:['hide screen cs_d5_insert'],676:['$ cs_d5_room("bg ext_dining_hall_near_sunset")'],719:['$ cs_d5_clock = "20:05"'],762:['$ cs_d5_room("bg ext_house_of_mt_night")'],790:['$ cs_d5_room("bg int_house_of_mt_night")'],801:['stop ambience fadeout 1.0'],807:['$ cs_d5_quiet = True','stop ambience fadeout 0.5','stop music fadeout 1.0','$ cs_d5_clock = "23:47"','show screen cs_d5_clock_face'],829:['$ cs_d5_clock = "23:59"'],831:['play sound cs_d5_seven_knocks'],832:['show expression Solid("#00081888") as cs_d5_darkness zorder 20','with Dissolve(0.6)'],852:['show screen cs_d5_insert("Семёну", "Конверт")'],854:['show screen cs_d5_insert("ОСТАТЬСЯ — ОДИН.\nВЕРНУТЬСЯ — ОДИН.\nВЫБИРАЕТ ПЕРВЫЙ", "Лицевая сторона карточки")'],859:['show screen cs_d5_insert("ТЫ УЖЕ ВЫБИРАЛ", "Оборот карточки")'],860:['hide screen cs_d5_insert'],924:['show screen cs_d5_insert("ПЕРВЫЙ ИЛИ ВТОРАЯ\nДО РАССВЕТА", "Надпись на внутренней двери")'],927:['hide screen cs_d5_insert']}
before[825]=['if not cs_d5_slavya_present:','    cs_narrator "Даша убрала термос от края стола."','if not cs_d5_alisa_present:','    cs_narrator "Ольга Дмитриевна взяла фонарик."','if not cs_d5_miku_present:','    cs_narrator "Виола проверила будильник."']
before[739]=['$ cs_actor_exit(["sl"])', '$ cs_d5_cast = []']
before[790]=[]
before[801].insert(0, '$ cs_d5_room("bg int_house_of_mt_night")')
before[933]=['$ cs_pov_begin()', 'with cs_sprite_leave', 'show screen cs_d5_notes']
before[522]=['play music cs_miku_piano_track fadein 0.5']
before[523]=['stop music fadeout 1.0']
before[295]=['$ cs_d5_room("cs_ext_administration_day")']
before[297]=['$ cs_d5_room("bg ext_washstand_day")']
before[760]=['if not cs_d5_slavya_present:','    cs_narrator "Славя передала дежурство по нашему отряду вожатой и присоединилась к обычному дежурству другого отряда."','if not cs_d5_miku_present or not cs_d5_alisa_present:','    cs_narrator "Ульяна обещала побыть с теми, кто сегодня не придёт в домик вожатой."']
# Continuity: originals start in the library drawer, not magically in Lena's bag.
REPLACE={174:'Я попросила сначала рассказать, что она сама вспомнила с вечера. Копии записей оставила в сумке: не хотелось подсовывать ответ вместе с вопросом.',186:'Это было лучше, чем уверенный ответ наугад. Я достала свои записи. Ольга Дмитриевна разложила на столе фотографии и список 1971 года: перед нашим приходом она забрала папку из запертого библиотечного ящика. Недатированный снимок всё это время оставался у неё.',198:'Оригиналы фотографий и списка остались у Ольги Дмитриевны. Я переписала дату и имена; Женя забрала свои записи.',85:'На турник я только посмотрела. Локоть, с которого вчера сняли повязку, напомнил о себе при разминке; спорить с ним сегодня не хотелось.',653:'Семён сложил свой листок вчетверо. На верхней стороне осталось его имя и нарисованный автобус.',654:'Когда он убрал бумагу, я перестала следить за его руками. Хотелось хотя бы перестать проверять его каждое движение.'}
META=re.compile(r'^(К оглавлению|Постановка:|Схождение|Общий текст|Если |Иначе|В обоих случаях|Очки |Дружба |day05_|Выбор |[АБ]\. )')
spoken=[]
emitted=[]
def emit_range(lo,hi,indent='    '):
 lines=[]; i=lo
 while i<hi:
  if i in B:
   end,parts=B[i]
   for n,(cond,a,b) in enumerate(parts):
    lines.append(indent+('else:' if cond is None else ('if ' if n==0 else 'elif ')+cond+':'))
    lines+=emit_range(a,b,indent+'    ')
   i=end; continue
  if i in M:
   end,opts=M[i]; lines.append(indent+'menu:')
   for title,a,b,actions in opts:
    label=re.sub(r'^[АБ]\.\s*','',P[title]).strip('«» .')
    lines.append(indent+'    '+q(label)+':')
    lines += [indent+'        $ '+v for v in actions]
    lines+=emit_range(a,b,indent+'        ')
   i=end;continue
  for v in before.get(i,[]):
   if v.startswith('show screen cs_d5_insert'):
    lines += [indent+'$ cs_pov_begin()',indent+'with cs_sprite_leave']
   lines.append(indent+v.replace('\n',r'\n'))
  for v in A.get(i,[]):lines.append(indent+'$ '+v)
  s=REPLACE.get(i,P[i])
  if i in SKIP or (META.match(s) and (ART is None or i not in ART)) or not s.strip():i+=1;continue
  emitted.append(i)
  if i in VARIANTS:
   condition,yes,no=VARIANTS[i]
   lines += [indent+'if '+condition+':',indent+'    cs_narrator '+q(yes)]
   if no is not None:lines += [indent+'else:',indent+'    cs_narrator '+q(no)]
   i+=1;continue
  if i in DIALOGUE or s.startswith('—'):
   who=speakers.get(i,'ls');spoken.append((i,who))
   # Attribution is already conveyed by the nameplate; retain all spoken clauses.
   if i in DIALOGUE:
    s=DIALOGUE[i][1]
   else:
    s=s[1:].strip()
    s=re.sub(r'\s*—\s*(?:спросил[аи]?|сказал[аи]?|ответил[аи]?|признал[асясь]+|объяснил[аи]?|добавил[аи]?|попросил[аи]?|уточнил[аи]?|предупредил[аи]?|пояснил[аи]?|согласил[асясь]+|заметил[аи]?|донеслось)[^—]*?(?:\.\s*—\s*|\.\s*$)', ' ', s).strip()
    s=s.rstrip(', ') + ('.' if s.endswith(',') else '')
   lines += [indent+'$ cs_d5_focus('+q(who)+')',indent+'with cs_sprite_change',indent+('cs_d5_voice' if who=='voice' else 'cs_'+who)+' '+q(s)]
  else:
   if i in THOUGHTS or (ART is None and len(s)>210):lines += [indent+'$ cs_pov_begin()',indent+'with cs_sprite_leave']
   lines.append(indent+('cs_th ' if i in THOUGHTS else 'cs_narrator ')+q(s))
  i+=1
 return lines
SCENES=[(45,48,91,'cs_house_lena_darya_int_day'),(91,94,130,'bg ext_house_of_mt_day'),(130,133,167,'bg int_dining_hall_people_day'),(167,170,202,'bg int_house_of_mt_day'),(202,205,224,'bg ext_no_bus'),(224,227,264,None),(264,267,299,'cs_camp_path_day'),(299,302,348,'bg int_library_day'),(348,351,394,'bg ext_playground_day'),(394,397,437,'bg ext_library_day'),(437,440,464,'bg int_dining_hall_people_day'),(464,467,499,None),(499,502,544,'bg int_musclub_day'),(544,547,587,'bg int_library_day'),(587,590,622,None),(622,625,655,'bg int_library_day'),(655,658,689,'bg int_dining_hall_sunset'),(689,692,724,'bg int_house_of_mt_sunset'),(724,727,804,'bg int_house_of_mt_night'),(804,807,936,None)]
from day05_expanded_layer import apply_expanded
P,B,M,A,SKIP,before,REPLACE,SCENES,speakers=apply_expanded(ROOT,P,B,M,A,SKIP,before,REPLACE,SCENES,speakers)
from day05_adv_layer import apply_adv
P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,ART,THOUGHTS=apply_adv(ROOT,P,B,M,A,SKIP,before,REPLACE,SCENES,speakers)
from day05_pov_layer import apply_pov
P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,ART,THOUGHTS,DIALOGUE=apply_pov(ROOT,P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,ART,THOUGHTS)
from day05_literary_layer import apply_literary
P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,ART,THOUGHTS,DIALOGUE,VARIANTS=apply_literary(ROOT,ROM)
from day05_corrected_layer import apply_corrected
P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,ART,THOUGHTS,DIALOGUE,VARIANTS=apply_corrected(ROOT,ROM)
for num,(title,lo,hi,bg) in enumerate(SCENES,1):
 lines=['# -*- coding: utf-8 -*-','label cs_day05_%02d:'%num,'    $ cs_d5_scene = '+str(num),'    $ save_name = '+q('Чужая смена — День 5: '+P[title].split(' ',2)[2])]
 lines+=['    $ cs_bus_scene_enter('+str(num)+')']
 if bg:lines+=['    $ cs_d5_room('+q(bg)+')','    with Dissolve(0.7)']
 if num==1:lines+=['    $ day_time()','    $ persistent.sprite_time = "day"','    stop music fadeout 1.0']
 if num==3:lines+=['    $ cs_d5_costume("pioneer")','    $ cs_rev_music(cs_day_music_daily)']
 if num==17:lines+=['    $ sunset_time()','    $ persistent.sprite_time = "sunset"']
 if num in (18,19):lines+=['    $ night_time()','    $ persistent.sprite_time = "night"']
 if num in (5,6,14,18,20):lines+=['    stop music fadeout 1.0']
 if num==20:lines+=['    stop ambience fadeout 0.5']
 lines+=emit_range(lo,hi)+['    return','']
 write('%02d_scene.rpy'%num,'\n'.join(lines))
flags='shared_pace asked_address zhenya_address semyon_address semyon_agency lena_respected lena_private_memory shared_fear slavya_volunteer miku_volunteer slavya_present alisa_present miku_present started done quiet dressed run_finished offscreen_exchange literary_initialized library_meeting_invited zhenya_cabinet_memory address_talk_agreed clock_stopped heard_offscreen pajamas_visible zhenya_personal_note repeat_trip_record lena_dream_shared_early un_day6_sketch_offer alisa_dream_full viola_early_note notice_completed miku_intro_heard'.split()
defaults={**{'cs_d5_'+f:False for f in flags},'cs_d5_documents_location':'library_locked_drawer','cs_d5_clock':'21:00','cs_d5_cast':[],'cs_d5_scene':0,'cs_d5_outfit':'pioneer'}
defaults['cs_d5_choice_results']={}
defaults['cs_d5_pajama_mood']='sleepy'
head='# -*- coding: utf-8 -*-\n'+''.join('default %s = %r\n'%(k,v) for k,v in defaults.items())
head+='init -9 python:\n    cs_state_defaults.update('+', '.join('%s=%r'%(k,v) for k,v in defaults.items())+')\n'
write('resources.rpy',head+'\n'+(ROOT/'tools/day05_corrected_runtime.rpy.txt').read_text(encoding='utf-8'))
flow=['# -*- coding: utf-8 -*-','label cs_day05:','    hide screen cs_day05_wait_screen','    if cs_d5_done:','        jump cs_day05_complete','    if not cs_d5_started:','        call cs_day_title(5) from cs_d5_title_return','    $ cs_d5_started = True','    window show dissolve']
for n in range(1,21):flow+=['    call cs_day05_%02d from cs_d5_scene_%02d_return'%(n,n)]
flow+=['    $ cs_d5_done = True','label cs_day05_complete:','    label cs_check_day05_complete:','    call screen cs_day05_end_screen','    jump cs_day05_complete','', 'screen cs_day05_end_screen():','    modal True','    frame:','        align (0.5, 0.5)','        padding (32, 24)','        background Solid("#142821ed")','        vbox:','            spacing 16','            text "Конец пятого дня" size 32','            text "Продолжение следует" size 24','            textbutton "Сохранить игру" action ShowMenu("save")','            textbutton "Загрузить игру" action ShowMenu("load")','            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]','']
write('00_flow.rpy','\n'.join(flow))
(ROOT/'source/day05/speakers.json').write_text(json.dumps(dict(spoken),ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'source/day05/emitted_paragraphs.json').write_text(json.dumps(emitted),encoding='utf-8')
if ART is not None:
 assert set(emitted)==ART,('ADV paragraph coverage',sorted(ART-set(emitted)),sorted(set(emitted)-ART))
 assert len(emitted)==len(set(emitted)), 'Duplicated ADV paragraph'
print('Day 5: 20 scenes, 5 menus, %d attributed dialogue paragraphs'%len(spoken))
# Old wait-screen saves enter the new episode through their existing label.
p=ROOT/'days/day04/00_flow.rpy'; s=p.read_text(encoding='utf-8')
s=s.replace('    call screen cs_day05_wait_screen\n    jump cs_day05_pending','    jump cs_day05')
start=s.index('screen cs_day05_wait_screen():')
s=s[:start]+'screen cs_day05_wait_screen():\n    timer 0.1 action Jump("cs_day05")\n'
p.write_text(s,encoding='utf-8')
p=ROOT/'day03_location_audio.rpy';s=p.read_text(encoding='utf-8')
anchor='    def cs_day03_audio_target(image):\n'
if 'getattr(store, "cs_d5_quiet", False)' not in s:
 s=s.replace(anchor,anchor+'        if getattr(store, "cs_d5_quiet", False) and getattr(store, "cs_d5_started", False):\n            return None\n')
p.write_text(s,encoding='utf-8')

