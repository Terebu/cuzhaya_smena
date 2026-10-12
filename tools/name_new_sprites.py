"""Give supplied PNGs readable names, retaining their exact bytes and provenance."""
import hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
catalog = {}
groups = [
    ('darya', 'sp/Dasha sprites/new', ['neutral','serious','surprised','explaining','worried','smile','thinking','wave','arms_crossed','shrug']),
    ('semen', 'sp/semen', ['neutral','relaxed','arms_crossed','wave','awkward','surprised','serious','confident','shy','thinking']),
]
old = ROOT/'sp/new_sprite_catalog.json'
previous = json.loads(old.read_text(encoding='utf8')) if old.exists() else {}
catalog.update(previous)
for person,folder,poses in groups:
    directory = ROOT/folder
    catalog[person] = list(previous.get(person,[]))
    for number,pose in enumerate(poses,1):
        named = directory/(person+'_pioneer_'+pose+'.png')
        if named.exists():
            origin = previous[person][number-1]['original_name']
        else:
            matches = [p for p in directory.glob('*.png') if re.search(r'-%d\.png$'%number,p.name)]
            if len(matches)!=1: raise ValueError((person,number,matches))
            origin = matches[0].name
            matches[0].rename(named)
        entry = {'number':number,'pose':pose,'path':'mods/chuzaya_smena/'+named.relative_to(ROOT).as_posix(),
                               'original_name':origin,'sha256':hashlib.sha256(named.read_bytes()).hexdigest()}
        if len(catalog[person]) >= number: catalog[person][number-1] = entry
        else: catalog[person].append(entry)
old.write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
print('Named 20 full PNGs; hashes and original names saved in sp/new_sprite_catalog.json.')
