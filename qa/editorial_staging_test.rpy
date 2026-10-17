# -*- coding: utf-8 -*-
label cs_qa_editorial_opening:
    $ cs_active = True
    stop music
    call cs_scene_01
    label cs_qa_editorial_opening_end:
    pause
    return

testcase cs_editorial_credits:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_editorial_opening")
    pause 2.3
    assert renpy.get_screen("cs_opening_credits_screen") is not None
    assert renpy.get_screen("say") is not None
    $ cs_qa_capture("credits_01_title")
    pause 2.0
    $ cs_qa_capture("credits_02_ai")
    pause 2.0
    $ cs_qa_capture("credits_03_all")
    pause 2.8
    $ cs_qa_capture("credits_04_title_gone")
    pause 1.7
    $ cs_qa_capture("credits_05_ai_gone")
    pause 2.0
    assert renpy.get_screen("cs_opening_credits_screen") is None
    $ cs_qa_capture("credits_06_finished")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_editorial_credits_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_editorial_night:
    $ cs_active = True
    $ night_time()
    $ persistent.sprite_time = "night"
    scene cs_house_lena_darya_int_night at cs_house_full_frame
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    call cs_day02_74
    label cs_qa_editorial_night_end:
    pause
    return

testcase cs_editorial_night:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_editorial_night")
    click until label cs_director_check_b11badd71b
    assert not renpy.showing("cs_darya") and cs_director_states.get("cs_darya") == "PRESENT_OFFSCREEN"
    $ cs_qa_capture("editorial_night_private")
    click until label cs_director_check_4862310767
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_editorial_night_bounds = renpy.get_image_bounds("cs_darya")
    $ renpy.take_screenshot()
    $ renpy.save("cs_editorial_lying_dialogue")
    $ renpy.load("cs_editorial_lying_dialogue")
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("editorial_lying_dialogue")
    click until label cs_director_check_d61a0c0e86
    assert not renpy.showing("cs_darya")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_editorial_night_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_editorial_reading:
    $ cs_active = True
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_library_day
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    call cs_day02_reading_06
    label cs_qa_editorial_reading_end:
    pause
    return

testcase cs_editorial_reading:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_editorial_reading")
    click until label cs_director_check_493862e91a
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    assert cs_director_states.get("cs_darya") == "PRESENT_OFFSCREEN"
    $ cs_qa_capture("editorial_reading_private")
    click until label cs_director_check_1915709574
    pause 0.5
    assert renpy.showing("cs_darya") and renpy.showing("cs_zhenya")
    $ cs_qa_capture("editorial_reading_conversation")
    click until label cs_qa_editorial_reading_end
    assert renpy.showing("cs_darya") and renpy.showing("cs_zhenya")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_editorial_reading_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_editorial_exit:
    $ cs_active = True
    $ night_time()
    scene bg ext_square_night
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    call cs_day02_70
    label cs_qa_editorial_exit_end:
    pause
    return

testcase cs_editorial_exit:
    pause 1.0
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_editorial_exit")
    click until label cs_director_check_c7fd37f7e0
    assert not renpy.showing("cs_darya") and cs_director_states.get("cs_darya") == "ABSENT"
    $ renpy.take_screenshot()
    $ renpy.save("cs_editorial_real_exit")
    $ renpy.load("cs_editorial_real_exit")
    pause 0.5
    assert not renpy.showing("cs_darya")
    $ cs_qa_capture("editorial_real_exit")
    click until label cs_qa_editorial_exit_end
    assert not renpy.showing("cs_darya")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_editorial_exit_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
