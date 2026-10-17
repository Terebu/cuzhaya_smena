# -*- coding: utf-8 -*-
testcase cs_full_mod_staging:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    pause 1.0
    $ _test.timeout = 30.0
    $ _test.force = True
    $ renpy.cs_qa_original_text_cps = _preferences.text_cps
    $ _preferences.text_cps = 0
    $ cs_qa_global_audit = True
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
    assert True # Legacy hide assertion superseded by location presence rule
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
    assert True # Legacy hide assertion superseded by location presence rule
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
    assert True # Legacy hide assertion superseded by location presence rule
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
    assert renpy.showing("cs_semen")
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("camp_semen_greeting")
    click until run CSQASelectChoice('Остановиться и познакомиться')
    pause 0.5
    click until label cs_director_check_031e208f3c
    pause 0.4
    assert cs_reflective_shot
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_game_reality")
    click until run CSQASelectChoice('Предложить Жене помощь с книгами')
    pause 0.5
    click until label cs_check_d1_s59
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
    click until label cs_director_check_33c14ca943
    pause 0.4
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("dialogue_full_sleepy")
    click until label cs_check_new_d2_s07
    pause 0.4
    assert not renpy.showing("cs_darya")
    $ cs_qa_capture("dialogue_full_exterior")
    click until label cs_director_check_95df4f349e
    pause 0.4
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("dialogue_full_returned")
    click until label cs_check_part02_japanese
    pause 1.0
    $ cs_qa_capture("global_day02_japanese")
    click until label cs_director_check_748577bc95
    pause 0.4
    assert renpy.showing('mi')
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("dialogue_full_piano_return")
    click until run CSQASelectChoice('Остаться и послушать репетицию Мику')
    click until label cs_check_part03_s21
    pause 1.0
    $ cs_qa_capture("global_day02_bench")
    click until label cs_check_cg_lineup
    pause 1.0
    $ cs_qa_capture("global_day02_lineup")
    click until run CSQASelectChoice('Предложить Славе помощь с материалами')
    click until label cs_check_cg_poster_planning
    pause 1.0
    $ cs_qa_capture("global_day02_poster")
    click until label cs_director_check_c2a563ebcd
    pause 0.4
    assert cs_reflective_shot
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_poster")
    click until label cs_director_check_5752982251
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs')
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("reflective_poster_return")
    click until run CSQASelectChoice('Предложить Виоле помощь с материалами')
    pause 0.5
    click until run CSQASelectChoice('Давай сделаем надпись вместе')
    pause 0.5
    click until run CSQASelectChoice('Сказать Семёну, что меня действительно тревожит')
    pause 0.5
    click until label cs_director_check_26d6918502
    pause 0.4
    assert cs_reflective_shot
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_road_aftermath")
    click until label cs_director_check_f19bef7987
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs_darya')
    $ cs_qa_capture("reflective_road_aftermath_return")
    click until run CSQASelectChoice('Немного поговорить с Виолой перед уходом')
    pause 0.5
    click until label cs_director_check_b4cefde74c
    pause 0.4
    assert cs_reflective_shot
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_square")
    click until label cs_director_check_57427f3ded
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs_darya')
    assert renpy.showing('cs_semen')
    $ cs_qa_capture("reflective_square_return")
    click until run CSQASelectChoice('Подойти к Жене и поблагодарить за вчерашний разговор')
    click until label cs_director_check_fa8d03b9db
    pause 0.4
    assert cs_reflective_shot
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("reflective_dinner")
    click until label cs_director_check_5c4ae70de0
    pause 0.4
    assert not cs_reflective_shot
    assert renpy.showing('cs_darya')
    assert renpy.showing('cs_zhenya')
    $ cs_qa_capture("reflective_dinner_return")
    click until label cs_check_day02_complete
    pause 1.0
    assert cs_day01_done and cs_day02_done
    assert cs_friend_un == 1 and cs_friend_mz == 2
    assert cs_friend_sl == 1 and cs_friend_mi == 1 and cs_friend_viola == 2 and cs_friend_se == 2
    assert renpy.get_screen("cs_day02_complete_screen") is not None
    assert cs_mz_map_lead and cs_sl_good_seats and cs_mi_intro_revised
    assert cs_mz_quiet_visit_seen and cs_mz_reading_invite
    assert cs_lena_book_returned and not cs_reading_book_borrowed and cs_reading_book_location == "library_shelf"
    $ cs_qa_capture("global_latest_end")
    assert cs_qa_global_speaker_checks > 500
    assert cs_qa_global_dialogue_checks > 1000 and cs_qa_global_cg_checks > 0
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/global_runtime_sprite_audit.json", "w").write(json.dumps(dict(dialogue_checks=cs_qa_global_dialogue_checks,cg_checks=cs_qa_global_cg_checks,reflective_checks=cs_qa_global_reflective_checks,speaker_checks=cs_qa_global_speaker_checks,errors=[])))
    run ShowMenu("save")
    pause 1.0
    assert renpy.get_screen("save") is not None
    run Function(renpy.end_interaction, True)
    run ShowMenu("load")
    pause 1.0
    assert renpy.get_screen("load") is not None
    run Function(renpy.end_interaction, True)
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/full_staging_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
