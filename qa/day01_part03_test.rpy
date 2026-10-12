# -*- coding: utf-8 -*-
label cs_qa_day01_part03:
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_slavya_known = True
    $ cs_olga_seen = True
    $ cs_day01_part02_done = True
    call cs_day01_10
    call cs_day01_11
    call cs_day01_12
    call cs_day01_13
    call cs_day01_14
    $ cs_day01_part03_done = True
    jump cs_day01_part09_pending

testcase cs_day01_part03:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    run Start("cs_qa_day01_part03")
    click until label cs_check_day01_part03_inside
    pause 2.0
    assert renpy.showing("cs_dasha_winter")
    assert renpy.showing("mt")
    assert renpy.music.get_playing(channel="ambience") == cs_day_cabin
    $ cs_qa_capture("day01_part03_inside")
    click until label cs_check_day01_part03_phone_off
    pause 1.0
    assert renpy.get_screen("cs_phone").scope["mode"] == "off"
    assert renpy.showing("mt")
    $ cs_qa_capture("day01_part03_phone_off")
    click until label cs_check_day01_part03_calculator
    pause 1.0
    $ cs_qa_capture("day01_part03_calculator")
    click until label cs_check_day01_part03_mirror
    pause 1.0
    assert renpy.showing("cs_lena_pioneer_mirror")
    assert not renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("day01_part03_mirror")
    click until label cs_check_day01_part03_pioneer
    click until label cs_check_darya_uniform_talk
    pause 1.0
    assert renpy.showing("cs_darya surprised pioneer normal")
    assert not renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("day01_part03_pioneer")
    click until label cs_check_day01_part03_horn
    pause 0.2
    assert renpy.music.get_playing(channel="sound") == cs_day_sfx_horn
    $ cs_qa_capture("day01_part03_horn")
    click until label cs_check_day01_part08_pending
    pause 1.0
    assert cs_day01_part03_done
    assert renpy.get_screen("cs_day01_pending") is not None
    assert renpy.music.get_playing(channel="music") == cs_day_music_everyday
    $ cs_qa_capture("day01_part03_pending")
    $ renpy.take_screenshot()
    $ renpy.save("cs-day01-part03")
    $ cs_day01_part03_done = False
    $ renpy.load("cs-day01-part03")
    pause 1.0
    assert cs_day01_part03_done
    assert renpy.get_screen("cs_day01_pending") is not None
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_part03_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: scenes 10-14, mirror CG, winter-to-pioneer change, horn on sound channel, open day, save/load.\n")
    run Quit(confirm=False)
