"""Apply the explicitly attributed POV manuscript to the existing scene tree."""
import difflib
import json
import re

NAMES = {'Лена Соколова':'ls', 'Даша':'da', 'Семён':'sy', 'Женя':'mz',
         'Ольга Дмитриевна':'mt', 'Лена Тихонова':'un', 'Славя':'sl',
         'Алиса':'dv', 'Мику':'mi', 'Виола':'vi', 'Неизвестный голос':'voice',
         'Пионер':'d5_pioneer', 'Другой пионер':'d5_other_pioneer',
         'Повариха':'d5_cook', 'Девочка':'d5_girl', 'Ульяна':'d5_ulyana'}

def old_spoken(text):
    text = text.lstrip('—').strip()
    text = re.sub(r'\s*—\s*(?:спросил[аи]?|сказал[аи]?|ответил[аи]?|признал[асясь]+|объяснил[аи]?|добавил[аи]?|попросил[аи]?|уточнил[аи]?|предупредил[аи]?|пояснил[аи]?|согласил[асясь]+|заметил[аи]?|донеслось)[^—]*?(?:\.\s*—\s*|\.\s*$)', ' ', text).strip()
    return text.rstrip(', ') + ('.' if text.endswith(',') else '')

def key(text):
    if text.startswith('—'): text = old_spoken(text)
    elif text.split(':',1)[0] in NAMES: text = text.split(':',1)[1].strip()
    return ' '.join(re.findall(r'\w+', text.lower()))

def apply_pov(root,P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,ART,THOUGHTS):
    rows = json.loads((root/'source/day05/pov_paragraphs.json').read_text(encoding='utf-8'))
    new = [r['text'] for r in rows]
    oldkeys, newkeys = list(map(key,P)), list(map(key,new))
    mapping, starts = {}, {}
    for tag,a,b,c,d in difflib.SequenceMatcher(None,oldkeys,newkeys,autojunk=False).get_opcodes():
        if tag=='equal': mapping.update((i,c+i-a) for i in range(a,b))
        elif tag=='insert': starts[a]=c
        elif tag=='delete': mapping.update((i,c) for i in range(a,b))
        else:
            starts[a]=c
            previous=c
            for i in range(a,b):
                choices=[(difflib.SequenceMatcher(None,oldkeys[i],newkeys[j],autojunk=False).ratio(),j) for j in range(previous,d)]
                score,pos=max(choices,key=lambda v:(v[0],-v[1]))
                if score<0.25: pos=min(d-1,max(previous,c+(i-a)*(d-c)//max(1,b-a)))
                mapping[i]=pos
                previous=pos
    mapping[len(P)]=len(new)
    I=lambda i:mapping[i]
    L=lambda i:starts.get(i,I(i))
    for k,(end,parts) in B.items():
        assert P[k]==new[I(k)], ('POV branch drift',k,P[k],new[I(k)])
    for k,(end,parts) in M.items():
        assert P[k]==new[I(k)], ('POV menu drift',k)
        for title,lo,hi,actions in parts:
            assert P[title]==new[I(title)], ('POV option drift',title)
    B={I(k):(I(end),[(cond,L(lo),I(hi)) for cond,lo,hi in parts]) for k,(end,parts) in B.items()}
    M={I(k):(I(end),[(I(title),L(lo),I(hi),actions) for title,lo,hi,actions in parts]) for k,(end,parts) in M.items()}
    def commands(table):
        result={}
        for k,v in table.items(): result.setdefault(I(k),[]).extend(v)
        return result
    A=commands(A)
    before=commands(before)
    # New actions separate entering the room, opening the window and playing.
    assert new[829]=='Мику сыграла отрывок и ткнула в строчку.'
    before[829]=before.pop(823)
    # Stay inside through the last look at the dining tables.
    assert new[1130]=='Мы сдали посуду и вышли вместе.'
    before[1130]=before.pop(1129)
    assert new[1500].startswith('Лена Соколова: Запиши всё, что ещё помнишь.')
    before.setdefault(1500,[]).append('$ cs_d5_focus("sy")')
    SCENES=[(I(title),L(lo),I(hi),bg) for title,lo,hi,bg in SCENES]
    # Zhenya's new parting reply is still inside the library, before the walk.
    SCENES[8]=(*SCENES[8][:3],None)
    assert new[578]=='Мы с Дашей вышли проветриться и дошли до скамейки у площадки.'
    before[578]=['$ cs_d5_room("bg ext_playground_day")']
    art={r['index'] for r in rows if SCENES[0][1]<=r['index']<SCENES[-1][2] and r['style'] in ('Narrative','Dialogue')}
    dialogue={}
    for i in sorted(art):
        if rows[i]['style']!='Dialogue': continue
        name,text=new[i].split(':',1)
        dialogue[i]=(NAMES[name],text.strip())
    # The second lap is Dasha's reply, as the immediately preceding action says.
    assert new[94]=='Лена Соколова: Я всё-таки больше по прогулкам.'
    dialogue[94]=('da',dialogue[94][1])
    discrepancies=[]
    for i in sorted(ART):
        if not P[i].startswith('—'): continue
        j=I(i)
        if j in dialogue and oldkeys[i]==newkeys[j] and speakers.get(i,'ls')!=dialogue[j][0]:
            discrepancies.append(dict(old_index=i,new_index=j,old_speaker=speakers.get(i,'ls'),new_speaker=dialogue[j][0],text=new[j]))
    # Reapply only reviewed continuity fixes and the user's later costume rule.
    REPLACE={I(i):text for i,text in REPLACE.items()}
    assert all(rows[i]['style']=='Narrative' for i in REPLACE), ('POV continuity fix became speech',REPLACE)
    thoughts={I(i) for i in THOUGHTS if I(i) in art and rows[I(i)]['style']=='Narrative'}
    SKIP={I(i) for i in SKIP if I(i) not in art}
    data=dict(status='PASS',paragraph_map=mapping,literary_paragraphs=len(art),dialogue_paragraphs=len(dialogue),thought_paragraphs=sorted(thoughts),speaker_changes=discrepancies,editorial_speaker_corrections=[dict(index=94,speaker='da',reason='Dasha slows down and says she prefers walking')],staging={str(i):dict(text=new[i],commands=v) for i,v in before.items()})
    (root/'source/day05/pov_mapping.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    return new,B,M,A,SKIP,before,REPLACE,SCENES,{i:v[0] for i,v in dialogue.items()},art,thoughts,dialogue
