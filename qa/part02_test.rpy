# -*- coding: utf-8 -*-
default cs_qa_part02_audit = False
init 40 python:
    def cs_qa_part02_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_part02_audit or not cs_part02_live:
            return
        tags = ("cs_darya", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [tag for tag in tags if renpy.showing(tag)]
        if len(actual) > 2 or set(actual) != set(cs_part02_cast):
            raise Exception("Incorrect music-club cast: %r instead of %r" % (actual, cs_part02_cast))
        if cs_part02_cg and actual:
            raise Exception("Portrait on top of piano CG")
    config.all_character_callbacks.append(cs_qa_part02_cast)

label cs_qa_part02_load:
    $ renpy.load("new-day02-breakfast")
    return

label cs_qa_part02_path:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_darya_known = True
    $ cs_qa_part02_audit = True
    window show
    call cs_day02_14
    jump cs_day02_part02_pending

label cs_qa_part02_replay:
    hide screen cs_day02_continue_screen
    window show
    call cs_day02_19
    jump cs_day02_part03_pending
