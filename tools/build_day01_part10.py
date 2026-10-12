"""Build the supplied library chapter with independent friendship and continuity."""
import json,re,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'days/day01/part10';OUT.mkdir(exist_ok=True)
folder=ROOT/'bg/lib';catalog=[]
for old,time in [('Изображение ChatGPT 12 окт. 2026 г., 01_03_53-1.png','sunset'),('Изображение ChatGPT 12 окт. 2026 г., 01_03_54-2.png','night')]:
    dest=folder/('library_exterior_'+time+'.png')
    if (folder/old).exists():(folder/old).rename(dest)
    catalog.append({'original':old,'renamed':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(folder/'background_catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
source=(ROOT/'source/day01_part10.md').read_text(encoding='utf8').split('## Реализация развилки')[0]
sections=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)',source)
speakers={'Лена':'cs_ls','Лена Соколова':'cs_ls','Дарья':'cs_da','Женя':'cs_mz','Лена Тихонова':'cs_un'}
names={'52':'after_dinner','53':'library_walk','54':'librarian','55':'choice','55А':'help','55Б':'search_alone','56':'old_books','57':'slip_of_tongue','58':'truth'}
scenes=[]
for i in range(1,len(sections),3):
    number=sections[i];blocks=[];condition=False
    for p in re.split(r'\n\s*\n',sections[i+2]):
        p=p.strip()
        if not p or p=='---' or p.startswith('#') or p.startswith('- ') or p.startswith('**Вариант'):continue
        if p.startswith('**['):
            stage=p[3:p.rfind(']')];blocks.append({'stage':stage})
            if stage.startswith('УСЛОВНАЯ ВСТАВКА'):condition=True
            if stage.startswith('КОНЕЦ УСЛОВНОЙ'):condition=False
            continue
        m=re.match(r'\*\*([^\n]+):\*\*\\?\s*\n—\s*(.*)',p,re.S)
        if m:
            name=re.sub(r' \([^)]*\)$','',m[1]);block={'who':speakers[name],'text':m[2].strip()}
        elif p.startswith('*'):block={'who':'cs_th','text':p.strip('*')}
        else:block={'who':'cs_narrator','text':re.sub(r'\s*\\\s*$','',p)}
        if condition:block['condition']='friend_un'
        blocks.append(block)
    scenes.append({'number':number,'title':sections[i+1],'blocks':blocks})
def d(p='shrug'):return 'show cs_darya '+p+' pioneer normal at cs_darya_normal_center'
def mz(p='normal'):return 'show mz '+p+' glasses pioneer at left zorder 10'
for s in scenes:
    n=s['number'];slug=n.replace('А','_a').replace('Б','_b')
    lines=['# -*- coding: utf-8 -*-','label cs_day01_'+slug+':','$ save_name = '+json.dumps('Чужая смена — День 1: '+s['title'],ensure_ascii=False)]
    indent='';first_bg=True;mz_pose=None;conditional=False;un_pose='normal';authored=[]
    if n in ('55А','55Б'):lines+=[mz(),d()]
    if n=='55':lines+=['label cs_check_day01_part10_choice_text:']
    for b in s['blocks']:
        if 'stage' in b:
            c=b['stage']
            if c.startswith('УСЛОВНАЯ ВСТАВКА'):
                lines+=['if cs_met_un and cs_friend_un > 0:','    $ cs_un_name_known = True','    show un smile pioneer at left zorder 10','    '+d(),'    label cs_check_day01_part10_un_friend:'];indent='    ';conditional=True
            elif c.startswith('КОНЕЦ УСЛОВНОЙ'):
                lines+=['    hide un','elif cs_met_un:','    show un normal pioneer at left zorder 10','    label cs_check_day01_part10_un_neutral:','    cs_un "Добрый вечер."','    cs_ls "Добрый вечер, Лена. Мы ненадолго в библиотеку."','    cs_un "Женя скоро закрывает. Лучше поторопитесь."','    hide un']
                authored += [{'who':'cs_un','text':'Добрый вечер.'},{'who':'cs_ls','text':'Добрый вечер, Лена. Мы ненадолго в библиотеку.'},{'who':'cs_un','text':'Женя скоро закрывает. Лучше поторопитесь.'}]
                indent='';conditional=False
            elif c.startswith('BG:'):
                if n=='52' and first_bg:lines+=['$ sunset_time()','$ persistent.sprite_time = "sunset"','scene bg int_dining_hall_sunset',d(),'with Dissolve(1.0)','label cs_check_day01_part10_start:']
                elif n=='53' and first_bg:lines+=['scene bg ext_dining_hall_near_sunset',d(),'with Dissolve(1.0)']
                elif n=='54' and first_bg:lines+=['scene bg int_library_day',mz(),d(),'with Dissolve(1.0)','label cs_check_day01_part10_library:']
                first_bg=False
            elif c.startswith('AMBIENCE:'):
                track='dining_hall_full' if 'dining_hall' in c else 'library_day' if 'library_day' in c else 'camp_center_evening'
                lines+=['$ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")','if renpy.music.get_playing(channel="ambience") != "sound/ambiences/'+track+'.ogg":','    play ambience "sound/ambiences/'+track+'.ogg" fadeout 1.5 fadein 1.5']
            elif c.startswith('MUSIC:'):
                if 'fadeout' in c:lines+=['stop music fadeout 2.0']
                elif 'продолж' not in c:
                    track=c.split('`')[1];audio='cs_day_music_doubt' if track=='doubt_everyone' else '"sound/music/'+track+'.ogg"'
                    lines+=['$ renpy.music.set_volume(0.23,delay=1.0,channel="music")','play music '+audio+' fadeout 2.0 fadein 2.5']
            elif c.startswith('SFX:'):lines+=['play sound cs_day_sfx_door']
            continue
        text=b['text'];who=b['who'];authored.append(b)
        if n=='53' and text=='Мы свернули к библиотеке.':lines+=['scene cs_library_exterior_sunset',d(),'with Dissolve(1.2)','label cs_check_day01_part10_exterior:']
        if who=='cs_un':
            pose='shy' if any(w in text for w in ('Только','Увидимся')) else 'smile'
            lines += [indent+'show un '+pose+' pioneer at left zorder 10']
        if who=='cs_mz':
            pose='angry' if any(w in text for w in ('издеваешься','потише','без шума','не верю','Лена…')) else 'smile' if any(w in text for w in ('Спасибо','спасибо','Вот именно','Нормально')) else 'normal'
            if pose!=mz_pose:lines+=[mz(pose)];mz_pose=pose
            if text=='Я Женя. За библиотеку отвечаю. Если хотите что-нибудь взять, сначала запишу вас.':lines+=['$ cs_met_mz = True']
        if n=='53' and text=='Она направилась по дорожке с книгой под мышкой.':lines+=['    hide un']
        lines += [indent+who+' '+json.dumps(text,ensure_ascii=False)]
    if n=='55':lines+=['label cs_check_day01_part10_choice:','if cs_part10_choice is None:','    menu:','        "Предложить Жене помощь с книгами":','            $ cs_friend_mz += 1','            $ cs_part10_choice = "help"','        "Не отвлекать Женю от работы":','            $ cs_part10_choice = "search"','if cs_part10_choice == "help":','    call cs_day01_55_a','else:','    call cs_day01_55_b']
    if n=='56':lines.insert(3,'label cs_check_day01_part10_join:')
    lines+=['return'];s['blocks']=authored
    (OUT/(slug+'_'+names[n]+'.rpy')).write_text('\n'.join(l if l.startswith('#') or l.startswith('label cs_day01') else '    '+l for l in lines)+'\n',encoding='utf8')
(ROOT/'source/day01_part10_dialogue.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Built library chapter, conditional Lena event and both Zhenya choices.')
