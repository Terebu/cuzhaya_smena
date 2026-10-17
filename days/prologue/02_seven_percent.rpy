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
    cs_narrator "Зимой город вообще становился гораздо приятнее."
    cs_narrator "Людей меньше."
    cs_narrator "Все куда-то торопятся."
    cs_narrator "Никому нет до тебя дела."
    cs_narrator "Красота."
    cs_narrator "Именно поэтому в то утро я вышла из дома совершенно без какого-либо плана."
    cs_narrator "За окном стояла самая обыкновенная зима."
    cs_narrator "Не сказочная."
    cs_narrator "Не рождественская."
    cs_narrator "Просто серое небо, грязный снег у обочин и машины, методично превращающие остатки белых сугробов в коричневую кашу."
    cs_narrator "На мне была длинная тёмная куртка, тёплая кофта, широкие брюки и ботинки."
    cs_narrator "Длинные фиолетовые волосы я оставила распущенными. Они постоянно лезли в лицо, цеплялись за шарф и электризовались от воротника."
    cs_narrator "Попытка поправить их особенного результата не дала."
    cs_narrator "Ну и чёрт с ними."
    cs_narrator "Я достала телефон."
    show screen cs_phone(7, "battery")
    label cs_check_battery7:
    cs_narrator "Прекрасно."
    cs_narrator "Просто замечательно."
    cs_narrator "Вообще-то я собиралась всего лишь съездить в супермаркет."
    cs_narrator "Купить что-нибудь съедобное."
    cs_narrator "Вернуться домой."
    cs_narrator "И провести остаток выходного так, как его должен проводить любой цивилизованный человек."
    cs_narrator "Не разговаривая ни с кем."
    hide screen cs_phone
    $ cs_director_scene("cs_stop")
    scene cs_stop
    with dissolve
    play sound cs_bus_stop
    cs_narrator "На остановке стоял автобус."
    cs_narrator "{b}410.{/b}"
    cs_narrator "Я посмотрела на номер."
    cs_narrator "Затем на маршрут в телефоне."
    cs_narrator "Потом снова на автобус."
    cs_narrator "Вроде подходил."
    cs_ls "Сойдёт."
    cs_narrator "Вот и всё моё стратегическое планирование."
    cs_narrator "Я убрала телефон в карман и поднялась по ступенькам."
    hide screen cs_phone
    #play sound cs_bus_door
    stop ambience fadeout 1.0
    return
