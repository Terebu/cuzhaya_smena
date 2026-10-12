# -*- coding: utf-8 -*-
label cs_qa_load_part09_friend:
    $ renpy.load("cs-preserved-part09-meet")
    return
label cs_qa_load_part09_stranger:
    $ renpy.load("cs-preserved-part09-pass")
    return

testcase cs_part10_un0_help:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_part09_stranger")
    pause 0.6
    assert cs_day01_part09_done and not cs_day01_part10_done
    $ cs_friend_un = 0
    run Jump("cs_check_day01_part09_pending")
    click until label cs_check_day01_part10_library
    pause 0.8
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert not renpy.showing("un")
    $ cs_qa_capture("part10_library_un0_help")
    click until label cs_check_day01_part10_choice
    assert cs_met_mz and cs_friend_mz == 0
    "Предложить Жене помощь с книгами"
    click until label cs_check_day01_part10_join
    pause 0.5
    assert cs_friend_un == 0 and cs_met_un == False
    assert cs_friend_mz == 1 and cs_met_mz
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un0_help-middle")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part10_un0_help-middle")
    pause 0.6
    assert cs_friend_mz == 1 and cs_friend_un == 0
    click until label cs_check_day01_part10_pending
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 1 and cs_friend_un == 0
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un0_help-end")
    $ cs_day01_part10_done = False
    $ renpy.load("cs_part10_un0_help-end")
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 1
    $ cs_qa_capture("part10_open_day_un0_help")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/cs_part10_un0_help_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-nine save, Lena state 0, Zhenya help, scores 0/1, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)

testcase cs_part10_un0_search:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_part09_stranger")
    pause 0.6
    assert cs_day01_part09_done and not cs_day01_part10_done
    $ cs_friend_un = 0
    run Jump("cs_check_day01_part09_pending")
    click until label cs_check_day01_part10_library
    pause 0.8
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert not renpy.showing("un")
    $ cs_qa_capture("part10_library_un0_search")
    click until label cs_check_day01_part10_choice
    assert cs_met_mz and cs_friend_mz == 0
    "Не отвлекать Женю от работы"
    click until label cs_check_day01_part10_join
    pause 0.5
    assert cs_friend_un == 0 and cs_met_un == False
    assert cs_friend_mz == 0 and cs_met_mz
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un0_search-middle")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part10_un0_search-middle")
    pause 0.6
    assert cs_friend_mz == 0 and cs_friend_un == 0
    click until label cs_check_day01_part10_pending
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 0 and cs_friend_un == 0
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un0_search-end")
    $ cs_day01_part10_done = False
    $ renpy.load("cs_part10_un0_search-end")
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 0
    $ cs_qa_capture("part10_open_day_un0_search")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/cs_part10_un0_search_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-nine save, Lena state 0, Zhenya search, scores 0/0, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)

testcase cs_part10_un1_help:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_part09_friend")
    pause 0.6
    assert cs_day01_part09_done and not cs_day01_part10_done
    $ cs_friend_un = 1
    run Jump("cs_check_day01_part09_pending")
    click until label cs_check_day01_part10_un_friend
    pause 0.5
    assert renpy.showing("un") and renpy.showing("cs_darya")
    $ cs_qa_capture("part10_lena_friend")
    click until label cs_check_day01_part10_library
    pause 0.8
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert not renpy.showing("un")
    $ cs_qa_capture("part10_library_un1_help")
    click until label cs_check_day01_part10_choice
    assert cs_met_mz and cs_friend_mz == 0
    "Предложить Жене помощь с книгами"
    click until label cs_check_day01_part10_join
    pause 0.5
    assert cs_friend_un == 1 and cs_met_un == True
    assert cs_friend_mz == 1 and cs_met_mz
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un1_help-middle")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part10_un1_help-middle")
    pause 0.6
    assert cs_friend_mz == 1 and cs_friend_un == 1
    click until label cs_check_day01_part10_pending
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 1 and cs_friend_un == 1
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un1_help-end")
    $ cs_day01_part10_done = False
    $ renpy.load("cs_part10_un1_help-end")
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 1
    $ cs_qa_capture("part10_open_day_un1_help")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/cs_part10_un1_help_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-nine save, Lena state 1, Zhenya help, scores 1/1, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)

testcase cs_part10_un1_search:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_part09_friend")
    pause 0.6
    assert cs_day01_part09_done and not cs_day01_part10_done
    $ cs_friend_un = 1
    run Jump("cs_check_day01_part09_pending")
    click until label cs_check_day01_part10_un_friend
    pause 0.5
    assert renpy.showing("un") and renpy.showing("cs_darya")
    $ cs_qa_capture("part10_lena_friend")
    click until label cs_check_day01_part10_library
    pause 0.8
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert not renpy.showing("un")
    $ cs_qa_capture("part10_library_un1_search")
    click until label cs_check_day01_part10_choice
    assert cs_met_mz and cs_friend_mz == 0
    "Не отвлекать Женю от работы"
    click until label cs_check_day01_part10_join
    pause 0.5
    assert cs_friend_un == 1 and cs_met_un == True
    assert cs_friend_mz == 0 and cs_met_mz
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un1_search-middle")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part10_un1_search-middle")
    pause 0.6
    assert cs_friend_mz == 0 and cs_friend_un == 1
    click until label cs_check_day01_part10_pending
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 0 and cs_friend_un == 1
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un1_search-end")
    $ cs_day01_part10_done = False
    $ renpy.load("cs_part10_un1_search-end")
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 0
    $ cs_qa_capture("part10_open_day_un1_search")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/cs_part10_un1_search_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-nine save, Lena state 1, Zhenya search, scores 1/0, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)

testcase cs_part10_un2_search:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_part09_friend")
    pause 0.6
    assert cs_day01_part09_done and not cs_day01_part10_done
    $ cs_friend_un = 0
    run Jump("cs_check_day01_part09_pending")
    click until label cs_check_day01_part10_un_neutral
    pause 0.5
    assert renpy.showing("un")
    $ cs_qa_capture("part10_lena_neutral")
    click until label cs_check_day01_part10_library
    pause 0.8
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert not renpy.showing("un")
    $ cs_qa_capture("part10_library_un2_search")
    click until label cs_check_day01_part10_choice
    assert cs_met_mz and cs_friend_mz == 0
    "Не отвлекать Женю от работы"
    click until label cs_check_day01_part10_join
    pause 0.5
    assert cs_friend_un == 0 and cs_met_un == True
    assert cs_friend_mz == 0 and cs_met_mz
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un2_search-middle")
    $ cs_friend_mz = 99
    $ renpy.load("cs_part10_un2_search-middle")
    pause 0.6
    assert cs_friend_mz == 0 and cs_friend_un == 0
    click until label cs_check_day01_part10_pending
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 0 and cs_friend_un == 0
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("cs_part10_un2_search-end")
    $ cs_day01_part10_done = False
    $ renpy.load("cs_part10_un2_search-end")
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == 0
    $ cs_qa_capture("part10_open_day_un2_search")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/cs_part10_un2_search_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-nine save, Lena state 2, Zhenya search, scores 2/0, both save/load checkpoints and unfinished day.\n")
    run Quit(confirm=False)
