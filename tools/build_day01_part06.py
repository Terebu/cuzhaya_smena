"""Build the six supplied scenes; keep dramatic cues local to each scene."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT/'days/day01/part06'
OUT.mkdir(exist_ok=True)
scenes = json.loads((ROOT/'source/day01_part06_dialogue.json').read_text(encoding='utf8'))
names = {25:'after_lunch',26:'new_home_path',27:'house_for_two',28:'without_witnesses',29:'observation_log',30:'at_the_door'}
def show_d(pose='neutral', far=False):
    return 'show cs_darya '+pose+' pioneer '+('far at cs_dasha_far_right' if far else 'normal at cs_day_dasha_right')+' with Dissolve(0.4)'
for scene in scenes:
    n=scene['number']; lines=['# -*- coding: utf-8 -*-','# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.','label cs_day01_'+str(n)+':','    $ save_name = '+json.dumps('Чужая смена — День 1: '+scene['title'],ensure_ascii=False)]
    if n==25:
        lines += ['    hide mt with dissolve','    hide sl','    show cs_semen thinking_alt pioneer far at cs_semen_far_left with Dissolve(0.6)','    '+show_d('tie_touch',True),'    label cs_check_day01_part06_lunch:']
    if n==26:
        lines += ['    scene bg ext_dining_hall_near_day','    show sl smile pioneer at left','    '+show_d().replace(' with Dissolve(0.4)',''),'    with Dissolve(1.3)']
    if n==27:
        lines += ['    scene cs_house_lena_darya_ext_day','    show sl smile pioneer at left','    '+show_d().replace(' with Dissolve(0.4)',''),'    with Dissolve(1.3)','    label cs_check_day01_part06_house_ext:']
    if n==28:lines += ['    label cs_check_day01_part06_private:']
    if n==29:lines += ['    label cs_check_day01_part06_notes:']
    if n==30:lines += ['    label cs_check_day01_part06_visitors:']
    dpose='tie_touch' if n==25 else 'neutral'; sy_pose='thinking_alt'; sl_pose='smile'
    for b in scene['blocks']:
        if 'stage' in b:
            cue=b['stage']
            if cue.startswith('MUSIC:'):
                if 'продолж' in cue:continue
                if 'fadeout' in cue:lines += ['    stop music fadeout '+('2.5' if '2.5' in cue else '2.0')]
                elif '`' in cue:
                    alias='think' if 'just_think' in cue else 'play' if 'i_want_to_play' in cue else 'daily'
                    lines += ['    $ renpy.music.set_volume('+('0.3' if alias=='think' else '0.45')+',delay=1.0,channel="music")','    play music cs_day_music_'+alias+' fadeout 2.0 fadein '+('3.0' if alias=='think' else '2.0')]
            elif cue.startswith('AMBIENCE:'):
                alias='dining_full' if n==25 else 'cabin' if n>=28 or n==27 and 'интерьер' in cue else 'camp_center'
                lines += ['    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")','    if renpy.music.get_playing(channel="ambience") != cs_day_'+alias+':','        play ambience cs_day_'+alias+' fadeout 1.5 fadein 2.0']
            elif cue.startswith('SPRITE: Славя') and 'hide' in cue:lines += ['    hide sl with Dissolve(0.5)']
            elif cue.startswith('SPRITE: Славя'):
                lines += ['    show sl smile pioneer far at cs_day_mt_center with Dissolve(0.5)'];sl_pose='smile'
            elif cue.startswith('BG: пользовательский BG интерьера'):
                lines += ['    scene cs_house_lena_darya_int_day','    show sl normal pioneer at left','    '+show_d().replace(' with Dissolve(0.4)',''),'    with Dissolve(1.4)','    label cs_check_day01_part06_house_int:'];sl_pose='normal';dpose='neutral'
            elif cue.startswith('SFX:'):
                alias='bed' if 'bed' in cue else 'knock' if 'стука' in cue else 'door'
                lines += ['    $ renpy.music.set_volume(0.45,channel="sound")','    play sound cs_day_sfx_'+alias]
                if alias=='knock':lines += ['    label cs_check_day01_part06_knock:']
            elif cue.startswith('PAUSE:'):lines += ['    pause '+cue.split(':',1)[1].strip()]
            continue
        who,text=b['who'],b['text']; far=n==25
        if n==26 and text=='Мы свернули на дорожку между домиками.':
            lines += ['    scene cs_camp_path_day','    show sl smile pioneer at left','    '+show_d(dpose).replace(' with Dissolve(0.4)',''),'    with Dissolve(1.4)']
        if who=='cs_da':
            pose='thinking' if '?' in text else 'forearm_hold' if n==28 else 'explaining' if len(text)>90 else 'neutral'
            if text in ('Я тоже.','Лен.'):pose='worried' if n==28 else 'serious'
            if text in ('Правильно.','Логично.','Спасибо тебе.'):pose='smile'
            if text in ('Очень амбициозно.','Временная.'):pose='amused'
            if pose!=dpose:lines+=['    '+show_d(pose,far)];dpose=pose
        if who=='cs_sy':
            pose='thinking_alt' if '?' in text else 'awkward_alt' if text in ('Точно.','Начинается…') else 'serious' if text in ('Ладно.',) else 'smile'
            if pose!=sy_pose:lines+=['    show cs_semen '+pose+' pioneer far at cs_semen_far_left with Dissolve(0.4)'];sy_pose=pose
        if who=='cs_sl':
            pose='surprise' if text in ('Какие платежи?','А где?') else 'normal' if 'Помнишь?' in text else 'smile'
            if pose!=sl_pose:lines+=['    show sl '+pose+' pioneer '+('far at cs_day_mt_center' if far else 'at left')+' with Dissolve(0.4)'];sl_pose=pose
        if who=='cs_narrator' and ('Дарья' in text and any(w in text for w in ('улыб','рассме','сдержив'))):
            pose='amused' if 'рассме' in text else 'smile'
            if pose!=dpose:lines+=['    '+show_d(pose,far)];dpose=pose
        if text=='Славя не удержалась от смеха.':lines+=['    show sl laugh pioneer at left with Dissolve(0.4)'];sl_pose='laugh'
        if text=='Я подняла карандаш.':lines+=['    '+show_d('thinking')];dpose='thinking'
        if text=='Да, Даш.':lines+=['    label cs_check_day01_part06_fear:']
        if text=='Я открыла дверь.':lines+=['    play sound cs_day_sfx_door','    label cs_check_day01_part06_open_door:']
        lines += ['    '+who+' '+json.dumps(text,ensure_ascii=False)]
    lines += ['    return']
    (OUT/(str(n)+'_'+names[n]+'.rpy')).write_text('\n'.join(lines)+'\n',encoding='utf8')
print('Built scenes 25-30; no ending of day 1.')
