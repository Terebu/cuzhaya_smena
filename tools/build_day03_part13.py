"""Authored closing library sequence; retain previous continuation/save labels."""
from pathlib import Path
import re,json
from stabilize_call_helpers import preserve_calls
R=Path(__file__).resolve().parent.parent;P=R/'days/day03/part13';P.mkdir(exist_ok=True)
s=(R/'source/day03_part13.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена 171.'):s.index('## Техническое задание для Codex')]
a=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)\n',s)
scenes={a[i].replace('А','a').replace('Б','b'):(a[i+1],a[i+2]) for i in range(1,len(a),3)}
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
def inward():return ['if not cs_reflective_shot:','    $ cs_pov_begin()','    with cs_sprite_leave']
def back():return ['if cs_reflective_shot:','    $ cs_pov_end()','    with cs_sprite_change']
def frame(bg,tags):return ['$ cs_director_scene("'+bg+'")','scene '+bg,'$ cs_frame_focus('+json.dumps(tags)+')','with Dissolve(0.7)']
def libcast():return ['if cs_mz_evening_help_completed_day3 and not cs_da_waiting_outside_library_day3:']+['    '+x for x in focus(['cs_zhenya','cs_darya'])]+['else:']+['    '+x for x in focus(['cs_zhenya'])]
def tokens(body):
 for raw in re.split(r'\n\s*\n',body):
  t=raw.strip().replace('**','')
  if not t or t=='---' or t.startswith(('#','- ','Выбор игрока:','1. «','2. «')):continue
  if t.startswith('['):yield ('cue',t);continue
  italic=t.startswith('*') and t.endswith('*');t=t.strip('*')
  m=re.match(r'(Лена Соколова(?: \([^)]*\))?|Дарья|Женя):\\?\s*[\n ]+[—–]\s*(.*)',t,re.S)
  who={'Дарья':'cs_da','Женя':'cs_mz'}.get(m[1],'cs_ls') if m else ('cs_th' if italic else 'cs_narrator')
  yield who,(m[2] if m else t).replace('\n',' ')
