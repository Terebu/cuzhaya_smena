# -*- coding: utf-8 -*-
label cs_qa_load_actual_part08:
    $ renpy.load("cs-preserved-part08")
    return

testcase cs_day01_part09_meet:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    assert renpy.can_load("cs-preserved-part08")
    run Start("cs_qa_load_actual_part08")
    pause 0.6
    assert cs_day01_part08_done and not cs_day01_part09_done
    run Jump("cs_check_day01_part08_pending")
    pause 0.8
    assert renpy.showing("cs_camp_path_sunset") and renpy.showing("cs_darya")
    assert persistent.sprite_time == "sunset"
    # Finish the saved-screen dissolve before judging the new composition.
    click
    click
    pause 0.8
    $ cs_qa_capture("part09_centered_start_meet")
    click until label cs_check_day01_part09_choice
    pause 0.8
    $ cs_qa_capture("part09_menu_meet")
    "Остановиться и познакомиться"
    click until label cs_check_day01_part09_trio
    pause 1.5
    assert renpy.showing("un") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert cs_un_name_known
    $ cs_qa_capture("part09_three_people")
    click until label cs_check_day01_part09_merge
    pause 0.8
    assert cs_friend_un == 1 and cs_met_un == True
    assert cs_part09_choice == "meet"
    assert not renpy.showing("un") and not renpy.showing("cs_semen")
    $ renpy.take_screenshot()
    $ renpy.save("cs-part09-branch-meet")
    $ cs_friend_un = 99
    $ renpy.load("cs-part09-branch-meet")
    pause 0.6
    assert cs_friend_un == 1 and cs_met_un == True
    click until label cs_check_day01_part09_introspection
    pause 0.8
    assert not renpy.showing("cs_darya")
    assert renpy.showing("cs_camp_path_sunset")
    $ cs_qa_capture("part09_thoughts_meet")
    click until label cs_check_day01_part09_returns
    pause 0.8
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part09_back_to_darya_meet")
    click until label cs_check_day01_part09_pending
    pause 0.8
    assert cs_day01_part09_done
    assert cs_friend_un == 1 and cs_met_un == True
    assert renpy.get_screen("cs_day01_pending") is not None
    assert renpy.get_screen("main_menu") is None
    $ renpy.take_screenshot()
    $ renpy.save("cs-part09-end-meet")
    $ cs_friend_un = 99
    $ cs_day01_part09_done = False
    $ renpy.load("cs-part09-end-meet")
    pause 0.6
    assert cs_day01_part09_done and cs_friend_un == 1
    assert renpy.music.get_playing(channel="music") == cs_day_music_everyday
    $ cs_qa_capture("part09_open_day_meet")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/part09_meet_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-eight save, meet branch, 1 point, merge, introspection, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)

testcase cs_day01_part09_pass:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    assert renpy.can_load("cs-preserved-part08")
    run Start("cs_qa_load_actual_part08")
    pause 0.6
    assert cs_day01_part08_done and not cs_day01_part09_done
    run Jump("cs_check_day01_part08_pending")
    pause 0.8
    assert renpy.showing("cs_camp_path_sunset") and renpy.showing("cs_darya")
    assert persistent.sprite_time == "sunset"
    # Finish the saved-screen dissolve before judging the new composition.
    click
    click
    pause 0.8
    $ cs_qa_capture("part09_centered_start_pass")
    click until label cs_check_day01_part09_choice
    pause 0.8
    $ cs_qa_capture("part09_menu_pass")
    "Извиниться и пройти дальше"
    click until label cs_check_day01_part09_merge
    pause 0.8
    assert cs_friend_un == 0 and cs_met_un == False
    assert cs_part09_choice == "pass"
    assert not renpy.showing("un") and not renpy.showing("cs_semen")
    $ renpy.take_screenshot()
    $ renpy.save("cs-part09-branch-pass")
    $ cs_friend_un = 99
    $ renpy.load("cs-part09-branch-pass")
    pause 0.6
    assert cs_friend_un == 0 and cs_met_un == False
    click until label cs_check_day01_part09_introspection
    pause 0.8
    assert not renpy.showing("cs_darya")
    assert renpy.showing("cs_camp_path_sunset")
    $ cs_qa_capture("part09_thoughts_pass")
    click until label cs_check_day01_part09_returns
    pause 0.8
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part09_back_to_darya_pass")
    click until label cs_check_day01_part09_pending
    pause 0.8
    assert cs_day01_part09_done
    assert cs_friend_un == 0 and cs_met_un == False
    assert renpy.get_screen("cs_day01_pending") is not None
    assert renpy.get_screen("main_menu") is None
    $ renpy.take_screenshot()
    $ renpy.save("cs-part09-end-pass")
    $ cs_friend_un = 99
    $ cs_day01_part09_done = False
    $ renpy.load("cs-part09-end-pass")
    pause 0.6
    assert cs_day01_part09_done and cs_friend_un == 0
    assert renpy.music.get_playing(channel="music") == cs_day_music_everyday
    $ cs_qa_capture("part09_open_day_pass")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/part09_pass_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-eight save, pass branch, 0 point, merge, introspection, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)
