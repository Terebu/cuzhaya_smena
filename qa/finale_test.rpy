# -*- coding: utf-8 -*-
default cs_qa_finale_audit = False
default cs_qa_finale_scores = ()
init 50 python:
    def cs_qa_finale_image_audit(event, **kwargs):
        if event != "show_done" or not cs_qa_finale_audit:
            return
        if (cs_friend_mz, cs_friend_se, cs_friend_sl, cs_friend_mi, cs_friend_viola, cs_friend_un) != cs_qa_finale_scores:
            raise Exception("Finale changed friendship")
    config.all_character_callbacks.append(cs_qa_finale_image_audit)

label cs_qa_finale_common:
    $ cs_day02_seating_done = False
    $ cs_day02_concert_done = False
    $ cs_day02_done = False
    $ cs_lena_book_returned = False
    $ cs_reading_book_id = "zhenya_second_copy"
    $ cs_reading_book_location = "cabin_table"
    $ cs_reading_book_borrowed = True
    $ cs_mz_quiet_visit_seen = True
    $ cs_lena_elbow_bandaged = True
    $ cs_lena_elbow_injury_day2 = 2
    $ cs_lena_no_sport_day2 = True
    $ cs_un_name_known = True
    $ cs_met_mz = True
    $ cs_active = True
    $ cs_qa_finale_scores = (cs_friend_mz, cs_friend_se, cs_friend_sl, cs_friend_mi, cs_friend_viola, cs_friend_un)
    $ cs_qa_finale_audit = True
    $ cs_qa_global_audit = True
    jump cs_day02_part10_start

label cs_qa_finale_0:
    $ cs_friend_mz = 0
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_friend_un = 0
    $ cs_mi_intro_revised = False
    $ cs_sl_good_seats = False
    $ cs_mz_map_lead = False
    $ cs_helped_sl_day2 = False
    jump cs_qa_finale_common

testcase cs_finale_0:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    $ _test.force = True
    run Start("cs_qa_finale_0")
    click until label cs_check_finale_67
    pause 1.0
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("finale_0_library")
    click until label cs_check_finale_returned_a
    assert cs_lena_book_returned and not cs_reading_book_borrowed and cs_reading_book_location == "library_shelf"
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_0-return")
    $ cs_lena_book_returned = False
    $ renpy.load("cs_finale_0-return")
    pause 0.6
    assert cs_lena_book_returned and not cs_reading_book_borrowed
    click until label cs_check_finale_concert_wide
    pause 1.5
    assert renpy.music.get_playing(channel="cs_piano") == "sound/music/miku_song_voice.ogg"
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("finale_0_concert_wide")
    click until label cs_check_finale_concert_close
    pause 1.5
    $ cs_qa_capture("finale_0_concert_close")
    click until label cs_check_finale_concert_done
    pause 1.0
    assert cs_day02_concert_done
    $ cs_qa_capture("finale_0_concert_end")
    click until label cs_check_finale_73
    pause 1.0
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("finale_0_night")
    click until label cs_check_day02_complete
    pause 1.0
    assert cs_day02_done and cs_day02_part10_done
    assert cs_lena_book_returned and cs_reading_book_location == "library_shelf"
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2 == 2 and cs_lena_no_sport_day2
    assert cs_viola_spare_bandage == False and cs_un_concert_sketch_seen == False
    assert (cs_friend_mz, cs_friend_se, cs_friend_sl, cs_friend_mi, cs_friend_viola, cs_friend_un) == cs_qa_finale_scores
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_0-end")
    $ cs_day02_done = False
    $ renpy.load("cs_finale_0-end")
    pause 0.6
    assert cs_day02_done and cs_lena_book_returned
    $ cs_qa_capture("finale_0_complete")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_finale_0_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_finale_1:
    $ cs_friend_mz = 1
    $ cs_friend_se = 0
    $ cs_friend_sl = 0
    $ cs_friend_mi = 0
    $ cs_friend_viola = 0
    $ cs_friend_un = 0
    $ cs_mi_intro_revised = False
    $ cs_sl_good_seats = False
    $ cs_mz_map_lead = True
    $ cs_helped_sl_day2 = False
    jump cs_qa_finale_common

