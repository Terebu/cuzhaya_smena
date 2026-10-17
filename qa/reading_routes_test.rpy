# -*- coding: utf-8 -*-
testcase cs_reading_zero:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 60.0
    $ _test.force = True
    run Start("cs_qa_reading_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (0, 0, 0, 0, 0, 0)
    $ cs_qa_reading_scores = (0, 0, 0, 0, 0, 0)
    $ cs_qa_reading_visits = []
    $ cs_mz_map_lead = True
    $ cs_qa_reading_map_before = True
    $ cs_mz_quiet_visit_seen = False
    $ cs_mz_reading_invite = False
    $ cs_reading_book_id = None
    $ cs_reading_book_location = "library_shelf"
    $ cs_reading_book_borrowed = False
    $ cs_qa_global_audit = True
    $ cs_qa_reading_audit = True
    $ _history_list = []
    run Jump("cs_day02_part09_start")
    click until label cs_check_reading_darya_left
    pause 0.5
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_zero_darya_left")
    click until label cs_check_reading_02
    pause 2.5
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_reading_zero_alone")
    click until label cs_check_reading_zhenya_approached
    pause 0.5
    assert renpy.showing("cs_zhenya") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_reading_zero_zhenya")
    click until label cs_check_reading_desk_04a
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_darya")
    assert cs_mz_quiet_visit_seen
    click until label cs_check_reading_darya_returned
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_zero_darya_returns")
    click until label cs_check_reading_three
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_reading_zero_three")
    click until label cs_check_reading_checkout
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not cs_reading_book_borrowed
    $ cs_qa_capture("cs_reading_zero_checkout")
    click until label cs_check_reading_borrowed
    pause 0.5
    assert cs_reading_book_borrowed and cs_reading_book_location == "lena_hand"
    assert cs_reading_book_id == "zhenya_second_copy"
    $ renpy.take_screenshot()
    $ renpy.save("cs_reading_zero-book")
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "lost"
    $ renpy.load("cs_reading_zero-book")
    pause 0.5
    assert cs_reading_book_borrowed and cs_reading_book_location == "lena_hand"
    click until label cs_check_reading_book_stored
    pause 0.5
    assert cs_reading_book_location == "cabin_table"
    assert renpy.showing("cs_house_lena_darya_int_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_zero_book_table")
    click until label cs_check_reading_complete
    pause 0.5
    assert cs_mz_quiet_visit_seen and cs_mz_reading_invite == False
    assert cs_mz_map_lead == True
    assert cs_reading_book_borrowed and cs_reading_book_location == "cabin_table"
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_reading_scores
    assert __import__("__builtin__").all(cs_qa_reading_visits.count(x) == 1 for x in ("cs_day02_reading_01","cs_day02_reading_02","cs_day02_reading_03","cs_day02_reading_05","cs_day02_reading_06","cs_day02_reading_08","cs_day02_reading_09","cs_day02_reading_book_drop"))
    assert __import__("__builtin__").all(("cs_day02_reading_04"+x in cs_qa_reading_visits) == (x=="a") for x in ("a","b","c"))
    assert __import__("__builtin__").all(("cs_day02_reading_07"+x in cs_qa_reading_visits) == (x=="a") for x in ("a","b","c"))
    $ cs_qa_capture("cs_reading_zero_to_dinner")
    $ renpy.take_screenshot()
    $ renpy.save("cs_reading_zero-stored")
    $ cs_reading_book_location = "lost"
    $ renpy.load("cs_reading_zero-stored")
    pause 0.5
    assert cs_reading_book_location == "cabin_table"
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_reading_zero_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_reading_one:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 60.0
    $ _test.force = True
    run Start("cs_qa_reading_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (1, 0, 0, 0, 0, 0)
    $ cs_qa_reading_scores = (1, 0, 0, 0, 0, 0)
    $ cs_qa_reading_visits = []
    $ cs_mz_map_lead = False
    $ cs_qa_reading_map_before = False
    $ cs_mz_quiet_visit_seen = False
    $ cs_mz_reading_invite = False
    $ cs_reading_book_id = None
    $ cs_reading_book_location = "library_shelf"
    $ cs_reading_book_borrowed = False
    $ cs_qa_global_audit = True
    $ cs_qa_reading_audit = True
    $ _history_list = []
    run Jump("cs_day02_part09_start")
    click until label cs_check_reading_darya_left
    pause 0.5
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_one_darya_left")
    click until label cs_check_reading_02
    pause 2.5
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_reading_one_alone")
    click until label cs_check_reading_zhenya_approached
    pause 0.5
    assert renpy.showing("cs_zhenya") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_reading_one_zhenya")
    click until label cs_check_reading_desk_04b
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_darya")
    assert cs_mz_quiet_visit_seen
    click until label cs_check_reading_darya_returned
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_one_darya_returns")
    click until label cs_check_reading_three
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_reading_one_three")
    click until label cs_check_reading_checkout
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not cs_reading_book_borrowed
    $ cs_qa_capture("cs_reading_one_checkout")
    click until label cs_check_reading_borrowed
    pause 0.5
    assert cs_reading_book_borrowed and cs_reading_book_location == "lena_hand"
    assert cs_reading_book_id == "zhenya_second_copy"
    $ renpy.take_screenshot()
    $ renpy.save("cs_reading_one-book")
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "lost"
    $ renpy.load("cs_reading_one-book")
    pause 0.5
    assert cs_reading_book_borrowed and cs_reading_book_location == "lena_hand"
    click until label cs_check_reading_book_stored
    pause 0.5
    assert cs_reading_book_location == "cabin_table"
    assert renpy.showing("cs_house_lena_darya_int_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_one_book_table")
    click until label cs_check_reading_complete
    pause 0.5
    assert cs_mz_quiet_visit_seen and cs_mz_reading_invite == False
    assert cs_mz_map_lead == False
    assert cs_reading_book_borrowed and cs_reading_book_location == "cabin_table"
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_reading_scores
    assert __import__("__builtin__").all(cs_qa_reading_visits.count(x) == 1 for x in ("cs_day02_reading_01","cs_day02_reading_02","cs_day02_reading_03","cs_day02_reading_05","cs_day02_reading_06","cs_day02_reading_08","cs_day02_reading_09","cs_day02_reading_book_drop"))
    assert __import__("__builtin__").all(("cs_day02_reading_04"+x in cs_qa_reading_visits) == (x=="b") for x in ("a","b","c"))
    assert __import__("__builtin__").all(("cs_day02_reading_07"+x in cs_qa_reading_visits) == (x=="b") for x in ("a","b","c"))
    $ cs_qa_capture("cs_reading_one_to_dinner")
    $ renpy.take_screenshot()
    $ renpy.save("cs_reading_one-stored")
    $ cs_reading_book_location = "lost"
    $ renpy.load("cs_reading_one-stored")
    pause 0.5
    assert cs_reading_book_location == "cabin_table"
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_reading_one_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_reading_all:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 60.0
    $ _test.force = True
    run Start("cs_qa_reading_load")
    pause 0.5
    $ cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un = (2, 1, 1, 2, 2, 2)
    $ cs_qa_reading_scores = (2, 1, 1, 2, 2, 2)
    $ cs_qa_reading_visits = []
    $ cs_mz_map_lead = False
    $ cs_qa_reading_map_before = False
    $ cs_mz_quiet_visit_seen = False
    $ cs_mz_reading_invite = False
    $ cs_reading_book_id = None
    $ cs_reading_book_location = "library_shelf"
    $ cs_reading_book_borrowed = False
    $ cs_qa_global_audit = True
    $ cs_qa_reading_audit = True
    $ _history_list = []
    run Jump("cs_day02_part09_start")
    click until label cs_check_reading_darya_left
    pause 0.5
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_all_darya_left")
    click until label cs_check_reading_02
    pause 2.5
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_reading_all_alone")
    click until label cs_check_reading_zhenya_approached
    pause 0.5
    assert renpy.showing("cs_zhenya") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_reading_all_zhenya")
    click until label cs_check_reading_desk_04c
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("cs_darya")
    assert cs_mz_quiet_visit_seen
    click until label cs_check_reading_darya_returned
    pause 0.5
    assert renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_all_darya_returns")
    click until label cs_check_reading_three
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_reading_all_three")
    click until label cs_check_reading_invited
    pause 0.5
    assert cs_mz_reading_invite and not renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    click until label cs_check_reading_checkout
    pause 0.5
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    assert not cs_reading_book_borrowed
    $ cs_qa_capture("cs_reading_all_checkout")
    click until label cs_check_reading_borrowed
    pause 0.5
    assert cs_reading_book_borrowed and cs_reading_book_location == "lena_hand"
    assert cs_reading_book_id == "zhenya_second_copy"
    $ renpy.take_screenshot()
    $ renpy.save("cs_reading_all-book")
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "lost"
    $ renpy.load("cs_reading_all-book")
    pause 0.5
    assert cs_reading_book_borrowed and cs_reading_book_location == "lena_hand"
    click until label cs_check_reading_book_stored
    pause 0.5
    assert cs_reading_book_location == "cabin_table"
    assert renpy.showing("cs_house_lena_darya_int_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("cs_reading_all_book_table")
    click until label cs_check_reading_complete
    pause 0.5
    assert cs_mz_quiet_visit_seen and cs_mz_reading_invite == True
    assert cs_mz_map_lead == False
    assert cs_reading_book_borrowed and cs_reading_book_location == "cabin_table"
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_reading_scores
    assert __import__("__builtin__").all(cs_qa_reading_visits.count(x) == 1 for x in ("cs_day02_reading_01","cs_day02_reading_02","cs_day02_reading_03","cs_day02_reading_05","cs_day02_reading_06","cs_day02_reading_08","cs_day02_reading_09","cs_day02_reading_book_drop"))
    assert __import__("__builtin__").all(("cs_day02_reading_04"+x in cs_qa_reading_visits) == (x=="c") for x in ("a","b","c"))
    assert __import__("__builtin__").all(("cs_day02_reading_07"+x in cs_qa_reading_visits) == (x=="c") for x in ("a","b","c"))
    $ cs_qa_capture("cs_reading_all_to_dinner")
    $ renpy.take_screenshot()
    $ renpy.save("cs_reading_all-stored")
    $ cs_reading_book_location = "lost"
    $ renpy.load("cs_reading_all-stored")
    pause 0.5
    assert cs_reading_book_location == "cabin_table"
    click until label cs_check_part09_pending
    pause 3.0
    assert cs_mz_map_lead and cs_sl_good_seats and cs_mi_intro_revised
    assert cs_reading_book_location == "cabin_table" and cs_mz_reading_invite
    assert not cs_day02_done
    assert (cs_friend_mz,cs_friend_sl,cs_friend_mi,cs_friend_se,cs_friend_viola,cs_friend_un) == cs_qa_reading_scores
    $ cs_qa_capture("cs_reading_all_after_dinner")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_reading_all_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
