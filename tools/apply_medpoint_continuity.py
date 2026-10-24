"""Apply the revised visit's consequences after regenerating parts 5 and 6."""
from pathlib import Path
R=Path(__file__).resolve().parent.parent
p=R/'days/day03/part05/104_scene.rpy';s=p.read_text(encoding='utf8')
if '# revised_medpoint_bridge' not in s:
 a=s.index('    if cs_day03_part05_legacy_entry:');b=s.index('    cs_narrator "Я сделала шаг вперёд."')
 old=s[a:b]
 old=old.replace('    label cs_check_day03_104:\n','')
 new='    # revised_medpoint_bridge: the decision was already made in part 4.\n    label cs_check_day03_104:\n    if cs_day03_medpoint_revision_done and not cs_day03_part05_legacy_entry:\n        cs_narrator "По дороге к домику вожатой я ещё раз посмотрела на повязку."\n        cs_ls "Помочь можно и без подвигов. Начнём с чего-нибудь, для чего не нужны обе руки."\n        cs_da "Вот с этого и начни разговор."\n    else:\n'+''.join('    '+line+'\n' for line in old.splitlines())
 s=s[:a]+new+s[b:];p.write_text(s,encoding='utf8')
p=R/'days/day03/part06/116_scene.rpy';s=p.read_text(encoding='utf8')
if '# morning_alice_trust' not in s:
 anchor='    cs_th "За первые два дня мы успели обменяться несколькими замечаниями, но толком так и не поговорили."\n'
 replacement='    # morning_alice_trust: a quiet callback, no disclosure of her visit.\n    if cs_dv_medpoint_day3:\n        cs_th "Утром мы уже поговорили без взаимных уколов. Теперь хотелось узнать, чем она живёт, кроме вечной готовности спорить."\n    else:\n'+ '    '+anchor
 assert anchor in s;s=s.replace(anchor,replacement)
 anchor='    cs_dv "Чего?"\n'
 s=s.replace(anchor,'    if cs_dv_medpoint_day3:\n        cs_dv "Опять ты, Соколова? Только без комиссий."\n        cs_ls "Никаких комиссий. Просто слушаю."\n    else:\n        cs_dv "Чего?"\n',1)
 # Avoid a judgmental compliment that provokes instead of respecting her craft.
 s=s.replace('Было видно, что ты занята музыкой, а не попытками убедить всех, какая ты крутая.','На концерте гитара хорошо держала ритм, даже когда зал шумел. Мне это понравилось.')
 p.write_text(s,encoding='utf8')
p=R/'days/day03/part06/117a_scene.rpy';s=p.read_text(encoding='utf8')
s=s.replace('Особенно если не начинать знакомство с попытки вывести её из себя.','Особенно если слушать её ответы, а не искать повод для следующей колкости.')
p.write_text(s,encoding='utf8')
print('Part4 → 5 → 6 continuity applied.')
