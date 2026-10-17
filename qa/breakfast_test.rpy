# -*- coding: utf-8 -*-
default cs_qa_breakfast_audit = False
init 40 python:
    def cs_qa_breakfast_cast(event, **kwargs):
        if event != "show_done" or not cs_qa_breakfast_audit or not cs_breakfast_live:
            return
        actors = ("cs_darya", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [tag for tag in actors if renpy.showing(tag)]
        if len(actual) > 2 or set(actual) != set(cs_breakfast_cast):
            raise Exception("Incorrect breakfast cast: %r instead of %r" % (actual, cs_breakfast_cast))
        if "un" in actual and not (cs_met_un and cs_friend_un >= 1):
            raise Exception("Tikhonova shown without friendship")
    config.all_character_callbacks.append(cs_qa_breakfast_cast)

label cs_qa_breakfast_load:
    $ renpy.load("cs_part10_un1_help-end")
    return

label cs_qa_breakfast_path:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_day02_done = False
    window show
    call cs_day02_10
    call cs_day02_11
    call cs_day02_12
    call cs_day02_13
    call cs_day02_14
    jump cs_day02_part02_pending

label cs_qa_breakfast_old:
    $ renpy.load("breakfast-before-rewrite")
    return

testcase cs_breakfast_old_save:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    run Start("cs_qa_breakfast_old")
    pause 1.5
    assert cs_friend_un == 1 and cs_friend_mz == 1
    click until label cs_check_part02_s15
    pause 1.0
    assert not cs_day02_done and cs_friend_un == 1
    $ cs_qa_capture("breakfast_old_save_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/breakfast_old_save_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
