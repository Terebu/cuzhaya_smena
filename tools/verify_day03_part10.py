from pathlib import Path
from collections import Counter
import ast,re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part10.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена'):s.index('## Техническое задание')]
parts=re.split(r'### Сцена (\d+[АБ]?)\. [^\n]+\n',s);expected=[]
for i in range(1,len(parts),2):
    k,body=parts[i:i+2]
    if k=='148':body=body.split('#### Выбор игрока')[0]
    for block in re.split(r'\n\s*\n',body):
        b=block.strip()
        if not b or b.startswith(('[','#')):continue
        b=re.sub(r'^(?:Лена Соколова|Дарья):\\?\s*[—–]\s*','',b)
        expected.append(b.replace('\n',' '))
allowed=set()
tree=ast.parse((R/'tools/build_day03_part10.py').read_text(encoding='utf8'))
for n in tree.body:
    if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ('replacements','own') for t in n.targets):allowed.update(ast.literal_eval(n.value))
actual=[]
for p in (R/'days/day03/part10').glob('*_scene.rpy'):
    for l in p.read_text(encoding='utf8').splitlines():
        m=re.match(r'\s+cs_\w+ (".*")$',l)
        if m:
            w=json.loads(m[1]);actual.append(w)
            assert not re.search(r'(Дарья|Лена Соколова):\s*—',w)
missing=Counter(expected)-Counter(actual)
assert set(missing)<=allowed,missing
text='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part10').glob('*.rpy'))
assert text.count('$ cs_friend_da += 1')==1 and 'if not cs_da_day3_music_awarded:' in text
assert 'if cs_da_day3_choice_done:' in text
assert text.count('play sound "sound/sfx/dinner_horn_processed.ogg"')==1
assert 'if not cs_day03_dinner_horn_played:' in text
assert 'cs_mz_friend_on_arrival_day3 >= 2' in text
assert 'if cs_friend_mi >= 2 and cs_mi_day3_arrangement_help:' in text
assert 'if cs_dv_music_talk_day3 and cs_friend_dv >= 2:' in text
assert not re.search(r'\$ cs_(?:mi|dv)_followup_invitation_day3\s*=',text)
assert not re.search(r'\$ cs_friend_(?:mz|se|mi|dv|un|sl)\s*[+\-]=',text)
assert 'if cs_un_sketch_completed_day3 == False:' in text
assert 'cs_day03_sketchbook_location = "house_table"' in text
assert 'cs_day03_reading_book_location = "house_table"' in text
assert not re.search(r'\$ cs_lena_elbow_\w+\s*=',text)
assert not re.search(r'\b(?:zoom|ypos|yoffset)\s',text)
paths=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
for pat in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
    c=Counter(re.findall(pat,alltext,re.M));assert not [k for k,v in c.items() if v>1]
assert len(expected)==935
result=dict(status='PASS',source_blocks=len(expected),runtime_blocks=len(actual),edited_blocks=dict(missing),checks=['One guarded Darya award','Exclusive silence/music outcome','One guarded horn','Arrival friendship snapshot','Independent MI/DV memories; invitations retained','Drawing duration conditional','Book and sketchbook stay home','Injury unchanged','No custom sprite lowering/zoom','Unique labels/defaults'])
(R/'source/day03_part10_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print('PART10_STATIC_PASS',len(expected),'source blocks;',len(actual),'runtime blocks')
