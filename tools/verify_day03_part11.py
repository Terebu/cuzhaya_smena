from pathlib import Path
from collections import Counter
import ast,re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part11.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена'):s.index('## Задание для Codex')]
parts=re.split(r'### Сцена (\d+[АБ]?)\. [^\n]+\n',s);expected=[]
for i in range(1,len(parts),2):
    k,body=parts[i:i+2]
    if k=='159':body=body.split('#### Выбор игрока')[0]
    for raw in re.split(r'\n\s*\n',body):
        b=raw.strip().replace('**','').strip()
        if not b or b=='---' or b.startswith(('[','#')):continue
        b=b.strip('*')
        b=re.sub(r'^(?:Лена Соколова|Дарья|Женя|Семён|Мику|Алиса):\\?\s*[—–]\s*','',b)
        expected.append(b.replace('\n',' '))
allowed=set();tree=ast.parse((R/'tools/build_day03_part11.py').read_text(encoding='utf8'))
for n in tree.body:
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('edits','variants') for t in n.targets):allowed.update(ast.literal_eval(n.value))
actual=[]
for p in (R/'days/day03/part11').glob('*_scene.rpy'):
    for l in p.read_text(encoding='utf8').splitlines():
        m=re.match(r'\s+cs_\w+ (".*")$',l)
        if m:
            w=json.loads(m[1]);actual.append(w);assert not re.search(r'(Дарья|Женя|Мику|Алиса|Семён|Лена Соколова):\s*—',w)
missing=Counter(expected)-Counter(actual);assert set(missing)<=allowed,missing
text='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part11').glob('*.rpy'))
assert text.count('$ cs_friend_mz += 1')==1 and 'if not cs_mz_evening_help_awarded:' in text
assert 'if cs_mz_evening_choice_done:' in text
assert 'cs_mz_dinner_friend_on_arrival >= 3 and cs_mz_open_library_invitation_day3' in text
assert '$ cs_mz_dinner_friend_on_arrival = cs_friend_mz' in text
assert 'if cs_mz_dinner_friend_on_arrival is None:' in text
assert text.count('$ cs_mz_hug_allowed_day3 = True')==1
assert 'if cs_day03_dinner_greeting_done:' in text
assert text.count('$ cs_mz_evening_help_completed_day3 = True')==1
assert 'if cs_mz_evening_help_completed_day3:' in text
assert 'play sound' not in text and 'dinner_horn' not in text
assert 'bg int_dining_hall_sunset' in text and 'int_dining_hall_people_sunset' not in text
assert 'if cs_friend_mi >= 2 and cs_mi_followup_invitation_day3:' in text
assert 'if cs_friend_dv >= 2 and cs_dv_followup_invitation_day3:' in text
assert '$ cs_mi_followup_target_day = 4' in text and '$ cs_dv_followup_target_day = 4' in text
assert not re.search(r'\$ cs_(?:mi|dv)_followup_invitation_day3\s*=',text)
assert not re.search(r'\$ cs_friend_(?:da|se|mi|dv|un|sl)\s*[+\-]=',text)
assert not re.search(r'\$ cs_(?:lena_elbow_\w+|day03_reading_book_location|day03_poster_location)\s*=',text)
assert not re.search(r'\b(?:zoom|ypos|yoffset)\s',text)
flow=(R/'days/day03/part11/00_flow.rpy').read_text(encoding='utf8')
assert re.search(r'if cs_mz_evening_help_day3:\n\s+call cs_day03_161a.*?\n\s+else:\n\s+call cs_day03_161b',flow,re.S)
paths=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
for pat in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
    c=Counter(re.findall(pat,alltext,re.M));assert not [k for k,v in c.items() if v>1]
assert len(expected)==961
result=dict(status='PASS',source_blocks=len(expected),runtime_blocks=len(actual),edited_blocks=dict(missing),checks=['Arrival snapshot before menu','One guarded MZ award','Consent hug only at prior threshold plus invitation','One guarded actual completion of help','Exclusive help/walk','No dinner horn replay','Independent day4 music appointments; pending flags retained','Book/poster/injury unchanged','No sprite lowering/zoom','Unique labels/defaults'])
(R/'source/day03_part11_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print('PART11_STATIC_PASS',len(expected),'source blocks;',len(actual),'runtime blocks')
