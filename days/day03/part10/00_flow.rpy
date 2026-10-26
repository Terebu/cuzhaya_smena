# -*- coding: utf-8 -*-
label cs_day03_part10:
    hide screen cs_day03_part09_wait_screen
    if cs_day03_part10_done:
        jump cs_day03_dinner_pending
    call cs_day03_146 from cs_return_27c0db6881d60ac094e0
    call cs_day03_147 from cs_return_b7c001ef4db8862e0090
    call cs_day03_148 from cs_return_3e9dc4f0fd3940ab83f7
    call cs_day03_darya_reading_choice from cs_return_777b416b3d00ee4bd9ea
    call cs_day03_149 from cs_return_aa8b91b09d5a66ec538e
    call cs_day03_150 from cs_return_c4993a042c4d451791ac
    call cs_day03_151 from cs_return_fd57b8cc273246df9764
    call cs_day03_152 from cs_return_772f4e9d0979c6c5db8e
    call cs_day03_153 from cs_return_6cdc581d96857481b042
    $ cs_day03_part10_done = True
    jump cs_day03_dinner_pending

label cs_day03_darya_reading_choice:
    if cs_da_day3_choice_done:
        return
    label cs_check_day03_148_menu:
    menu:
        "Отложить книгу и расспросить Дашу о музыке":
            if not cs_da_day3_music_awarded:
                $ cs_friend_da += 1
                $ cs_da_day3_music_awarded = True
            $ cs_da_day3_music_talk = True
            $ cs_da_day3_shared_silence = False
            $ cs_da_day3_choice_done = True
            call cs_day03_148a from cs_return_bd423323a7a49b12b7d2
        "Предложить просто посидеть рядом в тишине":
            $ cs_da_day3_shared_silence = True
            $ cs_da_day3_music_talk = False
            $ cs_da_day3_choice_done = True
            call cs_day03_148b from cs_return_c2aa933b5dd603577264
    label cs_check_day03_148_result:
    return

label cs_day03_dinner_pending:
    label cs_check_day03_part10_complete:
    hide screen cs_day03_part10_wait_screen
    jump cs_day03_part11

screen cs_day03_part10_wait_screen():
    timer 0.1 action Jump("cs_day03_dinner_pending")
