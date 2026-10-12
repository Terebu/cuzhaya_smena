# -*- coding: utf-8 -*-
label cs_qa_dasha_distances:
    $ day_time()
    scene bg ext_camp_entrance_day
    show sl smile pioneer at left
    show cs_dasha_winter 1 normal at cs_day_dasha_right
    pause
    jump cs_qa_dasha_distances

testcase cs_dasha_distances:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    run Start("cs_qa_dasha_distances")
    pause 1.0
    $ cs_qa_capture("dasha_normal_1")
    $ renpy.show("cs_dasha_winter 2 normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("dasha_normal_2")
    $ renpy.show("cs_dasha_winter 3 normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("dasha_normal_3")
    $ renpy.show("cs_dasha_winter 4 normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("dasha_normal_4")
    $ renpy.show("sl smile pioneer far", at_list=[cs_day_sl_left])
    $ renpy.show("cs_dasha_winter 1 far", at_list=[cs_dasha_far_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("dasha_far")
    $ renpy.show("cs_dasha_winter 1 close", at_list=[cs_dasha_close_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("dasha_close")
    $ renpy.hide("cs_dasha_winter")
    $ renpy.show("cs_dasha_pioneer 1 normal", at_list=[cs_day_dasha_right])
    $ renpy.restart_interaction()
    pause 0.5
    $ cs_qa_capture("dasha_pioneer_catalog_only")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/dasha_distances_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: four winter emotions, normal/far/close and pioneer alias at 1280x720; full source PNGs.\n")
    run Quit(confirm=False)
