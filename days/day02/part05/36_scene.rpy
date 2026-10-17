# -*- coding: utf-8 -*-
label cs_day02_36:
    $ save_name = "Чужая смена — День 2: Последние штрихи"
    $ cs_part04_live = False
    $ cs_part05_live = True
    if not renpy.showing("cs_cg_poster_planning_day"):
        $ cs_director_scene("cs_cg_poster_planning_day")
        scene cs_cg_poster_planning_day
    $ cs_part05_cg = True
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part05_cast = []
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() is None:
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    label cs_check_part05_s36:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы разложили перед собой готовую основу объявления."
    cs_narrator "Сверху — крупный заголовок:"
    cs_narrator "«МУЗЫКАЛЬНЫЙ ВЕЧЕР»"
    cs_narrator "Чуть ниже — небольшая гитара и несколько нот."
    cs_narrator "Внизу осталось место для информации."
    cs_narrator "Дарья взяла карандаш."
    cs_da "Так. Теперь самое важное."
    cs_ls "Указать, что выступление действительно состоится?"
    cs_da "Желательно."
    cs_narrator "Семён рассмеялся."
    cs_sy "Ольга Дмитриевна сказала, что после ужина. Точного времени пока не будет."
    cs_narrator "Я задумалась."
    cs_ls "Тогда так и напишем."
    cs_narrator "Дарья вывела аккуратными буквами:"
    cs_narrator "«Сегодня после ужина. На площади»."
    cs_narrator "Я посмотрела на результат."
    cs_narrator "Вполне читабельно."
    cs_narrator "И никакого риска, что мы ошибёмся с часами."
    cs_sy "Всё?"
    cs_ls "Почти."
    cs_narrator "Он насторожился."
    cs_sy "Что ещё?"
    cs_narrator "Я указала на нижний угол."
    cs_ls "Должна же здесь быть хотя бы маленькая художественная деталь."
    cs_narrator "Дарья приподняла бровь."
    cs_da "Только маленькая."
    cs_ls "Слово художника."
    cs_narrator "Я нарисовала в углу небольшую нотную строку."
    cs_narrator "Затем рядом — крошечную звёздочку."
    cs_narrator "Посмотрела."
    cs_narrator "Подумала."
    cs_narrator "И отложила карандаш."
    cs_th "Хватит."
    cs_th "Главное — вовремя остановиться."
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    $ cs_part05_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ cs_day02_poster_finished = True
    label cs_check_part05_poster_finished:
    cs_narrator "Семён поднял объявление."
    cs_narrator "Подержал на вытянутых руках."
    cs_sy "Нормально смотрится."
    cs_narrator "Дарья отошла на несколько шагов."
    cs_narrator "Прищурилась."
    cs_da "Заголовок видно. Место и время тоже."
    cs_narrator "Я кивнула."
    cs_ls "Значит, можно предъявлять заказчику."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part05_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ольге Дмитриевне?"
    cs_ls "Кому же ещё. Нашему главному управлению культурных мероприятий."
    cs_narrator "Семён усмехнулся."
    cs_narrator "Мы начали собирать карандаши."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show sl normal pioneer far at cs_actor_far_left zorder 10
    show cs_semen thinking pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part05_sl_arrived:
    cs_narrator "И тут со стороны площади появилась Славя."
    cs_sl "Ну что, как успехи?"
    cs_narrator "Я повернулась к ней."
    cs_ls "Работа завершена. Приступаем к государственной приёмке."
    cs_narrator "Славя рассмеялась."
    cs_sl "Можно посмотреть?"
    cs_narrator "Семён повернул объявление к ней."
    cs_narrator "Она внимательно прочитала текст."
    cs_narrator "Посмотрела на рисунок."
    cs_narrator "Потом улыбнулась."
    show sl smile pioneer far at cs_actor_far_left zorder 10
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Очень красиво получилось!"
    cs_narrator "Я кивнула."
    cs_ls "Спасибо."
    cs_sl "И всё понятно. Это самое главное."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Я же говорила."
    cs_narrator "Я подняла ладони."
    cs_ls "Признаю. Художественный редактор оказался прав."
    if cs_helped_sl_day2:
        label cs_check_part05_sl_helped:
        cs_narrator "Славя посмотрела на оставшиеся карандаши."
        cs_sl "Кстати, спасибо ещё раз за помощь с коробками. Я уже успела разобрать остальное."
        cs_ls "Не за что. Совместный труд укрепляет международную дружбу."
        cs_narrator "Славя улыбнулась."
        cs_sl "Я заметила."
    else:
        label cs_check_part05_sl_neutral:
        cs_narrator "Славя указала на папку."
        show sl normal pioneer far at cs_actor_far_left zorder 10
        $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Я как раз закончила разбирать материалы в кладовой. Потом занесу оставшиеся карандаши."
        show cs_darya smile pioneer far at cs_darya_far_right
        $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Хорошо. Мы всё соберём."
    cs_narrator "Славя посмотрела в сторону площади."
    cs_sl "Объявление можно повесить возле доски информации. Там его точно все увидят."
    cs_sy "Давайте я отнесу."
    cs_narrator "Я повернулась к нему."
    cs_ls "Подожди. Я тоже хочу увидеть, как наш шедевр займёт законное место."
    cs_narrator "Дарья вздохнула."
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только без торжественного открытия."
    cs_narrator "Я задумалась."
    cs_ls "А красную ленточку уже приготовили?"
    cs_da "Лена."
    cs_ls "Всё. Отменяется."
    cs_narrator "Все рассмеялись."
    cs_narrator "Мы направились к площади."
    return
