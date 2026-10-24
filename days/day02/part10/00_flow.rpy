# -*- coding: utf-8 -*-
label cs_day02_part10_start:
    hide screen cs_day02_concert_wait_screen
    window show dissolve
    $ cs_part09_live = False
    $ cs_reading_live = False
    if cs_reading_book_borrowed and not cs_lena_book_returned:
        call cs_day02_66 from cs_return_094801163811b0bba7ee
        call cs_day02_67 from cs_return_ba00d7e3a688319600a7
        call cs_day02_68 from cs_return_875a40c77b1154f074b9
        if cs_friend_mz >= 2:
            call cs_day02_68c from cs_return_3b08ac141f62f980ea0b
        elif cs_friend_mz == 1:
            call cs_day02_68b from cs_return_8ed90e07a62e6f6264c7
        else:
            call cs_day02_68a from cs_return_f608ed46b59a5823abbd
        call cs_day02_69 from cs_return_267569315f6bc8b2375f
    else:
        # Legacy saves never receive an invented library loan.
        $ cs_director_scene("cs_camp_path_sunset")
        scene cs_camp_path_sunset
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        with Dissolve(0.8)
        # cs_director_begin: entry frame; explicit scene plan
        $ cs_frame_focus(["cs_darya"])
        with cs_sprite_change
        # cs_director_end
        cs_narrator "Мы с Дарьей направились к площади: музыкальный вечер вот-вот должен был начаться."
    if not cs_day02_seating_done:
        call cs_day02_65 from cs_return_259a6661de2ee255a358
    if not cs_day02_concert_done:
        call cs_day02_concert from cs_return_752f9b4b63962dc617ef
    call cs_day02_70 from cs_return_f79a743f45c77ca4115b
    call cs_day02_71 from cs_return_6de683a6c1effd61c142
    call cs_day02_72 from cs_return_26d720cf439768fae369
    call cs_day02_73 from cs_return_042f4faacf1c75fff73d
    call cs_day02_74 from cs_return_2db53474ef6c4519c627
    $ cs_part10_live = False
    $ cs_day02_part10_done = True
    $ cs_day02_done = True
    jump cs_day02_complete

label cs_day02_complete:
    label cs_check_day02_complete:
    jump cs_day03

screen cs_day02_complete_screen():
    modal True
    frame:
        align (0.5, 0.5)
        padding (45, 30)
        background Solid("#142821ed")
        vbox:
            spacing 18
            text "День 2 — Без лишних слов" size 36
            text "Лагерь просыпается. Продолжить третий день." size 25
            textbutton "Продолжить" action Return()
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
