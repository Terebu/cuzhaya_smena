# -*- coding: utf-8 -*-
label cs_day02_concert:
    $ save_name = "Чужая смена — День 2: Музыкальный вечер"
    $ cs_part09_live = False
    $ cs_director_scene("bg ext_square_sunset")
    scene bg ext_square_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    if cs_sl_good_seats:
        # cs_director_begin: entry frame; explicit scene plan
        $ cs_frame_focus(["cs_darya"])
        with cs_sprite_change
        # cs_director_end
        cs_narrator "Мы вернулись к местам у края первого ряда. Отсюда сцену было видно целиком."
    else:
        cs_narrator "Мы устроились сбоку. Между головами зрителей было хорошо видно инструменты и обеих исполнительниц."
    cs_narrator "Последний раз щёлкнул переключатель усилителя. Разговоры перед сценой постепенно стихли."
    cs_narrator "Алиса провела ладонью по струнам, прислушалась и коротко кивнула Мику."
    cs_da "Кажется, начинается."
    cs_ls "Угу. Теперь можно просто слушать."
    if cs_friend_viola >= 2:
        show cs custom warm_smile medical normal at cs_viola_normal_left
        $ cs_presence_stage()
        with cs_sprite_enter
        cs_vi "Лена, на минутку. Вот, возьми про запас."
        cs_narrator "Виола протянула маленький свёрток с чистой повязкой. К локтю она не прикоснулась."
        cs_vi "Сегодня ничего менять не нужно. Если понадобится, зайдёшь ко мне."
        cs_ls "Спасибо. Я помню: без новых подвигов."
        cs_vi "Вот и договорились. Хорошего вечера."
        # cs_director_begin: Viola goes back to audience; no new treatment
        $ cs_frame_focus(["cs_darya"])
        with cs_sprite_change
        label cs_director_check_5a4b095373:
        # cs_director_end
        $ cs_viola_spare_bandage = True
    if cs_met_un and cs_friend_un >= 1:
        $ cs_un_name_known = True
        show un shy pioneer at cs_actor_left
        $ cs_presence_stage()
        with cs_sprite_enter
        cs_un "Лена… Я попробую зарисовать выступление. Потом показать тебе?"
        cs_ls "Конечно. Мне очень интересно, что ты заметишь."
        show un smile pioneer at cs_actor_left
        $ cs_presence_stage()
        with cs_sprite_change
        cs_un "Тогда после. Только это будет быстрый набросок."
        # cs_director_begin: Tikhonova resumes drawing offscreen
        $ cs_frame_focus(["cs_darya"])
        with cs_sprite_change
        label cs_director_check_ab2534ea89:
        # cs_director_end
    cs_narrator "Ольга Дмитриевна попросила тех, кто ещё стоял, занять места."
    cs_mt "Ну что, все готовы? Девочки, вам слово."
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.04, channel="ambience", delay=1.5)
    $ cs_director_scene("cs_cg_square_concert_evening")
    scene cs_cg_square_concert_evening
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.65, channel="cs_piano")
    play cs_piano "sound/music/miku_song_voice.ogg" noloop fadein 1.0
    label cs_check_finale_concert_wide:
    cs_narrator "Мику взяла первые ноты. Алиса вступила чуть позже, не перекрывая мелодию."
    if cs_mi_intro_revised:
        cs_narrator "Я узнала вступление. Мику оставила в нём больше воздуха — именно так, как решила на утренней репетиции."
        cs_da "Слышишь? Она всё-таки сократила начало."
        cs_ls "Да. И мелодия сразу дышит свободнее."
    else:
        cs_narrator "Вступление оказалось коротким и тихим. Оно не требовало внимания — просто постепенно собирало его."
    cs_narrator "Мику уже не спешила объяснять, что сейчас будет. Музыка говорила за неё."
    cs_narrator "Алиса смотрела на подругу и ловила движение её плеча, чтобы вступить точно в нужный момент."
    cs_narrator "Гитарные струны добавляли мелодии глубины. За первым рядом кто-то перестал шуршать бумажным пакетом."
    cs_narrator "Я устроила повреждённую руку поудобнее и выдохнула."
    cs_th "Никуда не торопиться. Ничего не проверять."
    cs_th "Просто побыть здесь."
    window hide dissolve
    pause 12.0
    $ cs_director_scene("cs_cg_square_concert_close")
    scene cs_cg_square_concert_close
    with Dissolve(2.0)
    window show dissolve
    label cs_check_finale_concert_close:
    cs_narrator "Мелодия поднялась выше. В голосе Мику появилась уверенность, которой утром ещё мешало волнение."
    cs_narrator "Алиса чуть улыбнулась. Здесь не было привычной перепалки — только внимательный взгляд и следующая вовремя взятая нота."
    cs_da "Они хорошо слышат друг друга."
    cs_ls "Наверное, иначе вместе и не сыграешь."
    cs_narrator "Я говорила вполголоса и больше не пыталась продолжить разговор."
    cs_narrator "Где-то за деревьями прошёл ветер. На сцене качнулся край Микуного галстука."
    cs_th "Потом мы опять будем думать о дороге."
    cs_th "Но этот вечер тоже настоящий."
    window hide dissolve
    pause 18.0
    window show dissolve
    cs_narrator "К последней фразе сопровождение стало тише. Алиса сняла руку со струн, оставив последней ноте время прозвучать."
    cs_narrator "На секунду площадь замерла. Затем с разных сторон раздались аплодисменты."
    cs_narrator "Я хлопала осторожно, почти не двигая больным локтем. Дарья улыбалась рядом."
    stop cs_piano fadeout 4.0
    $ cs_director_scene("bg ext_square_sunset")
    scene bg ext_square_sunset
    show mi happy pioneer at cs_actor_left
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(1.5)
    cs_mi "Спасибо вам! Я так волновалась, а теперь даже жалко, что уже всё!"
    cs_ls "Очень красиво получилось."
    if cs_mi_intro_revised:
        cs_mi "И начало теперь получилось как надо. Спасибо, что утром послушали!"
    else:
        cs_mi "Как хорошо, что вы пришли!"
    cs_da "Спасибо за музыку."
    cs_narrator "Алиса убрала гитару в сторону и махнула нам со сцены."
    if cs_friend_se >= 2:
        show cs_semen smile pioneer normal at cs_semen_normal_right
        $ cs_presence_stage()
        with cs_sprite_enter
        # cs_director_begin: Semen talks to the girls after the concert
        $ cs_frame_focus(["cs_darya", "cs_semen"])
        with cs_sprite_change
        label cs_director_check_515c9e8f55:
        # cs_director_end
        cs_sy "Ну как? Удалось хоть немного отдохнуть от наших исследований?"
        cs_ls "Удалось. И я даже никого не спрашивала про автобус."
        cs_sy "Запишем как успех. Остальное завтра, ладно?"
        cs_ls "Ладно. Сегодня хватит."
    if cs_met_un and cs_friend_un >= 1:
        show un smile pioneer at cs_actor_left
        $ cs_presence_stage()
        with cs_sprite_enter
        # cs_director_begin: Close viewpoint on the sketch, others remain offscreen
        $ cs_frame_focus(["cs_darya", "un"])
        with cs_sprite_change
        label cs_director_check_cf54d8590f:
        # cs_director_end
        cs_un "Вот… Я обещала показать."
        cs_narrator "На листе были два быстрых силуэта и несколько линий инструментов. Но наклон головы Мику узнавался сразу."
        cs_ls "Ты поймала момент, когда они посмотрели друг на друга."
        cs_un "Мне тоже он понравился."
        $ cs_un_concert_sketch_seen = True
    $ cs_day02_concert_done = True
    label cs_check_finale_concert_done:
    return
