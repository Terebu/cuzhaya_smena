"""Compile the reviewed Google Doc plus its branch specification, without editing days 1–4."""
from pathlib import Path
import json,re,sys
from global_text_paging import chunks
ROOT=Path(__file__).resolve().parent.parent
P=[p['text'] for p in json.loads((ROOT/'source/day06/document.json').read_text(encoding='utf-8'))['paragraphs']]
OUT=ROOT/'days/day06'
q=lambda s:json.dumps(s,ensure_ascii=False)
ROM='cs_da_shared_bed_day3 and cs_da_love_confession_day3'
SP={}
for who,ids in {'da':'144 157','sy':'146 162','mt':'148','vi':'150','mz':'160'}.items():
    for i in map(int,ids.split()):SP[i]=who
for who,ids in {
'da':'180 187 191 199 202 270 280 308 324 327 379 427 436 474 476 528 532 535 552 559 564 572 583 589 591 594 597 600 602 606 614 631 641 643 651 660 671 677 687 689 708 723 728 732 735 738 740 743 783 806 828 840 852 855 859 861 864 874 878 880 887 891 894 897 899 902 904 906 908 911 917 919 924 927 929 936',
'sy':'212 216 221 223 305 319 405 407 411 413 417 419 423 425 500 504 507 510 514 516',
'mz':'246 251 254 256 258 264 267 271 388 390 394 397 399 481 483 485 487',
'mt':'210 226 228 231 233 237 241 316 320 334 336 440 442 524 544 546 575 578 608 611 613 623 700 704 753 755 770 774 777 794 796 823 835 839',
'un':'286 289 292 295 298 359 361 365 369 372 375 378 380 489 492',
'sl':'279 344 346 350 457 461',
'dv':'282 284 465 467 470',
'mi':'473 475',
'vi':'617 619 713 716 748 760 776 786 800 822 845',
'driver':'439 441 450',
}.items():
    for i in map(int,ids.split()):
        assert P[i].startswith('—'),(i,P[i]);SP[i]=who

def say(who,text):
    lines=[]
    if who not in ('narrator','th'):lines.append('$ cs_d6_focus('+q(who)+')')
    for part in chunks(text):lines.append(('cs_d6_driver' if who=='driver' else 'cs_'+who)+' '+q(part))
    return '\n'.join(lines)
def s(text):
    """Small branch fragments: narrator|... or ls|...; $/control commands are literal."""
    out=[]
    for line in text.strip('\n').splitlines():
        if '|' in line and not line.lstrip().startswith('$'):
            who,text=line.split('|',1);out.extend(say(who.strip(),text.strip()).splitlines())
        else:out.append(line)
    return '\n'.join(out)
def ind(code):return '\n'.join('    '+x if x else '' for x in code.splitlines())
def iff(cond,yes,no=None):
    code='if '+cond+':\n'+ind(yes)
    if no is not None:code+='\nelse:\n'+ind(no)
    return code
def menu(number,options):
    return 'label cs_check_d6_choice_%d:\nmenu:\n'%number+'\n'.join('    '+q(title)+':\n        $ cs_d6_choose(%d,%d)\n'%(number,i)+ind(ind(code)) for i,(title,code) in enumerate(options))+'\nlabel cs_check_d6_choice_%d_done:'%number
def room(image,allowed):return '$ cs_d6_room('+q(image)+','+repr(allowed)+')'
def cg(name):return '$ cs_d6_cg('+q('cs_cg_'+name)+')'
PAIR=['cs_darya'];TRIO=PAIR+['cs_semen'];GROUP=TRIO+['mt'];DIN=GROUP+['cs_zhenya','un','sl','dv','mi']
C={};H={};R={};TH={193,194,207,301,302,310,311,348,421,448,539,540,568,586,648,663,682,683,684,696,697,778,779,808,820,830,846,905,916,933,934,938}
def hook(i,code):H[i]=H.get(i,'')+('\n' if i in H else '')+code
def custom(a,b,fn):C[a]=(b,fn)
def orig(a,b):return emit(a,b,ignore=a)
def emit(lo,hi,ignore=None):
    out=[];i=lo
    while i<hi:
        if i in H and i!=ignore:out.append(H[i])
        if i in C and i!=ignore:
            end,fn=C[i];out.append(fn());i=end;continue
        t=R.get(i,P[i]).replace('\v','\n')
        if not t or t.startswith(('К оглавлению','Глава ','Часть ')) or t in ('* * *','День 6'):i+=1;continue
        if i in TH:out.append('$ cs_d6_think()')
        if t.startswith('—'):
            who=SP.get(i,'ls');parts=re.split(r'\s+—\s+',t[1:].strip())
            for j,part in enumerate(parts):
                if j%2:
                    if part.startswith(('Она ','Он ','Я ')):out.append(say('narrator',part))
                    continue
                part=part.rstrip(', ')
                if part and part[-1] not in '.!?…':part+='.'
                out.append(say(who,part))
        else:out.append(say('th' if i in TH else 'narrator',t))
        i+=1
    return '\n'.join(out)

