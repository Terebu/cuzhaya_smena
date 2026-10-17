# -*- coding: utf-8 -*-
label cs_qa_dialogue_focus:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ cs_darya_known = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene cs_house_lena_darya_int_day
    pause
    call cs_day02_02
    call cs_day02_07
    scene bg int_musclub_day
    call cs_day02_18
    scene bg int_library_day
    call cs_day01_56
    scene bg int_clubs_male_day
    call cs_day02_26
    label cs_qa_dialogue_focus_end:
    pause
    return

testcase cs_dialogue_focus:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 60.0
    run Start("cs_qa_dialogue_focus")
    click until label cs_director_check_33c14ca943
    pause 0.4
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("dialogue_morning_sleepy")
    click until label cs_check_new_d2_s07
    pause 0.4
    assert not renpy.showing("cs_darya")
    $ cs_qa_capture("dialogue_morning_exterior")
    click until label cs_director_check_95df4f349e
    pause 0.4
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("dialogue_morning_return")
    $ renpy.cs_qa_morning_bounds = renpy.get_image_bounds("cs_darya")
    click until label cs_director_check_aedf775c9a
    pause 0.4
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("dialogue_morning_worried")
    assert renpy.get_image_bounds("cs_darya") == renpy.cs_qa_morning_bounds
    $ renpy.take_screenshot()
    $ renpy.save("cs_dialogue_focus_worried")
    $ renpy.load("cs_dialogue_focus_worried")
    pause 0.4
    assert renpy.showing("cs_darya worried pioneer normal")
    click until label cs_director_check_748577bc95
    pause 0.4
    assert renpy.showing('cs_darya')
    assert renpy.showing('mi')
    $ cs_qa_capture("dialogue_piano_dialogue")
    click until label cs_director_check_214c14521a
    pause 0.4
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("dialogue_library_return")
    click until label cs_qa_dialogue_focus_end
    assert cs_qa_global_speaker_checks > 80
    $ cs_qa_capture("dialogue_engineers_final")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/dialogue_focus_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
