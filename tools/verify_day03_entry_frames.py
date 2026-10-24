"""Check the clear top edge of the entry frames for the reproduced ghost."""
from pathlib import Path
import sys,json
from PIL import Image,ImageChops
r=Path(sys.argv[1]);ref=Image.open(r/'entry_normal.png').convert('RGB');box=(0,0,ref.width,80)
results=[]
for n in range(8):
 im=Image.open(r/('entry_%d.png'%n)).convert('RGB')
 diff=ImageChops.difference(im.crop(box),ref.crop(box));ok=diff.getbbox() is None
 results.append({'frame':n,'no_upper_ghost':ok})
assert all(x['no_upper_ghost'] for x in results),results
(r/'entry_visual_checks.json').write_text(json.dumps({'status':'PASS','frames':results},indent=2),encoding='utf8')
print('ENTRY_VISUAL_PASS: 8 frames, no stray sprite pixels above the correct head position')
