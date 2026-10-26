# -*- coding: utf-8 -*-
label cs_day03_part13:
    hide screen cs_day03_part12_wait_screen
    if cs_day03_part13_done:
        jump cs_day03_bedtime_pending
    $ cs_day03_part13_started = True
    call cs_day03_171 from cs_return_36b19626e465312ebae7
    call cs_day03_172 from cs_return_990b3d4daf1d01c146b0
    call cs_day03_173 from cs_return_fdd48ab4448b6b10cabd
    call cs_day03_174 from cs_return_40fd552608e8efc5fbbf
    call cs_day03_175 from cs_return_e2457aedb1a4b433711c
    call cs_day03_176 from cs_return_435c091524255853e518
    call cs_day03_177 from cs_return_ff2c7dc455c27583ff10
    call cs_day03_178 from cs_return_5959861f07b894689b38
    call cs_day03_darya_night_choice from cs_return_2ac02807f2488f85ee6b
    call cs_day03_179 from cs_return_68dc1a12280b3d119586
    $ cs_day03_part13_done = True
    jump cs_day03_bedtime_pending

label cs_day03_darya_night_choice:
    if cs_da_day3_night_choice_done:
        return
    $ cs_pov_end()
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_check_day03_178_menu:
    menu:
        "Рассказать Даше, почему меня задел финал книги":
            if not cs_da_day3_night_trust_awarded:
                $ cs_friend_da += 1
                $ cs_da_day3_night_trust_awarded = True
            $ cs_da_day3_fear_of_getting_used_to_camp = True
            $ cs_da_day3_night_choice_done = True
            call cs_day03_178a from cs_return_5e897a039105bc72f9e4
        "Не нарушать тишину и просто идти рядом":
            $ cs_da_day3_quiet_walk = True
            $ cs_da_day3_night_choice_done = True
            call cs_day03_178b from cs_return_a6a370e5d60ed124bd2b
    label cs_check_day03_178_result:
    return

label cs_day03_bedtime_pending:
    label cs_check_day03_part13_complete:
    jump cs_day03_part14

screen cs_day03_part13_wait_screen():
    timer 0.1 action Jump("cs_day03_part14")
