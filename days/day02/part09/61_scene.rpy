# -*- coding: utf-8 -*-
label cs_day02_61:
    $ save_name = "Чужая смена — День 2: Человек с книгой"
    $ cs_part08_live = False
    $ cs_part09_live = True
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part09_s61:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Возле столовой уже собирались пионеры."
    cs_narrator "Кто-то торопился занять место."
    cs_narrator "Кто-то продолжал разговор на крыльце."
    cs_narrator "А несколько девочек стояли чуть поодаль, споря о том, кто будет сидеть ближе к музыкальному выступлению."
    cs_narrator "Я невольно улыбнулась."
    cs_th "Вечер ещё не начался, а подготовка уже идёт полным ходом."
    cs_narrator "Мы поднялись по ступенькам."
    cs_narrator "И почти сразу я увидела знакомую фигуру."
    cs_narrator "Тёмные волосы."
    cs_narrator "Очки."
    cs_narrator "Книга под мышкой."
    cs_narrator "Выражение лица человека, который предпочёл бы сейчас находиться где-нибудь в тишине."
    cs_th "Женя."
    cs_narrator "Я замедлила шаг."
    cs_narrator "Дарья тоже посмотрела в её сторону."
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Видишь?"
    cs_narrator "Я кивнула."
    cs_ls "Вижу."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только давай без нового заседания библиотечной комиссии."
    cs_narrator "Я посмотрела на неё с самым серьёзным выражением лица."
    cs_ls "Сегодня я исключительно законопослушная гражданка."
    cs_narrator "Дарья посмотрела на перевязанный локоть."
    cs_da "Которая уже дважды посетила медпункт."
    cs_ls "Одно другому не противоречит."
    cs_narrator "Она усмехнулась."
    cs_narrator "Мы подошли ближе."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part09_zhenya_greeting:
    cs_narrator "Женя подняла взгляд от книги."
    if cs_friend_mz >= 2:
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "А, Соколова. Я тебя как раз хотела увидеть."
        cs_narrator "Я остановилась."
        cs_th "О."
        cs_th "Вот это уже неожиданно."
        cs_ls "Меня?"
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Нет, твою повязку. Конечно, тебя."
        cs_narrator "Я медленно улыбнулась."
        cs_ls "Какая тёплая встреча."
        cs_narrator "Женя закатила глаза."
        cs_narrator "Но уголки губ слегка дрогнули."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Только не начинай."
    elif cs_friend_mz >= 1:
        cs_narrator "Женя узнала нас и слегка кивнула."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya thinking pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Привет. Опять куда-то торопитесь?"
        cs_ls "На ужин. Сегодня исключительно мирные намерения."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Звучит подозрительно."
        cs_narrator "Я улыбнулась."
        cs_ls "Твоё доверие меня вдохновляет."
    else:
        cs_narrator "Женя мельком посмотрела на нас."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Привет."
        cs_ls "Привет."
        cs_narrator "Я невольно посмотрела на книгу под её мышкой."
        cs_th "Похоже, библиотечная деятельность продолжается даже после закрытия рабочего дня."
        cs_narrator "Женя уже собиралась вернуться к чтению, поэтому я не стала задерживать её ненужными вопросами."
    if cs_mz_quiet_visit_seen:
        cs_narrator "Женя посмотрела на повязку и снова напомнила беречь локоть."
        cs_ls "Помню. Смотрю под ноги."
    else:
        cs_narrator "Затем Женя заметила мой локоть."
        cs_narrator "Посмотрела на повязку."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya thinking pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "А это что?"
        cs_narrator "Я подняла руку."
        cs_ls "Результат исследования местной дорожной инфраструктуры."
        cs_narrator "Женя нахмурилась."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya thinking pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Чего?"
        cs_da "Лена споткнулась о корень и упала."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "А."
        cs_narrator "Она снова посмотрела на меня."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Тогда понятно."
        cs_narrator "Я возмущённо подняла здоровую руку."
        cs_ls "Почему всем сразу становится понятно?!"
        cs_narrator "Женя поправила очки."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya explaining pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Потому что ты вчера успела устроить достаточно шума в библиотеке, чтобы я примерно представляла твою способность находить неприятности."
        cs_narrator "Дарья негромко рассмеялась."
        cs_narrator "Я медленно повернулась к ней."
        cs_ls "Вижу, против меня снова формируется коалиция."
        cs_da "Никто не виноват, что вы обе пришли к одинаковым выводам."
        cs_narrator "Женя усмехнулась."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
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
        show cs_zhenya normal pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Просто в следующий раз смотри под ноги."
        cs_narrator "Я вздохнула."
        cs_ls "Этот совет сегодня популярнее любой музыкальной композиции."
    cs_narrator "Изнутри столовой донёсся голос, приглашавший проходить к раздаче."
    cs_narrator "Женя закрыла книгу."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ладно, идём. А то потом в очереди застрянем."
    cs_narrator "Мы направились внутрь."
    return
