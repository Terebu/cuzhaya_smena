# -*- coding: utf-8 -*-
label cs_day05:
    hide screen cs_day05_wait_screen
    if cs_d5_done:
        jump cs_day05_complete
    if not cs_d5_started:
        call cs_day_title(5) from cs_d5_title_return
    $ cs_d5_started = True
    window show dissolve
    call cs_day05_01 from cs_d5_scene_01_return
    call cs_day05_02 from cs_d5_scene_02_return
    call cs_day05_03 from cs_d5_scene_03_return
    call cs_day05_04 from cs_d5_scene_04_return
    call cs_day05_05 from cs_d5_scene_05_return
    call cs_day05_06 from cs_d5_scene_06_return
    call cs_day05_07 from cs_d5_scene_07_return
    call cs_day05_08 from cs_d5_scene_08_return
    call cs_day05_09 from cs_d5_scene_09_return
    call cs_day05_10 from cs_d5_scene_10_return
    call cs_day05_11 from cs_d5_scene_11_return
    call cs_day05_12 from cs_d5_scene_12_return
    call cs_day05_13 from cs_d5_scene_13_return
    call cs_day05_14 from cs_d5_scene_14_return
    call cs_day05_15 from cs_d5_scene_15_return
    call cs_day05_16 from cs_d5_scene_16_return
    call cs_day05_17 from cs_d5_scene_17_return
    call cs_day05_18 from cs_d5_scene_18_return
    call cs_day05_19 from cs_d5_scene_19_return
    call cs_day05_20 from cs_d5_scene_20_return
    $ cs_d5_done = True
label cs_day05_complete:
    label cs_check_day05_complete:
    call screen cs_day05_end_screen
    jump cs_day05_complete

screen cs_day05_end_screen():
    modal True
    frame:
        align (0.5, 0.5)
        padding (32, 24)
        background Solid("#142821ed")
        vbox:
            spacing 16
            text "Конец пятого дня" size 32
            text "Продолжение следует" size 24
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
