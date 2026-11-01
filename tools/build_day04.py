"""Day four manuscript compiler. Only owns day04; preserves earlier authored edits."""
from pathlib import Path
import json,re,shutil
from stabilize_call_helpers import preserve_calls
R=Path(__file__).resolve().parent.parent; P=R/'days/day04';P.mkdir(exist_ok=True)
S=(R/'source/day04.md').read_text(encoding='utf-8-sig')
a=re.split(r'^## Сцена (\d+)\. (.+)\n',S,flags=re.M)
scenes={a[i]:(a[i+1],a[i+2].split('## Редакторские замечания')[0]) for i in range(1,len(a),3)}
def q(t):return json.dumps(t,ensure_ascii=False)
def frame(bg,tags):return ['$ cs_director_scene('+q(bg)+')','scene '+bg,'$ cs_d4_scene_cast = '+repr(tags),'$ cs_frame_focus(cs_d4_scene_cast)','with Dissolve(0.7)']
def cast(tags):return ['$ cs_d4_scene_cast = '+repr(tags),'$ cs_frame_focus(cs_d4_scene_cast)','with cs_sprite_change']
def inward():return ['if not cs_reflective_shot:','    $ cs_pov_begin()','    with cs_sprite_leave']
def back():return ['if cs_reflective_shot:','    $ cs_frame_focus(cs_d4_scene_cast)','    with cs_sprite_change']
actors={'Лена Соколова':'cs_ls','Дарья':'cs_da','Даша':'cs_da','Семён':'cs_sy','Женя':'cs_mz','Виола':'cs_vi','Ольга Дмитриевна':'cs_mt','Славя':'cs_sl','Мику':'cs_mi','Алиса':'cs_dv','Электроник':'el'}
D=['cs_darya'];SE=['cs_semen'];Z=['cs_zhenya'];DS=D+SE;DZ=D+Z;TR=DZ+SE
edits={
 'Из-под одеяла выбивались короткие рыжие пряди. На стуле рядом лежала аккуратно сложенная пижама, а на спинке висело полотенце.':'Из-под одеяла выбивались рыжие пряди. На стуле рядом лежала аккуратно сложенная форма, а на спинке висело полотенце.',
 'Даша шла рядом, всё ещё не отпуская мою руку.':'Даша шла рядом и время от времени касалась моей здоровой руки.',
 'В другой руке я держала документы. Деревянная ножка стула до сих пор оставалась у меня, хотя практическая ценность этого предмета была уже под большим вопросом.':'Документы я несла под мышкой, прижав картон к боку. В здоровой руке всё ещё оставалась ножка стула, хотя практическая ценность этого предмета была уже под большим вопросом.',
 'Даша взяла ножку стула.':'Даша взяла ножку стула и оставила её у мусорной урны, подальше от прохода.',
 'Потом показала на ножку стула, которую Даша положила рядом со скамейкой.':'Потом кивнула в сторону урны, возле которой Даша оставила ножку стула.',
 'Там было совершенно темно. Телефона нет, никто не знает, куда я ушла. Если бы кто-то закрыл дверь или обрушилась лестница…':'Там было совершенно темно. Телефона нет, никто не знает, как глубоко я спустилась. Если бы кто-то закрыл дверь или обрушилась лестница…',
 'Я осторожно положила фотографии на стол, подальше от тазика с водой.':'Я осторожно положила фотографии на сухой край стола.',
 'Девушки отправились обратно в клуб, договорившись продолжить работу после обеда.':'Девушки вошли в столовую, договорившись продолжить работу после обеда.',
 'Давайте попробуем после обеда сыграть оба варианта. Возможно, длинное вступление действительно создаёт нужное настроение. А может, достаточно сократить переход.':'Сыграйте оба варианта и сравните. Возможно, длинное вступление действительно создаёт нужное настроение. А может, достаточно сократить переход. Я сейчас обещать, что успею послушать, не буду.',
 'Алиса протянула мне лист.':'Алиса протянула мне лист.',
 'Ты вчера вроде говорила, что иногда лучше убрать лишнее, чем добавлять новое?':'Ты ведь художница. Бывает, что лучше убрать лишнее, чем добавлять новое?',
 'Было дело.':'Бывает.',
 'Постараемся. После наших дел.':'Сегодня не обещаю: нужно разобраться с нашими делами. Давайте завтра, чтобы не заставлять вас ждать.',
 'Помню. Скоро у меня будет расписание творческих консультаций плотнее, чем у Слави.':'Помню. Давай завтра, если тебе удобно? Сегодня боюсь снова не успеть.',
 'Ты вчера обещала подобрать мне следующую книгу.':'Ты вчера говорила, что подберёшь мне следующую книгу. Если предложение ещё в силе, я бы попробовала.',
 'Я устроилась за привычным столом и открыла книгу.':'Я устроилась за свободным столом у окна и открыла книгу.',
 'Закрыла папку с документами на ключ.':'Проверила, что ящик с папкой заперт.',
 'Затем сняла с полки том Стругацких.':'Затем сняла с полки сборник научно-фантастических рассказов.',
 'Здесь герой рассказывает о месте, которое ему кажется знакомым, хотя он не должен был там бывать.':'Здесь герой возвращается к месту, которое помнил совсем другим. Невольно сравниваю с нашим лагерем.',
 'Сегодня утром я отправилась туда одна.':'Сегодня утром я отправилась туда одна.',
 'Но сейчас Семён спокойно идёт к своему домику.':'Но сейчас Семён спокойно ушёл к своему домику.',
 'Женя — к своему.':'Женя — к своему.',
}
# Explicit location and attention cues, tied to manuscript sentences, never every narration line.
before={
 '01':{'Дверь закрылась за моей спиной с тихим щелчком.':frame('cs_house_lena_darya_ext_night',[]),'Я направилась к площади.':frame('bg ext_square_night',[]),'Добравшись до спортивной площадки, я перешла на лёгкий бег.':frame('bg ext_playground_night',[]),'За спортивной площадкой я замедлилась.':frame('bg ext_path_day',[])+['stop music fadeout 1.0'],'На стене висели фотографии.':frame('cs_d4_old_corridor',[])},
 '02':{'Я осторожно вышла в коридор.':frame('cs_d4_old_corridor',[]),'Я подошла ближе.':frame('cs_d4_old_stairs',[])},
 '03':{'За дверью начинался короткий бетонный коридор.':frame('bg int_catacombs_entrance',[]),'Помещение напоминало небольшую мастерскую.':frame('bg int_catacombs_living',[]),'За ней начиналась ещё одна лестница.':frame('cs_d4_old_stairs',[]),'Я заглянула в тёмный проём.':frame('cs_d4_old_stairs',[]),'И свет погас.':frame('black',[]),'Там свет пока горел.':frame('bg int_catacombs_living',[]),'И обняла.':frame('cs_cg_lena_darya_bunker_reunion',[]),'Потом отстранилась, но осталась совсем рядом.':frame('cs_d4_old_stairs',[])},
 '04':{'Мы вышли на площадь.':frame('bg ext_square_day',SE)},
 '05':{'Внутри домика было всё так же спокойно, как утром.':frame('cs_house_lena_darya_int_day',[]),'Я вышла из-за ширмы.':['cs_narrator "Пока я приводила волосы в порядок, Даша тоже сменила спортивную куртку на пионерскую форму."']+cast(D),'Мы аккуратно сложили документы и вышли наружу.':frame('cs_house_lena_darya_ext_day',DS)},
 '06':{'Мы вошли.':frame('bg int_house_of_mt_day',['mt']+DS),'Осторожно положила её перед вожатой.':['stop music fadeout 2.0'],'Мы поднялись.':cast(['mt']),'Когда мы вышли, я ещё раз оглянулась.':frame('bg ext_house_of_mt_day',DS)},
 '07':{'Мы вошли в столовую.':frame('bg int_dining_hall_people_day',DS),'После завтрака Семён отправился по своим делам.':frame('cs_camp_path_day',[]),'Я подошла к двери.':cast(['cs']),'На улице оказалось заметно теплее.':frame('bg ext_aidpost_day',[])},
 '08':{'Возле музыкального клуба стояли Славя и Даша.':frame('bg ext_musclub_day',['sl']+D),'Мику заметила нас через открытую дверь.':cast(['sl','mi']+D),'Алиса появилась в дверях следом.':cast(['sl','dv']+D),'Некоторое время мы с Дашей стояли рядом со Славей.':cast(['sl']+D),'Мы с Дашей остались вдвоём.':cast(D),'Мы направились к столовой.':frame('bg ext_dining_hall_near_day',D),'У дверей нас догнали Алиса и Мику.':cast(['mi','dv']+D),'Мы с Дашей остались у столовой.':cast(D)},
 '09':{'Мы взяли еду и устроились у окна.':frame('bg int_dining_hall_people_day',DZ),'У выхода нас встретил Семён.':frame('bg ext_dining_hall_near_day',TR),'Мы попрощались с Семёном и направились в библиотеку.':frame('bg ext_library_day',DZ),'Я достала фотографию из папки за 1971 год.':['stop music fadeout 2.0']},
 '10':{'Свет постепенно менялся. Солнечные лучи уже падали под другим углом, освещая дальние стеллажи.':frame('cs_library_interior_evening',DZ),'Обложка была немного потёртой, но страницы сохранились хорошо.':['cs_narrator "На обложке значилось: Иван Тургенев, «Ася»."']},
 '11':{'И наконец я увидела знакомую фигуру.':frame('bg ext_square_sunset',TR+['el']),'Мы остались вчетвером.':cast(TR),'Мы вошли в столовую.':frame('bg int_dining_hall_sunset',TR),'Потом я вспомнила разговор в библиотеке.':['$ renpy.music.set_volume(0.13,channel="music",delay=1.5)'],'И вышли из столовой.':frame('bg ext_dining_hall_near_sunset',TR)},
 '12':{'Мы вошли.':frame('cs_library_interior_night',TR),'Мы вышли на крыльцо.':frame('cs_library_exterior_night',TR),'Мы остались втроём.':frame('bg ext_square_night',DS),'Даша стояла рядом.':cast(D),'Домик уже виднелся между деревьями.':frame('cs_house_lena_darya_ext_night',D),'Я открыла дверь.':frame('cs_house_lena_darya_int_night',D)}
}
inward_starts={'Я ещё немного посмотрела на неё.','И они от этого не исчезали.','Почему одни и те же имена встречаются в документах разных лет?','Постепенно строки начали складываться в образы.','Вот бы так ещё немного.','Она пришла раньше.','Всё словно пыталось сложиться в одну картину.','А потом на Женю.','Я пыталась понять, что именно услышала.','Сегодня утром я отправилась туда одна.','Я слушала и неожиданно почувствовала себя почти нормально.','Не физически.'}
begins={'01':frame('cs_house_lena_darya_int_sleep_night',[])+['$ night_time()','$ persistent.sprite_time = "night"','stop music'],
 '02':frame('cs_d4_old_corridor',[]), '03':frame('cs_d4_old_door',[]), '04':frame('bg ext_path_day',[])+['$ day_time()','$ persistent.sprite_time = "day"','play music cs_day_music_daily fadein 3.0'],
 '05':frame('cs_house_lena_darya_ext_day',SE), '06':frame('bg ext_house_of_mt_day',DS), '07':frame('cs_camp_path_day',DS)+['play music cs_day_music_daily fadein 2.0'],
 '08':frame('bg ext_square_day',[])+['play music cs_day_music_daily fadein 2.0'], '09':frame('bg ext_dining_hall_near_day',DZ),
 '10':frame('bg int_library_day',DZ)+['play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0'],
 '11':frame('cs_library_exterior_sunset',DZ)+['$ sunset_time()','$ persistent.sprite_time = "sunset"'],
 '12':frame('cs_library_exterior_sunset',TR)+['play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0']}
