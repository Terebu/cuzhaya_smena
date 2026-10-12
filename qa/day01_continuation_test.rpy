# -*- coding: utf-8 -*-
testcase cs_day01_continuation:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    $ _test.force = True
    run Start("cs_qa_day01_part04")
    click until label cs_check_day01_part04_final
    click until label cs_check_day01_part05_start
    pause 0.5
    assert renpy.showing("bg int_dining_hall_people_day")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part05_seamless_start")
    click until label cs_check_day01_part05_2026
    pause 2.0
    assert renpy.music.get_playing(channel="music") is None
    $ cs_qa_capture("part05_2026")
    click until label cs_check_day01_part05_novel
    pause 0.5
    assert renpy.showing("cs_semen")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part05_visual_novel")
    click until label cs_check_day01_part05_olga
    pause 0.5
    assert renpy.showing("mt")
    assert renpy.showing("cs_semen serious pioneer far")
    assert renpy.showing("cs_darya thinking pioneer far")
    $ cs_qa_capture("part05_olga_interrupts")
    click until label cs_check_day01_part05_agreement
    click until label cs_check_day01_part06_lunch
    pause 0.5
    assert cs_day01_part05_done
    assert renpy.music.get_playing(channel="music") == cs_day_music_home
    $ cs_qa_capture("part06_after_lunch")
    click until label cs_check_day01_part06_house_ext
    pause 0.5
    assert renpy.showing("cs_house_lena_darya_ext_day")
    assert renpy.showing("sl")
    assert renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("part06_house_exterior")
    click until label cs_check_day01_part06_house_int
    pause 0.5
    assert renpy.showing("cs_house_lena_darya_int_day")
    $ cs_qa_capture("part06_house_interior")
    click until label cs_check_day01_part06_fear
    pause 0.5
    assert not renpy.showing("sl")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part06_private_talk")
    click until label cs_check_day01_part06_knock
    pause 0.1
    assert renpy.music.get_playing(channel="sound") == cs_day_sfx_knock
    assert not renpy.showing("dv")
    assert not renpy.showing("us")
    $ cs_qa_capture("part06_knock")
    click until label cs_check_day01_part06_open_door
    pause 0.5
    assert renpy.music.get_playing(channel="music") == cs_day_music_play
    click until label cs_check_day01_part08_pending
    pause 0.5
    assert cs_day01_part05_done
    assert cs_day01_part06_done
    assert cs_day01_part07_done
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs-day01-continuation")
    $ cs_day01_part06_done = False
    $ renpy.load("cs-day01-continuation")
    pause 0.5
    assert cs_day01_part06_done
    assert cs_day01_part07_done
    $ cs_qa_capture("part06_pending_loaded")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_continuation_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: part-4 conversation continues through parts 5/6; home BGs, private talk, music silence, door knock/open, new sprites, save/load and open day.\n")
    run Quit(confirm=False)
