# -*- coding: utf-8 -*-
init 30 python:
    def cs_qa_capture(name):
        import os
        dest = os.path.join(config.gamedir, "mods", "chuzaya_smena", "qa", "screenshots")
        if not os.path.isdir(dest):
            os.makedirs(dest)
        if not renpy.screenshot(os.path.join(dest, name + ".png")):
            raise Exception("Could not save screenshot: " + name)

label cs_qa_new_day02_load:
    $ renpy.load("cs_part10_un1_help-end")
    return

testcase cs_new_day02:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 40.0
    assert renpy.has_image("bg ext_playground_day")
    assert renpy.has_image("bg ext_camp_entrance_day")
    assert renpy.has_image("bg ext_house_of_mt_day")
    assert renpy.loadable("sound/sfx/close_door_1.ogg")
    assert renpy.loadable("sound/ambiences/forest_day.ogg")
    run Start("cs_qa_new_day02_load")
    pause 1.5
    run Jump("cs_day01_part11")
    click until label cs_check_day_title
    pause 0.4
    assert renpy.get_screen("cs_day_title_screen") is not None
    assert cs_day01_done
    $ cs_qa_capture("new_day02_title")
    click until label cs_check_new_d2_s01
    pause 1.0
    assert not renpy.showing("cs_darya")
    assert renpy.music.get_playing() is None
    $ cs_qa_capture("new_day02_early_room")
    click until label cs_check_new_d2_sport
    pause 1.0
    $ cs_qa_capture("new_day02_sports_ground")
    click until label cs_check_new_d2_olga
    pause 1.0
    assert renpy.showing("mt") and not renpy.showing("cs_darya")
    $ cs_qa_capture("new_day02_olga")
    click until label cs_check_new_d2_gate
    pause 1.0
    assert not renpy.showing("mt") and not renpy.showing("cs_darya")
    $ cs_qa_capture("new_day02_empty_gate")
    click until label cs_check_new_d2_s06
    pause 1.0
    $ cs_qa_capture("new_day02_semen_house")
    click until label cs_check_new_d2_semen
    pause 1.0
    assert renpy.showing("cs_semen") and not renpy.showing("cs_darya")
    $ cs_qa_capture("new_day02_semen")
    click until label cs_check_new_d2_s07
    pause 1.0
    assert not renpy.showing("cs_semen")
    click until label cs_check_new_d2_wash
    pause 1.0
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("new_day02_washstand")
    click until label cs_check_new_d2_breakfast
    click until label cs_check_breakfast_table
    pause 1.0
    assert renpy.showing("cs_darya") and renpy.showing("cs_semen")
    $ cs_qa_capture("new_day02_breakfast")
    $ renpy.take_screenshot()
    $ renpy.save("new-day02-breakfast")
    $ cs_friend_un = 99
    $ renpy.load("new-day02-breakfast")
    pause 1.0
    assert cs_friend_un == 1 and cs_friend_mz == 1
    click until label cs_check_part02_menu
    "Поблагодарить Мику и пойти на линейку"
    click until label cs_check_part02_pending
    pause 1.0
    assert not cs_day02_done
    assert not renpy.showing("cs_darya") and not renpy.showing("cs_semen")
    assert renpy.get_screen("cs_day02_continue_screen") is not None
    $ cs_qa_capture("new_day02_part02_end")
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/new_day02_pass.txt", "w").write("PASS")
    run Quit(confirm=False)

label cs_qa_first_day_card:
    call cs_day_title(1)
    jump cs_day02

testcase cs_new_day01_card:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    run Start("cs_qa_first_day_card")
    click until label cs_check_day_title
    pause 0.4
    $ cs_qa_capture("new_day01_title")
    run Quit(confirm=False)
