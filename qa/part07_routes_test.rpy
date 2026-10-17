# -*- coding: utf-8 -*-
testcase cs_part07_leave:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    assert renpy.has_image("cs custom warm_smile medical normal") and renpy.has_image("cs normal stethoscope")
    assert renpy.loadable("sound/sfx/bodyfall_1.ogg")
    run Start("cs_qa_part07_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part07_audit = True
    $ cs_friend_viola = 1
    $ cs_met_mz = True
    $ _history_list = []
    $ cs_qa_part07_prior = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_se)
    assert cs_friend_viola == 1
    click until label cs_check_part07_s47
    pause 1.0
    assert cs_road_loop_observations == 2 and cs_road_notes_written
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part07_leave_continuity")
    click until label cs_check_part07_fall
    pause 0.6
    assert cs_lena_bandage_damaged and cs_lena_elbow_injury_day2 == 2
    assert renpy.showing("cs_darya worried pioneer normal")
    $ cs_qa_capture("cs_part07_leave_fall")
    click until label cs_check_part07_injury_focus
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_leave_injury_focus")
    click until label cs_check_part07_standing
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_leave_standing")
    click until label cs_check_part07_clinic
    pause 0.5
    assert renpy.showing("cs normal stethoscope") and renpy.showing("cs_darya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_part07_leave_original_viola")
    click until label cs_check_part07_treatment
    pause 0.5
    assert renpy.showing("cs custom serious medical normal") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_leave_custom_viola")
    click until label cs_check_part07_seated
    pause 0.5
    assert renpy.showing("cs_darya") and renpy.showing("cs")
    $ cs_qa_capture("cs_part07_leave_seated")
    assert ('Удивительно. Женя, Славя' in u" ".join(x.what for x in _history_list)) == True
    click until label cs_check_part07_bandaged
    pause 0.5
    assert cs_lena_elbow_bandaged and not cs_lena_bandage_damaged and cs_lena_no_sport_day2
    $ cs_qa_capture("cs_part07_leave_bandaged")
    click until run CSQAwaitMenu()
    pause 0.5
    $ cs_qa_capture("cs_part07_leave_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part07_leave-menu")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part07_leave-menu")
    pause 0.5
    assert cs_friend_viola == 1
    "Поблагодарить Виолу и дать ей вернуться к работе"
    click until label cs_check_part07_s52
    pause 0.5
    assert cs_friend_viola == 1
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part07_leave_outside")
    click until label cs_check_part07_s53
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_leave_walk")
    click until label cs_check_part08_s54
    pause 3.0
    assert not cs_day02_done and cs_day02_part07_complete
    assert cs_friend_viola == 1
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_se) == cs_qa_part07_prior
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2 and not cs_lena_bandage_damaged
    assert renpy.showing("cs_darya") and not renpy.showing("cs") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part07_leave_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part07_leave_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part07_talk:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    assert renpy.has_image("cs custom warm_smile medical normal") and renpy.has_image("cs normal stethoscope")
    assert renpy.loadable("sound/sfx/bodyfall_1.ogg")
    run Start("cs_qa_part07_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part07_audit = True
    $ cs_friend_viola = 1
    $ cs_met_mz = True
    $ _history_list = []
    $ cs_qa_part07_prior = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_se)
    assert cs_friend_viola == 1
    click until label cs_check_part07_s47
    pause 1.0
    assert cs_road_loop_observations == 2 and cs_road_notes_written
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part07_talk_continuity")
    click until label cs_check_part07_fall
    pause 0.6
    assert cs_lena_bandage_damaged and cs_lena_elbow_injury_day2 == 2
    assert renpy.showing("cs_darya worried pioneer normal")
    $ cs_qa_capture("cs_part07_talk_fall")
    click until label cs_check_part07_injury_focus
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_injury_focus")
    click until label cs_check_part07_standing
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_standing")
    click until label cs_check_part07_clinic
    pause 0.5
    assert renpy.showing("cs normal stethoscope") and renpy.showing("cs_darya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_part07_talk_original_viola")
    click until label cs_check_part07_treatment
    pause 0.5
    assert renpy.showing("cs custom serious medical normal") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_custom_viola")
    click until label cs_check_part07_seated
    pause 0.5
    assert renpy.showing("cs_darya") and renpy.showing("cs")
    $ cs_qa_capture("cs_part07_talk_seated")
    assert ('Удивительно. Женя, Славя' in u" ".join(x.what for x in _history_list)) == True
    click until label cs_check_part07_bandaged
    pause 0.5
    assert cs_lena_elbow_bandaged and not cs_lena_bandage_damaged and cs_lena_no_sport_day2
    $ cs_qa_capture("cs_part07_talk_bandaged")
    click until run CSQAwaitMenu()
    pause 0.5
    $ cs_qa_capture("cs_part07_talk_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part07_talk-menu")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part07_talk-menu")
    pause 0.5
    assert cs_friend_viola == 1
    "Немного поговорить с Виолой перед уходом"
    click until label cs_check_part07_s52
    pause 0.5
    assert cs_friend_viola == 2
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part07_talk_outside")
    click until label cs_check_part07_s53
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_walk")
    click until label cs_check_part08_s54
    pause 3.0
    assert not cs_day02_done and cs_day02_part07_complete
    assert cs_friend_viola == 2
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_se) == cs_qa_part07_prior
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2 and not cs_lena_bandage_damaged
    assert renpy.showing("cs_darya") and not renpy.showing("cs") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part07_talk_end")
    run Jump("cs_qa_part07_replay")
    click until run CSQAwaitMenu()
    "Немного поговорить с Виолой перед уходом"
    click until label cs_check_part08_s54
    assert cs_friend_viola == 2 and cs_viola_second_day2_awarded
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part07_talk_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part07_talk_neutral:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    assert renpy.has_image("cs custom warm_smile medical normal") and renpy.has_image("cs normal stethoscope")
    assert renpy.loadable("sound/sfx/bodyfall_1.ogg")
    run Start("cs_qa_part07_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part07_audit = True
    $ cs_friend_viola = 0
    $ cs_met_mz = False
    $ _history_list = []
    $ cs_qa_part07_prior = (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_se)
    assert cs_friend_viola == 0
    click until label cs_check_part07_s47
    pause 1.0
    assert cs_road_loop_observations == 2 and cs_road_notes_written
    assert renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part07_talk_neutral_continuity")
    click until label cs_check_part07_fall
    pause 0.6
    assert cs_lena_bandage_damaged and cs_lena_elbow_injury_day2 == 2
    assert renpy.showing("cs_darya worried pioneer normal")
    $ cs_qa_capture("cs_part07_talk_neutral_fall")
    click until label cs_check_part07_injury_focus
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_neutral_injury_focus")
    click until label cs_check_part07_standing
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_neutral_standing")
    click until label cs_check_part07_clinic
    pause 0.5
    assert renpy.showing("cs normal stethoscope") and renpy.showing("cs_darya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("cs_part07_talk_neutral_original_viola")
    click until label cs_check_part07_treatment
    pause 0.5
    assert renpy.showing("cs custom serious medical normal") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_neutral_custom_viola")
    click until label cs_check_part07_seated
    pause 0.5
    assert renpy.showing("cs_darya") and renpy.showing("cs")
    $ cs_qa_capture("cs_part07_talk_neutral_seated")
    assert ('Удивительно. Женя, Славя' in u" ".join(x.what for x in _history_list)) == False
    click until label cs_check_part07_bandaged
    pause 0.5
    assert cs_lena_elbow_bandaged and not cs_lena_bandage_damaged and cs_lena_no_sport_day2
    $ cs_qa_capture("cs_part07_talk_neutral_bandaged")
    click until run CSQAwaitMenu()
    pause 0.5
    $ cs_qa_capture("cs_part07_talk_neutral_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part07_talk_neutral-menu")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part07_talk_neutral-menu")
    pause 0.5
    assert cs_friend_viola == 0
    "Немного поговорить с Виолой перед уходом"
    click until label cs_check_part07_s52
    pause 0.5
    assert cs_friend_viola == 1
    assert renpy.showing("cs_darya") and not renpy.showing("cs")
    $ cs_qa_capture("cs_part07_talk_neutral_outside")
    click until label cs_check_part07_s53
    pause 0.5
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part07_talk_neutral_walk")
    click until label cs_check_part08_s54
    pause 3.0
    assert not cs_day02_done and cs_day02_part07_complete
    assert cs_friend_viola == 1
    assert (cs_friend_un, cs_friend_mz, cs_friend_sl, cs_friend_mi, cs_friend_se) == cs_qa_part07_prior
    assert cs_lena_elbow_bandaged and cs_lena_no_sport_day2 and not cs_lena_bandage_damaged
    assert renpy.showing("cs_darya") and not renpy.showing("cs") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part07_talk_neutral_end")
    run Jump("cs_qa_part07_replay")
    click until run CSQAwaitMenu()
    "Немного поговорить с Виолой перед уходом"
    click until label cs_check_part08_s54
    assert cs_friend_viola == 1 and cs_viola_second_day2_awarded
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part07_talk_neutral_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_morning_viola_cg_0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    run Start("cs_qa_morning_help_load")
    pause 1.0
    $ cs_qa_global_audit = True
    click until run CSQAwaitMenu()
    "Поблагодарить Виолу и не задерживаться"
    click until label cs_check_part04_s32
    pause 0.5
    assert cs_friend_viola == 0
    assert not renpy.showing("cs_cg_lena_darya_help_viola_day")
    assert not renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_morning_viola_cg_0_exit")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_morning_viola_cg_0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_morning_viola_cg_1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    run Start("cs_qa_morning_help_load")
    pause 1.0
    $ cs_qa_global_audit = True
    click until run CSQAwaitMenu()
    "Предложить Виоле помощь с материалами"
    click until label cs_check_cg_help_viola
    pause 1.0
    assert renpy.showing("cs_cg_lena_darya_help_viola_day")
    assert not renpy.showing("cs") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_morning_viola_cg_1_help")
    $ renpy.take_screenshot()
    $ renpy.save("cs_morning_viola_cg_1-cg")
    $ cs_friend_viola = 99
    $ renpy.load("cs_morning_viola_cg_1-cg")
    pause 0.5
    assert cs_friend_viola == 1
    click until label cs_check_part04_s32
    pause 0.5
    assert cs_friend_viola == 1
    assert not renpy.showing("cs_cg_lena_darya_help_viola_day")
    assert not renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_morning_viola_cg_1_exit")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_morning_viola_cg_1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
