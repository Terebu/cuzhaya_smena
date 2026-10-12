"""Rename supplied day/sunset/night backgrounds and replace forest path cues everywhere."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
folder=ROOT/'bg/camp_street';report=[]
for suffix,time in [('22_29_44-1','day'),('22_29_45-2','sunset'),('22_29_46-3','night')]:
    name='Изображение ChatGPT 11 окт. 2026 г., '+suffix+'.png';dest=folder/('camp_path_'+time+'.png');old=folder/name
    if old.exists():old.rename(dest)
    report.append({'original':name,'renamed':dest.name,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(folder/'background_catalog.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for path in list((ROOT/'days').rglob('*.rpy'))+list((ROOT/'qa').glob('*.rpy'))+list((ROOT/'tools').glob('*.py')):
    if path.name==Path(__file__).name:continue
    text=path.read_text(encoding='utf8')
    for time in ('day','sunset','night'):
        text=text.replace('bg ext_path_'+time,'cs_camp_path_'+time)
    if path.suffix=='.rpy':
        text=re.sub(r'^(\s*)show (cs_camp_path_\w+)(?![^\n]*zorder)([^\n]*)$',r'\1hide bg\n\1show \2 zorder -10\3',text,flags=re.M)
    # Source BG identifiers are parsed separately by generators.
    if path.name.startswith('build_day01'):
        text=text.replace("bg = 'ext_path_day'", "bg = 'cs_camp_path_day'")
    path.write_text(text,encoding='utf8')
print('Camp path assets renamed; runtime and QA cues replaced.')
