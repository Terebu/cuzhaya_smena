# -*- coding: utf-8 -*-
label cs_qa_load_actual_part07:
    $ renpy.load("cs-preserved-part07")
    return

testcase cs_day01_part08:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    assert renpy.can_load("cs-preserved-part07")
    run Start("cs_qa_load_actual_part07")
    pause 0.6
    assert cs_day01_part07_done and not cs_day01_part08_done
    # Let Ren'Py finish after_load before exercising the saved continuation label.
    run Jump("cs_check_day01_part07_pending")
    pause 0.6
    assert renpy.showing("bg ext_clubs_day")
    assert renpy.showing("cs_darya shrug pioneer normal")
    assert renpy.music.get_playing(channel="music") == cs_day_music_daily
    $ cs_qa_capture("part08_old_save_start")
    click until label cs_check_day01_part08_confession
    pause 0.6
    assert renpy.showing("cs_camp_path_sunset")
    assert persistent.timeofday == "sunset" and persistent.sprite_time == "sunset"
    assert renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("part08_confession")
    click until label cs_check_day01_part08_silence
    pause 3.1
    assert renpy.music.get_playing(channel="music") is None
    assert renpy.music.get_playing(channel="ambience") == "sound/ambiences/camp_center_evening.ogg"
    $ cs_qa_capture("part08_quiet_response")
    click until label cs_check_day01_part08_boundaries
    pause 0.6
    assert renpy.showing("cs_darya forearm_hold pioneer normal")
    $ cs_qa_capture("part08_no_immediate_agreement")
    click until label cs_check_day01_part08_semen
    pause 0.6
    assert renpy.showing("bg ext_square_sunset")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("part08_semen_square")
    click until label cs_check_day01_part08_opinion
    pause 0.6
    $ cs_qa_capture("part08_independent_opinion")
    click until label cs_check_day01_part08_semen_leaves
    pause 0.6
    assert not renpy.showing("cs_semen")
    assert renpy.showing("cs_darya")
    click until label cs_check_day01_part08_hug
    pause 0.6
    assert renpy.showing("cs_darya reaching pioneer normal")
    $ cs_qa_capture("part08_permission_to_hug")
    click until label cs_check_day01_part08_pending
    pause 0.6
    assert cs_day01_part08_done
    assert renpy.showing("cs_camp_path_sunset")
    assert renpy.showing("cs_darya shrug pioneer normal")
    assert renpy.music.get_playing(channel="music") == cs_day_music_home
    assert renpy.get_screen("cs_day01_pending") is not None
    assert renpy.get_screen("main_menu") is None
    $ renpy.take_screenshot()
    $ renpy.save("cs-day01-part08")
    $ cs_day01_part08_done = False
    $ renpy.load("cs-day01-part08")
    pause 0.6
    assert cs_day01_part08_done
    $ cs_qa_capture("part08_open_day_loaded")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_part08_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: real pre-part-eight save, scenes 40-45, sunset actors/UI, music silence, gradual confession, Semyon/exit, open day and save/load.\n")
    run Quit(confirm=False)
