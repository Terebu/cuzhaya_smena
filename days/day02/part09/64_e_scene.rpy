# -*- coding: utf-8 -*-
label cs_day02_64e:
    $ save_name = "Чужая смена — День 2: Семён и вечерние планы"
    $ cs_part09_live = True
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    label cs_check_dinner64e:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"] if cs_friend_mz >= 1 else ["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "К тому времени мы уже почти закончили ужинать."
    cs_narrator "Пюре действительно оказалось вкусным."
    cs_narrator "Котлета тоже."
    cs_narrator "И, к моему удивлению, за всё время я ни разу не почувствовала необходимости снова запеть знакомую песенку."
    cs_th "Личностный рост."
    cs_th "Причём совершенно без дополнительных медицинских вмешательств."
    cs_narrator "Я взяла стакан."
    cs_narrator "Сделала несколько глотков."
    cs_narrator "И заметила Семёна."
    cs_narrator "Он шёл между столами с пустым подносом."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen neutral pioneer far at cs_semen_far_center
        show cs_darya shrug pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen neutral pioneer normal at cs_semen_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    label cs_check_part09_semen:
    cs_narrator "Увидев нас, остановился."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen smile pioneer far at cs_semen_far_center
        show cs_darya shrug pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen smile pioneer normal at cs_semen_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_sy "О, вы ещё здесь."
    cs_narrator "Я подняла голову."
    cs_ls "Товарищ Семён. Какая неожиданная встреча в единственном заведении общественного питания на территории лагеря."
    cs_narrator "Он усмехнулся."
    cs_sy "Очень смешно."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen smile pioneer far at cs_semen_far_center
        show cs_darya thinking pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen smile pioneer normal at cs_semen_normal_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_da "Уже поужинал?"
    cs_narrator "Он поднял пустой поднос."
    cs_sy "Как видишь."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Неоспоримое доказательство."
    cs_narrator "Семён посмотрел на мой локоть."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen thinking pioneer far at cs_semen_far_center
        show cs_darya thinking pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen thinking pioneer normal at cs_semen_normal_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_sy "Рука как?"
    cs_ls "На месте."
    cs_sy "Это я вижу. Болит?"
    cs_narrator "Я немного помолчала."
    cs_ls "Если не трогать, почти не беспокоит."
    cs_narrator "Он кивнул."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen smile pioneer far at cs_semen_far_center
        show cs_darya thinking pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen smile pioneer normal at cs_semen_normal_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_sy "Ну и хорошо."
    cs_narrator "Затем посмотрел в сторону выхода."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen thinking pioneer far at cs_semen_far_center
        show cs_darya thinking pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen thinking pioneer normal at cs_semen_normal_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_sy "А вы на концерт собираетесь?"
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen thinking pioneer far at cs_semen_far_center
        show cs_darya shrug pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen thinking pioneer normal at cs_semen_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_da "Конечно. Мы как раз после ужина пойдём."
    cs_ls "Надо же оценить результаты собственного художественного труда."
    cs_narrator "Семён улыбнулся."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer far at cs_darya_far_left
        show cs_semen smile pioneer far at cs_semen_far_center
        show cs_darya shrug pioneer far at cs_darya_far_right
        $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_semen smile pioneer normal at cs_semen_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    cs_sy "Плакат действительно неплохо получился."
    cs_narrator "Я торжественно кивнула."
    cs_ls "Спасибо. Художественный отдел принимает положительные отзывы."
    if cs_friend_se >= 2:
        cs_narrator "Семён немного задержался."
        cs_narrator "Посмотрел на мою перевязанную руку."
        cs_narrator "Потом снова на Дарью."
        if cs_friend_mz >= 1:
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
            # cs_presence_keep: hide cs_dasha_winter
            # cs_presence_keep: hide cs_dasha_pioneer
            show cs_zhenya normal pioneer far at cs_darya_far_left
            show cs_semen explaining pioneer far at cs_semen_far_center
            show cs_darya shrug pioneer far at cs_darya_far_right
            $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
            $ cs_presence_stage()
            # cs_global_transition
            with cs_sprite_change
        else:
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
            # cs_presence_keep: hide cs_dasha_winter
            # cs_presence_keep: hide cs_dasha_pioneer
            show cs_semen explaining pioneer normal at cs_semen_normal_left
            show cs_darya shrug pioneer normal at cs_darya_normal_right
            $ cs_part09_cast = ["cs_semen", "cs_darya"]
            $ cs_presence_stage()
            # cs_global_transition
            with cs_sprite_change
        cs_sy "Слушайте, я после ужина всё равно собирался помочь со скамейками. Могу узнать у Слави, где вам будет удобнее сесть."
        cs_narrator "Я удивилась."
        cs_ls "Нам?"
        if cs_friend_mz >= 1:
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
            # cs_presence_keep: hide cs_dasha_winter
            # cs_presence_keep: hide cs_dasha_pioneer
            show cs_zhenya normal pioneer far at cs_darya_far_left
            show cs_semen smile pioneer far at cs_semen_far_center
            show cs_darya shrug pioneer far at cs_darya_far_right
            $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
            $ cs_presence_stage()
            # cs_global_transition
            with cs_sprite_change
        else:
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
            # cs_presence_keep: hide cs_dasha_winter
            # cs_presence_keep: hide cs_dasha_pioneer
            show cs_semen smile pioneer normal at cs_semen_normal_left
            show cs_darya shrug pioneer normal at cs_darya_normal_right
            $ cs_part09_cast = ["cs_semen", "cs_darya"]
            $ cs_presence_stage()
            # cs_global_transition
            with cs_sprite_change
        cs_sy "Ну да. Чтобы не пришлось пробираться через толпу с больной рукой."
        cs_narrator "Я посмотрела на него."
        cs_th "Надо же."
        cs_th "А ведь он сам об этом подумал."
        cs_ls "Спасибо. Только не надо специально никого пересаживать."
        cs_sy "Не собирался. Просто узнаю, где остались свободные места."
        cs_narrator "Дарья улыбнулась."
        cs_da "Было бы здорово."
        cs_narrator "Семён кивнул."
        cs_sy "Тогда до встречи."
    else:
        cs_narrator "Семён посмотрел на часы."
        cs_sy "Ладно, я побежал. Ещё обещал помочь с подготовкой."
        cs_narrator "Я улыбнулась."
        cs_ls "Только внимательно смотри под ноги."
        cs_narrator "Он посмотрел на мою руку."
        cs_narrator "Потом на меня."
        cs_narrator "И рассмеялся."
        if cs_friend_mz >= 1:
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
            # cs_presence_keep: hide cs_dasha_winter
            # cs_presence_keep: hide cs_dasha_pioneer
            show cs_zhenya normal pioneer far at cs_darya_far_left
            show cs_semen thinking pioneer far at cs_semen_far_center
            show cs_darya shrug pioneer far at cs_darya_far_right
            $ cs_part09_cast = ["cs_zhenya", "cs_semen", "cs_darya"]
            $ cs_presence_stage()
            # cs_global_transition
            with cs_sprite_change
        else:
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
            # cs_presence_keep: hide cs_dasha_winter
            # cs_presence_keep: hide cs_dasha_pioneer
            show cs_semen thinking pioneer normal at cs_semen_normal_left
            show cs_darya shrug pioneer normal at cs_darya_normal_right
            $ cs_part09_cast = ["cs_semen", "cs_darya"]
            $ cs_presence_stage()
            # cs_global_transition
            with cs_sprite_change
        cs_sy "Это ты мне говоришь?"
        cs_narrator "Я кивнула."
        cs_ls "Исключительно из личного опыта."
    if cs_friend_mz >= 1:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    label cs_check_part09_semen_left:
    cs_narrator "Семён попрощался и отправился к выходу."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_director_check_85a673846b:
    # cs_director_end
    cs_narrator "Я проводила его взглядом."
    cs_th "Забавно."
    # cs_director_begin: REFLECTIVE_SHOT: Independent events beyond the known story
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_8bd08eb62b:
    # cs_director_end
    cs_th "Ещё вчера мы обсуждали, почему все трое оказались в этом лагере."
    cs_th "Сегодня уже вместе рисовали объявление, проверяли дорогу и теперь собирались на концерт."
    cs_narrator "И чем дольше я здесь находилась, тем меньше всё происходящее напоминало обычную историю из игры."
    cs_narrator "Не потому, что знакомых событий стало меньше."
    cs_narrator "А потому, что между ними появлялось всё больше совершенно самостоятельных разговоров."
    cs_narrator "Поступков."
    cs_narrator "Решений."
    cs_narrator "Вещей, которых я никогда раньше не видела."
    if cs_friend_mz >= 1:
        # cs_director_begin: Return to direct interaction: Independent events beyond the known story
        $ cs_frame_focus(["cs_darya", "cs_zhenya"])
        with cs_sprite_change
        label cs_director_check_dca7850d0d:
        # cs_director_end
        cs_narrator "Женя закрыла книгу и взяла поднос."
        cs_mz "Ладно, мне пора."
        cs_narrator "Я посмотрела на неё."
        cs_ls "В библиотеку?"
        cs_mz "Нет. Хочу ещё кое-что сделать перед выступлением."
        cs_narrator "Она немного помолчала."
        cs_mz "И вообще, не обязательно же мне постоянно сидеть среди книг."
        cs_narrator "Я улыбнулась."
        cs_ls "Разумно."
        cs_narrator "Женя посмотрела на Дарью."
        cs_mz "Хорошего вечера."
        cs_da "И тебе."
        cs_narrator "Я кивнула."
        cs_ls "До встречи."
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        label cs_check_dinner64_zhenya_left:
        cs_narrator "Женя направилась к выходу."
        # cs_director_begin: Physical departure in the authored scene
        $ cs_actor_exit(["cs_zhenya"])
        with cs_sprite_leave
        label cs_director_check_f7de979cc9:
        # cs_director_end
        cs_th "Вот так."
        cs_th "Поужинали."
        cs_th "Поговорили."
        cs_th "И спокойно разошлись."
        cs_th "Без необходимости превращать её желание побыть одной в повод для очередной шутки."
    else:
        cs_narrator "Мы с Дарьей закончили ужин и собрали подносы."
        cs_narrator "В дальнем углу Женя всё ещё сидела за своим столом."
        cs_narrator "Я мельком посмотрела в её сторону."
        cs_narrator "Она читала."
        cs_narrator "Похоже, именно так и хотела провести вечер."
        cs_th "И хорошо."
        cs_th "Не всякому человеку нужна компания."
    # cs_director_begin: Common dialogue return after both dinner branches
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_9d0dc580fc:
    # cs_director_end
    cs_narrator "Дарья аккуратно помогла мне поднять поднос."
    cs_narrator "Мы отнесли посуду."
    cs_narrator "И направились к выходу."
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну что, на площадь?"
    cs_narrator "Я кивнула."
    cs_ls "Конечно."
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только без неожиданных экспедиций по дороге."
    cs_narrator "Я усмехнулась."
    cs_ls "Сегодня исследовательская деятельность официально закрыта."
    cs_narrator "Она улыбнулась."
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "До завтра?"
    cs_narrator "Я задумалась."
    cs_ls "До особого распоряжения."
    cs_narrator "Дарья рассмеялась."
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)
    play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    cs_narrator "Мы вышли из столовой."
    cs_narrator "Я посмотрела на закатное небо."
    cs_narrator "Где-то впереди слышались звуки настройки гитары."
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_dinner64_exit:
    cs_narrator "На площади постепенно собирались зрители."
    cs_th "Ну что ж."
    cs_th "На сегодня действительно хватит экспериментов."
    cs_th "Пора послушать музыку."
    return
