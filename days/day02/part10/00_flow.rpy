# -*- coding: utf-8 -*-
label cs_day02_part10_start:
    hide screen cs_day02_concert_wait_screen
    window show dissolve
    $ cs_part09_live = False
    $ cs_reading_live = False
    if cs_reading_book_borrowed and not cs_lena_book_returned:
        call cs_day02_66
        call cs_day02_67
        call cs_day02_68
        if cs_friend_mz >= 2:
            call cs_day02_68c
        elif cs_friend_mz == 1:
            call cs_day02_68b
        else:
            call cs_day02_68a
        call cs_day02_69
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
        call cs_day02_65
    if not cs_day02_concert_done:
        call cs_day02_concert
    call cs_day02_70
    call cs_day02_71
    call cs_day02_72
    call cs_day02_73
    call cs_day02_74
    $ cs_part10_live = False
    $ cs_day02_part10_done = True
    $ cs_day02_done = True
    jump cs_day02_complete

label cs_day02_complete:
    window hide dissolve
    $ cs_director_scene("black")
    scene black
    with Dissolve(2.0)
    show text "День 2 завершён" at truecenter
    with dissolve
    pause 2.0
    hide text with dissolve
    label cs_check_day02_complete:
    call screen cs_day02_complete_screen
    jump cs_check_day02_complete

screen cs_day02_complete_screen():
    modal True
    frame:
        align (0.5, 0.5)
        padding (45, 30)
        background Solid("#142821ed")
        vbox:
            spacing 18
            text "День 2 — Без лишних слов" size 36
            text "Лагерь засыпает. Третий день — впереди." size 25
            text "Это конец доступного вертикального среза." size 22
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio), MainMenu()]
