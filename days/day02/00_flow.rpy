# -*- coding: utf-8 -*-
default cs_day01_done = False
default cs_day02_done = False
default cs_friend_sl = 0
default cs_friend_mi = 0

label cs_day01_part11:
    hide screen cs_day01_pending
    window show dissolve
    call cs_day01_59
    call cs_day01_60
    call cs_day01_61
    call cs_day01_62
    call cs_day01_63
    call cs_day01_64
    $ cs_day01_done = True
    jump cs_day02

label cs_day02:
    $ cs_day02_done = False
    call cs_day_title(2)
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day02_01
    call cs_day02_02
    call cs_day02_03
    call cs_day02_04
    call cs_day02_05
    call cs_day02_06
    call cs_day02_07
    call cs_day02_08
    call cs_day02_09
    call cs_day02_10
    call cs_day02_11
    call cs_day02_12
    call cs_day02_13
    call cs_day02_14
    jump cs_day02_part02_pending

label cs_day02_part02_pending:
    jump cs_day02_part02

label cs_check_new_day02_pending:
    jump cs_day02_part02

label cs_day02_part02:
    hide screen cs_day02_continue_screen
    window show dissolve
    call cs_day02_15
    call cs_day02_16
    call cs_day02_17
    call cs_day02_18
    call cs_day02_19
    call cs_day02_20
    jump cs_day02_part03_pending

label cs_day02_19:
    label cs_check_part02_menu:
    menu:
        "Остаться и послушать репетицию Мику":
            if cs_day02_miku_listened is None:
                $ cs_friend_mi += 1
            $ cs_day02_miku_listened = True
            call cs_day02_19a
        "Поблагодарить Мику и пойти на линейку":
            $ cs_day02_miku_listened = False
            call cs_day02_19b
    return

label cs_day02_part03_pending:
    jump cs_day02_part03

label cs_check_part02_pending:
    jump cs_day02_part03

label cs_day02_part03:
    hide screen cs_day02_continue_screen
    window show dissolve
    call cs_day02_22
    call cs_day02_23
    call cs_day02_24
    call cs_day02_25
    jump cs_day02_part04_pending

label cs_day02_24:
    label cs_check_part03_menu:
    menu:
        "Предложить Славе помощь с материалами":
            if not cs_sl_day2_awarded:
                $ cs_friend_sl += 1
                $ cs_sl_day2_awarded = True
            $ cs_helped_sl_day2 = True
            call cs_day02_24a
        "Поблагодарить Славю и заняться объявлением":
            $ cs_helped_sl_day2 = False
            call cs_day02_24b
    return

label cs_day02_part04_pending:
    jump cs_day02_part04

label cs_check_part03_pending:
    jump cs_day02_part04

label cs_day02_part04:
    hide screen cs_day02_continue_screen
    hide screen cs_day02_work_continue_screen
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day02_26
    call cs_day02_27
    call cs_day02_28
    call cs_day02_29
    call cs_day02_30
    call cs_day02_31
    call cs_day02_viola_choice
    call cs_day02_32
    call cs_day02_33
    jump cs_day02_part05_pending

label cs_day02_viola_choice:
    label cs_check_part04_menu:
    menu:
        "Предложить Виоле помощь с материалами":
            if not cs_viola_day2_awarded:
                $ cs_friend_viola += 1
                $ cs_viola_day2_awarded = True
            $ cs_helped_viola_day2 = True
            call cs_day02_31a
        "Поблагодарить Виолу и не задерживаться":
            $ cs_helped_viola_day2 = False
            call cs_day02_31b
    return

label cs_day02_part05_pending:
    jump cs_day02_part05

label cs_check_part04_pending:
    jump cs_day02_part05

label cs_day02_part05:
    hide screen cs_day02_work_continue_screen
    hide screen cs_day02_continue_screen
    hide screen cs_day02_walk_continue_screen
    $ cs_part04_live = False
    window show dissolve
    call cs_day02_34
    call cs_day02_35
    call cs_day02_semen_choice
    call cs_day02_36
    call cs_day02_37
    call cs_day02_38
    call cs_day02_39
    jump cs_day02_part06_pending

label cs_day02_semen_choice:
    label cs_check_part05_menu:
    menu:
        "Давай сделаем надпись вместе":
            if not cs_se_day2_awarded:
                $ cs_friend_se += 1
                $ cs_se_day2_awarded = True
            $ cs_worked_with_se_day2 = True
            call cs_day02_35a
        "Я закончу рисунок, а ты займись буквами":
            $ cs_worked_with_se_day2 = False
            call cs_day02_35b
    return

label cs_day02_part06_pending:
    jump cs_day02_part06

label cs_check_part05_pending:
    jump cs_day02_part06

label cs_day02_part06:
    hide screen cs_day02_walk_continue_screen
    hide screen cs_day02_road_continue_screen
    $ cs_part05_live = False
    window show dissolve
    call cs_day02_40
    call cs_day02_41
    call cs_day02_road_choice
    call cs_day02_42
    call cs_day02_43
    call cs_day02_44
    call cs_day02_45
    call cs_day02_46
    jump cs_day02_part07_pending

label cs_day02_road_choice:
    label cs_check_part06_menu:
    menu:
        "Сказать Семёну, что меня действительно тревожит":
            if not cs_se_road_day2_awarded:
                $ cs_friend_se += 1
                $ cs_se_road_day2_awarded = True
            $ cs_trusted_se_road_day2 = True
            call cs_day02_41a
        "Ограничиться планом проверки дороги":
            $ cs_trusted_se_road_day2 = False
            call cs_day02_41b
    return

