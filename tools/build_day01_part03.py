"""Compile supplied part 3 only. Stage directions never become dialogue."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
source = (ROOT/'source/day01_part03.md').read_text(encoding='utf-8-sig')
body = source[source.index('### Сцена 10.'):source.index('## Техническое задание')]
parts = re.split(r'### Сцена (\d+)\. ([^\n]+)\n', body)[1:]
names = {10:'soviet_home',11:'state_machine',12:'calculator',13:'uniform',14:'third_guest'}
manifest = []
def stage(n,s):
    if s.startswith('BG:'): return []
    if s.startswith('MUSIC:'):
        if 'продолжить без' in s or 'продолжить, если' in s: return []
        d = re.search(r'fade(?:in|out) (\d+(?:\.\d+)?)',s)
        duration = d.group(1) if d else '2.0'
        if 'fadeout' in s: return ['stop music fadeout '+duration]
        track = re.search(r'`([^`]+)`',s).group(1)
        name = {'just_think':'think','i_want_to_play':'play','doubt_everyone':'doubt','my_daily_life':'daily','into_the_unknown':'unknown','everyday_theme':'everyday'}[track]
        commands = ['$ renpy.music.set_volume(%s, delay=1.0, channel="music")'%('0.3' if 'тихо' in s else '0.5'), 'play music cs_day_music_'+name+' fadeout 1.5 fadein '+duration]
        if 'если композиция' in s: return ['if renpy.music.get_playing(channel="music") != cs_day_music_'+name+':']+['    '+c for c in commands]
        return commands
    if s.startswith('AMBIENCE:'):
        vol = '0.5' if 'усилить' in s else '0.28' if 'приглуш' in s else '0.45'
        return ['$ renpy.music.set_volume('+vol+', delay=1.0, channel="ambience")']
    if s.startswith('PAUSE:'): return ['pause '+re.search(r'\d+(?:\.\d+)?',s).group(0)]
    if s.startswith('SFX:'):
        if 'если' in s or 'по ситуации' in s: return []
        name = 'horn' if 'dinner_horn' in s else 'bed' if 'bed_squeak' in s else 'door'
        return ['$ renpy.music.set_volume(%s, channel="sound")'%('0.35' if name=='bed' else '0.65'), 'play sound cs_day_sfx_'+name]
    if s.startswith('ПЕРЕХОД:'): return ['window hide dissolve','scene black with dissolve','pause 1.0','scene bg int_house_of_mt_day with Dissolve(1.0)','window show dissolve']
    if s.startswith('SPRITES:'):
        if n == 10: return ['show mt normal pioneer at left','show cs_dasha_winter 1 normal at cs_day_dasha_right']
        if n in (11,12): return ['hide sl','hide mt','show mt normal pioneer at left with dissolve','show cs_dasha_winter 1 normal at cs_day_dasha_right with dissolve']
        return ['hide mt','show sl smile pioneer at left with dissolve','show cs_dasha_winter 1 normal at cs_day_dasha_right with dissolve']
    if s.startswith('SPRITE:'):
        if 'Лена' in s: return [] # POV protagonist has a mirror CG, no separate sprite.
        if 'Зимняя Дарья' in s: return ['hide cs_dasha_winter','show cs_dasha_pioneer 1 normal at cs_day_dasha_right with Dissolve(1.0)']
        if 'Ольга' in s: return ['show mt '+('surprise' if 'удив' in s else 'normal')+' pioneer at left with dissolve']
        if 'Славя' in s:
            if 'hide' in s: return ['hide sl with dissolve']
            return ['show mt normal pioneer far at cs_day_mt_center with dissolve','show cs_dasha_winter 1 far at cs_dasha_far_right with dissolve','show sl smile pioneer far at cs_day_sl_left with dissolve']
        costume = 'pioneer' if 'pioneer' in s else 'winter'
        num = '3' if 'насторож' in s or 'winter 3' in s else '2' if 'улыб' in s else '1'
        return ['show cs_dasha_'+costume+' '+num+' normal at cs_day_dasha_right with dissolve']
    if s.startswith('КОНЕЦ'): return []
    raise ValueError(s)
checks = {'Мы с Дарьей вошли в домик.':'inside','Экран всё ещё оставался чёрным.':'phone_off','Калькулятор.':'calculator','Фиолетовые волосы.':'mirror','Вышла Дарья.':'pioneer','Снаружи раздался сигнал горна.':'horn'}
for k in range(0,len(parts),3):
    n,title,text = int(parts[k]),parts[k+1].strip(),parts[k+2]
    lines = ['# -*- coding: utf-8 -*-','# Source: source/day01_part03.md.','label cs_day01_%02d:'%n,'    $ save_name = u'+json.dumps('Чужая смена — День 1: '+title,ensure_ascii=False)]
    if n==10: lines += ['    hide screen cs_day01_pending','    hide screen cs_phone','    $ day_time()','    $ persistent.sprite_time = "day"','    scene bg int_house_of_mt_day with Dissolve(1.5)','    play ambience cs_day_cabin fadeout 1.0 fadein 2.0','    window show dissolve']
    if n==14: lines += ['    hide sl','    show mt normal pioneer at left with dissolve']
    for p in re.split(r'\n\s*\n', text.strip()):
        p=p.strip()
        if not p or p=='---': continue
        if p.startswith('**['): lines += ['    '+c for c in stage(n,p[3:-3])]; continue
        m=re.match(r'\*\*(Лена|Дарья|Славя|Ольга Дмитриевна)(?: \([^)]*\))?:\*\*\\?\s*\n—\s*(.*)',p,re.S)
        if m: who,value={'Лена':'cs_ls','Дарья':'cs_da','Славя':'cs_sl','Ольга Дмитриевна':'cs_mt'}[m.group(1)],m.group(2).strip()
        elif p.startswith('*') and not p.startswith('**'): who,value='cs_th',p[1:-1]
        else: who,value='cs_narrator',p
        if n==13 and value=='Фиолетовые волосы.': lines += ['    scene cs_lena_pioneer_mirror with dissolve']
        if n==13 and value=='Я повернулась.': lines += ['    scene bg int_house_of_mt_day with dissolve','    show mt normal pioneer at left with dissolve']
        if n==12 and value=='Я медленно достала телефон.': lines += ['    show screen cs_phone(mode="off", phone_x=820, phone_width=260)']
        if n==12 and value=='Я моментально убрала телефон.': lines += ['    hide screen cs_phone']
        if value in checks: lines += ['    label cs_check_day01_part03_'+checks[value]+':']
        value=re.sub(r'\*\*(.*?)\*\*',r'{b}\1{/b}',value)
        lines += ['    '+who+' '+json.dumps(value,ensure_ascii=False)]
        manifest.append({'scene':n,'speaker':who,'text':value})
    lines += ['    return']
    (ROOT/'days/day01'/('%02d_%s.rpy'%(n,names[n]))).write_text('\n'.join(lines)+'\n',encoding='utf8')
(ROOT/'qa/day01_part03_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 3:',len(manifest),'blocks; five scenes.')
