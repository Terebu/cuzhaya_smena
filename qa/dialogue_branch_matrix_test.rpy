# -*- coding: utf-8 -*-
label cs_qa_dialogue_branch_matrix:
    $ cs_active = True
    $ cs_qa_global_audit = True
    $ cs_darya_known = True
    $ cs_met_mz = True
    $ cs_lena_elbow_bandaged = True
    $ cs_lena_no_sport_day2 = True
    $ cs_lena_elbow_injury_day2 = 2
    $ day_time()
    $ persistent.sprite_time = "day"
    pause
    $ cs_friend_mz = 1
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_0:
    pause
    call cs_day01_61
    label cs_check_matrix_after_0:
    pause
    $ cs_friend_mz = 1
    $ cs_friend_un = 1
    $ cs_met_un = True
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_1:
    pause
    call cs_day01_61
    label cs_check_matrix_after_1:
    pause
    $ cs_friend_mz = 0
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = False
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_2:
    pause
    call cs_day02_reading_interlude
    label cs_check_matrix_after_2:
    pause
    $ cs_friend_mz = 1
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = False
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_3:
    pause
    call cs_day02_reading_interlude
    label cs_check_matrix_after_3:
    pause
    $ cs_friend_mz = 2
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = False
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_4:
    pause
    call cs_day02_reading_interlude
    label cs_check_matrix_after_4:
    pause
    $ cs_friend_mz = 0
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    label cs_check_matrix_before_5:
    pause
    call cs_day02_64
    label cs_check_matrix_after_5:
    pause
    $ cs_friend_mz = 1
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    label cs_check_matrix_before_6:
    pause
    call cs_day02_64
    label cs_check_matrix_after_6:
    pause
    $ cs_friend_mz = 2
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    label cs_check_matrix_before_7:
    pause
    call cs_day02_64
    label cs_check_matrix_after_7:
    pause
    $ cs_friend_mz = 2
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = True
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    label cs_check_matrix_before_8:
    pause
    call cs_day02_64
    label cs_check_matrix_after_8:
    pause
    $ cs_friend_mz = 0
    $ cs_friend_un = 0
    $ cs_met_un = False
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_mz_map_lead = False
    $ cs_sl_good_seats = False
    $ cs_mi_intro_revised = False
    $ cs_helped_sl_day2 = False
    $ cs_day02_miku_listened = False
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_9:
    pause
    call cs_day02_concert
    label cs_check_matrix_after_9:
    pause
    $ cs_friend_mz = 2
    $ cs_friend_un = 2
    $ cs_met_un = True
    $ cs_friend_se = 2
    $ cs_friend_sl = 1
    $ cs_friend_mi = 1
    $ cs_friend_viola = 2
    $ cs_mz_map_lead = True
    $ cs_sl_good_seats = True
    $ cs_mi_intro_revised = True
    $ cs_helped_sl_day2 = True
    $ cs_day02_miku_listened = True
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_mz_quiet_visit_seen = True
    $ cs_mz_reading_invite = False
    $ cs_qa_matrix_scores = (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola)
    $ cs_director_scene("black")
    scene black
    label cs_check_matrix_before_10:
    pause
    call cs_day02_concert
    label cs_check_matrix_after_10:
    pause
    return

testcase cs_dialogue_branch_matrix:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.force = True
    $ _test.timeout = 60.0
    $ renpy.cs_qa_branch_results = []
    run Start("cs_qa_dialogue_branch_matrix")
    click until label cs_check_matrix_before_0
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_matrix_after_0
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=0,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_day1_tikhonova_0")
    click until label cs_check_matrix_before_1
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_before_1")
    $ renpy.load("cs_matrix_before_1")
    pause 0.2
    click until label cs_check_matrix_after_1
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=1,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_day1_tikhonova_1")
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_after_1")
    $ renpy.load("cs_matrix_after_1")
    pause 0.2
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    click until label cs_check_matrix_before_2
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_matrix_after_2
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=2,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_reading_0")
    click until label cs_check_matrix_before_3
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_matrix_after_3
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=3,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_reading_1")
    click until label cs_check_matrix_before_4
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_before_4")
    $ renpy.load("cs_matrix_before_4")
    pause 0.2
    click until label cs_check_matrix_after_4
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=4,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_reading_2")
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_after_4")
    $ renpy.load("cs_matrix_after_4")
    pause 0.2
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    click until label cs_check_matrix_before_5
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_dinner64_separate
    pause 0.4
    assert renpy.showing("cs_darya") and not renpy.showing("cs_zhenya")
    $ cs_qa_capture("dialogue_branch_dinner_zero_separate")
    click until label cs_check_matrix_after_5
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=5,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_dinner_0_map_0")
    click until label cs_check_matrix_before_6
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_matrix_after_6
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=6,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_dinner_1_map_0")
    click until label cs_check_matrix_before_7
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_matrix_after_7
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=7,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_dinner_2_map_0")
    click until label cs_check_matrix_before_8
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_before_8")
    $ renpy.load("cs_matrix_before_8")
    pause 0.2
    click until label cs_check_matrix_after_8
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=8,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_dinner_2_map_1")
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_after_8")
    $ renpy.load("cs_matrix_after_8")
    pause 0.2
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    click until label cs_check_matrix_before_9
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    click until label cs_check_matrix_after_9
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=9,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_concert_0")
    click until label cs_check_matrix_before_10
    pause 0.2
    $ renpy.cs_qa_branch_before = cs_qa_global_speaker_checks
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_before_10")
    $ renpy.load("cs_matrix_before_10")
    pause 0.2
    click until label cs_check_matrix_after_10
    pause 0.3
    assert cs_qa_global_speaker_checks > renpy.cs_qa_branch_before
    $ renpy.cs_qa_branch_results.append(dict(case=10,speaker_checks=cs_qa_global_speaker_checks-renpy.cs_qa_branch_before))
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    $ cs_qa_capture("dialogue_branch_concert_1")
    $ renpy.take_screenshot()
    $ renpy.save("cs_matrix_after_10")
    $ renpy.load("cs_matrix_after_10")
    pause 0.2
    assert (cs_friend_mz,cs_friend_un,cs_friend_se,cs_friend_sl,cs_friend_mi,cs_friend_viola) == cs_qa_matrix_scores
    assert len(renpy.cs_qa_branch_results) == 11
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/dialogue_branch_results.json", "w").write(json.dumps(renpy.cs_qa_branch_results))
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/dialogue_branch_matrix_pass.txt", "w").write("PASS: 11 branch cases; friendship preserved")
    run Quit(confirm=False)
