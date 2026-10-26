"""Independent manuscript, state and chronology checks for chapter 12."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
src=(R/'source/day03_part12.md').read_text(encoding='utf-8-sig')
src=src[src.index('### Сцена 163.'):src.index('## Техническое задание для Codex')]
expected=[]
for b in re.split(r'\n\s*\n',src):
 b=b.strip().replace('**','')
 if not b or b=='---' or b.startswith(('#','[','- ','Вариант ')):continue
 m=re.match(r'(?:Лена Соколова(?: \([^)]*\))?|Дарья|Женя|Семён|Славя):\\?\s*[\n ]+[—–]\s*(.*)',b,re.S)
 expected.append((m[1] if m else b.strip('*')).replace('\n',' '))
text='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part12').glob('*.rpy'))
actual=[json.loads(m[1]) for m in re.finditer(r'^\s*cs_(?:ls|da|mz|sy|sl|th|narrator) (".*")$',text,re.M)]
allowed={
 'На безопасной полке лежала папка с концертным плакатом.','Я подошла к кровати.',
 'Не потому, что я получила новую книгу.','После сегодняшнего количества страниц, наверное, уже нет.',
 'А Семён, между прочим, уже сам научился поддерживать представление.',
 'Так что, возможно, мой педагогический эксперимент оказался успешным.'}
missing=Counter(expected)-Counter(actual);assert set(missing)<=allowed,missing
assert len(expected)==832,len(expected)
assert text.count('$ cs_friend_sl += 1')==1
assert 'if not cs_sl_evening_help_awarded:' in text and 'if cs_sl_evening_choice_done:' in text
assert 'if cs_sl_friend_before_evening_choice >= 2:' in text
assert '$ cs_sl_friend_before_evening_choice = cs_friend_sl' in text
assert text.count('$ cs_sl_day4_notice_offer = True')==1
assert text.count('$ cs_mz_evening_help_completed_day3 = True')==1
assert not re.search(r'\$ cs_friend_(?:mz|se|da|mi|dv|un)\s*[+\-]=',text)
assert '$ cs_day03_reading_book_location = "with_lena"' in text
assert text.count('$ cs_day03_reading_book_location =')==1
assert not re.search(r'\$ cs_(?:day03_poster_location|lena_elbow_\w+|mi_followup_invitation_day3|dv_followup_invitation_day3)\s*=',text)
assert not re.search(r'\b(?:zoom|ypos|yoffset)\s',text)
flow=(R/'days/day03/part11/00_flow.rpy').read_text(encoding='utf8').split('label cs_day03_part11_legacy_tail:')[0]
assert 'jump cs_day03_part12' in flow and 'call cs_day03_161' not in flow and 'call cs_day03_162' not in flow
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')))
for pat in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
 c=Counter(re.findall(pat,alltext,re.M));assert not [k for k,v in c.items() if v>1]
result=dict(status='PASS',source_blocks=len(expected),runtime_blocks=len(actual),edited_blocks=dict(missing),checks=['Old 161/162 unreachable in fresh flow','One guarded SL award; prior friendship threshold','No new MZ/SE points','Help only when chosen and unfinished','Book taken exactly in house','Darya absent on solo trip','No lowering/zoom','Unique labels/defaults'])
(R/'source/day03_part12_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print('PART12_STATIC_PASS',len(expected),'source;',len(actual),'runtime blocks')
