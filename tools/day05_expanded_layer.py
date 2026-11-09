"""Map the unchanged branch structure onto the expanded author manuscript.

Keep published logical anchors, but emit every new paragraph in document order.
No prose is inferred or replaced by filler. Mapping is checked and recorded.
"""
from pathlib import Path
import difflib,json

def apply_expanded(root,P,B,M,A,SKIP,before,REPLACE,SCENES,speakers):
    path=root/'source/day05/expanded_intake.txt'
    if not path.is_file():return P,B,M,A,SKIP,before,REPLACE,SCENES,speakers
    new=path.read_text(encoding='utf-8').splitlines()
    mapping={}; starts={}
    operations=difflib.SequenceMatcher(None,P,new,autojunk=False).get_opcodes()
    for tag,a,b,c,d in operations:
        if tag=='equal':
            mapping.update((i,c+i-a) for i in range(a,b))
        elif tag=='insert':starts[a]=c
        elif tag=='delete':mapping.update((i,c) for i in range(a,b))
        else:
            mapping.update((i,c+min(d-c-1,(i-a)*(d-c)//max(1,b-a))) for i in range(a,b))
    mapping[len(P)]=len(new)
    I=lambda i:mapping[i]
    L=lambda i:starts.get(i,I(i))
    for k,(_,parts) in B.items():
        assert P[k]==new[I(k)],('Changed branch marker',k,P[k],new[I(k)])
        for condition,lo,hi in parts:
            assert I(lo)<=I(hi)
    B={I(k):(I(end),[(condition,I(lo),I(hi)) for condition,lo,hi in parts]) for k,(end,parts) in B.items()}
    M={I(k):(I(end),[(I(title),I(lo),I(hi),actions) for title,lo,hi,actions in parts]) for k,(end,parts) in M.items()}
    A={I(k):v for k,v in A.items()}
    SKIP={I(i) for i in SKIP}|{70}
    before={I(k):v for k,v in before.items()}
    REPLACE={I(k):v for k,v in REPLACE.items()}
    REPLACE[564]=new[564].replace('пока Тихонова заберёт со стола свою книгу','пока Тихонова сдаст посуду')
    REPLACE[67]='Через несколько минут я справилась с галстуком, а Даша переоделась в спортивную форму и посмотрела на мои кеды.'
    SCENES=[(I(title),L(lo),I(hi),bg) for title,lo,hi,bg in SCENES]
    SCENES[4]=(*SCENES[4][:3],'bg ext_square_day')
    SCENES[12]=(*SCENES[12][:3],'cs_camp_path_day')
    speakers={I(k):v for k,v in speakers.items() if new[I(k)].startswith('—')}
    speakers.update({65:'da',68:'da',69:'ls',117:'da',118:'ls',119:'da',151:'da',152:'ls',200:'mt',201:'ls',202:'mt',218:'mt',235:'mt',236:'ls',256:'sy',410:'ls',411:'da',412:'ls',527:'sl',528:'ls',577:'da',684:'da',738:'ls',739:'mz',743:'ls',744:'da',745:'ls',758:'ls',903:'mz',904:'ls',905:'mz'})
    for k in speakers:assert new[k].startswith('—'),(k,new[k])
    # Dress before showing a portrait; sportswear for the run, pioneer after washing.
    before.pop(I(65),None)
    before[67]=['$ cs_d5_dressed = True','$ cs_d5_costume("sport")','$ cs_d5_focus("da")','with cs_sprite_enter']
    before[71]=['$ cs_d5_room("cs_house_lena_darya_ext_day")']
    before[72]=['$ cs_d5_room("bg ext_square_day")']
    before[143]=['$ cs_d5_room("bg ext_washstand_day")']
    before[145]=['$ cs_d5_room("cs_house_lena_darya_int_day")','cs_narrator "После умывальников мы ненадолго вернулись в домик. Даша переоделась в пионерскую форму, а я поправила галстук."','$ cs_d5_run_finished = True','$ cs_d5_costume("pioneer")','$ cs_d5_room("cs_camp_path_day")']
    before[190]=['$ cs_d5_room("cs_camp_path_day")']
    before[241]=['$ cs_d5_room("bg ext_square_day")']
    before[I(205)]=['$ cs_d5_room("bg ext_no_bus")']
    before.pop(I(297),None)
    before[343]=['$ cs_d5_room("bg ext_washstand_day")']
    before[572]=['$ cs_d5_room("bg ext_musclub_day")']
    before[I(504)]=['$ cs_d5_room("bg int_musclub_day")']
    before[575]=['play music cs_miku_piano_track fadein 0.5']
    before[576]=['stop music fadeout 1.0']
    before[I(855)]=before.pop(I(854))
    before[I(801)]=[v for v in before[I(801)] if not v.startswith('stop ambience')]
    before[910]=['$ cs_d5_quiet = True','stop ambience fadeout 1.0']
    before[I(832)]=['$ cs_director_scene("bg int_house_of_mt_night2")','show bg int_house_of_mt_night2 zorder -100','with Dissolve(0.6)']
    # New handovers leave an ordinary library afternoon without the adults.
    before[736]=['$ cs_actor_exit(["mt", "cs"])','$ cs_d5_cast = ["cs_zhenya"]']
    unknown=[i for i in range(SCENES[0][1],SCENES[-1][2]) if new[i].startswith('—') and i not in speakers]
    # All old POV lines are explicitly kept as POV; newly added ones are above.
    old_ls={I(i) for i in range(48,936) if P[i].startswith('—') and i not in {}}
    unknown=[i for i in unknown if i not in old_ls]
    assert not unknown,('Unattributed new dialogue',[(i,new[i]) for i in unknown])
    (root/'source/day05/expanded_mapping.json').write_text(json.dumps(dict(operations=operations,paragraph_map=mapping,new_paragraphs=len(new),spoken_paragraphs=sum(s.startswith('—') for s in new[48:SCENES[-1][2]])),ensure_ascii=False,indent=2),encoding='utf-8')
    return new,B,M,A,SKIP,before,REPLACE,SCENES,speakers
