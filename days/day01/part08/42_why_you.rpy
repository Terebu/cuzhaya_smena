# -*- coding: utf-8 -*-
label cs_day01_42:
    $ save_name = "Чужая смена — День 1: Почему именно ты?"
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы отошли от середины дорожки, пропуская двух пионеров с мячом."
    cs_narrator "Когда они скрылись за поворотом, Дарья снова посмотрела на меня."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Можно теперь я спрошу?"
    cs_ls "Конечно."
    cs_da "Почему я?"
    cs_narrator "Я открыла рот."
    cs_narrator "Потом закрыла."
    cs_th "Отлично."
    cs_th "Самый логичный вопрос оказался самым сложным."
    cs_ls "Сначала мне хотелось ответить, что не знаю."
    cs_da "А теперь?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Наверное, потому что рядом с тобой мне спокойно."
    cs_narrator "Дарья молчала."
    cs_ls "Я не особенно люблю большие компании. Не люблю, когда от меня постоянно ждут разговоров, шуток или какой-нибудь активности."
    cs_narrator "Я ненадолго остановилась."
    cs_ls "А с тобой можно просто идти рядом и молчать."
    cs_da "И тебе этого достаточно?"
    cs_ls "Не знаю насчёт отношений. Но для начала — уже немало."
    cs_narrator "Я улыбнулась краешком губ."
    cs_ls "И ещё ты очень красивая."
    # cs_darya_variety: reaction
    show cs_darya ear_touch pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья приподняла бровь."
    cs_da "А вот теперь звучит убедительнее."
    cs_ls "Между прочим, я очень долго составляла эту речь."
    cs_da "Минуты две?"
    cs_ls "Не обесценивай труд начинающего оратора."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_narrator "Я тоже улыбнулась."
    cs_narrator "Но затем снова стала серьёзной."
    cs_ls "Есть ещё одна причина."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Какая?"
    cs_narrator "Я посмотрела на деревья."
    cs_ls "Мы обе оказались здесь совершенно случайно."
    cs_narrator "Дарья кивнула."
    cs_ls "Ещё утром у каждой была своя жизнь в 2026 году. Свои дела, привычки, планы."
    cs_narrator "Я ненадолго замолчала."
    cs_ls "А теперь мы в неизвестном пионерлагере, без нормальной связи и без малейшего понимания, как вернуться домой."
    cs_da "Это правда."
    cs_ls "Семён хотя бы успел провести здесь сутки. Я знаю часть происходящего по игре."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Но ты пока почти ничего об этом месте не знаешь. И всё равно держишься."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья пожала плечами."
    cs_da "А что мне ещё остаётся?"
    cs_ls "Вот именно."
    cs_narrator "Я тихо усмехнулась."
    cs_ls "Мне нравится, что ты не пытаешься изображать человека, у которого на всё есть ответы."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она задумалась."
    cs_da "Мне кажется, у нас обеих сейчас ответов меньше, чем вопросов."
    cs_ls "Поэтому и предлагаю пока заниматься вопросами."
    cs_da "Вместе?"
    cs_ls "Вместе."
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "Затем Дарья спросила:"
    # cs_darya_variety: reaction
    show cs_darya worried pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А если я не отвечу тебе взаимностью?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Тогда не ответишь."
    cs_da "И что дальше?"
    cs_ls "Ничего особенного."
    cs_narrator "Я пожала плечами."
    cs_ls "Продолжим искать способ вернуться домой. Ходить на обед. Спорить из-за того, кто забыл закрыть дверь в домик."
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_ls "Ты не обязана мне ничем только потому, что я решила признаться."
    cs_narrator "Дарья опустила взгляд."
    cs_narrator "Потом снова посмотрела на меня."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Спасибо."
    cs_ls "За что?"
    cs_da "За то, что не торопишь."
    cs_ls "Я сегодня и так уже достаточно поторопилась. Особенно когда понесла телефон в кружок электроники."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она снова рассмеялась."
    cs_narrator "Но на этот раз улыбка не исчезла сразу."
    stop music fadeout 3.0
    $ renpy.music.set_volume(0.22,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    label cs_check_day01_part08_silence:
    cs_narrator "Дарья ненадолго задумалась."
    cs_da "Ты мне тоже нравишься, Лен."
    cs_narrator "Я повернулась к ней."
    cs_narrator "Она продолжила:"
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне с тобой интересно. И я рада, что мы оказались здесь не поодиночке."
    pause 0.7
    cs_narrator "Пауза."
    label cs_check_day01_part08_boundaries:
    cs_da "Но насчёт всего остального я пока не знаю."
    cs_narrator "Я кивнула."
    cs_ls "Поняла."
    # cs_darya_variety: reaction
    show cs_darya ear_touch pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Правда?"
    cs_ls "Да."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Решение принято к рассмотрению. Срок исполнения не установлен."
    cs_narrator "Дарья покачала головой."
    # cs_darya_variety: reaction
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты неисправима."
    cs_ls "Есть такое."
    cs_narrator "Мы снова пошли по дорожке."
    cs_narrator "Уже медленнее."
    cs_narrator "И почему-то теперь молчание казалось совсем другим."
    return
