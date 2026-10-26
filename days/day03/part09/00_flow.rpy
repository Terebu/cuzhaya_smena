# -*- coding: utf-8 -*-
label cs_day03_part09:
    if cs_day03_part09_done:
        jump cs_day03_evening_pending
    call cs_day03_137 from cs_return_749444a200c4303ff47f
    call cs_day03_138 from cs_return_3a78bbac3ebdff5057ee
    call cs_day03_139 from cs_return_0f88287a60c0699c1f7f
    call cs_day03_140 from cs_return_f845236e5be679f76a75
    call cs_day03_semen_square_choice from cs_return_b57571648da297340111
    if cs_se_day3_personal_talk:
        call cs_day03_141 from cs_return_0849310a6fd2d2fb3e62
    call cs_day03_142 from cs_return_a700491aac64ba65d31d
    call cs_day03_143 from cs_return_66f1890536d6e74df182
    if cs_un_sketch_time_agreed_day3:
        call cs_day03_144 from cs_return_5ca2bf67e9b2c1432fad
    else:
        call cs_day03_145 from cs_return_d3827772198e396b5e29
    $ cs_day03_part09_done = True
    jump cs_day03_evening_pending

label cs_day03_semen_square_choice:
    if cs_se_friend_before_square_day3 is None:
        $ cs_se_friend_before_square_day3 = cs_friend_se
    label cs_check_day03_140_menu:
    menu:
        "Остаться и поговорить с Семёном по-настоящему":
            if not cs_se_day3_square_awarded:
                $ cs_friend_se += 1
                $ cs_se_day3_square_awarded = True
            $ cs_se_day3_personal_talk = True
            call cs_day03_140a from cs_return_21c0be7b5ff7055ad4c2
        "Не задерживать Семёна и дать ему отдохнуть":
            $ cs_se_day3_personal_talk = False
            call cs_day03_140b from cs_return_7655d056b1ca6d717927
    label cs_check_day03_140_result:
    return

label cs_day03_evening_pending:
    label cs_check_day03_part09_complete:
    hide screen cs_day03_part09_wait_screen
    jump cs_day03_part10

screen cs_day03_part09_wait_screen():
    timer 0.1 action Jump("cs_day03_evening_pending")
