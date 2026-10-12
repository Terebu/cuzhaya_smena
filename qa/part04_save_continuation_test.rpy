# -*- coding: utf-8 -*-
init 30 python:
    def cs_qa_save_trace(message):
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/old_save_trace.txt"),"a") as cs_f:
            cs_f.write(message + "\n")

    def cs_qa_resume_actual_part04():
        cs_qa_save_trace("after_load flags: " + repr((cs_day01_part04_done,cs_day01_part05_done,cs_day01_part06_done)))
        config.after_load_callbacks.remove(cs_qa_resume_actual_part04)
        # The new flags are supplied by Ren'Py defaults when absent in old saves.
        if not cs_day01_part04_done or cs_day01_part05_done:
            raise Exception("Unexpected state in preserved pre-part-5 save")
        renpy.jump("cs_check_day01_part04_pending")

label cs_qa_load_actual_part04:
    $ cs_qa_save_trace("before load")
    $ config.after_load_callbacks.append(cs_qa_resume_actual_part04)
    $ renpy.load("cs-preserved-part04")
    return

testcase cs_part04_save_continuation:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    assert renpy.can_load("cs-preserved-part04")
    run Start("cs_qa_load_actual_part04")
    pause 0.5
    assert cs_day01_part04_done
    assert not cs_day01_part05_done
    assert not cs_day01_part06_done
    assert renpy.showing("bg int_dining_hall_people_day")
    $ cs_qa_capture("actual_part04_save_resumed")
    click until label cs_check_day01_part05_2026
    pause 0.5
    assert renpy.showing("cs_darya")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/actual_part04_save_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: real preserved part-4 save loaded, new default progress flags supplied, former pending label resumed part 5.\n")
    run Quit(confirm=False)
