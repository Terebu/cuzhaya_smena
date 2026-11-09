"""Preserve the author's ADV paragraph boundaries over the reviewed Day 5 tree."""
import difflib,json,re

def apply_adv(root,P,B,M,A,SKIP,before,REPLACE,SCENES,speakers):
    path=root/'source/day05/adv_paragraphs.json'
    if not path.is_file():
        return P,B,M,A,SKIP,before,REPLACE,SCENES,speakers,None,set()
    rows=json.loads(path.read_text(encoding='utf-8'))
    new=[r['text'] for r in rows]
    mapping={};starts={}
    for tag,a,b,c,d in difflib.SequenceMatcher(None,P,new,autojunk=False).get_opcodes():
        if tag=='equal':mapping.update((i,c+i-a) for i in range(a,b))
        elif tag=='insert':starts[a]=c
        elif tag=='delete':mapping.update((i,c) for i in range(a,b))
        else:
            previous=c
            for i in range(a,b):
                tokens=re.findall(r'\w+',P[i].lower())
                choices=[]
                for j in range(previous,d):
                    nt=re.findall(r'\w+',new[j].lower());prefix=0
                    for left,right in zip(tokens,nt):
                        if left!=right:break
                        prefix+=1
                    if prefix>=2:choices.append((prefix,j))
                if choices:
                    best=max(score for score,j in choices)
                    pos=min(j for score,j in choices if score==best)
                else:pos=min(d-1,max(previous,c+(i-a)*(d-c)//max(1,b-a)))
                mapping[i]=pos;previous=pos
    mapping[len(P)]=len(new)
    I=lambda i:mapping[i]
    L=lambda i:starts.get(i,I(i))
    for k,(_,parts) in B.items():assert P[k]==new[I(k)],('ADV branch drift',k,P[k],new[I(k)])
    for k,(_,parts) in M.items():
        assert P[k]==new[I(k)],('ADV menu drift',k)
        for title,lo,hi,actions in parts:assert P[title]==new[I(title)],('ADV option drift',title)
    B={I(k):(I(end),[(condition,I(lo),I(hi)) for condition,lo,hi in parts]) for k,(end,parts) in B.items()}
    M={I(k):(I(end),[(I(title),I(lo),I(hi),actions) for title,lo,hi,actions in parts]) for k,(end,parts) in M.items()}
    A={I(k):v for k,v in A.items()}
    before={I(k):v for k,v in before.items()}
    SCENES=[(I(title),L(lo),I(hi),bg) for title,lo,hi,bg in SCENES]
    speakers={I(k):v for k,v in speakers.items()}
    for k in speakers:assert new[k].startswith('—'),('ADV speaker drift',k,new[k])
    # The new document is authoritative for all prose boundaries. Reapply only
    # continuity corrections and the author's later costume clarification.
    REPLACE={
        78:'Через несколько минут я справилась с галстуком, а Даша переоделась в спортивную форму.',
        79:'Даша поправила футболку и посмотрела на мои кеды.',
        110:'Локоть, с которого вчера сняли повязку, напомнил о себе ещё при разминке.',
        262:'Копии записей оставила в сумке: не хотелось подсовывать ответ вместе с вопросом.',
        277:'Я достала свои записи.',
        278:'Ольга Дмитриевна разложила фотографии и список 1971 года: папку она уже забрала из запертого библиотечного ящика. Недатированный снимок всё это время хранился у неё.',
        719:'Мы как раз ждали, пока Тихонова сдаст посуду.',
        939:'Когда он убрал бумагу, я перестала следить за его руками. Хотелось хотя бы перестать проверять каждое его движение.',
    }
    # Every literary paragraph, including the card's three lines, gets a say.
    body_end=SCENES[-1][2]
    art={r['index'] for r in rows if SCENES[0][1]<=r['index']<body_end and r['style'] in ('Narrative','Dialogue')}
    SKIP={I(k) for k in SKIP if I(k) not in art}
    for i,commands in before.items():
        expanded=[]
        for command in commands:
            if command.startswith('cs_narrator "После умывальников мы ненадолго вернулись в домик.'):
                expanded+=['cs_narrator "Семён подождал у дорожки, пока мы с Дашей ненадолго зашли в домик."','cs_narrator "Даша переоделась в пионерскую форму, а я поправила галстук."']
            else:expanded.append(command)
        before[i]=expanded
    # Clear interior comments use the existing thought character, never speech.
    thoughts={69,86,128,267,594,815,864}
    assert thoughts<=art
    data=dict(status='PASS',paragraph_map=mapping,literary_paragraphs=len(art),dialogue_paragraphs=sum(rows[i]['style']=='Dialogue' for i in art),thought_paragraphs=sorted(thoughts))
    (root/'source/day05/adv_mapping.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    return new,B,M,A,SKIP,before,REPLACE,SCENES,speakers,art,thoughts
