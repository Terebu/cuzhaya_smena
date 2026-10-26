"""Day 3: shared reading, continuing either completed drawing branch."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
P=R/'days/day03/part10';P.mkdir(exist_ok=True)
s=(R/'source/day03_part10.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена'):s.index('## Техническое задание')]
a=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)\n',s)
scenes={a[i].replace('А','a').replace('Б','b'):(a[i+1],a[i+2]) for i in range(1,len(a),3)}
def focus():return ['$ cs_frame_focus(["cs_darya"])','with cs_sprite_change']
def inward():return ['if not cs_reflective_shot:','    $ cs_pov_begin()','    with cs_sprite_leave']
def back():return ['$ cs_pov_end()','with cs_sprite_change']
def frame(bg,tags=True):return ['$ cs_director_scene("'+bg+'")','scene '+bg,'$ cs_frame_focus('+('["cs_darya"]' if tags else '[]')+')','with Dissolve(0.7)']
def pose(em):return ['if renpy.showing("cs_darya"):','    show cs_darya '+em+' pioneer normal','    $ cs_presence_stage()','    with cs_sprite_change']
narr149={'Я снова открыла роман.','Несколько минут понадобилось, чтобы вернуться к повествованию.','Сначала я перечитала предыдущий абзац.','Потом ещё один.','Наконец вспомнила, на чём остановилась.','Я перевернула страницу.','В какой-то момент поймала себя на том, что почти спорю с одним из персонажей.','Я нахмурилась.','Прочитала следующий абзац.','Я тихо выдохнула.','Со стороны окна раздалось:','Я подняла голову.','Дарья смотрела на меня с лёгким интересом.','Она улыбнулась.','Я посмотрела на книгу.','Потом на неё.','Дарья рассмеялась.','Я прищурилась.','Она совершенно невинно пожала плечами.','Я медленно кивнула.','Дарья улыбнулась.','Я немного подумала.','Потом покачала головой.','Дарья кивнула.','Я снова посмотрела на страницу.','Дарья задумалась.','Я улыбнулась.','Она рассмеялась.','Я посмотрела на повязку.','Она довольно улыбнулась.','Я покачала головой.','И снова вернулась к чтению.','Потом следующую.','Постепенно чтение снова захватило всё внимание.'}
hooks={
 '146':{'Я осторожно положила рядом ещё несколько листов.':inward(),'Я взяла роман со стола.':back()+['$ cs_day03_reading_book_location = "lena"'], 'И погрузилась в чтение.':inward()},
 '147':{'Лен.':back(),'Вот.':inward()},
 '148a':{'Я положила закладку между страницами.':back()},
 '148b':{'Я ещё несколько секунд смотрела на Дашу.':back(),'Некоторое время мы занимались своими делами.':inward(),'Через некоторое время Даша подняла голову.':back()},
 '149':{'Кто?':back(),'И снова вернулась к чтению.':inward()},
 '150':{'Дарья заметила.':back(),'Странно.':inward(),'Я посмотрела на Дарью.':back(),'Москва.':inward(),'О чём думаешь?':back(),'Вот и хорошо.':inward()},
 '151':{'Хороший вопрос.':inward(),'Да. Очень.':back()},
 '152':{'И тут за окном раздался горн.':[
    'if not cs_day03_dinner_horn_played:','    $ cs_day03_dinner_horn_played = True',
    '    label cs_check_day03_152_horn:','    play sound "sound/sfx/dinner_horn_processed.ogg"',
    '$ renpy.music.set_volume(0.04,delay=0.7,channel="music")'],
    'Дарья подняла голову.':back(),'Потом быстро поцеловала её в щёку.':['$ cs_da_cheek_kiss_day3 = True']+pose('shy_smile'),
    'Положила книгу рядом с блокнотом.':['$ cs_day03_reading_book_location = "house_table"']},
 '153':{'Мы спустились с крыльца.':frame('cs_camp_path_sunset'),
        'Странно.':inward(),'Я посмотрела на Дашу.':back(),
        'И направились к столовой.':frame('bg ext_dining_hall_near_sunset')},
}
replacements={
 'Немного. Ещё несколько дней — и придётся составлять расписание встреч.':'Немного. Пока справляюсь.',
 'И какую половицу лучше не наступать ночью.':'И на какую половицу лучше не наступать ночью.',
 'Три дня назад я даже не знала, что окажусь здесь.':'Ещё перед поездкой я даже не знала, что окажусь здесь.',
 'Моя новая возможность на несколько часов забыть о существовании лагерных проблем.':'Моя новая возможность ненадолго забыть о существовании лагерных проблем.',
 'Особенно учитывая, что мы с Тихоновой почти не отвлекались друг от друга на разговоры.':'Особенно учитывая, что мы с Тихоновой почти не отвлекались от рисунков на разговоры.',
 'Вы вроде даже не заметили, сколько времени прошло.':'И надолго увлеклись?',
 'Даже когда я полчаса молчу и читаю Гончарова?':'Даже когда я молчу и читаю Гончарова?',
 'Ты уже давно сидишь почти не двигаясь.':'Ты засиделась в неудобной позе.',
 'Сегодня Тихонова показала мне один рисунок, который раньше никому не показывала.':'Сегодня Тихонова показала мне личный рисунок. Для неё это, кажется, было непросто.',
 'Ещё утром мы обсуждали с ней то, как люди меняются под воздействием обстоятельств.':'В библиотеке мы обсуждали с ней то, как люди меняются под воздействием обстоятельств.',
}
own={
 'И с каждой страницей всё сильнее убеждалась, что Женя выбрала произведение не случайно.':('cs_mz_friend_on_arrival_day3 >= 2','И с каждой страницей всё сильнее убеждалась, что удачно взяла именно этот роман.'),
 'Ещё утром мы обсуждали с ней то, как люди меняются под воздействием обстоятельств.':('cs_mz_day3_honest_book_talk','В библиотеке я уже успела задуматься о том, как обстоятельства меняют людей.'),
 'Всё-таки Женя действительно удачно выбрала роман.':('cs_mz_friend_on_arrival_day3 >= 1','Всё-таки роман попался удачный.'),
}
count=0;transcript={}
for k,(title,body) in scenes.items():
    if k=='148':body=body.split('#### Выбор игрока')[0]
    b=[]
    if k=='146':b=frame('cs_house_lena_darya_int_day')+[
        '$ cs_day03_darya_destination = "home"','$ cs_day03_sketchbook_location = "house_table"','play ambience "sound/ambiences/int_cabin_day.ogg" fadeout 1.5 fadein 1.5',
        'play music cs_day_music_home fadeout 2.0 fadein 2.0','$ renpy.music.set_volume(0.08,delay=1.0,channel="music")']
    if k=='148':b=inward()
    if k=='149':b=inward()
    if k=='150':b=inward()+['stop music fadeout 3.0']
    if k=='151':b=frame('cs_house_lena_darya_int_sunset')+['$ sunset_time()','$ persistent.sprite_time = "sunset"',
        'play music cs_day_music_home fadein 2.0','$ renpy.music.set_volume(0.08,delay=1.0,channel="music")']
    if k=='152':b=inward()
    if k=='153':b=frame('cs_house_lena_darya_ext_sunset')+['play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5','$ cs_day03_darya_destination = "dining_hall"']
    depth=0;in_thought=False;transcript[k]=[]
    for block in re.split(r'\n\s*\n',body):
        block=block.strip()
        if not block or block.startswith('#'):continue
        if block.startswith('['):
            if block.startswith('[ЕСЛИ ') and block.endswith(':]'):
                vals=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',block)
                c=' and '.join(' '.join(v) for v in vals).replace(' == True','')
                assert c,block
                if 'cs_friend_mz' in c:c=c.replace('cs_friend_mz','cs_mz_friend_on_arrival_day3')
                if 'cs_friend_se' in c:c='cs_se_day3_personal_talk and cs_se_friend_before_square_day3 >= 1'
                nested=k=='146' and 'cs_un_private' in c
                base=1 if nested else 0
                b+=['    '*base+'if '+c+':'];depth=base+1
            elif block.startswith('[ИНАЧЕ ЕСЛИ '):
                vals=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',block)
                b+=['elif '+' and '.join(' '.join(v) for v in vals).replace(' == True','')+':'];depth=1
            elif block=='[ИНАЧЕ:]':b+=['else:'];depth=1
            elif block.startswith('[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0
            continue
        m=re.match(r'(Лена Соколова|Дарья):\\?\s*[\n ]+[—–]\s*(.*)',block,re.S)
        who=('cs_ls' if m[1]=='Лена Соколова' else 'cs_da') if m else 'cs_narrator'
        w=(m[2] if m else block).replace('\n',' ')
        if who=='cs_narrator' and (k=='148' or (k=='149' and w not in narr149) or w in ('Москва.','Квартира.','Мой компьютер.','Планшет.','Хороший вопрос.','Так.','Чёрт.','Ну вот.')):who='cs_th'
        transcript[k].append([who,w]);count+=1
        lines=hooks.get(k,{}).get(w,[])
        em={'Дарья рассмеялась.':'amused','Дарья улыбнулась.':'shy_smile','Дарья задумалась.':'thinking','Дарья пожала плечами.':'shrug','Дарья прищурилась.':'serious'}.get(w)
        if em:lines=lines+pose(em)
        b+=['    '*depth+x for x in lines]
        if w in own:
            cond,alternative=own[w]
            lines=['if '+cond+':','    '+who+' '+json.dumps(replacements.get(w,w),ensure_ascii=False),'else:','    '+who+' '+json.dumps(alternative,ensure_ascii=False)]
        else:lines=[who+' '+json.dumps(replacements.get(w,w),ensure_ascii=False)]
        b+=['    '*depth+x for x in lines]
    if k=='153':b+=['$ cs_day03_reading_book_location = "house_table"','$ cs_day03_dinner_arrived = True']
    (P/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n    return\n',encoding='utf8')
defaults=dict(cs_friend_da=0,cs_day03_part10_done=False,cs_da_day3_music_talk=False,cs_da_day3_shared_silence=False,cs_da_day3_choice_done=False,cs_da_day3_music_awarded=False,cs_da_cheek_kiss_day3=False,cs_day03_dinner_horn_played=False,cs_day03_dinner_arrived=False,cs_day03_sketchbook_location=None)
(P/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+k+' = '+repr(v)+'\n' for k,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(k+'='+repr(v) for k,v in defaults.items())+')\n',encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day03_part10:
    hide screen cs_day03_part09_wait_screen
    if cs_day03_part10_done:
        jump cs_day03_dinner_pending
'''+''.join('    call cs_day03_'+k+'\n' for k in ('146','147','148'))+'''    call cs_day03_darya_reading_choice
'''+''.join('    call cs_day03_'+k+'\n' for k in ('149','150','151','152','153'))+'''    $ cs_day03_part10_done = True
    jump cs_day03_dinner_pending

label cs_day03_darya_reading_choice:
    if cs_da_day3_choice_done:
        return
    label cs_check_day03_148_menu:
    menu:
        "Отложить книгу и расспросить Дашу о музыке":
            if not cs_da_day3_music_awarded:
                $ cs_friend_da += 1
                $ cs_da_day3_music_awarded = True
            $ cs_da_day3_music_talk = True
            $ cs_da_day3_shared_silence = False
            $ cs_da_day3_choice_done = True
            call cs_day03_148a
        "Предложить просто посидеть рядом в тишине":
            $ cs_da_day3_shared_silence = True
            $ cs_da_day3_music_talk = False
            $ cs_da_day3_choice_done = True
            call cs_day03_148b
    label cs_check_day03_148_result:
    return

label cs_day03_dinner_pending:
    label cs_check_day03_part10_complete:
    call screen cs_day03_part10_wait_screen
    jump cs_day03_dinner_pending

screen cs_day03_part10_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Вечер: ужин" size 26
            text "Книга осталась дома. Девушки пришли к столовой." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
from stabilize_call_helpers import preserve_calls
p=P/'00_flow.rpy'
if p.exists():flow=preserve_calls(p.read_text(encoding='utf8'),flow)
p.write_text(flow,encoding='utf8')
old=R/'days/day03/part09/00_flow.rpy';t=old.read_text(encoding='utf8')
t=t.split('label cs_day03_evening_pending:')[0]+'''label cs_day03_evening_pending:
    label cs_check_day03_part09_complete:
    hide screen cs_day03_part09_wait_screen
    jump cs_day03_part10

screen cs_day03_part09_wait_screen():
    timer 0.1 action Jump("cs_day03_evening_pending")
'''
old.write_text(t,encoding='utf8')
(R/'source/day03_part10_transcript.json').write_text(json.dumps(dict(source_blocks=count,scenes=transcript),ensure_ascii=False,indent=2),encoding='utf8')
print('PART10_GENERATED',count,'blocks;',len(scenes),'scene files')
if (R/'source/day03_part11.md').exists():
    import runpy
    runpy.run_path(str(R/'tools/build_day03_part11.py'),run_name='__main__')
