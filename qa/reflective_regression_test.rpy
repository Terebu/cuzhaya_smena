# -*- coding: utf-8 -*-
label cs_qa_reflective_case_0:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg ext_camp_entrance_day
    call cs_day01_03
    label cs_qa_reflective_case_0_end:
    pause
    return

label cs_qa_reflective_case_1:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day
    call cs_day02_30
    label cs_qa_reflective_case_1_end:
    pause
    return

label cs_qa_reflective_case_2:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg ext_square_day
    call cs_day02_56
    label cs_qa_reflective_case_2_end:
    pause
    return

label cs_qa_reflective_case_3:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day
    call cs_day02_64d
    label cs_qa_reflective_case_3_end:
    pause
    return

label cs_qa_reflective_sunset:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    call cs_day01_50
    label cs_qa_reflective_sunset_end:
    pause
    return

testcase cs_reflective_regression:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_reflective_sunset")
    click until label cs_check_day01_part09_returns
    pause 0.4
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("reflective_sunset_dialogue")
    click until label cs_director_check_031e208f3c
    pause 0.4
    assert cs_reflective_shot and not any(renpy.showing(t) for t in cs_presence_tags)
    $ renpy.cs_qa_reflective_audio = (renpy.music.get_playing(), renpy.music.get_playing(channel="ambience"))
    $ renpy.take_screenshot()
    $ renpy.save("cs_reflective_sunset")
    $ renpy.load("cs_reflective_sunset")
    pause 0.5
    assert cs_reflective_shot and not any(renpy.showing(t) for t in cs_presence_tags)
    assert (renpy.music.get_playing(), renpy.music.get_playing(channel="ambience")) == renpy.cs_qa_reflective_audio
    $ cs_qa_capture("reflective_sunset_after_load")
    click until label cs_qa_reflective_sunset_end
    assert not renpy.showing("cs_darya")
    run Jump("cs_qa_reflective_case_0")
    click until label cs_director_check_73161bfb32
    pause 0.4
    assert cs_reflective_shot and not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_case_0_empty")
    click until label cs_director_check_9a7409ab4c
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs_dasha_winter')
    $ cs_qa_capture("reflective_case_0_return")
    run Jump("cs_qa_reflective_case_1")
    click until label cs_director_check_c2a563ebcd
    pause 0.4
    assert cs_reflective_shot and not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_case_1_empty")
    click until label cs_director_check_5752982251
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs')
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("reflective_case_1_return")
    run Jump("cs_qa_reflective_case_2")
    click until label cs_director_check_b4cefde74c
    pause 0.4
    assert cs_reflective_shot and not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_case_2_empty")
    click until label cs_director_check_57427f3ded
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs_darya')
    assert renpy.showing('cs_semen')
    $ cs_qa_capture("reflective_case_2_return")
    run Jump("cs_qa_reflective_case_3")
    click until label cs_director_check_fa8d03b9db
    pause 0.4
    assert cs_reflective_shot and not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_case_3_empty")
    click until label cs_director_check_5c4ae70de0
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs_darya')
    assert renpy.showing('cs_zhenya')
    $ cs_qa_capture("reflective_case_3_return")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/reflective_regression_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_cg_entry_regression:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene cs_cg_poster_planning_day
    pause
    call cs_day02_34
    call cs_day02_35
    call cs_day02_35a
    call cs_day02_35b
    call cs_day02_36
    label cs_qa_cg_entry_end:
    pause
    return

testcase cs_reflective_cg_entries:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_cg_entry_regression")
    click until label cs_check_part05_s34
    pause 0.4
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_cg_entry34")
    click until label cs_check_part05_s35
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    click until label cs_qa_cg_entry_end
    assert cs_qa_global_cg_checks > 30
    $ cs_qa_capture("reflective_cg_entry_after_work")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/reflective_cg_entries_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