def cond(t):
 vals=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',t.replace('`',''))
 assert vals,t
 return ' and '.join(' '.join(v) for v in vals).replace(' == True','').replace(' == False',' == False')
edits={
 'А ведь собиралась только немного почитать.':'За чтением прошло больше времени, чем я собиралась здесь провести.',
 'До конца оставалось совсем немного.':'Незаметно я добралась до последних страниц.',
 'А дядя наконец понял, что не всё в жизни измеряется карьерой и деньгами.':'А дядя хотя бы заметил, что из-за дел почти перестал видеть собственную жену.',
 'Жаль, что для этого понадобилось столько времени.':'Жаль, что так поздно. И всё-таки в самом конце он снова радуется чужому богатству — будто ещё не решил, что для него важнее.',
 'Ты сегодня после библиотеки даже не начала сразу шутить.':'Ты пошутила про писателей, а теперь снова задумалась.',
 'Нет. Нормально.':'Нет, всего несколько минут. Не успела замёрзнуть.',
 'На улице окончательно стемнело.':'Пока я читала, на улице окончательно стемнело.',
 'Пара страниц, одна глава, и домой.':'Пара страниц, одна глава — а потом ещё одна.',
 'Окна были тёмными.':'Ветки отбрасывали на стену подвижные тени.',
 'Потом открыла дверь.':'Потом придержала дверь, пропуская меня.',
}
variants={
 'Поэтому я и дала тебе эту книгу.':('cs_mz_friend_on_arrival_day3 >= 1','Значит, ты сама нашла подходящую книгу.'),
 'Ты говорила, что любишь истории, где решения имеют последствия.':('cs_mz_friend_on_arrival_day3 >= 1','Ты хорошо объяснила, почему тебе интересна эта история.'),
 'Она действительно всё запомнила.':('cs_mz_friend_on_arrival_day3 >= 1','Она действительно слушала, что я говорю.'),
 'Специально?':('cs_mz_friend_on_arrival_day3 >= 1','Значит, не зря сняла её с полки?'),
 'Значит, я не ошиблась с выбором.':('cs_mz_friend_on_arrival_day3 >= 1','Значит, ты не ошиблась с выбором.'),
 'Я даже успела обзавестись постоянным местом в библиотеке. Скоро начну требовать служебное удостоверение.':('cs_mz_quiet_reading_place_day3','Я даже успела найти любимый уголок в библиотеке. Скоро начну требовать читательский стаж.'),
 'Более того, кажется, завтра меня там снова будут рады видеть.':('cs_friend_mz >= 2','Завтра сюда опять можно будет прийти за книгой.'),
 'Сегодня она снова играла на пианино.':('cs_da_day3_music_talk or cs_mz_evening_help_completed_day3 == False','Сегодня она снова нашла время для музыки.'),
 'Я рисовала.':('cs_un_sketch_completed_day3','Я успела выбрать место для рисунков.'),
}
pre={
 '171':frame('cs_library_interior_night',[])+['$ night_time()','$ persistent.sprite_time = "night"','stop music fadeout 3.0'],
 '172':inward(),
 '173':back()+focus(['cs_zhenya']),
 '174':back()+focus(['cs_zhenya']),
 '175':back()+focus(['cs_zhenya']),
 '176':[],
 '177':frame('cs_camp_path_night',['cs_darya'])+['play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0','$ renpy.music.set_volume(0.08,channel="music",delay=1.0)'],
 '178':[], '178a':back(), '178b':[],
 '179':frame('cs_house_lena_darya_ext_night',['cs_darya']),
}
hooks={
 '171':{'Женя закрыла журнал.':libcast(),
  'Дарья улыбнулась нам обеим и вышла.':['$ cs_actor_exit(["cs_darya"])','with cs_sprite_leave','$ cs_da_waiting_outside_library_day3 = True','$ cs_day03_darya_destination = "library_entrance"'],
  'Последние страницы.':inward()},
 '172':{'И остановилась.':['$ cs_mz_book_finished_day3 = True','label cs_check_day03_172_book_finished:'],
  'Женя подняла голову.':back()+focus(['cs_zhenya'])},
 '173':{'Странно.':inward()},
 '174':{'Сделала пометку о возврате.':['$ cs_mz_book_borrowed_day3 = False','$ cs_day03_reading_book_location = "library"','label cs_check_day03_174_book_returned:'],
  'Странно.':inward(),'Всё-таки здесь красиво.':inward(),'Не хочется нарушать эту тишину.':inward()},
 '175':{'И осторожно закрыла её за собой.':frame('cs_library_exterior_night',[])+['play sound "sound/sfx/close_door_1.ogg"'],
  'Ну вот.':inward(),'И сама отпустила.':['$ cs_mz_hug_allowed_day3 = True','label cs_check_day03_175_first_hug:']},
 '176':{'И услышала знакомый голос.':focus(['cs_darya']),
  'Она поднялась, когда я посмотрела в её сторону.':['$ cs_da_waiting_outside_library_day3 = True','$ cs_day03_darya_destination = "with_lena"'],
  'И мы направились по дорожке.':['$ cs_da_waiting_outside_library_day3 = False']},
 '177':{'Красиво.':inward(),'Вот.':inward()},
 '178':{'Мы обе оказались здесь.':inward()},
 '178b':{'Нет.':inward(),'Надо же.':inward()},
 '179':{'Вот и пришли.':inward(),'Весьма насыщенный день.':inward(),
  'Ночной лагерь оставался позади.':inward(),
  'Я посмотрела на Дашу, которая ждала меня у двери.':back(),
  'И вошла в домик.':frame('cs_house_lena_darya_int_night',['cs_darya'])+['play sound "sound/sfx/close_door_1.ogg"','stop music fadeout 3.0','$ cs_day03_darya_destination = "house"']},
}
transcript={}
for k,(title,body) in scenes.items():
 # The document has two IFs for mutually exclusive farewell alternatives.
 if k=='175':body=body.replace('[ЕСЛИ `cs_friend_mz >= 3` И `cs_mz_hug_allowed_day3 == False`:]','[ИНАЧЕ ЕСЛИ `cs_friend_mz >= 3` И `cs_mz_hug_allowed_day3 == False`:]')
 ts=list(tokens(body));transcript[k]=[(w,t) for w,t in ts if w!='cue'];b=list(pre.get(k,[]));depth=0
 # At low trust keep the reply about the ending brief; do not claim intimacy.
 if k=='173':b+=['if cs_friend_mz >= 1:'];depth=1
 for who,w in ts:
  if who=='cue':
   if w.startswith('[ЕСЛИ '):b+=['if '+cond(w)+':'];depth=1
   elif w.startswith('[ИНАЧЕ ЕСЛИ '):b+=['elif '+cond(w)+':'];depth=1
   elif w.startswith('[ИНАЧЕ:]'):b+=['else:'];depth=1
   elif w.startswith('[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0
   elif w.startswith('[ФЛАГ:') and 'final_discussion = True' in w:b+=['    '*depth+'$ cs_mz_day3_final_discussion = True']
   continue
  pad='    '*depth
  if who in ('cs_da','cs_mz','cs_ls'):
   b += [pad+x for x in back()]
  b += [pad+x for x in hooks.get(k,{}).get(w,[])]
  if k=='179' and w=='Мику и Алиса ждут нас завтра в музыкальном клубе — если мы обещали прийти.':
   for flag,line in [('cs_mi_followup_invitation_day3','Мику ждёт нас завтра в музыкальном клубе — мы обещали зайти.'),('cs_dv_followup_invitation_day3','И Алисе я обещала послушать её новый переход.')]:b += [pad+'if '+flag+':',pad+'    cs_th '+json.dumps(line,ensure_ascii=False)]
   continue
  if w in variants:
   c,alt=variants[w];b += [pad+'if '+c+':',pad+'    '+who+' '+json.dumps(w,ensure_ascii=False),pad+'else:',pad+'    '+who+' '+json.dumps(alt,ensure_ascii=False)]
  else:b += [pad+who+' '+json.dumps(edits.get(w,w),ensure_ascii=False)]
  if k=='173' and w=='Она действительно всё запомнила.':
   b+=['else:','    cs_mz "Хорошо, что книга тебе подошла. А теперь давай её запишем — пора закрывать."','    cs_ls "Конечно. Спасибо, что дала закончить."'];depth=0
  emotions={'Женя усмехнулась.':('cs_zhenya','normal'),'Женя поправила очки.':('cs_zhenya','glasses_touch'),'Женя задумалась.':('cs_zhenya','thoughtful'),'Дарья рассмеялась.':('cs_darya','amused'),'Дарья улыбнулась.':('cs_darya','shy_smile')}
  if w in emotions:
   tag,emotion=emotions[w];b += [pad+'if renpy.showing("'+tag+'"):',pad+'    show '+tag+' '+emotion+' pioneer normal',pad+'    $ cs_presence_stage()',pad+'    with cs_sprite_change']
 p=P/(k+'_scene.rpy');out='# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n    return\n'
 if p.exists():out=preserve_calls(p.read_text(encoding='utf8'),out)
 p.write_text(out,encoding='utf8')
defaults=dict(cs_day03_part13_started=False,cs_day03_part13_done=False,cs_mz_book_finished_day3=False,cs_mz_day3_final_discussion=False,cs_da_day3_fear_of_getting_used_to_camp=False,cs_da_day3_quiet_walk=False,cs_da_day3_night_choice_done=False,cs_da_day3_night_trust_awarded=False,cs_da_waiting_outside_library_day3=False)
(P/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+k+' = '+repr(v)+'\n' for k,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(k+'='+repr(v) for k,v in defaults.items())+')\n\nimage cs_library_interior_night = LiveComposite((1920,1080), (0,0), "bg int_library_day", (0,0), Solid("#16203965"))\n',encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day03_part13:
    hide screen cs_day03_part12_wait_screen
    if cs_day03_part13_done:
        jump cs_day03_bedtime_pending
    $ cs_day03_part13_started = True
    call cs_day03_171
    call cs_day03_172
    call cs_day03_173
    call cs_day03_174
    call cs_day03_175
    call cs_day03_176
    call cs_day03_177
    call cs_day03_178
    call cs_day03_darya_night_choice
    call cs_day03_179
    $ cs_day03_part13_done = True
    jump cs_day03_bedtime_pending

label cs_day03_darya_night_choice:
    if cs_da_day3_night_choice_done:
        return
    $ cs_pov_end()
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_check_day03_178_menu:
    menu:
        "Рассказать Даше, почему меня задел финал книги":
            if not cs_da_day3_night_trust_awarded:
                $ cs_friend_da += 1
                $ cs_da_day3_night_trust_awarded = True
            $ cs_da_day3_fear_of_getting_used_to_camp = True
            $ cs_da_day3_night_choice_done = True
            call cs_day03_178a
        "Не нарушать тишину и просто идти рядом":
            $ cs_da_day3_quiet_walk = True
            $ cs_da_day3_night_choice_done = True
            call cs_day03_178b
    label cs_check_day03_178_result:
    return

label cs_day03_bedtime_pending:
    label cs_check_day03_part13_complete:
    call screen cs_day03_part13_wait_screen
    jump cs_day03_bedtime_pending

screen cs_day03_part13_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Последняя страница" size 26
            text "Девушки вернулись в домик. Впереди — разговор перед сном." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
p=P/'00_flow.rpy'
if p.exists():flow=preserve_calls(p.read_text(encoding='utf8'),flow)
p.write_text(flow,encoding='utf8')
p=R/'days/day03/part12/00_flow.rpy';t=p.read_text(encoding='utf8');t=t.replace('    call screen cs_day03_part12_wait_screen\n    jump cs_day03_library_closing_pending','    jump cs_day03_part13')
start=t.index('screen cs_day03_part12_wait_screen():');t=t[:start]+'screen cs_day03_part12_wait_screen():\n    timer 0.1 action Jump("cs_day03_part13")\n';p.write_text(t,encoding='utf8')
(R/'source/day03_part13_transcript.json').write_text(json.dumps(dict(source_blocks=sum(map(len,transcript.values())),scenes=transcript,edits=edits),ensure_ascii=False,indent=2),encoding='utf8')
print('PART13_GENERATED',sum(map(len,transcript.values())),'blocks;',len(scenes),'scene files')

if (R/"source/day03_part14.md").exists():
 import subprocess,sys
 subprocess.run([sys.executable,str(R/"tools/build_day03_part14.py")],check=True)