label cs_day02_part07_pending:
    jump cs_day02_part07

label cs_check_part06_pending:
    jump cs_day02_part07

label cs_day02_part07:
    hide screen cs_day02_road_continue_screen
    hide screen cs_day02_injury_continue_screen
    $ cs_part06_live = False
    window show dissolve
    call cs_day02_47
    call cs_day02_48
    call cs_day02_49
    call cs_day02_50
    call cs_day02_51
    call cs_day02_viola_second_choice
    call cs_day02_52
    call cs_day02_53
    jump cs_day02_part08_pending

label cs_day02_viola_second_choice:
    label cs_check_part07_menu:
    menu:
        "Немного поговорить с Виолой перед уходом":
            if not cs_viola_second_day2_awarded:
                $ cs_friend_viola += 1
                $ cs_viola_second_day2_awarded = True
            $ cs_talked_viola_second_day2 = True
            call cs_day02_51a
        "Поблагодарить Виолу и дать ей вернуться к работе":
            $ cs_talked_viola_second_day2 = False
            call cs_day02_51b
    return

label cs_day02_part08_pending:
    $ cs_part07_live = False
    hide screen cs_day02_injury_continue_screen
    label cs_check_part07_pending:
    jump cs_day02_part08_start

label cs_day02_part08_start:
    hide screen cs_day02_injury_continue_screen
    window show dissolve
    call cs_day02_54
    call cs_day02_55
    call cs_day02_56
    call cs_day02_57
    call cs_day02_58
    call cs_day02_zhenya_square_choice
    call cs_day02_59
    jump cs_day02_part09_pending

label cs_day02_zhenya_square_choice:
    label cs_check_part08_menu:
    menu:
        "Подойти к Жене и поблагодарить за вчерашний разговор":
            if not cs_mz_square_day2_awarded:
                $ cs_friend_mz += 1
                $ cs_mz_square_day2_awarded = True
            $ cs_talked_mz_square_day2 = True
            call cs_day02_58a
        "Не отвлекать Женю от её дел":
            $ cs_talked_mz_square_day2 = False
            call cs_day02_58b
    return

label cs_day02_part09_pending:
    $ cs_part08_live = False
    hide screen cs_day02_square_continue_screen
    label cs_check_part08_pending:
    jump cs_day02_part09_start

label cs_day02_part09_start:
    hide screen cs_day02_square_continue_screen
    window show dissolve
    call cs_day02_reading_interlude
    label cs_check_reading_complete:
    call cs_day02_60
    call cs_day02_61
    if cs_friend_mz >= 2:
        call cs_day02_62
    call cs_day02_63
    call cs_day02_64
    jump cs_day02_part10_start

label cs_day02_part10_pending:
    $ cs_day02_seating_done = True
    hide screen cs_day02_concert_wait_screen
    label cs_check_part09_pending:
    $ cs_day02_seating_done = True
    jump cs_day02_part10_start

screen cs_day02_concert_wait_screen():
    modal True
    frame:
        align (0.5, 0.96)
        padding (30, 18)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 2 — Котлетки с пюрешкой" size 32
            text "Зрители собрались. Музыкальный вечер — впереди." size 24
            hbox:
                spacing 30
                textbutton "Сохранить игру" action ShowMenu("save")
                textbutton "Загрузить игру" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

screen cs_day02_square_continue_screen():
    modal True
    frame:
        align (0.5, 0.96)
        padding (30, 18)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 2 — Угадай кто" size 32
            text "До вечернего выступления есть время. Продолжение следует." size 24
            hbox:
                spacing 30
                textbutton "Сохранить игру" action ShowMenu("save")
                textbutton "Загрузить игру" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

screen cs_day02_injury_continue_screen():
    modal True
    frame:
        align (0.5, 0.96)
        padding (30, 18)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 2 — Корень всех проблем" size 32
            text "Сегодня без новых подвигов. Продолжение следует." size 24
            hbox:
                spacing 30
                textbutton "Сохранить игру" action ShowMenu("save")
                textbutton "Загрузить игру" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

screen cs_day02_road_continue_screen():
    modal True
    frame:
        align (0.5, 0.96)
        padding (30, 18)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 2 — Дорога, которая возвращает" size 32
            text "Наблюдения записаны. Продолжение следует." size 24
            hbox:
                spacing 30
                textbutton "Сохранить игру" action ShowMenu("save")
                textbutton "Загрузить игру" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

screen cs_day02_walk_continue_screen():
    modal True
    frame:
        align (0.5, 0.96)
        padding (30, 18)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 2 — Бумажные дела и сердечные вопросы" size 32
            text "Объявление готово. Продолжение следует." size 24
            hbox:
                spacing 30
                textbutton "Сохранить игру" action ShowMenu("save")
                textbutton "Загрузить игру" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

screen cs_day02_work_continue_screen():
    modal True
    frame:
        align (0.5, 0.96)
        padding (30, 18)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 2 — Диагноз: анахронизм" size 32
            text "Работа над объявлением продолжается. Следующая часть — впереди." size 24
            hbox:
                spacing 30
                textbutton "Сохранить игру" action ShowMenu("save")
                textbutton "Загрузить игру" action ShowMenu("load")
                textbutton "Главное меню" action MainMenu()

screen cs_day02_continue_screen():
    modal True
    frame:
        align (0.5, 0.5)
        padding (50, 35)
        background Solid("#142821")
        vbox:
            spacing 20
            text "День 2 — Плановая самодеятельность" size 40
            text "Третья часть завершена. Продолжение следует." size 26
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action MainMenu()
