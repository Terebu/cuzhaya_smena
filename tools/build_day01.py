"""Build only the supplied first instalment of day 1; preserve every paragraph."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
source = (ROOT/'source/day01_part01.md').read_text(encoding='utf-8-sig')
paragraphs = [p.strip() for p in re.split(r'\n\s*\n', source) if p.strip() and not p.strip().startswith('#')]
darya = {2,6,12,14,17,20,22,25,27,29,31,33,35,37,39,42,44,46,48,52,54,56,58,60,62,64,66,68,70,73,75,78,81,84,87,91,92,96}
splits = {'Я медленно спустилась на землю.': 2,
          'И именно в этот момент мне пришло в голову кое-что ещё.': 3,
          'Я вспомнила начало новеллы.': 4}
names = ['bus','recognition','reflection','slavya']
starts = {
 1: ['$ day_time()', '$ persistent.sprite_time = "day"', 'stop music fadeout 1.0',
     'scene bg ext_camp_entrance_day with dissolve', 'show cs_windshield',
     'play ambience cs_forest fadein 1.0', 'window show dissolve'],
 2: ['hide cs_dasha with dissolve', 'scene bg ext_camp_entrance_day with Dissolve(1.2)',
     'play ambience cs_camp fadeout 1.0 fadein 1.5'],
 3: ['hide cs_dasha with dissolve', 'stop music fadeout 2.0'],
 4: ['hide cs_dasha with dissolve', 'stop music fadeout 2.0'],
}
before = {
 'На Дарью.': ['show cs_dasha neutral at cs_dasha_seated with dissolve'],
 'Автобус был пуст.': ['hide cs_dasha with dissolve', 'scene bg int_bus with dissolve'],
 'Позади послышались шаги.': ['show cs_dasha interested at cs_dasha_seated with dissolve'],
 'Двери автобуса оставались открытыми.': ['hide cs_dasha with dissolve'],
 'В летнем воздухе едва различимо звучала музыка. Негромкая, какая-то старомодная, почти теряющаяся среди шелеста листвы.': ['play music "<volume 0.18>sound/music/sunny_day.ogg" fadein 2.0'],
 'Дарья вышла следом.': ['show cs_dasha neutral at cs_dasha_seated with dissolve'],
 'В памяти начали всплывать образы.': ['hide cs_dasha with dissolve', 'play music cs_music_After_Hours fadeout 2.0 fadein 3.0'],
 'Дарья нахмурилась.': ['show cs_dasha interested at cs_dasha_seated with dissolve'],
 'Я снова повернулась к лагерю.': ['hide cs_dasha with dissolve'],
 'Я медленно вдохнула.': ['stop music fadeout 3.0'],
 'Дарья встала рядом.': ['show cs_dasha neutral at cs_dasha_seated with dissolve'],
 'Дарья подошла ко мне.': ['show cs_dasha interested at cs_dasha_seated with dissolve'],
 'Достала его из кармана.': ['hide cs_dasha with dissolve', 'show screen cs_phone(0, "off")'],
 'Дарья наблюдала за мной.': ['show cs_dasha neutral at cs_dasha_seated with dissolve'],
 'Я убрала телефон обратно в карман.': ['hide screen cs_phone'],
 'Квартира.': ['hide cs_dasha with dissolve', 'play music cs_music_calm fadein 3.0'],
 'Дарья повернулась ко мне.': ['show cs_dasha interested at cs_dasha_seated with dissolve'],
 'Из-за ворот вышла девушка.': ['hide cs_dasha with dissolve', 'show sl normal pioneer at center with dissolve'],
 'Удивлённо моргнула.': ['show sl surprise pioneer at center with dissolve'],
 'Затем приветливо улыбнулась.': ['show sl smile pioneer at center with dissolve'],
 '**Славя.**': ['$ cs_slavya_known = True'],
 'Я медленно повернулась к Дарье.': ['show sl smile pioneer at left with move', 'show cs_dasha interested at cs_dasha_seated with dissolve'],
}
checkpoints = { 'Я ещё секунд десять смотрела на вывеску.': 'bus',
               'Снаружи оказалось ещё жарче.': 'outside',
               'Посмотрела на отражение.': 'reflection',
               'Разумеется, экран оставался чёрным.': 'phone',
               '— Ой! Привет! Вы, наверное, только приехали?': 'slavya'}
files = {}
scene = 1
spoken = 0
for p in paragraphs:
    scene = splits.get(p, scene)
    if scene not in files:
        files[scene] = ['# -*- coding: utf-8 -*-', '# Source: source/day01_part01.md; supplied text only.',
                       'label cs_day01_%02d:' % scene,
                       '    $ save_name = u"Чужая смена — День 1, часть 1: %d"' % scene]
        files[scene] += ['    '+s for s in starts[scene]]
    lines = files[scene]
    lines += ['    '+s for s in before.get(p, [])]
    if p in checkpoints: lines.append('    label cs_check_day01_'+checkpoints[p]+':')
    if p.startswith('—'):
        spoken += 1
        who = 'cs_sl' if spoken == 94 else 'cs_da' if spoken in darya else 'cs_ls'
        text = p[1:].strip()
    elif p.startswith('*') and not p.startswith('**'):
        who, text = 'cs_th', p[1:-1]
    else:
        who, text = 'cs_narrator', p
    text = re.sub(r'\*\*(.*?)\*\*', r'{b}\1{/b}', text)
    lines.append('    '+who+' '+json.dumps(text, ensure_ascii=False))
if spoken != 98: raise ValueError('Expected 98 spoken paragraphs, got %d' % spoken)
dest = ROOT/'days/day01'
dest.mkdir(parents=True, exist_ok=True)
for n, lines in files.items():
    lines.append('    return')
    (dest/('%02d_%s.rpy' % (n, names[n-1]))).write_text('\n'.join(lines)+'\n', encoding='utf8')
print('Day 1 part 1:', len(paragraphs), 'paragraphs;', spoken, 'spoken; four scene files.')
