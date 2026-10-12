# -*- coding: utf-8 -*-
# Opt-in engine-native regression test. Does not run during normal gameplay.
# From the game root: "Everlasting Summer.exe" . test cs_vertical_slice
init 30 python:
    def cs_qa_capture(name):
        import os
        dest = os.path.join(config.gamedir, "mods", "chuzaya_smena", "qa", "screenshots")
        if not os.path.isdir(dest):
            os.makedirs(dest)
        # The shipped interpreter uses optimization: never put side effects in
        # Python assert (it is removed). Native testcase assert nodes do run.
        if not renpy.screenshot(os.path.join(dest, name + ".png")):
            raise Exception("Could not save QA screenshot: " + name)

testcase cs_vertical_slice:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    pause 1.0
    $ _test.timeout = 30.0
    $ renpy.cs_qa_original_text_cps = _preferences.text_cps
    $ _preferences.text_cps = 0
    run ShowMenu("mods")
    pause 1.0
    assert "chuzhaya_smena_start" in mods
    $ cs_qa_capture("00_mods_menu")
    "Чужая смена"
    click until label cs_check_room
    pause 2.0
    assert _history
    $ cs_qa_capture("01_room")
    click until label cs_check_battery7
    pause 1.0
    assert renpy.get_screen("cs_phone") is not None
    $ cs_qa_capture("02_battery7")
    click until label cs_check_neutral
    pause 1.0
    assert not renpy.showing("cs_dasha")
    assert renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("03_dasha_city")
    click until label cs_check_profile
    pause 1.0
    assert renpy.get_screen("cs_phone") is not None
    $ cs_qa_capture("04_profile")
    assert len(_history_list) > 50
    run ShowMenu("text_history")
    pause 1.0
    assert renpy.get_screen("text_history_screen") is not None
    $ cs_qa_capture("04_history")
    run Function(renpy.end_interaction, True)
    click until label cs_check_instagram_oni
    pause 0.5
    assert renpy.get_screen("cs_instagram_post") is not None
    assert not renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("04_instagram_oni")
    click until label cs_check_instagram_studio
    pause 0.5
    $ cs_qa_capture("04_instagram_studio")
    click until label cs_check_instagram_crush
    pause 0.5
    $ cs_qa_capture("04_instagram_crush")
    click until label cs_check_instagram_evening
    pause 0.5
    $ cs_qa_capture("04_instagram_evening")
    click until label cs_check_instagram_daily
    assert not renpy.showing("cs_dasha_winter")
    pause 0.5
    $ cs_qa_capture("04_instagram_daily")
    click until label cs_check_battery5
    assert renpy.get_screen("cs_instagram_post") is None
    pause 0.5
    $ cs_qa_capture("04_battery5")
    click until label cs_check_battery2
    pause 0.5
    $ cs_qa_capture("04_battery2")
    click until label cs_check_phone_off
    pause 0.5
    $ cs_qa_capture("04_phone_off")
    click until label cs_check_winter
    pause 1.0
    assert renpy.showing("cs_bus_winter")
    $ cs_qa_capture("05_winter")
    click until label cs_check_introduced
    pause 1.0
    assert cs_darya_known
    $ cs_qa_capture("05_introduced")
    run ShowMenu("save")
    pause 1.0
    assert renpy.get_screen("save") is not None
    $ cs_qa_capture("05_save_screen")
    run Function(renpy.end_interaction, True)
    run ShowMenu("load")
    pause 1.0
    assert renpy.get_screen("load") is not None
    $ cs_qa_capture("05_load_screen")
    run Function(renpy.end_interaction, True)
    $ renpy.take_screenshot()
    $ renpy.save("cs-qa-roundtrip", extra_info=u"Чужая смена: проверка сохранения")
    assert renpy.can_load("cs-qa-roundtrip")
    $ cs_darya_known = False
    $ renpy.load("cs-qa-roundtrip")
    pause 1.0
    assert cs_darya_known
    $ cs_qa_capture("05_loaded")
    click until label cs_check_sleep_winter
    pause 1.0
    assert not renpy.showing("cs_dasha")
    $ cs_qa_capture("06_sleep_winter")
    click until label cs_check_cg_winter
    pause 1.0
    assert renpy.showing("cs_sleep_winter")
    assert not renpy.showing("cs_dasha")
    $ cs_qa_capture("06_cg_winter")
    click until label cs_check_summer
    pause 1.0
    assert renpy.showing("bg int_bus")
    $ cs_qa_capture("07_summer")
    click until label cs_check_sleep_summer
    pause 1.0
    assert renpy.showing("cs_sleep_summer")
    assert not renpy.showing("cs_dasha")
    $ cs_qa_capture("07_sleep_summer")
    click until label cs_check_gate
    pause 5.0
    assert renpy.showing("bg ext_camp_entrance_day")
    assert persistent.timeofday == "day"
    $ cs_qa_capture("07_gate")
    click until label cs_check_day01_bus
    pause 1.0
    assert persistent.timeofday == "day"
    $ cs_qa_capture("day01_01_bus")
    click until label cs_check_day01_outside
    pause 1.0
    assert not renpy.showing("cs_windshield")
    $ cs_qa_capture("day01_02_outside")
    click until label cs_check_day01_reflection
    pause 1.0
    $ cs_qa_capture("day01_03_reflection")
    click until label cs_check_day01_phone
    pause 1.0
    assert renpy.get_screen("cs_phone") is not None
    $ cs_qa_capture("day01_03_phone")
    click until label cs_check_day01_silence
    pause 3.5
    assert renpy.music.get_playing(channel="music") is None
    $ cs_qa_capture("day01_04_silence")
    click until label cs_check_day01_slavya
    pause 1.0
    assert renpy.showing("sl smile pioneer")
    $ cs_qa_capture("day01_04_slavya")
    click until label cs_check_day01_part02_gate
    pause 1.0
    assert renpy.showing("cs_dasha_winter")
    assert renpy.music.get_playing(channel="music") == cs_day_music_friends
    $ cs_qa_capture("day01_part02_gate")
    click until label cs_check_day01_walk
    pause 1.0
    assert renpy.showing("cs_camp_path_day")
    $ cs_qa_capture("day01_part02_path")
    click until label cs_check_day01_trio
    pause 1.0
    assert renpy.showing("mt normal pioneer far")
    assert renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("day01_part02_trio")
    click until label cs_check_day01_name
    pause 1.0
    $ cs_qa_capture("day01_part02_name")
    click until label cs_check_day01_tension
    pause 1.0
    $ cs_qa_capture("day01_part02_tension")
    click until label cs_check_camp_olga_angry
    pause 0.6
    assert renpy.showing("mt angry pioneer")
    assert not renpy.showing("cs_dasha_winter")
    $ cs_qa_capture("camp_olga_firm")
    click until label cs_check_camp_olga_smile
    pause 0.6
    assert renpy.showing("mt smile pioneer")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("camp_olga_agrees")
    click until label cs_check_camp_cameo_reactions
    pause 0.6
    assert renpy.showing("dv grin pioneer far")
    assert renpy.showing("us grin pioneer far")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("camp_cameo_reactions")
    click until label cs_check_camp_semen_awkward
    pause 0.6
    assert renpy.showing("cs_semen awkward pioneer far")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("camp_semen_greeting")
    click until label cs_check_day01_part09_choice
    "Остановиться и познакомиться"
    click until label cs_check_day01_part10_choice
    "Предложить Жене помощь с книгами"
    click until label cs_check_day01_part10_pending
    pause 1.0
    assert cs_active
    assert cs_slavya_known
    assert cs_day01_part02_done
    assert cs_day01_part03_done
    assert cs_day01_part04_done
    assert cs_day01_part05_done
    assert cs_day01_part06_done
    assert cs_day01_part07_done
    assert cs_day01_part08_done
    assert cs_day01_part09_done
    assert cs_day01_part10_done
    assert cs_friend_mz == 1 and cs_met_mz
    assert cs_friend_un == 1 and cs_met_un
    assert renpy.get_screen("cs_day01_pending") is not None
    assert renpy.get_screen("main_menu") is None
    $ cs_qa_capture("day01_05_pending")
    $ _preferences.text_cps = renpy.cs_qa_original_text_cps
    python:
        import os
        with open(os.path.join(config.gamedir, "mods/chuzaya_smena/qa/runtime_pass.txt"), "w") as cs_f:
            cs_f.write("PASS: prologue and day 1 parts 1-10 at 1280x720; history/save/load; music silence; actors; both friendship choices; day remains open.\n")
    run Quit(confirm=False)
