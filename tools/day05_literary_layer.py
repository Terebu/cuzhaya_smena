"""Reviewed scene tree for 'До рассвета', literary revision of 2026-11-06.

Indices address immutable nonempty paragraphs in literary_paragraphs.json.
The manuscript's preface, staging notes and appendix are never player text.
"""
import json,re

def speech(text):
    pieces=text[1:].strip().split(' — ')
    if len(pieces)==1:return pieces[0]
    verbs=r'сказал|ответил|спросил|произн[её]с|заметил|добавил|позвал|поздоровал|предложил|уточнил|переспросил|пробормотал|признал|объявил|предупредил|перебил|поинтересовал|обрадовал'
    positions=[j for j in range(1,len(pieces)) if pieces[j][0].islower() and re.search(verbs,pieces[j])]
    if not positions:return ' — '.join(pieces)
    assert len(positions)==1,text
    j=positions[0];attribution=pieces[j]
    first=' — '.join(pieces[:j])
    if j==len(pieces)-1:return first.rstrip(',')+('.' if first.endswith(',') else '')
    tail=' — '.join(pieces[j+1:])
    if attribution.endswith(',') or first.rstrip(',') in ('Лен','Лена','Мику','Сёмочка','Даша','Ольга Дмитриевна'):
        return first.rstrip(',')+', '+tail[0].lower()+tail[1:]
    return first.rstrip(',')+('.' if first.endswith(',') else '')+' '+tail

