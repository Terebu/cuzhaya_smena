# -*- coding: utf-8 -*-
label cs_qa_gallery:
    $ cs_active = True
    $ cs_darya_known = False
    $ prolog_time()
    $ persistent.sprite_time = "day"
    scene cs_bus_city
    window show
    call cs_scene_03
    call cs_scene_04
    label cs_check_gallery_done:
    $ renpy.pause(hard=True)
    jump cs_check_gallery_done

testcase cs_instagram_focus:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_gallery")
    click until label cs_check_instagram_oni
    pause 0.6
    assert renpy.get_screen("cs_instagram_post") is not None
    assert not renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("instagram_focus_oni")
    click until label cs_check_instagram_crush
    pause 0.6
    assert not renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("instagram_focus_crush")
    # Emulate an older save in which the card overlapped a visible companion.
    $ renpy.show("cs_dasha_winter shrug normal", at_list=[cs_darya_normal_center])
    $ renpy.take_screenshot()
    $ renpy.save("cs-instagram-focused")
    $ renpy.load("cs-instagram-focused")
    pause 0.6
    assert renpy.get_screen("cs_instagram_post") is not None
    assert not renpy.showing("cs_dasha_winter")
    click until label cs_check_instagram_daily
    assert not renpy.showing("cs_dasha_winter")
    click until label cs_check_battery5
    pause 0.6
    assert renpy.get_screen("cs_instagram_post") is None
    assert renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("instagram_focus_return")
    click until label cs_check_gallery_done
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/instagram_focus_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: gallery-only focus, Darya hidden across posts and save/load, one return after closing gallery.\n")
    run Quit(confirm=False)
