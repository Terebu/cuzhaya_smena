"""Build the supplied sunset chapter as six independent Ren'Py scenes."""
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'days/day01/part08'
OUT.mkdir(exist_ok=True)
source=(ROOT/'source/day01_part08.md').read_text(encoding='utf8').split('## Инструкция для Codex')[0]
sections=re.split(r'### Сцена (\d+)\. ([^\n]+)',source)
speakers={'Лена':'cs_ls','Дарья':'cs_da','Семён':'cs_sy'}
names=['after_clubs','confession','why_you','square','independent_opinion','for_now']
scenes=[]
def d(p='shrug'):return 'show cs_darya '+p+' pioneer normal at cs_day_dasha_right with Dissolve(0.5)'
for i in range(1,len(sections),3):
    number=int(sections[i]);blocks=[]
    for p in re.split(r'\n\s*\n',sections[i+2]):
        p=p.strip()
        if not p or p=='---' or p.startswith('#'):continue
        if p.startswith('**['):blocks.append({'stage':p[3:p.rfind(']')]});continue
        m=re.match(r'\*\*(Лена|Дарья|Семён):\*\*\\?\s*\n—\s*(.*)',p,re.S)
        if m:blocks.append({'who':speakers[m[1]],'text':m[2].strip()})
        elif p.startswith('*'):blocks.append({'who':'cs_th','text':p.strip('*')})
        else:blocks.append({'who':'cs_narrator','text':p})
    scenes.append({'number':number,'title':sections[i+1],'blocks':blocks})
(ROOT/'source/day01_part08_dialogue.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for s in scenes:
    n=s['number'];lines=['# -*- coding: utf-8 -*-','label cs_day01_'+str(n)+':','$ save_name = '+json.dumps('Чужая смена — День 1: '+s['title'],ensure_ascii=False)]
    if n==40:lines+=['label cs_check_day01_part08_start:']
    if n==41:lines+=['label cs_check_day01_part08_private:']
    if n==44:lines+=['label cs_check_day01_part08_opinion:']
    sy=False;sy_pose=None
    for b in s['blocks']:
        if 'stage' in b:
            c=b['stage']
            if c.startswith('BG:') and 'dissolve' in c:
                name=c.split('`')[1]
                name='cs_camp_path_sunset' if name=='ext_path_sunset' else 'bg '+name
                if n==40:lines+=['$ sunset_time()','$ persistent.sprite_time = "sunset"']
                lines+=['scene '+name,d().replace(' with Dissolve(0.5)',''),'with Dissolve(1.5)']
                if n==43:lines+=['label cs_check_day01_part08_square:']
                if n==45:lines+=['label cs_check_day01_part08_walk:']
            elif c.startswith('MUSIC:') and 'продолж' not in c:
                if 'fadeout' in c:lines+=['stop music fadeout '+('3.0' if '3.0' in c else '2.0')]
                else:
                    track=c.split('`')[1]
                    lines+=['$ renpy.music.set_volume(0.28,delay=1.0,channel="music")','play music "sound/music/'+track+'.ogg" fadeout 2.0 fadein 3.0']
            elif c.startswith('AMBIENCE:'):
                track='camp_center_day' if 'camp_center_day' in c else 'camp_center_evening'
                lines+=['$ renpy.music.set_volume('+('0.35' if n==45 else '0.22')+',delay=1.5,channel="ambience")','if renpy.music.get_playing(channel="ambience") != "sound/ambiences/'+track+'.ogg":','    play ambience "sound/ambiences/'+track+'.ogg" fadeout 2.0 fadein 2.0']
                if n==42:lines+=['label cs_check_day01_part08_silence:']
            elif c.startswith('PAUSE:'):lines+=['pause '+c.split(':')[1].strip()]
            elif c.startswith('SPRITE:') and n in (40,41):lines+=[d()]
            continue
        text=b['text'];who=b['who']
        if n==43 and text=='Мы подошли к скамейке.':
            lines+=['show cs_semen thinking_down pioneer normal at cs_semen_normal_left with Dissolve(0.6)','label cs_check_day01_part08_semen:'];sy=True
        if n in (43,44,45) and who=='cs_sy':
            pose='thinking_alt' if '?' in text else 'smile' if any(w in text for w in ('забавные','стоите','Увидимся')) else 'awkward_alt' if 'не это' in text else 'relaxed'
            if pose!=sy_pose:lines+=['show cs_semen '+pose+' pioneer normal at cs_semen_normal_left with Dissolve(0.5)'];sy_pose=pose
        if n==41 and text=='В общем… Кажется, ты мне нравишься.':lines+=['label cs_check_day01_part08_confession:']
        if n==41 and text=='Дарья остановилась совершенно неподвижно.':lines+=[d('surprise_hand')]
        if n==42 and text=='Но насчёт всего остального я пока не знаю.':lines+=['label cs_check_day01_part08_boundaries:']
        if n==45 and text=='Он пошёл в сторону домиков.':lines+=['hide cs_semen with Dissolve(0.6)','label cs_check_day01_part08_semen_leaves:']
        if n==45 and text=='Я мягко приобняла её за плечи.':lines+=['label cs_check_day01_part08_hug:']
        if text in ('Пауза.','Небольшая пауза.'):lines+=['pause 0.7']
        lines += [who+' '+json.dumps(text,ensure_ascii=False)]
    lines+=['return']
    (OUT/(str(n)+'_'+names[n-40]+'.rpy')).write_text('\n'.join(l if l.startswith('#') or l.startswith('label cs_day01') else '    '+l for l in lines)+'\n',encoding='utf8')
print('Built scenes 40-45.')
