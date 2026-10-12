"""Independent checks for manuscript completeness and shipped asset references."""
import json
import re
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent.parent
errors = []
source = (root/'source/prologue.md').read_text(encoding='utf-8-sig')
expected = []
for paragraph in re.split(r'\n\s*\n', source):
    p = paragraph.strip()
    if not p or p.startswith('#') or p == '---' or p.startswith('**['):
        continue
    if p.startswith('—'): p = p[1:].strip()
    if p.startswith('*') and not p.startswith('**'): p = p[1:-1]
    p = re.sub(r'\*\*(.*?)\*\*', r'{b}\1{/b}', p)
    expected.append(p)

actual = []
counts = []
for script in sorted((root/'days/prologue').glob('*.rpy')):
    blocks = re.findall(r'^\s+cs_(?:ls|da|th|narrator) (".*")$', script.read_text(encoding='utf8'), re.M)
    actual.extend(json.loads(b) for b in blocks)
    counts.append({'file':script.name,'blocks':len(blocks)})
if actual != expected:
    errors.append('Source dialogue differs: %d vs %d blocks' % (len(expected),len(actual)))
    for i,(a,b) in enumerate(zip(expected,actual)):
        if a!=b: errors.append('First difference at block %d: %r != %r' % (i,a,b));break

archive = set((root/'qa/inventory/asset_index.txt').read_text(encoding='utf8').splitlines())
scripts = [p for p in root.rglob('*.rpy') if 'qa' not in p.parts]
checked = set()
for p in scripts:
    if re.search(r"андроид|NieR|Девола|существовала только в вымышленном мире", p.read_text(encoding="utf8"), re.I):
        errors.append("Nonhuman Darya reference: " + str(p))
for p in scripts:
    for asset in re.findall(r'"((?:images/|sound/|fonts/|mods/chuzaya_smena/)[^"\n]+\.(?:jpg|png|ogg|mp3|ttf))"',p.read_text(encoding='utf8')):
        checked.add(asset)
        if asset.startswith('mods/chuzaya_smena/'):
            exists=(root/asset[len('mods/chuzaya_smena/'):]).is_file()
        else: exists=asset in archive or (root.parent.parent/asset).is_file()
        if not exists: errors.append('Missing asset: '+asset)
day_source = (root/'source/day01_staged.md').read_text(encoding='utf-8-sig')
day_source = day_source[day_source.index('### Сцена 1.'):day_source.index('## Указания для Codex')]
day_expected = []
for p in re.split(r'\n\s*\n', day_source):
    p = p.strip()
    if not p or p.startswith('#') or p.startswith('**[') or p == '---': continue
    speaker = re.match(r'\*\*(Лена|Дарья|Славя):\*\*\\?\s*\n—\s*(.*)',p,re.S)
    if speaker: p = speaker.group(2).strip()
    if p.startswith('—'): p = p[1:].strip()
    if p.startswith('*') and not p.startswith('**'): p = p[1:-1]
    day_expected.append(re.sub(r'\*\*(.*?)\*\*', r'{b}\1{/b}', p))
day_actual = []
for p in sorted((root/'days/day01').rglob('[0-9][0-9]_*.rpy'), key=lambda p:(int(p.name[:2]),bool(re.match(r'\d\d_[ab]_',p.name)),p.name)):
    day_actual.extend(json.loads(b) for b in re.findall(r'^\s+cs_(?:ls|da|sl|mt|sy|dv|us|sh|el|un|mz|th|narrator) (".*")$',p.read_text(encoding='utf8'),re.M))
part02_source = (root/'source/day01_part02.md').read_text(encoding='utf-8-sig')
part02_source = part02_source[part02_source.index('### Сцена 7.'):part02_source.index('## 3. Что использовать')]
part02_expected = []
for p in re.split(r'\n\s*\n',part02_source):
    p = p.strip()
    if not p or p.startswith('#') or p.startswith('**[') or p == '---': continue
    speaker = re.match(r'\*\*(Лена|Дарья|Славя|Ольга Дмитриевна)(?: \([^)]*\))?:\*\*\\?\s*\n—\s*(.*)',p,re.S)
    if speaker: p = speaker.group(2).strip()
    if p.startswith('*') and not p.startswith('**'): p = p[1:-1]
    part02_expected.append(re.sub(r'\*\*(.*?)\*\*',r'{b}\1{/b}',p))
day_expected.extend(part02_expected)
part03_source = (root/'source/day01_part03.md').read_text(encoding='utf-8-sig')
part03_source = part03_source[part03_source.index('### Сцена 10.'):part03_source.index('## Техническое задание')]
part03_expected = []
for p in re.split(r'\n\s*\n',part03_source):
    p = p.strip()
    if not p or p.startswith('#') or p.startswith('**[') or p == '---': continue
    speaker = re.match(r'\*\*(Лена|Дарья|Славя|Ольга Дмитриевна)(?: \([^)]*\))?:\*\*\\?\s*\n—\s*(.*)',p,re.S)
    if speaker: p = speaker.group(2).strip()
    if p.startswith('*') and not p.startswith('**'): p = p[1:-1]
    part03_expected.append(re.sub(r'\*\*(.*?)\*\*',r'{b}\1{/b}',p))
