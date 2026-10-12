# -*- coding: utf-8 -*-
label cs_qa_new_characters:
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya neutral pioneer normal at cs_day_dasha_right
    pause
    jump cs_qa_new_characters

testcase cs_new_characters:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    run Start("cs_qa_new_characters")
    pause 1.0
    $ renpy.show("cs_darya neutral pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya neutral pioneer normal")
    $ cs_qa_capture("catalog_darya_neutral")
    $ renpy.show("cs_darya smile pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya smile pioneer normal")
    $ renpy.show("cs_darya arms_crossed pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya arms_crossed pioneer normal")
    $ renpy.show("cs_darya thinking pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya thinking pioneer normal")
    $ cs_qa_capture("catalog_darya_thinking")
    $ renpy.show("cs_darya serious pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya serious pioneer normal")
    $ renpy.show("cs_darya sad pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya sad pioneer normal")
    $ renpy.show("cs_darya shy pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya shy pioneer normal")
    $ renpy.show("cs_darya wave pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya wave pioneer normal")
    $ renpy.show("cs_darya shrug pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya shrug pioneer normal")
    $ renpy.show("cs_darya explaining pioneer normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_darya explaining pioneer normal")
    $ renpy.show("cs_semen neutral pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen neutral pioneer normal")
    $ cs_qa_capture("catalog_semen_neutral")
    $ renpy.show("cs_semen relaxed pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen relaxed pioneer normal")
    $ renpy.show("cs_semen arms_crossed pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen arms_crossed pioneer normal")
    $ renpy.show("cs_semen wave pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen wave pioneer normal")
    $ renpy.show("cs_semen awkward pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen awkward pioneer normal")
    $ renpy.show("cs_semen surprised pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen surprised pioneer normal")
    $ cs_qa_capture("catalog_semen_surprised")
    $ renpy.show("cs_semen serious pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen serious pioneer normal")
    $ renpy.show("cs_semen confident pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen confident pioneer normal")
    $ renpy.show("cs_semen shy pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen shy pioneer normal")
    $ renpy.show("cs_semen thinking pioneer normal", at_list=[cs_semen_normal_left])
    $ renpy.restart_interaction()
    pause 0.3
    assert renpy.showing("cs_semen thinking pioneer normal")
    $ cs_qa_capture("catalog_semen_thinking")
    $ renpy.show("cs_semen neutral pioneer far", at_list=[cs_semen_far_center])
    $ renpy.show("cs_darya neutral pioneer far", at_list=[cs_dasha_far_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("catalog_new_far")
    $ renpy.hide("cs_semen")
    $ renpy.show("cs_darya neutral pioneer close", at_list=[cs_dasha_close_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("catalog_darya_close")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/new_characters_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: 20 named full PNGs rendered; normal and far pairs, Darya close.\n")
    run Quit(confirm=False)
