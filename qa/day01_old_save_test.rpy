# -*- coding: utf-8 -*-
# Uses a preserved real save made before part 2 was implemented.
testcase cs_day01_old_save:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    assert renpy.can_load("cs-old-part01")
    $ renpy.load("cs-old-part01")
    pause 1.0
    assert not cs_day01_part02_done
    $ cs_qa_capture("day01_old_save_loaded")
    run Jump("cs_day01_continuation")
    click until label cs_check_day01_part08_pending
    pause 1.0
    assert cs_day01_part02_done
    assert cs_day01_part03_done
    assert cs_olga_seen
    assert renpy.get_screen("cs_day01_pending") is not None
    $ cs_qa_capture("day01_old_save_continued")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/day01_old_save_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: real pre-part-2 save loaded and continued through scenes 7-20.\n")
    run Quit(confirm=False)
