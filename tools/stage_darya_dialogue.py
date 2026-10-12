"""Offline staging based on Darya's story presence, independent of speaker/focus.
Run after chapter generators. Full PNGs, dialogue, audio and stable labels retained.
"""
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
SPRITE=re.compile(r'^\s*(?:show|hide) (?:cs_dasha(?:_winter|_pioneer|_full)?|cs_darya)(?:\s|$)')
SAY=re.compile(r'^\s+(cs_ls|cs_da|cs_mt|cs_sl|cs_sy|cs_th|cs_narrator) (".*")$')
MARKERS={
 'Я наклонилась ближе, чтобы идущая впереди вожатая нас не услышала.':'cs_check_darya_hold_pause',
 'Ты даже не спросила меня.':'cs_check_darya_housing_talk',
 'Вот. Демократическое голосование завершено единогласно.':'cs_check_darya_housing_hide',
 'То есть ты предполагаешь, что в лагере, который выглядит как советский лагерь восьмидесятых…':'cs_check_darya_reasoning',
 'Справедливо.':'cs_check_darya_smile',
 'Семён! Познакомься. У нас ещё две новенькие.':'cs_check_darya_semen_focus',
}
def emotion(text):
    t=text.lower()
    if t in ('нет.','лена.','не говори.','даже не начинай.','ты ужасно врёшь.','я вижу твой взгляд.','ты даже не спросила меня.'):return 'arms_crossed'
    if any(w in t for w in ('не уверена','непривыч','спокойнее','беспокоит','не должна','не спросила')):return 'worried'
    if any(w in t for w in ('справедливо','именно.','усмех','сме','разумеется','здравые мысли','хороший')):return 'smile'
    if t in ('что?','кто?','это тот самый?','тот самый семён?'):return 'surprised'
    if '?' in t or any(w in t for w in ('предполага','возможност','вариант','физичес','ошибку','знаешь')):return 'thinking'
    if any(w in t for w in ('не привыкай','продолжай','я просто','это преимущество')):return 'shrug'
    if any(w in t for w in ('ты могла','не видела','ты же','никто','меньше','мы здесь','слишком')):return 'serious'
    if len(t)>100:return 'explaining'
    return 'neutral'


report=[]
current=None
actors={}
for folder in ('days/prologue','days/day01'):
 for path in sorted((ROOT/folder).glob('[0-9][0-9]_*.rpy')):
    if path.name.startswith('00'):continue
    n=int(path.name[:2]); prologue=folder.endswith('prologue')
    visible=(n in (4,5,6)) if prologue else n!=2
    pioneer=not prologue and n>=14
    lines=[l for l in path.read_text(encoding='utf8').splitlines() if not SPRITE.match(l) and not l.strip().startswith(('# cs_darya_stage:', '# cs_darya_variety:')) and not re.match(r'\s+label cs_check_darya_',l)]
    output=[];changes=0
    for l in lines:
        t=l.strip();m=SAY.match(l)
        if t.startswith('scene '):
            current=None;actors={}
            if prologue: visible=n in (4,5,6) and not any(x in t for x in ('scene black','scene cs_sleep','scene cs_sunlight'))
            elif n==13: visible=False
            elif n==2: visible=False
            else:visible='scene bg ' in t
        am=re.match(r'show (sl|mt|dv|us|cs_semen) (.+?)(?: at | with |$)',t)
        if am:actors[am[1]]=am[2]
        hm=re.match(r'hide (sl|mt|dv|us|cs_semen)(?:\s|$)',t)
        if hm:actors.pop(hm[1],None)
        if m:
            who,text=m[1],json.loads(m[2])
            if prologue and n==3 and text=='Красные волосы.':visible=True
            if not prologue and n==2 and text=='Дарья вышла следом.':visible=True
            if not prologue and n==13 and text=='Вышла Дарья.':visible=True;pioneer=True
            # Only explicit departures remove a physically present companion.
            if re.search(r'Дарья (?:ушла|вышла из (?:комнаты|домика)|осталась (?:снаружи|в автобусе))',text):visible=False
            if visible:
                distance='far' if any('far' in a for a in actors.values()) or len(actors)>=2 else 'normal'
                pose=emotion(text) if who=='cs_da' else current[1] if current else 'neutral'
                if who=='cs_ls' and 'тебе очень идёт' in text.lower():pose='surprised'
                if pioneer:
                    desired=('pioneer',pose,distance)
                    command='show cs_darya '+pose+' pioneer '+distance+' at '+('cs_dasha_far_right' if distance=='far' else 'cs_day_dasha_right')
                else:
                    pose={'neutral':'neutral_alt','smile':'neutral_alt','surprised':'explaining','serious':'arms_crossed','interested':'thinking'}.get(pose,pose)
                    desired=('winter',pose,distance)
                    command='show cs_dasha_winter '+pose+' '+distance+' at '+('cs_dasha_seated' if prologue else 'cs_dasha_far_right' if distance=='far' else 'cs_day_dasha_right')
                if desired!=current:
                    # Switching costume also removes its old tag.
                    if current and current[0]!=desired[0]:output.append('    hide '+('cs_darya' if current[0]=='pioneer' else 'cs_dasha_winter'))
                    output+=['    # cs_darya_stage: present in story','    '+command+' with Dissolve(0.5)'];current=desired;changes+=1
            elif current:
                output+=['    # cs_darya_stage: absent in story','    hide '+('cs_darya' if current[0]=='pioneer' else 'cs_dasha_winter')+' with Dissolve(0.5)'];current=None;changes+=1
            if text in MARKERS:output.append('    label '+MARKERS[text]+':')
            if not prologue and n==13 and who=='cs_ls' and text=='Тебе очень идёт.':output.append('    label cs_check_darya_uniform_talk:')
        output.append(l)
    path.write_text('\n'.join(output)+'\n',encoding='utf8')
    report.append({'file':path.relative_to(ROOT).as_posix(),'stage_changes':changes})
(ROOT/'qa/darya_staging_manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print('Staged',len(report),'scenes by story presence;',sum(e['stage_changes'] for e in report),'reactions.')
# Keep the broader palette when the established rebuild workflow is used.
import runpy
runpy.run_path(str(ROOT/'tools/restage_mod.py'),run_name='__main__')
