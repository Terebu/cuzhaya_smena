# -*- coding: utf-8 -*-
label cs_qa_day01_part04:
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_slavya_known = True
    $ cs_olga_seen = True
    $ cs_day01_part03_done = True
    jump cs_day01_part04

testcase cs_day01_part04:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    run Start("cs_qa_day01_part04")
    click until label cs_check_day01_part04_housing
    pause 1.0
    assert renpy.showing("bg int_house_of_mt_day")
    assert renpy.showing("cs_darya")
    assert not renpy.showing("cs_dasha_winter")
    assert "/new/" in cs_dasha_metadata["pioneer"][0]["path"]
    $ cs_qa_capture("day01_part04_housing")
    click until label cs_check_day01_part04_passenger
    click until label cs_check_day01_part04_silence
    pause 1.5
    assert renpy.music.get_playing(channel="music") is None
    $ cs_qa_capture("day01_part04_passenger")
    click until label cs_check_day01_part04_outside
    pause 1.0
    assert renpy.showing("bg ext_house_of_mt_day")
    $ cs_qa_capture("day01_part04_outside")
    click until label cs_check_day01_part04_aidpost
    pause 1.0
    assert renpy.showing("bg ext_aidpost_day")
    $ cs_qa_capture("day01_part04_aidpost")
    click until label cs_check_day01_part04_cameo
    pause 1.0
    assert renpy.showing("dv normal pioneer far")
    assert renpy.showing("us smile pioneer far")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("day01_part04_cameo")
    click until label cs_check_day01_part04_semen
    pause 1.0
    assert renpy.showing("bg int_dining_hall_people_day")
    assert renpy.showing("cs_semen neutral pioneer far")
    assert renpy.showing("cs_darya")
    assert not renpy.showing("dv")
    assert not renpy.showing("us")
    assert renpy.music.get_playing(channel="ambience") == cs_day_dining_full
    $ cs_qa_capture("day01_part04_semen")
    click until label cs_check_day01_part04_reaction
    pause 1.0
    assert renpy.showing("cs_semen surprised pioneer far")
    $ cs_qa_capture("day01_part04_reaction")
    click until label cs_check_day01_part04_final
    pause 1.0
    assert renpy.music.get_playing(channel="music") == cs_day_music_unknown
    $ cs_qa_capture("day01_part04_final")
    click until label cs_check_day01_part08_pending
    pause 1.0
    assert cs_day01_part04_done
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs-day01-part04")
    $ cs_day01_part04_done = False
    $ renpy.load("cs-day01-part04")
    pause 1.0
    assert cs_day01_part04_done
    assert renpy.music.get_playing(channel="music") == cs_day_music_home
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_part04_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: scenes 15-20, updated Darya, own Semyon, cameos, original backgrounds/audio, open day, save/load.\n")
    run Quit(confirm=False)

testcase cs_day01_part03_save:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    assert renpy.can_load("cs-old-part03")
    $ renpy.load("cs-old-part03")
    pause 1.0
    assert cs_day01_part03_done
    assert not cs_day01_part04_done
    run Jump("cs_day01_part04_pending")
    click until label cs_check_day01_part08_pending
    pause 1.0
    assert cs_day01_part04_done
    assert renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ cs_qa_capture("day01_part03_save_continued")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_part03_save_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: prior part-3 save loaded and continued through scenes 15-20 with new sprites.\n")
    run Quit(confirm=False)
