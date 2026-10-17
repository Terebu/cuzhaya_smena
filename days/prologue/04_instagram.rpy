# -*- coding: utf-8 -*-
# Source: source/prologue.md. Dialogue is preserved verbatim.
label cs_scene_04:
    $ save_name = u"Чужая смена — Двести сорок семь тысяч"
    show cs_bus_city at cs_bus_ride zorder -10 with dissolve
    #stop ambience fadeout 2.0
    play music cs_music_After_Hours fadein 1.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я достала телефон."
    cs_narrator "Открыла Instagram."
    show screen cs_phone(5, "profile")
    label cs_check_profile:
    cs_narrator "За ночь прибавилось ещё около восьмисот человек."
    cs_narrator "Последняя фотография снова попала в рекомендации."
    # cs_phone_focus: camera
    # cs_presence_keep: hide cs_dasha_winter
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    show screen cs_instagram_post("cs_instagram_oni") with dissolve
    label cs_check_instagram_oni:
    # cs_director_begin: Phone gallery occupies the visual focus
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_c9bb96bb14:
    # cs_director_end
    cs_narrator "На ней я стояла возле красного Mitsubishi в лесу."
    cs_narrator "Грязная с ног до головы."
    cs_narrator "В огромном худи."
    cs_narrator "С маской они на лице."
    cs_narrator "И с металлической битой в руке."
    cs_narrator "Машина, кстати, была не моя. Как и большинство автомобилей на моих фотографиях."
    cs_narrator "Но комментаторов подобные мелочи никогда не интересовали."
    cs_narrator "Их гораздо сильнее волновал вопрос, кого именно я закопала за багажником."
    cs_narrator "Один особенно талантливый человек даже нарисовал примерную схему преступления."
    cs_narrator "С координатами."
    cs_narrator "Я усмехнулась."
    cs_th "Людям определённо нечем заняться."
    cs_narrator "Пролистала комментарии."
    show screen cs_instagram_post("cs_instagram_studio") with dissolve
    label cs_check_instagram_studio:
    cs_narrator "Следующая фотография — мастерская."
    show screen cs_instagram_post("cs_instagram_crush") with dissolve
    label cs_check_instagram_crush:
    cs_narrator "Дальше — селфи после одной крайне неудачной поездки."
    show screen cs_instagram_post("cs_instagram_evening") with dissolve
    label cs_check_instagram_evening:
    cs_narrator "Потом — вечерний городской пейзаж."
    show screen cs_instagram_post("cs_instagram_daily") with dissolve
    label cs_check_instagram_daily:
    cs_narrator "И ещё десятки совершенно не связанных друг с другом снимков."
    cs_narrator "Я смотрела на них несколько секунд."
    cs_narrator "Разные места."
    cs_narrator "Разная одежда."
    cs_narrator "Разные настроения."
    cs_narrator "Но один и тот же человек."
    cs_narrator "Я выключила экран."
    hide screen cs_instagram_post with dissolve
    # cs_phone_focus: camera
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    show screen cs_phone(5, "battery")
    label cs_check_battery5:
    cs_ls "Молодец, Лена. Просто молодец."
    hide screen cs_phone
    cs_narrator "Телефон отправился обратно в карман."
    cs_narrator "За окном медленно проплывали серые здания."
    cs_narrator "Магазины."
    cs_narrator "Остановки."
    cs_narrator "Люди."
    cs_narrator "Потом домов стало меньше."
    cs_narrator "Я нахмурилась."
    cs_narrator "Кажется, супермаркет должен был быть раньше."
    cs_narrator "Или позже?"
    cs_narrator "Я ведь даже не посмотрела, сколько остановок мне нужно проехать."
    cs_th "Гениально."
    cs_narrator "Снова достала телефон."
    show screen cs_phone(2, "battery")
    label cs_check_battery2:
    cs_ls "Да ладно..."
    cs_narrator "Я попыталась открыть карты."
    cs_narrator "Экран задумался."
    cs_narrator "Показал серый прямоугольник."
    cs_narrator "После чего окончательно погас."
    show screen cs_phone(0, "off")
    play sound cs_phone_error
    label cs_check_phone_off:
    cs_narrator "Несколько секунд я смотрела на собственное отражение в чёрном экране."
    cs_ls "Просто замечательно."
    cs_narrator "Красноволосая девушка рядом чуть повернула голову."
    cs_narrator "Мне показалось, что уголки её губ дрогнули."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Что?"
    cs_da "Ничего."
    cs_narrator "Голос оказался тихим."
    cs_narrator "Спокойным."
    cs_narrator "Даже немного сонным."
    hide screen cs_phone
    cs_narrator "Я убрала телефон."
    cs_ls "Если мы сейчас уедем в другую область, виноват будет Samsung."
    cs_narrator "Она взглянула на мой карман."
    cs_narrator "Потом на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Он сам выбирал автобус?"
    cs_narrator "Я замолчала."
    cs_narrator "Посмотрела на неё."
    cs_ls "Нет."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда, наверное, не он."
    cs_narrator "Я невольно усмехнулась."
    cs_ls "Ладно. Один ноль в твою пользу."
    cs_narrator "Она тихо хмыкнула и снова отвернулась."
    # cs_director_begin: The brief conversation is over
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_9530346d03:
    # cs_director_end
    cs_narrator "На этом наша социальная активность закончилась."
    cs_narrator "Меня полностью устраивало."
    return
