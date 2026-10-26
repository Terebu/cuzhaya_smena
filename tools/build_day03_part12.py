"""Replace the old post-dinner tail with book retrieval and evening reading."""
from pathlib import Path
import re,json
from stabilize_call_helpers import preserve_calls
R=Path(__file__).resolve().parent.parent;P=R/'days/day03/part12';P.mkdir(exist_ok=True)
s=(R/'source/day03_part12.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена 163.'):s.index('## Техническое задание для Codex')]
a=re.split(r'#{3,4} Сцена (\d+[АБ]?)\. ([^\n]+)\n',s)
scenes={a[i].replace('А','a').replace('Б','b'):(a[i+1],a[i+2]) for i in range(1,len(a),3)}
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
def inward():return ['if not cs_reflective_shot:','    $ cs_pov_begin()','    with cs_sprite_leave']
def back():return ['$ cs_pov_end()','with cs_sprite_change']
def frame(bg,tags):return ['$ cs_director_scene("'+bg+'")','scene '+bg,'$ cs_frame_focus('+json.dumps(tags)+')','with Dissolve(0.7)']
def pose(tag,emotion):
 attrs=' pioneer normal' if tag.startswith('cs_') else ' pioneer'
 return ['if renpy.showing("'+tag+'"):', '    show '+tag+' '+emotion+attrs,'    $ cs_presence_stage()','    with cs_sprite_change']
def library_cast():return ['if cs_mz_evening_help_day3:']+['    '+x for x in focus(['cs_zhenya','cs_darya'])]+['else:']+['    '+x for x in focus(['cs_zhenya'])]
se='cs_friend_se >= 2 and cs_se_day3_personal_talk'
edits={
 'На безопасной полке лежала папка с концертным плакатом.':'На столе лежала папка с концертным плакатом, которую мы оставили здесь раньше.',
 'Я подошла к кровати.':'Я подошла к столу.',
 'Не потому, что я получила новую книгу.':'Не потому, что я снова добралась до книги.',
 'После сегодняшнего количества страниц, наверное, уже нет.':'Нет. До конца ещё далеко, а читать наспех не хочется.',
 'А Семён, между прочим, уже сам научился поддерживать представление.':'А Семён, между прочим, умеет ответить так, что продолжать представление уже незачем.',
 'Так что, возможно, мой педагогический эксперимент оказался успешным.':'Хорошо, что я вовремя остановилась и дала ему сказать своё.',
}
variants={
 'Можешь занимать свой стол, когда придёшь.':('cs_mz_quiet_reading_place_day3','Можешь занимать свободный стол, когда придёшь.'),
 'Славя, я думала, мы подруги.':('cs_friend_sl >= 1','Славя, я ведь пришла с миром.'),
 'Семён, сегодня мы с тобой уже вполне нормально разговаривали.':('cs_se_day3_personal_talk','Семён, иногда мы с тобой вполне нормально разговариваем.'),
 'Видишь, а ты хотел меня прогнать. Потерял бы ценного консультанта.':('not ('+se+')','Вот видишь. У расследования обнаружилась практическая польза.'),
 'Давай, Соколова. А то Женя начнёт думать, что тебя похитили.':('cs_sl_evening_destination_told_day3','Давай, Соколова. У тебя ведь ещё дела.'),
 'Учитывая твои сегодняшние разговоры, это несложно.':('cs_mz_dinner_friend_on_arrival >= 1','После твоего объяснения догадаться несложно.'),
 'Всё-таки она действительно правильно выбрала произведение.':('cs_mz_friend_on_arrival_day3 >= 1','Всё-таки я удачно выбрала произведение.'),
 'Возможно, она уже тогда понимала, что я начну смотреть на эту историю немного иначе.':('cs_mz_friend_on_arrival_day3 >= 1','После того разговора я сама стала смотреть на эту историю немного иначе.'),
}
def cond(block):
 vals=re.findall(r'(cs_\w+)`?\s*(>=|==)\s*(True|False|\d+)',block.replace('`',''))
 assert vals,block
 c=' and '.join(' '.join(v) for v in vals).replace(' == True','').replace(' == False',' == False')
 if 'ДО ЭТОГО ВЫБОРА' in block:c=c.replace('cs_friend_sl','cs_sl_friend_before_evening_choice')
 if 'ДО ВЕЧЕРНЕГО ВЫБОРА' in block:c=c.replace('cs_friend_mz','cs_mz_dinner_friend_on_arrival')
 return c
def blocks(body):
 for raw in re.split(r'\n\s*\n',body):
  t=raw.strip().replace('**','')
  if not t or t=='---' or t.startswith(('#','- ')):continue
  yield t
