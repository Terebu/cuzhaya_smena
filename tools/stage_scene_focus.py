"""Apply camera focus to complete thought passages, retaining physical presence separately."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
SAY=re.compile(r'^(\s*)(cs_\w+) (".*")$')
files=list((ROOT/'days/prologue').glob('[0-9][0-9]_*.rpy'))+list((ROOT/'days/day01').rglob('[0-9][0-9]_*.rpy'))
manifest=[];current=None;others=set()
for path in sorted(files,key=lambda p:(0 if 'prologue' in p.parts else 1,int(p.name[:2]),p.name)):
    if path.name.startswith('00'):continue
    number=int(path.name[:2])
    group_scene='prologue' not in path.parts and (7<=number<=27 or number in (29,31,33,34,35,36,37,38,43,44,46,47,48,54,55,56,57,58))
    quiet_scene='prologue' not in path.parts and number in (49,50,51,52,53)
    raw=path.read_text(encoding='utf8').splitlines();lines=[];skip=False
    for line in raw:
        if '# cs_focus_suppressed: ' in line:
            line=line.replace('# cs_focus_suppressed: ','')
        if line.strip()=='# cs_focus: camera':skip=True;continue
        if skip:skip=False;continue
        lines.append(line)
    # Camera focus preserves the positions chosen by the group composition stage.
    has_d=any(re.match(r'\s*show cs_(darya|dasha)',l) for l in lines)
    for i,line in enumerate(lines):
        lines[i]=line
    # Thought runs can contain narration, pauses and emotion cues. External dialogue ends them.
    thoughts=[];i=0
    while i<len(lines):
        m=SAY.match(lines[i])
        internal=bool(m and m[2]=='cs_narrator' and any(t in json.loads(m[3]) for t in ('Потому что вспомнила','На экране компьютера','Ещё пару часов назад я знала','На мгновение захотелось','А я вдруг подумала','Я вдруг подумала','Я мысленно')))
        if not m or (m[2]!='cs_th' and not internal and not(quiet_scene and m[2]=='cs_narrator')):i+=1;continue
        start=i;j=i;thought_count=0;chars=0;total=0;blocks=0
        while j<len(lines):
            b=SAY.match(lines[j]);s=lines[j].strip()
            if b and b[2] not in ('cs_th','cs_narrator'):break
            if s.startswith(('scene ','hide ','return','menu:','if ','call ')):break
            if b and b[2]=='cs_th':thought_count+=1;chars+=len(json.loads(b[3]))
            if b:total+=len(json.loads(b[3]));blocks+=1
            j+=1
        if internal and total>=160 and blocks>=3 or quiet_scene and blocks>=4 and total>=100 or thought_count>=4 and chars>=150 or thought_count>=3 and total>=500 or chars>=300 or blocks>=10 and total>=550:thoughts.append((start,j))
        i=max(i+1,j)
    starts={a:b for a,b in thoughts};ends={b for a,b in thoughts};hidden=False;out=[];events=[]
    for i,line in enumerate(lines):
        stripped=line.strip();indent=line[:len(line)-len(line.lstrip())]
        dialogue=SAY.match(line)
        if hidden and current and dialogue and dialogue[2] not in ('cs_narrator','cs_th'):
            out += [indent+'# cs_focus: camera',indent+current+' with Dissolve(0.25)'];hidden=False
        if stripped.startswith('scene '):current=None;hidden=False;others=set()
        actor=re.match(r'show (sl|mt|dv|us|sh|el|un|mz|cs_semen)\b',stripped)
        if actor:
            others.add(actor[1])
            if hidden and current:
                out += [indent+'# cs_focus: camera',indent+current+' with Dissolve(0.25)'];hidden=False
        gone=re.match(r'hide (sl|mt|dv|us|sh|el|un|mz|cs_semen)\b',stripped)
        if gone:others.discard(gone[1])
        if re.match(r'hide cs_(darya|dasha_winter)(\s|$)',stripped):current=None;hidden=False
        show=re.match(r'show (cs_darya|cs_dasha_winter) ',stripped)
        if show:
            current=re.sub(r' with .*$', '',stripped)
            if hidden:
                out.append(indent+'# cs_focus_suppressed: '+stripped)
                continue
        if i in starts and current and not hidden and not others and not group_scene:
            # An establishing shot should start without a brief show/hide flash.
            if not any(SAY.match(x) for x in out):
                out=[re.sub(r'^(\s*)(show (?:cs_darya|cs_dasha_winter) .*)$',r'\1# cs_focus_suppressed: \2',x) for x in out]
            out += [indent+'# cs_focus: camera',indent+'hide '+current.split()[1]+' with Dissolve(0.25)'];hidden=True;events.append(i+1)
        out.append(line)
    # If a thought closes the scene, keep her hidden until the next scene establishes focus.
    path.write_text('\n'.join(out)+'\n',encoding='utf8')
    manifest.append({'file':path.relative_to(ROOT).as_posix(),'thought_passages':events})
(ROOT/'qa/scene_focus_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Staged',sum(len(x['thought_passages']) for x in manifest),'long private passages; group companions remain visible.')
