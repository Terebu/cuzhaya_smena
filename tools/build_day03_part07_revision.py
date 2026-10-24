"""Replace lunch, preserving public labels and the shared authored camera."""
from pathlib import Path
import json, re

R = Path(__file__).resolve().parent.parent
D = R / 'days/day03/part07'
s = (R/'source/day03_part07_revision.md').read_text(encoding='utf-8-sig')
s = s[s.index('### Сцена 121.'):s.index('## Задание для Codex')]
parts = re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)\n', s)
parts = {parts[i].replace('А','a').replace('Б','b'): (parts[i+1],parts[i+2]) for i in range(1,len(parts),3)}
transcript = {}

def focus(tags):
    return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']

def pose(tag, emotion):
    suffix = ' pioneer normal' if tag in ('cs_darya','cs_zhenya') else ' pioneer'
    return ['if renpy.showing("'+tag+'"):', '    show '+tag+' '+emotion+suffix,
            '    $ cs_presence_stage()', '    with cs_sprite_change']

def leave(tag):
    return ['$ cs_actor_exit(["'+tag+'"])','with cs_sprite_leave']

def pov(): return ['$ cs_pov_begin()','with cs_sprite_leave']
def back(): return ['$ cs_pov_end()','with cs_sprite_change']

hooks = {
 '124': {'Можно к вам?': focus(['cs_zhenya','cs_darya'])+pose('cs_darya','shy_smile'),
         'Папку с вчерашним плакатом она положила на свободный край стула, подальше от еды.': ['$ cs_day03_poster_location = "dining_chair"']},
 '125a': {'Тихонова повернулась.': focus(['cs_zhenya','cs_darya','un'])+pose('un','shy'),
          'И направилась к выходу.': leave('un')},
 '126': {'Женя направилась к выходу.': leave('cs_zhenya')+['label cs_check_day03_126_zhenya_left:'],
         'Да.': [],
         'Где-то там кипит обычная лагерная жизнь.': pov(),
         'Женя допила чай.': back(), 'Женя закончила чай.': back()},
 '127': {'И вышли на улицу.': [
       'if cs_day03_poster_location == "dining_chair":',
       '    cs_narrator "Дарья забрала папку с плакатом со стула и прижала к боку."',
       '    $ cs_day03_poster_location = "darya_folder"',
       '$ cs_director_scene("bg ext_dining_hall_near_day")','scene bg ext_dining_hall_near_day',
       'play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.5 fadein 1.5']+focus(['cs_darya'])+['with Dissolve(0.8)'],
       'Третий день.': pov(), 'Ты сейчас в библиотеку?': back(),
       'Она направилась к музыкальному клубу.': ['$ cs_day03_darya_destination = "music_club"']+leave('cs_darya')+['label cs_check_day03_127_darya_left:']},
 '123': {'Надо же.': pov(), 'Я вернулась к обеду.': back(), 'Вот и всё.': pov()},
 '124_entry': back(),
}
common = {}
for w, emotion in [('Женя поправила очки.','glasses_touch'),('Она поправила очки.','glasses_touch'),
                   ('Женя усмехнулась.','shrug'),('Женя приподняла бровь.','thinking'),
                   ('Женя слегка улыбнулась.','normal'),('Женя немного помолчала.','thoughtful'),
                   ('Она посмотрела на меня поверх очков.','arms_crossed')]:
    common[w]=pose('cs_zhenya',emotion)
for w, emotion in [('Дарья улыбнулась.','shy_smile'),('Дарья рассмеялась.','amused'),
                   ('Дарья покачала головой.','shrug'),('Дарья закрыла глаза.','arms_crossed')]:
    common[w]=pose('cs_darya',emotion)
for w, emotion in [('Тихонова чуть улыбнулась.','smile'),('Тихонова тихо улыбнулась.','smile'),
                   ('Она осторожно подошла.','shy'),('Тихонова немного задумалась.','normal')]:
    common[w]=pose('un',emotion)

