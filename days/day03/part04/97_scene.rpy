# -*- coding: utf-8 -*-
label cs_day03_97:
    $ save_name = "Чужая смена — День 3: Слишком привлекательная медицина"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    cs_narrator "Мы шли не торопясь."
    cs_narrator "Я уже успела убедиться, что бегать сегодня — идея сомнительная."
    cs_narrator "Виола вчера объяснила достаточно ясно, чего делать не стоит."
    cs_narrator "А утренний эксперимент показал, что её рекомендации существуют не исключительно ради украшения медицинской документации."
    cs_th "Какая неожиданность."
    cs_th "Медицинский работник оказался компетентнее пионерки с фиолетовыми волосами."
    cs_th "Соколова, очередное открытие века."
    cs_narrator "Дарья посмотрела на мою повязку."
    cs_da "Локоть сейчас не болит?"
    cs_narrator "Я осторожно согнула руку."
    cs_narrator "Остановилась, почувствовав лёгкое натяжение."
    cs_ls "Только если сильно двигать. В обычном положении нормально."
    cs_narrator "Она кивнула."
    cs_da "Тогда хорошо."
    cs_narrator "Немного помолчала."
    cs_da "И всё-таки."
    cs_narrator "Я повернулась."
    cs_ls "Что?"
    cs_narrator "Она слегка улыбнулась."
    cs_da "Тебе правда настолько нравится Виола?"
    cs_narrator "Я посмотрела на неё."
    cs_th "О."
    cs_th "Кажется, мой утренний монолог всё-таки не прошёл бесследно."
    cs_ls "Смотря что ты имеешь в виду."
    if renpy.showing("cs_darya"):
        show cs_darya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья пожала плечами."
    cs_da "Ты уже второй день говоришь, какая она красивая."
    cs_narrator "Я кивнула."
    cs_ls "Потому что она красивая."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "И?"
    cs_narrator "Я улыбнулась."
    cs_ls "И у неё хорошее чувство юмора."
    cs_narrator "Пауза."
    cs_ls "А ещё она умеет накладывать повязки, что в моём случае значительно повышает привлекательность профессии."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Понятно."
    cs_narrator "Я посмотрела на неё чуть внимательнее."
    cs_ls "А тебя это беспокоит?"
    cs_narrator "Она ненадолго задумалась."
    cs_da "Нет. Просто пытаюсь понять, когда ты говоришь серьёзно."
    cs_narrator "Я улыбнулась."
    cs_ls "Виола симпатичная. Это серьёзно."
    cs_narrator "Дарья кивнула."
    cs_narrator "Я продолжила:"
    cs_ls "Но девушка, которая мне нравится, сейчас идёт рядом."
    cs_narrator "Дарья повернулась ко мне."
    cs_narrator "На мгновение замолчала."
    cs_narrator "Затем чуть улыбнулась."
    cs_da "Очень своевременное уточнение."
    cs_narrator "Я кивнула."
    cs_ls "Я обучаемая."
    cs_narrator "Она рассмеялась."
    cs_da "Особенно когда тебе выгодно."
    cs_narrator "Я задумалась."
    cs_ls "Какая несправедливая характеристика."
    cs_da "Но точная."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом медленно кивнула."
    cs_ls "К сожалению, возражений не имею."
    cs_narrator "Мы засмеялись."
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_97_aidpost:
    cs_narrator "Впереди показался медпункт."
    cs_narrator "Знакомое небольшое здание."
    cs_narrator "Крыльцо."
    cs_narrator "Дверь."
    cs_th "Третий день."
    cs_th "А я уже могу найти это место с закрытыми глазами."
    cs_th "Хотя не стоит проверять. Достаточно, что однажды проверила собственную способность не замечать корни."
    cs_narrator "Я остановилась у ступенек."
    cs_narrator "Посмотрела на Дарью."
    cs_ls "Ну что, сопровождающая сторона готова?"
    cs_narrator "Она кивнула."
    cs_da "Готова."
    cs_narrator "Я поднялась на крыльцо."
    cs_narrator "Постучала."
    cs_narrator "Изнутри раздался знакомый голос."
    cs_vi "Входите."
    cs_narrator "Я улыбнулась."
    cs_ls "Слышишь? Даже приглашение звучит убедительно."
    cs_narrator "Дарья покачала головой."
    cs_da "Лена, это просто слово «входите»."
    cs_ls "Не разрушай мою веру в красоту профессионального общения."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я открыла дверь."
    return
