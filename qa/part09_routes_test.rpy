# -*- coding: utf-8 -*-
testcase cs_part09_zero:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part09_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (0, 0, 0, 0, 0, 0)
    $ cs_qa_part09_scores = (0, 0, 0, 0, 0, 0)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_day02_part09_start")
    click until label cs_check_part09_s60
    pause 0.5
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_zhenya_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part09_zero_greeting")
    click until label cs_check_part09_dinner
    pause 2.5
    assert bool(renpy.showing("cs_zhenya")) == False
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part09_zero_dinner")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == False
    $ cs_qa_capture("cs_part09_zero_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == False
    click until label cs_check_part09_square
    pause 0.5
    assert persistent.timeofday == "sunset"
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_slavya
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_qa_capture("part09_slavya_composition")
    click until label cs_check_part09_seats
    pause 0.5
    assert cs_sl_good_seats == False
    assert not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_zero_seats")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_day02_part09_complete and not cs_day02_done
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats == False
    assert cs_mi_intro_revised == False
    assert renpy.get_screen("cs_day02_concert_wait_screen") is not None
    assert renpy.showing("cs_darya") and not renpy.showing("mi") and not renpy.showing("sl")
    assert renpy.music.get_playing() is None
    assert ("cs_day02_62" in cs_qa_part09_visits) == False
    assert __import__("__builtin__").all(cs_qa_part09_visits.count(x) == 1 for x in ("cs_day02_60","cs_day02_61","cs_day02_63","cs_day02_64","cs_day02_65"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_part09_zero_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_zero-end")
    $ cs_sl_good_seats = not cs_sl_good_seats
    $ renpy.load("cs_part09_zero-end")
    pause 0.5
    assert cs_sl_good_seats == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part09_zero_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part09_zhenya:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part09_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (2, 0, 0, 0, 0, 0)
    $ cs_qa_part09_scores = (2, 0, 0, 0, 0, 0)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_day02_part09_start")
    click until label cs_check_part09_s60
    pause 0.5
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_zhenya_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part09_zhenya_greeting")
    click until label cs_check_part09_map_lead
    pause 0.5
    assert cs_mz_map_lead
    $ cs_qa_capture("cs_part09_zhenya_lead")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_zhenya-lead")
    $ cs_mz_map_lead = False
    $ renpy.load("cs_part09_zhenya-lead")
    pause 0.5
    assert cs_mz_map_lead
    click until label cs_check_part09_dinner
    pause 2.5
    assert bool(renpy.showing("cs_zhenya")) == True
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part09_zhenya_dinner")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == True
    $ cs_qa_capture("cs_part09_zhenya_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == True
    click until label cs_check_part09_square
    pause 0.5
    assert persistent.timeofday == "sunset"
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_slavya
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_qa_capture("part09_slavya_composition")
    click until label cs_check_part09_seats
    pause 0.5
    assert cs_sl_good_seats == False
    assert not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_zhenya_seats")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_day02_part09_complete and not cs_day02_done
    assert cs_mz_map_lead == True
    assert cs_sl_good_seats == False
    assert cs_mi_intro_revised == False
    assert renpy.get_screen("cs_day02_concert_wait_screen") is not None
    assert renpy.showing("cs_darya") and not renpy.showing("mi") and not renpy.showing("sl")
    assert renpy.music.get_playing() is None
    assert ("cs_day02_62" in cs_qa_part09_visits) == True
    assert __import__("__builtin__").all(cs_qa_part09_visits.count(x) == 1 for x in ("cs_day02_60","cs_day02_61","cs_day02_63","cs_day02_64","cs_day02_65"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_part09_zhenya_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_zhenya-end")
    $ cs_sl_good_seats = not cs_sl_good_seats
    $ renpy.load("cs_part09_zhenya-end")
    pause 0.5
    assert cs_sl_good_seats == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part09_zhenya_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part09_zhenya_one:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part09_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (1, 0, 0, 0, 0, 0)
    $ cs_qa_part09_scores = (1, 0, 0, 0, 0, 0)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_day02_part09_start")
    click until label cs_check_part09_s60
    pause 0.5
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_zhenya_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part09_zhenya_one_greeting")
    click until label cs_check_part09_dinner
    pause 2.5
    assert bool(renpy.showing("cs_zhenya")) == True
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part09_zhenya_one_dinner")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == True
    $ cs_qa_capture("cs_part09_zhenya_one_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == True
    click until label cs_check_part09_square
    pause 0.5
    assert persistent.timeofday == "sunset"
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_slavya
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_qa_capture("part09_slavya_composition")
    click until label cs_check_part09_seats
    pause 0.5
    assert cs_sl_good_seats == False
    assert not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_zhenya_one_seats")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_day02_part09_complete and not cs_day02_done
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats == False
    assert cs_mi_intro_revised == False
    assert renpy.get_screen("cs_day02_concert_wait_screen") is not None
    assert renpy.showing("cs_darya") and not renpy.showing("mi") and not renpy.showing("sl")
    assert renpy.music.get_playing() is None
    assert ("cs_day02_62" in cs_qa_part09_visits) == False
    assert __import__("__builtin__").all(cs_qa_part09_visits.count(x) == 1 for x in ("cs_day02_60","cs_day02_61","cs_day02_63","cs_day02_64","cs_day02_65"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_part09_zhenya_one_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_zhenya_one-end")
    $ cs_sl_good_seats = not cs_sl_good_seats
    $ renpy.load("cs_part09_zhenya_one-end")
    pause 0.5
    assert cs_sl_good_seats == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part09_zhenya_one_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part09_seats:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part09_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (0, 1, 0, 2, 0, 0)
    $ cs_qa_part09_scores = (0, 1, 0, 2, 0, 0)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_day02_part09_start")
    click until label cs_check_part09_s60
    pause 0.5
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_zhenya_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part09_seats_greeting")
    click until label cs_check_part09_dinner
    pause 2.5
    assert bool(renpy.showing("cs_zhenya")) == False
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part09_seats_dinner")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == False
    $ cs_qa_capture("cs_part09_seats_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == False
    click until label cs_check_part09_square
    pause 0.5
    assert persistent.timeofday == "sunset"
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_slavya
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_qa_capture("part09_slavya_composition")
    click until label cs_check_part09_seats
    pause 0.5
    assert cs_sl_good_seats == True
    assert not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_seats_seats")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_day02_part09_complete and not cs_day02_done
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats == True
    assert cs_mi_intro_revised == False
    assert renpy.get_screen("cs_day02_concert_wait_screen") is not None
    assert renpy.showing("cs_darya") and not renpy.showing("mi") and not renpy.showing("sl")
    assert renpy.music.get_playing() is None
    assert ("cs_day02_62" in cs_qa_part09_visits) == False
    assert __import__("__builtin__").all(cs_qa_part09_visits.count(x) == 1 for x in ("cs_day02_60","cs_day02_61","cs_day02_63","cs_day02_64","cs_day02_65"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_part09_seats_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_seats-end")
    $ cs_sl_good_seats = not cs_sl_good_seats
    $ renpy.load("cs_part09_seats-end")
    pause 0.5
    assert cs_sl_good_seats == True
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part09_seats_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part09_miku:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part09_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (0, 0, 1, 0, 0, 0)
    $ cs_qa_part09_scores = (0, 0, 1, 0, 0, 0)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_day02_part09_start")
    click until label cs_check_part09_s60
    pause 0.5
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_zhenya_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part09_miku_greeting")
    click until label cs_check_part09_dinner
    pause 2.5
    assert bool(renpy.showing("cs_zhenya")) == False
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part09_miku_dinner")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == False
    $ cs_qa_capture("cs_part09_miku_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == False
    click until label cs_check_part09_square
    pause 0.5
    assert persistent.timeofday == "sunset"
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_slavya
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_qa_capture("part09_slavya_composition")
    click until label cs_check_part09_seats
    pause 0.5
    assert cs_sl_good_seats == False
    assert not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_miku_seats")
    click until label cs_check_part09_miku
    pause 0.5
    assert renpy.showing("mi") and renpy.showing("cs_darya") and not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_miku_miku")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_day02_part09_complete and not cs_day02_done
    assert cs_mz_map_lead == False
    assert cs_sl_good_seats == False
    assert cs_mi_intro_revised == True
    assert renpy.get_screen("cs_day02_concert_wait_screen") is not None
    assert renpy.showing("cs_darya") and not renpy.showing("mi") and not renpy.showing("sl")
    assert renpy.music.get_playing() is None
    assert ("cs_day02_62" in cs_qa_part09_visits) == False
    assert __import__("__builtin__").all(cs_qa_part09_visits.count(x) == 1 for x in ("cs_day02_60","cs_day02_61","cs_day02_63","cs_day02_64","cs_day02_65"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_part09_miku_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_miku-end")
    $ cs_sl_good_seats = not cs_sl_good_seats
    $ renpy.load("cs_part09_miku-end")
    pause 0.5
    assert cs_sl_good_seats == False
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part09_miku_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part09_all:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part09_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (2, 1, 1, 2, 2, 2)
    $ cs_qa_part09_scores = (2, 1, 1, 2, 2, 2)
    $ cs_qa_part09_visits = []
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = True
    $ cs_qa_global_audit = True
    $ cs_qa_part09_audit = True
    run Jump("cs_day02_part09_start")
    click until label cs_check_part09_s60
    pause 0.5
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_zhenya_greeting
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part09_all_greeting")
    click until label cs_check_part09_map_lead
    pause 0.5
    assert cs_mz_map_lead
    $ cs_qa_capture("cs_part09_all_lead")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_all-lead")
    $ cs_mz_map_lead = False
    $ renpy.load("cs_part09_all-lead")
    pause 0.5
    assert cs_mz_map_lead
    click until label cs_check_part09_dinner
    pause 2.5
    assert bool(renpy.showing("cs_zhenya")) == True
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part09_all_dinner")
    click until label cs_check_part09_semen
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert bool(renpy.showing("cs_zhenya")) == True
    $ cs_qa_capture("cs_part09_all_semen")
    click until label cs_check_part09_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen")
    assert bool(renpy.showing("cs_zhenya")) == True
    click until label cs_check_part09_square
    pause 0.5
    assert persistent.timeofday == "sunset"
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_semen")
    click until label cs_check_part09_slavya
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_darya")
    $ cs_qa_capture("part09_slavya_composition")
    click until label cs_check_part09_seats
    pause 0.5
    assert cs_sl_good_seats == True
    assert not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_all_seats")
    click until label cs_check_part09_miku
    pause 0.5
    assert renpy.showing("mi") and renpy.showing("cs_darya") and not renpy.showing("sl")
    $ cs_qa_capture("cs_part09_all_miku")
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_day02_part09_complete and not cs_day02_done
    assert cs_mz_map_lead == True
    assert cs_sl_good_seats == True
    assert cs_mi_intro_revised == True
    assert renpy.get_screen("cs_day02_concert_wait_screen") is not None
    assert renpy.showing("cs_darya") and not renpy.showing("mi") and not renpy.showing("sl")
    assert renpy.music.get_playing() is None
    assert ("cs_day02_62" in cs_qa_part09_visits) == True
    assert __import__("__builtin__").all(cs_qa_part09_visits.count(x) == 1 for x in ("cs_day02_60","cs_day02_61","cs_day02_63","cs_day02_64","cs_day02_65"))
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_part09_scores
    $ cs_qa_capture("cs_part09_all_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part09_all-end")
    $ cs_sl_good_seats = not cs_sl_good_seats
    $ renpy.load("cs_part09_all-end")
    pause 0.5
    assert cs_sl_good_seats == True
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part09_all_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
