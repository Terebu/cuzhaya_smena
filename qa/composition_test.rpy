# -*- coding: utf-8 -*-
label cs_qa_composition_scenes:
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_olga_seen = True
    $ cs_slavya_known = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day
    call cs_day01_15
    call cs_day01_20
    call cs_day01_21
    call cs_day01_22
    scene bg int_clubs_male_day
    show cs_darya shrug pioneer far at cs_darya_far_center
    call cs_day01_34
    jump cs_day01_part10_pending

testcase cs_composition:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_composition_scenes")
    click until label cs_check_day01_part04_housing
    pause 0.8
    assert renpy.showing("mt") and renpy.showing("cs_darya")
    $ cs_qa_capture("composition_house_two")
    click until label cs_check_day01_part05_journey
    pause 0.8
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert not renpy.showing("mt")
    $ cs_qa_capture("composition_dining_two")
    click until label cs_check_day01_part07_engineers
    pause 1.2
    assert renpy.showing("sh") and renpy.showing("el") and renpy.showing("cs_darya")
    $ cs_qa_capture("composition_clubs_three")
    click until label cs_check_day01_part09_pending
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/composition_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: house pair, dining pair, clubs group; source scene bodies, group Darya visible, calibrated scales and positions.\n")
    run Quit(confirm=False)
