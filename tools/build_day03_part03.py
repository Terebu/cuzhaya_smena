"""Day 3 part 3: manuscript scenes with explicit staging and guarded choices."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent;D=R/'days/day03/part03';D.mkdir(parents=True,exist_ok=True)
s=(R/'source/day03_part03.md').read_text(encoding='utf8');s=s[s.index('### Сцена 89.'):s.index('## Техническое задание')]
p=re.split(r'### Сцена (\d+[А-Я]?)\. ([^\n]+)\n',s);sections={p[i]:(p[i+1],p[i+2]) for i in range(1,len(p),3)}
expected={}
def parse(t):
 out=[]
 for raw in re.split(r'\n\s*\n',t):
  t=raw.strip()
  if not t or t=='---' or t.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
  if m:
   name,w=m.groups();who={'Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz','Семён':'cs_sy'}[name]
  elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
  else:who,w='cs_narrator',t
  out.append((who,w.replace('\n',' ')))
 return out

def focus(expr):return ['$ cs_frame_focus('+expr+')','with cs_sprite_change']
def emotion(tag,pose):return ['if renpy.showing("'+tag+'"):', '    show '+tag+' '+pose+' pioneer normal','    $ cs_presence_stage()','    with cs_sprite_change']
def enter(tag,pose):return ['with None','show '+tag+' '+pose+' pioneer normal at cs_day03_p3_actor_enter(0.25)','$ renpy.pause(0.30, hard=True)','show '+tag+' '+pose+' pioneer normal at Transform(xpos=0.25, xanchor=0.5, ypos=1.60, yanchor=1.0, zoom=1.0, alpha=1.0)','$ cs_presence_stage()','with None']
def frame(image,with_mz=False):
 a=['$ cs_director_scene('+json.dumps(image)+')','scene '+image,'show cs_darya shy_smile pioneer normal at Transform(xpos=0.75, xanchor=0.5, ypos=1.60, yanchor=1.0)']
 if with_mz:a+=['show cs_zhenya normal pioneer normal at Transform(xpos=0.25, xanchor=0.5, ypos=1.60, yanchor=1.0)']
 return a+['$ cs_presence_stage()','with Dissolve(0.8)']
reflect=['$ cs_reflective_focus()','with cs_sprite_leave']
hooks={
 '89':{'Дарья приподняла бровь.':emotion('cs_darya','thinking'),'Потом медленно улыбнулась.':emotion('cs_darya','shy_smile'),'Она рассмеялась.':emotion('cs_darya','amused'),'Если серьёзно, дело было вовсе не в каком-то особенном режиме.':reflect+['label cs_check_day03_89_reflection:'],'Я посмотрела на Дарью.':focus('["cs_darya"]')+emotion('cs_darya','shy_smile')+['label cs_check_day03_89_dialogue:'],'Дарья рассмеялась.':emotion('cs_darya','amused')},
 '90':{'Доброе утро, Женя.':enter('cs_zhenya','normal')+['label cs_check_day03_90_zhenya:'],'Женя на секунду удивилась.':emotion('cs_zhenya','glasses_touch'),'Женя нахмурилась.':emotion('cs_zhenya','arms_crossed'),'Дарья улыбнулась.':emotion('cs_darya','shy_smile'),'Женя приподняла бровь.':emotion('cs_zhenya','thinking'),'Потом едва заметно улыбнулась.':emotion('cs_zhenya','normal'),'Женя улыбнулась.':emotion('cs_zhenya','shy')},
 '91':{'Женя посмотрела на повязку.':emotion('cs_zhenya','thoughtful'),'Дарья усмехнулась.':emotion('cs_darya','amused'),'Женя слегка улыбнулась.':emotion('cs_zhenya','normal'),'Дарья тихо рассмеялась.':emotion('cs_darya','amused')},
 '92':{'Женя приподняла бровь.':emotion('cs_zhenya','thinking'),'Женя отложила книгу.':emotion('cs_zhenya','glasses_touch'),'Мы с Дарьей устроились за соседним столом.':focus('["cs_darya"]')+['label cs_check_day03_92_separate:']},
 '93':{'Время от времени смотрела в окно.':reflect+['label cs_check_day03_93_reflection:'],'Лен.':focus('cs_day03_p3_breakfast_cast()')+['label cs_check_day03_93_dialogue:'],'Дарья рассмеялась.':emotion('cs_darya','amused'),'Дарья улыбнулась.':emotion('cs_darya','shy_smile'),'Женя отложила ложку.':emotion('cs_zhenya','thoughtful'),'Она слегка улыбнулась.':emotion('cs_zhenya','normal'),'Вы здесь.':focus('["cs_darya"]')+enter('cs_semen','neutral')+['label cs_check_day03_93_semen:'],'Он усмехнулся.':emotion('cs_semen','smile'),'Семён улыбнулся.':emotion('cs_semen','smile'),'Он направился к своему столу.':focus('cs_day03_p3_breakfast_cast()')+['label cs_check_day03_93_separate_semen:']},
 '94':{'Женя тоже закончила завтрак.':['if not cs_day03_mz_breakfast_together:', '    cs_narrator "Закончив есть, Женя прошла мимо нашего стола с книгой в руках."','    cs_narrator "Я обернулась к ней, не вставая."']+focus('["cs_zhenya", "cs_darya"]')+emotion('cs_zhenya','normal')+['label cs_check_day03_94_contact:'],'Поправила очки.':emotion('cs_zhenya','glasses_touch')},
 '94a':{'Женя ненадолго задумалась.':emotion('cs_zhenya','thinking'),'Она посмотрела на меня внимательнее.':emotion('cs_zhenya','thoughtful'),'Она слегка улыбнулась.':emotion('cs_zhenya','shy'),'Женя посмотрела на повязку.':emotion('cs_zhenya','normal'),'И никаких самовольных исследований шкафов.':emotion('cs_zhenya','arms_crossed'),'Она покачала головой.':emotion('cs_zhenya','normal')},
 '94b':{'Женя слегка улыбнулась.':emotion('cs_zhenya','normal')},
 '95':{'Мы вышли из столовой.':frame('bg ext_dining_hall_away_day',True),'Потом возле развилки Женя остановилась.':frame('cs_camp_path_day',True),'Она направилась к библиотеке.':['$ cs_actor_exit(["cs_zhenya"])','with cs_sprite_leave','label cs_check_day03_95_zhenya_left:'],'Вот и всё.':reflect,'Дарья остановилась возле меня.':focus('["cs_darya"]')+emotion('cs_darya','thinking'),'Она улыбнулась.':emotion('cs_darya','shy_smile'),'Дарья рассмеялась.':emotion('cs_darya','amused'),'Дарья засмеялась.':emotion('cs_darya','amused'),'Он заметил нас.':enter('cs_semen','smile')+['label cs_check_day03_95_semen_return:'],'Он усмехнулся.':emotion('cs_semen','smile'),'Он насторожился.':emotion('cs_semen','thinking'),'Он приподнял бровь.':emotion('cs_semen','awkward'),'Он направился к площади.':['$ cs_actor_exit(["cs_semen"])','with cs_sprite_leave','label cs_check_day03_95_semen_left:'],'Мы направились по дорожке.':['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0'],'Да.':[], 'Кажется, третий день действительно начался неплохо.':reflect+['label cs_check_day03_95_reflection:']}
}
def write(key,segments,pre=(),post=()):
 expected[key]=[];body=list(pre)
 for segment in segments:
  if isinstance(segment,list):body+=segment;continue
  text,depth=segment;indent='    '*depth
  for who,w in parse(text):
   expected[key].append((who,w))
   body += [indent+x for x in hooks.get(key,{}).get(w,[])]
   # Local edits preserve continuity with earlier choices/saves.
   if key=='89' and w=='Наш разговор о книге.':
    body+=['if cs_lena_book_returned:','    cs_narrator '+json.dumps(w,ensure_ascii=False),'else:','    cs_narrator "Наши вчерашние спокойные разговоры."'];continue
   if key=='89' and w.startswith('До столовой оставалось каких-то тридцать метров'):
    body+=['if cs_day03_at_dining_door:', '    cs_narrator "У самого входа в столовую мне в голову пришла совершенно замечательная мысль."','else:', '    '+who+' '+json.dumps(w,ensure_ascii=False)];continue
   if key=='94' and w=='Вчера она сама предложила мне ещё что-нибудь почитать.':
    body+=['if cs_lena_book_returned and cs_friend_mz >= 1:','    cs_th '+json.dumps(w,ensure_ascii=False),'else:','    cs_th "После нашего вчерашнего разговора мне стало любопытно, какие книги она любит."'];continue
   if key=='94a' and w.startswith('Да. Вчерашняя мне понравилась.'):
    body+=[indent+'if cs_lena_book_returned:',indent+'    '+who+' '+json.dumps(w,ensure_ascii=False),indent+'else:',indent+'    cs_ls "Да. Хочу попробовать что-нибудь из того, что ты считаешь хорошим."'];continue
   if key=='94b' and w=='Женя просто кивнула и направилась к выходу.':w='Женя просто кивнула и посмотрела в сторону выхода.'
   if key=='95' and w=='В этот момент из столовой вышел Семён.':w='В этот момент по дорожке от столовой к нам подошёл Семён.'
   if key=='95' and w=='И даже получилось договориться о следующей встрече.':
    body+=['if cs_day03_library_visit_time is not None:','    cs_th '+json.dumps(w,ensure_ascii=False),'else:','    cs_th "Можно просто встретиться ещё раз, когда появится повод."'];continue
   body.append(indent+who+' '+json.dumps(w,ensure_ascii=False))
 body+=list(post)+['return']
 (D/(key+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+key+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+sections.get(key,('Разговор о книгах',))[0],ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in body)+'\n',encoding='utf8')
def one(k,pre=(),post=()):write(k,[(sections[k][1],0)],pre,post)
one('89',pre=['label cs_check_day03_89:','$ cs_frame_focus(["cs_darya"])','if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":','    play music "sound/music/my_daily_life.ogg" fadein 2.0','play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0','$ renpy.music.set_volume(0.17, channel="ambience")'])
t=sections['90'][1];base,t=t.split('**[ЕСЛИ `cs_friend_mz >= 2`:]**');hi,t=t.split('**[ИНАЧЕ ЕСЛИ `cs_friend_mz == 1`:]**');mid,t=t.split('**[ИНАЧЕ:]**');low,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('90',[(base,0),['if cs_friend_mz >= 2:'],(hi,1),['elif cs_friend_mz == 1 and cs_lena_book_returned:'],(mid,1),['else:'],(low,1),(tail,0)],frame('bg ext_dining_hall_away_day'))
one('91',pre=frame('bg int_dining_hall_people_day',True)+['play ambience "sound/ambiences/dining_hall_full.ogg" fadein 1.5','$ renpy.music.set_volume(0.20, channel="ambience")','$ renpy.music.set_volume(0.13, delay=1.5, channel="music")','label cs_check_day03_91:'])
t=sections['92'][1];t=t.split('#### Если `cs_friend_mz >= 2`')[1];hi,t=t.split('#### Если `cs_friend_mz == 1`');mid,low=t.split('#### Если `cs_friend_mz == 0`')
write('92',[['$ cs_day03_mz_breakfast_together = cs_friend_mz >= 1','if cs_day03_mz_breakfast_together:'],['    label cs_check_day03_92_together:'],['    pass'],['if cs_friend_mz >= 2:'],(hi,1),['elif cs_friend_mz == 1:'],(mid,1),['else:'],(low,1)],post=['label cs_check_day03_92_result:'])
t=sections['93'][1];base,t=t.split('**[ЕСЛИ `cs_friend_mz >= 1`:]**');mz,t=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**',1);common,t=t.split('**[ЕСЛИ `cs_friend_se >= 3`:]**');hi,t=t.split('**[ИНАЧЕ:]**');low,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('93',[(base,0),['if cs_day03_mz_breakfast_together:'],(mz,1),(common,0),['$ cs_day03_semen_breakfast_joined = cs_friend_se >= 3','if cs_day03_semen_breakfast_joined:'],['    label cs_check_day03_93_joined:'],(hi,1),['else:'],(low,1),(tail,0)],post=['if cs_day03_semen_breakfast_joined:', '    cs_narrator "Семён первым отложил ложку и поднялся."','    cs_sy "Я пока отнесу поднос."','    cs_narrator "Он забрал посуду и отошёл к стойке у выхода."','    $ cs_frame_focus(cs_day03_p3_breakfast_cast())','    with cs_sprite_leave','label cs_check_day03_93_semen_offscreen:'])
write('94',[(sections['94'][1].split('**[MENU')[0],0)],post=['call cs_day03_zhenya_book_choice'])
t=sections['94А'][1];base,t=t.split('**[ЕСЛИ `cs_mz_map_lead == True`:]**');lead,t=t.split('**[ИНАЧЕ:]**');plain,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ ВЕТВИ.]**')
write('94a',[(base,0),['if cs_mz_map_lead:'],(lead,1),['else:'],(plain,1),(tail,0)],pre=['label cs_check_day03_94a:'])
t=sections['94Б'][1];base,t=t.split('**[ЕСЛИ `cs_mz_map_lead == True`:]**');lead,t=t.split('**[ИНАЧЕ ЕСЛИ `cs_friend_mz >= 1`:]**');invite,t=t.split('**[ИНАЧЕ:]**');none,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ ВЕТВИ.]**')
write('94b',[(base,0),['if cs_mz_map_lead:'],(lead,1),['elif cs_friend_mz >= 1:'],(invite,1),['else:'],(none,1),(tail,0)],pre=['label cs_check_day03_94b:'])
hooks['95']['Потом возле развилки Женя остановилась.']=[]
write('95',[(sections['95'][1].split('Я проводила её взглядом.')[0],0)])
(D/'00_flow.rpy').write_text('''# -*- coding: utf-8 -*-
label cs_day03_part03:
    hide screen cs_day03_part02_wait_screen
    $ cs_day03_part02_done = True
    $ cs_day03_at_dining_door = bool(renpy.showing("bg ext_dining_hall_away_day"))
    $ cs_day03_library_visit_time = "late_morning" if cs_mz_map_lead else None
    window show dissolve
    call cs_day03_89
    call cs_day03_90
    call cs_day03_91
    call cs_day03_92
    call cs_day03_93
    call cs_day03_94
    call cs_day03_95
    $ cs_day03_part03_done = True
    jump cs_day03_part04

label cs_day03_zhenya_book_choice:
    label cs_check_day03_94_menu:
    menu:
        "Спросить Женю, какую книгу она посоветовала бы прочитать":
            if not cs_mz_day3_book_awarded:
                $ cs_friend_mz += 1
                $ cs_mz_day3_book_awarded = True
            $ cs_mz_book_requested_day3 = True
            $ cs_day03_library_visit_time = "late_morning" if cs_mz_map_lead else "after_lunch"
            call cs_day03_94a
        "Не задерживать Женю перед её делами":
            call cs_day03_94b
    label cs_check_day03_94_result:
    return

label cs_day03_part04_pending:
    label cs_check_day03_part03_complete:
    jump cs_day03_part04_legacy

screen cs_day03_part03_wait_screen():
    modal True
    frame:
        align (0.03, 0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Серьёзная советская женщина" size 26
            text "Дальше — проверка локтя у Виолы." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
''',encoding='utf8')
(D/'resources.rpy').write_text('''# -*- coding: utf-8 -*-
default cs_day03_part03_done = False
default cs_mz_book_requested_day3 = False
default cs_mz_day3_book_awarded = False
default cs_day03_library_visit_time = None
default cs_day03_mz_breakfast_together = False
default cs_day03_semen_breakfast_joined = False
default cs_day03_at_dining_door = False
init -9 python:
    cs_state_defaults.update(cs_day03_part03_done=False, cs_mz_book_requested_day3=False,
        cs_mz_day3_book_awarded=False, cs_day03_library_visit_time=None,
        cs_day03_mz_breakfast_together=False, cs_day03_semen_breakfast_joined=False,
        cs_day03_at_dining_door=False)
    def cs_day03_p3_breakfast_cast():
        return ["cs_zhenya", "cs_darya"] if cs_day03_mz_breakfast_together else ["cs_darya"]

transform cs_day03_p3_actor_enter(x=0.25):
    xpos x
    xanchor 0.5
    ypos 1.60
    yanchor 1.0
    zoom 1.0
    alpha 0.0
    linear 0.28 alpha 1.0
''',encoding='utf8')
(R/'source/day03_part03_transcript.json').write_text(json.dumps(expected,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 3 manuscript blocks:',sum(map(len,expected.values())),'scene files:',len(expected))
