"""Compile the supplied two-branch chapter without including editorial instructions."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'days/day01/part09';OUT.mkdir(exist_ok=True)
source=(ROOT/'source/day01_part09.md').read_text(encoding='utf8').split('## Реализация развилки')[0]
sections=re.split(r'### Сцена (\d+[АБ]?)\. ([^\n]+)',source)
speakers={'Лена':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Семён (за кадром)':'cs_sy','Неизвестная девушка':'cs_un','Лена Тихонова':'cs_un'}
names={'46':'resemblance','47':'choice','48А':'meet','48Б':'pass','49':'together','50':'no_saves','51':'dinner_time'}
scenes=[]
def d(p='shrug',distance='normal'):
    return 'show cs_darya '+p+' pioneer '+distance+' at cs_darya_'+distance+'_center with Dissolve(0.5)'
for i in range(1,len(sections),3):
    number=sections[i];blocks=[]
    for p in re.split(r'\n\s*\n',sections[i+2]):
        p=p.strip()
        if not p or p=='---' or p.startswith('#') or p.startswith('- ') or p.startswith('**Вариант'):continue
        if p.startswith('**['):blocks.append({'stage':p[3:p.rfind(']')]});continue
        m=re.match(r'\*\*([^\n]+):\*\*\\?\s*\n—\s*(.*)',p,re.S)
        if m:blocks.append({'who':speakers[m[1]],'text':m[2].strip()})
        elif p.startswith('*'):blocks.append({'who':'cs_th','text':p.strip('*')})
        else:blocks.append({'who':'cs_narrator','text':p})
    scenes.append({'number':number,'title':sections[i+1],'blocks':blocks})
(ROOT/'source/day01_part09_dialogue.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for s in scenes:
    n=s['number'];slug=n.replace('А','_a').replace('Б','_b')
    lines=['# -*- coding: utf-8 -*-','label cs_day01_'+slug+':','$ save_name = '+json.dumps('Чужая смена — День 1: '+s['title'],ensure_ascii=False)]
    if n=='46':lines+=['$ sunset_time()','$ persistent.sprite_time = "sunset"','scene cs_camp_path_sunset',d().replace(' with Dissolve(0.5)',''),'with Dissolve(0.7)']
    if n=='47':lines+=['show un normal pioneer at left',d()]
    if n in ('48А','48Б'):lines+=['show un normal pioneer at left',d()]
    un_pose='normal';sy_pose=None;three=False
    for b in s['blocks']:
        if 'stage' in b:
            c=b['stage']
            if c.startswith('BG:') and 'dissolve' in c:
                bg=c.split('`')[1];bg='cs_camp_path_sunset' if bg=='ext_path_sunset' else 'bg '+bg
                lines+=['scene '+bg,d().replace(' with Dissolve(0.5)',''),'with Dissolve(1.5)']
                if n=='49':lines+=['label cs_check_day01_part09_merge:']
            elif c.startswith('MUSIC:'):
                if 'fadeout' in c or 'затихнуть' in c:
                    if 'продолжить' not in c:lines+=['stop music fadeout 2.5']
                elif 'без музыки' in c:lines+=['stop music fadeout 2.0']
                elif 'приглушить' in c:lines+=['$ renpy.music.set_volume(0.14,delay=2.0,channel="music")']
                else:
                    track=c.split('`')[1];audio='cs_day_music_everyday' if track=='everyday_theme' else '"sound/music/'+track+'.ogg"'
                    lines+=['$ renpy.music.set_volume(0.24,delay=1.0,channel="music")','play music '+audio+' fadeout 2.0 fadein 2.5']
            elif c.startswith('AMBIENCE:'):lines+=['$ renpy.music.set_volume(0.35,delay=1.5,channel="ambience")','if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":','    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0']
            elif c.startswith('PAUSE:'):lines+=['pause '+c.split(':')[1].strip()]
            elif c.startswith('SFX:') and 'sfx_dinner' in c:lines+=['play sound "sound/sfx/dinner_jingle_speaker.ogg"']
            elif c.startswith('SPRITE:') and 'un normal' in c and n=='46':lines+=['show un normal pioneer at left with Dissolve(0.7)']
            elif c.startswith('SPRITE:') and 'un shy' in c:lines+=['show un shy pioneer at left with Dissolve(0.5)'];un_pose='shy'
            elif c.startswith('SPRITE:') and 'un smile' in c and 'hide' not in c:lines+=['show un smile pioneer at left with Dissolve(0.5)'];un_pose='smile'
            elif c.startswith('SPRITE:') and 'Семёна' in c:
                lines+=['show un smile pioneer far at left',d(distance='far').replace(' with Dissolve(0.5)',''),'show cs_semen awkward pioneer far at cs_semen_far_right','with Dissolve(0.7)','label cs_check_day01_part09_trio:'];three=True
            elif c.startswith('SPRITE:') and 'hide' in c:lines+=['hide un with Dissolve(0.7)']
            continue
        text=b['text'];who=b['who']
        if n=='48А' and who=='cs_un' and text=='Увидимся, Лена.':lines+=['label cs_check_day01_un_farewell:']
        if who=='cs_un' and n=='48А':
            if text=='Да…':lines+=['$ cs_un_name_known = True']
            pose='shy' if any(w in text for w in ('Может','Наверное','Да…')) else 'smile' if any(w in text for w in ('Хорошо','Приятно','похожи','Увидимся')) else 'normal'
            if pose!=un_pose:lines+=['show un '+pose+' pioneer'+(' far' if three else '')+' at left with Dissolve(0.5)'];un_pose=pose
        if who=='cs_sy' and text!='Лена!':
            pose='surprised' if '?' in text or 'Э-э' in text else 'smile' if any(w in text for w in ('Увидимся','Разбер','Ладно')) else 'awkward_alt'
            if pose!=sy_pose:lines+=['show cs_semen '+pose+' pioneer far at cs_semen_far_right with Dissolve(0.5)'];sy_pose=pose
        if text=='Он продолжил путь по своим делам.':lines+=['hide cs_semen', 'show un smile pioneer at left',d().replace(' with Dissolve(0.5)',''),'with Dissolve(0.7)'];three=False
        if text=='Девушка направилась дальше, в сторону библиотеки.':lines+=['hide un with Dissolve(0.7)']
        if n=='50' and text=='И никаких сохранений.':lines+=['label cs_check_day01_part09_introspection:']
        if n=='50' and who=='cs_da' and text=='Ты опять задумалась?':lines+=['label cs_check_day01_part09_returns:']
        lines += [who+' '+json.dumps(text,ensure_ascii=False)]
    if n=='47':lines+=['label cs_check_day01_part09_choice:','if cs_part09_choice is None:','    menu:','        "Остановиться и познакомиться":','            $ cs_friend_un += 1','            $ cs_met_un = True','            $ cs_part09_choice = "meet"','        "Извиниться и пройти дальше":','            $ cs_part09_choice = "pass"','if cs_part09_choice == "meet":','    call cs_day01_48_a','else:','    call cs_day01_48_b']
    lines+=['return']
    (OUT/(slug+'_'+names[n]+'.rpy')).write_text('\n'.join(l if l.startswith('#') or l.startswith('label cs_day01') else '    '+l for l in lines)+'\n',encoding='utf8')
print('Built part 9, both friendship branches.')
