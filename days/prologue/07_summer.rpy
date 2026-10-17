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
    cs_narrator "Жарко."
    cs_narrator "Это было первое ощущение."
    cs_narrator "Не тепло."
    cs_narrator "Именно {b}жарко{/b}."
    cs_narrator "Я нахмурилась, не открывая глаз."
    cs_th "Что за?.."
    cs_narrator "Мне казалось, будто кто-то направил мне в лицо огромную лампу."
    cs_narrator "Кожа постепенно нагревалась."
    cs_narrator "Под курткой стало невыносимо душно."
    cs_narrator "Я попыталась повернуть голову."
    cs_narrator "Солнце."
    cs_narrator "Это определённо было солнце."
    cs_narrator "Настоящее."
    cs_narrator "Яркое."
    cs_narrator "Тёплое."
    cs_th "Откуда?.."
    cs_narrator "Потом я услышала птиц."
    play ambience cs_forest fadein 2.5
    cs_narrator "Много птиц."
    cs_narrator "Где-то стрекотали насекомые."
    cs_narrator "Шелестели листья."
    cs_narrator "Я лежала или сидела?"
    cs_narrator "Кажется, сидела."
    cs_narrator "Но почему тогда было так тихо?"
    cs_narrator "Я прислушалась."
    cs_narrator "Никакого двигателя."
    cs_narrator "Никакого отопителя."
    cs_narrator "Никакого шума дороги."
    cs_narrator "Только птицы."
    cs_narrator "Ветер."
    cs_narrator "И собственное дыхание."
    cs_th "Стоп."
    cs_th "Какие ещё, к чёрту, насекомые?"
    cs_th "На улице январь."
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
    cs_narrator "Потом различила деревья."
    cs_narrator "Зелёные."
    cs_narrator "Густые."
    cs_narrator "Залитые солнцем."
    cs_narrator "За окном не было ни снега, ни серого неба."
    cs_narrator "Только летний лес."
    cs_narrator "Я несколько секунд сидела неподвижно."
    cs_narrator "Смотрела наружу."
    cs_narrator "Моргнула."
    cs_narrator "Посмотрела ещё раз."
    cs_th "Нет."
    cs_th "Нет-нет-нет."
    cs_th "Что за чертовщина?"
    cs_narrator "Я медленно перевела взгляд на собственные руки."
    cs_narrator "Потом на окно."
    cs_narrator "Потом снова на деревья."
    cs_narrator "Лето."
    cs_narrator "Самое настоящее лето."
    cs_narrator "С ярким солнцем и зелёной травой."
    cs_narrator "Я резко повернула голову к соседнему сиденью."
    $ cs_director_scene("cs_sleep_summer")
    scene cs_sleep_summer
    with Dissolve(1.5)
    label cs_check_sleep_summer:
    cs_narrator "Дарья всё ещё была рядом."
    cs_narrator "Алые волосы рассыпались по её плечам. Глаза оставались закрытыми."
    cs_narrator "Она спокойно спала."
    cs_narrator "Словно ничего не произошло."
    cs_narrator "Я смотрела на неё несколько секунд."
    cs_narrator "Потом медленно повернулась вперёд."
    $ cs_director_scene("bg ext_camp_entrance_day")
    scene bg ext_camp_entrance_day
    with Dissolve(1.8)
    show cs_windshield
    play ambience cs_camp fadeout 1.0 fadein 1.0
    cs_narrator "Перед автобусом стояли ворота."
    cs_narrator "По обе стороны от них возвышались две каменные фигуры."
    cs_narrator "А между ними висела большая вывеска."
    show bg ext_camp_entrance_day at cs_gate_approach
    cs_narrator "Я прочитала надпись."
    label cs_check_gate:
    cs_narrator "{b}«СОВЁНОК»{/b}"
    return
