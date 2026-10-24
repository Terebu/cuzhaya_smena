# -*- coding: utf-8 -*-
label cs_day03_part05:
    if cs_day03_part05_done:
        jump cs_day03_part06_pending
    hide screen cs_day03_part04_wait_screen
    $ cs_day03_part05_started = True
    $ cs_day03_part04_done = True
    $ cs_day03_part05_route = None
    call cs_day03_104 from cs_return_20e856708a2ca3a60bc4
    call cs_day03_105 from cs_return_7c93b0a3fa5e33bb0c9c
    call cs_day03_106 from cs_return_4a7c7788a0aeca87f37a
    call cs_day03_107 from cs_return_5d948ca24512544cf170
    call cs_day03_108 from cs_return_f897233a8945a8773a9a
    call cs_day03_109 from cs_return_ed67902d6772a6ba58c5
    call cs_day03_110 from cs_return_82486a3b8534e8e2627c
    call cs_day03_111 from cs_return_437e901860c386e66bcf
    call cs_day03_112 from cs_return_fb1801383f026b8b6f23
    $ cs_day03_part05_done = True
    jump cs_day03_part06_pending

label cs_day03_slavya_inventory_choice:
    label cs_check_day03_109_menu:
    menu:
        "Помочь Славе закончить учёт инвентаря":
            if not cs_sl_day3_awarded:
                $ cs_friend_sl += 1
                $ cs_sl_day3_awarded = True
            $ cs_helped_sl_day3 = True
            call cs_day03_109a from cs_return_94ed297e6caeff0407c5
        "Извиниться и отправиться по своим делам":
            call cs_day03_109b from cs_return_b533a9101b5eb9fcba14
    label cs_check_day03_109_result:
    return

label cs_day03_part05_legacy:
    $ cs_day03_part05_legacy_entry = True
    jump cs_day03_part05

label cs_day03_part06_pending:
    label cs_check_day03_part05_complete:
    jump cs_day03_part06

label cs_check_day03_112_library:
    jump cs_day03_part06
label cs_check_day03_112_music:
    jump cs_day03_part06

screen cs_day03_part05_wait_screen():
    modal True
    frame:
        align (0.03,0.06)
        padding (24,20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Общественно полезная деятельность" size 26
            if cs_day03_part06_route == "library":
                text "Дальше — старые каталоги в библиотеке." size 22
            else:
                text "Дальше — музыкальный кружок." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