# Actual arrivals are staged here, never inferred from a narrator mentioning a name.
for i,image,cast in [(175,'cs_house_lena_darya_int_day',PAIR),(206,'bg ext_house_of_mt_day',PAIR),(217,'bg int_house_of_mt_day',GROUP),(244,'bg int_library_day',TRIO+['cs_zhenya']),(275,'bg ext_dining_hall_near_day',DIN),(300,'bg int_dining_hall_people_day',DIN),(331,'bg ext_dining_hall_near_day',GROUP),(339,'cs_camp_path_day',PAIR),(354,'bg ext_library_day',PAIR+['un']),(385,'bg ext_library_day',PAIR+['cs_zhenya']),(402,'cs_house_lena_darya_ext_day',TRIO),(432,'bg ext_no_bus',DIN),(543,'bg ext_house_of_mt_day',PAIR+['mt']),(548,'bg ext_square_day',PAIR),(549,'bg ext_playground_day',PAIR),(555,'bg int_library_day',PAIR),(574,'bg ext_house_of_mt_day',PAIR+['mt']),(581,'bg int_musclub_day',PAIR),(604,'bg int_house_of_mt_day',PAIR+['mt','cs']),(627,'cs_camp_path_day',PAIR),(628,'cs_d4_old_ext',PAIR),(632,'cs_d4_old_corridor',PAIR),(634,'cs_d4_old_stairs',PAIR),(637,'cs_d4_old_bunker',PAIR),(691,'cs_d4_old_stairs',PAIR),(692,'cs_d4_old_ext',PAIR),(699,'bg ext_house_of_mt_sunset',PAIR+['mt']),(711,'bg int_aidpost_day',PAIR+['cs']),(721,'cs_d6_pier_sunset',PAIR),(747,'bg ext_house_of_mt_sunset',PAIR+['mt','cs']),(767,'bg int_dining_hall_sunset',PAIR+['mt','cs']),(838,'bg ext_dining_hall_near_sunset',PAIR+['mt','cs']),(849,'cs_house_lena_darya_int_night',PAIR),(870,'cs_d6_washstand_night',PAIR),(877,'bg ext_library_night',PAIR),(884,'cs_house_lena_darya_int_night',PAIR)]:hook(i,room(image,cast))
hook(175,'$ cs_d6_costume("pajamas")')
hook(188,cg('day06_blank_pages_morning'))
hook(197,'$ cs_d6_costume("pioneer")\n'+room('cs_house_lena_darya_int_day',PAIR))
hook(210,'$ cs_d6_allowed = '+repr(GROUP))
hook(209,'$ cs_rev_knocks(2)')
hook(300,'play sound "sound/sfx/dinner_horn_processed.ogg"\n$ cs_rev_music(cs_day_music_daily,0.12)')
hook(438,'$ cs_bus_cue("stop")\n'+room('bg ext_bus',DIN)+'\n$ cs_bus_cue("open")')
hook(434,'$ cs_bus_engine("distant")')
hook(521,'$ cs_bus_cue("close")')
hook(522,cg('day06_semen_bus_wave')+'\n$ cs_bus_engine("depart")')
hook(523,'$ cs_bus_cue("gone")\n$ cs_d6_bus_departed = True\n'+room('bg ext_no_bus',['cs_darya','mt','cs'])+'\nstop sound fadeout 0.6\nstop music fadeout 2.0')
hook(538,room('cs_camp_path_day',PAIR))
hook(551,'play sound "sound/sfx/soccer_ball_kick.ogg"')
hook(627,'stop music fadeout 1.5')
hook(638,cg('day06_archive_comparison_day'))
hook(664,room('cs_d4_old_bunker',PAIR))
hook(666,'play sound "sound/sfx/brass_drop.ogg"')
hook(699,'$ cs_rev_time("sunset")')
hook(726,cg('day06_pier_evening'))
hook(751,cg('day06_cards_four'))
hook(782,cg('day06_fifth_place_intact')+'\nstop music fadeout 1.0')
hook(810,cg('day06_fifth_place_changed'))
hook(836,cg('day06_fifth_place_tray')+'\n$ cs_d6_fifth_tray_locked = True')
hook(849,'$ cs_rev_time("night")')
hook(884,'$ cs_d6_costume("pajamas")')
hook(932,'stop music fadeout 2.0')
hook(543,'$ cs_d6_library_key_location = "lena"')
hook(571,'$ cs_d6_book_borrowed = True\n$ cs_d6_book_location = "lena"')
hook(574,'$ cs_d6_library_key_location = "olga"')
hook(620,'$ cs_d6_firstaid_location = "lena"')
hook(710,'$ cs_d6_olga_copy = True')
hook(712,'$ cs_d6_firstaid_location = "viola"')

# Audible physical actions use the installed mod/game recordings.
for index,path,volume in [(184,'sound/sfx/drawer_rattle.ogg',0.3),(217,'sound/sfx/door_squeak_light.ogg',0.3),(260,'sound/sfx/paper_bag.ogg',0.22),(543,'sound/sfx/keys_rattle.ogg',0.32),(555,'sound/sfx/door_squeak_light.ogg',0.3),(637,'sound/sfx/paper_bag.ogg',0.22),(650,'sound/sfx/paper_bag.ogg',0.22),(724,'sound/sfx/water_splash.ogg',0.25),(747,'sound/sfx/paper_bag.ogg',0.23),(804,'sound/sfx/knock_glass.ogg',0.22),(871,'sound/sfx/scoop_water_cup.ogg',0.3)]:
    hook(index,'$ cs_rev_sfx('+q(path)+','+str(volume)+')')
hook(432,'stop music fadeout 1.5')
hook(522,'stop music fadeout 1.5')

