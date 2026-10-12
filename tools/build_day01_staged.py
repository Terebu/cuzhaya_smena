"""Compile the supplied six-scene staging revision, preserving spoken attribution."""
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
source = (ROOT/'source/day01_staged.md').read_text(encoding='utf-8-sig')
body = source[source.index('### Сцена 1.'):source.index('## Указания для Codex')]
parts = re.split(r'### Сцена (\d+)\. ([^\n]+)\n', body)[1:]
names = ['bus','recognition','reality','reflection','home','slavya']
manifest = []
music = dict(zip(['just_think','into_the_unknown','doubt_everyone','a_promise_from_distant_days','mystery_girl_v2','lets_be_friends'], ['cs_day_music_think','cs_day_music_unknown','cs_day_music_doubt','cs_day_music_home','cs_day_music_mystery','cs_day_music_friends']))

def stage(n, s):
    if s.startswith('BG:'):
        if n == 1: return ['scene bg int_bus with Dissolve(1.2)', 'window show dissolve']
        if 'ext_bus' in s: return ['hide cs_dasha with dissolve', 'scene bg ext_bus with dissolve']
        if n == 4: return ['hide cs_dasha with dissolve']
        if 'сохранить' in s or 'без смены' in s or n == 6: return []
        return ['scene bg ext_camp_entrance_day with Dissolve(1.5)']
    if s.startswith('MUSIC:'):
        if 'продолжить' in s or 'оставить' in s: return []
        t = re.search(r'`([^`]+)`', s)
        duration = re.search(r'fade(?:in|out) (\d+(?:\.\d+)?)', s)
        d = duration.group(1) if duration else '2.0'
        if 'fadeout' in s: return ['stop music fadeout '+d]
        if not t: raise ValueError(s)
        volume = 0.25 if 'очень тих' in s else 0.4 if any(v in s for v in ['тихо','тихое','невысок']) else 0.65
        return ['$ renpy.music.set_volume(%s, delay=1.0, channel="music")' % volume, 'play music '+music[t.group(1)]+' fadeout 2.0 fadein '+d]
    if s.startswith('AMBIENCE:'):
        if 'grasshoper_clean' in s: return ['play sound "<from 0 to 3>sound/ambiences/grasshoper_clean.ogg" volume 0.25 fadein 0.5 fadeout 0.5']
        volume = 0.15 if 'очень тихо' in s else 0.35 if 'приглуш' in s else 0.65
        commands = ['$ renpy.music.set_volume(%s, delay=2.0, channel="ambience")' % volume]
        if n == 1: commands += ['play ambience cs_camp fadein 2.0']
        return commands
    if s.startswith('PAUSE:'): return ['pause '+re.search(r'\d+(?:\.\d+)?',s).group(0)]
    if s.startswith('SFX:'): return [] # Optional accents omitted without a verified match.
    if s.startswith('Постановка:'): return ['hide cs_dasha with dissolve', '$ renpy.music.set_volume(0.2, delay=2.0, channel="ambience")']
    if s.startswith('КОНЕЦ СЦЕНЫ'): return []
    if s.startswith('SPRITE:'):
        if 'смещается' in s: return ['show cs_dasha interested at cs_day_dasha_right with MoveTransition(0.8)']
        if 'sl normal pioneer' in s: return ['show sl normal pioneer at left with Dissolve(1.0)']
        if 'sl smile pioneer' in s: return ['show sl smile pioneer at left with dissolve']
        if 'Славя' in s: return ['show sl normal pioneer at left with dissolve']
        emotion = 'smile' if 'улыбка' in s else 'interested' if any(v in s for v in ['заинтересованная','удивлённая','обеспокоенная','задумчивая','настороженная']) else 'neutral'
        return ['show cs_dasha '+emotion+' at '+('cs_day_dasha_right' if n == 6 else 'cs_dasha_seated')+' with dissolve']
    raise ValueError('Unhandled command: '+s)

checkpoints = {'Я ещё секунд десять смотрела на вывеску.':'bus','Снаружи оказалось ещё жарче.':'outside','Посмотрела на отражение.':'reflection','Разумеется, экран оставался чёрным.':'phone','Если они вообще сейчас существуют.':'silence','Ой! Привет! Вы, наверное, только приехали?':'slavya'}
dest = ROOT/'days/day01'
for k in range(0, len(parts), 3):
    n, title, scene = int(parts[k]), parts[k+1].strip(), parts[k+2]
    lines = ['# -*- coding: utf-8 -*-', '# Source: source/day01_staged.md.', 'label cs_day01_%02d:' % n, '    $ save_name = u'+json.dumps('Чужая смена — День 1: '+title, ensure_ascii=False)]
    for p in re.split(r'\n\s*\n', scene.strip()):
        p = p.strip()
        if not p or p == '---': continue
        if p.startswith('**['):
            lines += ['    '+c for c in stage(n,p[3:-3])]
            continue
        match = re.match(r'\*\*(Лена|Дарья|Славя):\*\*\\?\s*\n—\s*(.*)', p, re.S)
        if match: who, text = {'Лена':'cs_ls','Дарья':'cs_da','Славя':'cs_sl'}[match.group(1)], match.group(2).strip()
        elif p.startswith('*') and not p.startswith('**'): who, text = 'cs_th', p[1:-1]
        else: who, text = 'cs_narrator', p
        if text in ['Автобус был пуст.','Я снова повернулась к лагерю.']: lines += ['    hide cs_dasha with dissolve']
        if text == 'Достала его из кармана.': lines += ['    show screen cs_phone(0, "off")']
        if text in ['Дарья наблюдала за мной.','Я убрала телефон обратно в карман.']: lines += ['    hide screen cs_phone']
        if n == 5 and text.startswith('Потому что одно дело'): lines += ['    hide cs_dasha with dissolve']
        if text == 'Удивлённо моргнула.': lines += ['    show sl surprise pioneer at left with dissolve']
        if text == '**Славя.**': lines += ['    $ cs_slavya_known = True']
        if text == 'Что будем делать?' and n == 3: lines += ['    show cs_dasha interested at cs_dasha_seated with dissolve']
        if text in checkpoints: lines += ['    label cs_check_day01_'+checkpoints[text]+':']
        text = re.sub(r'\*\*(.*?)\*\*', r'{b}\1{/b}', text)
        lines += ['    '+who+' '+json.dumps(text, ensure_ascii=False)]
        manifest.append({'scene':n,'speaker':who,'text':text})
    lines += ['    return']
    (dest/('%02d_%s.rpy' % (n,names[n-1]))).write_text('\n'.join(lines)+'\n',encoding='utf8')
(ROOT/'qa/day01_staged_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Staged day 1:',len(manifest),'text blocks, six scene files.')
