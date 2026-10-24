"""Independent paragraph-to-dialogue comparison against the supplied manuscript."""
from pathlib import Path
from collections import Counter
import re,json
R=Path(__file__).resolve().parent.parent
s=(R/'source/day03_part01.md').read_text(encoding='utf8')
# Part 2 replaces the former scene 82 in full.
s=s[s.index('### Сцена 74А.'):s.index('### Сцена 82.')]
expected=[]
for raw in s.split('\n\n'):
    text=raw.strip()
    if not text or text.startswith('#') or text.startswith('**[') or text=='---':continue
    if text.startswith('**'):
        name,words=text.split('\n',1)
        who='cs_sl' if 'Славя' in name else 'cs_da' if 'Дарья' in name else 'cs_ls'
        words=words.strip().lstrip('—–').strip()
    elif text.startswith('*') and text.endswith('*'):who,words='cs_th',text[1:-1]
    else:who,words='cs_narrator',text
    expected.append((who,' '.join(words.splitlines())))
files=[R/'days/day02/part10/74a_scene.rpy']+sorted((R/'days/day03/part01').glob('*_scene.rpy'))
actual=[]
for path in files:
    actual.extend((m[1],json.loads(m[2])) for line in path.read_text(encoding='utf8').splitlines() if (m:=re.match(r'^\s+(cs_\w+) (".*")$',line)))
errors=[]
if Counter(expected)!=Counter(actual):
    errors+=['Missing: '+repr(x) for x in (Counter(expected)-Counter(actual)).elements()]
    errors+=['Added: '+repr(x) for x in (Counter(actual)-Counter(expected)).elements()]
elif expected!=actual:
    errors.append('Manuscript dialogue order differs from generated scenes')
all_rpy=[p for p in R.rglob('*.rpy') if not any(x in p.relative_to(R).parts for x in ('tools','qa','source'))]
labels=Counter();defaults=Counter()
for p in all_rpy:
    text=p.read_text(encoding='utf8')
    labels.update(re.findall(r'^\s*label (\w+)',text,re.M))
    defaults.update(re.findall(r'^default (\w+)\s*=',text,re.M))
errors+=['Duplicate label: '+x for x,n in labels.items() if n>1]
errors+=['Duplicate default: '+x for x,n in defaults.items() if n>1]
text='\n'.join(p.read_text(encoding='utf8') for p in files)
assert text.count('play sound "sound/sfx/dinner_horn_processed.ogg"')==1
assert not re.search(r'cs_friend_\w+\s*\+=',text)
assert 'call cs_day02_74a' in (R/'days/day02/part10/74_scene.rpy').read_text(encoding='utf8')
assert 'jump cs_day03' in (R/'days/day02/part10/00_flow.rpy').read_text(encoding='utf8')
report=dict(status='FAIL' if errors else 'PASS',manuscript_blocks=len(expected),implemented_blocks=len(actual),files=len(files),errors=errors)
(R/'source/day03_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
