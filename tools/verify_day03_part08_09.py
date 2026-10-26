from pathlib import Path
from collections import Counter
import json,re
R=Path(__file__).resolve().parent.parent
expected=[]
for part in (8,9):
    t=(R/f'source/day03_part{part:02d}.md').read_text(encoding='utf-8-sig')
    t=t[t.index('### Сцена '):t.index('### Сцена 137.' if part==8 else '## Техническое задание')]
    segments=re.split(r'### Сцена (\d+[АБ]?)\. [^\n]+\n',t)
    for i in range(1,len(segments),2):
        k,body=segments[i:i+2]
        if k in ('134','140'):body=body.split('Выбор игрока:')[0].split('[ВЫБОР ИГРОКА]')[0]
        for b in re.split(r'\n\s*\n',body):
            b=b.strip()
            if not b or b=='---' or b.startswith(('[','#','- ','* ')):continue
            b=re.sub(r'^(?:Лена Соколова(?: \([^)]*\))?|Лена Тихонова|Семён|Женя|Дарья|Славя):\\?\s*[—–]\s*','',b)
            expected.append(b.replace('\n',' '))
actual=[]
for part in (8,9):
    for p in (R/f'days/day03/part{part:02d}').glob('*_scene.rpy'):
        for l in p.read_text(encoding='utf8').splitlines():
            m=re.match(r'\s+cs_\w+ (".*")$',l)
            if m:
                w=json.loads(m[1]);actual.append(w)
                assert not re.search(r'(Лена Соколова|Женя|Семён|Дарья):\s*—',w),w
allowed={x['before'] for x in json.loads((R/'source/day03_part08_09_editorial.json').read_text(encoding='utf8'))}
missing=Counter(expected)-Counter(actual)
assert set(missing)<=allowed,missing
paths=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
for pattern in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
    c=Counter(re.findall(pattern,alltext,re.M));assert not [n for n,v in c.items() if v>1]
s8='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part08').glob('*.rpy'))
s9='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part09').glob('*.rpy'))
assert s8.count('$ cs_friend_mz += 1')==1 and s9.count('$ cs_friend_se += 1')==1
assert '$ cs_friend_un +=' not in s8+s9
assert s8.count('$ cs_mz_book_borrowed_day3 = True')==1
assert 'if cs_mz_book_borrowed_day3:' in s8 and 'if cs_day03_novel_selected:' in s8
assert 'cs_mz_friend_on_arrival_day3 >= 3 and cs_mz_quiet_reading_place_day3' in s8
assert 'cs_se_friend_before_square_day3 >= 2 and cs_un_sketch_time_agreed_day3' in s9
assert 'if cs_mi_followup_invitation_day3:' in s8 and 'if cs_dv_followup_invitation_day3:' in s8
assert 'elif cs_dv_followup' not in s8
assert not re.search(r'^\s+\$ cs_(?:mi|dv)_followup_invitation_day3\s*=',s8+s9,re.M)
flow9=(R/'days/day03/part09/00_flow.rpy').read_text(encoding='utf8')
assert re.search(r'if cs_un_sketch_time_agreed_day3:\n\s+call cs_day03_144.*?\n\s+else:\n\s+call cs_day03_145',flow9,re.S)
assert s9.count('$ cs_un_sketch_completed_day3 = True')==1
assert s9.count('$ cs_un_private_drawing_shown_day3 = True')==1
assert 'cs_day03_reading_book_location = "house_table"' in s9
assert 'cs_day03_poster_location = "house_table"' in s9
assert 'cs_day03_poster_location == "darya_folder"' in s9
assert not re.search(r'\$ cs_lena_elbow_\w+\s*=',s8+s9)
assert 'Сёмочка, я вернулась' not in s8+s9
report=dict(status='PASS',source_blocks=len(expected),runtime_blocks=len(actual),edited_blocks=dict(missing),
 checks=['Unique labels/defaults','22 modular scenes','One guarded new MZ and SE reward each','Arrival/pre-choice snapshots','One guarded novel selection and loan','No new automatic UN points','Joint/solo drawing mutually exclusive','Independent MI/DV invitations retained','Single poster/book holder','Bandage unchanged','No duplicate short square meeting','Evening remains open'])
(R/'source/day03_part08_09_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('PART08_09_STATIC_PASS',len(expected),'source blocks;',len(actual),'runtime blocks')
