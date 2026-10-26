"""Keep dialogue resume addresses in the unchanged breakfast exit script."""
from pathlib import Path
import io,hashlib,json
from rpyc_audit import DataUnpickler,payload
R=Path(__file__).resolve().parent.parent
old=Path('D:/stean/release_chuzaya_smena/day03_part11_20261025_final')
rel=Path('days/day03/part03/95_scene.rpy')
assert (R/rel).read_bytes()==(old/'source_snapshot'/rel).read_bytes()
root=DataUnpickler(io.BytesIO(payload(old/'content/cs_scripts_5ea2d086'/rel.with_suffix('.rpyc'))),encoding='utf8',errors='replace').load()
stack=[root];seen=set();mapping={}
while stack:
 obj=stack.pop()
 if id(obj) in seen:continue
 seen.add(id(obj))
 if isinstance(obj,dict):stack.extend(obj.values())
 elif isinstance(obj,(tuple,list,set)):stack.extend(obj)
 elif hasattr(obj,'__dict__'):
  d=vars(obj);stack.extend(d.values())
  if type(obj).__name__=='Say' and isinstance(d.get('name'),tuple):mapping[d['name']]=d['linenumber']
p=R/'day03_location_audio.rpy';s=p.read_text(encoding='utf8').split('# Verified old breakfast-exit dialogue resume addresses.')[0]
s+='''# Verified old breakfast-exit dialogue resume addresses.
# Add aliases only for absent IDs in this byte-identical mod script.
init 40 python:
    cs_day03_audio_legacy_says = '''+repr(mapping)+'''
    cs_day03_audio_current_says = {}
    for _cs_audio_node in list(renpy.game.script.namemap.values()):
        if type(_cs_audio_node).__name__ == "Say" and str(getattr(_cs_audio_node,"filename","")).replace("\\\\","/").rstrip("c").endswith("cs_scripts_5ea2d086/days/day03/part03/95_scene.rpy"):
            cs_day03_audio_current_says[_cs_audio_node.linenumber] = _cs_audio_node
    for _cs_audio_old, _cs_audio_line in cs_day03_audio_legacy_says.items():
        if _cs_audio_old not in renpy.game.script.namemap and _cs_audio_line in cs_day03_audio_current_says:
            renpy.game.script.namemap[_cs_audio_old] = cs_day03_audio_current_says[_cs_audio_line]
'''
p.write_text(s,encoding='utf8')
(R/'source/day03_audio_save_compat.json').write_text(json.dumps(dict(status='PASS',source=rel.as_posix(),source_sha256=hashlib.sha256((R/rel).read_bytes()).hexdigest(),previous_release=str(old),dialogue_aliases=len(mapping)),indent=2),encoding='utf8')
print('BREAKFAST_EXIT_SAVE_ALIASES',len(mapping))
