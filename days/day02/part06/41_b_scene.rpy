# -*- coding: utf-8 -*-
label cs_day02_41b:
    $ save_name = "Чужая смена — День 2: Только факты"
    $ cs_part05_live = False
    $ cs_part06_live = True
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
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/just_think.ogg":
        play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part06_s41b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на Семёна."
    cs_ls "Тогда зафиксируем план. Идём втроём, остаёмся на дороге, отмечаем ориентиры и возвращаемся, если ничего не найдём за разумное время."
    cs_narrator "Семён кивнул."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Сколько будем идти?"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья задумалась."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Давай начнём с пятнадцати минут в одном направлении. Если не будет ничего необычного, решим, нужно ли продолжать."
    cs_sy "А если дорога начнёт петлять?"
    cs_ls "Тогда хотя бы будем знать, что петляет. И не полезем через лес напрямик."
    cs_narrator "Он кивнул."
    cs_sy "Ладно. Главное, чтобы не получилось так, что мы ушли искать выход, а потом сами потерялись."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Поэтому и идём вместе."
    cs_narrator "Я улыбнулась."
    cs_ls "Отлично. Техническое задание утверждено."
    cs_narrator "Семён усмехнулся."
    cs_sy "Осталось только его выполнить."
    return
