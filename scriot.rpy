
# -*- coding: utf-8 -*-
# Keep the original entry label so the installed mod menu remains compatible.
init 10 python:
    mods["chuzhaya_smena_start"] = u"Чужая смена"

default cs_active = False
default cs_darya_known = False

label chuzhaya_smena_start:
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
    scene black with dissolve
    call cs_scene_01
    call cs_scene_02
    call cs_scene_03
    call cs_scene_04
    call cs_scene_05
    call cs_scene_06
    call cs_scene_07
    call cs_day01
    hide screen cs_phone
    hide screen cs_instagram_post
    $ cs_active = False
    $ day_time()
    $ set_mode_adv()
    label cs_check_finished:
    return
