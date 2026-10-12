# -*- coding: utf-8 -*-
label cs_qa_part09_visibility:
    $ cs_active = True
    $ cs_darya_known = True
    call cs_day01_46
    call cs_day01_47
    call cs_day01_49
    call cs_day01_50
    label cs_check_visibility_done:
    $ renpy.pause(hard=True)
    jump cs_check_visibility_done

testcase cs_part09_visibility:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 30.0
    run Start("cs_qa_part09_visibility")
    click until label cs_check_day01_part09_choice
    "Остановиться и познакомиться"
    click until label cs_check_day01_un_farewell
    pause 0.5
    assert renpy.showing("un")
    assert renpy.get_image_bounds("un")[1] < config.screen_height
    assert renpy.showing("cs_darya")
    $ cs_qa_capture("part09_lena_farewell_visible")
    # Emulate the old inherited bottom anchor and prove load repairs only the display.
    $ renpy.show("un smile pioneer", at_list=[Transform(xalign=0.03,yanchor=0.0,ypos=1.0)], zorder=10)
    $ renpy.take_screenshot()
    $ renpy.save("cs-un-old-anchor")
    $ renpy.load("cs-un-old-anchor")
    pause 0.6
    assert renpy.get_image_bounds("un")[1] < config.screen_height
    assert cs_friend_un == 1
    $ cs_qa_capture("part09_lena_old_anchor_loaded")
    python:
        import os,json
        cs_debug={"attributes":renpy.get_attributes("un"),"bounds":renpy.get_image_bounds("un"),"transforms":[repr(t) for t in renpy.get_at_list("un")]}
        cs_debug["states"]=[{k:repr(getattr(t.state,k,None)) for k in ("xpos","ypos","xanchor","yanchor","alpha","zoom","xzoom","yzoom")} for t in renpy.get_at_list("un")]
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/un_display_debug.json"),"w") as cs_f:json.dump(cs_debug,cs_f,indent=2)
    click until label cs_check_day01_part09_merge
    pause 0.5
    assert not renpy.showing("un") and not renpy.showing("cs_darya")
    $ cs_qa_capture("part09_description_without_darya")
    click until label cs_check_day01_part09_returns
    pause 0.5
    assert renpy.showing("cs_darya")
    click until label cs_check_visibility_done
    assert not renpy.showing("cs_darya")
    $ cs_qa_capture("part09_final_thoughts_without_darya")
    python:
        import os
        with open(os.path.join(config.gamedir,"mods/chuzaya_smena/qa/part09_visibility_pass.txt"),"w") as cs_f:
            cs_f.write("PASS: original Lena visible through goodbye; Darya hidden for descriptions and concluding thoughts, restored for conversation.\n")
    run Quit(confirm=False)
