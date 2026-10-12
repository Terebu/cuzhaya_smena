"""Keep full-source body baselines consistent with the newly calibrated sprite sizes."""
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
for path in (ROOT/'camp_resources.rpy',ROOT/'dasha_sprites.rpy',ROOT/'semen_sprites.rpy',ROOT/'house_resources.rpy',ROOT/'transforms.rpy',ROOT/'days/day01/resources.rpy'):
    text=path.read_text(encoding='utf8')
    def replace(m):
        name,body=m.group(1,2)
        if not any(w in name for w in ('darya','dasha','semen')):return m.group(0)
        value='1.35' if 'far' in name else '1.84' if 'close' in name else '1.60'
        return 'transform '+name+':\n'+re.sub(r'ypos [\d.]+','ypos '+value,body)
    text=re.sub(r'transform (\w+):\n((?:[ \t]+[^\n]*\n|\n)+)',replace,text)
    path.write_text(text,encoding='utf8')
