"""Keep Darya off-screen throughout the Instagram gallery, with one exit and return."""
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
current=None
for path in sorted((ROOT/'days/prologue').glob('[0-9][0-9]_*.rpy')):
    raw=path.read_text(encoding='utf8').splitlines();lines=[];skip=False
    for line in raw:
        if '# cs_phone_suppressed: ' in line:line=line.replace('# cs_phone_suppressed: ','')
        if line.strip()=='# cs_phone_focus: camera':skip=True;continue
        if skip:skip=False;continue
        lines.append(line)
    out=[];gallery=False
    for line in lines:
        s=line.strip();indent=line[:len(line)-len(line.lstrip())]
        if s.startswith('scene '):current=None
        if re.match(r'show (cs_darya|cs_dasha_winter) ',s):
            current=re.sub(r' with .*$', '',s)
            if gallery:
                out.append(indent+'# cs_phone_suppressed: '+s);continue
        if re.match(r'hide (cs_darya|cs_dasha_winter)\b',s):current=None
        if s.startswith('show screen cs_instagram_post') and not gallery:
            gallery=True
            if current:out += [indent+'# cs_phone_focus: camera',indent+'hide '+current.split()[1]+' with Dissolve(0.25)']
        out.append(line)
        if s.startswith('hide screen cs_instagram_post') and gallery:
            gallery=False
            if current:out += [indent+'# cs_phone_focus: camera',indent+current]
    path.write_text('\n'.join(out)+'\n',encoding='utf8')
print('Instagram gallery framed with one companion exit and return.')
