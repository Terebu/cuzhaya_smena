# -*- coding: utf-8 -*-
label cs_day03_part07:
    if cs_day03_part07_done:
        jump cs_day03_part08_pending
    hide screen cs_day03_part06_wait_screen
    call cs_day03_121 from cs_return_0700f75b6cc32b2f2a03
    call cs_day03_122 from cs_return_bf22cbefad97cbcf13a7
    call cs_day03_123 from cs_return_f0a26251b1ad2f018dee
    call cs_day03_124 from cs_return_844bd348e370e41a2adc
    call cs_day03_125 from cs_return_3342464fc5429e8feca2
    call cs_day03_un_lunch_choice from cs_return_800e4b06f2de4a69dae1
    call cs_day03_126 from cs_return_428413dfae88d9a8292a
    call cs_day03_127 from cs_return_2ed9f09a70cc7a013778
    call cs_day03_128 from cs_return_b6524af49256033f2955
    $ cs_day03_part07_done = True
    jump cs_day03_part08_pending

label cs_day03_un_lunch_choice:
    label cs_check_day03_125_menu:
    menu:
        "Предложить Лене Тихоновой пообедать вместе":
            if not cs_un_day3_lunch_awarded:
                $ cs_friend_un += 1
                $ cs_un_day3_lunch_awarded = True
            $ cs_un_day3_lunch_together = True
            call cs_day03_125a from cs_return_1d5d95edbe4f425e993a
        "Поздороваться и дать Лене самой выбрать место":
            $ cs_un_day3_lunch_together = False
            call cs_day03_125b from cs_return_2089f74e68d3f8e2e817
    label cs_check_day03_125_result:
    return

label cs_day03_part08_pending:
    label cs_check_day03_part07_complete:
    hide screen cs_day03_part07_wait_screen
    jump cs_day03_part08

# A loaded save can still be waiting on the old modal screen.
screen cs_day03_part07_wait_screen():
    timer 0.1 action Jump("cs_day03_part08_pending")
