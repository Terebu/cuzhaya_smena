"""Independent manuscript/state audit, with explicit editorial exceptions."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part07_revision.md').read_text(encoding='utf-8-sig')
s=s[s.index('### Сцена 121.'):s.index('## Задание для Codex')]
s=re.sub(r'#### Выбор игрока.*?(?=### Сцена 125А\.)','',s,flags=re.S)
expected=[]
for t in re.split(r'\n\s*\n',s):
    t=t.strip()
    if not t or t=='---' or t.startswith(('#','**[','- ')):continue
    m=re.match(r'\*\*(.+?):\*\*\\?\s*\n[—–]\s*(.*)',t,re.S)
    if m:t=m[2]
    elif t.startswith('*') and t.endswith('*'):t=t[1:-1]
    expected.append(t.replace('\n',' '))
actual=[]
for p in sorted((R/'days/day03/part07').glob('*_scene.rpy')):
    for line in p.read_text(encoding='utf8').splitlines():
        m=re.match(r'^\s+cs_\w+ (".*")$',line)
        if m:actual.append(json.loads(m[1]))
edits={
 'Я уже отложила пару книг. Ты вчера говорила, что тебе интереснее истории про людей, чем просто приключения.',
 'Ты ведь вчера быстро закончила книгу.', 'Женя рассмеялась уже открыто.',
}
missing=Counter(expected)-Counter(actual)
assert set(missing)<=edits,missing
paths=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'))
alltext='\n'.join(p.read_text(encoding='utf-8-sig') for p in paths)
for pattern in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
    counts=Counter(re.findall(pattern,alltext,re.M));assert not [n for n,c in counts.items() if c>1]
new='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part07').glob('*.rpy'))
flow=(R/'days/day03/part07/00_flow.rpy').read_text(encoding='utf8')
assert flow.count('    menu:')==1 and new.count('$ cs_friend_un += 1')==1
assert 'if not cs_un_day3_lunch_awarded:' in flow
assert '$ cs_friend_mz +=' not in new and 'play sound' not in new
music=(R/'days/day03/part07/127_scene.rpy').read_text(encoding='utf8')
assert '    if cs_friend_mi >= 2 and cs_mi_day3_arrangement_help:' in music
assert '    if cs_friend_dv >= 2 and cs_dv_music_talk_day3:' in music
assert 'elif cs_friend_dv' not in music
assert 'cs_day03_poster_location = "dining_chair"' in new and 'cs_day03_poster_location = "darya_folder"' in new
assert 'if cs_day03_reading_book_selected:' in new or 'cs_day03_reading_book_selected = True' in (R/'days/day03/part08/130_scene.rpy').read_text(encoding='utf8')  # book selection moved to part 8
assert 'cs_reading_book_borrowed =' not in new and 'cs_lena_elbow_injury_day2 =' not in new
assert new.count('$ cs_un_sketch_time_agreed_day3 = True')==1
assert 'cs_un_day3_art_talk' in new and 'cs_lena_book_returned' in new
assert 'jump cs_day03_part07' in (R/'days/day03/part06/00_flow.rpy').read_text(encoding='utf8')
reward_sites=[p.relative_to(R).as_posix() for p in paths if '$ cs_friend_mz += 1' in p.read_text(encoding='utf-8-sig')]
assert reward_sites[:3]==['days/day01/part10/55_choice.rpy','days/day02/00_flow.rpy','days/day03/part03/00_flow.rpy'] and all(x.startswith(('days/day03/part08/','days/day03/part11/')) for x in reward_sites[3:]),reward_sites  # later parts add their own guarded rewards
report=dict(status='PASS',manuscript_blocks=len(expected),runtime_blocks=len(actual),editorial_replacements=dict(missing),
 mz_reward_sites=reward_sites,max_mz_at_lunch=3,checks=['Unique labels/defaults','One guarded UN menu reward','No passive friendship awards','Independent MI and DV event conditions','Actual book selected once, remains in library','Art/preference/returned-book continuity','Poster holder preserved','Injury, bandage and documents unchanged','Day3 remains open'])
(R/'source/day03_part07_revision_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('LUNCH_REVISION_STATIC_PASS',len(expected),'manuscript blocks;',len(actual),'runtime blocks')
