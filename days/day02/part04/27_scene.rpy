# -*- coding: utf-8 -*-
label cs_day02_27:
    $ save_name = "Чужая смена — День 2: Незначительные повреждения"
    $ cs_part03_live = False
    $ cs_part04_live = True
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    $ cs_part04_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.2, channel="music", delay=1.0)
    label cs_check_part04_s27:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы вышли на крыльцо."
    cs_narrator "Солнце уже поднялось достаточно высоко."
    cs_narrator "Воздух стал заметно теплее."
    cs_narrator "Я машинально поправила галстук."
    cs_narrator "И только теперь почувствовала неприятное жжение на локте."
    cs_narrator "Посмотрела вниз."
    cs_narrator "На коже виднелась небольшая царапина."
    cs_th "А это ещё откуда?"
    cs_narrator "Я вспомнила, как возле входа в кружок задела рукой шероховатый край деревянного косяка."
    cs_narrator "Тогда даже не обратила внимания."
    cs_narrator "Теперь же царапина напоминала о себе."
    cs_narrator "Дарья заметила, куда я смотрю."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен, ты поцарапалась?"
    cs_ls "Похоже на то."
    cs_narrator "Она подошла ближе."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Покажи."
    cs_narrator "Я повернула руку."
    cs_narrator "Дарья осмотрела повреждение."
    cs_da "Небольшая. Но лучше обработать."
    cs_ls "Организм, конечно, предпочёл бы просто забыть о её существовании."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А ты предпочла бы потом вспоминать, где именно её получила?"
    cs_narrator "Я задумалась."
    cs_ls "Аргумент принят."
    cs_narrator "Семён посмотрел на нас."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "В медпункт сходите?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Думаю, да."
    cs_narrator "Я подняла взгляд."
    cs_th "Медпункт."
    cs_th "Точно."
    cs_narrator "И сразу вспомнила знакомый интерьер из игры."
    cs_narrator "Белые шкафы."
    cs_narrator "Кушетка."
    cs_narrator "Рабочий стол."
    cs_narrator "И медсестра, которая умела разговаривать так, что даже Семён иногда терялся."
    cs_th "Виола."
    cs_th "Ну здравствуйте."
    cs_narrator "Семён тем временем взял папку с бумагой и карандашами, оставленную у нашего рабочего стола."
    cs_sy "Я тогда уточню время выступления и подожду вас возле клубов."
    cs_ls "Только бумагу не потеряй."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я уже понял."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Скоро вернёмся."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part04_semen_left:
    cs_narrator "Он кивнул и направился к площади."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_director_check_3d08506588:
    # cs_director_end
    cs_narrator "Я посмотрела на Дашу."
    cs_ls "Ну что, идём знакомиться с местной медициной?"
    cs_da "Идём обрабатывать твою руку."
    cs_narrator "Я улыбнулась."
    cs_ls "Формулировка менее торжественная, но вполне точная."
    cs_narrator "Мы свернули на дорожку, ведущую к медпункту."
    return
