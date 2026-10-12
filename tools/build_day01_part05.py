"""Build the author-approved new part 5 from its human-readable manuscript."""
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'days/day01/part05'; OUT.mkdir(exist_ok=True)
source=(ROOT/'source/day01_part05.md').read_text(encoding='utf8')
NAMES={21:'not_a_simple_question',22:'similar_journey',23:'familiar_story',24:'working_group'}
WHO={'Лена':'cs_ls','Дарья':'cs_da','Семён':'cs_sy','Ольга Дмитриевна':'cs_mt'}
manifest=[]
for n,title,body in re.findall(r'### Сцена (\d+)\. ([^\n]+)\n(.*?)(?=### Сцена |\Z)',source,re.S):
    n=int(n);blocks=[]
    for par in re.split(r'\n\s*\n',body):
        par=par.strip()
        if not par:continue
        m=re.match(r'\*\*(.+?):\*\*\s*\n—\s*(.*)',par,re.S)
        if m:who,text=WHO[m[1]],m[2]
        elif par.startswith('*'):who,text='cs_th',par.strip('*')
        else:who,text='cs_narrator',par
        blocks.append({'who':who,'text':text})
    lines=['# -*- coding: utf-8 -*-','# Source: source/day01_part05.md.','label cs_day01_'+str(n)+':','    $ save_name = '+json.dumps('Чужая смена — День 1: '+title,ensure_ascii=False)]
    if n==21:lines+=['    window show dissolve','    label cs_check_day01_part05_start:']
    if n==22:lines+=['    $ renpy.music.set_volume(0.35,delay=1.0,channel="music")','    play music cs_day_music_home fadeout 1.5 fadein 2.5','    label cs_check_day01_part05_journey:']
    if n==23:lines+=['    $ renpy.music.set_volume(0.3,delay=1.0,channel="music")','    play music cs_day_music_think fadeout 2.0 fadein 2.5','    label cs_check_day01_part05_story:']
    if n==24:lines+=['    stop music fadeout 2.0','    label cs_check_day01_part05_home:']
    far=n==21; sy=None;da=None
    for b in blocks:
        who,text=b['who'],b['text']
        if text=='Она направилась к столу у окна.':
            lines+=['    hide mt with Dissolve(0.6)','    show cs_semen tie_touch pioneer far at cs_semen_far_left with MoveTransition(0.7)'];sy='tie_touch'
        if text=='Он — напротив.':
            lines+=['    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left','    show cs_darya forearm_hold pioneer normal at cs_day_dasha_right','    with Dissolve(0.8)'];far=False;sy='thinking_alt';da='forearm_hold'
        if who=='cs_sy':
            pose='serious' if n==23 or 'Ты серьёзно' in text else 'thinking_alt' if '?' in text else 'awkward_alt' if 'не помню' in text or 'другой год' in text else 'tie_touch'
            if text in ('Вместе.','Звучит разумно.','Если что-нибудь узнаю, скажу вам.'):pose='grateful'
            if pose!=sy:lines+=['    show cs_semen '+pose+' pioneer '+('far at cs_semen_far_center' if far and sy is None else 'far at cs_semen_far_left' if far else 'normal at cs_semen_normal_left')+' with Dissolve(0.4)'];sy=pose
        if who=='cs_da':
            pose='thinking' if '?' in text else 'worried' if 'объяснить' in text or text=='Мы тоже.' else 'forearm_hold' if n==23 else 'explaining' if len(text)>70 else 'neutral'
            if text in ('Договорились.','Спасибо.'):pose='smile'
            if pose!=da:lines+=['    show cs_darya '+pose+' pioneer '+('far at cs_dasha_far_right' if far else 'normal at cs_day_dasha_right')+' with Dissolve(0.4)'];da=pose
        if text=='Две тысячи двадцать шестой.':lines+=['    stop music fadeout 1.5','    label cs_check_day01_part05_2026:']
        if text=='У меня дома есть визуальная новелла. Компьютерная игра, в которой читают историю и иногда выбирают ответы.':lines+=['    label cs_check_day01_part05_novel:']
        if text=='Рядом со столом остановилась Ольга Дмитриевна.':
            lines+=['    show cs_semen serious pioneer far at cs_semen_far_center','    show cs_darya thinking pioneer far at cs_dasha_far_right','    show mt normal pioneer far at cs_day_sl_left','    with Dissolve(0.7)','    label cs_check_day01_part05_olga:'];far=True;sy='serious';da='thinking'
        if who=='cs_mt':
            pose='smile' if text=='Ну что, познакомились?' else 'normal'
            lines+=['    show mt '+pose+' pioneer far at cs_day_sl_left with Dissolve(0.35)']
        if text=='Она ещё раз оглядела стол и пошла дальше.':
            lines+=['    hide mt with Dissolve(0.5)','    show cs_semen tie_touch pioneer far at cs_semen_far_left with MoveTransition(0.7)'];sy='tie_touch'
        if text=='Значит, ищем ответы вместе. Без обещаний, что завтра всё выяснится.':
            lines+=['    $ renpy.music.set_volume(0.35,delay=1.0,channel="music")','    play music cs_day_music_home fadeout 2.0 fadein 2.5','    label cs_check_day01_part05_agreement:']
        if text=='Дарья усмехнулась.':lines+=['    show cs_darya amused pioneer far at cs_dasha_far_right with Dissolve(0.4)'];da='amused'
        lines+=['    '+who+' '+json.dumps(text,ensure_ascii=False)]
    lines+=['    return']
    (OUT/(str(n)+'_'+NAMES[n]+'.rpy')).write_text('\n'.join(lines)+'\n',encoding='utf8')
    manifest.append({'number':n,'title':title,'blocks':blocks})
(ROOT/'source/day01_part05_dialogue.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Built scenes 21-24,',sum(len(s['blocks']) for s in manifest),'text blocks.')
