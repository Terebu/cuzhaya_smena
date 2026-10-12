# -*- coding: utf-8 -*-
label cs_qa_day01_part07:
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_day01_part06_done = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene cs_house_lena_darya_int_day
    show cs_darya neutral pioneer normal at cs_day_dasha_right
    play ambience cs_day_cabin
    play music cs_day_music_play
    call cs_day01_30
    jump cs_day01_part07

testcase cs_day01_part07:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_day01_part07")
    click until label cs_check_day01_part07_guests
    pause 0.6
    assert renpy.showing("dv") and renpy.showing("us") and renpy.showing("cs_darya")
    assert renpy.music.get_playing(channel="music") == cs_day_music_play
    $ cs_qa_capture("part07_visitors")
    click until label cs_check_day01_part07_idea
    pause 0.6
    assert not renpy.showing("dv") and not renpy.showing("us")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part07_idea")
    click until label cs_check_day01_part07_engineers
    pause 0.6
    assert renpy.showing("bg int_clubs_male_day")
    assert renpy.showing("sh") and renpy.showing("el") and renpy.showing("cs_darya")
    $ cs_qa_capture("part07_engineers")
    click until label cs_check_day01_part07_silence
    pause 2.1
    assert renpy.music.get_playing(channel="music") is None
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part07_phone_silence")
    click until label cs_check_day01_part07_year
    pause 0.6
    $ cs_qa_capture("part07_1980")
    click until label cs_check_day01_part07_home
    pause 0.6
    $ cs_qa_capture("part07_phone_home")
    click until label cs_check_day01_part07_exit
    pause 0.6
    assert renpy.showing("bg ext_clubs_day")
    assert not renpy.showing("sh") and not renpy.showing("el")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part07_exit")
    click until label cs_check_day01_part08_pending
    pause 0.6
    assert cs_day01_part07_done
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.save("cs-day01-part07")
    $ renpy.load("cs-day01-part07")
    pause 0.6
    assert cs_day01_part07_done
    $ cs_qa_capture("part07_saved_open_day")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_part07_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: scenes 30-39, original actors/assets, quiet segment, 1980 revelation, exit, open day and save/load.\n")
    run Quit(confirm=False)
