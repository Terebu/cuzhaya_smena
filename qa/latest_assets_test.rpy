# -*- coding: utf-8 -*-
# Opt-in visual verification of the thirty newly supplied sprites and house BGs.
label cs_qa_latest_assets:
    $ day_time()
    $ persistent.sprite_time = "day"
    scene cs_house_lena_darya_ext_day
    pause 0.2
    $ cs_qa_capture("latest_house_ext_day")
    scene cs_house_lena_darya_int_day
    pause 0.2
    $ cs_qa_capture("latest_house_int_day")
    scene bg ext_camp_entrance_day
    python:
        for cs_e in cs_dasha_metadata["winter"][4:]:
            renpy.show("cs_dasha_winter " + cs_e["pose"] + " normal", at_list=[cs_day_dasha_right])
            renpy.pause(0.1)
        cs_qa_capture("latest_winter_walking")
        renpy.hide("cs_dasha_winter")
        for cs_e in cs_dasha_metadata["pioneer"][10:]:
            renpy.show("cs_darya " + cs_e["pose"] + " pioneer normal", at_list=[cs_day_dasha_right])
            renpy.pause(0.1)
        cs_qa_capture("latest_darya_surprise_hand")
        renpy.hide("cs_darya")
        for cs_e in cs_semen_metadata[10:]:
            renpy.show("cs_semen " + cs_e["pose"] + " pioneer normal", at_list=[cs_semen_normal_left])
            renpy.pause(0.1)
        cs_qa_capture("latest_semen_grateful")
    label cs_check_latest_assets:
    $ renpy.pause(hard=True)
    return

testcase cs_latest_assets:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    run Start("cs_qa_latest_assets")
    click until label cs_check_latest_assets
    pause 0.5
    assert len(cs_dasha_metadata["winter"]) == 14
    assert len(cs_dasha_metadata["pioneer"]) == 20
    assert len(cs_semen_metadata) == 20
    assert not [e for e in cs_dasha_metadata["pioneer"] if not renpy.has_image("cs_darya " + e["pose"] + " pioneer far")]
    assert not [e for e in cs_semen_metadata if not renpy.has_image("cs_semen " + e["pose"] + " pioneer close")]
    assert renpy.has_image("cs_dasha_winter 4 normal")
    assert renpy.showing("cs_semen grateful pioneer normal")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/latest_assets_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: thirty new full sprites rendered; 54 registered sprites with distances; house BGs; legacy winter aliases retained.\n")
    run Quit(confirm=False)
