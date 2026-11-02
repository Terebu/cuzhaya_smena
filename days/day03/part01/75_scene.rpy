# -*- coding: utf-8 -*-
label cs_day03_75:
    $ save_name = "Чужая смена — День 3: Утро без согласования"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_day03_dawn
    with Dissolve(0.8)
    $ cs_frame_focus([])
    play ambience "sound/ambiences/int_cabin_day.ogg" fadein 2.0
    $ renpy.music.set_volume(0.16, channel="ambience")
    play music "sound/music/my_daily_life.ogg" fadein 3.0
    $ renpy.music.set_volume(0.2, channel="music")
    label cs_check_day03_75:
    cs_narrator "Проснулась я раньше горна. Опять. Я села. Локоть потянуло, стоило согнуть руку. Повязка держалась, свежей крови не было. Но бегать сегодня ещё рано."
    cs_th "Вчера я уже выяснила, что человеческое тело не любит знакомиться с корнями деревьев. Прогуляться, впрочем, никто не запрещал."
    cs_narrator "На соседней кровати спала Дарья. Красные пряди растрепались по подушке. Она лежала на боку, натянув одеяло до плеч. Вчера она собиралась пойти со мной. Но сейчас будить её не хотелось. Я достала футболку, шорты и кроссовки."
    cs_narrator "Переоделась, стараясь не задевать повязку. Собрала волосы так, чтобы они не мешали."
    $ cs_director_scene("cs_cg_lena_sport_mirror_bandaged_morning")
    scene cs_cg_lena_sport_mirror_bandaged_morning at cs_day03_dawn
    with Dissolve(0.8)
    label cs_check_day03_mirror:
    cs_narrator "Потом посмотрела на себя."
    cs_th "Неплохо. Спортивная форма и забинтованный локоть. Убедительная реклама здорового образа жизни."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_day03_dawn
    with Dissolve(0.8)
    cs_narrator "Я тихо усмехнулась. У двери я обернулась к Дарье."
    cs_ls "Я ненадолго. Скоро вернусь."
    cs_narrator "Она не проснулась. Я и не ждала ответа."
    cs_th "Хотя записку, наверное, оставить стоит."
    cs_narrator "После вчерашнего разговора с Ольгой Дмитриевной у ворот выходить без предупреждения уже не хотелось. Нашла листок и карандаш, написала: «Даш, я вышла прогуляться по лагерю. За ворота не хожу, подвиги не совершаю. Скоро вернусь. Лена»."
    cs_narrator "Посмотрела на написанное."
    cs_th "«Подвиги» несколько снижают убедительность записки. Но сойдёт."
    cs_narrator "Оставила записку на тумбочке, где Дарья наверняка её заметит. Потом осторожно открыла дверь."
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day at cs_day03_dawn
    with Dissolve(0.8)
    cs_narrator "И вышла наружу."
    return
