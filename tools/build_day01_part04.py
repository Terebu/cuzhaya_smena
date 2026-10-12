"""Stage only supplied scenes 15-20, using semantic full-sprite names."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
source = (ROOT/'source/day01_part04.md').read_text(encoding='utf-8-sig')
body = source[source.index('### Сцена 15.'):source.index('## Инструкция Codex')]
parts = re.split(r'### Сцена (\d+)\. ([^\n]+)\n',body)[1:]
names = {15:'two_newcomers',16:'another_passenger',17:'beyond_the_screen',18:'anachronism',19:'dining_hall',20:'comrade_semen'}
manifest = []
def darya(pose='neutral',distance='normal'):
    return 'show cs_darya '+pose+' pioneer '+distance+' at '+('cs_dasha_far_right' if distance=='far' else 'cs_day_dasha_right')+' with dissolve'
def stage(n,s):
    if s.startswith('BG:'):
        if 'без смены' in s or '— сохранить' in s: return []
        bg = {15:'int_house_of_mt_day',17:'ext_house_of_mt_day',18:'ext_aidpost_day',19:'ext_dining_hall_near_day',20:'int_dining_hall_people_day'}[n]
        if n==15: return ['if not renpy.showing("bg int_house_of_mt_day"):', '    scene bg '+bg+' with dissolve']
        return ['scene bg '+bg+' with Dissolve(1.5)']+([darya()] if n==18 else [])
    if s.startswith('MUSIC:'):
        if 'продолж' in s: return []
        d = re.search(r'fade(?:in|out) (\d+(?:\.\d+)?)',s)
        duration = d.group(1) if d else '2.0'
        if 'fadeout' in s: return ['stop music fadeout '+duration]
        track = re.search(r'`([^`]+)`',s).group(1)
        name={'my_daily_life':'daily','just_think':'think','into_the_unknown':'unknown','a_promise_from_distant_days':'home','doubt_everyone':'doubt','everyday_theme':'everyday'}[track]
        return ['$ renpy.music.set_volume(%s, delay=1.0, channel="music")'%('0.3' if 'тихо' in s or 'негромко' in s else '0.5'), 'play music cs_day_music_'+name+' fadeout 1.5 fadein '+duration]
    if s.startswith('AMBIENCE:'):
        if 'сохранить' in s or 'продолжить' in s: return []
        vol = '0.25' if 'тихо' in s or 'приглушить' in s else '0.45'
        result = ['$ renpy.music.set_volume('+vol+', delay=1.0, channel="ambience")']
        if 'приглушить' in s: return result
        name='cs_day_dining_full' if 'dining_hall_full' in s else 'cs_day_cabin' if 'int_cabin_day' in s else 'cs_day_camp_center'
        return result+['if renpy.music.get_playing(channel="ambience") != '+name+':','    play ambience '+name+' fadeout 1.0 fadein 2.0']
    if s.startswith('PAUSE:'): return ['pause '+re.search(r'\d+(?:\.\d+)?',s).group(0)]
    if s.startswith('TRANSITION:') or s.startswith('КОНЕЦ'): return []
    if s.startswith('Постановка:'): return [] # Own Semyon is shown when he stands, via narrative hook.
    if s.startswith('SPRITES:'):
        if 'Алиса и Ульяна' in s: return ['hide dv with dissolve','hide us with dissolve','hide mt','hide cs_darya']
        if n==17: return [darya()]
        return ['hide mt','hide cs_dasha','hide cs_dasha_winter','hide cs_dasha_pioneer','show mt normal pioneer at left with dissolve',darya()]
    if s.startswith('SPRITE:'):
        if 'Дарья' in s:
            pose='thinking' if 'задумч' in s else 'smile' if 'улыб' in s else 'arms_crossed' if 'удивление' in s else 'neutral'
            return [darya(pose)]
        if 'Алиса' in s and 'Ульяна' in s: return ['show dv normal pioneer far at cs_day_sl_left with dissolve','show us smile pioneer far at cs_day_mt_center with dissolve']
        if 'Алиса' in s: return ['hide mt',darya('neutral','far'),'show dv normal pioneer far at cs_day_sl_left with dissolve']
        if 'Ульяна' in s: return ['show us smile pioneer far at cs_day_mt_center with dissolve']
    raise ValueError(s)
checks={'Ольга Дмитриевна ещё раз окинула нас взглядом.':'housing','Семён.':'passenger','Я медленно опустила взгляд.':'silence','На улице оказалось ещё жарче.':'outside','Мы приблизились к медпункту.':'aidpost','…может находиться изображение события из будущего?':'hypothesis',
        'Немного дальше прошла Славя.':'cameo','Мне пришлось приложить некоторое усилие, чтобы не улыбнуться.':'semen','Ты случайно не на четыреста десятом сюда приехал?':'bus_question','Откуда ты…':'reaction','…у нас с тобой есть о чём поговорить.':'final'}
for k in range(0,len(parts),3):
    n,title,text = int(parts[k]),parts[k+1].strip(),parts[k+2]
    lines=['# -*- coding: utf-8 -*-','# Source: source/day01_part04.md.','label cs_day01_%02d:'%n,'    $ save_name = u'+json.dumps('Чужая смена — День 1: '+title,ensure_ascii=False)]
    if n==15: lines += ['    hide screen cs_day01_pending','    hide screen cs_phone','    $ day_time()','    $ persistent.sprite_time = "day"','    window show dissolve']
    for p in re.split(r'\n\s*\n',text.strip()):
        p=p.strip()
        if not p or p=='---': continue
        if p.startswith('**['): lines += ['    '+c for c in stage(n,p[3:-3])]; continue
        m=re.match(r'\*\*(Лена|Дарья|Славя|Ольга Дмитриевна|Семён)(?: \([^)]*\))?:\*\*\\?\s*\n—\s*(.*)',p,re.S)
        if m: who,value={'Лена':'cs_ls','Дарья':'cs_da','Славя':'cs_sl','Ольга Дмитриевна':'cs_mt','Семён':'cs_sy'}[m.group(1)],m.group(2).strip()
        elif p.startswith('*') and not p.startswith('**'):
            who,value='cs_th',p[1:-1]
        else: who,value='cs_narrator',p
        if n==17 and value=='Мы прошли мимо нескольких домиков.': lines += ['    show bg ext_houses_day with Dissolve(1.5)']
        if n==17 and value=='Я на мгновение замедлила шаг.': lines += ['    show cs_camp_path_day with Dissolve(1.5)']
        if n==20 and value=='Парень медленно поднялся.': lines += ['    hide cs_darya','    show cs_darya thinking pioneer far at cs_dasha_far_right with dissolve','    show mt normal pioneer far at cs_day_sl_left with dissolve','    show cs_semen neutral pioneer far at cs_semen_far_center with dissolve']
        if n==20 and value=='Ольга Дмитриевна помахала ему рукой.': lines += ['    show mt normal pioneer at left with dissolve']
        if n==20 and value=='Он слегка напрягся.': lines += ['    show cs_semen thinking pioneer far at cs_semen_far_center with dissolve']
        if n==20 and value=='Его лицо изменилось мгновенно.': lines += ['    show cs_semen surprised pioneer far at cs_semen_far_center with dissolve']
        if value in checks and (value!='Семён.' or n==16 and who=='cs_mt'): lines += ['    label cs_check_day01_part04_'+checks[value]+':']
        value=re.sub(r'\*\*(.*?)\*\*',r'{b}\1{/b}',value)
        lines += ['    '+who+' '+json.dumps(value,ensure_ascii=False)]
        manifest.append({'scene':n,'speaker':who,'text':value})
    lines += ['    return']
    (ROOT/'days/day01'/('%02d_%s.rpy'%(n,names[n]))).write_text('\n'.join(lines)+'\n',encoding='utf8')
(ROOT/'qa/day01_part04_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 4:',len(manifest),'blocks; six scenes.')
