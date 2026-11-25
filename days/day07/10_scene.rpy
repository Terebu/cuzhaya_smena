# -*- coding: utf-8 -*-

label cs_day07_10:
    $ cs_d7_scene("bg int_dining_hall_day")
    stop ambience fadeout 0.8
    scene bg int_dining_hall_day with dissolve
    cs_narrator "Обед прошёл быстро, спокойно и почти по-домашнему."
    cs_narrator "Никаких прощальных речей, никакого лишнего пафоса."
    cs_narrator "Ольга разогрела лёгкий куриный суп, нарезала свежий хлеб, разлила по кружкам прохладный яблочный компот."
    cs_narrator "Мы ели не спеша, перебрасываясь короткими фразами про дорогу."
    cs_narrator "Ольга вполголоса прикидывала, какие ключи ещё надо сдать в хозкорпус, а Виола подшучивала, что теперь у них наконец-то начнётся тихий сезон без внезапных ночных совещаний."
    show mt normal pioneer at cleft
    show cs_darya neutral pioneer at cs_darya_normal_center
    show cs custom serious medical normal at cs_viola_normal_right
    with dissolve
    mt "Даже немного непривычно будет."
    cs_narrator "Призналась Ольга, отставляя кружку."
    mt "Сначала шумит весь лагерь, потом четверо, а через полчаса останемся вдвоём с Виолой."
    cs_ls "Зато никто не будет приносить вам папки из подвала к половине шестого."
    cs_narrator "Напомнила я."
    mt "Ну, по этому я точно не соскучусь."
    cs_narrator "Рассмеялась вожатая."
    $ cs_bus_engine("distant")
    cs_narrator "Где-то далеко за соснами послышался знакомый низкий гул дизеля."
    cs_narrator "Мы с Дашей переглянулись."
    cs_narrator "На этот раз никто не напрягся и не стал считать секунды."
    $ cs_d7_hide_portraits()
    with dissolve
    $ cs_rev_sfx("sound/sfx/knock_glass.ogg", 0.12)
    cs_narrator "Я допила компот, и мы быстро отнесли тарелки на раздачу."
    $ cs_d7_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day with dissolve
    $ cs_d7_ambience("sound/ambiences/int_cabin_day.ogg")
    cs_narrator "В домике мы забрали сумки."
    $ cs_d7_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day with dissolve
    $ cs_d7_ambience("sound/ambiences/forest_day.ogg")
    $ cs_rev_sfx("sound/sfx/lock_close.ogg", 0.16)
    cs_narrator "Последний раз щёлкнула задвижка на нашей двери, и мы пошли к воротам."
    $ cs_d7_scene("bg ext_bus")
    scene bg ext_bus with dissolve
    $ cs_d7_ambience("sound/ambiences/forest_day.ogg")
    $ cs_bus_engine("idle")
    cs_narrator "Когда мы вышли на дорогу, автобус уже стоял на обочине и лениво урчал на холостых."
    cs_narrator "Тот самый, знакомый по вчерашнему отъезду смены: чуть пыльный по бокам, с приоткрытой форточкой у кабины, тряпкой на переднем стекле и слегка дребезжащей крышкой у водительского места."
    cs_narrator "За рулём сидел Пётр."
    cs_narrator "Увидев нас с Ольгой, он вышел на ступеньки с путевым листом в руках и спокойно кивнул."
    cs_d6_driver "Всё по графику, Ольга Дмитриевна."
    cs_d6_driver "Отдельный рейс, две пассажирки."
    cs_d6_driver "Багаж в салон закинем, места сегодня полно — можно хоть на первом ряду, хоть на последнем."
    mt "Спасибо, Пётр."
    mt "Документы в порядке?"
    cs_d6_driver "Как всегда, проверяйте."
    cs_narrator "Ольга быстро пробежала глазами бумагу, поставила подпись и отдала лист обратно водителю."
    show mt normal pioneer at cleft
    show cs custom serious medical normal at cs_viola_normal_right
    with dissolve
    cs_narrator "Потом повернулась к нам."
    cs_narrator "Виола стояла рядом, засунув руки в карманы белого халата."
    mt "Ну всё, девочки."
    cs_narrator "Сказала Ольга, коротко и крепко обнимая сначала Дашу, потом меня."
    mt "Все формальности закрыты."
    mt "Доедете спокойно — и ни о чём лишнем больше не переживайте."
    cs "Воду взяли?"
    cs_narrator "Уточнила Виола, кивая на наши рюкзаки."
    cs "Отлично."
    cs "Высыпайтесь обе и не ищите приключений там, где их нет."
    cs_ls "Постараемся."
    cs_narrator "Ответила я, и на этот раз это прозвучало не как дежурная отговорка."
    $ cs_bus_stock_sound(cs_bus_door_open, 0.32)
    $ cs_d7_hide_portraits()
    show cs_cg_d7_farewell with dissolve
    cs_narrator "Пётр помог закинуть сумки в салон."
    cs_narrator "Я пропустила Дашу вперёд по высоким ступенькам, на секунду сжала ей запястье и поднялась следом."
    $ cs_d7_scene("bg int_bus")
    $ cs_bus_engine("off")
    $ cs_d7_ambience(cs_bus_idle, 0.12)
    scene bg int_bus with dissolve
    cs_narrator "Внутри пахло нагретым на солнце дерматином, сухой пылью и старым бензином — самый обычный запах междугороднего автобуса."
    cs_narrator "Кроме нас двоих, в длинном ряду сидений никого не было."
    cs_narrator "Прежде чем Пётр нажал кнопку и двери с шипением поехали навстречу друг другу, я всё-таки позволила себе один короткий взгляд назад, через широкое окно на территорию «Совёнка»."
    cs_narrator "У ворот стояли Ольга Дмитриевна и Виола, обе махали на прощание."
    cs_narrator "За их спинами тянулась пустая дорожка к площади, крыши домиков и тёмная полоса сосен возле библиотеки."
    cs_narrator "Там было совершенно пусто."
    cs_narrator "Никакой третьей фигуры."
    cs_narrator "Никакой похожей девушки в тени деревьев."
    cs_narrator "Просто летний лагерь, в котором закончилась смена."
    $ cs_bus_stock_sound(cs_bus_door_close, 0.32)
    cs_narrator "Двери глухо захлопнулись."
    $ cs_d7_ambience(cs_bus_moving)
    cs_narrator "Автобус мягко тронулся, вывернул за ворота и покатил по лесной дороге."
    cs_narrator "Я больше не оборачивалась и спокойно села на сиденье рядом с Дашей."
    $ cs_d7_departed = True
    jump cs_day07_11
