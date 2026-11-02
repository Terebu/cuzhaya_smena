# -*- coding: utf-8 -*-
label cs_day02_64d:
    $ save_name = "Чужая смена — День 2: Ужин без обязательной тишины"
    $ cs_part09_live = True
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_dinner64d:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Некоторое время мы действительно молчали. Женя ела. Дарья тоже."
    # cs_director_begin: REFLECTIVE_SHOT: Dinner plate and Moscow memory
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_fa8d03b9db:
    # cs_director_end
    cs_narrator "А я рассматривала собственную тарелку. Картофельное пюре. Котлета. Небольшой кусочек хлеба."
    cs_narrator "Самый обыкновенный ужин. Если не считать того, что ещё недавно я сидела перед монитором в Москве, а теперь находилась в советском пионерском лагере."
    cs_th "Пожалуй, за два дня я уже почти перестала удивляться подобным обстоятельствам. Опасная тенденция."
    cs_narrator "Я взяла ложку. Попробовала пюре."
    cs_th "Неплохо. Очень даже."
    # cs_director_begin: Return to direct interaction: Dinner plate and Moscow memory
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    label cs_director_check_5c4ae70de0:
    # cs_director_end
    cs_narrator "Женя заметила, что я снова задумалась."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Что-то не так с едой?"
    cs_narrator "Я подняла взгляд."
    cs_ls "Нет. Наоборот."
    cs_mz "Тогда чего смотришь на тарелку?"
    cs_narrator "Я улыбнулась."
    cs_ls "Вспоминаю одну старую песенку."
    cs_narrator "Дарья тихо рассмеялась. Женя посмотрела на неё."
    cs_mz "Я так понимаю, это долгая история?"
    cs_da "Нет. Просто Лена по дороге вспомнила старый интернетный мем про котлеты с пюре."
    cs_narrator "Женя некоторое время молчала. Затем посмотрела на свою тарелку, потом на меня."
    cs_mz "И ты теперь каждый раз будешь вспоминать его, когда увидишь котлеты?"
    cs_ls "Надеюсь, что нет."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Очень обнадёживает."
    cs_narrator "Я улыбнулась."
    if cs_mz_quiet_visit_seen:
        cs_narrator "Мы снова ненадолго заговорили о той самой книге — без пересказов и спойлеров."
    else:
        cs_narrator "Потом Женя осторожно отодвинула книгу подальше от тарелки. Я заметила обложку."
        cs_ls "Что читаешь?"
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Книгу."
        cs_narrator "Я замолчала. Дарья прикрыла рот ладонью."
        cs_ls "Исчерпывающий ответ."
        cs_mz "Ты спросила — я ответила."
        cs_ls "Формально безупречно."
        cs_narrator "Женя усмехнулась. Затем всё-таки повернула книгу так, чтобы я могла прочитать название. Я посмотрела."
        cs_ls "Интересная?"
        cs_narrator "Она ненадолго задумалась."
        cs_mz "Пока да. Только главный герой временами ведёт себя совершенно нелогично."
        cs_ls "Знакомое чувство."
        cs_narrator "Женя посмотрела на меня."
        # cs_presence_keep: hide cs_semen
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya thinking pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Что?"
        cs_narrator "Я пожала плечами."
        cs_ls "Иногда читаешь историю и думаешь: ну зачем человек сейчас именно это сделал? Можно же было просто поговорить."
        cs_narrator "Она кивнула."
        # cs_presence_keep: hide cs_semen
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Вот именно."
        cs_da "А потом оказывается, что если бы он поговорил, половины книги просто не было бы."
        cs_narrator "Я посмотрела на неё, потом на Женю. Обе молчали. Я медленно улыбнулась."
        cs_ls "Между прочим, отличное объяснение некоторых литературных сюжетов."
        cs_narrator "Женя неожиданно рассмеялась. Негромко. Совсем недолго. Но совершенно искренне."
        cs_narrator "Я посмотрела на неё."
        cs_th "Вот ведь. Оказывается, Женю не обязательно постоянно поддевать, чтобы услышать, как она смеётся. Достаточно просто найти тему, которая ей интересна."
        cs_narrator "И эта мысль показалась гораздо приятнее, чем любая удачная шутка."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А ты вообще всегда читаешь во время еды?"
    cs_narrator "Женя посмотрела на книгу."
    cs_mz "Не всегда. Только когда вокруг слишком шумно."
    cs_ls "То есть книга используется как средство индивидуальной защиты?"
    cs_narrator "Женя поправила очки."
    cs_mz "От некоторых людей — определённо."
    cs_ls "Надо будет взять на вооружение."
    cs_narrator "Дарья усмехнулась."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты сама чаще всех разговариваешь."
    cs_ls "Именно. Значит, защита нужна окружающим."
    cs_narrator "Женя покачала головой. Но теперь уже улыбалась."
    return
