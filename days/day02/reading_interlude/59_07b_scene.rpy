# -*- coding: utf-8 -*-
label cs_day02_reading_07b:
    $ save_name = "Чужая смена — Тишина на троих: О книге — если есть доверие"
    $ cs_part08_live = False
    $ cs_reading_live = True
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
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_07b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя уже собиралась вернуться за стол, но остановилась."
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Кстати, до какого места ты дошла?"
    cs_narrator "Я показала страницу."
    cs_narrator "Она посмотрела."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А. Уже туда."
    cs_narrator "Я улыбнулась."
    cs_ls "Судя по выражению лица, дальше будет что-то интересное."
    cs_mz "Возможно."
    cs_ls "Очень информативно."
    cs_narrator "Она усмехнулась."
    cs_mz "Ты же сама просила без рассказов о том, что произойдёт дальше."
    cs_narrator "Я кивнула."
    cs_ls "Справедливо."
    cs_narrator "Женя немного помолчала."
    cs_narrator "Потом спросила:"
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А главный герой тебе нравится?"
    cs_narrator "Я задумалась."
    cs_ls "Пока не особенно."
    cs_narrator "Она удивилась."
    cs_mz "Почему?"
    cs_narrator "Я посмотрела на закрытую книгу."
    cs_ls "Он слишком долго избегает очевидного разговора, хотя понимает, что из-за этого всё только усложняется."
    cs_narrator "Женя кивнула."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Мне тоже так показалось."
    cs_narrator "Я улыбнулась."
    cs_ls "Значит, согласны."
    cs_mz "Пока."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она слегка усмехнулась."
    cs_mz "Посмотрим, что ты скажешь, когда дочитаешь."
    cs_narrator "Я тоже улыбнулась."
    # cs_presence_keep: hide cs_zhenya
    $ cs_reading_cast = ["cs_darya"]
    cs_narrator "Она вернулась к работе."
    # cs_director_begin: Zhenya finishes conversation and resumes work
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_9f19b77133:
    # cs_director_end
    cs_th "Оказывается, у нас довольно похожие взгляды на персонажей книг."
    cs_th "Надо будет запомнить."
    label cs_check_reading_desk_07b:
    pause 0.5
    return
