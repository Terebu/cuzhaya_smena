"""Compile the supplied day-three transcript with explicit authored staging."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
S=(R/'source/day03_part01.md').read_text(encoding='utf8')
story=S[S.index('### Сцена 74А.'):S.index('## Задание для Codex')]
parts=re.split(r'### Сцена (\d+[А-Я]?)\. ([^\n]+)\n',story)
sections={parts[i]:(parts[i+1],parts[i+2]) for i in range(1,len(parts),3)}
expected={}

def parse(text):
    blocks=[]
    for paragraph in re.split(r'\n\s*\n',text):
        p=paragraph.strip()
        if not p or p=='---' or p.startswith(('#','**[')):continue
        m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',p,re.S)
        if m:
            name,words=m.groups()
            who='cs_da' if name.startswith('Дарья') else 'cs_sl' if name.startswith('Славя') else 'cs_ls'
        elif p.startswith('*') and p.endswith('*'):
            who,words='cs_th',p[1:-1]
        else:who,words='cs_narrator',p
        blocks.append((who,words.replace('\n',' ')))
    return blocks

def scene(image,early=False):
    return ['$ cs_director_scene('+json.dumps(image)+')','scene '+image+(' at cs_day03_dawn' if early else ''),'with Dissolve(0.8)']
def actor(tag,pose):
    if tag=='sl':spec='sl '+pose+' pioneer at cs_actor_left'
    else:spec='cs_darya '+pose+' pioneer normal at cs_darya_normal_center'
    return ['show '+spec,'$ cs_presence_stage()','with cs_sprite_change']

def frame(image,tag,pose,early=False):
    # Carry the companion into the new view before the transition starts.
    return scene(image,early)[:2]+actor(tag,pose)[:2]+['with Dissolve(0.8)']

# Exact paragraph anchors are authored directions, never runtime text heuristics.
events={
 '74a':{
  'Она подняла голову.':actor('da','neutral'),
  '— Тогда нет.':[],
  'Тогда нет.':actor('da','arms_crossed'),
  'Дарья тихо рассмеялась.':actor('da','amused'),
  'И неожиданно улыбнулась.':actor('da','shy_smile'),
  'Лена, это не обещание.':actor('da','thinking'),
  'Спи уже, переговорщица.':actor('da','shy_smile'),
  'Я повернулась на бок, стараясь не задевать повреждённый локоть.':['$ cs_reflective_focus()','with cs_sprite_leave'],
 },
 '75':{
  'Потом посмотрела на себя.':scene('cs_cg_lena_sport_mirror_bandaged_morning',True)+['label cs_check_day03_mirror:'],
  'Я тихо усмехнулась.':scene('cs_house_lena_darya_int_day',True),
  'И вышла наружу.':scene('cs_house_lena_darya_ext_day',True),
 },
 '76':{
  'Я направилась к площади.':scene('bg ext_square_day',True),
  'В сторону спортивной площадки.':scene('bg ext_playground_day',True)+['label cs_check_day03_sport:'],
 },
 '77':{
  'Она рассмеялась.':actor('sl','laugh'),
  'Славя посмотрела на мой локоть.':actor('sl','normal'),
  'И скрестила руки.':actor('sl','normal'),
  'Она улыбнулась.':actor('sl','smile'),
 },
 '78a':{
  'Она засмеялась.':actor('sl','laugh'),
  'Она немного задумалась.':actor('sl','normal'),
  'Я улыбнулась.':actor('sl','smile'),
 },
 '78b':{'Славя рассмеялась.':actor('sl','laugh'),'Славя закрыла коробку.':actor('sl','normal')},
 '79':{'Она нахмурилась.':actor('sl','sad'),'Она заметно расслабилась.':actor('sl','smile'),'Славя рассмеялась.':actor('sl','laugh')},
 '80':{'Она удивлённо посмотрела на меня.':actor('sl','surprise'),'Она рассмеялась.':actor('sl','laugh'),'Славя заинтересованно повернулась.':actor('sl','normal'),'Славя остановилась.':actor('sl','surprise'),'Потом рассмеялась.':actor('sl','laugh'),'Я посмотрела на неё.':actor('sl','smile')},
 '81':{'Она рассмеялась.':actor('sl','laugh'),'Она взяла коробку поудобнее и направилась к хозяйственной постройке.':['$ cs_actor_exit(["sl"])','with cs_sprite_leave','label cs_check_day03_sl_left:'],'И в этот момент над лагерем раздался горн.':['stop music fadeout 2.0','play sound "sound/sfx/dinner_horn_processed.ogg"']},
 '82':{'Дарья посмотрела на мой локоть.':actor('da','worried'),'Она прищурилась.':actor('da','arms_crossed'),'Она рассмеялась.':actor('da','amused'),'Дарья улыбнулась.':actor('da','shy_smile'),'Когда Дарья вдруг спросила:':actor('da','thinking')},
 '82a':{'Дарья удивилась.':actor('da','neutral'),'Дарья улыбнулась.':actor('da','shy_smile')},
 '82b':{'Она улыбнулась.':actor('da','shy_smile')},
 '82c':{'Она улыбнулась мне.':actor('da','shy_smile')},
}

def emit(key,title,text,pre=(),post=()):
    blocks=parse(text);expected[key]=blocks
    lines=['# -*- coding: utf-8 -*-','label '+('cs_day02_74a' if key=='74a' else 'cs_day03_'+key)+':', '    $ save_name = '+json.dumps('Чужая смена — '+('День 2: Переговоры перед сном' if key=='74a' else 'День 3: '+title),ensure_ascii=False)]
    body=list(pre);last_pose=None
    for who,words in blocks:
        commands=events.get(key,{}).get(words,[])
        # Avoid redundant same-pose dissolves on repeated narrative phrases.
        if commands and commands[0].startswith('show '):
            if commands[0]==last_pose:commands=[]
            else:last_pose=commands[0]
        body.extend(commands)
        body.append(who+' '+json.dumps(words,ensure_ascii=False))
    body+=list(post)+['return']
    if key=='74a':body=[x.replace('cs_darya_normal_center','cs_darya_normal_right') for x in body]
    lines+=['    '+x for x in body]
    directory=R/('days/day02/part10' if key=='74a' else 'days/day03/part01');directory.mkdir(parents=True,exist_ok=True)
    path=directory/(key+'_scene.rpy');path.write_text('\n'.join(lines)+'\n',encoding='utf8')

emit('74a','Переговоры перед сном',sections['74А'][1],actor('da','thinking')+['$ cs_frame_focus(["cs_darya"])','label cs_check_day03_night_insert:'])
emit('75',sections['75'][0],sections['75'][1],scene('cs_house_lena_darya_int_day',True)+['$ cs_frame_focus([])','play ambience "sound/ambiences/forest_day.ogg" fadein 2.0','$ renpy.music.set_volume(0.16, channel="ambience")','play music "sound/music/my_daily_life.ogg" fadein 3.0','$ renpy.music.set_volume(0.2, channel="music")','label cs_check_day03_75:'])
emit('76',sections['76'][0],sections['76'][1],scene('cs_camp_path_day',True)+['$ cs_frame_focus([])','label cs_check_day03_76:'])
emit('77',sections['77'][0],sections['77'][1],actor('sl','smile')+['$ cs_frame_focus(["sl"])','label cs_check_day03_77:'])
s78=sections['78'][1]; high,low=s78.split('#### Если `cs_friend_sl == 0`');high=high.split('#### Если `cs_friend_sl >= 1`')[1]
emit('78a','Последствия вчерашней помощи',high,post=['if not cs_sl_poster_saved_day3:','    $ cs_sl_poster_saved_day3 = True','    $ cs_day03_poster_location = "slavya"'])
emit('78b','Вчерашнее объявление',low)
for key in ('79','80','81'):
    pre=frame('bg ext_clubs_day','sl','smile',True) if key=='80' else frame('cs_camp_path_day','sl','smile',True) if key=='81' else []
    emit(key,sections[key][0],sections[key][1],pre)
# Scene 82 was superseded by part 2. Keep only old named entry points.
for old,target in [('82','83'),('82a','85'),('82b','85'),('82c','86')]:
    (R/'days/day03/part01'/(old+'_scene.rpy')).write_text('# -*- coding: utf-8 -*-\n# Compatibility entry; the replacement manuscript is in part02.\nlabel cs_day03_'+old+':\n    jump cs_day03_'+target+'\n',encoding='utf8')
(R/'source/day03_part01_transcript.json').write_text(json.dumps(expected,ensure_ascii=False,indent=2),encoding='utf8')
print('Authored day-three blocks:',sum(map(len,expected.values())))
