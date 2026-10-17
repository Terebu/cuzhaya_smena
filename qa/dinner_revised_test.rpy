# -*- coding: utf-8 -*-
label cs_qa_dinner_revised_load:
    $ renpy.load("cs_part09_zero-end")
    return

label cs_qa_dinner_revised_run:
    hide screen cs_day02_concert_wait_screen
    window show
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day
    play ambience "sound/ambiences/dining_hall_full.ogg" fadein 0.5
    play music "sound/music/my_daily_life.ogg" fadein 0.5
    call cs_day02_64
    call cs_day02_65
    jump cs_day02_part10_pending
