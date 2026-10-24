
# -*- coding: utf-8 -*-
# Keep the original entry label so the installed mod menu remains compatible.
init 10 python:
    mods["chuzhaya_smena_start"] = u"Чужая смена"

default cs_active = False
default cs_darya_known = False

label chuzhaya_smena_start:
    $ cs_reset_state()
    $ cs_active = True
    $ cs_darya_known = False
    $ cs_slavya_known = False
    $ cs_olga_seen = False
    $ cs_day01_part02_done = False
    $ cs_day01_part03_done = False
    $ cs_day01_part04_done = False
    $ prolog_time()
    $ set_mode_adv()
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    $ renpy.music.set_volume(1.0, channel="music")
    $ renpy.music.set_volume(1.0, channel="ambience")
    $ renpy.music.set_volume(1.0, channel="sound")
    scene black with dissolve
    call cs_scene_01 from cs_return_5ab25bfc0b1849835c11
    call cs_scene_02 from cs_return_37460e53b3f2b972248c
    call cs_scene_03 from cs_return_374f5543e2f7e1a35e27
    call cs_scene_04 from cs_return_a5e0c348ea6ddd7bfe80
    call cs_scene_05 from cs_return_cb7b2b964e9e509bf19f
    call cs_scene_06 from cs_return_02198889b11b54cb5373
    call cs_scene_07 from cs_return_386974f9a818d9f0684c
    call cs_day01 from cs_return_6af0b45c345066e12922
    hide screen cs_phone
    hide screen cs_instagram_post
    $ cs_active = False
    $ day_time()
    $ set_mode_adv()
    label cs_check_finished:
    return
