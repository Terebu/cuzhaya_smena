# -*- coding: utf-8 -*-
label cs_day02_63:
    $ save_name = "Чужая смена — День 2: Мем материализовался"
    $ cs_part08_live = False
    $ cs_part09_live = True
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    label cs_check_part09_s63:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Очередь постепенно продвигалась. Я посмотрела на раздачу, затем на тарелки впереди. И внезапно замерла."
    cs_th "Нет."
    cs_th "Не может быть."
    cs_narrator "Картофельное пюре. Котлеты. Я медленно повернулась к Дарье. Она сразу заметила выражение моего лица."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Даша."
    cs_da "Что?"
    cs_narrator "Я указала на раздачу."
    cs_ls "Ты видишь?"
    cs_narrator "Она посмотрела."
    cs_da "Котлеты?"
    cs_ls "С пюрешкой."
    cs_narrator "Дарья несколько секунд смотрела на меня. Потом закрыла глаза. И начала смеяться."
    cs_da "Ты серьёзно?"
    cs_ls "Абсолютно!"
    cs_narrator "Я снова посмотрела на тарелки."
    cs_th "Вот ведь. Сначала вспомнила старый мем по дороге. А теперь ужин решил буквально воспроизвести его содержание. Какова вероятность?"
    cs_narrator "Женя обернулась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Что у вас опять?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Небольшое культурное совпадение."
    cs_narrator "Она нахмурилась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Какое ещё совпадение?"
    cs_ls "Просто у меня дома была одна старая шуточная песенка. Про котлеты и пюре."
    cs_narrator "Женя посмотрела на раздачу, потом на меня."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И?"
    cs_narrator "Я развела руками."
    cs_ls "И теперь вот они."
    cs_narrator "Она несколько секунд молчала."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Соколова, это обычный ужин."
    cs_ls "Именно поэтому совпадение особенно прекрасно."
    cs_narrator "Женя вздохнула."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "У тебя очень странные представления о прекрасном."
    cs_narrator "Дарья улыбнулась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Она сегодня вспоминает старый интернет."
    cs_narrator "Женя посмотрела на нас обеих."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Старый что?"
    cs_narrator "Я на секунду замерла."
    cs_th "Ах да. Разные культурные контексты."
    cs_ls "Долгая история."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Я так и думала."
    cs_narrator "Она взяла поднос."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Может, сначала поедим?"
    cs_narrator "Я торжественно кивнула."
    cs_ls "Разумное предложение."
    cs_narrator "Мы подошли к раздаче. Получили ужин. И я некоторое время просто рассматривала тарелку. Картофельное пюре."
    cs_narrator "Котлета. Совершенно обычная еда. В совершенно необычном месте."
    cs_th "А ведь дома я могла бы даже не обратить внимания. Сфотографировала бы какую-нибудь ерунду, отправила знакомым и пошла дальше. А здесь даже телефон не включить."
    cs_narrator "Я невольно улыбнулась."
    cs_th "Может, это и к лучшему. Некоторые вещи можно просто запомнить."
    cs_narrator "Женя уже направилась к столам. Дарья легко коснулась моего плеча."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я повернулась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты собираешься ужинать или продолжишь изучать котлету?"
    cs_ls "Полагаю, научная экспертиза завершена."
    cs_narrator "Она засмеялась. И мы отправились искать свободные места."
    return
