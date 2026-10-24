"""Day 3 part 2: verbatim dialogue, explicit camera cuts and stable actor tags."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
D=R/'days/day03/part02';D.mkdir(parents=True,exist_ok=True)
s=(R/'source/day03_part02.md').read_text(encoding='utf8')
s=s[s.index('### Сцена 83.'):s.index('## Техническое задание')]
p=re.split(r'### Сцена (\d+[А-Я]?)\. ([^\n]+)\n',s)
sections={p[i]:(p[i+1],p[i+2]) for i in range(1,len(p),3)}
expected={}
def blocks(s):
 out=[]
 for raw in re.split(r'\n\s*\n',s):
  t=raw.strip()
  if not t or t=='---' or t.startswith(('#','**[','**Вариант','- ')):continue
  m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
  if m:
   name,text=m.groups();who={'Дарья':'cs_da','Семён':'cs_sy','Лена Соколова':'cs_ls'}[name]
  elif t.startswith('*') and t.endswith('*'):who,text='cs_th',t[1:-1]
  else:who,text='cs_narrator',t
  out.append((who,text.replace('\n',' ')))
 return out

def scene(image,cast=False):
 a=['$ cs_director_scene('+json.dumps(image)+')','scene '+image]
 if cast:a+=['show cs_darya shy_smile pioneer normal at cs_darya_normal_right','$ cs_frame_focus(["cs_darya"])']
 return a+['with Dissolve(0.8)']
def da(pose):return ['show cs_darya '+pose+' pioneer normal','$ cs_presence_stage()','with cs_sprite_change']
def se(pose):return ['show cs_semen '+pose+' pioneer normal','$ cs_presence_stage()','with cs_sprite_change']
# Hooks are authored against exact manuscript beats, never speaker callbacks.
hooks={
 '83':{
 'И вошла.':scene('cs_house_lena_darya_int_day')+['play ambience "sound/ambiences/int_cabin_day.ogg" fadein 1.0','label cs_check_day03_83_door:'],
 'Дарья стояла возле своей кровати.':['show cs_darya neutral underwear normal at cs_day03_darya_enter','$ renpy.pause(0.30, hard=True)','with None','$ cs_frame_focus(["cs_darya"])','label cs_check_day03_83_underwear:'],
 'Я немедленно повернулась к двери.':['$ cs_reflective_focus()','with cs_sprite_leave','label cs_check_day03_83_turned_away:'],
 'Она уже была в пионерской форме.':['with None','show cs_darya neutral pioneer normal at cs_day03_darya_enter','label cs_check_day03_83_enter:','$ renpy.pause(0.30, hard=True)','with None','$ cs_frame_focus(["cs_darya"])','label cs_check_day03_83_dressed:'],
 'Она усмехнулась.':da('shy_smile'), 'Дарья рассмеялась.':da('amused'),
 'Она слегка удивилась.':da('neutral'), 'Дарья улыбнулась.':da('shy_smile'),
 'Тогда предлагаю ввести небольшой свод правил.':da('thinking'),
 'Потом медленно улыбнулась.':da('shy_smile'),
 },
 '84':{
 'Дарья тем временем завязывала галстук.':da('tie_touch'),
 'Дарья указала на тумбочку.':da('explaining'),
 'Дарья внимательно посмотрела на повязку.':da('worried'),
 'Она приподняла бровь.':da('arms_crossed'),
 'Дарья немного расслабилась.':da('neutral'),
 'Дарья рассмеялась.':da('amused'),
 'В следующий раз можешь меня разбудить.':da('shy_smile'),
 # This is a brief glance at the mirror, not the day-one CG in Olga's cabin.
 'Посмотрела на себя в зеркало.':['label cs_check_day03_84_mirror:'],
 'Всё, готово.':['label cs_check_day03_84_restored:'],
 'Без пробежек и без неожиданных экспериментов.':da('arms_crossed'),
 },
 '85':{'Дарья поправила волосы.':da('hair_touch'),'Дарья рассмеялась.':da('amused'),'Дарья улыбнулась.':da('shy_smile'),'Дарья замолчала.':da('thinking')},
 '85a':{'Она удивилась.':da('neutral'),'Дарья улыбнулась.':da('shy_smile'),'Дарья рассмеялась.':da('amused')},
 '85b':{'Дарья улыбнулась.':da('shy_smile')},
 '85c':{'Я открыла дверь.':scene('cs_house_lena_darya_ext_day',True)},
 '86':{
 'Дарья рассмеялась.':da('amused'), 'Она остановилась.':da('thinking'),
 'Дарья усмехнулась.':da('shy_smile'),
 'Заметив нас, остановился.':['show cs_semen neutral pioneer normal at cs_semen_normal_left','$ cs_frame_focus(["cs_semen", "cs_darya"])','with cs_sprite_enter','label cs_check_day03_86_semen:'],
 'Он прищурился.':se('thinking'), 'Семён усмехнулся.':se('smile'),
 },
 '87a':{
 'Он немного удивился.':se('awkward'), 'Семён немного помолчал.':se('thinking'),
 'Дарья перестала улыбаться.':da('serious'), 'Семён немного удивился.':se('awkward'),
 'Дарья тихо усмехнулась.':da('shy_smile'), 'Семён улыбнулся.':se('smile'),
 'Семён немного задумался.':se('thinking'), 'Потом чуть улыбнулся.':se('smile'),
 },
 '87b':{'Он приподнял бровь.':se('awkward'),'Дарья улыбнулась.':da('shy_smile'),'Семён рассмеялся.':se('smile')},
 '88':{
 'Я проводила его взглядом.':['$ cs_actor_exit(["cs_semen"])','with cs_sprite_leave','label cs_check_day03_88_semen_left:'],
 'Дарья рассмеялась.':da('amused'), 'Она немного подумала.':da('thinking'),
 'Просто хотела сказать, что тебе сегодня очень идёт форма.':da('shy_smile')+['label cs_check_day03_88_compliment:'],
 'Дарья улыбнулась.':da('shy_smile'),
 'Мы приблизились к столовой.':['label cs_check_day03_88_dining:'],
 'Мы поднялись по ступенькам столовой.':[],
 }
}
def emit(key,title,text,pre=(),post=()):
 expected[key]=blocks(text)
 out=['# -*- coding: utf-8 -*-','label cs_day03_'+key+':','    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)]
 body=list(pre);last=None;dressed=False
 for who,words in expected[key]:
  if key=='88' and words=='Мы поднялись по ступенькам столовой.':words='До столовой оставалось совсем немного.'
  commands=hooks.get(key,{}).get(words,[])
  if key=='83' and words=='Она уже была в пионерской форме.':dressed=True
  if key=='83' and not dressed and words=='Дарья улыбнулась.':
   commands=['show cs_darya hair_touch underwear normal','$ cs_presence_stage()','with cs_sprite_change','label cs_check_day03_83_hair_touch:']
  if commands and commands[0].startswith('show '):
   if last==commands[0]:commands=[]
   else:last=commands[0]
  body+=commands+[who+' '+json.dumps(words,ensure_ascii=False)]
 body+=list(post)+['return'];out+=['    '+x for x in body]
 (D/(key+'_scene.rpy')).write_text('\n'.join(out)+'\n',encoding='utf8')

emit('83',*sections['83'],pre=scene('cs_house_lena_darya_ext_day')+['$ cs_frame_focus([])','play music "sound/music/my_daily_life.ogg" fadein 2.0','$ renpy.music.set_volume(0.2,channel="music")','play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0','$ renpy.music.set_volume(0.17,channel="ambience")','label cs_check_day03_83:'])
emit('84',*sections['84'])
main,tail=sections['85'][1].split('**[ЕСЛИ `cs_sl_poster_saved_day3 == True`:]**')
high,tail=tail.split('**[ИНАЧЕ:]**');low,common=tail.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
emit('85',sections['85'][0],main,post=['if cs_sl_poster_saved_day3:','    call cs_day03_85a','else:','    call cs_day03_85b','label cs_check_day03_85_poster_result:','call cs_day03_85c'])
emit('85a','Первый советский сувенир',high)
emit('85b','Утренняя встреча',low)
emit('85c','Выход к завтраку',common)
emit('86',*sections['86'],pre=scene('cs_camp_path_day',True)+['play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0'])
emit('87',sections['87'][0],sections['87'][1].split('**[MENU')[0],post=['call cs_day03_semen_choice'])
emit('87a',*sections['87А'],pre=['label cs_check_day03_87a:'])
emit('87b',*sections['87Б'],pre=['label cs_check_day03_87b:'])
emit('88',*sections['88'])
(D/'00_flow.rpy').write_text('''# -*- coding: utf-8 -*-
label cs_day03_part02:
    hide screen cs_day03_part01_wait_screen
    $ cs_day03_part01_done = True
    window show dissolve
    call cs_day03_83
    call cs_day03_84
    call cs_day03_85
    call cs_day03_86
    call cs_day03_87
    call cs_day03_88
    $ cs_day03_part02_done = True
    jump cs_day03_part03_pending

label cs_day03_semen_choice:
    label cs_check_day03_87_menu:
    menu:
        "Спросить Семёна, как у него дела":
            if not cs_se_day3_morning_awarded:
                $ cs_friend_se += 1
                $ cs_se_day3_morning_awarded = True
            call cs_day03_87a
        "Не задерживать его перед завтраком":
            call cs_day03_87b
    return

label cs_day03_part03_pending:
    label cs_check_day03_part02_complete:
    hide screen cs_day03_part02_wait_screen
    jump cs_day03_part03

screen cs_day03_part02_wait_screen():
    modal True
    frame:
        align (0.03, 0.06)
        padding (24, 20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Двадцать секунд самоконтроля" size 26
            text "Продолжение — за завтраком." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
''',encoding='utf8')
(D/'resources.rpy').write_text('''# -*- coding: utf-8 -*-
default cs_day03_part02_done = False
default cs_se_day3_morning_awarded = False
init -9 python:
    cs_state_defaults.update(cs_day03_part02_done=False, cs_se_day3_morning_awarded=False)

# Fade only the entering actor; the whole-scene transition must not reuse
# a transient placement of the newly rendered full-height image.
transform cs_day03_darya_enter:
    xpos 0.5
    xanchor 0.5
    ypos 1.60
    yanchor 1.0
    zoom 1.0
    xoffset 0
    yoffset 0
    alpha 0.0
    linear 0.28 alpha 1.0
''',encoding='utf8')
(R/'source/day03_part02_transcript.json').write_text(json.dumps(expected,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 2:',sum(map(len,expected.values())),'dialogue/narrative blocks in',len(expected),'scene files')
