# -*- coding: utf-8 -*-
label cs_day03_part03:
    hide screen cs_day03_part02_wait_screen
    $ cs_day03_part02_done = True
    $ cs_day03_at_dining_door = bool(renpy.showing("bg ext_dining_hall_away_day"))
    $ cs_day03_library_visit_time = "late_morning" if cs_mz_map_lead else None
    window show dissolve
    call cs_day03_89 from cs_return_51df2ffa779f2db03ee8
    call cs_day03_90 from cs_return_f1a793880e81f3e5e6bc
    call cs_day03_91 from cs_return_d7e86ca44b778f6b9f51
    call cs_day03_92 from cs_return_48c76212d0275efb0a8c
    call cs_day03_93 from cs_return_38c04297d2a61c8eaf2d
    call cs_day03_94 from cs_return_014e545309fbb0f9b12f
    call cs_day03_95 from cs_return_db41c3956f2d44cd2a92
    $ cs_day03_part03_done = True
    jump cs_day03_part04

label cs_day03_zhenya_book_choice:
    label cs_check_day03_94_menu:
    menu:
        "Спросить Женю, какую книгу она посоветовала бы прочитать":
            if not cs_mz_day3_book_awarded:
                $ cs_friend_mz += 1
                $ cs_mz_day3_book_awarded = True
            $ cs_mz_book_requested_day3 = True
            $ cs_day03_library_visit_time = "late_morning" if cs_mz_map_lead else "after_lunch"
            call cs_day03_94a from cs_return_3b7d14f9ee4348b15c94
        "Не задерживать Женю перед её делами":
            call cs_day03_94b from cs_return_b6466759ee7c0d365116
    label cs_check_day03_94_result:
    return

label cs_day03_part04_pending:
    label cs_check_day03_part03_complete:
    jump cs_day03_part04_legacy

screen cs_day03_part03_wait_screen():
    modal True
    frame:
        align (0.03, 0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Серьёзная советская женщина" size 26
            text "Дальше — проверка локтя у Виолы." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