# Four choices. Friendship at arrival determines memory, not today's reward.
def mz_choice():
    high=orig(262,269)+'\n$ cs_d6_mz_independent = True'
    medium=s('''narrator|Женя провела карандашом по краю листа.
mz|Стол у Ольги помню. Мы что-то писали. А что — не могу сказать.
ls|Людей помнишь?
mz|Тебя, Дашу. Семён возле двери. Может, просто потому, что он там живёт.
narrator|Я попросила записать и это, отдельно от догадок. Потом показала свой лист.
mz|Знакомо. Но я не уверена, что вспомнила бы сама.
ls|Тогда так и отметим.''')
    low=s('''mz|Не помню. И если сейчас прочту твой рассказ, потом уже не разберу, что вспомнила сама.
narrator|Я убрала листы.
ls|Хорошо. Можешь просто записать, что у тебя было последним?
mz|Это могу.
narrator|Она написала несколько строк и придвинула лист ко мне.
mz|Я не обещаю, что поверю.
ls|От тебя пока и не требуется.''')
    wait=iff('cs_d6_before("mz") >= 4',high,iff('cs_d6_before("mz") >= 1',medium,low))+ '\n'+orig(269,274)
    rush=s('''narrator|Я развернула перед ней листы.
ls|Прочти. Может, так быстрее.
narrator|Женя пробежала глазами строки и положила карандаш.
mz|Теперь я уже не проверю, вспомнила бы сама.
narrator|Я посмотрела на её пустую страницу.
ls|Да. Поторопилась.
mz|Не в первый раз. Ладно, оставь копию.''')
    return menu(1,[('Сначала запиши своё. Мы подождём',wait),('У нас мало времени. Вот что было',rush)])
custom(261,274,mz_choice)

def optional_memories():
    code=''
    for key,flag,yes,no in [
    ('sl','slavya',s('''sl|Плед на колени положили. А чай почти никто не пил.
ls|Ты помнишь?
sl|Не всё. Я собиралась убрать кружки и почему-то боялась отойти от стола.
narrator|Она остановилась, пытаясь вспомнить дальше.
ls|Хватит пока. Это уже помогло.'''),s('sl|Я ночью там не была. Но ты сейчас совсем бледная. Пойдём поедим, потом расскажешь.')),
    ('dv','alisa',s('''narrator|Алиса отвела меня на шаг от двери.
dv|Было что-то на двери у Ольги. Я оттуда уйти хотела, а потом осталась.
ls|Что было написано?
dv|Не помню. Только твоё лицо.
ls|Если ещё что-нибудь вспомнишь, скажешь?
dv|Скажу. Только не бегай за мной каждые пять минут.'''),s('dv|Ночью меня с вами не было. А автобус проверить — это можно. Только без очередного допроса.')),
    ('mi','miku',s('''mi|Я возле стола сидела. И боялась, что сейчас кого-нибудь не станет.
narrator|Она посмотрела на Семёна, потом на Дашу.
mi|Но не знаю, почему.
da|Пока все здесь. Давай с этого начнём.'''),s('mi|В домике я ночью не была. Но если вам сейчас нужна помощь, скажите.'))]:
        code+='\n'+iff('cs_d6_before('+q(key)+') >= 4',iff('cs_d5_'+flag+'_present',yes,no))
    return code
hook(285,optional_memories())
R[278]='Те, кто не был с нами у Ольги, помнили свой обычный вечер. У остальных дорога до домиков выпадала из рассказа.'
def un_memory():
    high=orig(292,300)+'\n$ cs_d6_un_independent = True'
    closed=s('''un|Можно потом тебе кое-что сказать?
narrator|Тихонова повернулась к Даше. Я уже открыла рот, но остановилась.
ls|Я пока за завтраком. Если захотите, позовёте.''')+'\n$ cs_d6_un_private = True'
    medium=s('''un|После завтрака можно я посижу с вами?
ls|Конечно.
un|Мне снилось, что меня всё время с кем-то путают.
ls|Где?
un|Не знаю. И я не уверена, что это про вчера.
ls|Тогда запишем как сон. Без выводов.''')
    low=s('''ls|Хочешь сесть с нами?
un|Спасибо. Я сегодня отдельно.
narrator|Лена закрыла альбом и направилась завтракать. Я не стала её задерживать.''')
    return iff('cs_d6_before("un") >= 4',iff('cs_d5_lena_respected',high,closed),iff('cs_d6_before("un") >= 1',medium,low))
custom(292,300,un_memory)
custom(306,307,lambda:iff('cs_d6_mz_independent or cs_d6_un_independent',orig(306,307),say('ls','Пока начало. У нас троих воспоминания остались. Если опять потеряем записи, будем друг другу рассказывать.')))

