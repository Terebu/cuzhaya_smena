# -*- coding: utf-8 -*-
label cs_day04:
    hide screen cs_day04_wait_screen
    if cs_day04_done:
        jump cs_day05_pending
    if not cs_day04_started:
        call cs_day_title(4)
    $ cs_day04_started = True
    window show dissolve
    call cs_day04_01 from cs_return_282c3dbc0107b99b2e17
    call cs_day04_02 from cs_return_e4858a6f9bd2dc9b5ede
    call cs_day04_03 from cs_return_638fdbdb899d68af253d
    $ cs_d4_undated_photo_location = cs_d4_photo1971_location = cs_d4_roster_location = "lena"
    call cs_day04_04 from cs_return_deaeef4977a3fdb49fa5
    call cs_day04_05 from cs_return_b897cfb85ff5e50f8155
    call cs_day04_06 from cs_return_1235997ba96e731142c3
    $ cs_d4_undated_photo_location = "olga"
    call cs_day04_07 from cs_return_f12b661605a9627c694a
    call cs_day04_08 from cs_return_5c7111eb1c32e92e213e
    call cs_day04_09 from cs_return_b2eb6a49d972688acb16
    call cs_day04_10 from cs_return_a2c5f07a2add795da84e
    $ cs_d4_photo1971_location = cs_d4_roster_location = "library_locked_drawer"
    call cs_day04_11 from cs_return_2adad047c8a5b1096505
    call cs_day04_12 from cs_return_6c8be14b3822c479f47c
    $ cs_d4_dream_notes_location = "library_locked_drawer"
    $ cs_day04_done = True
    jump cs_day05_pending

label cs_day05_pending:
    label cs_check_day04_complete:
    call screen cs_day05_wait_screen
    jump cs_day05_pending

screen cs_day05_wait_screen():
    modal True
    frame:
        align (0.5,0.5)
        padding (32,24)
        background Solid("#142821ed")
        vbox:
            spacing 16
            text "Четвёртый день завершён" size 32
            text "Продолжение — в пятом дне." size 24
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
