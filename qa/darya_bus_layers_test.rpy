# -*- coding: utf-8 -*-
label cs_qa_darya_bus_layers:
    $ cs_active = True
    $ cs_darya_known = False
    $ prolog_time()
    $ persistent.sprite_time = "day"
    scene cs_bus_city at cs_bus_ride
    show cs_dasha_winter shrug normal at cs_dasha_seated
    call cs_scene_05
    call cs_scene_06
    jump cs_day01_part09_pending

testcase cs_darya_bus_layers:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    run Start("cs_qa_darya_bus_layers")
    click until label cs_check_winter
    pause 0.6
    assert renpy.showing("cs_bus_winter")
    assert renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("darya_winter_background_layer_fixed")
    click until label cs_check_introduced
    pause 0.6
    assert cs_darya_known and renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("darya_winter_name_layer_fixed")
    click until label cs_check_sleep_winter
    pause 0.6
    $ cs_qa_capture("darya_winter_sleep_layer_fixed")
    click until label cs_check_cg_winter
    pause 0.6
    assert renpy.showing("cs_sleep_winter")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/darya_bus_layers_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: winter background remains behind present Darya, introduction and sleep CG transition.\n")
    run Quit(confirm=False)
