"""Real PNG-to-registration inventory, including virtual distances and positions."""
from pathlib import Path
import json,re,csv,hashlib
from PIL import Image
R=Path(__file__).resolve().parent.parent
scripts=[p for p in (R/'days').rglob('*.rpy')]
shows='\n'.join(p.read_text(encoding='utf8') for p in scripts)
metadata=json.loads((R/'sp/dasha_metadata.json').read_text(encoding='utf8'))
groups=[('darya_pioneer','cs_darya',metadata['pioneer'],1560),('darya_winter','cs_dasha_winter',metadata['winter'],1560),('semen','cs_semen',json.loads((R/'sp/semen_metadata.json').read_text(encoding='utf8')),1580),('zhenya','cs_zhenya',json.loads((R/'sp/zhenya/metadata.json').read_text(encoding='utf8')),1500)]
if (R/'sp/viola/metadata.json').exists():groups.append(('viola','cs',json.loads((R/'sp/viola/metadata.json').read_text(encoding='utf8')),1560))
rows=[];overflow=[];known=set()
for costume,tag,entries,height in groups:
 for entry in entries:
  relative=entry['path'].removeprefix('mods/chuzaya_smena/');known.add(relative);png=R/relative;size=Image.open(png).size
  pose=entry.get('pose','neutral')
  if costume=='darya_winter':pose={1:'neutral',2:'smile',3:'interested',4:'sleep'}.get(entry['number'],pose)
  for distance,ratio in [('far',.82),('normal',1.),('close',1.22)]:
   name=('cs custom '+pose+' medical' if costume=='viola' else tag+' '+pose+('' if costume=='darya_winter' else ' pioneer'))+' '+distance
   positions=sorted(set(re.findall(r'\bshow '+re.escape(name)+r' at (\w+)',shows)))
   scale=height*ratio/(entry['bbox'][3]-entry['bbox'][1]);width=(entry['bbox'][2]-entry['bbox'][0])*scale
   if width>1000*ratio:overflow.append(dict(path=relative,distance=distance,width=width,canvas_width=1000*ratio))
   effective=relative
   if costume=='darya_pioneer' and pose=='smile':effective=next(e['path'].removeprefix('mods/chuzaya_smena/') for e in entries if e['pose']=='surprised')
   rows.append(dict(path=relative,registered_name=name,tag=tag,pose=pose,distance=distance,factor=round(scale,5),visible_height=height*ratio,canvas=[int(1000*ratio),int(1600*ratio)],positions=positions,source_size=list(size),effective_png=effective,sha256=hashlib.sha256(png.read_bytes()).hexdigest()))
orphans=sorted(p.relative_to(R).as_posix() for p in (R/'sp').rglob('*.png') if p.relative_to(R).as_posix() not in known)
result=dict(rows=rows,unregistered_pngs=orphans,canvas_overflow=overflow,lena_sokolova='POV; no standalone sprite used',aliases='Existing numeric/legacy aliases kept for saved scripts; all current camp Darya shows use cs_darya, winter uses cs_dasha_winter')
(R/'source/custom_sprite_inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
with (R/'source/custom_sprite_inventory.csv').open('w',encoding='utf-8-sig',newline='') as file:
 writer=csv.DictWriter(file,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print('Inventory:',len(rows),'registered distances;',len(orphans),'unused PNGs;',len(overflow),'canvas overflows')
if overflow:print(json.dumps(overflow[:8],ensure_ascii=False))
