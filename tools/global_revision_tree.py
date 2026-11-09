"""Reviewed control flow for the author's 6 November editions.

All coordinates address the immutable paragraph arrays, not generated RPY lines.
The old published scripts remain intact; the compatibility layer routes entry.
"""
import json,re

def tree(root,name):
    P=[x['text'] for x in json.loads((root/'source/global_revision_20261106'/(name+'_paragraphs.json')).read_text(encoding='utf-8'))]
    end=P.index('Приложение для Codex')
    B={}
    def branch(start,stop,*parts):B[start]=(stop,parts)
    def one(start,stop,cond):branch(start,stop,(cond,start+1,stop))
    def two(start,middle,stop,cond):branch(start,stop,(cond,start+1,middle),(None,middle+1,stop))
    if name=='prologue_day01':
        two(827,831,833,'cs_friend_mz >= 1')
        one(842,860,'cs_met_un and cs_friend_un >= 1')
    elif name=='day02':
        one(194,196,'cs_met_un and cs_friend_un >= 1')
        two(203,228,230,'cs_met_un and cs_friend_un >= 1')
        two(397,399,401,'cs_day02_miku_listened')
        one(602,604,'cs_helped_sl_day2')
        two(796,798,800,'cs_met_mz')
        branch(962,980,('cs_friend_mz <= 0',963,966),('cs_friend_mz == 1',967,971),(None,972,980))
        branch(1001,1017,('cs_friend_mz <= 0',1002,1005),('cs_friend_mz == 1',1006,1009),(None,1010,1017))
        one(1019,1027,'cs_talked_mz_square_day2')
        branch(1056,1076,('cs_friend_mz >= 2',1057,1064),('cs_friend_mz == 1',1065,1069),(None,1070,1076))
        one(1077,1089,'cs_friend_mz >= 1')
        one(1086,1088,'cs_mz_map_lead')
        two(1092,1096,1100,'cs_friend_se >= 2')
        two(1105,1115,1119,'cs_friend_sl >= 1')
        one(1108,1110,'cs_friend_se >= 2')
        one(1111,1113,'cs_helped_sl_day2')
        two(1121,1125,1128,'cs_friend_mi >= 1')
        one(1129,1134,'cs_friend_viola >= 2')
        one(1135,1138,'cs_met_un and cs_friend_un >= 1')
        two(1141,1144,1146,'cs_mi_intro_revised')
        two(1156,1158,1160,'cs_mi_intro_revised')
        one(1163,1167,'cs_friend_se >= 2')
        one(1168,1174,'cs_met_un and cs_friend_un >= 1')
    elif name=='day03':
        two(91,100,102,'cs_friend_sl >= 1')
        branch(167,178,('cs_friend_mz <= 0',168,170),('cs_friend_mz == 1',171,174),(None,175,178))
        one(180,183,'cs_mz_map_lead')
        one(249,253,'cs_rev_viola_before >= 2')
        one(314,319,'cs_sl_poster_saved_day3')
        one(332,334,'cs_mz_map_lead')
        one(414,416,'cs_mz_book_requested_day3')
        one(425,437,'cs_mz_map_lead')
        branch(438,446,('cs_mz_friend_on_arrival_day3 <= 0',439,440),('cs_mz_friend_on_arrival_day3 == 1',441,442),(None,443,446))
        one(501,507,'cs_se_friend_before_square_day3 >= 2')
        two(519,535,538,'cs_un_sketch_invite_day3')
        one(567,574,'cs_mz_dinner_friend_on_arrival >= 3 and cs_mz_open_library_invitation_day3')
        one(597,600,'cs_friend_se >= 2 and cs_se_day3_personal_talk')
        one(629,636,'cs_mz_evening_help_day3')
        branch(638,643,('cs_friend_mz >= 3',639,641),(None,642,643))
        one(651,656,'cs_mz_day3_honest_book_talk')
        two(667,669,671,'cs_mz_evening_help_day3')
        two(719,725,731,'cs_da_friend_before_night >= 1')
        two(739,763,766,'cs_da_shared_bed_day3')
    elif name=='day04':
        two(34,50,54,'cs_da_shared_bed_day3')
        two(41,46,50,'cs_da_love_confession_day3')
        two(324,331,340,'cs_d4_left_note')
        branch(516,537,('cs_da_love_confession_day3',517,529),('cs_da_shared_bed_day3',530,534),(None,535,537))
        one(781,788,'cs_sl_day4_notice_offer')
        # These invitations are independent, even when both are pending.
        one(791,799,'cs_mi_followup_invitation_day3')
        one(799,805,'cs_dv_followup_invitation_day3')
        two(871,878,881,'cs_friend_mz >= 3')
        one(886,890,'cs_mz_hug_allowed_day3')
        two(976,981,984,'cs_d4_mz_friend_before_choice >= 3 and cs_mz_hug_allowed_day3')
        two(1135,1140,1144,'cs_d4_se_honest_fear')
        two(1245,1250,1253,'cs_d4_mz_friend_before_choice >= 3 and cs_mz_hug_allowed_day3')
        two(1295,1306,1313,'cs_da_shared_bed_day3')
        one(1302,1306,'cs_da_love_confession_day3')
        one(1310,1313,'cs_friend_da >= 3')
    else:raise ValueError(name)
    M={}
    starts=[i for i,s in enumerate(P[:end]) if re.match(r'^Выбор \d+\.',s)]
    for h in starts:
        number=int(re.search(r'\d+',P[h])[0])
        a=next(i for i in range(h+1,end) if P[i].startswith('А. '))
        b=next(i for i in range(a+1,end) if P[i].startswith('Б. '))
        va=next(i for i in range(b+1,end) if P[i]=='Вариант А')
        vb=next(i for i in range(va+1,end) if P[i]=='Вариант Б')
        # Common markers inside the first option belong to nested conditions.
        stop=next((i for i in range(vb+1,end) if P[i]=='Общая сцена' or re.match(r'^Сцена (?:\d|П)',P[i])),end)
        M[a]=(stop,number,[(a,va+1,vb),(b,vb+1,stop)])
    art={i for i in range(67 if name=='prologue_day01' else next(i for i,s in enumerate(P) if re.match(r'^Сцена \d\d\.',s))+2,end)
         if not P[i].startswith(('[','Сцена ','Глава ','Выбор ','Вариант ','А. ','Б. ','Общая сцена','День 1. Глава'))}
    return P,B,M,art,end
