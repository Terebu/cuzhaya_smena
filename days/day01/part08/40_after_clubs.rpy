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
    cs_narrator "Электроник и Шурик остались внутри. Судя по тому, с каким энтузиазмом они обсуждали источник питания и незнакомый разъём, завтрашний день обещал стать для местной инженерной школы весьма насыщенным."
    cs_narrator "Надеюсь, только без дыма."
    cs_narrator "Я машинально коснулась кармана."
    cs_narrator "Телефон был на месте."
    cs_narrator "Выключенный."
    cs_narrator "Бесполезный."
    cs_narrator "Но хотя бы целый."
    cs_th "Уже достижение."
    cs_th "Советская инженерная школа получила техническое задание, а заказчик сохранил оборудование."
    cs_narrator "Мы с Дарьей направились по дорожке в сторону площади."
    cs_narrator "Некоторое время шли молча."
    cs_narrator "После нескольких часов разговоров, знакомств и попыток разобраться с происходящим тишина оказалась неожиданно приятной."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Красные волосы."
    cs_narrator "Белая рубашка."
    cs_narrator "Пионерский галстук."
    cs_narrator "Тёмно-синяя юбка."
    cs_narrator "Она шла рядом, иногда поглядывая на окружающие деревья и домики."
    cs_narrator "Интересно, о чём она сейчас думала?"
    cs_narrator "О доме?"
    cs_narrator "О странном автобусе?"
    cs_narrator "О том, как мы вообще собираемся возвращаться?"
    cs_narrator "Вопросов хватало."
    cs_narrator "И всё же меня вдруг заинтересовало совершенно другое."
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
    cs_narrator "Я усмехнулась."
    cs_narrator "Но продолжить сразу почему-то не получилось."
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
