"""Verify part 2 against its source, with independent parsing and route checks."""
from pathlib import Path
from collections import Counter
import json,re
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part02.md').read_text(encoding='utf8')
s=s[s.index('### Сцена 83.'):s.index('## Техническое задание')]
s=re.sub(r'\*\*\[MENU.*?### Сцена 87А\.', '### Сцена 87А.',s,flags=re.S)
expected=[]
for raw in s.split('\n\n'):
 t=raw.strip()
 if not t or t=='---' or t.startswith(('#','**[')):continue
 if t.startswith('**'):
  who,line=t.split('\n',1)
  who='cs_da' if 'Дарья' in who else 'cs_sy' if 'Семён' in who else 'cs_ls'
  words=line.strip().lstrip('—–').strip()
 elif t.startswith('*') and t.endswith('*'):who,words='cs_th',t[1:-1]
 else:who,words='cs_narrator',t
 expected.append((who,words.replace('\n',' ').replace('Мы поднялись по ступенькам столовой.','До столовой оставалось совсем немного.')))
files=sorted((R/'days/day03/part02').glob('*_scene.rpy'))
# 85 calls its branches and common tail; compare serialized authoring order.
actual=[]
for p in files:
 for l in p.read_text(encoding='utf8').splitlines():
  m=re.match(r'^\s+(cs_\w+) (".*")$',l)
  if m:actual.append((m[1],json.loads(m[2])))
assert expected==actual,repr((Counter(expected)-Counter(actual),Counter(actual)-Counter(expected)))
flow=(R/'days/day03/part01/00_flow.rpy').read_text(encoding='utf8')
assert 'call cs_day03_82' not in flow and 'jump cs_day03_part02' in flow
new='\n'.join(p.read_text(encoding='utf8') for p in (R/'days/day03/part02').glob('*.rpy'))
assert new.count('$ cs_friend_se += 1')==1 and 'if not cs_se_day3_morning_awarded:' in new
assert not re.search(r'cs_friend_(?!se)\w+\s*\+=',new)
assert 'dinner_horn' not in new and 'int_dining_hall' not in new
assert 'cs_lena_pioneer_mirror' not in new, "The uniform CG belongs to day one in Olga\'s cabin"
assert '$ cs_actor_exit(["cs_semen"])' in new
assert 'cs_day03_poster_location =' not in new
report={'status':'PASS','manuscript_blocks':len(expected),'implemented_blocks':len(actual),'files':len(files),'retired_scene82':'replaced by 83-88; old named labels retained'}
(R/'source/day03_part02_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))
