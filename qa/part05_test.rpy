# -*- coding: utf-8 -*-
default cs_qa_part05_audit = False
init 40 python:
    def cs_qa_part05_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_part05_audit or not cs_part05_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [t for t in tags if renpy.showing(t)]
        if len(actual) > 3 or set(actual) != set(cs_part05_cast):
            raise Exception("Incorrect part-5 cast: %r instead of %r" % (actual, cs_part05_cast))
        if cs_part05_cg and actual:
            raise Exception("Portrait on top of part-5 CG")
    config.all_character_callbacks.append(cs_qa_part05_cast)

label cs_qa_part05_load_help:
    $ renpy.load("cs_part04_help-poster")
    return

label cs_qa_part05_load_leave:
    $ renpy.load("cs_part04_leave-poster")
    return

label cs_qa_semen_replay:
    hide screen cs_day02_walk_continue_screen
    window show
    $ cs_part05_live = True
    $ cs_part05_cg = True
    scene cs_cg_poster_planning_day
    $ cs_part05_cast = []
    call cs_day02_semen_choice
    jump cs_day02_part06_pending
