"""Author the supplied part seven with explicit speaker assignments and local staging."""
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'days/day01/part07'
OUT.mkdir(exist_ok=True)
# Indexed assignments keep ambiguous, unattributed dialogue reviewable.
turns={31:'ALALUDULUDUAULDULALALALALAU AALUDDLLDLL'.replace(' ',''),32:'LDLDLDLDLDLDLDLDLDLLDL',33:'DLDLDLLDLE'}
names=['visitors','an_idea','clubs_path','engineers','calculator','forty_six_years','transistors','five_volts','future_in_pocket']
turns[34]='L E S L L D E S L S L E L S L E L E L S L D L D E'.replace(' ','')
turns[35]='E L D L D L S L S L E L E L S L E L E L E L S L S L S L L S L S L E L S L S L S L S L E L S'.replace(' ','')
turns[36]='D L S L S L E L E L S L S L D E L S L S L L E L E L L S L L E L E L S L S L S L E L S L S L E L L S L'.replace(' ','')
turns[37]='S L S L S L S L S L S L E S L S L S L S L S L L E L S L D L'.replace(' ','')
turns[38]='S L S L L S L E L L L L S E S L S L S L S L S L E L S'.replace(' ','')
turns[39]='E L E L E L E L E L E L S L S L E L E L L S L S L E L E L E L L E L S L D L D L D L D L L D L D L L'.replace(' ','')
who={'L':'cs_ls','D':'cs_da','A':'cs_dv','U':'cs_us','S':'cs_sh','E':'cs_el'}
src=(ROOT/'source/day01_part07.md').read_text(encoding='utf8')
sections=re.split(r'### Сцена (\d+)\. ([^\n]+)',src)
scenes=[]
for i in range(1,len(sections),3):
    n=int(sections[i]); blocks=[]; turn=0
    for p in re.split(r'\n\s*\n',sections[i+2].split('## Инструкция')[0]):
        p=p.strip()
        if not p or p=='---' or p.startswith('#'):continue
        if p.startswith('**['):
            blocks.append({'stage':p[3:p.rfind(']')]});continue
        speaker='cs_narrator'
        if p.startswith('—'):
            
            if turn>=len(turns[n]):raise ValueError((n,turn,len(turns[n])))
            speaker=who[turns[n][turn]];turn+=1
            # Remove only inline attribution between the two em dashes.
            p=p[1:].strip()
            p=re.sub(r',? — (?:произнесла|ответила|сказала|уточнила|поинтересовалась|удивилась|переспросила|возмутилась|спросил|добавил|представилась|согласилась|признала|возразил|негромко произнесла)[^—]*?\. — ','. ',p)
            p=re.sub(r',? — (?:произнесла|ответила|сказала|уточнила|поинтересовалась|удивилась|переспросила|возмутилась|спросил|добавил|представилась|согласилась|признала|возразил|негромко произнесла)[^—]*?\.$','.',p)
            p=re.sub(r' — Ульяна повернулась к Дарье\.$','',p)
            p=re.sub(r',? — (?:спокойно представилась|ответил|переспросил)[^—]*?\. — ','. ',p)
            p=re.sub(r',? — (?:спокойно представилась|ответил|переспросил)[^—]*?\.$','.',p)
            p=re.sub(r'([?!])\.',r'\1',p)
        elif p.startswith('*'):
            speaker='cs_th';p=p.strip('*')
        if n==31 and p=='Я открыла дверь.':continue # The door was opened at the end of scene 30.
        blocks.append({'who':speaker,'text':p})
    if turn!=len(turns[n]):raise ValueError((n,turn,len(turns[n])))
    scenes.append({'number':n,'title':sections[i+1],'blocks':blocks})
