"""Library, square and drawing: authored text split into small scene files."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
transcript={};edits=[]
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
def reflect():return ['$ cs_pov_begin()','with cs_sprite_leave']
def back():return ['$ cs_pov_end()','with cs_sprite_change']
def leave(tags):return ['$ cs_actor_exit('+json.dumps(tags)+')','with cs_sprite_leave']
def frame(bg,tags=()):return ['$ cs_director_scene("'+bg+'")','scene '+bg,'$ cs_frame_focus('+json.dumps(list(tags))+')','with Dissolve(0.7)']
def pose(tag,emotion):
    attrs=' pioneer normal' if tag in ('cs_darya','cs_semen','cs_zhenya') else ' pioneer'
    return ['if renpy.showing("'+tag+'"):', '    show '+tag+' '+emotion+attrs,'    $ cs_presence_stage()','    with cs_sprite_change']
speakers={'Женя':'cs_mz','Дарья':'cs_da','Семён':'cs_sy','Лена Соколова':'cs_ls','Лена Тихонова':'cs_un','Славя':'cs_sl'}
def parse(block):
    m=re.match(r'(Лена Соколова(?: \([^)]*\))?|Лена Тихонова|Дарья|Женя|Семён|Славя):\\?\s*[\n ]+[—–]\s*(.*)',block,re.S)
    if m:return speakers[re.sub(r' \(.*','',m[1])],m[2].replace('\n',' ')
    return 'cs_narrator',block.replace('\n',' ')
def load(part):
    s=(R/f'source/day03_part{part:02d}.md').read_text(encoding='utf-8-sig')
    s=s[s.index('### Сцена '):s.index('### Техническое задание' if part==8 else '## Техническое задание')]
    a=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)\n',s)
    return {a[i].replace('А','a').replace('Б','b'):(a[i+1],a[i+2]) for i in range(1,len(a),3)}
sources={8:load(8),9:load(9)}
def cond(part,k,block):
    if k=='140a':return 'cs_se_friend_before_square_day3 >= '+('1' if block.startswith('[ИНАЧЕ') else '2')
    if k=='141':return 'cs_se_friend_before_square_day3 >= 2 and cs_un_sketch_time_agreed_day3'
    vals=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',block)
    c=' and '.join(' '.join(v) for v in vals).replace(' == True','')
    assert c,block
    if part==8 and k not in ('128','136'):c=c.replace('cs_friend_mz','cs_mz_friend_on_arrival_day3')
    if k in ('136','138'):c=c.replace('cs_friend_mz','cs_mz_friend_on_arrival_day3')
    if k=='136':c=c.replace('cs_mz_friend_on_arrival_day3 >= 2','cs_mz_friend_on_arrival_day3 >= 1')  # inner 'выбрала/помогла выбрать' split stays reachable
    if k=='132':c+=' and cs_helped_sl_day3'
    if k=='143' and 'poster' in c:c+=' and cs_day03_poster_location == "darya_folder"'
    return c

# Explicit inward shots are grouped beats, never a response to each sentence.
hooks={
 '128':{'Я остановилась возле знакомого здания.':frame('bg ext_library_day')},
 '132':{'Славя.':focus(['cs_zhenya','sl']), 'Славя вскоре попрощалась.':leave(['sl'])},
 '133':{'Соколова.':back()+focus(['cs_zhenya']),
        'В этот момент я вдруг поймала себя на мысли, что сказала больше, чем собиралась.':reflect(),
        'Женя заметила мою задумчивость.':back()},
 '134a':{'Мне нравится, что автор не пытается сделать одного героя полностью правым.':pose('cs_zhenya','explaining')},
 '134b':{'Я продолжила читать.':['$ cs_reflective_focus()','with cs_sprite_leave']},
 '135':{'Она что-то записывала.':focus(['cs_zhenya']),
        'Она внесла запись.':['label cs_check_day03_135_loan:','$ cs_mz_book_borrowed_day3 = True','$ cs_day03_reading_book_location = "lena"'],
        'Вот и всё.':reflect(), 'Я направилась к выходу.':back(),
        'Дверь тихо закрылась за моей спиной.':frame('bg ext_library_day')+['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.5']},
 '136':{'Дарья: — Лен!':[], 'Лен!':focus(['cs_darya'])+pose('cs_darya','wave'),
        'И почти сразу увидела Дашу.':focus(['cs_darya'])},
 '137':{'И мы направились к Семёну.':focus(['cs_darya','cs_semen'])+pose('cs_semen','neutral')},
 '140a':{'Он немного помолчал.':pose('cs_semen','thinking')},
 '141':{'И направились к домикам.':leave(['cs_semen'])},
 '142':{'Интересная вещь.':reflect(), 'А что насчёт его прозвища?':back()},
 '143':{'И вошла следом.':frame('cs_house_lena_darya_int_day',['cs_darya']),
        'Положила книгу.':['$ cs_day03_reading_book_location = "house_table"'],
        'Дарья положила на стол папку с нашим концертным плакатом.':['$ cs_day03_poster_location = "house_table"','$ cs_day03_poster_stored_home = True'],
        'Если вернёмся.':reflect(),'Я достала из своих вещей небольшой блокнот.':back()},
 '144':{'Лена Тихонова уже стояла возле деревьев с альбомом в руках.':focus(['un']),
        'Тихонову я встретила возле клубов.':focus(['un']),
        'Интересно.':reflect(), 'Тихонова первой нарушила молчание.':back(),
        'Вокруг продолжалась обычная лагерная жизнь.':reflect(),'Тихонова вдруг посмотрела на мой блокнот.':back(),
        'Мы вернулись к работе.':pose('un','normal'),
        'И разошлись по дорожкам.':leave(['un'])},
 '145':{'Мы вышли из домика.':frame('cs_camp_path_day',['cs_darya']),
        'Она направилась к клубам.':['$ cs_day03_darya_destination = "music_club"']+leave(['cs_darya'])},
}
hooks.setdefault('140',{})['Интересный всё-таки человек.']=reflect()
hooks.setdefault('130',{})['Положила книгу перед собой.']=['if not cs_day03_hint_album_seen:',
 '    cs_narrator "Женя, не поднимая головы, добавила:"',
 '    cs_mz "Кстати. Разбирала карточки и нашла запись про фотоальбом старых смен."',
 '    cs_mz "Его когда-то передали в старый корпус. Не знаю, остался ли он там."',
 '    $ cs_day03_hint_album_seen = True']
# Speaker-less interior paragraphs in the supplied prose remain thoughts, not
# spoken disclosures to Zhenya. Camera cues above are authored separately.
force_narrator={'131':{'Я чуть улыбнулась.'},'133':{'Я посмотрела в окно.','На солнечную дорожку.','На деревья.','На пионеров, проходивших мимо.'}}
inner_ranges={
 '129':[('Кратко.','Вполне в её стиле.'),('Ну что ж.','Осталось главное — книга.')],
 '130':[('Хм.','Звучит подозрительно актуально.'),('Что ж.','Посмотрим, чем ты собираешься меня удивлять, товарищ Гончаров.')],
 '131':[('Забавно.','Только литературный.'),('Вот что мне нравится.','Причём на этот раз хотя бы добровольно.'),('Да уж.','Учитывая, что предыдущая история сама затянула тебя внутрь.'),('Нет.','Для этого будет другой день.')],
 '133':[('Решения имеют цену.','Не поиски выхода.')],
 '137':[('Надо же.','Практически музейный.'),('Чёрт.','Слишком хорошо меня знает.'),('Ну вот.','Хотя, конечно, с моей подачи это почти никогда не получается с первого раза.')],
 '140':[('Интересный всё-таки человек.','В конце концов, он явно пришёл сюда немного отдохнуть.')],
 '142':[('Интересная вещь.','А иногда способным сказать что-нибудь настолько обычное и искреннее, что вся моя заранее подготовленная ирония становилась неуместной.')],
 '143':[('Если вернёмся.','Хочется верить, что однажды мы действительно сможем поставить её у себя дома.')],
}
for k in list(sources[8])+list(sources[9]):
    h=hooks.setdefault(k,{})
    for text,p in [('Женя поправила очки.','glasses_touch'),('Женя усмехнулась.','shrug'),('Женя задумалась.','thinking'),('Женя слегка улыбнулась.','normal')]:h.setdefault(text,pose('cs_zhenya',p))
    for text,p in [('Дарья рассмеялась.','amused'),('Дарья улыбнулась.','shy_smile'),('Дарья покачала головой.','shrug'),('Дарья задумалась.','thinking')]:h.setdefault(text,pose('cs_darya',p))
    for text,p in [('Семён усмехнулся.','smile'),('Семён задумался.','thinking'),('Семён пожал плечами.','explaining'),('Семён рассмеялся.','relaxed'),('Семён прищурился.','serious')]:h.setdefault(text,pose('cs_semen',p))
    for text,p in [('Тихонова немного смутилась.','shy'),('Тихонова чуть улыбнулась.','smile'),('Она тихо рассмеялась.','smile')]:
        if k=='144':h.setdefault(text,pose('un',p))

def edit(k,who,w):
    own_choice={
      'Ничего. Просто подумала, что ты удачно выбрала книгу.':'Ничего. Просто подумала, что удачно взяла именно эту книгу.',
      'Спасибо, Женя. Хорошую книгу выбрала.':'Спасибо, Женя. Хорошо, что можно спокойно почитать.',
      'А можно немного подробнее поговорить о том, почему именно она выбрала эту историю.':'А можно подробнее поговорить о том, что ей самой нравится в этой истории.',
    }
    if w in own_choice:
        return ['if cs_mz_friend_on_arrival_day3 >= 1:', '    '+who+' '+json.dumps(w,ensure_ascii=False),
                'else:', '    '+who+' '+json.dumps(own_choice[w],ensure_ascii=False)]
    changes={
 'Только локоть береги.':'Увидимся позже.',
 'Даша, у меня скоро появится коллекция напоминаний. Можно будет издать отдельной книгой.':'Постараюсь не потеряться.',
     'Кстати, раз уж мы заговорили о рисовании…':'Кстати, о планах на вечер…',
     'Ты вчера говорила, что тебе интересны персонажи. Особенно когда они меняются по ходу истории.':'Сегодня мы говорили об историях, где важны люди и их решения. Здесь как раз можно проследить, как человек меняется.',
     'Ты говорила, что любишь истории про людей?':'Хочешь попробовать историю про людей и их решения?',
     'Можно взять эту?':'Можно почитать эту здесь?',
     'Можно. Только запишу.':'Можно. Если решишь унести с собой, подойди — запишу выдачу.',
     'Она внесла запись в журнал и вернула том.':'Она проверила переплёт и вернула мне том.',
     'И самое главное — Женя сама подобрала книгу.':None,
     'Мы обаятельно переглянулись.':'Мы улыбнулись друг другу.',
     'Тогда заглянем. Не сегодня прямо сейчас, но немного позже.':'Тогда заглянем. Не прямо сейчас, но немного позже.',
     'Но и дядя у него не производит впечатления человека, который обязательно прав только потому, что уже успел во всём разочароваться.':'Но и дядя у него не обязательно прав только потому, что старше и считает себя практичным человеком.',
     'Ты не стараешься сразу прорисовать каждую деталь. Но уже понятно, какой получится картинка.':'Ты не стараешься сразу прорисовать каждую деталь. Но уже понятно, какая получится картинка.',
     'Вчера ещё клеили этот плакат и спорили о надписях.':'Вчера ещё готовили этот плакат и спорили о надписях.',
     'В конце концов, художник должен иногда вспоминать о своём существовании не только при изготовлении концертных плакатов.':'В конце концов, художнику иногда стоит рисовать просто для себя.',
     'Лена Тихонова уже стояла возле деревьев с альбомом в руках.':'Тихонова шла от клуба с альбомом. Заметив меня, она замедлила шаг возле деревьев.',
    }
    if w=='Знакомо. Я сегодня помогала считать медицинские материалы.':
        return ['if cs_helped_viola_day3:', '    cs_ls '+json.dumps(w,ensure_ascii=False),'else:',
                '    cs_ls "Знакомо. Сегодня была у Виолы с локтем. Она меня от лишней работы пока освободила."']
    if w=='Да. Если договорённость с Тихоновой ещё в силе.':
        return ['if cs_un_sketch_time_agreed_day3:', '    cs_ls '+json.dumps(w,ensure_ascii=False),'else:', '    cs_ls "Да. Немного порисую сама."']
    if w=='Я сегодня с Тихоновой обсуждала её рисунки. Возможно, ближе к вечеру вместе что-нибудь нарисуем.':
        return ['if cs_un_sketch_time_agreed_day3:', '    cs_ls '+json.dumps(w,ensure_ascii=False),'else:', '    cs_ls "Утром видели Тихонову с альбомом. Я вот тоже хочу сегодня порисовать."']
    if w=='И самое главное — Женя сама подобрала книгу.':
        return ['if cs_mz_friend_on_arrival_day3 >= 1:', '    cs_ls '+json.dumps(w,ensure_ascii=False),'else:', '    cs_ls "Сама нашла на полке. И, кажется, удачно."']
    if w=='Женя выбрала для меня книгу.':
        return ['if cs_mz_friend_on_arrival_day3 >= 2:', '    cs_narrator '+json.dumps(w,ensure_ascii=False),'else:', '    cs_narrator "Женя помогла мне выбрать книгу."']
    if w in changes and changes[w] is not None:
        edits.append(dict(scene=k,before=w,after=changes[w]));w=changes[w]
    return [who+' '+json.dumps(w,ensure_ascii=False)]

flag_actions={
 '135': ['$ cs_mz_open_library_invitation_day3 = True'],
 '141': ['$ cs_se_sketch_spot_day3 = True'],
}
def generate(part,k,pre=(),post=()):
    title,t=sources[part][k];b=list(pre);depth=0;open_if=False;transcript[k]=[]
    if k in ('134','140'):t=t.split('Выбор игрока:')[0].split('[ВЫБОР ИГРОКА]')[0]
    if k=='128':
        a=t.index('Женя действительно отложила');z=t.index('Я остановилась возле знакомого здания.')
        t=t[:a]+'[ЕСЛИ cs_mz_book_prepared_day3 == True:]\n\n'+t[a:z]+'[ИНАЧЕ:]\n\nХотелось просто выбрать книгу и немного почитать. Без поручений и попыток найти ответы в каждом шкафу.\n\n[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]\n\n'+t[z:]
    inward=False
    for block in re.split(r'\n\s*\n',t):
        block=block.strip()
        if not block or block=='---' or block.startswith(('#','- ','* ','1\\.','2\\.')):continue
        if block.startswith('['):
            if block.startswith('[ЕСЛИ ') and block.endswith(':]'):
                c=cond(part,k,block);b+=['if '+c+':'];depth=1;open_if=True
            elif block.startswith('[ИНАЧЕ ЕСЛИ '):b+=['elif '+cond(part,k,block)+':'];depth=1
            elif block.startswith('[ИНАЧЕ:'):b+=['else:'];depth=1
            elif block.startswith('[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0;open_if=False
            elif block.startswith('[ФЛАГ:'):
                a=[]
                if k=='135':a=flag_actions[k]
                if k=='141':a=flag_actions[k]
                if k=='144' and 'cs_un_private_drawing_shown_day3 = True' in block:a=['$ cs_un_private_drawing_shown_day3 = True']
                if k=='144' and 'cs_un_sketch_completed_day3 = True' in block:a=['$ cs_un_sketch_completed_day3 = True']
                b+=['    '*depth+x for x in a]
            continue
        who,w=parse(block)
        if any(w==a for a,z in inner_ranges.get(k,[])):inward=True
        if inward and who=='cs_narrator':who='cs_th'
        if w in force_narrator.get(k,()):who='cs_narrator'
        transcript[k].append([who,w])
        b+=['    '*depth+x for x in hooks.get(k,{}).get(w,[])]
        b+=['    '*depth+x for x in edit(k,who,w)]
        if any(w==z for a,z in inner_ranges.get(k,[])):inward=False
    b+=list(post)+['return']
    folder=R/f'days/day03/part{part:02d}';folder.mkdir(parents=True,exist_ok=True)
    label='cs_day03_128_path' if k=='128' else 'cs_day03_'+k
    (folder/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel '+label+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n',encoding='utf8')

generate(8,'128',pre=frame('cs_camp_path_day')+['play music "sound/music/my_daily_life.ogg" fadein 2.0','$ renpy.music.set_volume(0.12,delay=1.0,channel="music")'])
generate(8,'129',pre=[
 'if cs_mz_friend_on_arrival_day3 is None:','    $ cs_mz_friend_on_arrival_day3 = cs_friend_mz',
 '$ cs_day03_library_legacy_bridge = cs_day03_reading_book_id == "paustovsky_warm_bread"',
 ]+frame('bg int_library_day',['cs_zhenya'])+['stop ambience fadeout 1.5','play music cs_day_music_home fadeout 2.0 fadein 2.0','$ renpy.music.set_volume(0.08,delay=1.0,channel="music")',
 'label cs_check_day03_128_library:',
 'if cs_day03_library_legacy_bridge:',
 '    cs_narrator "Я отложила сборник Паустовского, который только успела полистать. Женя подняла голову от записей."',
 '    cs_mz "Можешь посмотреть ещё один вариант. Роман Гончарова. Только первый сборник оставь здесь."',
 '    jump cs_day03_129_seated'],post=['label cs_day03_129_seated:','pass'])
generate(8,'130',pre=['if cs_day03_novel_selected:','    cs_narrator "Роман уже лежал передо мной. Я вернулась к отмеченной странице."','    return'],post=[
 '$ cs_day03_novel_selected = True','$ cs_day03_reading_book_selected = True','$ cs_day03_reading_book_id = "goncharov_ordinary_story"','$ cs_day03_reading_book_location = "library_reading_table"','label cs_check_day03_130_selected:','pass'])
generate(8,'131',pre=['$ cs_reflective_focus()','with cs_sprite_leave','stop music fadeout 3.0'])
generate(8,'132',post=['$ cs_reflective_focus()','with cs_sprite_leave'])
generate(8,'133',pre=['play music cs_day_music_home fadein 2.0','$ renpy.music.set_volume(0.08,delay=1.0,channel="music")'])
generate(8,'134');generate(8,'134a',pre=focus(['cs_zhenya']));generate(8,'134b',pre=focus(['cs_zhenya']))
generate(8,'135',pre=['if cs_mz_book_borrowed_day3:','    return','$ cs_reflective_focus()','with cs_sprite_leave'])
generate(8,'136',pre=frame('cs_camp_path_day')+['play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0','$ renpy.music.set_volume(0.12,delay=1.0,channel="music")'],post=[
 'if cs_sl_poster_collected_day3 and cs_day03_poster_location == "darya_folder":',
 '    cs_narrator "Папку с плакатом Даша несла под мышкой: из клуба она забрала её с собой."'])

generate(9,'137',pre=frame('bg ext_square_day',['cs_darya']))
generate(9,'138')
generate(9,'139',pre=['$ renpy.music.set_volume(0.06,delay=1.0,channel="music")'])
generate(9,'140',pre=['if cs_se_friend_before_square_day3 is None:','    $ cs_se_friend_before_square_day3 = cs_friend_se'],post=back())
generate(9,'140a');generate(9,'140b')
generate(9,'141')
generate(9,'142',pre=frame('cs_camp_path_day',['cs_darya'])+['$ renpy.music.set_volume(0.12,delay=1.0,channel="music")'])
generate(9,'143',pre=frame('cs_house_lena_darya_ext_day',['cs_darya']),post=[
 'if cs_un_sketch_time_agreed_day3:',
 '    cs_da "Тогда увидимся перед ужином. Я к Мику, а ты не забудь блокнот."',
 '    cs_narrator "Даша вышла первой. Я немного отдохнула, взяла карандаш и собралась на встречу."',
 '    $ cs_day03_darya_destination = "music_club"',
 '    $ cs_actor_exit(["cs_darya"])','    with cs_sprite_leave'])
generate(9,'144',pre=['if cs_un_sketch_completed_day3:','    return','if cs_se_sketch_spot_day3:']+
 ['    '+x for x in frame('bg ext_musclub_day')]+['else:']+['    '+x for x in frame('cs_camp_path_day')]+[
 'play music cs_day_music_home fadeout 2.0 fadein 2.0','$ renpy.music.set_volume(0.10,delay=1.0,channel="music")'],post=['label cs_check_day03_144_completed:','pass'])
generate(9,'145',pre=focus(['cs_darya']),post=['$ cs_day03_solo_sketch_done = True','label cs_check_day03_145_solo:','pass'])

defaults8=dict(cs_day03_part08_started=False,cs_day03_part08_done=False,cs_mz_friend_on_arrival_day3=None,
 cs_mz_day3_honest_book_talk=False,cs_mz_book_talk_awarded_day3=False,cs_mz_book_borrowed_day3=False,
 cs_mz_open_library_invitation_day3=False,cs_day03_novel_selected=False,cs_day03_library_legacy_bridge=False)
defaults9=dict(cs_day03_part09_done=False,cs_se_friend_before_square_day3=None,cs_se_day3_personal_talk=False,
 cs_se_day3_square_awarded=False,cs_se_sketch_spot_day3=False,cs_un_private_drawing_shown_day3=False,
 cs_un_sketch_completed_day3=False,cs_day03_solo_sketch_done=False,cs_day03_poster_stored_home=False)
for part,defaults in [(8,defaults8),(9,defaults9)]:
 (R/f'days/day03/part{part:02d}/resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+n+' = '+repr(v)+'\n' for n,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(n+'='+repr(v) for n,v in defaults.items())+')\n',encoding='utf8')

flow8='''# -*- coding: utf-8 -*-
label cs_day03_part08:
    if cs_day03_part08_done:
        jump cs_day03_part09
    hide screen cs_day03_part07_wait_screen
    $ cs_day03_part08_started = True
'''+''.join('    call cs_day03_'+k+'\n' for k in ('129','130','131','132','133','134'))+'''    call cs_day03_zhenya_novel_choice
    call cs_day03_135
    call cs_day03_136
    $ cs_day03_part08_done = True
    jump cs_day03_part09

label cs_day03_zhenya_novel_choice:
    label cs_check_day03_134_menu:
    menu:
        "Спросить Женю, что ей самой нравится в этой истории":
            if not cs_mz_book_talk_awarded_day3:
                $ cs_friend_mz += 1
                $ cs_mz_book_talk_awarded_day3 = True
            $ cs_mz_day3_honest_book_talk = True
            call cs_day03_134a
        "Поблагодарить и продолжить читать":
            call cs_day03_134b
    label cs_check_day03_134_result:
    return
'''
flow9='''# -*- coding: utf-8 -*-
label cs_day03_part09:
    if cs_day03_part09_done:
        jump cs_day03_evening_pending
'''+''.join('    call cs_day03_'+k+'\n' for k in ('137','138','139','140'))+'''    call cs_day03_semen_square_choice
    if cs_se_day3_personal_talk:
        call cs_day03_141
    call cs_day03_142
    call cs_day03_143
    if cs_un_sketch_time_agreed_day3:
        call cs_day03_144
    else:
        call cs_day03_145
    $ cs_day03_part09_done = True
    jump cs_day03_evening_pending

label cs_day03_semen_square_choice:
    if cs_se_friend_before_square_day3 is None:
        $ cs_se_friend_before_square_day3 = cs_friend_se
    label cs_check_day03_140_menu:
    menu:
        "Остаться и поговорить с Семёном по-настоящему":
            if not cs_se_day3_square_awarded:
                $ cs_friend_se += 1
                $ cs_se_day3_square_awarded = True
            $ cs_se_day3_personal_talk = True
            call cs_day03_140a
        "Не задерживать Семёна и дать ему отдохнуть":
            $ cs_se_day3_personal_talk = False
            call cs_day03_140b
    label cs_check_day03_140_result:
    return

label cs_day03_evening_pending:
    label cs_check_day03_part09_complete:
    call screen cs_day03_part09_wait_screen
    jump cs_day03_evening_pending

screen cs_day03_part09_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Продолжение вечера" size 26
            if cs_un_sketch_completed_day3:
                text "Совместное рисование завершено. Вечер ещё впереди." size 22
            else:
                text "Лена отправилась рисовать. Вечер ещё впереди." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
# Preserve explicit call anchors when regenerating these new flows.
for part,flow in [(8,flow8),(9,flow9)]:
 p=R/f'days/day03/part{part:02d}/00_flow.rpy'
 if p.exists():
    from stabilize_call_helpers import preserve_calls
    flow=preserve_calls(p.read_text(encoding='utf8'),flow)
 p.write_text(flow,encoding='utf8')
old=R/'days/day03/part07/00_flow.rpy'
t=old.read_text(encoding='utf8').split('label cs_day03_part08_pending:')[0]
t+='''label cs_day03_part08_pending:
    label cs_check_day03_part07_complete:
    hide screen cs_day03_part07_wait_screen
    jump cs_day03_part08

# A loaded save can still be waiting on the old modal screen.
screen cs_day03_part07_wait_screen():
    timer 0.1 action Jump("cs_day03_part08_pending")
'''
old.write_text(t,encoding='utf8')
(R/'days/day03/part07/128_scene.rpy').write_text('''# -*- coding: utf-8 -*-
# Preserve the old call site/return; the full path belongs to part 8.
label cs_day03_128:
    jump cs_day03_128_path
''',encoding='utf8')
(R/'source/day03_part08_09_transcript.json').write_text(json.dumps(transcript,ensure_ascii=False,indent=2),encoding='utf8')
(R/'source/day03_part08_09_editorial.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2),encoding='utf8')
print('PART08_09_GENERATED',sum(map(len,transcript.values())),'manuscript blocks;',len(transcript),'modular scenes')
if (R/'source/day03_part10.md').exists():
    import runpy
    runpy.run_path(str(R/'tools/build_day03_part10.py'),run_name='__main__')
