# -*- coding: utf-8 -*-
label cs_qa_day01_phone_focus:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_active = True
    $ cs_darya_known = True
    $ cs_olga_seen = True
    scene bg int_house_of_mt_day
    call cs_day01_12
    return

testcase cs_day01_phone_focus:
    pause 1.0
    $ renpy.set_physical_size((1280,720))
    run Start("cs_qa_day01_phone_focus")
    click until label cs_check_day01_part03_phone_off
    pause 1.0
    assert renpy.showing("mt normal pioneer")
    assert renpy.get_screen("cs_phone").scope["mode"] == "off"
    assert renpy.get_screen("cs_phone").scope["phone_x"] == 820
    $ cs_qa_capture("day01_part03_phone_off")
    run Quit(confirm=False)