(ROOT/'source/day01_part07_dialogue.json').write_text(json.dumps(scenes,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def d(p='neutral',far=False):return 'show cs_darya '+p+' pioneer '+('far at cs_dasha_far_right' if far else 'normal at cs_day_dasha_right')+' with Dissolve(0.4)'
def bg(name,far=False):return ['scene '+name,d(far=far).replace(' with Dissolve(0.4)',''),'with Dissolve(1.0)']
for s in scenes:
    n=s['number']; lines=['# -*- coding: utf-8 -*-','label cs_day01_'+str(n)+':','$ save_name = '+json.dumps('Чужая смена — День 1: '+s['title'],ensure_ascii=False)]
    if n==31:lines += ['show dv normal pioneer far at left','show us grin pioneer far at cs_day_mt_center',d(far=True),'label cs_check_day01_part07_guests:']
    if n==32:lines += [d(),'label cs_check_day01_part07_idea:']
    if n==34:lines += ['show sh normal pioneer far at left','show el normal pioneer far at cs_day_mt_center',d(far=True),'with Dissolve(0.6)','label cs_check_day01_part07_engineers:']
    poses={};outside=False;guests=True
    for b in s['blocks']:
        if 'stage' in b:
            c=b['stage']
            if c.startswith('MUSIC:') and 'продолж' not in c:
                if 'fadeout' in c:lines += ['stop music fadeout 2.0']
                elif '`' in c:
                    track=c.split('`')[1];lines += ['$ renpy.music.set_volume(0.30,delay=1.0,channel="music")','play music "sound/music/'+track+'.ogg" fadeout 2.0 fadein 2.5']
            elif c.startswith('AMBIENCE:'):
                track='int_cabin_day' if n==31 else 'camp_center_day' if 'camp_center' in c else 'clubs_inside_day'
                lines += ['$ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")','if renpy.music.get_playing(channel="ambience") != "sound/ambiences/'+track+'.ogg":','    play ambience "sound/ambiences/'+track+'.ogg" fadeout 1.5 fadein 2.0']
            elif c.startswith('SFX:'):
                sound='close_door_1' if 'close_door' in c else 'knock_door7_polite' if 'knock' in c else 'open_door_clubs'
                lines += ['play sound "sound/sfx/'+sound+'.ogg"']
            elif c.startswith('SPRITES: Алиса') and 'hide' in c:
                lines+=['hide dv','hide us',d(),'with Dissolve(0.5)'];guests=False
            elif c.startswith('BG: `bg ext_houses'):lines+=bg('bg ext_houses_day')
            elif c.startswith('BG: `bg int_clubs') and 'dissolve' in c:lines+=bg('bg int_clubs_male_day',True)
            elif c.startswith('BG: `bg ext_clubs'):
                lines+=bg('bg ext_clubs_day');outside=True
            elif c.startswith('PAUSE:'):lines+=['pause '+c.split(':')[1].strip()]
            continue
        text=b['text'];speaker=b['who']
        if n==35 and text=='Экран не загорелся.':
            lines+=['stop music fadeout 2.0','label cs_check_day01_part07_silence:']
        if n==33 and text=='Мы свернули за один из домиков.':lines+=bg('cs_camp_path_day')
        if n==33 and text=='Через несколько минут показалось знакомое здание.':lines+=bg('bg ext_clubs_day')
        far=n==31 and guests or 34<=n<=39 and not outside
        if speaker in ('cs_da','cs_sh','cs_el','cs_dv','cs_us'):
            tag=speaker[3:];tag='cs_darya' if tag=='da' else tag
            pose=('thinking' if '?' in text else 'explaining' if len(text)>100 else 'neutral') if tag=='cs_darya' else ('surprise' if '?' in text else 'smile' if tag in ('el','dv') else 'normal')
            if tag=='us':pose='grin' if '?' in text else 'smile'
            if tag=='sh':pose='surprise' if text in ('Миллиарды?','Из какого?','Сколько?') else 'serious' if n in (35,36,38) else 'normal'
            if tag=='cs_darya' and n==38:pose='worried'
            if poses.get(tag)!=pose:
                lines += [d(pose,far) if tag=='cs_darya' else 'show '+tag+' '+pose+' pioneer far at '+('left' if tag in ('sh','dv') else 'cs_day_mt_center')+' with Dissolve(0.4)'];poses[tag]=pose
        if speaker=='cs_narrator' and 'Дарья' in text and any(w in text for w in ('рассме','засме','улыб')):lines+=[d('amused',far)]
        if speaker=='cs_narrator':
            for actor,tag in (('Электроник','el'),('Шурик','sh'),('Алиса','dv'),('Ульяна','us')):
                if actor not in text:continue
                pose='laugh' if any(w in text for w in ('рассме','засме')) else 'smile' if any(w in text for w in ('улыб','усмех')) else 'surprise' if 'удив' in text else None
                if tag=='us' and pose=='surprise':pose='surp1'
                if pose and poses.get(tag)!=pose:
                    lines+=['show '+tag+' '+pose+' pioneer far at '+('left' if tag in ('sh','dv') else 'cs_day_mt_center')+' with Dissolve(0.4)'];poses[tag]=pose
        if n==36 and text=='Тысяча девятьсот восьмидесятый.':lines+=['label cs_check_day01_part07_year:']
        if n==38 and text.startswith('Возможно, это единственная'):lines+=['label cs_check_day01_part07_home:']
        if n==39 and text=='Я вышла на крыльцо.':lines+=['label cs_check_day01_part07_exit:']
        lines += [speaker+' '+json.dumps(text,ensure_ascii=False)]
    lines+=['return']
    (OUT/(str(n)+'_'+names[n-31]+'.rpy')).write_text('\n'.join(l if l.startswith('#') or l.startswith('label cs_day01') else '    '+l for l in lines)+'\n',encoding='utf8')
print('Built scenes 31–39.')
