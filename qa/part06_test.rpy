# -*- coding: utf-8 -*-
default cs_qa_part06_audit = False
init 40 python:
    def cs_qa_part06_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_part06_audit or not cs_part06_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [t for t in tags if renpy.showing(t)]
        if len(actual) > 3 or set(actual) != set(cs_part06_cast):
            raise Exception("Incorrect part-6 cast: %r instead of %r" % (actual, cs_part06_cast))
    config.all_character_callbacks.append(cs_qa_part06_cast)

label cs_qa_part06_load:
    $ renpy.load("cs_part05_m1_s1_e1-cg")
    return

label cs_qa_road_replay:
    hide screen cs_day02_road_continue_screen
    window show
    $ cs_part06_live = True
    scene bg int_dining_hall_people_day
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    call cs_day02_road_choice
    jump cs_day02_part07_pending