def help_choice():
    sl=orig(341,353)
    dv=room('bg ext_musclub_day',PAIR+['dv'])+'\n'+s('''narrator|Алиса пыталась одновременно удержать гитару и застегнуть сумку.
ls|Давай подержу.
narrator|Она посмотрела на мою руку.
dv|Только ничего не урони.
ls|Спасибо за доверие. Почти тронута.
narrator|Я взяла чехол здоровой рукой. Даша помогла со второй сумкой.
narrator|До домика дошли без потерь. Алиса всё-таки забыла ремень, пришлось вернуться.
ls|Без нас бы уехала без половины вещей.
dv|Без тебя я бы меньше отвлекалась.
ls|Но скучнее.
narrator|Она усмехнулась и забрала чехол.
dv|Ладно. Спасибо.''')
    mi=room('bg int_musclub_day',PAIR+['mi'])+'\n'+s('''narrator|Мику складывала ноты сразу в три стопки и уже путалась, какую собиралась взять.
ls|Эту оставляем?
mi|Да. Нет, подожди, тут второй лист от той песни.
narrator|Я села рядом.
ls|Хорошо. Ты говоришь, мы раскладываем. Две минуты без самостоятельного творчества.
narrator|Даша нашла бечёвку. Мы перевязали стопку для клуба и собрали дорожную папку.
mi|Я думала, не успею.
ls|Успела. Теперь можно вспоминать, что забыла.
narrator|Она засмеялась и тут же проверила карманы.''')
    return s('narrator|До обеда оставался свободный час. Успеть в три места сразу не получится; надо выбрать, кому помочь.')+'\n'+menu(2,[('Помочь Славе закончить сборы',sl),('Помочь Алисе с гитарой и сумками',dv),('Забрать с Мику вещи из клуба',mi)])
custom(340,353,help_choice)
hook(342,'$ cs_d6_allowed = '+repr(PAIR+['sl']))

def un_bench():
    low=s('''narrator|У библиотеки мы встретили Тихонову с собранной сумкой.
ls|Что-нибудь ещё вспомнила?
un|Нет. И если опять увидишь там похожую девушку — не принимай её за меня.
ls|Помню. Подходить не стану.''')
    draw=orig(364,369)+'\n$ cs_d6_sketch_done = True\n'+cg('day06_drawing_by_library')
    nodraw=s('''narrator|Я не стала задерживать её с альбомом.
ls|Успеешь собраться?
un|Почти всё готово.
narrator|Лена провела пальцем по углу обложки.''')
    quiet_draw=s('''narrator|Тихонова сама раскрыла альбом.
un|Мы же обещали порисовать. Давайте только без разговоров про ночь?
ls|Конечно.''')+'\n'+orig(366,369)+'\n$ cs_d6_sketch_done = True\n'+cg('day06_drawing_by_library')
    shared=iff('cs_d6_un_private',say('narrator','Мы встретились у библиотечной скамейки. К ночным событиям я не возвращалась.'),orig(354,364))+'\n'+iff('cs_d5_un_day6_sketch_offer',iff('cs_d6_un_private',quiet_draw,draw),nodraw)+'\n'+orig(369,384)
    private=iff('cs_d6_un_private',s('''narrator|Даша на минуту задержалась с Тихоновой. Я отошла к двери библиотеки.
narrator|Вернувшись, Даша сказала только, что Лена пока не хочет обсуждать ночь со мной. Подробностей я не стала спрашивать.'''))
    cancelled=iff('cs_d5_un_day6_sketch_offer',s('''un|Вчера я обещала порисовать. Но сейчас не хочу.
ls|Хорошо. Не будем через силу.'''))
    return room('bg ext_library_day',PAIR+['un'])+'\n'+private+'\n'+iff('cs_d6_before("un") >= 1',shared,low+'\n'+cancelled)
custom(354,384,un_bench)

custom(392,395,lambda:iff('cs_d6_mz_listened',orig(392,395)+'\n'+iff('cs_friend_mz >= 4',s('''mz|Одинаковые фамилии ещё ничего не решают. Смотри, один ли это список или разные документы.
narrator|Женя добавила в памятку поля: год, номер смены, заголовок, страница.
ls|То есть меньше радостно кричать и больше переписывать?
mz|Ты удивительно быстро понимаешь, когда хочешь.''')+'\n$ cs_d6_archive_guide = True'),s('narrator|Я сама разделила чистый лист на факты и предположения. Женя проверила только, не перепутаны ли наши копии.')))
custom(396,401,lambda:iff('cs_d5_zhenya_address or (cs_friend_mz >= 4 and cs_d6_mz_listened and not cs_d5_asked_address)',iff('cs_d5_zhenya_address',s('''ls|Твой адрес остался на вчерашнем листе. Запишешь ещё раз?
mz|Запишу. Держи отдельно от остального.'''),s('''ls|Если захочешь, можешь оставить адрес.
narrator|Женя сама взяла карандаш.'''))+'\n'+orig(397,401)+'\n$ cs_d6_mz_address_received = True',s('''narrator|Перед уходом я спросила про адрес.
mz|Пока не хочу.
narrator|Я кивнула и убрала чистый лист.
ls|Хорошо. Это не обязательная часть проводов.
mz|Вот и договорились.''')))

def se_choice():
    yes=orig(412,421)
    ifcontinue=iff('cs_d5_semyon_agency',say('ls','Как и вчера: проверим вместе, а решишь ты. Я помню нашу договорённость.'))
    yes=ifcontinue+'\n'+yes
    no=s('''ls|Сначала я всё проверю. До этого не садись.
narrator|Семён посмотрел на меня.
sy|Вместе проверим. Но поеду я, Лена.
narrator|Мне захотелось возразить. Вместо этого я потёрла ладонью колено.
ls|Да. Я поняла.
sy|Вот и хорошо.''')
    return menu(3,[('Проверим автобус, а решишь ты',yes),('Сначала я всё проверю. До этого не садись',no)])
