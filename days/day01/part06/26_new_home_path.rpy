# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_26:
    $ save_name = "Чужая смена — День 1: Дорога к новому дому"
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    show sl smile pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(1.3)
    $ renpy.music.set_volume(0.45,delay=1.0,channel="music")
    play music cs_day_music_daily fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_camp_center:
        play ambience cs_day_camp_center fadeout 1.5 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После столовой солнце припекало ещё сильнее. Я поправила галстук: утром собиралась за продуктами, теперь иду по пионерлагерю в бесплатной форме."
    cs_th "Интересная программа лояльности."
    cs_narrator "Славя шагала впереди."
    cs_sl "Ваш домик недалеко. Там сейчас никто не живёт, так что можете располагаться вдвоём."
    cs_ls "Замечательно. А коммунальные платежи здесь предусмотрены?"
    cs_narrator "Славя удивлённо посмотрела на меня."
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Какие платежи?"
    cs_ls "Никакие. Уточняю условия проживания."
    cs_narrator "Дарья бросила на меня взгляд."
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_ls "Что?"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Может, хотя бы пять минут без вопросов, которые никто не понимает?"
    cs_ls "Сложное требование. Но попробую."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show sl smile pioneer at cs_actor_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(1.4)
    # cs_director_begin: REFLECTIVE_SHOT: Camp paths and independent world
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_3da2ea974f:
    # cs_director_end
    cs_narrator "Мы свернули между домиками. Шелестели деревья, издалека слышались голоса."
    cs_narrator "Я узнавала поворот, ограду, фасад клуба между стволами. А за ними обнаруживались места, которых на игровых фонах не было."
    cs_narrator "Знакомая карта заканчивалась. И это притягивало не меньше, чем пугало."
    # cs_director_begin: Return to direct interaction: Camp paths and independent world
    $ cs_frame_focus(["sl", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_ffe656a9cf:
    # cs_director_end
    cs_narrator "Дарья заметила, что я замедлила шаг."
    cs_da "Опять что-то узнала?"
    cs_ls "Скорее пытаюсь сопоставить географию с памятью."
    cs_da "Получается?"
    cs_ls "Пока да. Но это как пользоваться картой города, нарисованной человеком, который видел только пять перекрёстков."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Звучит не слишком надёжно."
    cs_ls "Поэтому и проверяем."
    cs_narrator "Славя оглянулась."
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Вы раньше бывали в похожем лагере?"
    cs_ls "В похожем"
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "А где?"
    cs_ls "Дома."
    cs_narrator "Славя приняла расплывчатый ответ и пошла дальше. Дарья тихо произнесла:"
    cs_da "Неплохо выкрутилась."
    cs_ls "Спасибо. Запишем в протокол."
    return
