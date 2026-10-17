# -*- coding: utf-8 -*-
testcase cs_part04_leave:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg int_aidpost_day", "bg ext_aidpost_day", "cs normal stethoscope", "cs smile stethoscope", "sh serious pioneer", "el grin pioneer", "cs_cg_poster_planning_day"))
    assert __import__("__builtin__").all(renpy.loadable("sound/" + x + ".ogg") for x in ("music/smooth_machine", "music/my_daily_life", "music/just_think", "music/get_to_know_me_better", "ambiences/medstation_inside_day", "sfx/knock_door7_polite"))
    run Start("cs_qa_part04_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part04_audit = True
    assert cs_friend_viola == 0 and not cs_met_viola
    click until run CSQAwaitMenu()
    "Предложить Славе помощь с материалами"
    click until label cs_check_part03_clubs
    pause 0.05
    assert renpy.showing("bg int_clubs_male_day")
    $ cs_qa_capture("cs_part04_leave_boundary")
    click until label cs_check_part04_s26
    pause 3.0
    assert renpy.showing("sh") and renpy.showing("el")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing() == "sound/music/smooth_machine.ogg"
    $ cs_qa_capture("cs_part04_leave_engineers")
    click until label cs_check_part04_s27
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert not renpy.showing("sh") and not renpy.showing("el")
    $ cs_qa_capture("cs_part04_leave_outside")
    click until label cs_check_part04_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part04_leave_semen_left")
    click until label cs_check_part04_s29
    pause 0.5
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part04_leave_viola")
    click until label cs_check_part04_poster_observation
    pause 0.5
    assert cs_met_viola
    assert not renpy.showing("cs") and not renpy.showing("cs_darya")
    assert renpy.showing("bg int_aidpost_day")
    $ cs_qa_capture("cs_part04_leave_anatomy")
    click until label cs_check_part04_viola_restored
    pause 0.5
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part04_leave_restored")
    click until run CSQAwaitMenu()
    pause 0.5
    assert cs_friend_viola == 0 and cs_met_viola
    $ cs_qa_capture("cs_part04_leave_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part04_leave-choice")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part04_leave-choice")
    pause 0.5
    assert cs_friend_viola == 0
    "Поблагодарить Виолу и не задерживаться"
    click until label cs_check_part04_s32
    pause 0.5
    assert cs_friend_viola == 0 and cs_helped_viola_day2 == False
    assert not renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part04_leave_merged")
    click until label cs_check_part04_s33
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert not renpy.showing("cs")
    $ cs_qa_capture("cs_part04_leave_returned")
    click until label cs_check_part04_poster_work
    pause 0.5
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part04_leave_poster_work")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part04_leave-poster")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part04_leave-poster")
    pause 0.5
    assert cs_friend_viola == 0 and renpy.showing("cs_cg_poster_planning_day")
    click until label cs_check_part05_s34
    pause 0.5
    assert not cs_day02_done and cs_day02_part04_complete
    assert cs_friend_mi == 1 and cs_friend_sl == 1
    assert cs_friend_viola == 0
    assert renpy.showing("cs_cg_poster_planning_day")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    assert renpy.showing("cs_cg_poster_planning_day")
    $ cs_qa_capture("cs_part04_leave_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part04_leave_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part04_help:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert __import__("__builtin__").all(renpy.has_image(x) for x in ("bg int_aidpost_day", "bg ext_aidpost_day", "cs normal stethoscope", "cs smile stethoscope", "sh serious pioneer", "el grin pioneer", "cs_cg_poster_planning_day"))
    assert __import__("__builtin__").all(renpy.loadable("sound/" + x + ".ogg") for x in ("music/smooth_machine", "music/my_daily_life", "music/just_think", "music/get_to_know_me_better", "ambiences/medstation_inside_day", "sfx/knock_door7_polite"))
    run Start("cs_qa_part04_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part04_audit = True
    assert cs_friend_viola == 0 and not cs_met_viola
    click until run CSQAwaitMenu()
    "Предложить Славе помощь с материалами"
    click until label cs_check_part03_clubs
    pause 0.05
    assert renpy.showing("bg int_clubs_male_day")
    $ cs_qa_capture("cs_part04_help_boundary")
    click until label cs_check_part04_s26
    pause 3.0
    assert renpy.showing("sh") and renpy.showing("el")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    assert renpy.music.get_playing() == "sound/music/smooth_machine.ogg"
    $ cs_qa_capture("cs_part04_help_engineers")
    click until label cs_check_part04_s27
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert not renpy.showing("sh") and not renpy.showing("el")
    $ cs_qa_capture("cs_part04_help_outside")
    click until label cs_check_part04_semen_left
    pause 0.5
    assert not renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part04_help_semen_left")
    click until label cs_check_part04_s29
    pause 0.5
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    assert not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part04_help_viola")
    click until label cs_check_part04_poster_observation
    pause 0.5
    assert cs_met_viola
    assert not renpy.showing("cs") and not renpy.showing("cs_darya")
    assert renpy.showing("bg int_aidpost_day")
    $ cs_qa_capture("cs_part04_help_anatomy")
    click until label cs_check_part04_viola_restored
    pause 0.5
    assert renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part04_help_restored")
    click until run CSQAwaitMenu()
    pause 0.5
    assert cs_friend_viola == 0 and cs_met_viola
    $ cs_qa_capture("cs_part04_help_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part04_help-choice")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part04_help-choice")
    pause 0.5
    assert cs_friend_viola == 0
    "Предложить Виоле помощь с материалами"
    click until label cs_check_part04_s32
    pause 0.5
    assert cs_friend_viola == 1 and cs_helped_viola_day2 == True
    assert not renpy.showing("cs") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part04_help_merged")
    click until label cs_check_part04_s33
    pause 0.5
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert not renpy.showing("cs")
    $ cs_qa_capture("cs_part04_help_returned")
    click until label cs_check_part04_poster_work
    pause 0.5
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    $ cs_qa_capture("cs_part04_help_poster_work")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part04_help-poster")
    $ cs_friend_viola = 99
    $ renpy.load("cs_part04_help-poster")
    pause 0.5
    assert cs_friend_viola == 1 and renpy.showing("cs_cg_poster_planning_day")
    click until label cs_check_part05_s34
    pause 0.5
    assert not cs_day02_done and cs_day02_part04_complete
    assert cs_friend_mi == 1 and cs_friend_sl == 1
    assert cs_friend_viola == 1
    assert renpy.showing("cs_cg_poster_planning_day")
    assert renpy.music.get_playing() == "sound/music/my_daily_life.ogg"
    assert renpy.showing("cs_cg_poster_planning_day")
    $ cs_qa_capture("cs_part04_help_end")
    run Jump("cs_qa_viola_replay")
    click until run CSQAwaitMenu()
    "Предложить Виоле помощь с материалами"
    click until label cs_check_part05_s34
    assert cs_friend_viola == 1 and cs_viola_day2_awarded
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part04_help_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
