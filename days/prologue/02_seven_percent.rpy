# -*- coding: utf-8 -*-
# Source: source/prologue.md. Dialogue is preserved verbatim.
label cs_scene_02:
    $ save_name = u"Чужая смена — Семь процентов"
    $ cs_director_scene("cs_street")
    scene cs_street
    with fade
    stop music fadeout 2.0
    play ambience cs_wind fadein 1.5
    window show dissolve
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Зимой город становился гораздо приятнее: людей меньше, все торопятся, никому нет до тебя дела."
    cs_narrator "Красота."
    cs_narrator "Поэтому в то утро я вышла из дома без всякого плана."
    cs_narrator "Зима стояла самая обыкновенная — не сказочная и не рождественская."
    cs_narrator "Просто серое небо, грязный снег у обочин и машины, методично превращающие остатки белых сугробов в коричневую кашу."
    cs_narrator "На мне была длинная тёмная куртка, тёплая кофта, широкие брюки и ботинки."
    cs_narrator "Длинные фиолетовые волосы я оставила распущенными. Они лезли в лицо, цеплялись за шарф и электризовались от воротника. Поправлять было бесполезно."
    cs_narrator "Ну и чёрт с ними."
    cs_narrator "Я достала телефон."
    show screen cs_phone(7, "battery")
    label cs_check_battery7:
    cs_narrator "Семь процентов. Прекрасно."
    cs_narrator "Вообще-то я собиралась просто съездить в супермаркет, купить что-нибудь съедобное и провести остаток выходного как цивилизованный человек — ни с кем не разговаривая."
    hide screen cs_phone
    $ cs_director_scene("cs_stop")
    scene cs_stop
    with dissolve
    play sound cs_bus_stop
    cs_narrator "На остановке стоял автобус."
    cs_narrator "{b}410.{/b}"
    cs_narrator "Я сверила номер с маршрутом в телефоне."
    cs_narrator "Вроде подходил."
    cs_ls "Сойдёт."
    cs_narrator "Вот и всё моё стратегическое планирование."
    cs_narrator "Я убрала телефон в карман и поднялась по ступенькам."
    hide screen cs_phone
    #play sound cs_bus_door
    stop ambience fadeout 1.0
    return
