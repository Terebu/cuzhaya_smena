# -*- coding: utf-8 -*-
default cs_day01_done = False
default cs_day02_done = False
default cs_friend_sl = 0
default cs_friend_mi = 0

label cs_day01_part11:
    hide screen cs_day01_pending
    window show dissolve
    call cs_day01_59 from cs_return_efdde9964d8091c65515
    call cs_day01_60 from cs_return_3595ddf9301338048359
    call cs_day01_61 from cs_return_2dea37f9eb2c014be688
    call cs_day01_62 from cs_return_ae3aa83b4430b3e783b2
    call cs_day01_63 from cs_return_4b735e6976aed5b23513
    call cs_day01_64 from cs_return_1c648212d6ba39a3d4c0
    $ cs_day01_done = True
    jump cs_day02

label cs_day02:
    $ cs_day02_done = False
    call cs_day_title(2)
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    call cs_day02_01 from cs_return_00a53d9a67f90a82adbd
    call cs_day02_02 from cs_return_f018354585a22b438762
    call cs_day02_03 from cs_return_fdf95fec0874a65a3dfd
    call cs_day02_04 from cs_return_2d111751239a4a9d048a
    call cs_day02_05 from cs_return_4aaa225d38167569220b
    call cs_day02_06 from cs_return_3751bab44e6020b51e31
    call cs_day02_07 from cs_return_e7081a6050e6ebda4c26
    call cs_day02_08 from cs_return_e135cec9ccbf48cf2dc1
    call cs_day02_09 from cs_return_a1d1bd6d8acc8f12164a
    call cs_day02_10 from cs_return_912c669c5fb0033b23d3
    call cs_day02_11 from cs_return_17a483a39f89e5c83978
    call cs_day02_12 from cs_return_fe3c6222cc377d156111
    call cs_day02_13 from cs_return_0ac401e0a9a809679a2f
    call cs_day02_14 from cs_return_14142740aaada969c6a3
    jump cs_day02_part02_pending

label cs_day02_part02_pending:
    jump cs_day02_part02

label cs_check_new_day02_pending:
    jump cs_day02_part02

label cs_day02_part02:
    hide screen cs_day02_continue_screen
    window show dissolve
    call cs_day02_15 from cs_return_7c308ba1603f4e619f9a
    call cs_day02_16 from cs_return_20eaed2834f765b2ea00
    call cs_day02_17 from cs_return_75e9e939250d40e244ac
    call cs_day02_18 from cs_return_3a7e77c98126786cf905
    call cs_day02_19 from cs_return_bc0d9d5636b8a9afcb3f
    call cs_day02_20 from cs_return_c2762c059f5e6b62c291
    jump cs_day02_part03_pending

label cs_day02_19:
    label cs_check_part02_menu:
    menu:
        "Остаться и послушать репетицию Мику":
            if cs_day02_miku_listened is None:
                $ cs_friend_mi += 1
            $ cs_day02_miku_listened = True
            call cs_day02_19a from cs_return_e7308f462f8c90e19b02
        "Поблагодарить Мику и пойти на линейку":
            $ cs_day02_miku_listened = False
            call cs_day02_19b from cs_return_115290ff2912742d9bce
    return

label cs_day02_part03_pending:
    jump cs_day02_part03

label cs_check_part02_pending:
    jump cs_day02_part03

label cs_day02_part03:
    hide screen cs_day02_continue_screen
    window show dissolve
    call cs_day02_22 from cs_return_bf5b5e589c5e71674b7b
    call cs_day02_23 from cs_return_408f3ebeadad127af322
    call cs_day02_24 from cs_return_55242850f8ab495e82c1
    call cs_day02_25 from cs_return_4b58f98c942b7b2293f2
    jump cs_day02_part04_pending

label cs_day02_24:
    label cs_check_part03_menu:
    menu:
        "Предложить Славе помощь с материалами":
            if not cs_sl_day2_awarded:
                $ cs_friend_sl += 1
                $ cs_sl_day2_awarded = True
            $ cs_helped_sl_day2 = True
            call cs_day02_24a from cs_return_c8689558ccb82ca70110
        "Поблагодарить Славю и заняться объявлением":
            $ cs_helped_sl_day2 = False
            call cs_day02_24b from cs_return_4f6c17af76a05a9c64f7
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
    call cs_day02_26 from cs_return_df785663c76d67b7d817
    call cs_day02_27 from cs_return_564fa2ad36ec9a7ded62
    call cs_day02_28 from cs_return_b184cfe59eae633805c3
    call cs_day02_29 from cs_return_895197f766d37a7b9b21
    call cs_day02_30 from cs_return_119f3bbfb2d1e9f01873
    call cs_day02_31 from cs_return_f1cf012c029bf4c06b95
    call cs_day02_viola_choice from cs_return_a62711fb6729f85591a7
    call cs_day02_32 from cs_return_c4e180a3b89b1355034f
    call cs_day02_33 from cs_return_41736dd7491410f19a7c
    jump cs_day02_part05_pending

label cs_day02_viola_choice:
    label cs_check_part04_menu:
    menu:
        "Предложить Виоле помощь с материалами":
            if not cs_viola_day2_awarded:
                $ cs_friend_viola += 1
                $ cs_viola_day2_awarded = True
            $ cs_helped_viola_day2 = True
            call cs_day02_31a from cs_return_15f3864900240e977ec2
        "Поблагодарить Виолу и не задерживаться":
            $ cs_helped_viola_day2 = False
            call cs_day02_31b from cs_return_eff74ee5fdcc03ce794a
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
    call cs_day02_34 from cs_return_e714e3226a063690f0ba
    call cs_day02_35 from cs_return_5653b228789facf187e1
    call cs_day02_semen_choice from cs_return_fd3c4613eba9829a60a8
    call cs_day02_36 from cs_return_c2ca142fc6847356e152
    call cs_day02_37 from cs_return_57bfb67855e3b5c6e5a4
    call cs_day02_38 from cs_return_dfd3195f1e4d730dc96e
    call cs_day02_39 from cs_return_90bd763918e3a3adb9a4
    jump cs_day02_part06_pending

