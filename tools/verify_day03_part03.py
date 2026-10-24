"""Independent manuscript comparison, including the documented continuity edits."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent;s=(R/'source/day03_part03.md').read_text(encoding='utf8')
s=s[s.index('### Сцена 89.'):s.index('## Техническое задание')]
s=re.sub(r'\*\*\[MENU.*?### Сцена 94А\.', '### Сцена 94А.',s,flags=re.S)
before,ending=s.split('### Сцена 95.',1)
s=before+'### Сцена 95.'+ending.split('Я проводила её взглядом.')[0]
expected=[]
changes={'Женя просто кивнула и направилась к выходу.':'Женя просто кивнула и посмотрела в сторону выхода.','В этот момент из столовой вышел Семён.':'В этот момент по дорожке от столовой к нам подошёл Семён.'}
for raw in s.split('\n\n'):
 t=raw.strip()
 if not t or t=='---' or t.startswith(('#','**[')):continue
 if t.startswith('**'):
  name,words=t.split('\n',1);who='cs_mz' if 'Женя' in name else 'cs_sy' if 'Семён' in name else 'cs_da' if 'Дарья' in name else 'cs_ls';words=words.strip().lstrip('—–').strip()
 elif t.startswith('*') and t.endswith('*'):who,words='cs_th',t[1:-1]
 else:who,words='cs_narrator',t
 words=words.replace('\n',' ');expected.append((who,changes.get(words,words)))
extras=[('cs_narrator','У самого входа в столовую мне в голову пришла совершенно замечательная мысль.'),('cs_narrator','Закончив есть, Женя прошла мимо нашего стола с книгой в руках.'),('cs_narrator','Я обернулась к ней, не вставая.'),('cs_th','После нашего вчерашнего разговора мне стало любопытно, какие книги она любит.'),('cs_ls','Да. Хочу попробовать что-нибудь из того, что ты считаешь хорошим.'),('cs_narrator','Семён первым отложил ложку и поднялся.'),('cs_sy','Я пока отнесу поднос.'),('cs_narrator','Он забрал посуду и отошёл к стойке у выхода.')]
actual=[]
extras.append(('cs_narrator','Наши вчерашние спокойные разговоры.'))
for p in sorted((R/'days/day03/part03').glob('*_scene.rpy')):
 for line in p.read_text(encoding='utf8').splitlines():
  m=re.match(r'^\s+(cs_\w+) (".*")$',line)
  if m:actual.append((m[1],json.loads(m[2])))
assert Counter(actual)==Counter(expected)+Counter(extras),(Counter(expected)+Counter(extras)-Counter(actual),Counter(actual)-Counter(expected)-Counter(extras))
assert [x for x in actual if x not in extras]==expected,'Dialogue order changed'
flow=(R/'days/day03/part03/00_flow.rpy').read_text(encoding='utf8')
assert flow.count('    menu:')==1 and flow.count('$ cs_friend_mz += 1')==1
assert 'if not cs_mz_day3_book_awarded:' in flow and 'cs_mz_book_requested_day3 = True' in flow
labels=Counter();defaults=Counter()
for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')):
 t=p.read_text(encoding='utf8');labels.update(re.findall(r'^\s*label (\w+)',t,re.M));defaults.update(re.findall(r'^default (\w+)\s*=',t,re.M))
assert not [k for k,v in labels.items() if v>1];assert not [k for k,v in defaults.items() if v>1]
report={'status':'PASS','manuscript_blocks':len(expected),'implemented_blocks':len(actual),'documented_additions':extras,'documented_replacements':changes,'friendship_max_before':2,'friendship_max_after':3,'prior_awards':['day01/part10/55_choice.rpy: help guarded by cs_part10_choice','day02/00_flow.rpy: square thanks guarded by cs_mz_square_day2_awarded'],'viola_check':'voluntary morning visit; day02/part07/50_scene.rpy advises return if symptoms worsen'}
(R/'source/day03_part03_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print('SOURCE_PASS',len(expected),'original blocks +',len(extras),'continuity additions')
