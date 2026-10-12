# -*- coding: utf-8 -*-
testcase cs_day01_part02_save:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    assert renpy.can_load("cs-old-part02")
    $ renpy.load("cs-old-part02")
    pause 1.0
    assert not cs_day01_part03_done
    run Jump("cs_day01_next_part")
    click until label cs_check_day01_part03_phone_off
    pause 1.0
    assert renpy.get_screen("cs_phone") is not None
    assert renpy.get_screen("cs_phone").scope["mode"] == "off"
    $ cs_qa_capture("day01_part03_phone_off")
    click until label cs_check_day01_part08_pending
    pause 1.0
    assert cs_day01_part03_done
    assert renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ cs_qa_capture("day01_part02_save_continued")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_part02_save_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: real part-2 save loaded and continued through scenes 10-20.\n")
    run Quit(confirm=False)