label cs_day02_semen_choice:
    label cs_check_part05_menu:
    menu:
        "Давай сделаем надпись вместе":
            if not cs_se_day2_awarded:
                $ cs_friend_se += 1
                $ cs_se_day2_awarded = True
            $ cs_worked_with_se_day2 = True
            call cs_day02_35a from cs_return_ac2783db9cc916123217
        "Я закончу рисунок, а ты займись буквами":
            $ cs_worked_with_se_day2 = False
            call cs_day02_35b from cs_return_9486da47a7a4d8b06681
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
    call cs_day02_40 from cs_return_bacd217ea8a8b17bbe77
    call cs_day02_41 from cs_return_c62193d8550357b1c070
    call cs_day02_road_choice from cs_return_120141166f18366191ef
    call cs_day02_42 from cs_return_b18e8312d0e44bafe69a
    call cs_day02_43 from cs_return_c99b86323a9a358f4661
    call cs_day02_44 from cs_return_23efb75be1c504782c12
    call cs_day02_45 from cs_return_988325a7a5ae9e66e836
    call cs_day02_46 from cs_return_437d7f54b2a3da866ded
    jump cs_day02_part07_pending

label cs_day02_road_choice:
    label cs_check_part06_menu:
    menu:
        "Сказать Семёну, что меня действительно тревожит":
            if not cs_se_road_day2_awarded:
                $ cs_friend_se += 1
                $ cs_se_road_day2_awarded = True
            $ cs_trusted_se_road_day2 = True
            call cs_day02_41a from cs_return_928433122195b5954c32
        "Ограничиться планом проверки дороги":
            $ cs_trusted_se_road_day2 = False
            call cs_day02_41b from cs_return_b097103797076bbd7aa2
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
    call cs_day02_47 from cs_return_3a0efc9c11a31b878940
    call cs_day02_48 from cs_return_a4fda06e66c565f346e9
    call cs_day02_49 from cs_return_9061f22eb7e33b9aa3b5
    call cs_day02_50 from cs_return_a4b974d7c497fbcf8d35
    call cs_day02_51 from cs_return_0140ad1ebe39c25a8e0b
    call cs_day02_viola_second_choice from cs_return_54afafc80c353bcc4fba
    call cs_day02_52 from cs_return_bd7601db2f5e06b9112a
    call cs_day02_53 from cs_return_b0a09a87126085d1793f
    jump cs_day02_part08_pending

label cs_day02_viola_second_choice:
    label cs_check_part07_menu:
    menu:
        "Немного поговорить с Виолой перед уходом":
            if not cs_viola_second_day2_awarded:
                $ cs_friend_viola += 1
                $ cs_viola_second_day2_awarded = True
            $ cs_talked_viola_second_day2 = True
            call cs_day02_51a from cs_return_701ed7f781a4ad34a38a
        "Поблагодарить Виолу и дать ей вернуться к работе":
            $ cs_talked_viola_second_day2 = False
            call cs_day02_51b from cs_return_4efbe3c3335ce1a13398
    return

label cs_day02_part08_pending:
    $ cs_part07_live = False
    hide screen cs_day02_injury_continue_screen
    label cs_check_part07_pending:
    jump cs_day02_part08_start

label cs_day02_part08_start:
    hide screen cs_day02_injury_continue_screen
    window show dissolve
    call cs_day02_54 from cs_return_9b44f9db50d99700611a
    call cs_day02_55 from cs_return_0f7c2632672a6ce0f7bf
    call cs_day02_56 from cs_return_efcc399cd7aa17364166
    call cs_day02_57 from cs_return_ef52f5e9d876ca075699
    call cs_day02_58 from cs_return_5f5f1782e6eaa43f8a92
    call cs_day02_zhenya_square_choice from cs_return_18b5b2b376c755f07222
    call cs_day02_59 from cs_return_d2f30b4899cf505865eb
    jump cs_day02_part09_pending

label cs_day02_zhenya_square_choice:
    label cs_check_part08_menu:
    menu:
        "Подойти к Жене и поблагодарить за вчерашний разговор":
            if not cs_mz_square_day2_awarded:
                $ cs_friend_mz += 1
                $ cs_mz_square_day2_awarded = True
            $ cs_talked_mz_square_day2 = True
            call cs_day02_58a from cs_return_371c36d24dc8b89c483d
        "Не отвлекать Женю от её дел":
            $ cs_talked_mz_square_day2 = False
            call cs_day02_58b from cs_return_7939818de31368ae74fe
    return

label cs_day02_part09_pending:
    $ cs_part08_live = False
    hide screen cs_day02_square_continue_screen
    label cs_check_part08_pending:
    jump cs_day02_part09_start

label cs_day02_part09_start:
    hide screen cs_day02_square_continue_screen
    window show dissolve
    call cs_day02_reading_interlude from cs_return_19fec527a2c7256413b5
    label cs_check_reading_complete:
    call cs_day02_60 from cs_return_f57e5ec5264d19b948f1
    call cs_day02_61 from cs_return_cba42e5086e79d0579c9
    if cs_friend_mz >= 2:
        call cs_day02_62 from cs_return_4883d45ac9e58968e1e5
    call cs_day02_63 from cs_return_136753ef806172f2bdff
    call cs_day02_64 from cs_return_d557fd84a9aebd32ad7e
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
