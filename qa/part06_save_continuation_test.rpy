# -*- coding: utf-8 -*-
init 30 python:
    def cs_qa_resume_actual_part06():
        config.after_load_callbacks.remove(cs_qa_resume_actual_part06)
        if not cs_day01_part06_done or cs_day01_part07_done:
            raise Exception("Unexpected state in preserved part-six save")
        renpy.jump("cs_check_day01_part06_pending")

label cs_qa_load_actual_part06:
    $ config.after_load_callbacks.append(cs_qa_resume_actual_part06)
    $ renpy.load("cs-preserved-part06")
    return

testcase cs_part06_save_continuation:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    assert renpy.can_load("cs-preserved-part06")
    run Start("cs_qa_load_actual_part06")
    pause 0.6
    assert cs_day01_part06_done and not cs_day01_part07_done
    assert renpy.showing("cs_house_lena_darya_int_day")
    assert renpy.showing("dv") and renpy.showing("us") and renpy.showing("cs_darya")
    assert renpy.music.get_playing(channel="music") == cs_day_music_play
    $ cs_qa_capture("actual_part06_save_resumed")
    click until label cs_check_day01_part07_engineers
    pause 0.6
    assert renpy.showing("sh") and renpy.showing("el")
    click until label cs_check_day01_part08_pending
    pause 0.6
    assert cs_day01_part07_done
    assert renpy.get_screen("cs_day01_pending") is not None
    $ cs_qa_capture("actual_part06_save_finished_part07")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/actual_part06_save_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: preserved real part-six save loads with new defaults and resumes through all nine part-seven scenes.\n")
    run Quit(confirm=False)
