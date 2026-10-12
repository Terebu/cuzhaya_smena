"""Compile only supplied part 2 (scenes 7-9); no invented continuation."""
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
source = (ROOT/'source/day01_part02.md').read_text(encoding='utf-8-sig')
body = source[source.index('### Сцена 7.'):source.index('## 3. Что использовать')]
parts = re.split(r'### Сцена (\d+)\. ([^\n]+)\n',body)[1:]
names = {7:'uninvited',8:'camp_walk',9:'counsellor'}
trio = False
manifest = []

def stage(n, s):
    global trio
    if s.startswith('BG:'):
        if 'краткий акцент' in s or 'ext_square' in s or 'сохранить' in s: return []
        if n == 7: return [] # Retain the gate and running music from scene 6.
        bg = 'cs_camp_path_day' if n == 8 else 'ext_house_of_mt_day'
        return ['hide sl', 'hide cs_dasha_winter', 'hide cs_dasha', 'scene '+('' if bg.startswith('cs_') else 'bg ')+bg+' with Dissolve(1.5)', 'window show dissolve']
    if s.startswith('MUSIC:'):
        if any(v in s for v in ['продолж','оставить']): return []
        if 'приглушить' in s: return ['$ renpy.music.set_volume(0.15, delay=2.0, channel="music")']
        if 'вернуть' in s: return ['$ renpy.music.set_volume(0.35, delay=2.0, channel="music")']
        d = re.search(r'fade(?:in|out) (\d+(?:\.\d+)?)',s)
        duration = d.group(1) if d else '2.0'
        if 'fadeout' in s: return ['stop music fadeout '+duration]
        track = re.search(r'`([^`]+)`',s).group(1)
        name = {'my_daily_life':'cs_day_music_daily','just_think':'cs_day_music_think','mystery_girl_v2':'cs_day_music_mystery','into_the_unknown':'cs_day_music_unknown'}[track]
        vol = 0.22 if 'очень тихо' in s else 0.35 if 'тихо' in s else 0.55
        return ['$ renpy.music.set_volume(%s, delay=1.0, channel="music")'%vol, 'play music '+name+' fadeout 2.0 fadein '+duration]
    if s.startswith('AMBIENCE:'):
        if 'оставить' in s: return []
        vol = 0.2 if 'приглушить' in s else 0.35 if 'тихо' in s else 0.55
        result = ['$ renpy.music.set_volume(%s, delay=1.5, channel="ambience")'%vol]
        if n == 8: result += ['play ambience cs_day_camp_center fadeout 1.0 fadein 2.0']
        return result
    if s.startswith('PAUSE:'): return ['pause '+re.search(r'\d+(?:\.\d+)?',s).group(0)]
    if s.startswith('SFX:') or s.startswith('КОНЕЦ ЧАСТИ'): return [] # Optional sounds not auditioned.
    if s.startswith('SPRITES:'):
        if n == 8: return [] # Walking background initially clear until they turn.
        return ['hide cs_dasha', 'show sl '+('smile' if n == 7 else 'normal')+' pioneer at left with dissolve', 'show cs_dasha_winter 1 normal at cs_day_dasha_right with dissolve']
    if s.startswith('SPRITE:'):
        if 'Ольга' in s and 'normal' in s:
            trio = True
            return ['show sl normal pioneer far at cs_day_sl_left with MoveTransition(0.8)',
                    'show cs_dasha_winter 1 far at cs_dasha_far_right with MoveTransition(0.8)',
                    'show mt normal pioneer far at cs_day_mt_center with dissolve']
        if 'Ольга' in s: return ['show mt surprise pioneer far at cs_day_mt_center with dissolve']
        if 'Славя' in s:
            emotion = re.search(r'sl (\w+)',s)
            emotion = emotion.group(1) if emotion else 'normal'
            suffix, position = (' far','cs_day_sl_left') if trio else ('','left')
            return ['show sl '+emotion+' pioneer'+suffix+' at '+position+' with dissolve']
        num = re.search(r'winter (\d+)',s)
        number = num.group(1) if num else '1'
        distance, position = ('far','cs_dasha_far_right') if trio else ('normal','cs_day_dasha_right')
        return ['show cs_dasha_winter '+number+' '+distance+' at '+position+' with dissolve']
    raise ValueError(s)

checks = {'Славя несколько секунд смотрела на меня с тем выражением, которое обычно появляется у человека, когда незнакомка совершенно неожиданно называет его по имени.':'part02_gate',
          'Мы прошли через ворота.':'walk', 'Белая рубашка.':'trio',
          'Лена, давайте для начала зайдём внутрь.':'name',
          'Вот теперь интересно.':'tension'}
for k in range(0,len(parts),3):
    n,title,text = int(parts[k]),parts[k+1].strip(),parts[k+2]
    lines = ['# -*- coding: utf-8 -*-','# Source: source/day01_part02.md.',
             'label cs_day01_%02d:'%n,'    $ save_name = u'+json.dumps('Чужая смена — День 1: '+title,ensure_ascii=False)]
    if n == 7: lines += ['    hide screen cs_day01_pending', '    window show dissolve']
    for p in re.split(r'\n\s*\n',text.strip()):
        p = p.strip()
        if not p or p == '---': continue
        if p.startswith('**['): lines += ['    '+c for c in stage(n,p[3:-3])]; continue
        m = re.match(r'\*\*(Лена|Дарья|Славя|Ольга Дмитриевна)(?: \([^)]*\))?:\*\*\\?\s*\n—\s*(.*)',p,re.S)
        if m: who, rendered = {'Лена':'cs_ls','Дарья':'cs_da','Славя':'cs_sl','Ольга Дмитриевна':'cs_mt'}[m.group(1)],m.group(2).strip()
        elif p.startswith('*') and not p.startswith('**'): who,rendered='cs_th',p[1:-1]
        else: who,rendered='cs_narrator',p
        if n == 9 and rendered == 'Из домика вышла женщина.': lines += ['    $ cs_olga_seen = True']
        if n == 9 and rendered == 'Славя моментально приняла серьёзный вид.': lines += ['    show sl normal pioneer far at cs_day_sl_left with dissolve']
        if n == 8 and rendered == 'Некоторое время мы шли молча.': lines += ['    hide cs_dasha_winter with dissolve', '    hide sl with dissolve']
        if n == 8 and rendered.startswith('У тебя хотя бы имеется опыт'): lines += ['    show cs_dasha_winter 3 normal at cs_day_dasha_right with dissolve']
        if rendered in checks and not (rendered == 'Белая рубашка.' and n != 9): lines += ['    label cs_check_day01_'+checks[rendered]+':']
        rendered = re.sub(r'\*\*(.*?)\*\*',r'{b}\1{/b}',rendered)
        lines += ['    '+who+' '+json.dumps(rendered,ensure_ascii=False)]
        manifest.append({'scene':n,'speaker':who,'text':rendered})
    lines += ['    return']
    (ROOT/'days/day01'/('%02d_%s.rpy'%(n,names[n]))).write_text('\n'.join(lines)+'\n',encoding='utf8')
(ROOT/'qa/day01_part02_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Part 2:',len(manifest),'paragraphs; three scenes.')
