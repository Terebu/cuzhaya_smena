# -*- coding: utf-8 -*-
label cs_day03_part11:
    hide screen cs_day03_part10_wait_screen
    if cs_day03_part11_done:
        jump cs_day03_after_dinner_pending
    call cs_day03_154 from cs_return_aae5e16400855fe6697a
    call cs_day03_155 from cs_return_fc456b22106b82f3758b
    call cs_day03_156 from cs_return_ae16cdab8ed4c469606a
    call cs_day03_157 from cs_return_21b6890029ce08f208c3
    call cs_day03_158 from cs_return_7cdcc953e092c4d066a5
    call cs_day03_159 from cs_return_4bf5222eadfe20db2938
    call cs_day03_evening_library_choice from cs_return_6113d59d94ea2b7fe4dd
    call cs_day03_160 from cs_return_6164a8173b5819208491
    $ cs_day03_part11_done = True
    jump cs_day03_part12

label cs_day03_part11_legacy_tail:
    if cs_mz_evening_help_day3:
        call cs_day03_161a from cs_return_d441feee7514a8db3112
    else:
        call cs_day03_161b from cs_return_5cb2ff3a2290b6b5676e
    jump cs_day03_part12_from_legacy
    call cs_day03_162 from cs_return_7cd4dc55c78159de8fcf
    $ cs_day03_part11_done = True
    jump cs_day03_part12_from_legacy

label cs_day03_evening_library_choice:
    if cs_mz_evening_choice_done:
        return
    label cs_check_day03_159_menu:
    menu:
        "Предложить Жене помощь с возвращёнными книгами":
            if not cs_mz_evening_help_awarded:
                $ cs_friend_mz += 1
                $ cs_mz_evening_help_awarded = True
            $ cs_mz_evening_help_day3 = True
            $ cs_mz_evening_choice_done = True
            call cs_day03_159a from cs_return_f6065dada5f26e6b0586
        "Не вмешиваться в работу Жени и пожелать ей хорошего вечера":
            $ cs_mz_evening_help_day3 = False
            $ cs_mz_evening_choice_done = True
            call cs_day03_159b from cs_return_2a261455a76352386914
    label cs_check_day03_159_result:
    return

label cs_day03_after_dinner_pending:
    label cs_check_day03_part11_complete:
    jump cs_day03_part12_from_legacy

screen cs_day03_part11_wait_screen():
    timer 0.1 action Jump("cs_day03_part12_from_legacy")
