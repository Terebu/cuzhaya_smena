"""Explicitly retain the speaking original girl until her authored departure."""
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
for path in (ROOT/'days/day01').rglob('[0-9][0-9]_*.rpy'):
    if path.name.endswith('_scene.rpy'):continue
    raw=path.read_text(encoding='utf8').splitlines();lines=[];skip=False
    for line in raw:
        if line.strip()=='# cs_speaker: present':skip=True;continue
        if skip:skip=False;continue
        lines.append(line)
    last={};out=[]
    for line in lines:
        s=line.strip();indent=line[:len(line)-len(line.lstrip())]
        if s.startswith('scene '):last={}
        show=re.match(r'show (un|mz|cs_zhenya) ',s)
        if show:
            line=re.sub(r' with .*$', '',line)
            if 'zorder' not in line:line+=' zorder 10'
            last["mz" if show[1]=="cs_zhenya" else show[1]]=line.strip()
        voice=re.match(r'cs_(un|mz) ',s)
        if voice:
            tag=voice[1];command=last.get(tag,('show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10' if tag=='mz' else 'show un normal pioneer at cs_actor_left zorder 10'))
            out += [indent+'# cs_speaker: present',indent+command]
        out.append(line)
    path.write_text('\n'.join(out)+'\n',encoding='utf8')
