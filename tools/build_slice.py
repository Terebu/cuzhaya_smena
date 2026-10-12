"""Rebuild the seven scene files from the supplied authoritative manuscript.

Development tool only; never imported by Ren'Py. Python 3 + Pillow.
"""
import json
import re
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'source' / 'prologue.md'
PREFIX = 'mods/chuzaya_smena/'

def write(name, text):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + '\n', encoding='utf-8')

def quote(text):
    return json.dumps(text, ensure_ascii=False)

def markup(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'{b}\1{/b}', text)
    return text.replace('{', '{')

# Explicit attribution, including exchanges separated by narration.
SPEAKERS = {
    2: ['cs_ls'],
    4: ['cs_ls', 'cs_ls', 'cs_ls', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls'],
    5: ['cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls',
        'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da',
        'cs_da', 'cs_ls', 'cs_da'],
    6: ['cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls', 'cs_da', 'cs_ls'],
}

CHECKPOINTS = {
    (1, 'Меня зовут **Лена Соколова**.'): 'room',
    (2, 'Прекрасно.'): 'battery7',
    (3, 'Красные волосы.'): 'neutral',
    (4, 'За ночь прибавилось ещё около восьмисот человек.'): 'profile',
    (4, '— Молодец, Лена. Просто молодец.'): 'battery5',
    (4, '— Да ладно...'): 'battery2',
    (4, 'Несколько секунд я смотрела на собственное отражение в чёрном экране.'): 'phone_off',
    (5, 'Сугробы по краям дороги становились всё выше, а фонарей почти не осталось.'): 'winter',
    (5, 'Я кивнула.'): 'introduced',
    (6, 'Я заметила, как она прикрыла глаза.'): 'sleep_winter',
    (7, 'Сначала я увидела свет.'): 'summer',
    (7, 'Дарья всё ещё была рядом.'): 'sleep_summer',
    (7, '**«СОВЁНОК»**'): 'gate',
}

SCENE_START = {
    1: ['scene cs_room with Dissolve(1.2)', 'play music cs_music_calm fadein 2.0', 'window show dissolve'],
    2: ['scene cs_street with fade', 'play ambience cs_wind fadein 1.5', 'window show dissolve'],
    3: ['scene cs_bus_city at cs_bus_ride with fade', 'play ambience cs_bus_idle fadein 1.5', 'window show dissolve'],
    4: ['show cs_bus_city at cs_bus_ride with dissolve'],
    5: ['show cs_bus_city at cs_bus_ride with dissolve', 'play music cs_music_410 fadeout 2.0 fadein 3.0'],
    6: ['show cs_bus_winter at cs_bus_ride with Dissolve(1.5)'],
    7: ['scene black', 'window show dissolve'],
}

def directive(scene, text):
    # Scene opening directions are represented by SCENE_START.
    if text.startswith('ФОН:'):
        if 'Автобусная остановка' in text:
            return ['hide screen cs_phone', 'scene cs_stop with dissolve']
        if 'Вид из салона' in text:
            return ['hide cs_dasha with dissolve', 'scene bg ext_camp_entrance_day with Dissolve(1.8)',
                    'show cs_windshield', 'play ambience cs_camp fadeout 1.0 fadein 1.0']
        if scene == 7 and 'Салон автобуса' in text:
            return []  # The summer reveal happens in the preceding transition.
        return []
    if text.startswith('СПРАЙТ:'):
        emotion = 'neutral'
        if 'улыбка' in text: emotion = 'smile'
        if 'заинтересованная' in text: emotion = 'interested'
        if 'усталая' in text or 'спящая' in text: emotion = 'sleep'
        return ['show cs_dasha ' + emotion + ' at cs_dasha_seated zorder 5 with Dissolve(0.45)']
    if text.startswith('ИНТЕРФЕЙС:'):
        if 'Профиль' in text: return ['show screen cs_phone(5, "profile")']
        n = re.search(r'(\d+)%', text)
        if n: return ['show screen cs_phone(' + n.group(1) + ', "battery")']
    if text.startswith('ПАУЗА:'):
        if '3 секунды' in text:
            return ['window hide dissolve', 'pause 3.0']
        return ['pause 1.0']
    if text.startswith('КАМЕРА:'):
        return ['show bg ext_camp_entrance_day at cs_gate_approach']
    if text.startswith('ПЕРЕХОД:'):
        if 'летнем свете' in text:
            return ['window hide dissolve', 'scene cs_sunlight with Dissolve(2.0)', 'pause 0.6',
                    'scene bg int_bus with Dissolve(2.5)', 'window show dissolve']
        return ['window hide dissolve', 'scene black with Dissolve(1.0)', 'pause 0.6']
    if text.startswith('ЭКРАН:'):
        if 'Резкое' in text: return ['window hide', 'scene black', 'stop ambience fadeout 1.5']
        if 'Медленное' in text:
            return ['window hide dissolve', 'scene black with Dissolve(3.0)']
        return []
    if text.startswith('МУЗЫКА:'):
        if 'Постепенное' in text: return ['stop music fadeout 6.0']
        if 'заключительная' in text:
            return ['play music cs_music_calm noloop fadein 0.5', 'pause 3.0', 'stop music fadeout 2.0', 'pause 2.0']
        return []
    if text.startswith('ЗВУК:'):
        if 'исчезает' in text: return ['stop ambience fadeout 3.0', 'pause 3.0']
        if 'Пение птиц' in text: return ['play ambience cs_forest fadein 2.5']
        if 'Шипение' in text: return ['play sound cs_bus_stop']
        if 'Закрывающиеся' in text: return ['hide screen cs_phone', 'play sound cs_bus_door', 'stop ambience fadeout 1.0']
        if 'трогается' in text: return ['play sound cs_bus_start', 'play ambience cs_bus_moving fadeout 1.0 fadein 2.0']
        if 'телефона' in text: return ['show screen cs_phone(0, "off")', 'play sound cs_phone_error']
        return []
    raise ValueError('Unhandled stage direction: ' + text)

def main():
    text = SOURCE.read_text(encoding='utf-8-sig')
    parts = re.split(r'### Сцена (\d+)\. ([^\n]+)\n', text)[1:]
    manifest = []
    for k in range(0, len(parts), 3):
        n, title, body = int(parts[k]), parts[k+1].strip(), parts[k+2]
        lines = ['# -*- coding: utf-8 -*-', '# Source: source/prologue.md. Dialogue is preserved verbatim.',
                 'label cs_scene_%02d:' % n, '    $ save_name = u' + quote('Чужая смена — ' + title)]
        lines += ['    ' + cmd for cmd in SCENE_START[n]]
        spoken = 0
        count = 0
        for para in re.split(r'\n\s*\n', body.strip()):
            para = para.strip()
            if not para or para == '---' or para.startswith('###'): continue
            if para.startswith('**['):
                lines += ['    ' + cmd for cmd in directive(n, para[3:-3])]
                continue
            original = para
            if para.startswith('—'):
                who = SPEAKERS[n][spoken]; spoken += 1
                para = para[1:].strip()
            elif para.startswith('*') and not para.startswith('**'):
                who = 'cs_th'; para = para[1:-1]
            else: who = 'cs_narrator'
            # Story-controlled overlays are dismissed at the exact putting-away beats.
            if original in ['Телефон отправился обратно в карман.', 'Я убрала телефон.']:
                lines += ['    hide screen cs_phone']
            if n == 5 and original == 'Окраина — редкими домами.':
                lines += ['    show cs_bus_winter at cs_bus_ride with Dissolve(2.0)', '    show cs_dasha neutral at cs_dasha_seated zorder 5 with dissolve']
            if n == 5 and original == '— Дарья.':
                lines += ['    $ cs_darya_known = True']
            if n == 5 and original == 'За окном медленно падал снег.':
                lines += ['    show cs_snow at cs_snow_drift with dissolve']
            if (n, original) in CHECKPOINTS:
                lines += ['    label cs_check_' + CHECKPOINTS[(n, original)] + ':']
            lines += ['    ' + who + ' ' + quote(markup(para))]
            manifest.append({'scene': n, 'speaker': who, 'source': original, 'rendered': markup(para)})
            count += 1
        assert spoken == len(SPEAKERS.get(n, [])), (n, spoken)
        lines += ['    return']
        write('scenes/%02d_%s.rpy' % (n, ['ordinary','seven_percent','stranger','instagram','wrong_way','last_stop','summer'][n-1]), '\n'.join(lines))
        print('Scene', n, title, ':', count, 'paragraphs;', spoken, 'spoken lines')
    write('qa/dialogue_manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
    # Native vector masks, not edits of source art. Runtime AlphaMask replaces only windows.
    mask = Image.new('RGBA', (1920,1080), (255,255,255,255))
    d = ImageDraw.Draw(mask)
    windows = [[(0,316),(45,320),(72,454),(0,454)], [(237,326),(393,325),(393,405),(224,413)],
               [(580,310),(754,310),(754,394),(578,395)],
               [(811,289),(867,291),(869,332),(936,335),(932,355),(884,362),(883,408),(932,413),(938,533),(811,540)],
               [(1010,293),(1301,291),(1316,205),(1333,189),(1354,410),(1283,432),(1135,409),(1069,451),(1054,535),(945,531),(947,414),(959,409),(961,361),(944,354),(944,335),(1007,334)],
               [(1474,317),(1631,320),(1631,424),(1488,424)], [(1791,318),(1920,318),(1920,493),(1762,490)]]
    for poly in windows: d.polygon(poly,fill=(255,255,255,0))
    (ROOT/'ui').mkdir(exist_ok=True); mask.save(ROOT/'ui'/'bus_window_mask.png')
    # Snow confined to windows; ATL handles gentle falling motion.
    snow = Image.new('RGBA',(1920,1080),(0,0,0,0)); ds=ImageDraw.Draw(snow)
    import random
    rng=random.Random(410)
    for i in range(160):
        x=rng.randrange(1920);y=rng.randrange(1080);r=rng.randrange(1,4)
        if mask.getpixel((x,y))[3] == 0: ds.ellipse((x-r,y-r,x+r,y+r),fill=(240,243,248,130))
    snow.save(ROOT/'ui'/'snow.png')

if __name__ == '__main__': main()
