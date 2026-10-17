# -*- coding: utf-8 -*-
testcase cs_breakfast_u0_m1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    run Start("cs_qa_breakfast_load")
    pause 1.5
    $ cs_friend_un = 0
    $ cs_met_un = True
    $ cs_darya_known = True
    $ cs_qa_breakfast_audit = True
    run Jump("cs_qa_breakfast_path")
    click until label cs_check_breakfast_table
    pause 1.0
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert cs_breakfast_un_here == False
    $ cs_qa_capture("cs_breakfast_u0_m1_table")
    $ renpy.take_screenshot()
    $ renpy.save("cs_breakfast_u0_m1-table")
    $ cs_friend_un = 99
    $ renpy.load("cs_breakfast_u0_m1-table")
    pause 1.0
    assert cs_friend_un == 0
    click until label cs_check_breakfast_private
    pause 1.0
    assert not renpy.showing("un") and not cs_breakfast_un_here
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_breakfast_u0_m1_private")
    click until label cs_check_breakfast_square
    pause 1.0
    assert renpy.showing("bg ext_dining_hall_near_day")
    $ cs_qa_capture("cs_breakfast_u0_m1_square")
    click until label cs_check_part02_s15
    pause 1.0
    assert cs_friend_un == 0 and not cs_day02_done
    assert cs_friend_mz == 1
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_breakfast_u0_m1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_breakfast_u1_m1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    run Start("cs_qa_breakfast_load")
    pause 1.5
    $ cs_friend_un = 1
    $ cs_met_un = True
    $ cs_darya_known = True
    $ cs_qa_breakfast_audit = True
    run Jump("cs_qa_breakfast_path")
    click until label cs_check_breakfast_table
    pause 1.0
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert cs_breakfast_un_here == True
    $ cs_qa_capture("cs_breakfast_u1_m1_table")
    $ renpy.take_screenshot()
    $ renpy.save("cs_breakfast_u1_m1-table")
    $ cs_friend_un = 99
    $ renpy.load("cs_breakfast_u1_m1-table")
    pause 1.0
    assert cs_friend_un == 1
    click until label cs_check_breakfast_un
    pause 1.0
    assert renpy.showing("un") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_breakfast_u1_m1_two_lenas")
    $ renpy.take_screenshot()
    $ renpy.save("cs_breakfast_u1_m1-un")
    $ cs_friend_un = 99
    $ renpy.load("cs_breakfast_u1_m1-un")
    pause 1.0
    assert cs_friend_un == 1
    click until label cs_check_breakfast_private
    pause 1.0
    assert not renpy.showing("un") and not cs_breakfast_un_here
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_breakfast_u1_m1_private")
    click until label cs_check_breakfast_square
    pause 1.0
    assert renpy.showing("bg ext_dining_hall_near_day")
    $ cs_qa_capture("cs_breakfast_u1_m1_square")
    click until label cs_check_part02_s15
    pause 1.0
    assert cs_friend_un == 1 and not cs_day02_done
    assert cs_friend_mz == 1
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_breakfast_u1_m1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_breakfast_u1_m0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    run Start("cs_qa_breakfast_load")
    pause 1.5
    $ cs_friend_un = 1
    $ cs_met_un = False
    $ cs_darya_known = True
    $ cs_qa_breakfast_audit = True
    run Jump("cs_qa_breakfast_path")
    click until label cs_check_breakfast_table
    pause 1.0
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert cs_breakfast_un_here == False
    $ cs_qa_capture("cs_breakfast_u1_m0_table")
    $ renpy.take_screenshot()
    $ renpy.save("cs_breakfast_u1_m0-table")
    $ cs_friend_un = 99
    $ renpy.load("cs_breakfast_u1_m0-table")
    pause 1.0
    assert cs_friend_un == 1
    click until label cs_check_breakfast_private
    pause 1.0
    assert not renpy.showing("un") and not cs_breakfast_un_here
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_breakfast_u1_m0_private")
    click until label cs_check_breakfast_square
    pause 1.0
    assert renpy.showing("bg ext_dining_hall_near_day")
    $ cs_qa_capture("cs_breakfast_u1_m0_square")
    click until label cs_check_part02_s15
    pause 1.0
    assert cs_friend_un == 1 and not cs_day02_done
    assert cs_friend_mz == 1
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_breakfast_u1_m0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
