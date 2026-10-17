# -*- coding: utf-8 -*-
testcase cs_part05_m1_s1_e1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg ext_clubs_day", "bg ext_square_day", "sl normal pioneer far", "cs normal", "cs_cg_lena_darya_hand_in_hand_day"))
    assert __import__("__builtin__").all(renpy.loadable("sound/music/" + x + ".ogg") for x in ("my_daily_life", "lets_be_friends", "get_to_know_me_better", "a_promise_from_distant_days"))
    run Start("cs_qa_part05_load_help")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part05_audit = True
    $ cs_day02_miku_listened = True
    $ cs_friend_mi = 1
    $ cs_helped_sl_day2 = True
    $ cs_friend_sl = 1
    $ cs_qa_part05_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)
    $ _history_list = []
    click until label cs_check_part05_s34
    pause 0.5
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part05_m1_s1_e1_continuity")
    click until run CSQAwaitMenu()
    pause 0.5
    assert cs_friend_se == 0
    $ cs_qa_capture("cs_part05_m1_s1_e1_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m1_s1_e1-menu")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m1_s1_e1-menu")
    pause 0.5
    assert cs_friend_se == 0
    "Давай сделаем надпись вместе"
    click until label cs_check_part05_poster_finished
    pause 0.5
    assert cs_day02_poster_finished
    assert cs_friend_se == 1 and cs_worked_with_se_day2 == True
    click until label cs_check_part05_sl_arrived
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s1_e1_three_clubs")
    click until label cs_check_part05_sl_helped
    pause 0.5
    $ cs_qa_capture("cs_part05_m1_s1_e1_sl_branch")
    click until label cs_check_part05_s37
    pause 0.5
    assert renpy.showing("bg ext_square_day")
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s1_e1_three_square")
    assert ('спасибо ещё раз за помощь с коробками' in u" ".join(x.what for x in _history_list)) == True
    click until label cs_check_part05_viola_arrived
    pause 0.5
    assert cs_met_viola and cs_day02_poster_posted
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s1_e1_viola")
    click until label cs_check_part05_viola_left
    pause 0.5
    assert not renpy.showing("cs")
    assert renpy.showing("sl") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m1_s1_e1_viola_left")
    click until label cs_check_part05_companions_left
    pause 0.5
    assert not renpy.showing("sl") and not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s1_e1_departed")
    click until label cs_check_part05_s38
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part05_m1_s1_e1_private_walk")
    click until label cs_check_part05_hand_in_hand
    pause 1.0
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m1_s1_e1_hand_in_hand")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m1_s1_e1-cg")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m1_s1_e1-cg")
    pause 0.5
    assert cs_friend_se == 1 and renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    click until label cs_check_part05_pending
    pause 3.0
    assert not cs_day02_done and cs_day02_part05_complete
    assert cs_day02_poster_finished and cs_day02_poster_posted
    assert cs_friend_se == 1
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part05_prior_friends
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert renpy.music.get_playing() is None
    assert renpy.get_screen("cs_day02_walk_continue_screen") is not None
    assert ('высокую лавку' in u" ".join(x.what for x in _history_list)) == True
    $ cs_qa_capture("cs_part05_m1_s1_e1_end")
    run Jump("cs_qa_semen_replay")
    click until run CSQAwaitMenu()
    "Давай сделаем надпись вместе"
    click until label cs_check_part05_pending
    assert cs_friend_se == 1 and cs_se_day2_awarded
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part05_m1_s1_e1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part05_m0_s1_e0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg ext_clubs_day", "bg ext_square_day", "sl normal pioneer far", "cs normal", "cs_cg_lena_darya_hand_in_hand_day"))
    assert __import__("__builtin__").all(renpy.loadable("sound/music/" + x + ".ogg") for x in ("my_daily_life", "lets_be_friends", "get_to_know_me_better", "a_promise_from_distant_days"))
    run Start("cs_qa_part05_load_leave")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part05_audit = True
    $ cs_day02_miku_listened = False
    $ cs_friend_mi = 0
    $ cs_helped_sl_day2 = True
    $ cs_friend_sl = 1
    $ cs_qa_part05_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)
    $ _history_list = []
    click until label cs_check_part05_s34
    pause 0.5
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part05_m0_s1_e0_continuity")
    click until run CSQAwaitMenu()
    pause 0.5
    assert cs_friend_se == 0
    $ cs_qa_capture("cs_part05_m0_s1_e0_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m0_s1_e0-menu")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m0_s1_e0-menu")
    pause 0.5
    assert cs_friend_se == 0
    "Я закончу рисунок, а ты займись буквами"
    click until label cs_check_part05_poster_finished
    pause 0.5
    assert cs_day02_poster_finished
    assert cs_friend_se == 0 and cs_worked_with_se_day2 == False
    click until label cs_check_part05_sl_arrived
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s1_e0_three_clubs")
    click until label cs_check_part05_sl_helped
    pause 0.5
    $ cs_qa_capture("cs_part05_m0_s1_e0_sl_branch")
    click until label cs_check_part05_s37
    pause 0.5
    assert renpy.showing("bg ext_square_day")
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s1_e0_three_square")
    assert ('спасибо ещё раз за помощь с коробками' in u" ".join(x.what for x in _history_list)) == True
    click until label cs_check_part05_viola_arrived
    pause 0.5
    assert cs_met_viola and cs_day02_poster_posted
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s1_e0_viola")
    click until label cs_check_part05_viola_left
    pause 0.5
    assert not renpy.showing("cs")
    assert renpy.showing("sl") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m0_s1_e0_viola_left")
    click until label cs_check_part05_companions_left
    pause 0.5
    assert not renpy.showing("sl") and not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s1_e0_departed")
    click until label cs_check_part05_s38
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part05_m0_s1_e0_private_walk")
    click until label cs_check_part05_hand_in_hand
    pause 1.0
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m0_s1_e0_hand_in_hand")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m0_s1_e0-cg")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m0_s1_e0-cg")
    pause 0.5
    assert cs_friend_se == 0 and renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    click until label cs_check_part05_pending
    pause 3.0
    assert not cs_day02_done and cs_day02_part05_complete
    assert cs_day02_poster_finished and cs_day02_poster_posted
    assert cs_friend_se == 0
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part05_prior_friends
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert renpy.music.get_playing() is None
    assert renpy.get_screen("cs_day02_walk_continue_screen") is not None
    assert ('высокую лавку' in u" ".join(x.what for x in _history_list)) == False
    $ cs_qa_capture("cs_part05_m0_s1_e0_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part05_m0_s1_e0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part05_m1_s0_e0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg ext_clubs_day", "bg ext_square_day", "sl normal pioneer far", "cs normal", "cs_cg_lena_darya_hand_in_hand_day"))
    assert __import__("__builtin__").all(renpy.loadable("sound/music/" + x + ".ogg") for x in ("my_daily_life", "lets_be_friends", "get_to_know_me_better", "a_promise_from_distant_days"))
    run Start("cs_qa_part05_load_help")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part05_audit = True
    $ cs_day02_miku_listened = True
    $ cs_friend_mi = 1
    $ cs_helped_sl_day2 = False
    $ cs_friend_sl = 0
    $ cs_qa_part05_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)
    $ _history_list = []
    click until label cs_check_part05_s34
    pause 0.5
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part05_m1_s0_e0_continuity")
    click until run CSQAwaitMenu()
    pause 0.5
    assert cs_friend_se == 0
    $ cs_qa_capture("cs_part05_m1_s0_e0_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m1_s0_e0-menu")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m1_s0_e0-menu")
    pause 0.5
    assert cs_friend_se == 0
    "Я закончу рисунок, а ты займись буквами"
    click until label cs_check_part05_poster_finished
    pause 0.5
    assert cs_day02_poster_finished
    assert cs_friend_se == 0 and cs_worked_with_se_day2 == False
    click until label cs_check_part05_sl_arrived
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s0_e0_three_clubs")
    click until label cs_check_part05_sl_neutral
    pause 0.5
    $ cs_qa_capture("cs_part05_m1_s0_e0_sl_branch")
    click until label cs_check_part05_s37
    pause 0.5
    assert renpy.showing("bg ext_square_day")
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s0_e0_three_square")
    assert ('спасибо ещё раз за помощь с коробками' in u" ".join(x.what for x in _history_list)) == False
    click until label cs_check_part05_viola_arrived
    pause 0.5
    assert cs_met_viola and cs_day02_poster_posted
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s0_e0_viola")
    click until label cs_check_part05_viola_left
    pause 0.5
    assert not renpy.showing("cs")
    assert renpy.showing("sl") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m1_s0_e0_viola_left")
    click until label cs_check_part05_companions_left
    pause 0.5
    assert not renpy.showing("sl") and not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m1_s0_e0_departed")
    click until label cs_check_part05_s38
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part05_m1_s0_e0_private_walk")
    click until label cs_check_part05_hand_in_hand
    pause 1.0
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m1_s0_e0_hand_in_hand")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m1_s0_e0-cg")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m1_s0_e0-cg")
    pause 0.5
    assert cs_friend_se == 0 and renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    click until label cs_check_part05_pending
    pause 3.0
    assert not cs_day02_done and cs_day02_part05_complete
    assert cs_day02_poster_finished and cs_day02_poster_posted
    assert cs_friend_se == 0
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part05_prior_friends
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert renpy.music.get_playing() is None
    assert renpy.get_screen("cs_day02_walk_continue_screen") is not None
    assert ('высокую лавку' in u" ".join(x.what for x in _history_list)) == True
    $ cs_qa_capture("cs_part05_m1_s0_e0_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part05_m1_s0_e0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part05_m0_s0_e1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg ext_clubs_day", "bg ext_square_day", "sl normal pioneer far", "cs normal", "cs_cg_lena_darya_hand_in_hand_day"))
    assert __import__("__builtin__").all(renpy.loadable("sound/music/" + x + ".ogg") for x in ("my_daily_life", "lets_be_friends", "get_to_know_me_better", "a_promise_from_distant_days"))
    run Start("cs_qa_part05_load_leave")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part05_audit = True
    $ cs_day02_miku_listened = False
    $ cs_friend_mi = 0
    $ cs_helped_sl_day2 = False
    $ cs_friend_sl = 0
    $ cs_qa_part05_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)
    $ _history_list = []
    click until label cs_check_part05_s34
    pause 0.5
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    $ cs_qa_capture("cs_part05_m0_s0_e1_continuity")
    click until run CSQAwaitMenu()
    pause 0.5
    assert cs_friend_se == 0
    $ cs_qa_capture("cs_part05_m0_s0_e1_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m0_s0_e1-menu")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m0_s0_e1-menu")
    pause 0.5
    assert cs_friend_se == 0
    "Давай сделаем надпись вместе"
    click until label cs_check_part05_poster_finished
    pause 0.5
    assert cs_day02_poster_finished
    assert cs_friend_se == 1 and cs_worked_with_se_day2 == True
    click until label cs_check_part05_sl_arrived
    pause 0.5
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s0_e1_three_clubs")
    click until label cs_check_part05_sl_neutral
    pause 0.5
    $ cs_qa_capture("cs_part05_m0_s0_e1_sl_branch")
    click until label cs_check_part05_s37
    pause 0.5
    assert renpy.showing("bg ext_square_day")
    assert renpy.showing("sl") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s0_e1_three_square")
    assert ('спасибо ещё раз за помощь с коробками' in u" ".join(x.what for x in _history_list)) == False
    click until label cs_check_part05_viola_arrived
    pause 0.5
    assert cs_met_viola and cs_day02_poster_posted
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s0_e1_viola")
    click until label cs_check_part05_viola_left
    pause 0.5
    assert not renpy.showing("cs")
    assert renpy.showing("sl") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m0_s0_e1_viola_left")
    click until label cs_check_part05_companions_left
    pause 0.5
    assert not renpy.showing("sl") and not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part05_m0_s0_e1_departed")
    click until label cs_check_part05_s38
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part05_m0_s0_e1_private_walk")
    click until label cs_check_part05_hand_in_hand
    pause 1.0
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part05_m0_s0_e1_hand_in_hand")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part05_m0_s0_e1-cg")
    $ cs_friend_se = 99
    $ renpy.load("cs_part05_m0_s0_e1-cg")
    pause 0.5
    assert cs_friend_se == 1 and renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    click until label cs_check_part05_pending
    pause 3.0
    assert not cs_day02_done and cs_day02_part05_complete
    assert cs_day02_poster_finished and cs_day02_poster_posted
    assert cs_friend_se == 1
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part05_prior_friends
    assert renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert renpy.music.get_playing() is None
    assert renpy.get_screen("cs_day02_walk_continue_screen") is not None
    assert ('высокую лавку' in u" ".join(x.what for x in _history_list)) == False
    $ cs_qa_capture("cs_part05_m0_s0_e1_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part05_m0_s0_e1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