def apply_literary(root,romance):
    rows=json.loads((root/'source/day05/literary_paragraphs.json').read_text(encoding='utf-8'))
    P=[r['text'] for r in rows]
    heads=[i for i,s in enumerate(P) if s.startswith('### Сцена ')]
    assert len(heads)==20 and heads[-1]==1626
    end=P.index('## Техническое приложение для Codex')
    art={i for i in range(12,end) if not P[i].startswith(('#','[','А.','Б.')) and not P[i].isdigit()}
    speakers={i:'ls' for i in art if P[i].startswith('—')}
    reviewed={
      'da':'''18 20 23 26 28 31 33 39 41 45 51 53 61 63 70 73 80 96
      113 130 139 177 187 202 204 215 235 244 246 334 347 391 395 408 424 426 428
      457 462 478 480 497 522 524 557 597 599 622 690 701 705 707 710 714 717
      724 727 729 733 735 737 739 744 783 807 822 915 949 960 987 997 1020 1034
      1059 1091 1094 1096 1149 1175 1203 1216 1219 1222 1305 1313 1316 1320
      1323 1329 1343 1381 1383 1403 1423 1425 1428 1433 1464 1486 1547 1567
      1590 1596 1598 1604 1607 1612 1614 1635 1638 1641 1648 1758''',
      'sy':'''90 98 105 108 110 112 114 118 120 122 125 128 131 134 136 140 143
      145 147 153 155 157 159 162 166 168 171 173 180 182 185 190 192 207 209
      259 268 305 307 324 337 361 394 396 399 406 410 414 416 419 434 454
      470 489 492 494 504 517 540 542 545 548 550 555 558 565 568 570 572
      577 579 586 589 591 611 614 619 638 670 672 674 894 900 902 905 907
      931 934 936 939 951 973 1072 1074 1078 1086 1126 1166 1186 1200 1213
      1265 1267 1269 1287 1289 1303 1331 1334 1337 1397 1406 1409 1412
      1415 1417 1445 1460 1495 1497 1523 1579 1582 1585 1652 1654 1656
      1662 1664 1679 1690 1693 1714 1720 1737 1744 1752 1755 1762 1766 1771 1786''',
      'mz':'''219 221 224 226 229 231 234 236 239 250 252 254 256 262 264 267 269
      272 274 279 282 284 289 295 298 301 607 610 613 618 620 624 627 631 633 636
      639 646 649 655 657 659 662 665 677 687 847 850 869 880 882 904 954
      1112 1115 1127 1145 1147 1180 1221 1231 1245 1282 1301 1387 1390 1392
      1395 1512 1518 1521 1524 1681''',
      'mt':'''314 316 319 323 325 329 331 336 338 342 344 346 351 354 356 359 364
      366 1119 1121 1123 1129 1132 1169 1226 1284 1298 1442 1448 1457 1470
      1472 1514 1539 1556 1691 1697 1718 1721''',
      'us':'''378 380 383 385 388''',
      'un':'''752 755 758 760 767 772 774 779 784 788 792 795 798 800 804 813 816
      818 821 826 828 833 835 837 841 843 851 856 858 861 864 867 870 873
      1237 1240 1243 1246 1249 1251 1355 1360 1363 1529 1537 1541''',
      'sl':'''914 917 921 924 933 935 938 943 948 950 953 955 959 964 967 1554 1557 1560''',
      'dv':'''977 980 982 984 991 993 1004 1010 1014 1016 1025 1028 1036 1042 1044 1073 1075 1081''',
      'mi':'''1019 1021 1033 1038 1051 1054 1056 1064 1066 1566 1568''',
      'vi':'''1264 1266 1268 1271 1273 1276 1281 1453 1463 1465 1477 1479 1481 1483 1683''',
      'voice':'''1730 1741 1745 1750 1764 1777''',
    }
    for who,indices in reviewed.items():
        for i in map(int,indices.split()):
            assert i in speakers,(who,i,P[i])
            assert speakers[i]=='ls',('Repeated speaker override',i)
            speakers[i]=who
    DIALOGUE={i:(who,speech(P[i])) for i,who in speakers.items()}
    # Previously returned book: this is explicitly today's different loan.
    DIALOGUE[788]=('un','Хотела вернуть книгу, которую взяла сегодня утром.')
    DIALOGUE[843]=('un','Ладно. Тогда я просто отнесу книгу Жене.')
    B={
      151:(175,[('cs_friend_se >= 4',152,165),('cs_friend_se >= 1',166,170),(None,171,175)]),
      653:(668,[('cs_friend_mz >= 4',654,667)]),
      722:(741,[('cs_d5_shared_pace',723,731),(None,732,741)]),
      853:(863,[('cs_d5_lena_respected',854,863)]),
      863:(876,[('cs_friend_un >= 4',864,875)]),
      963:(971,[('cs_friend_sl >= 4',964,970),(None,970,971)]),
      1052:(1069,[('cs_friend_mi >= 4',1053,1068),(None,1068,1069)]),
      1089:(1100,[('cs_friend_da >= 4',1090,1100)]),
      1178:(1185,[('cs_friend_mz >= 4',1179,1184),(None,1184,1185)]),
      1235:(1256,[('cs_friend_un >= 4',1236,1255),(None,1255,1256)]),
      1353:(1367,[('cs_friend_un >= 4',1354,1366)]),
      1476:(1489,[('cs_friend_viola >= 4',1477,1488),(None,1488,1489)]),
      1530:(1546,[('cs_friend_un >= 4',1531,1545),(None,1545,1546)]),
      1553:(1564,[('cs_friend_sl >= 4 and cs_d5_slavya_volunteer',1554,1563),(None,1563,1564)]),
      1565:(1574,[('cs_friend_mi >= 4 and cs_d5_miku_volunteer',1566,1573)]),
      1576:(1589,[('cs_friend_se >= 4 and not cs_d5_semyon_address',1577,1588)]),
      1602:(1609,[('cs_friend_da >= 4',1603,1608),(None,1608,1609)]),
    }
    M={
      67:(85,[(68,69,77,['cs_d5_choose(1, 0)']),(77,78,84,['cs_d5_choose(1, 1)'])]),
      276:(293,[(277,278,287,['cs_d5_choose(2, 0)']),(287,288,292,['cs_d5_choose(2, 1)'])]),
      561:(584,[(562,563,574,['cs_d5_choose(3, 0)']),(574,575,583,['cs_d5_choose(3, 1)'])]),
      809:(846,[(810,811,830,['cs_d5_choose(4, 0)']),(830,831,845,['cs_d5_choose(4, 1)'])]),
      1325:(1348,[(1326,1327,1340,['cs_d5_choose(5, 0)']),(1340,1341,1347,['cs_d5_choose(5, 1)'])]),
    }
    before={
      12:['$ cs_d5_enter_literary()'],
      36:['$ cs_d5_costume("sport")'],
      47:['$ cs_d5_dressed = True','$ cs_d5_room("cs_house_lena_darya_ext_day")'],
      55:['$ cs_d5_room("bg ext_square_day")'],
      56:['$ cs_d5_room("bg ext_playground_day")'],
      85:['$ cs_d5_room("bg ext_square_day")'],
      104:['$ cs_d5_focus("sy")'],
      105:['play music cs_day_music_think fadein 1.2'],
      183:['stop music fadeout 1.0','$ cs_d5_room("bg ext_washstand_day")'],
      195:['$ cs_d5_room("cs_house_lena_darya_int_day")','cs_narrator "Семён подождал у дорожки, пока мы с Дашей зашли переодеться."','cs_narrator "Мы сменили спортивную одежду на пионерскую форму и догнали его у столовой."','$ cs_d5_run_finished = True','$ cs_d5_costume("pioneer")','$ cs_d5_room("bg ext_dining_hall_near_day")'],
      293:['$ cs_d5_room("bg ext_dining_hall_near_day")'],
      303:['$ cs_actor_exit(["cs_zhenya"])','$ cs_d5_cast = []'],
      317:['$ cs_d5_room("bg int_house_of_mt_day")'],
      340:['cs_narrator "Ольга Дмитриевна достала папку, которую утром забрала из запертого библиотечного ящика."','$ cs_d5_documents_location = "olga"'],
      368:['$ cs_d5_room("bg ext_house_of_mt_day")'],
      369:['$ cs_d5_room("bg ext_square_day")'],
      393:['$ cs_actor_exit(["us"])','$ cs_d5_cast = []','$ cs_d5_room("cs_camp_path_day")'],
      404:['$ cs_d5_room("bg ext_no_bus")'],
      440:['$ cs_d5_room("bg ext_bus")'],
      459:['$ cs_pov_begin()','with cs_sprite_leave'],
      499:['$ cs_pov_begin()','with cs_sprite_leave'],
      514:['$ cs_d5_room("bg ext_no_bus")'],
      585:['$ cs_d5_room("bg ext_washstand_day")'],
      593:['$ cs_actor_exit(["cs_semen"])','$ cs_d5_cast = []'],
      601:['$ cs_d5_room("cs_camp_path_day")'],
      692:['$ cs_d5_room("cs_camp_path_day")'],
      693:['$ cs_d5_room("bg ext_playground_day")'],
      745:['$ cs_d5_room("bg ext_library_day")'],
      846:['$ cs_d5_room("bg int_library_day")'],
      1000:['play music cs_day_music_daily fadein 1.0'],
      1017:['$ cs_d5_room("bg int_musclub_day")'],
      1030:['play music cs_miku_piano_track fadein 0.5'],
      1032:['stop music fadeout 0.5'],
      1047:['play music cs_miku_piano_track fadein 0.5'],
      1050:['stop music fadeout 0.5'],
      1069:['if cs_friend_mi >= 4:','    cs_ls "Мы вечером зайдём к Ольге Дмитриевне с записями. Хочешь присоединиться после репетиции?"','    cs_mi "Хочу! Я только закончу здесь и приду."','    $ cs_d5_miku_volunteer = True','else:','    $ cs_d5_miku_volunteer = False','play music cs_day_music_daily fadein 1.0'],
      1109:['$ cs_d5_documents_location = "library"'],
      1197:['$ cs_d5_room("bg ext_library_day")'],
      1229:['$ cs_d5_room("bg int_library_day")'],
      1307:['$ cs_d5_room("bg ext_square_day")'],
      1291:['$ cs_actor_exit(["cs"])','$ cs_d5_cast = []'],
      1318:['$ cs_d5_room("cs_camp_path_day")'],
      1348:['$ cs_d5_room("bg ext_playground_day")'],
      1401:['$ cs_d5_room("bg ext_square_sunset")'],
      1421:['$ cs_actor_exit(["cs_semen"])','$ cs_d5_cast = []'],
      1422:['$ cs_d5_room("cs_camp_path_sunset")'],
      1436:['$ cs_d5_room("bg ext_house_of_mt_sunset")'],
      1450:['$ cs_d5_documents_location = "olga"'],
      1449:['$ cs_d5_room("bg int_house_of_mt_night")'],
      1552:['$ cs_d5_focus("sl")','with cs_sprite_enter'],
      1563:['$ cs_d5_slavya_present = False','$ cs_actor_exit(["sl"])','$ cs_d5_cast = []'],
      1574:['$ cs_d5_miku_present = cs_friend_mi >= 4 and cs_d5_miku_volunteer'],
      1592:['$ cs_d5_room("bg ext_house_of_mt_night")'],
      1618:['$ cs_d5_room("bg int_house_of_mt_night")'],
      1628:['$ cs_d5_quiet = True','stop ambience fadeout 0.5','stop music fadeout 1.0','$ cs_d5_clock = "23:59"','show screen cs_d5_clock_face'],
      1625:['$ cs_pov_begin()','with cs_sprite_leave'],
      1672:['$ cs_d5_clock_stopped = True'],
      1729:['$ cs_pov_begin()','with cs_sprite_leave'],
    }
    # The text names each knock separately: audio follows the reader's pacing.
    for i in (1156,1157,1158,1160,1161,1162,1163,1700,1702,1703,1705,1706,1707,1708):
        before[i]=['play sound cs_d5_single_knock']
    A={
      964:['cs_d5_slavya_volunteer = True'],970:['cs_d5_slavya_volunteer = False'],
      657:['cs_d5_zhenya_cabinet_memory = True'],
      864:['cs_d5_lena_private_memory = True'],
      1554:['cs_d5_slavya_present = True'],
      1587:['cs_d5_address_talk_agreed = True'],
    }
    replacements={
      36:'Я нашла спортивные шорты, футболку и кроссовки. Пока переодевалась, Даша достала свою спортивную форму и собрала волосы.',
      333:'Даша придвинула стул ближе к столу.',
      640:'Я посмотрела на копию снимка.',
      854:'Я достала копию фотографии и положила перед Тихоновой.',
      970:'Славя обещала сообщить, если сама заметит что-нибудь необычное, и вернулась к обеду.',
      1068:'Мику предложила ещё раз послушать готовую композицию. На этот раз я слушала, не пытаясь подобрать ноты сама.',
      1184:'Женя осталась у стола. Дверь она предложила проверить только после того, как вожатая посмотрит в окно.',
      1255:'Вернувшаяся в библиотеку Тихонова молча слушала обсуждение. Расспрашивать её я не стала.',
      1307:'Мы с Дашей и Семёном вышли из библиотеки.',
      1488:'Виола коротко спросила о самочувствии. Я ответила, что всё в порядке.',
      1545:'Тихонова показала набросок по нашим рассказам: отметила окна и дорожку, а там, где подробностей не хватало, оставила чистое место.',
      1563:'Славя передала вожатой нужные вещи и ушла заканчивать вечерние поручения.',
      1608:'Даша осталась рядом. Когда станет холодно, она предложила вернуться внутрь.',
    }
    art.update(i for i in replacements if P[i].startswith('['))
    variants={14:(romance,P[14],'Даша спала на соседней кровати, отвернувшись к стене.'),
              15:(romance,P[15],'Я тихо села и нащупала ногой кроссовок.'),
              1564:('cs_friend_mi >= 4 and cs_d5_miku_volunteer',P[1564],'Мику осталась заканчивать репетицию. Вожатая знала, где её найти.')}
    thoughts={16,57,58,99,123,138,194,195,371,432,433,460,461,527,528,538,552,560,711,911,962,1067,1102,1103,1104,1105,1139,1140,1141,1195,1196,1257,1258,1505,1723,1724,1732,1733,1789}
    scenes=[(h,h+2,(heads[n+1] if n<19 else end),None) for n,h in enumerate(heads)]
    backgrounds={0:'cs_house_lena_darya_int_day',1:'bg ext_square_day',2:'bg int_dining_hall_people_day',3:'bg ext_house_of_mt_day',4:'bg ext_square_day',5:'bg ext_bus',6:'cs_camp_path_day',7:'bg int_library_day',9:'bg ext_library_day',10:'bg int_dining_hall_people_day',12:'bg ext_musclub_day',13:'bg int_library_day',16:'bg int_dining_hall_sunset',17:'bg ext_house_of_mt_night',18:'bg int_house_of_mt_night'}
    scenes=[(h,lo,hi,backgrounds.get(n)) for n,(h,lo,hi,bg) in enumerate(scenes)]
    (root/'source/day05/literary_speakers_review.txt').write_text('\n'.join('%s %s: %s'%(i,speakers[i],DIALOGUE[i][1]) for i in sorted(speakers)),encoding='utf-8')
    return P,B,M,A,set(range(12,end))-art,before,replacements,scenes,speakers,art,thoughts,DIALOGUE,variants
