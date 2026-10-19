# -*- coding: utf-8 -*-
label cs_day02_71:
    $ save_name = "Чужая смена — День 2: Возвращение Соколовой"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    $ cs_director_scene("cs_house_lena_darya_ext_night")
    scene cs_house_lena_darya_ext_night
    with Dissolve(0.8)
    $ renpy.music.set_volume(0.12, channel="music")
    label cs_check_finale_71:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "До домика я дошла без приключений."
    cs_narrator "Что после сегодняшнего дня само по себе заслуживало небольшого праздника."
    cs_narrator "Я открыла дверь."
    $ cs_director_scene("cs_house_lena_darya_int_night")
    scene cs_house_lena_darya_int_night at cs_house_full_frame
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Внутри горел тёплый свет."
    cs_narrator "Дарья сидела на кровати, рассматривая свою книгу."
    cs_narrator "Услышав меня, подняла голову."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вернулась."
    cs_narrator "Я кивнула."
    cs_ls "Вернулась."
    cs_narrator "Сняла туфли."
    cs_narrator "Аккуратно поставила их возле кровати."
    cs_narrator "Проверила, не задела ли повязку."
    cs_narrator "Потом села."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Дарья снова опустила взгляд к книге."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И вдруг почувствовала, что настроение постепенно меняется."
    cs_narrator "Не резко."
    cs_narrator "Не будто кто-то нажал невидимую кнопку."
    cs_narrator "Просто после нескольких спокойных часов мне снова захотелось поговорить."
    cs_narrator "Немного пошутить."
    cs_narrator "Вспомнить сегодняшние нелепости."
    cs_narrator "И, возможно, слегка подразнить Дашу."
    cs_th "Соколова."
    cs_th "Ты ведь обещала себе сегодня не превращать каждый разговор в представление."
    cs_th "С другой стороны…"
    cs_th "Никто не запрещал просто быть весёлой."
    cs_narrator "Я медленно улыбнулась."
    cs_narrator "Дарья заметила."
    cs_narrator "Подняла голову."
    cs_narrator "Посмотрела на меня."
    cs_narrator "И сразу прищурилась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена."
    cs_narrator "Я повернулась."
    cs_ls "Что?"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты опять что-то придумала?"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Поздравляю."
    cs_narrator "Она посмотрела на меня ещё внимательнее."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "С чем?"
    cs_narrator "Я торжественно расправила плечи."
    cs_ls "С окончанием вечера образцово спокойной и интеллектуальной Соколовой."
    cs_narrator "Дарья замолчала."
    cs_narrator "Потом медленно улыбнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А что будет вместо неё?"
    cs_narrator "Я задумалась."
    cs_ls "Всё та же Соколова. Только теперь у неё снова есть силы разговаривать."
    cs_narrator "Дарья рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А я уже начала привыкать к тишине."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Можем продолжить молчать, если хочешь."
    cs_narrator "Она покачала головой."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нет. Мне интересно, что ты сейчас скажешь."
    cs_narrator "Я довольно кивнула."
    cs_ls "Очень смелое заявление."
    cs_narrator "И устроилась поудобнее на кровати."
    cs_th "Ну вот."
    cs_th "Кажется, отдых действительно пошёл мне на пользу."
    return
