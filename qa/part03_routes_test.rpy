# -*- coding: utf-8 -*-
testcase cs_part03_m0_s0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert renpy.loadable(cs_miku_piano_track)
    run Start("cs_qa_part02_load")
    pause 1.0
    run Jump("cs_qa_part03_path")
    click until label cs_check_d2_piano_darya
    pause 1.0
    assert renpy.showing("cs_cg_darya_piano_day")
    $ cs_qa_capture("cs_part03_m0_s0_darya")
    click until run CSQAwaitMenu()
    "Поблагодарить Мику и пойти на линейку"
    click until label cs_check_cg_lineup
    pause 1.0
    assert cs_friend_mi == 0
    assert renpy.showing("cs_cg_morning_lineup_day")
    assert not renpy.showing("mt") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s0_lineup")
    click until run CSQAwaitMenu()
    pause 1.0
    assert not renpy.showing("mt") and not renpy.showing("mi")
    $ cs_qa_capture("cs_part03_m0_s0_slavya_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part03_m0_s0-menu")
    $ cs_friend_sl = 99
    $ renpy.load("cs_part03_m0_s0-menu")
    pause 1.0
    assert cs_friend_sl == 0
    "Поблагодарить Славю и заняться объявлением"
    click until label cs_check_part03_s25
    pause 1.0
    assert cs_friend_sl == 0
    assert not renpy.showing("sl")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s0_working_group")
    click until label cs_check_cg_poster_planning
    pause 1.0
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s0_poster")
    click until label cs_check_part03_clubs
    pause 0.05
    assert renpy.showing("bg int_clubs_male_day")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s0_clubs")
    click until label cs_check_part04_s26
    pause 1.0
    assert not cs_day02_done and cs_friend_mi == 0 and cs_friend_sl == 0
    $ cs_qa_capture("cs_part03_m0_s0_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part03_m0_s0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part03_m0_s1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert renpy.loadable(cs_miku_piano_track)
    run Start("cs_qa_part02_load")
    pause 1.0
    run Jump("cs_qa_part03_path")
    click until label cs_check_d2_piano_darya
    pause 1.0
    assert renpy.showing("cs_cg_darya_piano_day")
    $ cs_qa_capture("cs_part03_m0_s1_darya")
    click until run CSQAwaitMenu()
    "Поблагодарить Мику и пойти на линейку"
    click until label cs_check_cg_lineup
    pause 1.0
    assert cs_friend_mi == 0
    assert renpy.showing("cs_cg_morning_lineup_day")
    assert not renpy.showing("mt") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s1_lineup")
    click until run CSQAwaitMenu()
    pause 1.0
    assert not renpy.showing("mt") and not renpy.showing("mi")
    $ cs_qa_capture("cs_part03_m0_s1_slavya_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part03_m0_s1-menu")
    $ cs_friend_sl = 99
    $ renpy.load("cs_part03_m0_s1-menu")
    pause 1.0
    assert cs_friend_sl == 0
    "Предложить Славе помощь с материалами"
    click until label cs_check_part03_storage
    pause 1.0
    assert cs_friend_sl == 1 and cs_helped_sl_day2
    assert renpy.showing("cs_storage_int_day")
    $ cs_qa_capture("cs_part03_m0_s1_storage")
    click until label cs_check_part03_s25
    pause 1.0
    assert cs_friend_sl == 1
    assert not renpy.showing("sl")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s1_working_group")
    click until label cs_check_cg_poster_planning
    pause 1.0
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s1_poster")
    click until label cs_check_part03_clubs
    pause 0.05
    assert renpy.showing("bg int_clubs_male_day")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m0_s1_clubs")
    click until label cs_check_part04_s26
    pause 1.0
    assert not cs_day02_done and cs_friend_mi == 0 and cs_friend_sl == 1
    $ cs_qa_capture("cs_part03_m0_s1_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part03_m0_s1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part03_m1_s0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert renpy.loadable(cs_miku_piano_track)
    run Start("cs_qa_part02_load")
    pause 1.0
    run Jump("cs_qa_part03_path")
    click until label cs_check_d2_piano_darya
    pause 1.0
    assert renpy.showing("cs_cg_darya_piano_day")
    $ cs_qa_capture("cs_part03_m1_s0_darya")
    click until run CSQAwaitMenu()
    "Остаться и послушать репетицию Мику"
    click until label cs_check_d2_piano_miku
    pause 1.0
    assert renpy.music.get_playing(channel="cs_piano") == "sound/music/miku_song_voice.ogg"
    $ cs_qa_capture("cs_part03_m1_s0_miku_song")
    click until label cs_check_part03_s21
    pause 1.0
    assert cs_friend_mi == 1
    assert not renpy.showing("mi")
    $ cs_qa_capture("cs_part03_m1_s0_bench")
    click until label cs_check_cg_lineup
    pause 1.0
    assert cs_friend_mi == 1
    assert renpy.showing("cs_cg_morning_lineup_day")
    assert not renpy.showing("mt") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s0_lineup")
    click until run CSQAwaitMenu()
    pause 1.0
    assert not renpy.showing("mt") and not renpy.showing("mi")
    $ cs_qa_capture("cs_part03_m1_s0_slavya_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part03_m1_s0-menu")
    $ cs_friend_sl = 99
    $ renpy.load("cs_part03_m1_s0-menu")
    pause 1.0
    assert cs_friend_sl == 0
    "Поблагодарить Славю и заняться объявлением"
    click until label cs_check_part03_s25
    pause 1.0
    assert cs_friend_sl == 0
    assert not renpy.showing("sl")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s0_working_group")
    click until label cs_check_cg_poster_planning
    pause 1.0
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s0_poster")
    click until label cs_check_part03_clubs
    pause 0.05
    assert renpy.showing("bg int_clubs_male_day")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s0_clubs")
    click until label cs_check_part04_s26
    pause 1.0
    assert not cs_day02_done and cs_friend_mi == 1 and cs_friend_sl == 0
    $ cs_qa_capture("cs_part03_m1_s0_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part03_m1_s0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

testcase cs_part03_m1_s1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    assert renpy.loadable(cs_miku_piano_track)
    run Start("cs_qa_part02_load")
    pause 1.0
    run Jump("cs_qa_part03_path")
    click until label cs_check_d2_piano_darya
    pause 1.0
    assert renpy.showing("cs_cg_darya_piano_day")
    $ cs_qa_capture("cs_part03_m1_s1_darya")
    click until run CSQAwaitMenu()
    "Остаться и послушать репетицию Мику"
    click until label cs_check_d2_piano_miku
    pause 1.0
    assert renpy.music.get_playing(channel="cs_piano") == "sound/music/miku_song_voice.ogg"
    $ cs_qa_capture("cs_part03_m1_s1_miku_song")
    click until label cs_check_part03_s21
    pause 1.0
    assert cs_friend_mi == 1
    assert not renpy.showing("mi")
    $ cs_qa_capture("cs_part03_m1_s1_bench")
    click until label cs_check_cg_lineup
    pause 1.0
    assert cs_friend_mi == 1
    assert renpy.showing("cs_cg_morning_lineup_day")
    assert not renpy.showing("mt") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s1_lineup")
    click until run CSQAwaitMenu()
    pause 1.0
    assert not renpy.showing("mt") and not renpy.showing("mi")
    $ cs_qa_capture("cs_part03_m1_s1_slavya_menu")
    $ renpy.take_screenshot()
    $ renpy.save("cs_part03_m1_s1-menu")
    $ cs_friend_sl = 99
    $ renpy.load("cs_part03_m1_s1-menu")
    pause 1.0
    assert cs_friend_sl == 0
    "Предложить Славе помощь с материалами"
    click until label cs_check_part03_storage
    pause 1.0
    assert cs_friend_sl == 1 and cs_helped_sl_day2
    assert renpy.showing("cs_storage_int_day")
    $ cs_qa_capture("cs_part03_m1_s1_storage")
    click until label cs_check_part03_s25
    pause 1.0
    assert cs_friend_sl == 1
    assert not renpy.showing("sl")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s1_working_group")
    click until label cs_check_cg_poster_planning
    pause 1.0
    assert renpy.showing("cs_cg_poster_planning_day")
    assert not renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s1_poster")
    click until label cs_check_part03_clubs
    pause 0.05
    assert renpy.showing("bg int_clubs_male_day")
    assert renpy.showing("cs_semen") and renpy.showing("cs_darya")
    $ cs_qa_capture("cs_part03_m1_s1_clubs")
    click until label cs_check_part04_s26
    pause 1.0
    assert not cs_day02_done and cs_friend_mi == 1 and cs_friend_sl == 1
    $ cs_qa_capture("cs_part03_m1_s1_end")
    run Jump("cs_qa_sl_replay")
    click until run CSQAwaitMenu()
    "Предложить Славе помощь с материалами"
    click until label cs_check_part04_s26
    pause 1.0
    assert cs_friend_sl == 1
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_part03_m1_s1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
