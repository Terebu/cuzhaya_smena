"""Measure actual full PNGs without changing them. Used by runtime scaling."""
import json
from pathlib import Path
from PIL import Image
root = Path(__file__).resolve().parent.parent
data = {}
for costume, folder, count in [('winter','winter',4)]:
    data[costume] = []
    for n in range(1,count+1):
        path = root/'sp'/folder/('%d.png'%n)
        im = Image.open(path)
        data[costume].append({'number':n,'path':'mods/chuzaya_smena/sp/'+folder+'/'+path.name,
                              'size':list(im.size),'bbox':list(im.getbbox())})
catalog = json.loads((root/'sp/new_sprite_catalog.json').read_text(encoding='utf8'))
def measure(entries):
    result = []
    for entry in entries:
        im = Image.open(root/entry['path'][len('mods/chuzaya_smena/'):])
        if im.mode != 'RGBA': raise ValueError('Expected transparent full PNG: '+entry['path'])
        result.append(dict(entry, size=list(im.size), bbox=list(im.getbbox())))
    return result
data['pioneer'] = measure(catalog['darya'])
data['winter'].extend(measure(catalog.get('winter', [])))
(root/'sp/semen_metadata.json').write_text(json.dumps(measure(catalog['semen']),ensure_ascii=False,indent=2),encoding='utf8')
(root/'sp/dasha_metadata.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print('Measured',sum(map(len,data.values())),'full PNGs.')
