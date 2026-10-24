# -*- coding: utf-8 -*-
label cs_day03_part02:
    hide screen cs_day03_part01_wait_screen
    $ cs_day03_part01_done = True
    window show dissolve
    call cs_day03_83 from cs_return_adc5f18dcf87ce97217d
    call cs_day03_84 from cs_return_7d0bd545b8b89e1700cf
    call cs_day03_85 from cs_return_04a0fe1a19cc6d8e26ee
    call cs_day03_86 from cs_return_e688c3eb123b549f6b3b
    call cs_day03_87 from cs_return_d07260330de4681be369
    call cs_day03_88 from cs_return_cc1a654b81c5c4295251
    $ cs_day03_part02_done = True
    jump cs_day03_part03_pending

label cs_day03_semen_choice:
    label cs_check_day03_87_menu:
    menu:
        "Спросить Семёна, как у него дела":
            if not cs_se_day3_morning_awarded:
                $ cs_friend_se += 1
                $ cs_se_day3_morning_awarded = True
            call cs_day03_87a from cs_return_bb415629862e8d911167
        "Не задерживать его перед завтраком":
            call cs_day03_87b from cs_return_dcae345623aa4bffd824
    return

label cs_day03_part03_pending:
    label cs_check_day03_part02_complete:
    hide screen cs_day03_part02_wait_screen
    jump cs_day03_part03

screen cs_day03_part02_wait_screen():
    modal True
    frame:
        align (0.03, 0.06)
        padding (24, 20)
        background Solid("#142821ed")
        vbox:
            spacing 12
            text "День 3. Двадцать секунд самоконтроля" size 26
            text "Продолжение — за завтраком." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
