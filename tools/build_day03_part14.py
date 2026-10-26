"""Authored last evening: preserve source dialogue, conditional consent and save anchors."""
from pathlib import Path
import re,json
from stabilize_call_helpers import preserve_calls
R=Path(__file__).resolve().parent.parent;P=R/'days/day03/part14';P.mkdir(exist_ok=True)
s=(R/'source/day03_part14.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена 180.'):s.index('## Задание для Codex')]
a=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)\n',s)
scenes={a[i].replace('А','a').replace('Б','b'):(a[i+1],a[i+2]) for i in range(1,len(a),3)}
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
def inward():return ['if not cs_reflective_shot:','    $ cs_pov_begin()','    with cs_sprite_leave']
def back():return ['if cs_reflective_shot:','    $ cs_pov_end()','    with cs_sprite_change']
def frame(bg,tags):return ['$ cs_director_scene("'+bg+'")','scene '+bg,'$ cs_frame_focus('+json.dumps(tags)+')','with Dissolve(0.7)']
def tokens(body):
 for raw in re.split(r'\n\s*\n',body):
  t=raw.strip().replace('**','')
  if not t or t=='---' or t.startswith(('#','- ','Выбор игрока:','1. «','2. «')):continue
  if t.startswith('['):yield 'cue',t;continue
  italic=t.startswith('*') and t.endswith('*');t=t.strip('*')
  m=re.match(r'(Лена Соколова(?: \([^)]*\))?|Дарья):\\?\s*[\n ]+[—–]\s*(.*)',t,re.S)
  who=('cs_da' if m[1]=='Дарья' else 'cs_ls') if m else ('cs_th' if italic else 'cs_narrator')
  yield who,(m[2] if m else t).replace('\n',' ')
def cond(t):
 vals=re.findall(r'(cs_\w+)\s*(>=|==)\s*(True|False|\d+)',t.replace('`',''))
 assert vals,t
 return (' or ' if 'ИЛИ' in t else ' and ').join(' '.join(v) for v in vals).replace(' == True','')
edits={
 'Мы уже почти дошли до домика.':'Я закрыла за нами дверь и на секунду задержалась у порога.',
 'За спиной остались площадь, библиотека и освещённые фонарями дорожки. Впереди виднелось наше крыльцо.':'За спиной остались библиотека и освещённые фонарями дорожки. Передо мной была наша комната.',
 'Наше.':'Наша.',
 'Она шла рядом, придерживая меня под здоровую руку.':'Она стояла рядом и ждала, пока я уберу руку с дверной ручки.',
 'Мы почти не разговаривали с того момента, как вышли из библиотеки.':'Последние шаги до двери мы прошли молча.',
 'На полке всё ещё находилась папка с концертным плакатом.':'На столе всё ещё находилась папка с концертным плакатом.',
 'Дарья сняла галстук.':'Дарья поправила ослабленный галстук.',
 'Аккуратно повесила его на спинку стула.':'Потом отодвинула стул, чтобы можно было пройти к кровати.',
 'Я переоденусь. Ты пока можешь умыться.':'Давай сначала умоемся. А потом переоденемся и ляжем.',
 'Когда вернулась, Даша уже переоделась и аккуратно складывала пионерскую форму.':'Когда я вернулась, Даша положила полотенце на спинку стула. Одежду для сна мы пока оставили рядом с подушками.',
 'Я тоже сменила одежду, пока она отвернулась.':'Я отложила своё полотенце и поправила рукав над повязкой.',
 'За то, что мы нормально провели время. Что ты не пыталась всё превращать в шутку. И что можно было просто посидеть рядом.':'За то, что можно было и поговорить, и просто посидеть рядом. И что за твоими шутками всё-таки слышно тебя.',
 'Знаешь, а ведь сегодня мы вообще довольно много времени провели рядом и почти не разговаривали.':'Знаешь, даже когда мы сегодня молчали, я не чувствовала себя одиноко.',
 'Не знаю, вернёмся ли мы домой. Не знаю, как долго здесь останемся. И даже не знаю, что мы будем делать завтра.':'Не знаю, вернёмся ли мы домой. Не знаю, как долго здесь останемся. И даже наши планы на завтра пока только планы.',
 'Даша, я могу шутить о Семёне сколько угодно. Но не собираюсь превращать наш разговор в лагерную новость.':'Даша, я иногда слишком увлекаюсь шутками. Но не собираюсь превращать наш разговор в лагерную новость.',
 'У меня появилась книга, которую хочется обсудить.':'У меня появилась прочитанная книга, к которой хочется вернуться в разговоре.',
 'Я медленно закрыла глаза.':'Я уже почти не различала собственные мысли.',
}
variants={
 'Женя, похоже, придерживается противоположного мнения.':('cs_mz_open_library_invitation_day3','Женя, по крайней мере, не запретила мне приходить снова.'),
 'И ни одного нового происшествия, после которого пришлось бы бежать к Виоле.':('cs_lena_elbow_bandaged','И ни одного нового происшествия.'),
 'Рисунки, которые хочется закончить.':('cs_un_sketch_completed_day3','Идеи для рисунков, которые хочется попробовать.'),
}
introchange=['cs_narrator "Мы по очереди переоделись, давая друг другу спокойно отвернуться, и сложили форму на стуле."']
pre={'180':frame('cs_house_lena_darya_int_night',['cs_darya'])+['$ night_time()','$ persistent.sprite_time = "night"','stop music fadeout 2.0'],
 '181':back()+focus(['cs_darya']), '182':[], '183':back()+focus(['cs_darya']),
 '184':frame('cs_house_lena_darya_int_night',[])+introchange,
 '185':frame('cs_house_lena_darya_int_night',[])+introchange,
 '186':['play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0','$ renpy.music.set_volume(0.08,channel="music",delay=1.0)'],
 '187':[], '187a':[], '187b':[], '188':['stop music fadeout 4.0'], '189':[]}
