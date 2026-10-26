# -*- coding: utf-8 -*-
label cs_day03_part14:
    hide screen cs_day03_part13_wait_screen
    if cs_day03_part14_done:
        jump cs_day04_pending
    $ cs_day03_part14_started = True
    call cs_day03_180 from cs_return_c5b83d1cbbd42ab624d0
    call cs_day03_181 from cs_return_b98384efc526b3343aa5
    if cs_da_friend_before_night is None:
        $ cs_da_friend_before_night = cs_friend_da
    call cs_day03_182 from cs_return_476b6e22134c2b0a5e54
    call cs_day03_bed_choice from cs_return_4e9735b4912ef56af400
    if cs_da_shared_bed_day3:
        call cs_day03_185 from cs_return_74c6949e2da929518378
        call cs_day03_186 from cs_return_52c80ae2c60c7d39d4b2
        call cs_day03_187 from cs_return_ae43058a9189f4c0d667
        call cs_day03_confession_choice from cs_return_68984a66bee0360084a1
        call cs_day03_188 from cs_return_73b65557c6f37f9d78fe
    else:
        call cs_day03_184 from cs_return_86983593bec42502a6a4
    call cs_day03_189 from cs_return_857d170f7b32428594d3
    $ cs_day03_part14_done = cs_day03_completed = True
    jump cs_day04_pending

label cs_day03_bed_choice:
    if cs_da_bed_choice_done_day3:
        return
    if cs_da_friend_before_night is None:
        $ cs_da_friend_before_night = cs_friend_da
    $ cs_pov_end()
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_check_day03_182_menu:
    menu:
        "Сказать Даше, что сегодня хочется спать рядом с ней":
            $ cs_da_bed_request_day3 = True
            call cs_day03_183 from cs_return_ffc535d0832015a6f6e8
        "Не торопить события и пожелать Даше спокойной ночи":
            $ cs_da_respected_space_day3 = True
            $ cs_da_shared_bed_day3 = False
            cs_ls "Давай отдыхать. Спокойной ночи, Даш."
            cs_da "И тебе, Лен."
    $ cs_da_bed_choice_done_day3 = True
    label cs_check_day03_182_result:
    return

label cs_day03_confession_choice:
    if cs_da_confession_choice_done_day3 or not cs_da_shared_bed_day3:
        return
    if cs_da_friend_before_night >= 2:
        label cs_check_day03_187_menu:
        menu:
            "Сказать Даше: «Я тебя люблю»":
                $ cs_da_love_confession_day3 = True
                call cs_day03_187a from cs_return_02e7a2c6e63d22af6892
            "Не торопить события и просто остаться рядом":
                $ cs_da_unspoken_feelings_day3 = True
                call cs_day03_187b from cs_return_7a4634697278678f1fe9
    else:
        $ cs_da_unspoken_feelings_day3 = True
        call cs_day03_187b from cs_return_80d03d44f0213442d94e
    $ cs_da_confession_choice_done_day3 = True
    return

label cs_day04_pending:
    label cs_check_day03_part14_complete:
    call screen cs_day04_wait_screen
    jump cs_day04_pending

screen cs_day04_wait_screen():
    modal True
    frame:
        align (0.5,0.5)
        padding (32,24)
        background Solid("#142821ed")
        vbox:
            spacing 16
            text "Третий день завершён" size 32
            text "Продолжение — в четвёртом дне." size 24
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Главное меню" action [Function(cs_restore_audio),MainMenu()]
