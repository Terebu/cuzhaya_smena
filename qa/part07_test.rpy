# -*- coding: utf-8 -*-
default cs_qa_part07_audit = False
init 40 python:
    def cs_qa_part07_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_part07_audit or not cs_part07_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [t for t in tags if renpy.showing(t)]
        if len(actual) > 2 or set(actual) != set(cs_part07_cast):
            raise Exception("Incorrect part-7 cast: %r instead of %r" % (actual, cs_part07_cast))
        if renpy.showing("cs_semen") or renpy.showing("un"):
            raise Exception("Absent character in the second medical visit")
    config.all_character_callbacks.append(cs_qa_part07_cast)

label cs_qa_part07_load:
    $ renpy.load("cs_part06_trust-loop")
    return

label cs_qa_part07_replay:
    hide screen cs_day02_injury_continue_screen
    window show
    $ cs_part07_live = True
    scene bg int_aidpost_day
    show cs custom warm_smile medical normal at cs_viola_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    call cs_day02_viola_second_choice
    jump cs_day02_part08_pending

label cs_qa_morning_help_load:
    $ renpy.load("cs_part04_help-choice")
    return
