from pathlib import Path
from PIL import Image, ImageDraw
import sys,json
root=Path(sys.argv[1]);prefix=sys.argv[2];files=sorted(root.glob(prefix+'*.png'))
per_page=int(sys.argv[3]) if len(sys.argv)>3 else 32
columns=8 if per_page==64 else 4
width,height=(256,144) if per_page==64 else (320,180)
row_height=height+24
out=root/(prefix.rstrip('_')+'_contacts');out.mkdir(exist_ok=True)
index=[]
for start in range(0,len(files),per_page):
 batch=files[start:start+per_page];sheet=Image.new('RGB',(columns*width,row_height*((len(batch)+columns-1)//columns)),'#202020');draw=ImageDraw.Draw(sheet)
 for n,path in enumerate(batch):
  x,y=(n%columns)*width,(n//columns)*row_height
  with Image.open(path) as im:sheet.paste(im.resize((width,height)),(x,y))
  draw.text((x+3,y+height+2),path.stem.removeprefix(prefix),fill='white')
 target=out/('%02d.png'%(start//per_page+1));sheet.save(target)
 index.append(dict(sheet=target.name,frames=[p.name for p in batch]))
(out/'index.json').write_text(json.dumps(index,indent=2),encoding='utf8')
print(out, len(files),'frames /',len(index),'sheets')
