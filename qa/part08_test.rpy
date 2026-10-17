# -*- coding: utf-8 -*-
default cs_qa_part08_audit = False
init 45 python:
    def cs_qa_part08_images(event, **kwargs):
        if event != "show_done" or not cs_qa_part08_audit or not cs_part08_live:
            return
        tags = ("cs_darya", "cs_dasha_winter", "cs_dasha_pioneer", "cs_semen", "cs_zhenya", "mz", "un", "mi", "dv", "sl", "us", "mt", "sh", "el", "cs")
        actual = [t for t in tags if renpy.showing(t)]
        if set(actual) != set(cs_part08_cast) or len(actual) > 2:
            raise Exception("Part-8 cast mismatch: %r / %r" % (actual, cs_part08_cast))
        if cs_part08_cg and actual:
            raise Exception("Portraits over guess-who CG")
    config.all_character_callbacks.append(cs_qa_part08_images)

label cs_qa_part08_load:
    $ renpy.load("cs_part07_leave-menu")
    return

label cs_qa_part08_replay:
    hide screen cs_day02_square_continue_screen
    window show
    $ cs_part08_live = True
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    scene bg ext_square_day
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    call cs_day02_zhenya_square_choice
    call cs_day02_59
    jump cs_day02_part09_pending

testcase cs_part07_portrait_height:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    $ _preferences.text_cps = 0
    $ _test.timeout = 50.0
    $ _test.force = True
    run Start("cs_qa_part07_load")
    pause 1.0
    $ cs_qa_global_audit = True
    $ cs_qa_part07_audit = True
    click until label cs_check_part07_fall
    pause 0.5
    $ cs_qa_darya_height = renpy.get_image_bounds("cs_darya")[1]
    click until label cs_check_part07_injury_focus
    pause 0.5
    assert abs(renpy.get_image_bounds("cs_darya")[1] - cs_qa_darya_height) < 2
    $ cs_qa_capture("part07_height_crouch")
    click until label cs_check_part07_standing
    pause 0.5
    assert abs(renpy.get_image_bounds("cs_darya")[1] - cs_qa_darya_height) < 2
    click until label cs_check_part07_treatment
    pause 0.5
    $ cs_qa_darya_clinic_height = renpy.get_image_bounds("cs_darya")[1]
    click until label cs_check_part07_seated
    pause 0.5
    assert abs(renpy.get_image_bounds("cs_darya")[1] - cs_qa_darya_clinic_height) < 2
    $ cs_qa_capture("part07_height_clinic")
    $ renpy.take_screenshot()
    $ renpy.save("part07-height-clinic")
    $ renpy.load("part07-height-clinic")
    pause 0.5
    assert abs(renpy.get_image_bounds("cs_darya")[1] - cs_qa_darya_clinic_height) < 2
    click until run CSQAwaitMenu()
    $ open(config.gamedir + "/mods/chuzaya_smena/qa/part07_portrait_height_pass.txt", "w").write("PASS")
    run Quit(confirm=False)
