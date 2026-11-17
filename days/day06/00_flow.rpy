# -*- coding: utf-8 -*-
label cs_day06:
    hide screen cs_day05_end_screen
    if cs_d6_done:
        jump cs_day06_complete
    $ cs_d6_begin()
    call cs_day_title(6) from cs_d6_title_return
    $ cs_rev_time("day")
    window show dissolve
    call cs_day06_01 from cs_d6_scene_01_return
    call cs_day06_02 from cs_d6_scene_02_return
    call cs_day06_03 from cs_d6_scene_03_return
    call cs_day06_04 from cs_d6_scene_04_return
    call cs_day06_05 from cs_d6_scene_05_return
    call cs_day06_06 from cs_d6_scene_06_return
    call cs_day06_07 from cs_d6_scene_07_return
    call cs_day06_08 from cs_d6_scene_08_return
    $ cs_d6_done = True
    $ cs_bus_cue("silence")
    stop music fadeout 1.5
    stop sound fadeout 0.5
    window hide dissolve
    $ cs_director_scene("black")
    scene black with Dissolve(1.0)
label cs_day06_complete:
    label cs_check_day06_complete:
    call screen cs_day06_end_screen
    jump cs_day06_complete
