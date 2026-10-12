from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
output='''# -*- coding: utf-8 -*-
label cs_qa_load_part09_friend:
    $ renpy.load("cs-preserved-part09-meet")
    return
label cs_qa_load_part09_stranger:
    $ renpy.load("cs-preserved-part09-pass")
    return
'''
for un,choice in [(0,'help'),(0,'search'),(1,'help'),(1,'search'),(2,'search')]:
    score=0 if un==2 else un
    met=un>0
    name=f'cs_part10_un{un}_{choice}';button='Предложить Жене помощь с книгами' if choice=='help' else 'Не отвлекать Женю от работы';point=int(choice=='help')
    event='''    click until label cs_check_day01_part10_un_friend
    pause 0.5
    assert renpy.showing("un") and renpy.showing("cs_darya")
    $ cs_qa_capture("part10_lena_friend")
''' if un==1 else '''    click until label cs_check_day01_part10_un_neutral
    pause 0.5
    assert renpy.showing("un")
    $ cs_qa_capture("part10_lena_neutral")
''' if un==2 else ''
    output+=f'''
testcase {name}:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_load_part09_{'friend' if un else 'stranger'}")
    pause 0.6
    assert cs_day01_part09_done and not cs_day01_part10_done
    $ cs_friend_un = {score}
    run Jump("cs_check_day01_part09_pending")
{event}    click until label cs_check_day01_part10_library
    pause 0.8
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert not renpy.showing("un")
    $ cs_qa_capture("part10_library_un{un}_{choice}")
    click until label cs_check_day01_part10_choice
    assert cs_met_mz and cs_friend_mz == 0
    "{button}"
    click until label cs_check_day01_part10_join
    pause 0.5
    assert cs_friend_un == {score} and cs_met_un == {met}
    assert cs_friend_mz == {point} and cs_met_mz
    $ renpy.take_screenshot()
    $ renpy.save("{name}-middle")
    $ cs_friend_mz = 99
    $ renpy.load("{name}-middle")
    pause 0.6
    assert cs_friend_mz == {point} and cs_friend_un == {score}
    click until label cs_check_day01_part10_pending
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == {point} and cs_friend_un == {score}
    assert renpy.showing("mz") and renpy.showing("cs_darya")
    assert renpy.get_screen("cs_day01_pending") is not None
    $ renpy.take_screenshot()
    $ renpy.save("{name}-end")
    $ cs_day01_part10_done = False
    $ renpy.load("{name}-end")
    pause 0.6
    assert cs_day01_part10_done and cs_friend_mz == {point}
    $ cs_qa_capture("part10_open_day_un{un}_{choice}")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/{name}_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: old part-nine save, Lena state {un}, Zhenya {choice}, scores {score}/{point}, both save/load checkpoints and unfinished day.\\n")
    run Quit(confirm=False)
'''
(ROOT/'qa/day01_part10_test.rpy').write_text(output,encoding='utf8')
