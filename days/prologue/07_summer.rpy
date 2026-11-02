# -*- coding: utf-8 -*-
# Source: source/prologue.md. Dialogue is preserved verbatim.
label cs_scene_07:
    $ save_name = u"Чужая смена — Лето"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_director_scene("black")
    scene black
    window show dissolve
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Жарко. Это было первое ощущение — не тепло, а именно {b}жарко{/b}."
    cs_narrator "Я нахмурилась, не открывая глаз."
    cs_th "Что за?.."
    cs_narrator "Словно кто-то направил мне в лицо огромную лампу. Кожа нагревалась, под курткой стало невыносимо душно."
    cs_narrator "Я попыталась повернуть голову."
    cs_narrator "Солнце. Настоящее, яркое, тёплое."
    cs_th "Откуда?.."
    cs_narrator "Потом я услышала птиц."
    play ambience cs_forest fadein 2.5
    cs_narrator "Много птиц. Стрекотали насекомые, шелестели листья."
    cs_narrator "Я лежала или сидела? Кажется, сидела."
    cs_narrator "Но почему тогда было так тихо?"
    cs_narrator "Я прислушалась."
    cs_narrator "Ни двигателя, ни отопителя, ни шума дороги. Только птицы, ветер и собственное дыхание."
    cs_th "Стоп. Какие ещё насекомые? На улице январь."
    cs_narrator "Я медленно открыла глаза."
    window hide dissolve
    $ cs_director_scene("cs_sunlight")
    scene cs_sunlight
    with Dissolve(2.0)
    pause 0.6
    $ cs_director_scene("bg int_bus")
    scene bg int_bus
    with Dissolve(2.5)
    window show dissolve
    label cs_check_summer:
    cs_narrator "Сначала я увидела свет."
    cs_narrator "Пришлось несколько раз моргнуть."
    cs_narrator "Потом различила деревья — зелёные, густые, залитые солнцем."
    cs_narrator "За окном не было ни снега, ни серого неба."
    cs_narrator "Только летний лес."
    cs_narrator "Я моргнула и посмотрела ещё раз."
    cs_th "Нет."
    cs_th "Нет-нет-нет."
    cs_th "Что за чертовщина?"
    cs_narrator "Лето. Самое настоящее, с ярким солнцем и зелёной травой."
    cs_narrator "Я резко повернула голову к соседнему сиденью."
    $ cs_director_scene("cs_sleep_summer")
    scene cs_sleep_summer
    with Dissolve(1.5)
    label cs_check_sleep_summer:
    cs_narrator "Дарья всё ещё была рядом."
    cs_narrator "Алые волосы рассыпались по её плечам. Глаза оставались закрытыми."
    cs_narrator "Она спокойно спала, словно ничего не произошло."
    cs_narrator "Я повернулась вперёд."
    $ cs_director_scene("bg ext_camp_entrance_day")
    scene bg ext_camp_entrance_day
    with Dissolve(1.8)
    show cs_windshield
    play ambience cs_camp fadeout 1.0 fadein 1.0
    cs_narrator "Перед автобусом стояли ворота с двумя каменными фигурами по краям. Между ними висела большая вывеска."
    show bg ext_camp_entrance_day at cs_gate_approach
    cs_narrator "Я прочитала надпись."
    label cs_check_gate:
    cs_narrator "{b}«СОВЁНОК»{/b}"
    return
