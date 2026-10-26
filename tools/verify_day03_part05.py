"""Independent manuscript, state, handoff and resource-reference audit."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part05.md').read_text(encoding='utf8');s=s[s.index('### Сцена 104.'):s.index('## Техническое задание')]
s=re.sub(r'\*\*Выбор:\*\*.*?### Сцена 109А\.', '### Сцена 109А.',s,flags=re.S)
s=s.split('**[ЕСЛИ `cs_mz_map_lead == True`:]**')[0]
expected=[]
for t in s.split('\n\n'):
 t=t.strip()
 if not t or t=='---' or t.startswith(('#','**[')):continue
 if t.startswith('**'):
  name,w=t.split('\n',1);who='cs_mt' if 'Ольга' in name else 'cs_sl' if 'Славя' in name else 'cs_sy' if 'Семён' in name else 'cs_da' if 'Дарья' in name else 'cs_ls';w=w.strip().lstrip('—–').strip()
 elif t.startswith('*') and t.endswith('*'):who,w='cs_th',t[1:-1]
 else:who,w='cs_narrator',t
 expected.append((who,w.replace('\n',' ')))
extras=[('cs_narrator','Мы ещё не успели далеко уйти от развилки, когда мне в голову пришла очередная мысль.'),('cs_ls','А сегодня хотя бы понятно, зачем нужно отнести документы в администрацию.'),('cs_narrator','Мы поднялись на крыльцо административного корпуса.')]
extras += [('cs_narrator','По дороге к домику вожатой я ещё раз посмотрела на повязку.'),('cs_ls','Помочь можно и без подвигов. Начнём с чего-нибудь, для чего не нужны обе руки.'),('cs_da','Вот с этого и начни разговор.')]
actual=[]
for p in sorted((R/'days/day03/part05').glob('*_scene.rpy')):
 for l in p.read_text(encoding='utf8').splitlines():
  m=re.match(r'^\s+(cs_\w+) (".*")$',l)
  if m:actual.append((m[1],json.loads(m[2])))
assert Counter(actual)==Counter(expected)+Counter(extras),(Counter(expected)+Counter(extras)-Counter(actual),Counter(actual)-Counter(expected)-Counter(extras))
assert [x for x in actual if x not in extras]==expected
alltext='\n'.join(p.read_text(encoding='utf8') for p in list(R.glob('*.rpy'))+list((R/'days').rglob('*.rpy')))
for pattern in (r'^\s*label (\w+)',r'^default (\w+)\s*='):
 c=Counter(re.findall(pattern,alltext,re.M));assert not [x for x,n in c.items() if n>1]
flow=(R/'days/day03/part05/00_flow.rpy').read_text(encoding='utf8')
assert flow.count('    menu:')==1 and flow.count('$ cs_friend_sl += 1')==1
assert 'if not cs_sl_day3_awarded:' in flow
assert len(re.findall(r'\$ cs_friend_sl \+= 1',alltext))==3  # day 3 part 12 added a third, intentional Slavya reward
t=(R/'days/day03/part05/110_scene.rpy').read_text(encoding='utf8')
assert 'if cs_sl_poster_saved_day3 and not cs_sl_poster_collected_day3:' in t
assert '$ cs_day03_poster_location = "darya_folder"' in t
assert '$ cs_day03_documents_location = "administration"' in (R/'days/day03/part05/107_scene.rpy').read_text(encoding='utf8')
assert 'jump cs_day03_part06' in flow
assert all((R/'bg/admin_camp'/f).is_file() for f in ('ext_administration_day.png','int_administration_day.png'))
report=dict(status='PASS',manuscript_blocks=len(expected),implemented_blocks=len(actual),continuity_additions=extras,prior_sl_award='day02/00_flow.rpy: cs_day02_24, guarded by cs_sl_day2_awarded',reachable_sl_before=1,reachable_sl_after=2,poster='saved in78a; kept by Slavya until110 physical handoff; location=darya_folder; no new item if not saved or already collected',part04_glue='scene103 reduced to exterior establishing shot; 92 old ending blocks moved/replaced by104/112; old named entry points retained',administration='User supplied exterior and interior renamed, registered and used; no invented actor')
(R/'source/day03_part05_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('SOURCE_PASS',len(expected),'original +',len(extras),'continuity additions')