custom(412,421,se_choice)
custom(409,412,lambda:iff('cs_d6_before("se") >= 4',orig(409,412),iff('cs_d6_before("se") >= 1',s('''ls|Хочешь поговорить до посадки?
narrator|Семён сел на ступеньку. Даша отложила рубашку.
sy|А если автобус окажется обычным?'''),s('''narrator|Семён остался возле крыльца. Мы с Дашей спросили, что он думает о рейсе.
sy|Я всё помню. И карточку, и надпись. Но сегодня еду.
ls|Автобус всё равно проверим?
sy|Конечно. А если он обычный?'''))))
custom(422,426,lambda:iff('cs_d5_semyon_address or cs_friend_se >= 4',orig(422,426)+'\n$ cs_d6_se_address_offered = True'))
custom(427,429,lambda:iff('cs_d6_se_agency',orig(427,429),s('''da|Дашь ему самому решить?
ls|Да. Даже если мне от этого не спокойнее.''')))

custom(432,433,lambda:s('narrator|После обеда сумки потянулись к воротам.')+'\n'+iff('cs_d6_help == "mi"',s('narrator|Мику спокойно ждала с дорожной папкой. Алиса громко возмущалась, что её гитару считают отдельным местом багажа.'),s('narrator|Мику ещё раз вернулась в клуб. Алиса громко возмущалась, что её гитару считают отдельным местом багажа.')))
custom(445,446,lambda:iff('cs_d6_help == "sl"',say('narrator','Славя сверила списки. Даша вместе с ней прошла по салону.'),say('narrator','Славя сверила списки и вернулась к багажу. Даша вместе с Ольгой проверила салон.'))+'\n'+iff('cs_d6_help == "dv"',say('dv','Пойдём, с другой стороны посмотрим.'))+'\n'+say('narrator','Семён обошёл автобус снаружи и сам заглянул внутрь.'))
custom(455,463,lambda:iff('cs_d6_help == "sl"',orig(455,463)+'\n$ cs_d6_towels_carried = True',s('''narrator|Славя поставила последнюю сумку у багажного отделения и наконец выпрямилась.
sl|Всё, теперь можно ехать.
ls|Попробуй хотя бы в дороге посидеть.
sl|Если никто больше ничего не забудет.'''))+'\n'+iff('cs_d6_before("sl") >= 4',s('''sl|Возьми. У меня второй есть.
narrator|Славя протянула запасной значок.
ls|Теперь точно не выгонят за нарушение формы.
sl|За форму — нет.
narrator|Я приколола значок к карману.
ls|Остальные основания ты благоразумно оставила.''')+'\n$ cs_d6_sl_badge_received = True'))
hook(471,iff('cs_d6_help == "dv" and cs_friend_dv >= 4',s('''narrator|Алиса положила мне в ладонь медиатор.
dv|Потом вернёшь.
ls|Ты сейчас выдаёшь мне повод приставать к тебе после лагеря?
dv|Ты и без повода справляешься.
ls|Спасибо.''')+'\n$ cs_d6_dv_pick_received = True'))
hook(480,iff('cs_d6_help == "mi" and cs_friend_mi >= 4',iff('cs_d5_miku_intro_heard or cs_day02_miku_listened',s('''mi|Я отдельно начало записала. Не пытайся сразу всю песню вспомнить.
ls|Я ноты читаю примерно как старые ведомости.
narrator|Она напела первые звуки и показала строку пальцем.
mi|Тогда запомни хотя бы так.
narrator|Я повторила. Со второго раза стало похоже.''')+'\n$ cs_d6_mi_known_motif = True',s('''mi|Это короткий напев на прощание. Новый — такого мы ещё не играли.
narrator|Она напела и положила в конверт несколько записанных тактов.'''))+'\n$ cs_d6_mi_music_received = True'))
def exit_actor(tag):
    return 'with None\n$ cs_actor_exit(['+q(tag)+'])\n$ cs_d6_cast = [t for t in cs_d6_cast if t != '+q(tag)+']\nwith cs_sprite_leave'
hook(464,exit_actor('sl'))
hook(472,exit_actor('dv'))
R[479]='Мику всё-таки улыбнулась и обняла нас обеих.'
hook(480,say('narrator','Потом Мику побежала в салон, прижимая к себе сумку.')+'\n'+exit_actor('mi'))
hook(488,exit_actor('cs_zhenya'))
hook(495,exit_actor('un'))
custom(482,483,lambda:iff('cs_d6_mz_address_received',orig(482,483),say('ls','Наблюдения отдельно. Фантазии оставила в голове.')))
custom(484,488,lambda:iff('cs_friend_mz >= 4 and cs_d6_mz_listened',orig(484,488),say('narrator','Женя кивнула на прощание и поднялась в автобус.')))
custom(489,495,lambda:iff('cs_d6_sketch_done and cs_friend_un >= 4',orig(489,495)+'\n$ cs_d6_un_sketch_received = True',s('''narrator|Тихонова коротко пожала мне руку. Альбом остался у неё.
un|Хорошей дороги завтра.
ls|И тебе сегодня.''')))
def se_farewell():
    address=iff('cs_d6_se_address_offered',orig(509,512)+'\n$ cs_d6_se_address_received = True')
    account=iff('cs_d6_se_agency and cs_friend_se >= 4',s('''narrator|Перед посадкой Семён оставил нам ещё один лист. На нём были его последние воспоминания о ночи: карточка, слова голоса и вопрос о выборе.
sy|Сравните со своим рассказом. Тут только то, что я сам помню.
ls|Спасибо.''')+'\n$ cs_d6_se_account_received = True')
    high=orig(496,500)+'\n'+cg('day06_semen_farewell_day')+'\n'+orig(500,509)+'\n'+room('bg ext_bus',DIN)+'\n'+address+'\n'+account+'\n'+orig(512,518)
    low=s('''narrator|Семён подошёл к автобусу. Даша пожала ему руку; я пожелала хорошей дороги.''')+'\n'+iff('cs_d6_se_address_offered',s('''narrator|Семён протянул заново записанный адрес.
sy|Вчерашний лист пропал. Этот положи отдельно.
ls|Спасибо.''')+'\n$ cs_d6_se_address_received = True')+'\n'+s('''sy|До встречи.
ls|До встречи, Семён.
narrator|Он поднялся в салон.''')
    return iff('cs_d6_before("se") >= 1',high,low)+'\n$ cs_actor_exit(["cs_semen"])\n$ cs_d6_cast = [t for t in cs_d6_cast if t != "cs_semen"]\nwith cs_sprite_leave\n'+iff('cs_d6_se_address_received',say('narrator','Я осталась у ступенек с его адресом в руке.'))+'\n'+iff(ROM,s('''narrator|Когда Семён сел, Даша взяла меня за руку.
da|Отпустила?
ls|Физически — да. Мысленно ещё держу за воротник.
da|Отпускай постепенно.
narrator|Я переплела наши пальцы и кивнула.'''))
custom(496,519,se_farewell)
custom(530,531,lambda:iff('cs_d6_towels_carried',orig(530,531),say('narrator','Ольга попросила зайти к ней за поручением. Виола пошла закрывать медпункт после осмотра уезжавших.')))
custom(534,536,lambda:iff('cs_d6_towels_carried',orig(534,536),s('''da|Выдержу. Пойдём к Ольге.''')))

