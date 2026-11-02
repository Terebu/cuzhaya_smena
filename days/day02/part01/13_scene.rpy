# -*- coding: utf-8 -*-
label cs_day02_13:
    $ save_name = "Чужая смена — День 2: Разговор без лишних ушей"
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    $ cs_breakfast_un_here = False
    if renpy.music.get_playing() != "sound/music/just_think.ogg":
        play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/dining_hall_full.ogg":
        play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.12, channel="ambience", delay=1.0)
    label cs_check_breakfast_s13:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда завтрак подходил к концу, Семён немного наклонился к нам. Выражение его лица стало серьёзнее."
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
    $ cs_breakfast_cast = []
    show cs_semen serious pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_breakfast_private:
    cs_sy "Слушайте. Насчёт автобуса."
    cs_narrator "Я поставила стакан. Дарья тоже повернулась к нему."
    cs_ls "Да?"
    cs_sy "Я после нашего разговора всё думаю, когда он мог исчезнуть."
    cs_ls "Я тоже."
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
    $ cs_breakfast_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты точно не видела ничего необычного у ворот?"
    cs_narrator "Я задумалась. Перед глазами снова появилась пустая дорога. Лес. Асфальт."
    cs_narrator "Место, где вчера стоял автобус."
    cs_ls "Ничего определённого. Даже следы шин нормально рассмотреть не получилось."
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
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
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
    $ cs_breakfast_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы ведь пока даже не знаем, куда ведёт эта дорога."
    cs_narrator "Я посмотрела на неё."
    cs_th "Вот. Именно."
    cs_narrator "Вчера всё казалось довольно простым. Есть лагерь. Есть дорога. Есть автобус."
    cs_narrator "Значит, где-то должен существовать маршрут обратно. Но теперь исчез единственный знакомый транспорт. И сама дорога оставалась совершенно неизвестной."
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
    $ cs_breakfast_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Нам нужно сначала выяснить, что находится за воротами."
    cs_narrator "Семён кивнул."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я поэтому и предложил сходить."
    cs_da "Посмотреть можно. Но не обязательно сегодня уходить далеко."
    cs_narrator "Я повернулась к ней."
    cs_ls "Согласна."
    cs_narrator "Она посмотрела на меня чуть внимательнее. Кажется, всё ещё проверяла, действительно ли я собираюсь соблюдать собственное обещание."
    cs_th "Да, Даш. На этот раз без самостоятельных экспедиций."
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
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
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
    $ cs_breakfast_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Тогда когда?"
    cs_narrator "Я задумалась. На сегодня у нас уже было одно вполне конкретное дело. Телефон. Шурик."
    cs_narrator "Электроник. И, вероятно, очередная встреча с местной электротехникой."
    cs_ls "После линейки хотела снова сходить в клубы. Посмотреть, получилось ли что-нибудь с питанием телефона."
    cs_sy "Можно с вами?"
    cs_narrator "Я уже открыла рот. Но остановилась. Посмотрела на Дарью. Она заметила."
    cs_narrator "И немного улыбнулась."
    cs_da "Конечно. Вместе будет проще."
    cs_narrator "Семён кивнул."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Хорошо."
    cs_ls "Значит, сначала клубы. А с дорогой определимся, когда разберёмся с делами на сегодня."
    cs_sy "Ладно."
    cs_narrator "Я посмотрела на него."
    cs_ls "Кстати, это уже третий день твоего пребывания?"
    cs_sy "Да."
    cs_da "А у нас второй."
    cs_narrator "Я задумалась."
    # cs_director_begin: REFLECTIVE_SHOT: Remembered chronology and missing notebook
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_f9be118425:
    # cs_director_end
    cs_th "Вот ещё одна деталь, которую нельзя потерять."
    cs_narrator "Разница в один день. Пока небольшая. Но если наше пребывание действительно связано с историей, которую я помню, она может оказаться важной. Я машинально потянулась к карману."
    cs_narrator "И сразу вспомнила, что лист наблюдений остался в домике."
    cs_th "Прекрасно. Система документирования дала сбой."
    # cs_director_begin: Return to direct interaction: Remembered chronology and missing notebook
    $ cs_frame_focus(["cs_darya", "cs_semen"])
    with cs_sprite_change
    label cs_director_check_1fda380022:
    # cs_director_end
    cs_narrator "Дарья заметила моё движение."
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
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Записать хотела?"
    cs_ls "Да."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Давай потом. Ты запомнишь."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Думаешь?"
    cs_da "Два и три — не такие уж сложные числа."
    cs_narrator "Семён усмехнулся."
    cs_sy "Пока мы здесь втроём, можно просто спросить."
    cs_narrator "Я посмотрела на него, потом на Дарью."
    cs_th "А ведь верно."
    cs_narrator "Не всякую информацию обязательно немедленно превращать в отчёт. Иногда достаточно того, что рядом есть люди, которые помнят то же самое. Я улыбнулась."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Хорошо. Откладываем заседание комиссии до окончания завтрака."
    cs_da "Наконец-то."
    return
