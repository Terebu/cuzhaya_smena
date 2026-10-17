# -*- coding: utf-8 -*-
testcase cs_part06_plan:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert renpy.has_image("bg ext_no_bus") and renpy.loadable("images/bg/ext_no_bus.jpg")
    run Start("cs_qa_part06_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part06_audit = True
    $ cs_qa_part06_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)
    assert cs_friend_se == 1
    click until label cs_check_part06_s40
    pause 1.0
    assert not renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lunch_approach")
    click until label cs_check_part06_semen_arrived
    pause 0.5
    assert renpy.showing("bg int_dining_hall_people_day")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part06_plan_lunch")
    click until run CSQAwaitMenu()
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part06_plan_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part06_plan-menu")
    $ cs_friend_se = 99
    $ renpy.load("cs_part06_plan-menu")
    pause 0.5
    assert cs_friend_se == 1
    "Ограничиться планом проверки дороги"
    click until label cs_check_part06_empty_bus_stop
    pause 1.0
    assert cs_friend_se == 1
    assert renpy.showing("bg ext_no_bus")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_part06_plan_empty_bus_stop")
    click until label cs_check_part06_control_created
    pause 0.5
    assert renpy.showing("cs_road_marked_verge_day")
    $ cs_qa_capture("cs_part06_plan_control")
    click until label cs_check_part06_lap1_a
    pause 0.5
    assert renpy.showing("cs_road_powerlines_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap1_a")
    click until label cs_check_part06_lap1_b
    pause 0.5
    assert renpy.showing("cs_road_left_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap1_b")
    click until label cs_check_part06_lap1_c
    pause 0.5
    assert renpy.showing("cs_road_right_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap1_c")
    click until label cs_check_part06_lap1_return
    pause 0.5
    assert renpy.showing("cs_road_marked_verge_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap1_return")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part06_plan-loop")
    $ cs_friend_se = 99
    $ renpy.load("cs_part06_plan-loop")
    pause 0.5
    assert cs_friend_se == 1
    click until label cs_check_part06_lap2_a
    pause 0.5
    assert renpy.showing("cs_road_powerlines_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap2_a")
    click until label cs_check_part06_lap2_b
    pause 0.5
    assert renpy.showing("cs_road_left_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap2_b")
    click until label cs_check_part06_lap2_c
    pause 0.5
    assert renpy.showing("cs_road_right_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap2_c")
    click until label cs_check_part06_lap2_return
    pause 0.5
    assert renpy.showing("cs_road_marked_verge_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_lap2_return")
    assert renpy.music.get_playing() == "sound/music/waltz_of_doubts.ogg"
    click until label cs_check_part06_gate_return
    pause 0.5
    assert cs_road_loop_observations == 2
    assert renpy.showing("bg ext_no_bus")
    assert cs_road_visual_trace == ["approach", "control_created", "lap1_a", "lap1_b", "lap1_c", "lap1_return", "lap2_a", "lap2_b", "lap2_c", "lap2_return", "back_c", "back_b", "back_a"]
    $ cs_qa_capture("cs_part06_plan_gate_return")
    click until label cs_check_part06_olga_arrived
    pause 0.5
    assert renpy.showing("mt") and renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_olga")
    click until label cs_check_part06_olga_left
    pause 0.5
    assert not renpy.showing("mt") and renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_plan_olga_left")
    click until label cs_check_part06_semen_left
    pause 0.5
    assert cs_road_notes_written
    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part06_plan_semen_left")
    click until label cs_check_part06_pending
    pause 3.0
    assert cs_day02_part06_complete and not cs_day02_done
    assert cs_friend_se == 1
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part06_prior_friends
    assert renpy.showing("cs_darya") and not renpy.showing("mt") and not renpy.showing("cs_semen")
    assert renpy.music.get_playing() is None
    assert renpy.get_screen("cs_day02_road_continue_screen") is not None
    $ cs_qa_capture("cs_part06_plan_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part06_plan_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part06_trust:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert renpy.has_image("bg ext_no_bus") and renpy.loadable("images/bg/ext_no_bus.jpg")
    run Start("cs_qa_part06_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part06_audit = True
    $ cs_qa_part06_prior_friends = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola)
    assert cs_friend_se == 1
    click until label cs_check_part06_s40
    pause 1.0
    assert not renpy.showing("cs_cg_lena_darya_hand_in_hand_day")
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lunch_approach")
    click until label cs_check_part06_semen_arrived
    pause 0.5
    assert renpy.showing("bg int_dining_hall_people_day")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part06_trust_lunch")
    click until run CSQAwaitMenu()
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part06_trust_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part06_trust-menu")
    $ cs_friend_se = 99
    $ renpy.load("cs_part06_trust-menu")
    pause 0.5
    assert cs_friend_se == 1
    "Сказать Семёну, что меня действительно тревожит"
    click until label cs_check_part06_empty_bus_stop
    pause 1.0
    assert cs_friend_se == 2
    assert renpy.showing("bg ext_no_bus")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_part06_trust_empty_bus_stop")
    click until label cs_check_part06_control_created
    pause 0.5
    assert renpy.showing("cs_road_marked_verge_day")
    $ cs_qa_capture("cs_part06_trust_control")
    click until label cs_check_part06_lap1_a
    pause 0.5
    assert renpy.showing("cs_road_powerlines_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap1_a")
    click until label cs_check_part06_lap1_b
    pause 0.5
    assert renpy.showing("cs_road_left_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap1_b")
    click until label cs_check_part06_lap1_c
    pause 0.5
    assert renpy.showing("cs_road_right_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap1_c")
    click until label cs_check_part06_lap1_return
    pause 0.5
    assert renpy.showing("cs_road_marked_verge_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap1_return")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part06_trust-loop")
    $ cs_friend_se = 99
    $ renpy.load("cs_part06_trust-loop")
    pause 0.5
    assert cs_friend_se == 2
    click until label cs_check_part06_lap2_a
    pause 0.5
    assert renpy.showing("cs_road_powerlines_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap2_a")
    click until label cs_check_part06_lap2_b
    pause 0.5
    assert renpy.showing("cs_road_left_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap2_b")
    click until label cs_check_part06_lap2_c
    pause 0.5
    assert renpy.showing("cs_road_right_bend_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap2_c")
    click until label cs_check_part06_lap2_return
    pause 0.5
    assert renpy.showing("cs_road_marked_verge_day")
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_lap2_return")
    assert renpy.music.get_playing() == "sound/music/waltz_of_doubts.ogg"
    click until label cs_check_part06_gate_return
    pause 0.5
    assert cs_road_loop_observations == 2
    assert renpy.showing("bg ext_no_bus")
    assert cs_road_visual_trace == ["approach", "control_created", "lap1_a", "lap1_b", "lap1_c", "lap1_return", "lap2_a", "lap2_b", "lap2_c", "lap2_return", "back_c", "back_b", "back_a"]
    $ cs_qa_capture("cs_part06_trust_gate_return")
    click until label cs_check_part06_olga_arrived
    pause 0.5
    assert renpy.showing("mt") and renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_olga")
    click until label cs_check_part06_olga_left
    pause 0.5
    assert not renpy.showing("mt") and renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part06_trust_olga_left")
    click until label cs_check_part06_semen_left
    pause 0.5
    assert cs_road_notes_written
    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part06_trust_semen_left")
    click until label cs_check_part06_pending
    pause 3.0
    assert cs_day02_part06_complete and not cs_day02_done
    assert cs_friend_se == 2
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_viola) == cs_qa_part06_prior_friends
    assert renpy.showing("cs_darya") and not renpy.showing("mt") and not renpy.showing("cs_semen")
    assert renpy.music.get_playing() is None
    assert renpy.get_screen("cs_day02_road_continue_screen") is not None
    $ cs_qa_capture("cs_part06_trust_end")
    run Jump("cs_qa_road_replay")
    click until run CSQAwaitMenu()
    "Сказать Семёну, что меня действительно тревожит"
    click until label cs_check_part06_pending
    assert cs_friend_se == 2 and cs_se_road_day2_awarded
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part06_trust_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