testcase cs_finale_1:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    $ _test.force = True
    run Start("cs_qa_finale_1")
    click until label cs_check_finale_67
    pause 1.0
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("finale_1_library")
    click until label cs_check_finale_returned_b
    assert cs_lena_book_returned and not cs_reading_book_borrowed and cs_reading_book_location == "library_shelf"
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_1-return")
    $ cs_lena_book_returned = False
    $ renpy.load("cs_finale_1-return")
    pause 0.6
    assert cs_lena_book_returned and not cs_reading_book_borrowed
    click until label cs_check_finale_concert_wide
    pause 1.5
    assert renpy.music.get_playing(channel="cs_piano") == "sound/music/miku_song_voice.ogg"
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("finale_1_concert_wide")
    click until label cs_check_finale_concert_close
    pause 1.5
    $ cs_qa_capture("finale_1_concert_close")
    click until label cs_check_finale_concert_done
    pause 1.0
    assert cs_day02_concert_done
    $ cs_qa_capture("finale_1_concert_end")
    click until label cs_check_finale_73
    pause 1.0
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("finale_1_night")
    click until label cs_check_day02_complete
    pause 1.0
    assert cs_day02_done and cs_day02_part10_done
    assert cs_lena_book_returned and cs_reading_book_location == "library_shelf"
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2 == 2 and cs_lena_no_sport_day2
    assert cs_viola_spare_bandage == False and cs_un_concert_sketch_seen == False
    assert (cs_friend_mz, cs_friend_se, cs_friend_sl, cs_friend_mi, cs_friend_viola, cs_friend_un) == cs_qa_finale_scores
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_1-end")
    $ cs_day02_done = False
    $ renpy.load("cs_finale_1-end")
    pause 0.6
    assert cs_day02_done and cs_lena_book_returned
    $ cs_qa_capture("finale_1_complete")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_finale_1_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_finale_2:
    $ cs_friend_mz = 2
    $ cs_friend_se = 2
    $ cs_friend_sl = 1
    $ cs_friend_mi = 1
    $ cs_friend_viola = 2
    $ cs_friend_un = 2
    $ cs_mi_intro_revised = True
    $ cs_sl_good_seats = True
    $ cs_mz_map_lead = True
    $ cs_helped_sl_day2 = True
    jump cs_qa_finale_common

testcase cs_finale_2:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    $ _test.force = True
    run Start("cs_qa_finale_2")
    click until label cs_check_finale_67
    pause 1.0
    assert renpy.showing("cs_zhenya") and renpy.showing("cs_darya")
    $ cs_qa_capture("finale_2_library")
    click until label cs_check_finale_returned_c
    assert cs_lena_book_returned and not cs_reading_book_borrowed and cs_reading_book_location == "library_shelf"
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_2-return")
    $ cs_lena_book_returned = False
    $ renpy.load("cs_finale_2-return")
    pause 0.6
    assert cs_lena_book_returned and not cs_reading_book_borrowed
    click until label cs_check_finale_concert_wide
    pause 1.5
    assert renpy.music.get_playing(channel="cs_piano") == "sound/music/miku_song_voice.ogg"
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ cs_qa_capture("finale_2_concert_wide")
    click until label cs_check_finale_concert_close
    pause 1.5
    $ cs_qa_capture("finale_2_concert_close")
    click until label cs_check_finale_concert_done
    pause 1.0
    assert cs_day02_concert_done
    $ cs_qa_capture("finale_2_concert_end")
    click until label cs_check_finale_73
    pause 1.0
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("finale_2_night")
    click until label cs_check_day02_complete
    pause 1.0
    assert cs_day02_done and cs_day02_part10_done
    assert cs_lena_book_returned and cs_reading_book_location == "library_shelf"
    assert cs_lena_elbow_bandaged and cs_lena_elbow_injury_day2 == 2 and cs_lena_no_sport_day2
    assert cs_viola_spare_bandage == True and cs_un_concert_sketch_seen == True
    assert (cs_friend_mz, cs_friend_se, cs_friend_sl, cs_friend_mi, cs_friend_viola, cs_friend_un) == cs_qa_finale_scores
    assert not any(renpy.showing(t) for t in cs_presence_tags)
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_2-end")
    $ cs_day02_done = False
    $ renpy.load("cs_finale_2-end")
    pause 0.6
    assert cs_day02_done and cs_lena_book_returned
    $ cs_qa_capture("finale_2_complete")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_finale_2_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_finale_map_false:
    $ cs_friend_mz = 2
    $ cs_mz_map_lead = False
    scene bg int_library_day
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    call cs_day02_68c
    label cs_check_finale_map_false_done:
    pause
    return

testcase cs_finale_map_false:
    pause 1.0
    $ _preferences.text_cps = 0
    run Start("cs_qa_finale_map_false")
    click until label cs_check_finale_map_false_done
    assert not cs_mz_map_lead and cs_friend_mz == 2 and cs_lena_book_returned
    $ renpy.take_screenshot()
    $ renpy.save("cs_finale_no_map")
    $ cs_lena_book_returned = False
    $ renpy.load("cs_finale_no_map")
    pause 0.6
    assert cs_lena_book_returned and not cs_mz_map_lead
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_finale_map_false_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_finale_legacy_load:
    $ renpy.load("cs_part09_zero-end")
    return

testcase cs_finale_legacy:
    pause 1.0
    $ _preferences.text_cps = 0
    $ _test.force = True
    run Start("cs_qa_finale_legacy_load")
    click until label cs_check_finale_concert_wide
    assert not cs_reading_book_borrowed and not cs_lena_book_returned
    assert not cs_mz_quiet_visit_seen
    click until label cs_check_day02_complete
    assert cs_day02_done and cs_day02_part10_done
    assert not cs_lena_book_returned and not cs_reading_book_borrowed
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/cs_finale_legacy_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