speakers={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz','Лена Тихонова':'cs_un'}
def line(t):
    m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
    if m:
        name,w=m.groups();name=re.sub(r'\s*\(.*\)$','',name)
        return speakers[name],w.replace('\n',' ')
    if t.startswith('*') and t.endswith('*'): return 'cs_th',t[1:-1].replace('\n',' ')
    return 'cs_narrator',t.replace('\n',' ')

def edited(w):
    if w=='Женя рассмеялась уже открыто.':
        return ['if cs_friend_mz >= 1:', '    cs_narrator "Женя негромко рассмеялась."',
                'else:', '    cs_narrator "Женя фыркнула и спрятала улыбку за чашкой."']
    if w=='Ты не мешаешь, когда просто сидишь рядом.':
        return ['if cs_friend_mz >= 1:', '    cs_mz '+json.dumps(w,ensure_ascii=False),
                'else:', '    cs_mz "Если ты спокойно читаешь, мне это не мешает. Правда."']
    # Preferences were discussed this morning, and only on the book-choice path.
    if w=='Я уже отложила пару книг. Ты вчера говорила, что тебе интереснее истории про людей, чем просто приключения.':
        return ['if cs_mz_day3_book_awarded:',
                '    cs_mz "Я уже отложила пару книг. Утром мы говорили об историях, где важнее люди и их решения. Помнишь?"',
                'else:', '    cs_mz "Я уже отложила пару книг. Подумала, тебе могут подойти истории про людей и их решения."',
                '$ cs_mz_book_prepared_day3 = True']
    if w=='Ты ведь вчера быстро закончила книгу.':
        return ['if cs_lena_book_returned:', '    cs_mz "Вчерашнюю книгу ты уже вернула. Хочешь ещё что-нибудь?"',
                'else:', '    cs_mz "Хочешь ещё что-нибудь посмотреть?"']
    if w=='Да. Хотела попробовать что-нибудь ещё.':
        return ['cs_ls "Да. Хотела попробовать что-нибудь ещё."']
    if w=='После утреннего разговора о рисовании мне хочется пообщаться ещё.':
        return ['if cs_un_day3_art_talk:', '    cs_th '+json.dumps(w,ensure_ascii=False),
                'else:', '    cs_th "Утром мы не стали надолго её отвлекать. Может, теперь удастся поговорить?"']
    if w=='Пора узнать, какую книгу мне приготовила Женя.':
        return ['if cs_mz_book_prepared_day3:', '    cs_th '+json.dumps(w,ensure_ascii=False),
                'else:', '    cs_th "Пора выбрать что-нибудь почитать."']
    if w=='Немного прогуляюсь и зайду к Жене. Она обещала подобрать книгу.':
        return ['if cs_mz_book_prepared_day3:', '    cs_ls '+json.dumps(w,ensure_ascii=False),
                'else:', '    cs_ls "Немного прогуляюсь и зайду к Жене. Посмотрю, что есть почитать."']
    # Do not assert an art consultation happened on a declined morning branch.
    replacements={
      'Получилось изменить передний план?':('cs_un_day3_art_talk','Получилось изменить передний план?','Удалось продолжить?'),
      'Да. Как ты советовала.':('cs_un_day3_art_talk','Да. Как ты советовала.','Да. Я немного переделала рисунок.'),
      'И ты, конечно, уже успела дать художественную консультацию.':('cs_un_day3_art_talk','И ты, конечно, уже успела дать художественную консультацию.','Вы уже успели обсудить рисунок?'),
      'Между прочим, исключительно по запросу.':('cs_un_day3_art_talk','Между прочим, исключительно по запросу.','Утром только посмотрели. Не стали отвлекать.'),
      'Правда. Я сама попросила.':('cs_un_day3_art_talk','Правда. Я сама попросила.','Я тогда ещё не закончила. Сейчас уже можно показать.'),
    }
    if w in replacements:
        c,a,b=replacements[w];who='cs_un' if w in ('Да. Как ты советовала.','Правда. Я сама попросила.') else ('cs_mz' if w.startswith('И ты,') else 'cs_ls')
        return ['if '+c+':','    '+who+' '+json.dumps(a,ensure_ascii=False),'else:','    '+who+' '+json.dumps(b,ensure_ascii=False)]

flag_actions={
 'cs_mz_quiet_reading_place_day3': ['$ cs_mz_quiet_reading_place_day3 = True'],
 'cs_un_sketch_time_agreed_day3': ['$ cs_un_sketch_time_agreed_day3 = True','$ cs_un_sketch_plan_discussed_day3 = True'],
 'cs_un_sketch_invite_day3': ['$ cs_un_sketch_invite_day3 = True'],
 'cs_mi_followup_invitation_day3': ['$ cs_mi_followup_invitation_day3 = True'],
 'cs_dv_followup_invitation_day3': ['$ cs_dv_followup_invitation_day3 = True'],
}
def generate(k,pre=(),post=()):
    title,t=parts[k];b=list(pre);depth=0;transcript[k]=[]
    if k=='125':t=t.split('#### Выбор игрока')[0]
    for block in re.split(r'\n\s*\n',t):
        block=block.strip()
        if not block or block=='---':continue
        if block.startswith('**['):
            if block.startswith('**[ЕСЛИ ') and block.endswith(':]**'):
                cond=' and '.join(re.findall(r'`([^`]+)`',block)).replace(' == True','')
                if k=='124':cond+=' and cs_day03_poster_location in ("darya_folder", "dining_chair")'
                b+=['if '+cond+':'];depth=1
            elif block.startswith('**[ИНАЧЕ ЕСЛИ '):
                vals=re.findall(r'`([^`]+)`',block);cond=' and '.join(vals).replace(' == True','')
                # Technical note explicitly overrides the manuscript's elif.
                b+=[('if ' if k=='127' else 'elif ')+cond+':'];depth=1
            elif block.startswith('**[ИНАЧЕ:]'): b+=['else:'];depth=1
            elif block.startswith('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0
            elif block.startswith('**[ФЛАГ:'):
                name=re.search(r'`(cs_\w+)',block).group(1)
                b+=['    '*depth+x for x in flag_actions[name]]
            continue
        if block.startswith(('#','- ')):continue
        who,w=line(block);transcript[k].append((who,w))
        h=hooks.get(k,{}).get(w,common.get(w,[]))
        b+=['    '*depth+x for x in h]
        custom=edited(w)
        b+=['    '*depth+x for x in (custom if custom is not None else [who+' '+json.dumps(w,ensure_ascii=False)])]
    b+=list(post)+['return']
    (D/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n',encoding='utf8')

generate('121',pre=focus(['cs_zhenya'])+['$ cs_day03_part07_book_promised_before = cs_mz_book_requested_day3',
    'cs_narrator "У входа Ольга Дмитриевна на минуту остановила Дашу. Та махнула нам: идите, догоню."',
    'play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0',
    '$ renpy.music.set_volume(0.12,delay=1.0,channel="music")','label cs_check_day03_121_queue:'],
    post=['$ cs_mz_book_requested_day3 = True','$ cs_day03_library_visit_time = "after_lunch"'])
generate('122',pre=['stop music fadeout 3.0'])
generate('123')
generate('124',pre=back())
generate('125')
generate('125a')
generate('125b')
generate('126',pre=focus(['cs_zhenya','cs_darya']))
generate('127',pre=focus(['cs_darya'])+['play music "sound/music/my_daily_life.ogg" fadein 2.0','$ renpy.music.set_volume(0.12,delay=1.0,channel="music")'])

# Keep the old public arrival label, with a short playable fulfilment of lunch's
# promise. The full reading scene is deliberately left for the next part.
(D/'128_scene.rpy').write_text('''# -*- coding: utf-8 -*-
label cs_day03_128:
    $ save_name = "Чужая смена — День 3: После обеда"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    with Dissolve(0.8)
    cs_narrator "Я пошла к библиотеке не торопясь. Торопиться после обеда вообще казалось дурной привычкой."
    cs_th "Ни новых экспедиций, ни обязательного поиска ответов. Просто книга."
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    with dissolve
    cs_narrator "Дверь библиотеки была открыта. Я поднялась на крыльцо."
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    stop ambience fadeout 1.5
    stop music fadeout 2.0
    $ cs_frame_focus(["cs_zhenya"])
    with Dissolve(0.8)
    label cs_check_day03_128_library:
    cs_narrator "Женя уже сидела за своим столом. Здесь было тихо даже после столовой."
    # Also covers an old save made after the former version of the lunch.
    if cs_friend_mz >= 2:
        $ cs_mz_book_prepared_day3 = True
    if cs_day03_reading_book_selected:
        cs_mz "Твоя книга на столе. Я её никуда не убирала."
    else:
        if cs_mz_book_prepared_day3:
            cs_narrator "Она подвинула ко мне два небольших томика."
            cs_mz "Вот, посмотри. Я бы начала с Паустовского. Здесь есть «Тёплый хлеб»."
            cs_ls "Почему именно с него?"
            show cs_zhenya thoughtful pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
            cs_mz "Он короткий. Но дело не в этом. Там человек сначала делает гадость, а потом приходится что-то исправлять. Не словами."
            cs_ls "То есть лёгкого чтения после обеда не обещаешь?"
            cs_mz "Читать легко. А дальше сама решишь."
            cs_narrator "Я взяла предложенный сборник и посмотрела оглавление."
        else:
            cs_ls "Я всё-таки дошла. Можно посмотреть рассказы?"
            cs_mz "Вон тот стеллаж, средняя полка. Только не перемешивай."
            cs_narrator "Я нашла сборник Паустовского и раскрыла на оглавлении. Среди названий попалось знакомое: «Тёплый хлеб»."
            cs_ls "Начну с этого. Здесь посижу, выносить не буду."
            cs_mz "Хорошо."
        $ cs_day03_reading_book_selected = True
        $ cs_day03_reading_book_id = "paustovsky_warm_bread"
        $ cs_day03_reading_book_location = "library_reading_table"
    if cs_mz_quiet_reading_place_day3:
        cs_narrator "Я устроилась за дальним столом у окна, который Женя предложила за обедом. Заново спрашивать разрешения не понадобилось."
        cs_mz "Если свет будет мешать, штору можно поправить. Только не дёргай."
        cs_ls "Разберусь. Спасибо."
    else:
        cs_ls "За свободным столом можно?"
        cs_mz "Да. Садись."
        cs_narrator "Я выбрала свободное место и осторожно положила локоть рядом с книгой."
    if cs_mz_map_lead and cs_mz_catalog_checked_day3:
        cs_th "Каталоги мы уже проверили утром. Сейчас можно оставить их в покое."
    $ cs_reflective_focus()
    with cs_sprite_leave
    cs_narrator "Я раскрыла сборник на первой странице рассказа. Из окна тянуло тёплым воздухом."
    cs_th "Пожалуй, начну."
    return
''',encoding='utf8')

flags=['cs_day03_part07_done','cs_un_day3_lunch_together','cs_un_sketch_plan_discussed_day3',
 'cs_un_day3_lunch_awarded','cs_day03_part07_book_promised_before','cs_mz_book_prepared_day3',
 'cs_mz_quiet_reading_place_day3','cs_un_sketch_time_agreed_day3','cs_mi_followup_invitation_day3',
 'cs_dv_followup_invitation_day3','cs_day03_reading_book_selected']
defaults={n:False for n in flags}
defaults.update(cs_day03_darya_destination=None,cs_day03_reading_book_id=None,cs_day03_reading_book_location='library_shelf')
(D/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+n+' = '+repr(v)+'\n' for n,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(n+'='+repr(v) for n,v in defaults.items())+')\n',encoding='utf8')
flow=(D/'00_flow.rpy').read_text(encoding='utf-8-sig')
if 'call cs_day03_125\n' not in flow and not re.search(r'call cs_day03_125 from ',flow):
    flow=re.sub(r'(    call cs_day03_124[^\n]*\n)',r'\1    call cs_day03_125\n',flow)
flow=flow.replace('Не отвлекать Лену от выбора места','Поздороваться и дать Лене самой выбрать место').replace('День 3. Общество тихих людей','День 3. Тишина тоже сближает').replace('Продолжение — послеобеденное чтение с Женей.','Лена выбрала книгу. Продолжение — послеобеденное чтение.')
(D/'00_flow.rpy').write_text(flow,encoding='utf8')
(R/'source/day03_part07_revision_transcript.json').write_text(json.dumps(transcript,ensure_ascii=False,indent=2),encoding='utf8')
print('Revised lunch:',sum(map(len,transcript.values())),'manuscript blocks; 9 manuscript scenes + library bridge.')
