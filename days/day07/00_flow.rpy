# -*- coding: utf-8 -*-
label cs_day07:
    hide screen cs_day06_end_screen
    $ cs_d7_started = True
    $ cs_bus_cue("calm")
    stop ambience fadeout 0.8
    $ cs_d7_scene("black")
    call cs_day_title(7) from cs_d7_title_return
    $ cs_rev_time("day")
    window show dissolve
    jump cs_day07_01
