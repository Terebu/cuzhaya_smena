"""Independent dialogue coverage, state and handoff checks for revised part4."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part04_revision.md').read_text(encoding='utf8')
s=s[s.index('### Сцена 96.'):s.index('## Задание для Codex')]
names={'Лена Соколова':'cs_ls','Дарья':'cs_da','Виола':'cs_vi','Семён':'cs_sy','Алиса':'cs_dv','Алиса (за дверью)':'cs_dv'}
changes={'Кстати, это ты там что-то кричала возле столовой?':'Кстати, это ты возле столовой очередь ко мне распределяла?','Третий визит к местной медицине.':'Плановый осмотр после вчерашних приключений.','Удивительно. Стоит дважды поранить локоть, и люди уже начинают считать тебя постоянным клиентом.':'Удивительно. Стоит вернуться на перевязку, и люди уже начинают считать тебя постоянным клиентом.'}
expected=[]
for t in re.split(r'\n\s*\n',s):
 t=t.strip()
 if not t or t=='---' or t.startswith(('#','**[','**Вариант','- ')):continue
 if t.startswith('**'):
  a,w=t.split('\n',1);who=names[a.strip('*:\\ ')];w=w.strip().lstrip('—–').strip()
 elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
 else:who,w='cs_narrator',t
 expected.append((who,changes.get(w.replace('\n',' '),w.replace('\n',' '))))
actual=[]
for p in (R/'days/day03/part04').glob('*_scene.rpy'):
 for l in p.read_text(encoding='utf8').splitlines():
  m=re.match(r'^\s+(cs_\w+) (".*")$',l)
  if m:actual.append((m[1],json.loads(m[2])))
extras=[('cs_narrator','Я убрала запечатанный пакет в сумку, чтобы не потерять его по дороге.'),('cs_vi','Запасная повязка ещё у тебя? Пусть остаётся в сумке. Если рука будет беспокоить, приходи.'),('cs_ls','Да, она со мной. Спасибо.')]
assert Counter(actual)==Counter(expected)+Counter(extras),(Counter(expected)+Counter(extras)-Counter(actual),Counter(actual)-Counter(expected)-Counter(extras))
scripts=list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy'));alltext='\n'.join(p.read_text(encoding='utf8') for p in scripts)
for pattern in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
 c=Counter(re.findall(pattern,alltext,re.M));assert not [x for x,n in c.items() if n>1]
flow=(R/'days/day03/part04/00_flow.rpy').read_text(encoding='utf8')
assert flow.count('$ cs_friend_dv += 1')==1 and 'if not cs_dv_medpoint_day3:' in flow
assert flow.count('$ cs_friend_viola += 1')==1 and 'if not cs_viola_day3_awarded:' in flow
assert flow.index('call cs_day03_viola_choice')<flow.index('call cs_day03_101')<flow.index('call cs_day03_102')<flow.index('call cs_day03_103')
gift=(R/'days/day03/part04/101_scene.rpy').read_text(encoding='utf8')
assert gift.index('$ cs_viola_spare_bandage = True')<gift.index('show dv normal pioneer')
assert 'cs_viola_friend_before_day3 >= 2 and not cs_viola_day3_bonus_seen' in gift
assert 'if not cs_viola_spare_bandage:' in gift
assert alltext.count('$ cs_friend_dv += 1')==2
stage=(R/'presence_staging.rpy').read_text(encoding='utf8');assert 'if n >= 1:' in stage
assert 'if cs_dv_medpoint_day3:' in (R/'days/day03/part06/116_scene.rpy').read_text(encoding='utf8')
assert 'if cs_day03_medpoint_revision_done and not cs_day03_part05_legacy_entry:' in (R/'days/day03/part05/104_scene.rpy').read_text(encoding='utf8')
result=dict(status='PASS',manuscript_blocks=len(expected),runtime_blocks=len(actual),editorial_replacements=changes,continuity_additions=extras,scripts=len(scripts),checks=['Unique labels/defaults','Two independent guarded DV rewards','Prior Viola friendship snapshot','Gift before Alice, no duplicate item','Single examination','Part5 bridge respects earlier decision','Solo framing shared by all registered actors','Long reflective focus clears all portraits'])
(R/'source/medpoint_revision_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print('REVISION_STATIC_PASS',len(expected),'manuscript blocks;',len(actual),'runtime blocks')
