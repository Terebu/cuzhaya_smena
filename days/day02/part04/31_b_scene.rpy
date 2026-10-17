# -*- coding: utf-8 -*-
label cs_day02_31b:
    $ save_name = "Чужая смена — День 2: Не будем мешать"
    $ cs_part03_live = False
    $ cs_part04_live = True
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
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part04_s31b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на шкаф."
    cs_narrator "Затем на Виолу."
    cs_narrator "Она уже занялась своими делами."
    cs_th "Пожалуй, не стоит задерживать человека без необходимости."
    cs_narrator "Я подошла к двери."
    cs_ls "Спасибо за помощь. И извини, что отвлекли."
    cs_narrator "Виола подняла глаза."
    cs_vi "Это моя работа."
    cs_narrator "Она улыбнулась."
    cs_vi "Только в следующий раз будь осторожнее."
    cs_ls "Постараюсь."
    cs_narrator "Дарья тоже попрощалась."
    cs_da "До свидания."
    cs_vi "До свидания, девочки."
    cs_narrator "Мы направились к выходу."
    return
