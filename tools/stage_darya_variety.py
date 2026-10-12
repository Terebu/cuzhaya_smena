"""Expand chapter reactions before the camera stage, preserving costume and scale."""
import json
import re
from collections import Counter
from pathlib import Path
from darya_emotions import reaction,WINTER
ROOT=Path(__file__).resolve().parent.parent
SHOW=re.compile(r'^(\s*show )(cs_darya|cs_dasha_winter) ([a-z_]+)(.*)$')
SAY=re.compile(r'^\s+(cs_da|cs_narrator|cs_ls|cs_th|cs_sy|cs_sl|cs_mt|cs_dv|cs_us|cs_sh|cs_el) (".*")$')
report=[];current=None
for folder in ('days/prologue','days/day01'):
    for path in sorted((ROOT/folder).rglob('[0-9][0-9]_*.rpy'),key=lambda p:int(p.name[:2])):
        if path.name.startswith('00'):continue
        raw=path.read_text(encoding='utf8').splitlines();lines=[];skip=False
        for line in raw:
            if '# cs_focus_suppressed: ' in line:line=line.replace('# cs_focus_suppressed: ','')
            if '# cs_phone_suppressed: ' in line:line=line.replace('# cs_phone_suppressed: ','')
            if line.strip() in ('# cs_darya_variety: reaction','# cs_focus: camera','# cs_composition: regroup','# cs_phone_focus: camera','# cs_speaker: present'):skip=True;continue
            if skip:skip=False;continue
            lines.append(line)
        output=[];previous='';chapter=path.name[:2];gap=8
        for i,line in enumerate(lines):
            stripped=line.strip()
            # A newly shown bus background must not cover an already present companion.
            if re.match(r'show cs_bus_(city|winter)(\s|$)',stripped) and 'zorder' not in line:
                line=line.replace(' with ',' zorder -10 with ') if ' with ' in line else line+' zorder -10'
            if stripped.startswith('scene '):current=None
            if re.match(r'hide (cs_darya|cs_dasha_winter)(\s|$)',stripped):current=None
            m=SHOW.match(line)
            if m:
                tag,pose,tail=m.group(2,3,4)
                if pose in ('neutral','neutral_alt'):pose='shrug'
                line=m.group(1)+tag+' '+pose+tail
                current=(tag,pose,re.sub(r' with .*$', '',tail))
                gap=0
            say=SAY.match(line)
            if say:
                gap+=1
                speaker,text=say[1],json.loads(say[2])
                pose=reaction(text,speaker,previous,chapter) if current else None
                urgent=pose in ('surprise_hand','reaching')
                if pose and (gap>=4 or urgent) and (pose!='shrug' or gap>=8):
                    if current[0]=='cs_dasha_winter':pose=WINTER.get(pose,pose)
                    if pose!=current[1]:
                        indent=line[:len(line)-len(line.lstrip())]
                        output += [indent+'# cs_darya_variety: reaction',indent+'show '+current[0]+' '+pose+current[2]]
                        current=(current[0],pose,current[2])
                        gap=0
                previous=text
            output.append(line)
        path.write_text('\n'.join(output)+'\n',encoding='utf8')
        counts=Counter((m.group(2)+'/'+m.group(3)) for l in output if (m:=SHOW.match(l)))
        report.append({'file':path.relative_to(ROOT).as_posix(),'poses':dict(counts)})
(ROOT/'qa/darya_variety_manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Updated reactions in',len(report),'scenes; presence and scales preserved.')
