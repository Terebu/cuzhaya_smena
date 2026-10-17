# -*- coding: utf-8 -*-
label cs_day02_31:
    $ save_name = "Чужая смена — День 2: Немного взаимопомощи"
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
    label cs_check_part04_s31:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Виола вернулась к столу."
    cs_narrator "Начала убирать принадлежности после обработки моей руки."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на шкаф, возле которого стояла небольшая коробка с запечатанными упаковками бинтов."
    cs_vi "Ладно, девочки. С рукой всё в порядке. Если больше ничего не беспокоит, можете идти."
    cs_narrator "Я уже направилась к двери."
    cs_narrator "Но заметила, что Виола одной рукой придерживает коробку, пытаясь открыть шкаф."
    cs_th "Может, помочь?"
    cs_th "В конце концов, человек только что потратил время на мою царапину."
    return
