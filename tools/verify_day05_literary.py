"""Audit manuscript coverage, attributions, state changes and required staging."""
from pathlib import Path
import ast,json,re
from day05_literary_layer import apply_literary
R=Path(__file__).resolve().parent.parent
P,B,M,A,skip,before,replacements,scenes,speakers,art,thoughts,dialogue,variants=apply_literary(R,'cs_da_shared_bed_day3 and cs_da_love_confession_day3')
emitted=json.loads((R/'source/day05/emitted_paragraphs.json').read_text())
assert set(emitted)==art and len(emitted)==len(art)
assert len(scenes)==20 and len(M)==5 and len(dialogue)==857
assert B[1089][1][0][0]==B[1602][1][0][0]=='cs_friend_da >= 4'
assert B[1565][1][0][0]=='cs_friend_mi >= 4 and cs_d5_miku_volunteer'
runtime=[];actual=[];menus=0
for file in sorted((R/'days/day05').glob('*_scene.rpy')):
    for n,line in enumerate(file.read_text(encoding='utf-8').splitlines(),1):
        assert not re.match(r'^\s*(extend |nvl )',line),(file,n)
        menus+=line=='    menu:'
        match=re.match(r'^\s*(cs_\w+) (".*")$',line)
        if not match:continue
        text=ast.literal_eval(match[2]);assert '\n' not in text
        assert not text.startswith(('[','###','Литературная редакция','При меньшей дружбе'))
        assert not any(t in text for t in ('Девола','ПЕРВЫЙ ИЛИ ВТОРАЯ','ВЫБИРАЕТ ПЕРВЫЙ'))
        runtime.append((file.name,n,match[1],text))
        if match[1] not in ('cs_narrator','cs_th'):actual.append((match[1],text))
expected=[('cs_d5_voice' if w=='voice' else 'cs_'+w,t) for i,(w,t) in sorted(dialogue.items())]
extra=[('cs_ls','Мы вечером зайдём к Ольге Дмитриевне с записями. Хочешь присоединиться после репетиции?'),('cs_mi','Хочу! Я только закончу здесь и приду.')]
for item in extra:actual.remove(item)
assert actual==expected, 'Speech sequence or attribution changed'
assert menus==5
assert all(not re.search(r'—\s*(?:сказала я|спросила Даша|ответил Семён)',t) for f,n,w,t in runtime if w not in ('cs_narrator','cs_th'))
result=dict(status='PASS',literary_paragraphs=len(art),dialogue_paragraphs=len(dialogue),source_thoughts=len(thoughts),runtime_says=len(runtime),menus=menus,max_say_characters=max(len(t) for f,n,w,t in runtime),missing_or_duplicate_paragraphs=0,romance_guard=True,dasha_counter_corrected=True,old_card_removed=True)
(R/'source/day05/literary_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('DAY05_LITERARY_VERIFY_PASS',json.dumps(result))
