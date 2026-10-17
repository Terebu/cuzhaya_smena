# -*- coding: utf-8 -*-
testcase cs_part08_pass:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part08_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part08_audit = True
    $ cs_friend_se = 0
    $ cs_qa_part08_prior = (cs_friend_mz, cs_friend_se, cs_friend_viola, cs_friend_un, cs_friend_mi, cs_friend_sl)
    click until run CSQAwaitMenu()
    "Поблагодарить Виолу и дать ей вернуться к работе"
    click until label cs_check_part08_s54
    pause 0.6
    assert cs_road_loop_observations == 2 and cs_road_notes_written
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2 and not cs_lena_bandage_damaged
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part08_pass_continuity")
    click until label cs_check_part08_square
    pause 0.5
    assert renpy.showing("bg ext_square_day")
    $ cs_qa_capture("cs_part08_pass_square")
    click until label cs_check_part08_guess_cg
    pause 0.8
    assert renpy.showing("cs_cg_lena_semen_guess_who_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part08_pass_cg")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part08_pass-cg")
    $ cs_friend_se = 99
    $ renpy.load("cs_part08_pass-cg")
    pause 0.5
    assert cs_friend_se == 0
    assert renpy.showing("cs_cg_lena_semen_guess_who_day")
    click until label cs_check_part08_turned
    pause 0.8
    assert renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert not renpy.showing("cs_cg_lena_semen_guess_who_day")
    $ cs_qa_capture("cs_part08_pass_turned")
    $ cs_qa_semen_upright_bounds = renpy.get_image_bounds("cs_semen")
    click until label cs_check_part08_darya_returns
    pause 0.6
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part08_pass_two")
    click until label cs_check_part08_seated
    pause 0.5
    $ cs_qa_capture("cs_part08_pass_seated")
    assert abs(renpy.get_image_bounds("cs_semen")[1] - cs_qa_semen_upright_bounds[1]) < 2
    click until label cs_check_part08_trust
    pause 0.5
    assert renpy.showing("cs_semen neutral pioneer normal")
    $ cs_qa_capture("cs_part08_pass_trust")
    click until run CSQAwaitMenu()
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("mz")
    $ cs_qa_capture("cs_part08_pass_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part08_pass-menu")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part08_pass-menu")
    pause 0.5
    assert cs_friend_mz == cs_qa_part08_prior[0]
    "Не отвлекать Женю от её дел"
    click until label cs_check_part08_s59
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("mz")
    assert cs_friend_mz == cs_qa_part08_prior[0] + 0
    click until label cs_check_part08_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part08_pass_semen_left")
    click until label cs_check_part08_pending
    pause 3.0
    assert cs_day02_part08_complete and not cs_day02_done
    assert renpy.get_screen("cs_day02_square_continue_screen") is not None
    assert renpy.music.get_playing() is None
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert (cs_friend_se, cs_friend_viola, cs_friend_un, cs_friend_mi, cs_friend_sl) == cs_qa_part08_prior[1:]
    assert cs_friend_mz == cs_qa_part08_prior[0] + 0
    $ cs_qa_capture("cs_part08_pass_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part08_pass-end")
    $ cs_lena_elbow_bandaged = False
    $ renpy.load("cs_part08_pass-end")
    pause 0.5
    assert cs_lena_elbow_bandaged
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part08_pass_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part08_talk:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part08_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part08_audit = True
    $ cs_friend_se = 2
    $ cs_qa_part08_prior = (cs_friend_mz, cs_friend_se, cs_friend_viola, cs_friend_un, cs_friend_mi, cs_friend_sl)
    click until run CSQAwaitMenu()
    "Поблагодарить Виолу и дать ей вернуться к работе"
    click until label cs_check_part08_s54
    pause 0.6
    assert cs_road_loop_observations == 2 and cs_road_notes_written
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2 and not cs_lena_bandage_damaged
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part08_talk_continuity")
    click until label cs_check_part08_square
    pause 0.5
    assert renpy.showing("bg ext_square_day")
    $ cs_qa_capture("cs_part08_talk_square")
    click until label cs_check_part08_guess_cg
    pause 0.8
    assert renpy.showing("cs_cg_lena_semen_guess_who_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part08_talk_cg")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part08_talk-cg")
    $ cs_friend_se = 99
    $ renpy.load("cs_part08_talk-cg")
    pause 0.5
    assert cs_friend_se == 2
    assert renpy.showing("cs_cg_lena_semen_guess_who_day")
    click until label cs_check_part08_turned
    pause 0.8
    assert renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert not renpy.showing("cs_cg_lena_semen_guess_who_day")
    $ cs_qa_capture("cs_part08_talk_turned")
    $ cs_qa_semen_upright_bounds = renpy.get_image_bounds("cs_semen")
    click until label cs_check_part08_darya_returns
    pause 0.6
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part08_talk_two")
    click until label cs_check_part08_seated
    pause 0.5
    $ cs_qa_capture("cs_part08_talk_seated")
    assert abs(renpy.get_image_bounds("cs_semen")[1] - cs_qa_semen_upright_bounds[1]) < 2
    click until label cs_check_part08_trust
    pause 0.5
    assert renpy.showing("cs_semen relaxed pioneer normal")
    $ cs_qa_capture("cs_part08_talk_trust")
    click until run CSQAwaitMenu()
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("mz")
    $ cs_qa_capture("cs_part08_talk_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part08_talk-menu")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part08_talk-menu")
    pause 0.5
    assert cs_friend_mz == cs_qa_part08_prior[0]
    "Подойти к Жене и поблагодарить за вчерашний разговор"
    click until label cs_check_part08_zhenya
    pause 0.5
    assert renpy.showing("cs_zhenya") and not renpy.showing("mz")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part08_talk_zhenya")
    click until label cs_check_part08_zhenya_left
    pause 0.5
    assert not renpy.showing("cs_zhenya")
    click until label cs_check_part08_rejoined
    pause 0.5
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part08_talk_rejoined")
    click until label cs_check_part08_s59
    pause 0.5
    assert not renpy.showing("cs_zhenya") and not renpy.showing("mz")
    assert cs_friend_mz == cs_qa_part08_prior[0] + 1
    click until label cs_check_part08_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part08_talk_semen_left")
    click until label cs_check_part08_pending
    pause 3.0
    assert cs_day02_part08_complete and not cs_day02_done
    assert renpy.get_screen("cs_day02_square_continue_screen") is not None
    assert renpy.music.get_playing() is None
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2
    assert (cs_friend_se, cs_friend_viola, cs_friend_un, cs_friend_mi, cs_friend_sl) == cs_qa_part08_prior[1:]
    assert cs_friend_mz == cs_qa_part08_prior[0] + 1
    $ cs_qa_capture("cs_part08_talk_end")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part08_talk-end")
    $ cs_lena_elbow_bandaged = False
    $ renpy.load("cs_part08_talk-end")
    pause 0.5
    assert cs_lena_elbow_bandaged
    run Jump("cs_qa_part08_replay")
    click until run CSQAwaitMenu()
    "Подойти к Жене и поблагодарить за вчерашний разговор"
    click until label cs_check_part08_pending
    assert cs_friend_mz == cs_qa_part08_prior[0] + 1 and cs_mz_square_day2_awarded
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part08_talk_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
