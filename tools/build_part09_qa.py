"""Generate independent native tests for both choices and real saved continuation."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
helper='''# -*- coding: utf-8 -*-
label cs_qa_load_actual_part08:
    $ renpy.load("cs-preserved-part08")
    return
'''
for branch,option,points in [('meet','Остановиться и познакомиться',1),('pass','Извиниться и пройти дальше',0)]:
    extra='''    click until label cs_check_day01_part09_trio
    pause 1.5
    assert renpy.showing("un") and renpy.showing("cs_semen") and renpy.showing("cs_darya")
    assert cs_un_name_known
    $ cs_qa_capture("part09_three_people")
''' if points else ''
    helper+=f'''
testcase cs_day01_part09_{branch}:
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
    $ cs_qa_capture("part09_centered_start_{branch}")
    click until label cs_check_day01_part09_choice
    pause 0.8
    $ cs_qa_capture("part09_menu_{branch}")
    "{option}"
{extra}    click until label cs_check_day01_part09_merge
    pause 0.8
    assert cs_friend_un == {points} and cs_met_un == {bool(points)}
    assert cs_part09_choice == "{branch}"
    assert not renpy.showing("un") and not renpy.showing("cs_semen")
    $ renpy.take_screenshot()
    $ renpy.save("cs-part09-branch-{branch}")
    $ cs_friend_un = 99
    $ renpy.load("cs-part09-branch-{branch}")
    pause 0.6
    assert cs_friend_un == {points} and cs_met_un == {bool(points)}
    click until label cs_check_day01_part09_introspection
    pause 0.8
    assert not renpy.showing("cs_darya")
    assert renpy.showing("cs_camp_path_sunset")
    $ cs_qa_capture("part09_thoughts_{branch}")
    click until label cs_check_day01_part09_returns
    pause 0.8
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part09_back_to_darya_{branch}")
    click until label cs_check_day01_part09_pending
    pause 0.8
    assert cs_day01_part09_done
    assert cs_friend_un == {points} and cs_met_un == {bool(points)}
    assert renpy.get_screen("cs_day01_pending") is not None
    assert renpy.get_screen("main_menu") is None
    $ renpy.take_screenshot()
    $ renpy.save("cs-part09-end-{branch}")
    $ cs_friend_un = 99
    $ cs_day01_part09_done = False
    $ renpy.load("cs-part09-end-{branch}")
    pause 0.6
    assert cs_day01_part09_done and cs_friend_un == {points}
    assert renpy.music.get_playing(channel="music") == cs_day_music_everyday
    $ cs_qa_capture("part09_open_day_{branch}")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/part09_{branch}_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-eight save, {branch} branch, {points} point, merge, introspection, both save/load checkpoints and unfinished day.\\n")
    run Quit(confirm=False)
'''
(ROOT/'qa/day01_part09_test.rpy').write_text(helper,encoding='utf8')
