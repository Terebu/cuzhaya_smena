# -*- coding: utf-8 -*-
label cs_day03_part08:
    if cs_day03_part08_done:
        jump cs_day03_part09
    hide screen cs_day03_part07_wait_screen
    $ cs_day03_part08_started = True
    call cs_day03_129 from cs_return_aa99e35ebd05c0e7a429
    call cs_day03_130 from cs_return_b6ad8b256e89e10db71c
    call cs_day03_131 from cs_return_2bc31db6e05b875e2a19
    call cs_day03_132 from cs_return_ec4809b58946a55a0033
    call cs_day03_133 from cs_return_dc8ad6c8663eb8821a55
    call cs_day03_134 from cs_return_b9f44acd8afe52806338
    call cs_day03_zhenya_novel_choice from cs_return_ad1330240c1e069b59ec
    call cs_day03_135 from cs_return_c6e7807989fec198a4ea
    call cs_day03_136 from cs_return_4067c31376b7549efaa6
    $ cs_day03_part08_done = True
    jump cs_day03_part09

label cs_day03_zhenya_novel_choice:
    label cs_check_day03_134_menu:
    menu:
        "Спросить Женю, что ей самой нравится в этой истории":
            if not cs_mz_book_talk_awarded_day3:
                $ cs_friend_mz += 1
                $ cs_mz_book_talk_awarded_day3 = True
            $ cs_mz_day3_honest_book_talk = True
            call cs_day03_134a from cs_return_78493c65c41bc80bb934
        "Поблагодарить и продолжить читать":
            call cs_day03_134b from cs_return_24aea0576818949ee788
    label cs_check_day03_134_result:
    return
