"""Day3 part5: authored frames, document delivery, guarded Sl choice and poster."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent;D=R/'days/day03/part05';D.mkdir(parents=True,exist_ok=True)
s=(R/'source/day03_part05.md').read_text(encoding='utf8');s=s[s.index('### Сцена 104.'):s.index('## Техническое задание')]
p=re.split(r'### Сцена (\d+[А-Я]?)\. ([^\n]+)\n',s);parts={p[i]:(p[i+1],p[i+2]) for i in range(1,len(p),3)};transcript={}
def parse(t):
 out=[]
 for t in re.split(r'\n\s*\n',t):
  t=t.strip()
  if not t or t=='---' or t.startswith(('#','**[','- ')):continue
  m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
  if m:
   n,w=m.groups();who={'Лена Соколова':'cs_ls','Дарья':'cs_da','Ольга Дмитриевна':'cs_mt','Славя':'cs_sl','Семён':'cs_sy'}[n]
  elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
  else:who,w='cs_narrator',t
  out.append((who,w.replace('\n',' ')))
 return out
def pose(tag,p):
 attrs=' '+p+' pioneer'+(' normal' if tag.startswith('cs_') else '')
 return ['if renpy.showing("'+tag+'"):', '    show '+tag+attrs,'    $ cs_presence_stage()','    with cs_sprite_change']
def frame(bg,actor=None,expression='normal'):
 a=['$ cs_director_scene("'+bg+'")','scene '+bg,'show cs_darya neutral pioneer normal at cs_darya_normal_right']
 if actor:a+=['show '+actor+' '+expression+' pioneer at cs_actor_left']
 return a+['$ cs_presence_stage()','with Dissolve(0.8)']
def focus(tags):return ['$ cs_frame_focus('+json.dumps(tags)+')','with cs_sprite_change']
reflect=['$ cs_reflective_focus()','with cs_sprite_leave']
hooks={
 '104':{'Мы свернули к домикам.':frame('cs_camp_path_day')},
 '105':{'Доброе. Что на этот раз?':pose('mt','normal'),'Она приподняла бровь.':pose('mt','surprise'),'Сама?':pose('mt','surprise'),'Ольга Дмитриевна заметно расслабилась.':pose('mt','smile'),'Ольга Дмитриевна протянула её Дарье.':['$ cs_day03_documents_location = "darya"','label cs_check_day03_105_documents:'],'Если будете меньше разговаривать, управитесь быстрее.':pose('mt','grin')},
 '106':{'Она немедленно насторожилась.':pose('mt','normal'),'Ольга Дмитриевна прищурилась.':pose('mt','angry'),'Потом неожиданно тоже усмехнулась.':pose('mt','grin'),'Она посмотрела на меня уже без улыбки.':pose('mt','normal'),'Ольга Дмитриевна посмотрела на меня с явным удивлением.':pose('mt','surprise'),'Ольга Дмитриевна посмотрела на нас обеих.':pose('mt','smile'),'Мы попрощались и направились к площади.':['$ cs_actor_exit(["mt"])']+frame('cs_camp_path_day')+['label cs_check_day03_106_mt_left:'],'И, пожалуй, это было важнее всех моих шуток.':reflect},
 '107':{'Административное помещение оказалось совсем не таким, каким я его себе представляла.':['$ cs_director_scene("cs_int_administration_day")','scene cs_int_administration_day','with Dissolve(0.8)','$ renpy.music.set_volume(0.07,delay=0.5,channel="ambience")','label cs_check_day03_107_administration:'],'Дарья передала папку.':['$ cs_day03_documents_location = "administration"','$ cs_day03_documents_delivered = True','label cs_check_day03_107_delivered:'],'Мы вышли обратно на дорожку.':frame('cs_ext_administration_day')+['$ renpy.music.set_volume(0.18,delay=1.0,channel="ambience")','label cs_check_day03_107_back:'],'Мы направились к клубам.':frame('cs_camp_path_day')},
 '108':{'Она рассмеялась.':pose('sl','laugh'),'Славя немного удивилась.':pose('sl','surprise'),'Славя кивнула.':pose('sl','normal'),'Славя улыбнулась.':pose('sl','smile'),'Славя засмеялась.':pose('sl','laugh')},
 '109a':{'Мы устроились за столом.':['label cs_check_day03_109_seated:'],'Славя подошла.':pose('sl','normal'),'Славя рассмеялась.':pose('sl','laugh'),'Она улыбнулась.':pose('sl','smile'),'Она довольно улыбнулась.':pose('sl','smile')},
 '109b':{'Она посмотрела на повязку.':pose('sl','normal'),'Славя улыбнулась.':pose('sl','smile'),'Славя рассмеялась.':pose('sl','laugh')},
 '110':{'Дарья осторожно взяла её.':['$ cs_sl_poster_collected_day3 = True','$ cs_day03_poster_location = "darya_folder"','label cs_check_day03_110_poster_received:'],'Славя рассмеялась.':pose('sl','laugh'),'Я отошла от стола.':frame('cs_camp_path_day')+['label cs_check_day03_110_sl_left:']},
 '111':{'Увидев нас, он остановился.':['with None','show cs_semen neutral pioneer normal at cs_day03_p3_actor_enter(0.25)','$ renpy.pause(0.30,hard=True)','show cs_semen neutral pioneer normal at Transform(xpos=0.25,xanchor=0.5,ypos=1.60,yanchor=1.0,zoom=1.0,alpha=1.0)','$ cs_presence_stage()','with None','label cs_check_day03_111_semen:'],'Он прищурился.':pose('cs_semen','thinking'),'Он закрыл глаза.':pose('cs_semen','awkward'),'Потом неожиданно улыбнулся.':pose('cs_semen','smile'),'Семён рассмеялся.':pose('cs_semen','smile'),'Он говорил спокойно, но вполне серьёзно.':pose('cs_semen','serious'),'Да. Ты попросил — я услышала.':['$ cs_semen_privacy_respected_day3 = True','label cs_check_day03_111_boundary:'],'Семён удивился.':pose('cs_semen','surprised'),'Семён направился по дорожке.':['$ cs_actor_exit(["cs_semen"])','with cs_sprite_leave','label cs_check_day03_111_semen_left:']},
 '112':{'Хотя слово «собственными» здесь всё ещё звучало немного странно.':reflect+['label cs_check_day03_112_reflection:'],'О чём задумалась?':focus(['cs_darya'])+['label cs_check_day03_112_dialogue:'],'Мы свернули к библиотеке.':['$ cs_day03_part06_route = "library"','label cs_check_day03_112_library:'],'Мы направились к клубам.':['$ cs_day03_part06_route = "music"','label cs_check_day03_112_music:']}
}
for key in ('104','105','106','107','108','109','109a','109b','110','111','112'):
 h=hooks.setdefault(key,{})
 for w,p in [('Дарья рассмеялась.','amused'),('Дарья улыбнулась.','shy_smile'),('Дарья тихо рассмеялась.','amused'),('Дарья приподняла бровь.','thinking'),('Она посмотрела на меня с подозрением.','thinking')]:h.setdefault(w,pose('cs_darya',p))
def write(k,segments,pre=(),post=()):
 b=list(pre);transcript[k]=[]
 for x in segments:
  if isinstance(x,list):b+=x;continue
  text,depth=x;indent='    '*depth
  for who,w in parse(text):
   transcript[k].append((who,w));b += [indent+y for y in hooks.get(k,{}).get(w,[])]
   if k=='104' and w.startswith('От медпункта мы успели отойти всего'):
    b+=['if cs_day03_part05_legacy_entry:','    cs_narrator "Мы ещё не успели далеко уйти от развилки, когда мне в голову пришла очередная мысль."','else:','    cs_narrator '+json.dumps(w,ensure_ascii=False)];continue
   if k=='110' and w=='А сегодня хотя бы понятно, зачем нужно пересчитать шесть красных лент.':
    b+=['if cs_helped_sl_day3:','    cs_ls '+json.dumps(w,ensure_ascii=False),'else:','    cs_ls "А сегодня хотя бы понятно, зачем нужно отнести документы в администрацию."'];continue
   b.append(indent+who+' '+json.dumps(w,ensure_ascii=False))
 b+=list(post)+['return'];title=parts[k.replace('a','А').replace('b','Б')][0]
 (D/(k+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\nlabel cs_day03_'+k+':\n    $ save_name = '+json.dumps('Чужая смена — День 3: '+title,ensure_ascii=False)+'\n'+'\n'.join('    '+x for x in b)+'\n',encoding='utf8')
def one(k,pre=(),post=()):write(k,[(parts[k][1],0)],pre,post)
one('104',pre=['if cs_day03_part05_legacy_entry:']+['    '+x for x in frame('cs_camp_path_day')]+['else:']+['    '+x for x in frame('bg ext_aidpost_day')]+['if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":','    play music "sound/music/my_daily_life.ogg" fadein 2.0','play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0','label cs_check_day03_104:'])
one('105',pre=frame('bg ext_house_of_mt_day','mt')+['label cs_check_day03_105:'])
one('106');one('107',pre=frame('cs_ext_administration_day')+['label cs_check_day03_107_exterior:','cs_narrator "Мы поднялись на крыльцо административного корпуса."'])
one('108',pre=frame('bg ext_clubs_day','sl','smile')+['label cs_check_day03_108:'])
write('109',[(parts['109'][1].split('**Выбор:**')[0],0)],post=['call cs_day03_slavya_inventory_choice'])
write('109a',[(parts['109А'][1],0)]);write('109b',[(parts['109Б'][1],0)])
t=parts['110'][1];_,t=t.split('**[ЕСЛИ `cs_sl_poster_saved_day3 == True` И `cs_sl_poster_collected_day3 == False`:]**');yes,t=t.split('**[ИНАЧЕ:]**');no,tail=t.split('**[ОБЩЕЕ ПРОДОЛЖЕНИЕ.]**')
write('110',[['if cs_sl_poster_saved_day3 and not cs_sl_poster_collected_day3:'],(yes,1),['else:'],(no,1),(tail,0)],post=['label cs_check_day03_110_result:'])
one('111',pre=['$ cs_frame_focus(["cs_darya"])','with cs_sprite_change'])
t=parts['112'][1];base,t=t.split('**[ЕСЛИ `cs_mz_map_lead == True`:]**');yes,no=t.split('**[ИНАЧЕ:]**')
write('112',[(base,0)],pre=frame('cs_camp_path_day'))
(D/'resources.rpy').write_text('''# -*- coding: utf-8 -*-
default cs_day03_part05_done = False
default cs_day03_part05_started = False
default cs_day03_part05_legacy_entry = False
default cs_sl_day3_awarded = False
default cs_helped_sl_day3 = False
default cs_sl_poster_collected_day3 = False
default cs_day03_documents_location = None
default cs_day03_documents_delivered = False
default cs_semen_privacy_respected_day3 = False
default cs_day03_part06_route = None
image cs_ext_administration_day = im.Scale(cs_root + "bg/admin_camp/ext_administration_day.png",1920,1080)
image cs_int_administration_day = im.Scale(cs_root + "bg/admin_camp/int_administration_day.png",1920,1080)
init -9 python:
    cs_state_defaults.update(cs_day03_part05_done=False,cs_day03_part05_started=False,
        cs_day03_part05_legacy_entry=False,cs_sl_day3_awarded=False,cs_helped_sl_day3=False,
        cs_sl_poster_collected_day3=False,cs_day03_documents_location=None,
        cs_day03_documents_delivered=False,cs_semen_privacy_respected_day3=False,
        cs_day03_part06_route=None)
''',encoding='utf8')
(D/'00_flow.rpy').write_text('''# -*- coding: utf-8 -*-
label cs_day03_part05:
    if cs_day03_part05_done:
        jump cs_day03_part06_pending
    hide screen cs_day03_part04_wait_screen
    $ cs_day03_part05_started = True
    $ cs_day03_part04_done = True
    $ cs_day03_part05_route = None
    call cs_day03_104
    call cs_day03_105
    call cs_day03_106
    call cs_day03_107
    call cs_day03_108
    call cs_day03_109
    call cs_day03_110
    call cs_day03_111
    call cs_day03_112
    $ cs_day03_part05_done = True
    jump cs_day03_part06_pending

label cs_day03_slavya_inventory_choice:
    label cs_check_day03_109_menu:
    menu:
        "Помочь Славе закончить учёт инвентаря":
            if not cs_sl_day3_awarded:
                $ cs_friend_sl += 1
                $ cs_sl_day3_awarded = True
            $ cs_helped_sl_day3 = True
            call cs_day03_109a
        "Извиниться и отправиться по своим делам":
            call cs_day03_109b
    label cs_check_day03_109_result:
    return

label cs_day03_part05_legacy:
    $ cs_day03_part05_legacy_entry = True
    jump cs_day03_part05

label cs_day03_part06_pending:
    label cs_check_day03_part05_complete:
    jump cs_day03_part06

label cs_check_day03_112_library:
    jump cs_day03_part06
label cs_check_day03_112_music:
    jump cs_day03_part06

screen cs_day03_part05_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Общественно полезная деятельность" size 26
            if cs_day03_part06_route == "library":
                text "Дальше — старые каталоги в библиотеке." size 22
            else:
                text "Дальше — музыкальный кружок." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
''',encoding='utf8')
(R/'source/day03_part05_transcript.json').write_text(json.dumps(transcript,ensure_ascii=False,indent=2),encoding='utf8')
print('Part5:',sum(map(len,transcript.values())),'manuscript blocks in',len(transcript),'scene files')
import runpy
runpy.run_path(str(R/'tools/apply_medpoint_continuity.py'))