bg_cues={('01','старый корпус'): 'cs_d4_old_ext',('01','коридор заброшенного'): 'cs_d4_old_foyer',('07','дневной интерьер медпункта'):'bg int_aidpost_day',('09','дневной интерьер библиотеки'):'bg int_library_day'}
def condition(c):
 v=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',c.replace('`',''));assert v,c
 return ' and '.join(' '.join(x) for x in v)
stats={};audit=[]
expressions={
 'Рассказывай с самого начала.':('cs_semen','explaining pioneer normal'),
 'В следующий раз говори заранее. Хотя бы одному из нас.':('cs_semen','serious pioneer normal'),
 'А у меня есть выбор?':('cs_semen','awkward pioneer normal'),
 'Лен, ты уверена, что Ольге Дмитриевне нужно рассказывать всё сразу?':('cs_darya','thinking pioneer normal'),
 'У меня весьма широкий диапазон поведения.':('cs_darya','amused pioneer normal'),
 'Садись.':('cs','custom explaining medical normal'),
 'Что вы нашли, Лена?':('cs','custom thoughtful medical normal'),
 'Вот и хорошо.':('cs','custom warm_smile medical normal'),
 'Я не терялась.':('cs_darya','shrug pioneer normal'),
 'Показывай.':('cs_zhenya','arms_crossed pioneer normal'),
 'Я знаю, как выгляжу.':('cs_zhenya','glasses_touch pioneer normal'),
 'Кажется, я его слышала.':('cs_zhenya','thoughtful pioneer normal'),
 'Пока больше ничего не помню.':('cs_zhenya','normal pioneer normal'),
 'Мне интересно, что ты скажешь о героях.':('cs_zhenya','explaining pioneer normal'),
 'Я просто знаю, на что ты способна.':('cs_zhenya','shrug pioneer normal'),
 'Я здесь.':('cs_semen','serious pioneer normal'),
 'Была дорога.':('cs_semen','thinking pioneer normal'),
 'Я вспомнила ещё кое-что.':('cs_zhenya','thoughtful pioneer normal'),
 'Можно. Только недолго.':('cs_zhenya','shy pioneer normal'),
 'Сегодня опять вместе?':('cs_darya','shy_smile pioneer normal'),
}
def compile_tokens(ts,scene):
 b=[];depth=0;else_count=0;ifs=0;menu_done=False;i=0
 while i<len(ts):
  t=ts[i].strip().replace('**','');i+=1
  if not t:continue
  if t.startswith('### '):
   options=[];prelude=[];pad='    '*depth
   # A choice heading can introduce a scene before listing its options.
   # Compile that scene normally; skipping to option 1 loses the setup.
   while i<len(ts) and not re.match(r'[12]\\?\. ',ts[i]):
    prelude.append(ts[i]);i+=1
   assert i<len(ts),(scene,'Choice heading has no options')
   b += [pad+line for line in compile_tokens(prelude,scene)]
   while i<len(ts):
    m=re.match(r'[12]\\?\. «(.+?)»\.',ts[i]);assert m,ts[i];label=m[1];i+=1;body=[]
    while i<len(ts) and not re.match(r'[12]\\?\. ',ts[i]) and not ts[i].startswith(('[ОБЕ ВЕТВИ','[ОБЩЕЕ ПРОДОЛЖЕНИЕ')):body.append(ts[i]);i+=1
    options.append((label,body))
    if i>=len(ts) or ts[i].startswith(('[ОБЕ ВЕТВИ','[ОБЩЕЕ ПРОДОЛЖЕНИЕ')):break
   assert len(options)==2,(scene,options)
   b+=[pad+'if not cs_d4_choice_'+scene+'_done:']
   if scene=='09':b+=[pad+'    if cs_d4_mz_friend_before_choice is None:',pad+'        $ cs_d4_mz_friend_before_choice = cs_friend_mz']
   b+=[pad+'    menu:']
   for label,body in options:
    b+=[pad+'        '+q(label)+':']+[pad+'            '+line for line in compile_tokens(body,scene)]
   b+=[pad+'    $ cs_d4_choice_'+scene+'_done = True'];depth=0;continue
  pad='    '*depth
  if t.startswith('['):
   if t.startswith('[ЕСЛИ '):
    if scene=='01' and ifs==1:depth=1
    elif scene=='12' and 'cs_friend_da' in t:depth=1
    else:depth=0
    b+=['    '*depth+'if '+condition(t)+':'];depth+=1;ifs+=1;else_count=0
   elif t.startswith('[ИНАЧЕ ЕСЛИ'):
    b+=['    '*(depth-1)+'elif '+condition(t)+':']
   elif t.startswith('[ИНАЧЕ'):
    if scene=='01':
     else_count+=1;depth=2 if else_count==1 else 1
    b+=['    '*(depth-1)+'else:']
   elif t.startswith(('[ОБЩЕЕ ПРОДОЛЖЕНИЕ','[ОБЕ ВЕТВИ')):depth=0
   elif t.startswith(('[ФЛАГ:','[ФЛАГИ:','[ЭФФЕКТ:')):
    for var,op,val in re.findall(r'(cs_\w+)\s*(\+=|=)\s*(True|False|\d+)',t):b+=[pad+'$ '+var+' '+op+' '+val]
    if 'cs_d4_elbow_bandage_removed' in t:b += [pad+'$ cs_lena_elbow_bandaged = False']
    if 'cs_d4_olga_has_undated_photo' in t:b += [pad+'$ cs_d4_undated_photo_location = "olga"']
    if 'cs_d4_mz_has_1971_photo' in t:b += [pad+'$ cs_d4_photo1971_location = cs_d4_roster_location = "library_locked_drawer"']
    if 'cs_d4_dream_phrase_second' in t:b += [pad+'$ cs_d4_dream_notes_location = "library_locked_drawer"']
   elif t.startswith('[BG:'):
    for (sn,needle),bg in bg_cues.items():
     if scene==sn and needle in t:b += [pad+x for x in frame(bg,(['cs'] if scene=='07' else DZ if scene=='09' else []))]
   elif t.startswith('[MUSIC:') and ('убрать' in t or 'остановить' in t):b += [pad+'stop music fadeout 1.5']
   elif t.startswith('[SFX:') and 'сигнал' in t:b += [pad+'play sound sfx_dinner_horn_processed']
   continue
  if t.startswith(('## ','---')):continue
  t=t.replace('1971\\.','1971.').replace('1963\\.','1963.')
  # Explicit scene changes before the authored sentence.
  if t in before.get(scene,{}):b += [pad+x for x in before[scene][t]]
  if t in inward_starts:b += [pad+x for x in inward()]
  m=re.match(r'('+ '|'.join(map(re.escape,actors))+r')(?: \([^)]*\))?:\s*—\s*(.*)',t,re.S)
  who=actors[m[1]] if m else 'cs_d4_voice' if t.startswith('— ') else 'cs_narrator'
  line=m[2] if m else t[2:] if t.startswith('— ') else t
  line=edits.get(line,edits.get(t,line)).replace('\n',' ')
  if m:b += [pad+x for x in back()]
  # Authored emotional beats. Do not alternate poses on every line or question.
  if m and line in expressions:
   tag,attrs=expressions[line]
   b += [pad+'if renpy.showing('+q(tag)+') and renpy.get_attributes('+q(tag)+') != tuple('+q(attrs)+'.split()):',pad+'    show '+tag+' '+attrs,pad+'    $ cs_presence_stage()',pad+'    with cs_sprite_change']
  b += [pad+who+' '+q(line)]
  if scene in ('09','12') and t=='Я осторожно обняла её.':b += [pad+'$ cs_d4_mz_hug_'+scene+' = True']
  if scene=='02' and t=='Фотографию удалось поместить между ними, не сгибая.':b += [pad+'$ cs_d4_undated_photo_location = "lena"']
  if scene=='03' and t=='Находки поместила между листами картона рядом с первым снимком.':b += [pad+'$ cs_d4_photo1971_location = cs_d4_roster_location = "lena"']
  stats[scene]=stats.get(scene,0)+1
  if line!= (m[2] if m else t):audit.append(dict(scene=scene,source=t,result=line))
  if scene=='08' and t=='Славя рассмеялась.' and depth:
   pass
 return b
for sn,(title,body) in scenes.items():
 ts=[x.strip() for x in re.split(r'\n\s*\n',body) if x.strip()]
 b=begins[sn]+compile_tokens(ts,sn)
 if sn=='08':
  b+=['if cs_mi_followup_invitation_day3:','    $ cs_mi_followup_target_day = 5','if cs_dv_followup_invitation_day3:','    $ cs_dv_followup_target_day = 5','if cs_sl_day4_notice_offer:','    $ cs_d4_sl_notice_deferred = True']
 if sn=='10':b += ['$ cs_d4_new_book_location = "library_reading_table"']
 if sn=='12':b+=['$ cs_d4_shared_bed = cs_da_shared_bed_day3','cs_narrator "Мы по очереди умылись и переоделись ко сну. Разговоры наконец стихли."']+cast([])+['if cs_d4_shared_bed:']+['    '+x for x in frame('cs_cg_lena_darya_shared_sleep_night',[])]+['    cs_narrator "Даша устроилась рядом. Я почувствовала её спокойное дыхание и закрыла глаза."','else:','    cs_narrator "Мы легли каждая на свою кровать. Я пожелала Даше спокойной ночи и закрыла глаза."','stop music fadeout 2.0','stop ambience fadeout 2.0','window hide dissolve']+frame('black',[])+['show text "Конец четвёртого дня" at truecenter','with Dissolve(0.8)','$ renpy.pause(2.0)','hide text','with Dissolve(0.8)']
 text='# -*- coding: utf-8 -*-\nlabel cs_day04_'+sn+':\n    $ save_name = '+q('Чужая смена — День 4: '+title)+'\n'+'\n'.join('    '+x for x in b)+'\n    return\n'
 p=P/(sn+'_scene.rpy');p.write_text(preserve_calls(p.read_text(encoding='utf8'),text) if p.exists() else text,encoding='utf8')
defaults=dict(cs_day04_started=False,cs_day04_done=False,cs_d4_scene_cast=[],cs_d4_mz_friend_before_choice=None,cs_d4_new_book_location=None,cs_d4_shared_bed=False,cs_d4_sl_notice_deferred=False,cs_d4_mz_hug_09=False,cs_d4_mz_hug_12=False)
for n in ('01','04','06','07','08','09','12'):defaults['cs_d4_choice_'+n+'_done']=False
for name in set(re.findall(r'cs_d4_\w+',S)):
 if name not in defaults:defaults[name]=False
defaults.update(cs_d4_undated_photo_location=None,cs_d4_photo1971_location=None,cs_d4_roster_location=None,cs_d4_dream_notes_location=None)
images={'cs_d4_old_ext':'bg/old_camp/old_camp_exterior_morning.png','cs_d4_old_foyer':'bg/old_camp/old_camp_foyer_morning.png','cs_d4_old_corridor':'bg/old_camp/old_camp_corridor_right_turn.png','cs_d4_old_stairs':'bg/old_camp/old_camp_stairs_down.png','cs_d4_old_door':'bg/old_camp/old_camp_rust_metal_door.png','cs_cg_lena_darya_bunker_reunion':'cg/lena_n_dasha/cg_lena_darya_bunker_reunion_morning.png'}
resource='# -*- coding: utf-8 -*-\n'+''.join('default '+k+' = '+repr(v)+'\n' for k,v in sorted(defaults.items()))+'init -9 python:\n    cs_state_defaults.update('+', '.join(k+'='+repr(v) for k,v in sorted(defaults.items()))+')\n'
resource+='init 20 python:\n    cs_d4_voice = Character(None, what_style="normal_prolog", ctc="ctc_animation", ctc_position="fixed")\n'
resource+=''.join('image '+k+' = im.Scale(cs_resolve_asset('+q(v)+'),1920,1080)\n' for k,v in images.items())
(P/'resources.rpy').write_text(resource,encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day04:
    hide screen cs_day04_wait_screen
    if cs_day04_done:
        jump cs_day05_pending
    if not cs_day04_started:
        call cs_day_title(4)
    $ cs_day04_started = True
    window show dissolve
'''
for sn in scenes:
 flow+='    call cs_day04_'+sn+'\n'
 if sn=='03':flow+='    $ cs_d4_undated_photo_location = cs_d4_photo1971_location = cs_d4_roster_location = "lena"\n'
 if sn=='06':flow+='    $ cs_d4_undated_photo_location = "olga"\n'
 if sn=='10':flow+='    $ cs_d4_photo1971_location = cs_d4_roster_location = "library_locked_drawer"\n'
 if sn=='12':flow+='    $ cs_d4_dream_notes_location = "library_locked_drawer"\n'
flow+='''    $ cs_day04_done = True
    jump cs_day05_pending

label cs_day05_pending:
    label cs_check_day04_complete:
    call screen cs_day05_wait_screen
    jump cs_day05_pending

screen cs_day05_wait_screen():
    modal True
    frame:
        align (0.5,0.5)
        padding (32,24)
        background Solid("#142821ed")
        vbox:
            spacing 16
            text "Четвёртый день завершён" size 32
            text "Продолжение — в пятом дне." size 24
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
'''
p=P/'00_flow.rpy';p.write_text(preserve_calls(p.read_text(encoding='utf8'),flow) if p.exists() else flow,encoding='utf8')
# Preserve old wait label and screen for existing saves.
p=R/'days/day03/part14/00_flow.rpy';t=p.read_text(encoding='utf8');t=t.replace('    call screen cs_day04_wait_screen\n    jump cs_day04_pending','    jump cs_day04');t=t[:t.index('screen cs_day04_wait_screen():')]+'screen cs_day04_wait_screen():\n    timer 0.1 action Jump("cs_day04")\n';p.write_text(t,encoding='utf8')
(R/'source/day04_editorial.json').write_text(json.dumps(dict(scene_blocks=stats,edits=audit,resources=images),ensure_ascii=False,indent=2),encoding='utf8')
print('DAY04_GENERATED',len(scenes),'scenes;',sum(stats.values()),'blocks')

# Preserve the rebuilt costumes and new archive staging on regeneration.
if (R/"sp/darya_sport").is_dir():
    __import__("runpy").run_path(str(R/"tools/apply_rebuilt_day04_assets.py"))

__import__("runpy").run_path(str(R/"tools/apply_day04_continuity.py"))

# Apply reviewed prose last so camera/continuity anchors remain reproducible.
__import__("runpy").run_path(str(R/"tools/apply_day04_prose.py"))