custom(581,586,lambda:iff('cs_d6_mi_music_received',s('''narrator|В клубе Даша открыла окно, а я села за пианино и достала листок Мику.
narrator|Я попробовала найти короткий напев. Даша тихо напела начало; с третьей попытки стало похоже.
ls|Вот теперь концерт с программой.
da|И с автором, которого стоит указать.
ls|Обязательно. Моё тут только героическое усилие.''')+'\n$ cs_d6_mi_motif_tried = True',orig(581,586)))
R[619]='— После ваших вчерашних рассказов — вполне обычные.'
hook(620,iff('cs_friend_viola >= 4 and cs_d4_viola_full_trust',s('''vi|Ты уже рассказывала, как туда ходила. В этот раз без импровизаций. Сырой пол обходите. Свет в коридоре ещё не значит, что с проводкой всё хорошо.
ls|Учтём.
vi|И локоть береги. Мне приятно, когда мои советы переживают хотя бы один день.''')))
hook(664,iff('cs_d6_archive_guide',s('''narrator|Я вернулась к памятке Жени и сравнила номера ведомостей. У бумаг за 1970-й и 1971-й оказались разные номера смен.
ls|Вот это можно проверить. Не один и тот же список с разными датами.
da|Перепиши оба заголовка целиком.''')+'\n$ cs_d6_archive_compared = True'))
hook(717,iff('cs_friend_viola >= 4 and cs_d4_viola_full_trust',s('''narrator|Я показала Виоле копии с датами. Она прочла подписи и попросила оставить лист рядом с Ольгиной копией.
vi|О причинах пока не гадаю. Но это стоит сохранить.''')+'\n$ cs_d6_viola_documents_shared = True'))
custom(784,791,lambda:menu(4,[('Записать, как всё стоит, и спокойно поесть',orig(784,791)),('Не будем снова себя накручивать. Садимся',s('''narrator|Я отодвинула себе стул.
ls|Садимся. Если Ольга поставила лишнее, суп от этого хуже не станет.
narrator|Даша села рядом. Пятое место осталось с торца.'''))]))
custom(818,831,lambda:iff('cs_d6_place_recorded',orig(818,831),s('''ls|Хлеб таким был?
narrator|Даша наклонилась к тарелке.
da|Не знаю. Я не смотрела.
narrator|Ольга тоже не смогла вспомнить. Виола сказала, что кусок мог отломиться ещё на кухне.
narrator|Я медленно села обратно.
ls|Надо было сначала посмотреть.
da|Теперь уже не проверим. Запишем, что есть сейчас.''')))
hook(858,iff('cs_d6_place_recorded',say('narrator','В записи стояло: до ужина хлеб был целым; после у края не хватало куска.'),say('narrator','Я отдельно отметила: исходное состояние хлеба мы не проверили. Что именно произошло за ужином, утверждать нельзя.'))+'\n'+iff('cs_d6_se_account_received',say('narrator','Я ещё раз сверила ночные события с листом Семёна. Его рассказ лежал отдельно от наших догадок.'))+'\n'+iff('cs_d6_dv_pick_received',say('narrator','Медиатор Алисы положила рядом с конвертом, чтобы утром не забыть.')))
def pack():
    return s('narrator|Я убрала конверт в сумку, а книгу положила рядом, чтобы утром вернуть.')+'\n'+iff('cs_d6_un_sketch_received',say('narrator','Рисунок Даши спрятала между чистыми страницами.'))+'\n'+iff('cs_d6_mz_address_received or cs_d6_se_address_received',say('narrator','Полученные адреса убрала в отдельный карман.'))+'\n$ cs_d6_items_packed = True\n$ cs_d6_book_location = "room_table"'
