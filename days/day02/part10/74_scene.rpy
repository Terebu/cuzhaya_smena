# -*- coding: utf-8 -*-
label cs_day02_74:
    $ save_name = "Чужая смена — День 2: Завтра будет завтра"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_74:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Через некоторое время мы всё-таки отпустили руки."
    cs_narrator "Дарья поднялась со своей кровати."
    cs_narrator "Аккуратно убрала книгу на тумбочку."
    cs_narrator "Я тоже начала устраиваться на ночь."
    cs_narrator "Повреждённый локоть неприятно напомнил о себе, когда я попыталась снять галстук слишком резким движением."
    cs_ls "Ай."
    cs_narrator "Дарья сразу обернулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Рука?"
    cs_narrator "Я кивнула."
    cs_ls "Немного."
    cs_narrator "Она подошла ближе."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Помочь?"
    cs_narrator "Я посмотрела на галстук."
    cs_narrator "Потом на неё."
    cs_ls "Если не трудно."
    cs_narrator "Дарья осторожно помогла мне развязать узел, стараясь не задеть повреждённую руку."
    cs_narrator "Я поблагодарила её."
    cs_narrator "Она улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Пожалуйста."
    cs_narrator "Я аккуратно сложила галстук."
    cs_narrator "Села на кровать."
    cs_ls "Всё-таки сегодня у меня какой-то удивительный день."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему?"
    cs_narrator "Я задумалась."
    if cs_lena_book_returned:
        cs_ls "Утром бегала. Днём исследовала пространственную петлю. Потом познакомилась с землёй поближе, чем планировала. Вечером дочитала книгу и послушала концерт."
    else:
        cs_ls "Утром бегала. Днём исследовала пространственную петлю. Потом познакомилась с землёй поближе, чем планировала. Вечером послушала концерт."
    cs_narrator "Дарья усмехнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Действительно насыщенно."
    cs_ls "И ведь завтра будет только третий день."
    cs_narrator "Она посмотрела на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Если ты собираешься завтра снова бегать, хотя бы посмотри, как будет чувствовать себя локоть."
    cs_narrator "Я кивнула."
    cs_ls "Да. Виола ведь не зря просила его беречь."
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вот это уже разумно."
    cs_narrator "Я задумалась."
    cs_narrator "Потом посмотрела на неё."
    cs_ls "А если рука перестанет болеть, составишь мне компанию на утренней прогулке?"
    cs_narrator "Она немного помолчала."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "На прогулке — возможно."
    cs_narrator "Я улыбнулась."
    cs_ls "Прекрасно."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не превращай её в очередной забег."
    cs_ls "Никаких соревнований."
    cs_narrator "Она прищурилась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Точно?"
    cs_narrator "Я вздохнула."
    cs_ls "Даша, ты начинаешь совершенно необоснованно сомневаться в моей дисциплинированности."
    cs_narrator "Она посмотрела на мой локоть."
    cs_narrator "Потом на меня."
    cs_narrator "И рассмеялась."
    cs_narrator "Я тоже."
    cs_ls "Ладно. Возможно, не совсем необоснованно."
    cs_narrator "Мы закончили готовиться ко сну."
    cs_narrator "Дарья погасила основной свет."
    cs_narrator "Комната погрузилась в мягкую темноту."
    # Keep the same portrait height through bedtime, per user request.
    cs_narrator "Из окна доносилось стрекотание сверчков."
    cs_narrator "Я осторожно улеглась на бок, не прижимая повреждённую руку к матрасу."
    # cs_director_begin: Private night reflection, not the sleeping pose itself
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_b11badd71b:
    # cs_director_end
    cs_narrator "Некоторое время просто смотрела в потолок."
    cs_th "Какой же странный день."
    cs_narrator "Ещё утром мне казалось, что я обязана каждую свободную минуту посвящать возвращению домой."
    cs_narrator "А теперь…"
    cs_narrator "Теперь я понимала, что это невозможно."
    cs_narrator "Не потому, что перестала хотеть домой."
    cs_narrator "И не потому, что мне внезапно стало всё равно."
    cs_narrator "Просто человеческая голова не способна бесконечно существовать в состоянии тревоги."
    cs_narrator "Иногда нужно остановиться."
    cs_narrator "Почитать."
    cs_narrator "Послушать музыку."
    cs_narrator "Поговорить с кем-нибудь."
    cs_narrator "Или просто помолчать рядом с человеком, который тебе нравится."
    # cs_director_begin: Lena addresses Darya, both lying down
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_4862310767:
    # cs_director_end
    cs_narrator "Я повернула голову."
    cs_narrator "Дарья уже лежала на своей кровати."
    cs_ls "Даш."
    cs_narrator "Она откликнулась почти сразу."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "М?"
    cs_narrator "Я немного помолчала."
    cs_ls "Спасибо за сегодняшний день."
    cs_narrator "Дарья повернулась ко мне."
    cs_narrator "В темноте я почти не различала её лица."
    cs_narrator "Но голос прозвучал тепло."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И тебе, Лен."
    cs_narrator "Я улыбнулась."
    call cs_day02_74a from cs_return_3e0bdedba4a00ba6c482
    # Compatibility label for saves already at the old final reflection.
    label cs_director_check_d61a0c0e86:
    stop music fadeout 4.0
    stop ambience fadeout 4.0
    return
