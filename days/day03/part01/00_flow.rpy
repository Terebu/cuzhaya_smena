# -*- coding: utf-8 -*-
label cs_day03:
    hide screen cs_day02_complete_screen
    $ cs_day02_done = True
    $ cs_day02_part10_done = True
    $ cs_part10_live = False
    $ cs_director_scene("black")
    call cs_day_title(3)
    $ cs_day03_started = True
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day03_75 from cs_return_2812958b39d39b36cfb0
    call cs_day03_76 from cs_return_5952df350a127525d9ab
    call cs_day03_77 from cs_return_f4bc1c75c74764ca98bb
    if cs_friend_sl >= 1:
        call cs_day03_78a from cs_return_dfe21804ec55496c068a
    else:
        call cs_day03_78b from cs_return_faaf1b118d914678522a
    label cs_check_day03_poster_result:
    call cs_day03_79 from cs_return_5721843101f006bebdcc
    call cs_day03_80 from cs_return_f4c303507d6f991125fa
    call cs_day03_81 from cs_return_2bf4b707106f02be0bca
    $ cs_day03_part01_done = True
    jump cs_day03_part02_pending

label cs_day03_part02_pending:
    label cs_check_day03_part01_complete:
    hide screen cs_day03_part01_wait_screen
    jump cs_day03_part02

screen cs_day03_part01_wait_screen():
    modal True
    frame:
        align (0.5, 0.15)
        padding (28, 22)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Часть 1 — Доброе утро, товарищ Соколова" size 27
            text "Девушки идут на завтрак. Продолжение — в следующей части." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