transcript={}
for k,(title,body) in scenes.items():
 ts=list(tokens(body));transcript[k]=[(w,t) for w,t in ts if w!='cue'];b=list(pre[k]);depth=0;skip=False;thoughts=0
 for who,w in ts:
  if who=='cue':
   if w.startswith('[ЕСЛИ '):b+=['if '+cond(w)+':'];depth=1
   elif w.startswith('[ИНАЧЕ'):b+=['else:'];depth=1
   elif w.startswith('[ОБЩЕЕ ПРОДОЛЖЕНИЕ'):depth=0
   continue
  # Part13 already brought the girls inside; never replay the door/arrival.
  if k=='180' and w=='Мы поднялись на крыльцо.':skip=True
  if k=='180' and w=='На столе лежали мой блокнот и карандаши. Рядом — аккуратно сложенные вещи.':skip=False
  if skip:continue
  pad='    '*depth
  if k in ('180','181','182','183'):
   thoughts=thoughts+1 if who=='cs_th' else 0
   if thoughts==3:b += [pad+x for x in inward()]
   if who in ('cs_da','cs_ls'):b += [pad+x for x in back()]
  if (k=='184' and w=='Я выключила лампу.') or (k=='185' and w=='Щёлкнул выключатель.'):
   b += [pad+x for x in frame('cs_house_lena_darya_int_sleep_night',[])]
  if k=='181' and w=='Я взяла полотенце и ненадолго вышла.':b += [pad+x for x in inward()]
  if k=='181' and w.startswith('Когда вернулась,'):b += [pad+x for x in back()]
  if k=='188' and w=='Я закрыла глаза.':
   b += [pad+'cs_narrator "Я повернулась на бок. Даша осторожно придвинулась сзади, оставив моей перевязанной руке свободное место."']
   b += [pad+x for x in frame('cs_cg_lena_darya_shared_sleep_night',[])]+[pad+'$ cs_da_shared_sleep_cg_seen_day3 = True']
  if w in variants:
   c,alt=variants[w];b += [pad+'if '+c+':',pad+'    '+who+' '+json.dumps(edits.get(w,w),ensure_ascii=False),pad+'else:',pad+'    '+who+' '+json.dumps(alt,ensure_ascii=False)]
  else:b += [pad+who+' '+json.dumps(edits.get(w,w),ensure_ascii=False)]
  if k=='183' and w=='А я не собираюсь превращать это согласие в обязательство на каждый следующий вечер.':
   b += ['    $ cs_da_shared_bed_day3 = True','    if not cs_da_shared_bed_awarded_day3:','        $ cs_friend_da += 1','        $ cs_da_shared_bed_awarded_day3 = True']
  if k=='181' and w=='Сегодня многое изменилось.':
   b += ['if cs_da_day3_fear_of_getting_used_to_camp:','    cs_th "Я уже смогла сказать ей, почему боюсь привыкнуть к лагерю. И она выслушала."','elif cs_da_day3_music_talk:','    cs_th "После разговора о музыке мне стало легче говорить с ней без заготовленных шуток."']
  if k in ('180','181','183') and w in ('Дарья рассмеялась.','Даша рассмеялась.','Она улыбнулась.'):
   em='amused' if 'рассмеялась' in w else 'shy_smile'
   b += [pad+'if renpy.showing("cs_darya"):',pad+'    show cs_darya '+em+' pioneer normal',pad+'    $ cs_presence_stage()',pad+'    with cs_sprite_change']
 if k=='189':b += ['stop music fadeout 2.0','stop ambience fadeout 2.0']+frame('black',[])+['show text "Конец третьего дня" at truecenter','with Dissolve(1.0)','$ renpy.pause(2.0)','hide text','with Dissolve(1.0)']
 p=P/(k+'_scene.rpy');out='# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n    return\n'
 if p.exists():out=preserve_calls(p.read_text(encoding='utf8'),out)
 p.write_text(out,encoding='utf8')