def night():
    romance=pack()+'\n'+s('''narrator|Даша поставила кружку на тумбочку. Я помедлила возле своей кровати.
ls|Можно сегодня с тобой?
narrator|Она подвинула подушку.
da|Иди. Только конверт оставь в сумке.
ls|Даже расследование не пустишь в постель?
da|Особенно его.
narrator|Я легла рядом, осторожно устроила больную руку поверх одеяла. Даша помогла расправить край.
da|Так нормально?
ls|Да.''')+'\n'+cg('lena_darya_shared_sleep_night')+'\n'+s('''narrator|Некоторое время я слушала, как она дышит.
ls|Что ты обо мне подумала в первый день?
da|Что ты всё время шутишь.
ls|А что-нибудь приятное?
da|Что хочу ещё с тобой поговорить.
ls|Вот с этого и надо было начинать.
narrator|Она улыбнулась и убрала волосы с моего лица.
da|А ты?
ls|Что ты красивая. И что рядом с тобой мне полегче.
da|Даже когда я с тобой спорю?
ls|Особенно тогда. Кому-то же надо останавливать мои лучшие идеи.
narrator|Даша тихо засмеялась. Я попросила её наклониться и коротко поцеловала.
narrator|На этот раз добавлять шутку не захотелось.''')
    friendly=orig(885,914)+'\n'+cg('day06_separate_beds_night')
    return iff(ROM,romance,friendly)
custom(885,914,night)
custom(932,933,lambda:iff('not cs_d6_items_packed',pack())+'\n'+say('narrator','Потом я погасила лампу у стола.'))
custom(937,938,lambda:iff(ROM,say('narrator','Я устроилась у Даши под плечом. Завтра всё равно пришлось бы вставать, что бы нас там ни ждало.'),orig(937,938)))

def integrate_day5():
    # Keep published scene 20 and its save anchors. Its edited events already
    # implement chapter 19.4, including trust and the actual overnight cast.
    flow=ROOT/'days/day05/00_flow.rpy'
    text=flow.read_text(encoding='utf-8')
    if 'call cs_day05_21' not in text:
        text=text.replace('    $ cs_d5_done = True','    call cs_day05_21 from cs_d5_scene_21_return\n    $ cs_d5_done = True')
    text=text.replace('    call screen cs_day05_end_screen\n    jump cs_day05_complete','    if not cs_d5_missing_minute_done:\n        call cs_day05_21 from cs_d5_legacy_missing_minute_return\n    jump cs_day06')
    # Old saves can be suspended inside the former final modal screen.
    a=text.index('screen cs_day05_end_screen():')
    text=text[:a]+'screen cs_day05_end_screen():\n    timer 0.1 action Jump("cs_day05_complete")\n'
    flow.write_text(text,encoding='utf-8')
    p=ROOT/'days/day05/20_scene.rpy';text=p.read_text(encoding='utf-8')
    tail='    hide screen cs_d5_insert\n    hide screen cs_d5_clock_face\n    hide screen cs_d5_notes\n'
    cut=text.rfind(tail)
    if cut!=-1:text=text[:cut]+'    return\n'
    p.write_text(text,encoding='utf-8')
    script=['# -*- coding: utf-8 -*-','label cs_day05_21:','    if cs_d5_missing_minute_done:','        return','    $ save_name = "Чужая смена — День 5: Пропавшая минута"','    $ cs_d5_scene = 20','    $ cs_d5_room("bg int_house_of_mt_night")','    $ cs_d5_clock = "23:59"','    show screen cs_d5_clock_face','    $ cs_d5_focus("mz")','    with cs_sprite_enter']
    # Preserve the authored reaction when electricity returns after the blackout.
    light_return=(ROOT/'source/day05/light_return.rpy.txt').read_text(encoding='utf-8').splitlines()
    light_at=script.index('    $ cs_d5_room("bg int_house_of_mt_night")')
    script[light_at:light_at+1]=light_return
    # Emit the added scene with existing Day 5 staging, not the Day 6 director.
    body=emit(139,171).replace('cs_d6_focus','cs_d5_focus').replace('cs_d6_think','cs_pov_begin')
    body=body.replace('Женя попросила повторить последнюю фразу.', 'Женя сделала пометку и попросила повторить, на чём мы остановились.')
    for line in body.splitlines():
        script.append('    '+line)
        if line.startswith('$ cs_d5_focus('):script.append('    with cs_sprite_change')
    pos=next(i for i,x in enumerate(script) if 'Я посмотрела на часы.' in x)
    optional=[]
    for flag,who,text in [('slavya','sl','Славя опустилась на свободный стул, так и не убрав плед.'),('alisa','dv','Алиса пыталась что-то сказать и закрыла глаза, опершись о стену.'),('miku','mi','Мику прижала ладонь ко лбу и попросила не вставать без неё.')]:
        optional+=['    if cs_d5_'+flag+'_present:','        cs_narrator '+q(text)]
    script[pos:pos]=optional
    cgpos=next(i for i,x in enumerate(script) if 'Даша придвинулась ближе' in x)
    script[cgpos:cgpos]=['    $ cs_director_scene("cs_cg_day05_missing_minute")','    scene cs_cg_day05_missing_minute with Dissolve(0.7)']
    script+=['    $ cs_d5_missing_minute_done = True','    hide screen cs_d5_clock_face','    hide screen cs_d5_notes','    hide screen cs_d5_insert','    $ cs_bus_cue("silence")','    window hide dissolve','    $ cs_director_scene("black")','    scene black with Dissolve(1.0)','    return','']
    (ROOT/'days/day05/21_scene.rpy').write_text('\n'.join(script),encoding='utf-8')

