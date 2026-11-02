# -*- coding: utf-8 -*-
label cs_day01_40:
    $ save_name = "Чужая смена — День 1: После кружка"
    label cs_check_day01_part08_start:
    $ renpy.music.set_volume(0.22,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 2.0 fadein 2.0
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы вышли из клуба уже ближе к вечеру."
    cs_narrator "Парни остались обсуждать источник питания. Надеюсь, завтра обойдётся без дыма."
    cs_narrator "Я проверила карман: телефон на месте. Выключенный, зато целый."
    cs_narrator "Мы молча пошли к площади. После нескольких часов разговоров тишина была кстати."
    cs_narrator "Дарья шла рядом, поглядывая на деревья и домики. Красные волосы, белая рубашка, галстук."
    cs_narrator "О чём она думает? О доме, автобусе, возвращении?"
    cs_narrator "А спросить мне вдруг захотелось о другом."
    cs_narrator "Я замедлила шаг."
    cs_ls "Даш."
    # cs_darya_variety: reaction
    show cs_darya ear_touch pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "М?"
    cs_ls "Можно один личный вопрос?"
    cs_narrator "Она посмотрела на меня с лёгким подозрением."
    cs_da "Насколько личный?"
    cs_ls "Пока сама определяюсь."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Уже многообещающе."
    cs_narrator "Я усмехнулась, но продолжить сразу не смогла."
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.22,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    stop music fadeout 2.0
    return
