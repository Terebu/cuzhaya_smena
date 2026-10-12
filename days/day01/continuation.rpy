# -*- coding: utf-8 -*-
default cs_day01_part05_done = False
default cs_day01_part06_done = False
default cs_day01_part07_done = False
default cs_day01_part08_done = False
default cs_day01_part09_done = False

label cs_day01_part05:
    hide screen cs_day01_pending
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day01_21
    call cs_day01_22
    call cs_day01_23
    call cs_day01_24
    $ cs_day01_part05_done = True
    jump cs_day01_part06

label cs_day01_part06:
    hide screen cs_day01_pending
    # Continue the same table and music into the end of lunch, without a reset.
    call cs_day01_25
    call cs_day01_26
    call cs_day01_27
    call cs_day01_28
    call cs_day01_29
    call cs_day01_30
    $ cs_day01_part06_done = True
    jump cs_day01_part07_pending

label cs_day01_part07_pending:
    jump cs_day01_part07

# Preserve the label stored by saves made at the previous development stop.
label cs_check_day01_part06_pending:
    jump cs_day01_part07

label cs_day01_part07:
    hide screen cs_day01_pending
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day01_31
    call cs_day01_32
    call cs_day01_33
    call cs_day01_34
    call cs_day01_35
    call cs_day01_36
    call cs_day01_37
    call cs_day01_38
    call cs_day01_39
    $ cs_day01_part07_done = True
    jump cs_day01_part08_pending

label cs_day01_part08_pending:
    jump cs_day01_part08

label cs_check_day01_part07_pending:
    jump cs_day01_part08

label cs_day01_part08:
    hide screen cs_day01_pending
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day01_40
    call cs_day01_41
    call cs_day01_42
    call cs_day01_43
    call cs_day01_44
    call cs_day01_45
    $ cs_day01_part08_done = True
    jump cs_day01_part09_pending

label cs_day01_part09_pending:
    jump cs_day01_part09

label cs_check_day01_part08_pending:
    jump cs_day01_part09

label cs_day01_part09:
    if cs_day01_part09_done:
        jump cs_day01_part10_pending
    hide screen cs_day01_pending
    window show dissolve
    call cs_day01_46
    call cs_day01_47
    call cs_day01_49
    call cs_day01_50
    call cs_day01_51
    $ cs_day01_part09_done = True
    jump cs_day01_part10_pending

label cs_day01_part10_pending:
    jump cs_day01_part10

label cs_check_day01_part09_pending:
    jump cs_day01_part10

label cs_day01_part10:
    if cs_day01_part10_done:
        jump cs_day01_part11_pending
    hide screen cs_day01_pending
    window show dissolve
    call cs_day01_dinner_bridge
    call cs_day01_52
    call cs_day01_53
    call cs_day01_54
    call cs_day01_55
    call cs_day01_56
    call cs_day01_57
    call cs_day01_58
    $ cs_day01_part10_done = True
    jump cs_day01_part11_pending

label cs_day01_part11_pending:
    hide screen cs_phone
    window hide dissolve
    show screen cs_day01_pending
    label cs_check_day01_part10_pending:
    $ renpy.checkpoint()
    $ renpy.pause(hard=True)
    jump cs_check_day01_part10_pending
