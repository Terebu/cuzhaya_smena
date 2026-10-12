"""Author-directed emotion cues; preserve positions, costumes and distances.

Run before stage_darya_dialogue.py after regenerating a chapter.
"""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
CUES = {
    'cs_mt': {
        'surprise': ['Какие ещё девушки?', 'Ваш автобус?', 'Какой ещё план?', 'Ты серьёзно?', 'Ты не знаешь, какой сейчас год?', 'Пионерскую?', 'Что это у тебя?', 'Какой ещё калькулятор?', 'А где у него кнопки?', 'Откуда?', 'Это как понимать?', 'Вы знакомы?', 'Какой ещё истории?', 'Какое ещё голосование?'],
        'angry': ['Лена!', 'Следи за выражениями. Здесь дети.', 'Стой спокойно.', 'Ты опять за своё?', 'Лена.'],
        'smile': ['Добрый день.', 'Хорошо. Форму вам найдём.', 'Хорошо. Есть один свободный домик на двоих.', 'Через несколько часов ты ещё можешь изменить своё мнение.', 'Да. Пойдёмте, заодно познакомлю вас с остальными.', 'Семён! Познакомься. У нас ещё две новенькие.'],
        'normal': ['Дай сюда.', 'Вообще-то пионеров распределяют не так.', 'В пионеры вас действительно никто не принимал.', 'Кстати, вы не первые новенькие.', 'Вчера приехал ещё один молодой человек.', 'Семён.', 'Ваши вещи пока оставьте здесь. После обеда Славя покажет вам домик.', 'Девочки! В столовую, обедать!'],
        'sad': ['Лена…'],
    },
    'cs_sl': {
        'surprise': ['Простите?', 'На автобусе?', 'Но сейчас же июль.', 'Обе?', 'И проснулись уже здесь?', 'Вы её знаете?', 'Но знаете имя?', 'Откуда?'],
        'normal': ['Может быть, водитель просто отошёл?', 'Вы что-то сказали?', 'Точно. Я даже не знала, как тебя зовут.'],
        'smile': ['Хорошо!', 'Нашла!', 'Хорошо. Тогда давайте я отведу вас к вожатой!', 'Только вам, наверное, лучше снять тёплую одежду. Сегодня очень жарко.'],
        'shy': ['Ну… нет.'],
    },
    'cs_sy': {'awkward': ['Семён.'], 'serious': ['Да?'], 'thinking': ['Какой?'], 'surprised': ['Откуда ты…']},
}
TAGS = {'cs_mt':'mt', 'cs_sl':'sl', 'cs_sy':'cs_semen'}
# Reactions to narrated actions, rather than inventing spoken lines for cameos.
NARRATIVE = {
    ('19_dining_hall.rpy','И тут Алиса сама повернулась в нашу сторону.'): ('dv','surprise'),
    ('19_dining_hall.rpy','С явным интересом что-то сказала Ульяне.'): ('dv','grin'),
    ('19_dining_hall.rpy','Та моментально обернулась.'): ('us','grin'),
    ('15_two_newcomers.rpy','Ольга Дмитриевна вздохнула.'): ('mt','sad'),
}
CHECKPOINTS = {
    ('13_uniform.rpy','Следи за выражениями. Здесь дети.'): 'cs_check_camp_olga_angry',
    ('15_two_newcomers.rpy','Хорошо. Есть один свободный домик на двоих.'): 'cs_check_camp_olga_smile',
    ('19_dining_hall.rpy','Та моментально обернулась.'): 'cs_check_camp_cameo_reactions',
    ('20_comrade_semen.rpy','Семён.'): 'cs_check_camp_semen_awkward',
}
actors = {}
count = 0
for p in sorted((ROOT/'days/day01').glob('[0-9][0-9]_*.rpy')):
    if p.name.startswith('00'): continue
    lines = []; skip = False
    for line in p.read_text(encoding='utf8').splitlines():
        if re.match(r'\s+label cs_check_camp_',line): continue
        if line.strip() == '# cs_camp_emotion: text reaction': skip = True; continue
        if skip: skip = False; continue
        lines.append(line)
    out = []
    for line in lines:
        t = line.strip()
        if t.startswith('scene '): actors = {}
        show = re.match(r'show (mt|sl|dv|us|cs_semen) (\w+) (pioneer(?: far| close)?)(?: at (\w+))?',t)
        if show: actors[show[1]] = (show[2],show[3],show[4])
        hide = re.match(r'hide (mt|sl|dv|us|cs_semen)(?:\s|$)',t)
        if hide: actors.pop(hide[1],None)
        say = re.match(r'(cs_mt|cs_sl|cs_sy|cs_narrator) (".*")$',t)
        if say:
            who,text = say[1],json.loads(say[2]); tag = TAGS.get(who); pose = None
            for emotion,phrases in CUES.get(who,{}).items():
                if text in phrases: pose = emotion; break
            cue = NARRATIVE.get((p.name,text))
            if cue: tag,pose = cue
            if tag in actors and pose and actors[tag][0] != pose:
                _,costume,position = actors[tag]
                out += ['    # cs_camp_emotion: text reaction','    show '+tag+' '+pose+' '+costume+(' at '+position if position else '')+' with Dissolve(0.35)']
                actors[tag] = (pose,costume,position); count += 1
            checkpoint = CHECKPOINTS.get((p.name,text))
            if checkpoint: out.append('    label '+checkpoint+':')
        out.append(line)
    p.write_text('\n'.join(out)+'\n',encoding='utf8')
print('Staged',count,'camp character reactions.')
