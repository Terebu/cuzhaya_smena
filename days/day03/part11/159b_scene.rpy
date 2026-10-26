# -*- coding: utf-8 -*-
label cs_day03_159b:
    $ save_name = "Чужая смена — День 3: Иногда лучше просто пожелать хорошего вечера"
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на книгу Жени."
    cs_narrator "Потом на неё."
    cs_ls "Тогда не буду тебя задерживать."
    cs_narrator "Женя кивнула."
    cs_mz "Хорошо."
    cs_narrator "Я улыбнулась."
    cs_ls "Удачи с книгами."
    cs_narrator "Она усмехнулась."
    cs_mz "Спасибо. Надеюсь, они сегодня будут вести себя приличнее некоторых посетителей."
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Женя, мне кажется, сейчас прозвучало совершенно необоснованное обвинение."
    cs_narrator "Она улыбнулась."
    cs_mz "Я вообще-то никого не называла."
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Я задумалась."
    cs_narrator "Потом кивнула."
    cs_ls "Понимаю. Доказать ничего не получится."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Вот и хорошо."
    cs_narrator "Я немного улыбнулась."
    cs_ls "Тогда до завтра?"
    if cs_mz_open_library_invitation_day3:
        cs_narrator "Женя кивнула."
        cs_mz "Конечно. Ты же знаешь, где меня найти."
        cs_narrator "Я улыбнулась."
        cs_ls "Знаю."
    else:
        cs_mz "Если захочешь взять ещё что-нибудь, приходи."
        cs_narrator "Я кивнула."
        cs_ls "Хорошо."
    cs_th "И этого вполне достаточно."
    cs_th "Хорошее отношение не означает, что нужно непременно участвовать во всех делах человека."
    return
