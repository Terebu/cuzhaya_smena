# -*- coding: utf-8 -*-
testcase cs_dinner_revised_zero:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 50.0
    run Start("cs_qa_dinner_revised_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (0, 1, 1, 0, 2, 2)
    $ cs_qa_part09_scores = (0, 1, 1, 0, 2, 2)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_qa_dinner_revised_run")
    click until label cs_check_dinner64_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_zero_greeting")
    click until label cs_check_dinner64c
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    click until label cs_check_dinner64_separate
    pause 0.5
    assert not renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_dinner_revised_zero_alone")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == False
    $ cs_qa_capture("cs_dinner_revised_zero_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == False
    click until label cs_check_dinner64_exit
    pause 0.5
    assert renpy.showing("bg ext_square_sunset") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_zero_exit")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats and cs_mi_intro_revised
    assert not cs_day02_done
    assert cs_qa_part09_visits.count("cs_day02_64") == 1 and cs_qa_part09_visits.count("cs_day02_65") == 1
    assert ("cs_day02_64d1" in cs_qa_part09_visits) == False
    assert ("cs_day02_64d2" in cs_qa_part09_visits) == False
    assert ("cs_day02_64d" in cs_qa_part09_visits) == False
    assert __import__("__builtin__").all(("cs_day02_64"+x in cs_qa_part09_visits) == (x=="c") for x in ("a","b","c"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_dinner_revised_zero_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_dinner_revised_zero-end")
    $ cs_mz_map_lead = not cs_mz_map_lead
    $ renpy.load("cs_dinner_revised_zero-end")
    pause 0.5
    assert cs_mz_map_lead == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_dinner_revised_zero_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_dinner_revised_one:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 50.0
    run Start("cs_qa_dinner_revised_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (1, 1, 1, 2, 2, 2)
    $ cs_qa_part09_scores = (1, 1, 1, 2, 2, 2)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_qa_dinner_revised_run")
    click until label cs_check_dinner64_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_one_greeting")
    click until label cs_check_dinner64b
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    click until label cs_check_dinner64d
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_dinner_revised_one_shared")
    click until label cs_check_dinner64d2
    pause 0.5
    $ cs_qa_capture("cs_dinner_revised_one_trust")
    $ renpy.take_screenshot()
    $ renpy.save("cs_dinner_revised_one-trust")
    $ cs_mz_map_lead = not cs_mz_map_lead
    $ renpy.load("cs_dinner_revised_one-trust")
    pause 0.5
    assert cs_mz_map_lead == False
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == True
    $ cs_qa_capture("cs_dinner_revised_one_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == True
    click until label cs_check_dinner64_zhenya_left
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_dinner64_exit
    pause 0.5
    assert renpy.showing("bg ext_square_sunset") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_one_exit")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats and cs_mi_intro_revised
    assert not cs_day02_done
    assert cs_qa_part09_visits.count("cs_day02_64") == 1 and cs_qa_part09_visits.count("cs_day02_65") == 1
    assert ("cs_day02_64d1" in cs_qa_part09_visits) == False
    assert ("cs_day02_64d2" in cs_qa_part09_visits) == True
    assert ("cs_day02_64d" in cs_qa_part09_visits) == True
    assert __import__("__builtin__").all(("cs_day02_64"+x in cs_qa_part09_visits) == (x=="b") for x in ("a","b","c"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_dinner_revised_one_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_dinner_revised_one-end")
    $ cs_mz_map_lead = not cs_mz_map_lead
    $ renpy.load("cs_dinner_revised_one-end")
    pause 0.5
    assert cs_mz_map_lead == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_dinner_revised_one_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_dinner_revised_trust:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 50.0
    run Start("cs_qa_dinner_revised_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (2, 1, 1, 2, 2, 2)
    $ cs_qa_part09_scores = (2, 1, 1, 2, 2, 2)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = True
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_qa_dinner_revised_run")
    click until label cs_check_dinner64_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_trust_greeting")
    click until label cs_check_dinner64a
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    click until label cs_check_dinner64d
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_dinner_revised_trust_shared")
    click until label cs_check_dinner64d1
    pause 0.5
    $ cs_qa_capture("cs_dinner_revised_trust_trust")
    $ renpy.take_screenshot()
    $ renpy.save("cs_dinner_revised_trust-trust")
    $ cs_mz_map_lead = not cs_mz_map_lead
    $ renpy.load("cs_dinner_revised_trust-trust")
    pause 0.5
    assert cs_mz_map_lead == True
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == True
    $ cs_qa_capture("cs_dinner_revised_trust_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == True
    click until label cs_check_dinner64_zhenya_left
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_dinner64_exit
    pause 0.5
    assert renpy.showing("bg ext_square_sunset") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_trust_exit")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert cs_mz_map_lead == True
    assert cs_sl_good_seats and cs_mi_intro_revised
    assert not cs_day02_done
    assert cs_qa_part09_visits.count("cs_day02_64") == 1 and cs_qa_part09_visits.count("cs_day02_65") == 1
    assert ("cs_day02_64d1" in cs_qa_part09_visits) == True
    assert ("cs_day02_64d2" in cs_qa_part09_visits) == False
    assert ("cs_day02_64d" in cs_qa_part09_visits) == True
    assert __import__("__builtin__").all(("cs_day02_64"+x in cs_qa_part09_visits) == (x=="a") for x in ("a","b","c"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_dinner_revised_trust_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_dinner_revised_trust-end")
    $ cs_mz_map_lead = not cs_mz_map_lead
    $ renpy.load("cs_dinner_revised_trust-end")
    pause 0.5
    assert cs_mz_map_lead == True
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_dinner_revised_trust_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_dinner_revised_no_lead:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 50.0
    run Start("cs_qa_dinner_revised_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (2, 1, 1, 0, 2, 2)
    $ cs_qa_part09_scores = (2, 1, 1, 0, 2, 2)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_qa_dinner_revised_run")
    click until label cs_check_dinner64_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_no_lead_greeting")
    click until label cs_check_dinner64a
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    click until label cs_check_dinner64d
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_dinner_revised_no_lead_shared")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == True
    $ cs_qa_capture("cs_dinner_revised_no_lead_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == True
    click until label cs_check_dinner64_zhenya_left
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_dinner64_exit
    pause 0.5
    assert renpy.showing("bg ext_square_sunset") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_dinner_revised_no_lead_exit")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats and cs_mi_intro_revised
    assert not cs_day02_done
    assert cs_qa_part09_visits.count("cs_day02_64") == 1 and cs_qa_part09_visits.count("cs_day02_65") == 1
    assert ("cs_day02_64d1" in cs_qa_part09_visits) == False
    assert ("cs_day02_64d2" in cs_qa_part09_visits) == False
    assert ("cs_day02_64d" in cs_qa_part09_visits) == True
    assert __import__("__builtin__").all(("cs_day02_64"+x in cs_qa_part09_visits) == (x=="a") for x in ("a","b","c"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_dinner_revised_no_lead_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_dinner_revised_no_lead-end")
    $ cs_mz_map_lead = not cs_mz_map_lead
    $ renpy.load("cs_dinner_revised_no_lead-end")
    pause 0.5
    assert cs_mz_map_lead == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_dinner_revised_no_lead_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
