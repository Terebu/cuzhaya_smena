# -*- coding: utf-8 -*-
label cs_day03_134b:
    $ save_name = "Чужая смена — День 3: Тишина по обоюдному согласию"
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Я улыбнулась."
    if cs_mz_friend_on_arrival_day3 >= 1:
        cs_ls "Спасибо, Женя. Хорошую книгу выбрала."
    else:
        cs_ls "Спасибо, Женя. Хорошо, что можно спокойно почитать."
    cs_narrator "Она кивнула."
    cs_mz "Пожалуйста."
    cs_narrator "Я снова открыла роман."
    cs_ls "Не буду тебя отвлекать."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя слегка улыбнулась."
    cs_mz "Хорошо."
    cs_narrator "Она вернулась за свой стол."
    $ cs_reflective_focus()
    with cs_sprite_leave
    cs_narrator "Я продолжила читать."
    cs_narrator "В конце концов, я пришла сюда именно за этим."
    cs_narrator "И совершенно не обязательно превращать каждый хороший разговор в часовую дискуссию."
    return
