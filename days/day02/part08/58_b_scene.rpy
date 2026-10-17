# -*- coding: utf-8 -*-
label cs_day02_58b:
    $ save_name = "Чужая смена — День 2: Иногда можно просто пройти мимо"
    $ cs_part07_live = False
    $ cs_part08_live = True
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
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part08_s58b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Она шла в сторону клубов, прижимая книги к боку."
    cs_narrator "Выглядела сосредоточенной."
    cs_th "Пожалуй, не буду отвлекать."
    cs_narrator "Вчера у нас и так состоялся достаточно необычный разговор."
    cs_narrator "А сегодня ей, судя по всему, хотелось просто закончить свои дела."
    cs_narrator "Я повернулась к Дарье."
    cs_ls "Нет, давай не будем её задерживать."
    cs_narrator "Дарья кивнула."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо."
    cs_narrator "Семён посмотрел в сторону Жени."
    cs_sy "А я думал, ты обязательно подойдёшь."
    cs_narrator "Я улыбнулась."
    cs_ls "Видишь? Учусь неожиданным решениям."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он усмехнулся."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Это действительно неожиданно."
    cs_narrator "Я ещё раз посмотрела на уходящую Женю."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_zhenya"])
    with cs_sprite_leave
    label cs_director_check_3d94979afb:
    # cs_director_end
    cs_th "Ничего страшного."
    cs_th "У нас наверняка будет возможность поговорить в другой раз."
    cs_th "Не каждое знакомство нужно превращать в отдельное событие."
    return