def apply_location_fixes():
    edits=json.loads((ROOT/'source/day06/location_fixes.json').read_text(encoding='utf-8'))
    for edit in edits:
        path=OUT/edit['file']
        text=path.read_text(encoding='utf-8')
        if text.count(edit['old'])!=edit['count']:
            raise ValueError(('Day 6 location anchor changed',edit['file'],edit['old']))
        path.write_text(text.replace(edit['old'],edit['new']),encoding='utf-8')

def apply_attention_cuts():
    """Authored prose/action beats, not an automatic hide on every narration."""
    anchors=json.loads((ROOT/'source/day06/attention_cuts.json').read_text(encoding='utf-8'))
    hits={text:0 for text in anchors}
    for path in sorted(OUT.glob('[0-9][0-9]_scene.rpy')):
        result=[]
        for line in path.read_text(encoding='utf-8').splitlines():
            text=line.strip()
            for anchor in anchors:
                if text=='cs_narrator '+q(anchor):
                    hits[anchor]+=1
                    if not result or result[-1].strip()!='$ cs_d6_think()':
                        result.append(line[:len(line)-len(line.lstrip())]+'$ cs_d6_think()')
                    break
            result.append(line)
        path.write_text('\n'.join(result)+'\n',encoding='utf-8')
    missing=[text for text,count in hits.items() if not count]
    if missing:raise ValueError(('Missing authored attention cue',missing))
    return hits

def build():
    OUT.mkdir(parents=True,exist_ok=True)
    defaults={'cs_d5_missing_minute_done':False,'cs_d6_started':False,'cs_d6_done':False,'cs_d6_friend_on_arrival':{},'cs_d6_choice_results':{},'cs_d6_help':None,'cs_d6_outfit':'pioneer','cs_d6_room_image':None,'cs_d6_cast':[],'cs_d6_allowed':[]}
    defaults.update(cs_d6_book_borrowed=False,cs_d6_book_location=None,cs_d6_library_key_location='olga',cs_d6_firstaid_location='viola',cs_d6_olga_copy=False)
    for flag in 'mz_listened mz_independent un_independent un_private archive_guide archive_compared sketch_done mz_address_received se_address_offered se_address_received un_sketch_received sl_badge_received dv_pick_received mi_music_received mi_known_motif mi_motif_tried se_account_received se_agency place_recorded bus_departed towels_carried viola_documents_shared fifth_tray_locked items_packed'.split():defaults['cs_d6_'+flag]=False
    code='# -*- coding: utf-8 -*-\n'+''.join('default %s = %r\n'%(k,v) for k,v in defaults.items())
    code+='init -9 python:\n    cs_state_defaults.update('+','.join(k+'='+repr(v) for k,v in defaults.items())+')\n'
    for item in json.loads((ROOT/'cg/day06_cg_fullhd/manifest.json').read_text(encoding='utf-8')):
        name=Path(item['file']).stem.removeprefix('cg_')
        code+='image cs_cg_%s = im.Scale(cs_resolve_asset(%s),1920,1080)\n'%(name,q('cg/day06_cg_fullhd/'+item['file']))
    code+=(ROOT/'tools/day06_runtime.rpy.txt').read_text(encoding='utf-8')
    (OUT/'resources.rpy').write_text(code,encoding='utf-8')
    scenes=[('Утро без записей',175,312),('Сборы',315,430),('Автобус',432,540),('Свободный час',543,625),('Бумаги под землёй',627,696),('До ужина',699,764),('Лишний прибор',766,847),('До утра',849,940)]
    for num,(title,a,b) in enumerate(scenes,1):
        code='# -*- coding: utf-8 -*-\nlabel cs_day06_%02d:\n    $ save_name = %s\n'%(num,q('Чужая смена — День 6: '+title))
        
        if num==3:
            code+=ind(room('bg int_dining_hall_people_day',DIN)+'\nplay sound \"sound/sfx/dinner_horn_processed.ogg\"\n'+s('narrator|На обед мы пришли вместе. За разговорами о багаже еду разобрали быстро; потом каждый отправился за своей сумкой.'))+'\n'
        code+=ind(emit(a,b))+'\n    return\n'
        (OUT/('%02d_scene.rpy'%num)).write_text(code,encoding='utf-8')
    flow=['# -*- coding: utf-8 -*-','label cs_day06:','    hide screen cs_day05_end_screen','    if cs_d6_done:','        jump cs_day06_complete','    $ cs_d6_begin()','    call cs_day_title(6) from cs_d6_title_return','    $ cs_rev_time("day")','    window show dissolve']
    for n in range(1,9):flow+=['    call cs_day06_%02d from cs_d6_scene_%02d_return'%(n,n)]
    flow+=['    $ cs_d6_done = True','    $ cs_bus_cue("silence")','    stop music fadeout 1.5','    stop sound fadeout 0.5','    window hide dissolve','    $ cs_director_scene("black")','    scene black with Dissolve(1.0)','label cs_day06_complete:','    label cs_check_day06_complete:','    call screen cs_day06_end_screen','    jump cs_day06_complete','']
    (OUT/'00_flow.rpy').write_text('\n'.join(flow),encoding='utf-8')
    apply_attention_cuts()
    apply_location_fixes()
    integrate_day5()
    print('Day 6: eight parts, four decisions, twelve CG registrations; Day 5 missing minute linked.')

if __name__=='__main__':
    if '--day5-only' in sys.argv:integrate_day5()
    else:build()
