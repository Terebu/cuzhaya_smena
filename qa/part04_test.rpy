# -*- coding: utf-8 -*-
default cs_qa_part04_audit = False
init 40 python:
    def cs_qa_part04_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_part04_audit or not cs_part04_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [t for t in tags if renpy.showing(t)]
        if len(actual) > 2 or set(actual) != set(cs_part04_cast):
            raise Exception("Incorrect part-4 cast: %r instead of %r" % (actual, cs_part04_cast))
        if cs_part04_cg and actual:
            raise Exception("Standing portrait on poster-work CG")
    config.all_character_callbacks.append(cs_qa_part04_cast)

label cs_qa_part04_load:
    $ renpy.load("cs_part03_m1_s1-menu")
    return

label cs_qa_viola_replay:
    hide screen cs_day02_work_continue_screen
    window show
    $ cs_part04_live = True
    $ cs_part04_cg = False
    scene bg int_aidpost_day
    show cs normal stethoscope at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    call cs_day02_viola_choice
    call cs_day02_32
    call cs_day02_33
    jump cs_day02_part05_pending
