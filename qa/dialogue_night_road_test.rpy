# -*- coding: utf-8 -*-
label cs_qa_night_and_road:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ cs_darya_known = True
    $ night_time()
    $ persistent.sprite_time = "night"
    scene cs_house_lena_darya_int_night at cs_house_full_frame
    show cs_darya neutral pioneer normal at cs_darya_normal_center
    pause
    call cs_day01_64
    label cs_check_qa_night_finished:
    pause
    return

label cs_qa_road_expressions:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_road_loop_observations = 1
    scene cs_road_marked_verge_day
    pause
    call cs_day02_44
    label cs_check_qa_road_finished:
    pause
    return

testcase cs_dialogue_night_and_road:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_night_and_road")
    click until label cs_check_d1_s64
    pause 0.4
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("dialogue_day1_lying_conversation")
    click until label cs_director_check_a1a1ceb800
    pause 0.4
    assert cs_reflective_shot and not renpy.showing("cs_darya")
    $ cs_qa_capture("dialogue_day1_final_private")
    click until label cs_check_qa_night_finished
    run Jump("cs_qa_road_expressions")
    click until label cs_check_part06_back_c
    pause 0.4
    assert renpy.showing("cs_darya thinking pioneer far")
    $ cs_qa_capture("dialogue_road_serious_far")
    click until label cs_check_part06_gate_return
    pause 0.4
    assert renpy.showing("cs_darya thinking pioneer normal")
    $ cs_qa_capture("dialogue_road_serious_normal")
    click until label cs_check_qa_road_finished
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/dialogue_night_and_road_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