defaults=dict(cs_day03_part14_started=False,cs_day03_part14_done=False,cs_day03_completed=False,cs_da_friend_before_night=None,cs_da_bed_request_day3=False,cs_da_respected_space_day3=False,cs_da_shared_bed_day3=False,cs_da_love_confession_day3=False,cs_da_unspoken_feelings_day3=False,cs_da_bed_choice_done_day3=False,cs_da_shared_bed_awarded_day3=False,cs_da_confession_choice_done_day3=False,cs_da_shared_sleep_cg_seen_day3=False)
(P/'resources.rpy').write_text('# -*- coding: utf-8 -*-\n'+''.join('default '+k+' = '+repr(v)+'\n' for k,v in defaults.items())+'init -9 python:\n    cs_state_defaults.update('+', '.join(k+'='+repr(v) for k,v in defaults.items())+')\nimage cs_house_lena_darya_int_sleep_night = LiveComposite((1920,1080), (0,0), "cs_house_lena_darya_int_night", (0,0), Solid("#10152660"))\nimage cs_cg_lena_darya_shared_sleep_night = im.Scale(cs_resolve_asset("cg/lena_n_dasha/cg_lena_darya_shared_sleep_night.png"),1920,1080)\n',encoding='utf8')
flow='''# -*- coding: utf-8 -*-
label cs_day03_part14:
    hide screen cs_day03_part13_wait_screen
    if cs_day03_part14_done:
        jump cs_day04_pending
    $ cs_day03_part14_started = True
    call cs_day03_180
    call cs_day03_181
    if cs_da_friend_before_night is None:
        $ cs_da_friend_before_night = cs_friend_da
    call cs_day03_182
    call cs_day03_bed_choice
    if cs_da_shared_bed_day3:
        call cs_day03_185
        call cs_day03_186
        call cs_day03_187
        call cs_day03_confession_choice
        call cs_day03_188
    else:
        call cs_day03_184
    call cs_day03_189
    $ cs_day03_part14_done = cs_day03_completed = True
    jump cs_day04_pending

label cs_day03_bed_choice:
    if cs_da_bed_choice_done_day3:
        return
    if cs_da_friend_before_night is None:
        $ cs_da_friend_before_night = cs_friend_da
    $ cs_pov_end()
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_check_day03_182_menu:
    menu:
        "Сказать Даше, что сегодня хочется спать рядом с ней":
            $ cs_da_bed_request_day3 = True
            call cs_day03_183
        "Не торопить события и пожелать Даше спокойной ночи":
            $ cs_da_respected_space_day3 = True
            $ cs_da_shared_bed_day3 = False
            cs_ls "Давай отдыхать. Спокойной ночи, Даш."
            cs_da "И тебе, Лен."
    $ cs_da_bed_choice_done_day3 = True
    label cs_check_day03_182_result:
    return

label cs_day03_confession_choice:
    if cs_da_confession_choice_done_day3 or not cs_da_shared_bed_day3:
        return
    if cs_da_friend_before_night >= 2:
        label cs_check_day03_187_menu:
        menu:
            "Сказать Даше: «Я тебя люблю»":
                $ cs_da_love_confession_day3 = True
                call cs_day03_187a
            "Не торопить события и просто остаться рядом":
                $ cs_da_unspoken_feelings_day3 = True
                call cs_day03_187b
    else:
        $ cs_da_unspoken_feelings_day3 = True
        call cs_day03_187b
    $ cs_da_confession_choice_done_day3 = True
    return

label cs_day04_pending:
    label cs_check_day03_part14_complete:
    call screen cs_day04_wait_screen
    jump cs_day04_pending

screen cs_day04_wait_screen():
    modal True
    frame:
        align (0.5,0.5)
        padding (32,24)
        background Solid("#142821ed")
        vbox:
            spacing 16
            text "Третий день завершён" size 32
            text "Продолжение — в четвёртом дне." size 24
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
'''
p=P/'00_flow.rpy'
if p.exists():flow=preserve_calls(p.read_text(encoding='utf8'),flow)
p.write_text(flow,encoding='utf8')
p=R/'days/day03/part13/00_flow.rpy';t=p.read_text(encoding='utf8').replace('    call screen cs_day03_part13_wait_screen\n    jump cs_day03_bedtime_pending','    jump cs_day03_part14');t=t[:t.index('screen cs_day03_part13_wait_screen():')]+'screen cs_day03_part13_wait_screen():\n    timer 0.1 action Jump("cs_day03_part14")\n';p.write_text(t,encoding='utf8')
(R/'source/day03_part14_transcript.json').write_text(json.dumps(dict(source_blocks=sum(map(len,transcript.values())),scenes=transcript,edits=edits),ensure_ascii=False,indent=2),encoding='utf8')
print('PART14_GENERATED',sum(map(len,transcript.values())),'blocks;',len(scenes),'scenes')
