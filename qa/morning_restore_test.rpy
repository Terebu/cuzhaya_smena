# -*- coding: utf-8 -*-
label cs_qa_morning_restore:
    $ cs_active = True
    $ cs_darya_known = True
    $ day_time()
    $ persistent.sprite_time = "day"
    call cs_day02_07
    call cs_day02_08
    label cs_qa_morning_restore_end:
    pause
    return

testcase cs_morning_restore:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 60.0
    run Start("cs_qa_morning_restore")
    click until label cs_director_check_aedf775c9a
    pause 0.5
    $ renpy.cs_qa_before_restore_bounds = renpy.get_image_bounds("cs_darya")
    $ cs_qa_capture("morning_restore_before")
    click until label cs_check_new_d2_s08
    pause 0.5
    click
    pause 0.5
    assert renpy.showing("cs_darya")
    assert renpy.get_image_bounds("cs_darya") == renpy.cs_qa_before_restore_bounds
    $ cs_qa_capture("morning_restore_wardrobe")
    $ renpy.take_screenshot()
    $ renpy.save("cs_morning_restore")
    $ renpy.load("cs_morning_restore")
    pause 0.5
    assert renpy.get_image_bounds("cs_darya") == renpy.cs_qa_before_restore_bounds
    $ cs_qa_capture("morning_restore_loaded")
    click until label cs_qa_morning_restore_end
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/morning_restore_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
