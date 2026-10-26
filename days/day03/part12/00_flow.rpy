# -*- coding: utf-8 -*-
label cs_day03_part12:
    hide screen cs_day03_part11_wait_screen
    if cs_day03_part12_done:
        jump cs_day03_library_closing_pending
    if not cs_day03_part12_started:
        $ cs_day03_part12_started = True
        call cs_day03_163 from cs_return_02f48ab2d8286438b761
    call cs_day03_164 from cs_return_72010fc5ab65fe4244c2
    call cs_day03_165 from cs_return_271901b788aa5463402f
    call cs_day03_slavya_evening_choice from cs_return_4aa9be91880f40e8858e
    call cs_day03_166 from cs_return_f094b784a8710b412f9f
    call cs_day03_167 from cs_return_9213bcc6b74c823b2edb
    call cs_day03_168 from cs_return_2c5f522e0a57fe7e8331
    if cs_mz_evening_help_day3:
        if not cs_mz_evening_help_completed_day3:
            call cs_day03_169a from cs_return_9eaa2233badffc5713b8
        else:
            $ cs_frame_focus(["cs_zhenya", "cs_darya"])
            with cs_sprite_change
            cs_narrator "С карточками мы уже разобрались раньше. Я открыла книгу, а Даша устроилась рядом; Женя закончила оставшиеся записи."
    else:
        call cs_day03_169b from cs_return_7a1ebe591c47b3689dc9
    call cs_day03_170 from cs_return_6ab3c7851a47ba3a5ae4
    $ cs_day03_part12_done = True
    jump cs_day03_library_closing_pending

label cs_day03_slavya_evening_choice:
    if cs_sl_evening_choice_done:
        return
    if cs_sl_friend_before_evening_choice is None:
        $ cs_sl_friend_before_evening_choice = cs_friend_sl
    $ cs_pov_end()
    $ cs_frame_focus(["cs_semen", "sl"])
    with cs_sprite_change
    label cs_check_day03_165_menu:
    menu:
        "Предложить помочь сверить завтрашние поручения":
            if not cs_sl_evening_help_awarded:
                $ cs_friend_sl += 1
                $ cs_sl_evening_help_awarded = True
            $ cs_sl_evening_schedule_help_day3 = True
            $ cs_sl_evening_choice_done = True
            call cs_day03_165a from cs_return_3e79b83af52e0c472251
        "Не отвлекать их и отправиться за книгой":
            $ cs_sl_evening_choice_done = True
            call cs_day03_165b from cs_return_48c7a67b638bb66983c9
    label cs_check_day03_165_result:
    return

label cs_day03_part12_from_legacy:
    hide screen cs_day03_part11_wait_screen
    $ cs_day03_part11_done = True
    if cs_day03_part12_done or cs_day03_part12_started:
        jump cs_day03_part12
    $ cs_day03_part12_started = True
    $ cs_day03_part12_legacy_entry = True
    $ cs_day03_started = True
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("cs_house_lena_darya_ext_sunset")
    scene cs_house_lena_darya_ext_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "После ужина мы уже успели дойти до домика. Я решила захватить оставленный на столе роман и ещё немного почитать в библиотеке."
    if cs_mz_evening_help_day3:
        $ cs_day03_darya_destination = "library"
        if cs_mz_evening_help_completed_day3:
            cs_da "Я пока вернусь к Жене. С карточками мы уже закончили, можно просто спокойно посидеть."
        else:
            cs_da "Я зайду к Жене первой. Заодно посмотрю, что подготовить к нашей помощи."
    else:
        $ cs_day03_darya_destination = "music_club"
        cs_da "А я загляну к Мику уточнить планы на завтра. Потом встретимся у домика."
    cs_ls "Хорошо. Я зайду за книгой и скоро вернусь."
    jump cs_day03_part12

label cs_day03_library_closing_pending:
    label cs_check_day03_part12_complete:
    jump cs_day03_part13

screen cs_day03_part12_wait_screen():
    timer 0.1 action Jump("cs_day03_part13")