day_expected.extend(part03_expected)
part04_source = (root/'source/day01_part04.md').read_text(encoding='utf-8-sig')
part04_source = part04_source[part04_source.index('### Сцена 15.'):part04_source.index('## Инструкция Codex')]
part04_expected = []
for p in re.split(r'\n\s*\n',part04_source):
    p = p.strip()
    if not p or p.startswith('#') or p.startswith('**[') or p == '---': continue
    speaker = re.match(r'\*\*(Лена|Дарья|Славя|Ольга Дмитриевна|Семён)(?: \([^)]*\))?:\*\*\\?\s*\n—\s*(.*)',p,re.S)
    if speaker: p = speaker.group(2).strip()
    if p.startswith('*') and not p.startswith('**'): p = p[1:-1]
    part04_expected.append(re.sub(r'\*\*(.*?)\*\*',r'{b}\1{/b}',p))
day_expected.extend(part04_expected)
part05_expected=[]
part05_source=(root/'source/day01_part05.md').read_text(encoding='utf8')
for p in re.split(r'\n\s*\n',part05_source):
    p=p.strip()
    if not p or p.startswith('#'):continue
    m=re.match(r'\*\*[^\n]+:\*\*\s*\n—\s*(.*)',p,re.S)
    if m:p=m[1]
    elif p.startswith('*'):p=p.strip('*')
    part05_expected.append(p)
day_expected.extend(part05_expected)
part06_expected=[b['text'] for s in json.loads((root/'source/day01_part06_dialogue.json').read_text(encoding='utf8')) for b in s['blocks'] if 'text' in b]
day_expected.extend(part06_expected)
part07_expected=[b['text'] for s in json.loads((root/'source/day01_part07_dialogue.json').read_text(encoding='utf8')) for b in s['blocks'] if 'text' in b]
day_expected.extend(part07_expected)
part08_expected=[b['text'] for s in json.loads((root/'source/day01_part08_dialogue.json').read_text(encoding='utf8')) for b in s['blocks'] if 'text' in b]
day_expected.extend(part08_expected)
part09_expected=[b['text'] for s in json.loads((root/'source/day01_part09_dialogue.json').read_text(encoding='utf8')) for b in s['blocks'] if 'text' in b]
day_expected.extend(part09_expected)
part10_expected=[b['text'] for s in json.loads((root/'source/day01_part10_dialogue.json').read_text(encoding='utf8')) for b in s['blocks'] if 'text' in b]
day_expected.extend(part10_expected)
if day_actual != day_expected: errors.append('Day 1 differs from the staged manuscript')
metadata = json.loads((root/'sp/dasha_metadata.json').read_text(encoding='utf8'))
metadata['semen'] = json.loads((root/'sp/semen_metadata.json').read_text(encoding='utf8'))
for entries in metadata.values():
    for entry in entries:
        im = Image.open(root/entry['path'][len('mods/chuzaya_smena/'):])
        if im.mode != 'RGBA' or list(im.size) != entry['size'] or list(im.getbbox()) != entry['bbox']:
            errors.append('Sprite metadata must be remeasured: '+entry['path'])
import hashlib
for entries in json.loads((root/'sp/new_sprite_catalog.json').read_text(encoding='utf8')).values():
    for entry in entries:
        content = (root/entry['path'][len('mods/chuzaya_smena/'):]).read_bytes()
        if hashlib.sha256(content).hexdigest() != entry['sha256']: errors.append('Sprite bytes changed: '+entry['path'])
        if entry['path'] not in {e['path'] for group in metadata.values() for e in group}: errors.append('New sprite not registered: '+entry['path'])
lint=(root/'qa/lint.txt').read_text(encoding='utf8',errors='replace')
if re.search(r'^game/mods/chuzaya_smena/',lint,re.M): errors.append('Mod-specific lint diagnostics found')

result={'status':'FAIL' if errors else 'PASS','manuscript_blocks':len(expected),'implemented_blocks':len(actual),
        'day01_source_blocks':len(day_expected),'day01_implemented_blocks':len(day_actual),
        'day01_part02_blocks':len(part02_expected),
        'day01_part03_blocks':len(part03_expected),
        'day01_part04_blocks':len(part04_expected),
        'day01_part05_blocks':len(part05_expected),
        'day01_part06_blocks':len(part06_expected),
        'day01_part07_blocks':len(part07_expected),
        'day01_part08_blocks':len(part08_expected),
        'day01_part09_blocks':len(part09_expected),
        'day01_part10_blocks':len(part10_expected),
        'scenes':counts,'literal_asset_references_checked':len(checked),'errors':errors}
(root/'qa/static_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
