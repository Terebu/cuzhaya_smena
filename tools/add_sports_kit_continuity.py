"""Keep the first-day editable transcript in sync with the new sports-kit line."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent.parent
anchor='Здесь можно хранить вещи. Постельное бельё уже должно быть приготовлено.'
line='На нижней полке лежат футболки и спортивные шорты для физкультуры. Если захотите позаниматься, берите.'
p=R/'source/day01_part06_dialogue.json';scenes=json.loads(p.read_text(encoding='utf8'))
for scene in scenes:
 blocks=scene['blocks']
 if any(b.get('text')==line for b in blocks):continue
 for i,b in enumerate(blocks):
  if b.get('text')==anchor:
   entry=dict(b);entry['text']=line;blocks.insert(i+1,entry);break
p.write_text(json.dumps(scenes,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'source/day01_part06.md';text=p.read_text(encoding='utf8')
if line not in text:text=text.replace(anchor,anchor+'\n\n**Славя:**\n— '+line)
p.write_text(text,encoding='utf8')
