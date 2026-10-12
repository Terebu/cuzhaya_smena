"""Stage physical groups before inner-monologue focus; avoid overlap and per-line motion."""
import re,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
ACTORS={'sl','mt','dv','us','sh','el','un','mz','cs_semen'}
SHOW=re.compile(r'^(\s*)show (\w+) (.*)$')
others={};actor_commands={};darya=None;report=[]
def position(command):
    if re.search(r'at (?:right|\w*right)\b',command):return 'right'
    if re.search(r'at (?:left|\w*left)\b',command):return 'left'
    return 'center'
def arrange(command):
    distance='far' if ' far ' in command else 'close' if ' close ' in command else 'normal'
    if len(others)>=2:
        side='center';distance='far'
    elif others:side='left' if next(iter(others.values()))=='right' else 'right'
    else:side='center'
    if len(others)>=2:
        command=re.sub(r'\b(normal|close)\b','far',command)
    transform='cs_darya_'+distance+'_'+side
    command=re.sub(r' at \w+',' at '+transform,command)
    if ' at ' not in command:command+=' at '+transform
    return command
files=list((ROOT/'days/prologue').glob('[0-9][0-9]_*.rpy'))+list((ROOT/'days/day01').rglob('[0-9][0-9]_*.rpy'))
for path in sorted(files,key=lambda p:(0 if 'prologue' in p.parts else 1,int(p.name[:2]),p.name)):
    if path.name.startswith('00'):continue
    raw=path.read_text(encoding='utf8').splitlines();lines=[];skip=False
    for line in raw:
        if line.strip()=='# cs_composition: regroup':skip=True;continue
        if skip:skip=False;continue
        lines.append(line)
    out=[];events=[];scene_pending=False
    for line in lines:
        stripped=line.strip();indent=line[:len(line)-len(line.lstrip())];changed=False
        if stripped.startswith('scene '):others={};actor_commands={};darya=None;scene_pending=True
        if re.match(r'cs_\w+ [u]?"',stripped):scene_pending=False
        # Distance or group changes during a conversation must not crossfade whole bodies.
        if re.match(r'with (?:Dissolve\(|dissolve)',stripped) and not scene_pending and darya:
            line=indent+'with None'
        m=SHOW.match(line)
        if m and m[2] in ('cs_darya','cs_dasha_winter'):
            command=arrange(re.sub(r' with .*$', '',stripped));line=indent+command
            darya=re.sub(r' with .*$', '',command)
        elif m and m[2] in ACTORS:
            tag=m[2];side=position(stripped)
            occupied={v for k,v in others.items() if k!=tag}
            if tag in others:side=others[tag]
            elif side=='center' or side in occupied:side='right' if 'left' in occupied else 'left'
            if tag not in others or others[tag]!=side:changed=True
            clean=re.sub(r' with .*$', '',stripped)
            transform=('cs_semen_'+('far' if ' far ' in clean else 'normal')+'_'+side) if tag=='cs_semen' else ('cs_actor_far_'+side if len(others)>=2 and ' far' in clean else 'cs_actor_right' if side=='right' else 'cs_actor_left')
            clean=re.sub(r' at \w+',' at '+transform,clean)
            if ' at ' not in clean:clean+=' at '+transform
            line=indent+clean
            actor_commands[tag]=clean
            others[tag]=side
        hide=re.match(r'hide (\w+)\b',stripped)
        if hide:
            if hide[1] in ('cs_darya','cs_dasha_winter'):darya=None
            if hide[1] in others:others.pop(hide[1]);actor_commands.pop(hide[1],None);changed=True
        out.append(line)
        if changed and len(others)>=2:
            for tag,command in list(actor_commands.items()):
                if tag=='cs_semen' or ' far' not in command:continue
                command=re.sub(r' at \w+',' at cs_actor_far_'+others[tag],command)
                if command!=actor_commands[tag]:
                    out += [indent+'# cs_composition: regroup',indent+command];actor_commands[tag]=command
        if changed and darya:
            command=arrange(darya)
            if command!=darya:
                out += [indent+'# cs_composition: regroup',indent+command];darya=command;events.append(len(out))
    path.write_text('\n'.join(out)+'\n',encoding='utf8')
    report.append({'file':path.relative_to(ROOT).as_posix(),'group_changes':events})
(ROOT/'qa/composition_manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Staged companion positions by group size in',len(report),'scenes.')
