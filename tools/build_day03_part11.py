"""Dinner and voluntary library help, preserving friendship earned beforehand."""
from pathlib import Path
import re,json
from stabilize_call_helpers import preserve_calls
R=Path(__file__).resolve().parent.parent;P=R/'days/day03/part11';P.mkdir(exist_ok=True)
s=(R/'source/day03_part11.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена'):s.index('## Задание для Codex')]
a=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)\n',s)
scenes={a[i].replace('А','a').replace('Б','b'):(a[i+1],a[i+2]) for i in range(1,len(a),3)}
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
def inward():return ['if not cs_reflective_shot:','    $ cs_pov_begin()','    with cs_sprite_leave']
def back():return ['$ cs_pov_end()','with cs_sprite_change']
def frame(bg,tags):return ['$ cs_director_scene("'+bg+'")','scene '+bg,'$ cs_frame_focus('+json.dumps(tags)+')','with Dissolve(0.7)']
def leave(tags):return ['$ cs_actor_exit('+json.dumps(tags)+')','with cs_sprite_leave']
def pose(tag,em):
    attrs=' pioneer normal' if tag in ('cs_zhenya','cs_darya','cs_semen') else ' pioneer'
    return ['if renpy.showing("'+tag+'"):', '    show '+tag+' '+em+attrs,'    $ cs_presence_stage()','    with cs_sprite_change']
def codecond(block):
    vals=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',block)
    assert vals,block
    return ' and '.join(' '.join(v) for v in vals).replace(' == True','').replace('cs_friend_mz','cs_mz_dinner_friend_on_arrival')
