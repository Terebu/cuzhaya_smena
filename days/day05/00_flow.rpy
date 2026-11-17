# -*- coding: utf-8 -*-
label cs_day05:
    hide screen cs_day05_wait_screen
    if cs_d5_done:
        jump cs_day05_complete
    if not cs_d5_started:
        call cs_day_title(5) from cs_d5_title_return
    $ cs_d5_started = True
    window show dissolve
    call cs_day05_01 from cs_d5_scene_01_return
    call cs_day05_02 from cs_d5_scene_02_return
    call cs_day05_03 from cs_d5_scene_03_return
    call cs_day05_04 from cs_d5_scene_04_return
    call cs_day05_05 from cs_d5_scene_05_return
    call cs_day05_06 from cs_d5_scene_06_return
    call cs_day05_07 from cs_d5_scene_07_return
    call cs_day05_08 from cs_d5_scene_08_return
    call cs_day05_09 from cs_d5_scene_09_return
    call cs_day05_10 from cs_d5_scene_10_return
    call cs_day05_11 from cs_d5_scene_11_return
    call cs_day05_12 from cs_d5_scene_12_return
    call cs_day05_13 from cs_d5_scene_13_return
    call cs_day05_14 from cs_d5_scene_14_return
    call cs_day05_15 from cs_d5_scene_15_return
    call cs_day05_16 from cs_d5_scene_16_return
    call cs_day05_17 from cs_d5_scene_17_return
    call cs_day05_18 from cs_d5_scene_18_return
    call cs_day05_19 from cs_d5_scene_19_return
    call cs_day05_20 from cs_d5_scene_20_return
    call cs_day05_21 from cs_d5_scene_21_return
    $ cs_d5_done = True
label cs_day05_complete:
    label cs_check_day05_complete:
    if not cs_d5_missing_minute_done:
        call cs_day05_21 from cs_d5_legacy_missing_minute_return
    jump cs_day06

screen cs_day05_end_screen():
    timer 0.1 action Jump("cs_day05_complete")
