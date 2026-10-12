# -*- coding: utf-8 -*-
# Opt-in targeted check of the unfinished day's save/resume point.
label cs_qa_day01_resume:
    $ day_time()
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_slavya_known = True
    scene bg ext_camp_entrance_day
    $ renpy.music.set_volume(0.25, channel="music")
    play music cs_day_music_unknown
    $ cs_day01_part02_done = True
    $ cs_day01_part03_done = True
    $ cs_day01_part04_done = True
    jump cs_day01_part05_pending

testcase cs_day01_resume:
    pause 1.0
    run Start("cs_qa_day01_resume")
    pause 2.0
    assert renpy.get_screen("cs_day01_pending") is not None
    run ShowMenu("save")
    pause 1.0
    assert renpy.get_screen("save") is not None
    $ cs_qa_capture("day01_06_save")
    run Function(renpy.end_interaction, True)
    pause 0.5
    $ renpy.take_screenshot()
    $ renpy.save("cs-day01-continuation", extra_info=u"День 1: продолжение")
    assert renpy.can_load("cs-day01-continuation")
    $ cs_slavya_known = False
    $ renpy.load("cs-day01-continuation")
    pause 1.0
    assert cs_slavya_known
    assert cs_active
    assert persistent.timeofday == "day"
    assert renpy.music.get_playing(channel="music") == cs_day_music_unknown
    assert renpy.get_screen("cs_day01_pending") is not None
    $ cs_qa_capture("day01_07_resumed")
    python:
        import os
        with open(os.path.join(config.gamedir, "mods/chuzaya_smena/qa/day01_resume_pass.txt"), "w") as cs_f:
            cs_f.write("PASS: unfinished day save menu and save/load roundtrip; continuation screen restored.\n")
    run Quit(confirm=False)