edits={
 'Она ведь не Семён, которого можно поймать за плечо и объявить любимым супругом при половине лагеря.':'Личные границы важнее любого моего внезапного порыва. И с Семёном это правило тоже стоило помнить.',
 'Нет. Где-то чуть дальше середины.':'Нет. Прочитала ещё несколько глав, но до конца пока далеко.',
 'Женя, ты уже четвёртый человек за сегодня, который напоминает мне об этом.':'Женя, мне уже не первый раз за сегодня об этом напоминают.',
 'Ты сегодня уже третий раз оказываешься рядом с Женей.':'Ты сегодня уже не первый раз оказываешься рядом с Женей.',
 'Ещё пару дней назад я бы обязательно попыталась расшевелить Женю.':'При первом знакомстве я бы обязательно попыталась расшевелить Женю.',
 'Просто за эти два дня я уже успела понять, что не обязательно проверять терпение человека до самого предела.':'Просто за эти дни я уже успела понять, что не обязательно проверять терпение человека до самого предела.',
}
variants={
 'Уже начинаю подозревать, что ты специально выбрала произведение, чтобы проверить мою способность спокойно воспринимать чужие ошибки.':('cs_mz_friend_on_arrival_day3 >= 1','Начинаю подозревать, что эта книга проверяет мою способность спокойно воспринимать чужие ошибки.'),
 'Я вообще хотела сказать, что ты сегодня получила приглашение уже несколько раз.':('cs_mz_dinner_friend_on_arrival >= 2','Я вообще хотела сказать, что вы уже нашли общую тему.'),
 'Но сегодня мы нормально поговорили. И договорились, что некоторые темы больше не трогаем.':('cs_se_day3_personal_talk','Но если вижу, что ему неприятно, останавливаюсь. Некоторые темы мы больше не трогаем.'),
 'Сегодня мне довелось поработать в медпункте, помочь с лагерными делами и теперь ещё попробовать себя в библиотечном хозяйстве.':('cs_helped_viola_day3 and cs_helped_sl_day3','Сегодня лагерных дел и без того хватило. А теперь ещё попробую себя в библиотечном хозяйстве.'),
 'И если завтра снова придёшь почитать, можешь не ждать, пока я освобожусь. Просто занимай своё место.':('cs_mz_quiet_reading_place_day3','Если завтра придёшь читать, выбирай свободный стол. Пока я занята журналом, можешь спокойно начинать.'),
}
hooks={
 '154':{'Он увидел меня.':focus(['cs_semen','cs_darya']), 'А потом я увидела знакомые очки.':leave(['cs_semen']),
        'Вообще-то за сегодняшний день я действительно стала спокойнее.':inward()},
 '155':{'Я сразу отпустила.':['label cs_check_day03_155_hug:','$ cs_mz_hug_allowed_day3 = True'],
        'Спасибо тебе, Даша.':inward(),'Пока этого вполне достаточно.':[],
        'Женя посмотрела на меня.':back()},
 '157':{'Хорошо.':[], 'Поразительно хорошо.':inward(),'Через некоторое время Дарья подняла голову.':back()},
 '159':{'Понятно.':inward()},
 '159a':{'Я посмотрела на Женю.':back()},'159b':{'Я посмотрела на книгу Жени.':back()},
 '160':{'Надо же.':inward(),'Ты чего задумалась?':back(),
        'Тебе бы сначала собственные вещи научиться не терять.':['cs_narrator "Пока я доедала, Даша успела рассказать Жене, как я искала карандаш. Конца истории я не слышала."'],
        'Неподалёку появилась Мику.':focus(['cs_zhenya','cs_darya','mi']),
        'Алиса, проходившая неподалёку, усмехнулась.':leave(['cs_zhenya'])+focus(['cs_darya','mi','dv']),
        'Мику обрадовалась.':[],
        'Алиса посмотрела на меня.':leave(['mi','cs_zhenya'])+focus(['cs_darya','dv']),
        'Женя направилась к выходу.':leave(['cs_zhenya'])},
 '161a':{'Женя открыла дверь.':back(), 'Пропустила нас внутрь.':frame('cs_library_interior_evening',['cs_zhenya','cs_darya'])+['stop ambience fadeout 1.5'],
         'Наконец-то задача, в которой всё зависит от того, насколько хорошо умеешь читать цифры.':inward(),
         'Всё сходится?':back(),
         'Мы с Дарьей вышли наружу.':['$ cs_mz_evening_help_completed_day3 = True','label cs_check_day03_161_help_completed:']+frame('cs_camp_path_sunset',['cs_darya'])+['play ambience "sound/ambiences/camp_center_evening.ogg" fadein 1.5']},
 '161b':{'Ну что ж.':inward(),'Дарья посмотрела на меня.':back(),'Мы направились к площади.':frame('cs_camp_path_sunset',['cs_darya'])},
 '162':{'Наверное, она права.':inward(),'Я слегка улыбнулась.':back(),
        'Мне действительно нравится этот лагерь.':inward(),'Я посмотрела на неё.':back(),
        'И мы направились к нашему домику.':frame('cs_house_lena_darya_ext_sunset',['cs_darya'])},
}
pre={
 '154':['if cs_mz_dinner_friend_on_arrival is None:','    $ cs_mz_dinner_friend_on_arrival = cs_friend_mz',
        '$ sunset_time()','$ persistent.sprite_time = "sunset"','$ cs_day03_darya_destination = "dining_hall"']+frame('bg ext_dining_hall_near_sunset',['cs_darya'])+[
        'play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5',
        'play music cs_day_music_home fadeout 2.0 fadein 2.0','$ renpy.music.set_volume(0.08,delay=1.0,channel="music")'],
 '155':['if cs_day03_dinner_greeting_done:','    return']+back()+focus(['cs_zhenya','cs_darya']),
 '156':frame('bg int_dining_hall_sunset',['cs_zhenya','cs_darya'])+['play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.5 fadein 1.5'],
 '159a':back(),'159b':back(),
 '160':back()+focus(['cs_zhenya','cs_darya']),
 '161a':['if cs_mz_evening_help_completed_day3:','    return','$ cs_day03_darya_destination = "library"']+frame('cs_library_exterior_sunset',['cs_zhenya','cs_darya'])+['play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5'],
 '161b':frame('bg ext_dining_hall_near_sunset',['cs_darya'])+['play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5'],
 '162':['$ cs_day03_darya_destination = "home"']+frame('cs_camp_path_sunset',['cs_darya'])
}
post={'155':['$ cs_day03_dinner_greeting_done = True'],'160':['$ cs_day03_dinner_finished = True']}
speakers={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz','Семён':'cs_sy','Мику':'cs_mi','Алиса':'cs_dv'}
transcript={};count=0
for k,(title,body) in scenes.items():
    if k=='159':body=body.split('#### Выбор игрока')[0]
    if k=='157':
        body=body.replace('Через некоторое время Дарья подняла голову.','[ЕСЛИ cs_friend_mz >= 1:]\n\nЧерез некоторое время Дарья подняла голову.')+'\n\n[ИНАЧЕ:]\n\nДарья кивнула мне и вернулась к ужину.\n\n[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]\n'
        hooks[k]['Дарья кивнула мне и вернулась к ужину.']=back()
    b=list(pre.get(k,[]));depth=0;transcript[k]=[]
    for raw in re.split(r'\n\s*\n',body):
        block=raw.strip().replace('**','');block=block.strip()
        if not block or block=='---':continue
        if block.startswith('['):
            if block.startswith('[ЕСЛИ '):b+=['if '+codecond(block)+':'];depth=1
            elif block.startswith('[ИНАЧЕ ЕСЛИ '):b+=['elif '+codecond(block)+':'];depth=1
            elif block=='[ИНАЧЕ:]':b+=['else:'];depth=1
            elif block.startswith('[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0
            elif k=='160' and block.startswith('[ПОСЛЕДСТВИЕ:'):
                field='cs_dv_followup_target_day' if 'Алисы' in block else 'cs_mi_followup_target_day'
                b+=['    '*depth+'$ '+field+' = 4']
            continue
        italic=block.startswith('*') and block.endswith('*');block=block.strip('*')
        m=re.match(r'(Лена Соколова|Дарья|Женя|Семён|Мику|Алиса):\\?\s*[\n ]+[—–]\s*(.*)',block,re.S)
        who=speakers[m[1]] if m else ('cs_th' if italic else 'cs_narrator')
        w=(m[2] if m else block).replace('\n',' ');transcript[k].append([who,w]);count+=1
        lines=hooks.get(k,{}).get(w,[])
        poses={'Женя усмехнулась.':('cs_zhenya','shrug'),'Женя поправила очки.':('cs_zhenya','glasses_touch'),
               'Женя немного задумалась.':('cs_zhenya','thinking'),'Женя улыбнулась.':('cs_zhenya','normal'),
               'Дарья рассмеялась.':('cs_darya','amused'),'Дарья улыбнулась.':('cs_darya','shy_smile'),
               'Семён рассмеялся.':('cs_semen','smile'),'Мику рассмеялась.':('mi','laugh'),'Алиса усмехнулась.':('dv','grin')}
        if w in poses:lines=lines+pose(*poses[w])
        if k=='160' and w=='Женя посмотрела на нас.':lines=leave(['mi','dv'])+focus(['cs_zhenya','cs_darya'])
        b+=['    '*depth+x for x in lines]
        if w in variants:
            cond,alt=variants[w];lines=['if '+cond+':','    '+who+' '+json.dumps(w,ensure_ascii=False),'else:','    '+who+' '+json.dumps(alt,ensure_ascii=False)]
        else:lines=[who+' '+json.dumps(edits.get(w,w),ensure_ascii=False)]
        b+=['    '*depth+x for x in lines]
    b+=post.get(k,[])
    # At zero previous friendship the dinner stays polite; no sudden disclosure.
    if k=='158':b=['if cs_mz_dinner_friend_on_arrival >= 1:']+['    '+x for x in b]+[
        'else:','    cs_narrator "Мы спокойно ужинали. Женя иногда отвечала на короткие вопросы, затем снова возвращалась к тарелке."',
        '    cs_th "Не обязательно превращать каждую встречу в откровенный разговор. Пока достаточно того, что она не против нашей компании."']
    label='cs_day03_'+k
    (P/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel '+label+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n    return\n',encoding='utf8')
defaults=dict(cs_day03_part11_done=False,cs_mz_dinner_friend_on_arrival=None,cs_mz_hug_allowed_day3=False,
 cs_day03_dinner_greeting_done=False,cs_mz_evening_help_day3=False,cs_mz_evening_help_completed_day3=False,
 cs_mz_evening_choice_done=False,cs_mz_evening_help_awarded=False,cs_day03_dinner_finished=False,
 cs_mi_followup_target_day=None,cs_dv_followup_target_day=None)
(P/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+k+' = '+repr(v)+'\n' for k,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(k+'='+repr(v) for k,v in defaults.items())+')\n\nimage cs_library_interior_evening = LiveComposite((1920,1080), (0,0), "bg int_library_day", (0,0), Solid("#17213d40"))\n',encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day03_part11:
    hide screen cs_day03_part10_wait_screen
    if cs_day03_part11_done:
        jump cs_day03_after_dinner_pending
'''+''.join('    call cs_day03_'+k+'\n' for k in ('154','155','156','157','158','159'))+'''    call cs_day03_evening_library_choice
    call cs_day03_160
    if cs_mz_evening_help_day3:
        call cs_day03_161a
    else:
        call cs_day03_161b
    call cs_day03_162
    $ cs_day03_part11_done = True
    jump cs_day03_after_dinner_pending

label cs_day03_evening_library_choice:
    if cs_mz_evening_choice_done:
        return
    label cs_check_day03_159_menu:
    menu:
        "Предложить Жене помощь с возвращёнными книгами":
            if not cs_mz_evening_help_awarded:
                $ cs_friend_mz += 1
                $ cs_mz_evening_help_awarded = True
            $ cs_mz_evening_help_day3 = True
            $ cs_mz_evening_choice_done = True
            call cs_day03_159a
        "Не вмешиваться в работу Жени и пожелать ей хорошего вечера":
            $ cs_mz_evening_help_day3 = False
            $ cs_mz_evening_choice_done = True
            call cs_day03_159b
    label cs_check_day03_159_result:
    return

label cs_day03_after_dinner_pending:
    label cs_check_day03_part11_complete:
    call screen cs_day03_part11_wait_screen
    jump cs_day03_after_dinner_pending

screen cs_day03_part11_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. После ужина" size 26
            text "Девушки вернулись к домику. Спокойный вечер продолжается." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
p=P/'00_flow.rpy'
if p.exists():flow=preserve_calls(p.read_text(encoding='utf8'),flow)
p.write_text(flow,encoding='utf8')
p=R/'days/day03/part10/00_flow.rpy';t=p.read_text(encoding='utf8').split('label cs_day03_dinner_pending:')[0]
t+='''label cs_day03_dinner_pending:
    label cs_check_day03_part10_complete:
    hide screen cs_day03_part10_wait_screen
    jump cs_day03_part11

screen cs_day03_part10_wait_screen():
    timer 0.1 action Jump("cs_day03_dinner_pending")
''';p.write_text(t,encoding='utf8')
(R/'source/day03_part11_transcript.json').write_text(json.dumps(dict(source_blocks=count,scenes=transcript),ensure_ascii=False,indent=2),encoding='utf8')
print('PART11_GENERATED',count,'blocks;',len(scenes),'scene files')

if (R/'source/day03_part12.md').exists():
    import runpy
    runpy.run_path(str(R/'tools/build_day03_part12.py'))
