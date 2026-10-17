# -*- coding: utf-8 -*-
label cs_day02_51b:
    $ save_name = "Чужая смена — День 2: Хватит приключений"
    $ cs_part06_live = False
    $ cs_part07_live = True
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
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_check_part07_s51b:
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
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я осторожно поднялась с кушетки."
    cs_ls "Не будем больше тебя задерживать. Спасибо ещё раз."
    cs_narrator "Виола кивнула."
    show cs custom stern medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Не за что. Только с повязкой аккуратнее."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы проследим."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Мне кажется, мне только что назначили персонального инспектора по технике безопасности."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Очень своевременно."
    cs_narrator "Виола усмехнулась."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Пожалуй."
    cs_narrator "Мы попрощались."
    return