def tokens(body):
 out=[]
 for t in blocks(body):
  if t.startswith('['):out.append(('cue',t));continue
  italic=t.startswith('*') and t.endswith('*');t=t.strip('*')
  m=re.match(r'(Лена Соколова(?: \([^)]*\))?|Дарья|Женя|Семён|Славя):\\?\s*[\n ]+[—–]\s*(.*)',t,re.S)
  who={'Дарья':'cs_da','Женя':'cs_mz','Семён':'cs_sy','Славя':'cs_sl'}.get(m[1],'cs_ls') if m else ('cs_th' if italic else 'cs_narrator')
  out.append((who,(m[2] if m else t).replace('\n',' ')))
 return out
pre={
 '163':['$ sunset_time()','$ persistent.sprite_time = "sunset"']+frame('bg int_dining_hall_sunset',['cs_zhenya','cs_darya'])+['play music cs_day_music_home fadeout 2.0 fadein 2.0','$ renpy.music.set_volume(0.08,channel="music")'],
 '164':frame('bg ext_square_sunset',[]),
 '165':['if cs_sl_friend_before_evening_choice is None:','    $ cs_sl_friend_before_evening_choice = cs_friend_sl'],
 '165a':back()+focus(['cs_semen','sl']), '165b':back()+focus(['cs_semen','sl']),
 '166':frame('cs_house_lena_darya_ext_sunset',[]),
 '167':frame('bg ext_square_sunset',['cs_semen','sl']),
 '168':frame('cs_library_exterior_sunset',[]),
 '169a':['if cs_mz_evening_help_completed_day3:','    return']+back()+library_cast(),
 '169b':back()+focus(['cs_zhenya']),
 '170':back()+library_cast(),
}
hooks={
 '163':{'Я попрощалась с ними.':['if cs_mz_evening_help_day3:','    $ cs_day03_darya_destination = "library"','else:','    $ cs_day03_darya_destination = "music_club"'],
        'И вышла на улицу.':frame('bg ext_dining_hall_near_sunset',[])},
 '164':{'Я направилась к ним.':focus(['cs_semen','sl'])},
 '165a':{'Тогда я спрошу тебя завтра, если будет время.':['$ cs_sl_day4_notice_offer = True'],
         'Ладно, товарищи. Мне всё-таки пора.':['cs_ls "Зайду в домик за книгой и вернусь в библиотеку."','$ cs_sl_evening_destination_told_day3 = True'],
         'И направилась к домику.':frame('cs_camp_path_sunset',[])},
 '165b':{'Ладно, не буду мешать. Вам ещё нужно разобраться с бумагами.':['cs_ls "Я как раз за книгой, а потом в библиотеку."','$ cs_sl_evening_destination_told_day3 = True'],
         'И направилась к домику.':frame('cs_camp_path_sunset',[])},
 '166':{'Внутри было тихо.':frame('cs_house_lena_darya_int_sunset',[]),
         'Взяла её здоровой рукой.':['label cs_check_day03_166_book_taken:','$ cs_day03_reading_book_location = "with_lena"'],
         'И вышла.':frame('cs_camp_path_sunset',[])},
 '167':{'И продолжила путь.':frame('cs_camp_path_sunset',[])},
 '168':{'Внутри было тихо.':frame('cs_library_interior_evening',[])+library_cast(),
        'Если не хочешь, можешь сразу приступить к работе.':[],
        'Вот и хорошо.':inward()},
 '169a':{'Вполне нормальная работа.':inward(),'Слушай, здесь, кажется, цифры перепутаны.':back()+library_cast(),
         'Я вернулась к столу.':['$ cs_mz_evening_help_completed_day3 = True','label cs_check_day03_169_help_completed:'],
         'Идеально.':inward()},
 '169b':{'Ну вот.':inward(),'Всё тот же роман?':back()+focus(['cs_zhenya']),'Я вернулась к книге.':inward()},
 '170':{'Интересно.':inward(),'Слушай.':back()+library_cast(),
        'И через некоторое время поймала себя на странной мысли.':inward(),
        'Женя закрыла журнал.':back()+library_cast(),
        'Я снова посмотрела на страницу.':inward()},
}
transcript={}
for k,(title,body) in scenes.items():
 if k=='165':body='' # The authored choice is handled once by the flow.
 if k=='169':continue # Container heading; its two sub-scenes are executable.
 if k=='168':
  # The final COMMON closes BOTH the nested invitation and the help branch.
  body=body.replace('[ЕСЛИ `cs_mz_open_library_invitation_day3 == True`:]','[NESTED cs_mz_open_library_invitation_day3:]')
  body=body.replace('[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]','[CLOSE_ALL]')
 ts=tokens(body);transcript[k]=[(w,t) for w,t in ts if w!='cue']
 b=list(pre.get(k,[]));depth=0;nested=False
 for who,w in ts:
  if who=='cue':
   if w.startswith('[NESTED '):b+=['    '*depth+'if cs_mz_open_library_invitation_day3:'];depth+=1;nested=True
   elif w=='[CLOSE_ALL]':depth=0;nested=False
   elif w.startswith('[ЕСЛИ '):b+=['if '+cond(w)+':'];depth=1
   elif w.startswith('[ИНАЧЕ ЕСЛИ '):b+=['elif '+cond(w)+':'];depth=1
   elif w.startswith('[ИНАЧЕ:]'):
    if nested:b+=['    '+'else:'];depth=2
    else:b+=['else:'];depth=1
   elif w.startswith('[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0
   continue
  lines=hooks.get(k,{}).get(w,[])
  emotional={'Дарья рассмеялась.':('cs_darya','amused'),'Дарья улыбнулась.':('cs_darya','shy_smile'),
   'Семён рассмеялся.':('cs_semen','smile'),'Он усмехнулся.':('cs_semen','smile'),
   'Славя улыбнулась.':('sl','smile'),'Славя рассмеялась.':('sl','laugh'),
   'Женя усмехнулась.':('cs_zhenya','normal'),'Женя посмотрела на меня поверх очков.':('cs_zhenya','glasses_touch'),
   'Она посмотрела на меня внимательнее.':('cs_zhenya','thoughtful')}
  if w in emotional:lines=lines+pose(*emotional[w])
  if k=='164' and w=='Я трагически вздохнула.':b+=['if '+se+':'];depth=1
  b+=['    '*depth+x for x in lines]
  if k=='164' and w=='Семён покачал головой.':
   b+=['    '*depth+who+' '+json.dumps(w,ensure_ascii=False),'else:',
      '    cs_ls "Ладно, без представления. Не буду мешать вашему совещанию."',
      '    cs_narrator "Славя показала листок, а Семён кивнул. Я не стала продолжать шутку."'];depth=0;continue
  if k=='168' and w=='Если не хочешь, можешь сразу приступить к работе.':
   b+=['    '*depth+'if cs_mz_evening_help_completed_day3:',
       '    '*(depth+1)+'cs_mz "Работу мы уже закончили. Если хочешь, можешь спокойно почитать."',
       '    '*depth+'else:','    '*(depth+1)+'cs_mz '+json.dumps(w,ensure_ascii=False)];continue
  if k=='163' and w=='Можешь. Только начнём, когда Лена вернётся. Она же тоже собиралась помогать.':
   b+=['    '*depth+'if cs_mz_evening_help_completed_day3:', '    '*(depth+1)+'cs_mz "Можешь. Мы уже всё сверили, теперь я только закончу записи."',
       '    '*depth+'else:','    '*(depth+1)+who+' '+json.dumps(w,ensure_ascii=False)];continue
  if w in variants:
   c,alt=variants[w];b+=['    '*depth+'if '+c+':','    '*(depth+1)+who+' '+json.dumps(w,ensure_ascii=False),'    '*depth+'else:','    '*(depth+1)+who+' '+json.dumps(alt,ensure_ascii=False)]
  else:b+=['    '*depth+who+' '+json.dumps(edits.get(w,w),ensure_ascii=False)]
 if k=='164':b+=inward()
 if k in ('165a','165b'):b+=['$ cs_sl_evening_scene_done_day3 = True']
 if k=='163':b+=['$ cs_day03_dinner_finished = True']
 if k=='166':b+=['$ cs_day03_evening_book_retrieved = True']
 p=P/(k+'_scene.rpy');out='# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n    return\n'
 if p.exists():out=preserve_calls(p.read_text(encoding='utf8'),out)
 p.write_text(out,encoding='utf8')
defaults=dict(cs_day03_part12_started=False,cs_day03_part12_done=False,cs_sl_friend_before_evening_choice=None,
 cs_sl_evening_schedule_help_day3=False,cs_sl_day4_notice_offer=False,cs_sl_evening_choice_done=False,
 cs_sl_evening_help_awarded=False,cs_sl_evening_scene_done_day3=False,cs_sl_evening_destination_told_day3=False,
 cs_day03_evening_book_retrieved=False,cs_day03_part12_legacy_entry=False)
(P/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+k+' = '+repr(v)+'\n' for k,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(k+'='+repr(v) for k,v in defaults.items())+')\n',encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day03_part12:
    hide screen cs_day03_part11_wait_screen
    if cs_day03_part12_done:
        jump cs_day03_library_closing_pending
    if not cs_day03_part12_started:
        $ cs_day03_part12_started = True
        call cs_day03_163
    call cs_day03_164
    call cs_day03_165
    call cs_day03_slavya_evening_choice
    call cs_day03_166
    call cs_day03_167
    call cs_day03_168
    if cs_mz_evening_help_day3:
        if not cs_mz_evening_help_completed_day3:
            call cs_day03_169a
        else:
            $ cs_frame_focus(["cs_zhenya", "cs_darya"])
            with cs_sprite_change
            cs_narrator "С карточками мы уже разобрались раньше. Я открыла книгу, а Даша устроилась рядом; Женя закончила оставшиеся записи."
    else:
        call cs_day03_169b
    call cs_day03_170
    $ cs_day03_part12_done = True
    jump cs_day03_library_closing_pending

label cs_day03_slavya_evening_choice:
    if cs_sl_evening_choice_done:
        return
    if cs_sl_friend_before_evening_choice is None:
        $ cs_sl_friend_before_evening_choice = cs_friend_sl
    $ cs_pov_end()
    $ cs_frame_focus(["cs_semen", "sl"])
    with cs_sprite_change
    label cs_check_day03_165_menu:
    menu:
        "Предложить помочь сверить завтрашние поручения":
            if not cs_sl_evening_help_awarded:
                $ cs_friend_sl += 1
                $ cs_sl_evening_help_awarded = True
            $ cs_sl_evening_schedule_help_day3 = True
            $ cs_sl_evening_choice_done = True
            call cs_day03_165a
        "Не отвлекать их и отправиться за книгой":
            $ cs_sl_evening_choice_done = True
            call cs_day03_165b
    label cs_check_day03_165_result:
    return

label cs_day03_part12_from_legacy:
    hide screen cs_day03_part11_wait_screen
    $ cs_day03_part11_done = True
    if cs_day03_part12_done or cs_day03_part12_started:
        jump cs_day03_part12
    $ cs_day03_part12_started = True
    $ cs_day03_part12_legacy_entry = True
    $ cs_day03_started = True
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("cs_house_lena_darya_ext_sunset")
    scene cs_house_lena_darya_ext_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "После ужина мы уже успели дойти до домика. Я решила захватить оставленный на столе роман и ещё немного почитать в библиотеке."
    if cs_mz_evening_help_day3:
        $ cs_day03_darya_destination = "library"
        if cs_mz_evening_help_completed_day3:
            cs_da "Я пока вернусь к Жене. С карточками мы уже закончили, можно просто спокойно посидеть."
        else:
            cs_da "Я зайду к Жене первой. Заодно посмотрю, что подготовить к нашей помощи."
    else:
        $ cs_day03_darya_destination = "music_club"
        cs_da "А я загляну к Мику уточнить планы на завтра. Потом встретимся у домика."
    cs_ls "Хорошо. Я зайду за книгой и скоро вернусь."
    jump cs_day03_part12

label cs_day03_library_closing_pending:
    label cs_check_day03_part12_complete:
    call screen cs_day03_part12_wait_screen
    jump cs_day03_library_closing_pending

screen cs_day03_part12_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Вечер в библиотеке" size 26
            text "Женя скоро закроет библиотеку. Продолжение следует." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
p=P/'00_flow.rpy'
if p.exists():flow=preserve_calls(p.read_text(encoding='utf8'),flow)
p.write_text(flow,encoding='utf8')
# Retain former call return addresses for saves inside the retired tail.
p=R/'days/day03/part11/00_flow.rpy';t=p.read_text(encoding='utf8')
if 'label cs_day03_part11_legacy_tail:' not in t:
 i=t.index('    if cs_mz_evening_help_day3:');end=t.index('\nlabel cs_day03_evening_library_choice:')
 tail=t[i:end]
 tail=tail.replace('    call cs_day03_162','    jump cs_day03_part12_from_legacy\n    call cs_day03_162')
 tail=tail.replace('    jump cs_day03_after_dinner_pending','    jump cs_day03_part12_from_legacy')
 # Both branch return sites flow into the bridge, bypassing the old scene 162.
 t=t[:i]+'    $ cs_day03_part11_done = True\n    jump cs_day03_part12\n\nlabel cs_day03_part11_legacy_tail:\n'+tail+t[end:]
 t=t.replace('    call screen cs_day03_part11_wait_screen\n    jump cs_day03_after_dinner_pending','    jump cs_day03_part12_from_legacy')
 start=t.index('screen cs_day03_part11_wait_screen():')
 t=t[:start]+'''screen cs_day03_part11_wait_screen():
    timer 0.1 action Jump("cs_day03_part12_from_legacy")
'''
 p.write_text(t,encoding='utf8')
(R/'source/day03_part12_transcript.json').write_text(json.dumps(dict(source_blocks=sum(map(len,transcript.values())),scenes=transcript),ensure_ascii=False,indent=2),encoding='utf8')
print('PART12_GENERATED',sum(map(len,transcript.values())),'blocks;',len(transcript),'scene files')

if (R/'source/day03_part13.md').exists():
    import runpy
    runpy.run_path(str(R/'tools/build_day03_part13.py'))
