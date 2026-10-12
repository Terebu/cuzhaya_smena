# -*- coding: utf-8 -*-
testcase cs_darya_dialogue:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    run Start("cs_qa_day01_part04")
    click until label cs_check_day01_part04_housing
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("darya_present_olga")
    click until label cs_check_darya_housing_talk
    pause 0.5
    assert renpy.showing("cs_darya arms_crossed pioneer normal")
    $ cs_qa_capture("darya_housing_reaction")
    click until label cs_check_darya_housing_hide
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("darya_present_group_talk")
    click until label cs_check_darya_hold_pause
    pause 0.6
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("darya_kept_during_pause")
    click until label cs_check_darya_reasoning
    pause 0.5
    assert renpy.showing("cs_darya thinking pioneer normal")
    $ cs_qa_capture("darya_thinking_new")
    click until label cs_check_darya_smile
    pause 0.5
    assert renpy.showing("cs_darya smile pioneer normal")
    $ cs_qa_capture("darya_smile_new")
    click until label cs_check_darya_semen_focus
    pause 0.5
    assert renpy.showing("cs_darya")
    click until label cs_check_day01_part04_final
    pause 0.5
    assert renpy.showing("cs_darya")
    assert renpy.showing("cs_semen surprised pioneer far")
    assert renpy.showing("cs_darya surprised pioneer far")
    $ cs_qa_capture("darya_present_semen_talk")
    click until label cs_check_day01_part08_pending
    pause 0.5
    assert cs_day01_part04_done
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/darya_dialogue_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: Darya remains present with Olga/Semyon, Lena and narration pauses; crossed arms, thinking and smile; new full PNGs.\n")
    run Quit(confirm=False)
