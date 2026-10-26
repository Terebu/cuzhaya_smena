"""Independent source coverage plus continuity invariants, before native tests."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part13.md').read_text(encoding='utf-8-sig');s=s[s.index('### Сцена 171.'):s.index('## Техническое задание для Codex')]
expected=[]
for b in re.split(r'\n\s*\n',s):
 b=b.strip().replace('**','')
 if not b or b=='---' or b.startswith(('#','[','- ','Выбор игрока:','1. «','2. «')):continue
 m=re.match(r'(?:Лена Соколова(?: \([^)]*\))?|Дарья|Женя):\\?\s*[\n ]+[—–]\s*(.*)',b,re.S)
 expected.append((m[1] if m else b.strip('*')).replace('\n',' '))
t='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part13').glob('*.rpy'))
actual=[json.loads(m[1]) for m in re.finditer(r'^\s*cs_(?:ls|da|mz|th|narrator) (".*")$',t,re.M)]
allowed={
 'А ведь собиралась только немного почитать.','До конца оставалось совсем немного.',
 'А дядя наконец понял, что не всё в жизни измеряется карьерой и деньгами.',
 'Жаль, что для этого понадобилось столько времени.','Ты сегодня после библиотеки даже не начала сразу шутить.',
 'Нет. Нормально.','На улице окончательно стемнело.','Пара страниц, одна глава, и домой.',
 'Мику и Алиса ждут нас завтра в музыкальном клубе — если мы обещали прийти.',
 'Окна были тёмными.','Потом открыла дверь.'}
missing=Counter(expected)-Counter(actual);assert set(missing)<=allowed,missing
assert len(expected)==817,len(expected)
assert t.count('$ cs_friend_da += 1')==1
assert 'if not cs_da_day3_night_trust_awarded:' in t and 'if cs_da_day3_night_choice_done:' in t
assert not re.search(r'\$ cs_friend_(?:mz|se|sl|mi|dv|un)\s*[+\-]=',t)
assert t.count('$ cs_day03_reading_book_location = "library"')==1
assert t.count('$ cs_mz_book_borrowed_day3 = False')==1
assert t.count('$ cs_mz_book_finished_day3 = True')==1
assert 'elif cs_friend_mz >= 3 and cs_mz_hug_allowed_day3 == False:' in t
assert t.index('Можно тебя обнять на прощание?')<t.index('Ладно. Только недолго.')<t.index('Осторожно обняла её здоровой рукой.')
assert not re.search(r'\b(?:zoom|ypos|yoffset)\s',t)
assert not re.search(r'\$ cs_(?:day03_poster_location|day03_sketchbook_location|lena_elbow_\w+|mi_followup_invitation_day3|dv_followup_invitation_day3|sl_day4_notice_offer)\s*=',t)
assert 'if cs_mi_followup_invitation_day3:' in t and 'if cs_dv_followup_invitation_day3:' in t
assert 'if cs_mz_friend_on_arrival_day3 >= 1:' in t
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')))
for pat in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
 c=Counter(re.findall(pat,alltext,re.M));assert not [k for k,v in c.items() if v>1]
result=dict(status='PASS',source_blocks=len(expected),runtime_blocks=len(actual),edited_blocks=dict(missing),checks=['one guarded DA reward','book finished then returned','first hug consent and mutually exclusive farewell','preserved all future hooks','prior book-selection snapshot','no lowering','shared actor staging','unique defaults and labels'])
(R/'source/day03_part13_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print('PART13_STATIC_PASS',len(expected),'source;',len(actual),'runtime blocks')
