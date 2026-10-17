# -*- coding: utf-8 -*-
label cs_day02_59:
    $ save_name = "Чужая смена — День 2: До вечера"
    $ cs_part07_live = False
    $ cs_part08_live = True
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
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part08_s59:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Семён поднялся с лавочки."
    cs_narrator "Убрал карандаш в карман."
    cs_sy "Ладно, мне ещё нужно зайти в клубы. Шурик попросил кое-что передать."
    cs_narrator "Я кивнула."
    cs_ls "Только осторожнее. Там сейчас разрабатывают технологии двадцать первого века."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он усмехнулся."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "До работающего телефона ещё далеко?"
    cs_narrator "Я посмотрела на собственный карман."
    cs_ls "Судя по сегодняшним результатам, да."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ну, может, позже получится."
    cs_narrator "Я кивнула."
    cs_ls "Будем надеяться."
    cs_narrator "Он посмотрел на Дарью."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А вы куда?"
    cs_narrator "Она ненадолго задумалась."
    cs_da "Думаю, просто немного погуляем. Лене сегодня лучше отдохнуть."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Подтверждаю. Пациентке рекомендован щадящий режим эксплуатации."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Семён рассмеялся."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Тогда до ужина?"
    cs_da "Увидимся."
    cs_ls "До вечера, товарищ Семён."
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
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part08_semen_left:
    cs_narrator "Он махнул рукой и направился к клубам."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_director_check_76550c8595:
    # cs_director_end
    cs_narrator "Я проводила его взглядом."
    cs_narrator "И вдруг подумала, что ещё вчера совершенно не представляла, как мы будем общаться."
    cs_narrator "Слишком многое знала о нём заранее."
    cs_narrator "И слишком многое оказалось совершенно не таким, как я ожидала."
    cs_narrator "Он шутил."
    cs_narrator "Уставал."
    cs_narrator "Переживал."
    cs_narrator "Иногда злился."
    cs_narrator "И, как выяснилось сегодня, умел самостоятельно превращать мои же шутки в оружие против меня."
    cs_th "Неплохой результат."
    cs_th "Для двух дней знакомства."
    cs_narrator "Дарья подошла ближе."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну что, куда теперь?"
    cs_narrator "Я посмотрела вокруг."
    cs_narrator "На столовую."
    cs_narrator "На дорожку к библиотеке."
    cs_narrator "На клубы."
    cs_narrator "На площадь, где вечером должны были выступать Мику и Алиса."
    cs_narrator "Затем на собственную руку."
    cs_ls "Знаешь, впервые за сегодня я действительно не хочу никуда торопиться."
    cs_narrator "Она улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Невероятно."
    cs_ls "Вот и я удивлена."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
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
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part08_walk:
    cs_narrator "Мы пошли по дорожке."
    cs_narrator "Не особенно быстро."
    cs_narrator "Я старалась смотреть под ноги."
    cs_narrator "Дарья это заметила."
    cs_narrator "И довольно улыбнулась."
    cs_da "Всё-таки научилась."
    cs_narrator "Я повернулась к ней."
    cs_ls "Да. Современные методы обучения иногда бывают довольно болезненными."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я тоже улыбнулась."
    cs_narrator "Некоторое время мы шли молча."
    cs_narrator "Потом я спросила:"
    cs_ls "А ты хочешь вечером послушать выступление?"
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Конечно. Мы ведь утром были у Мику. Интересно, что у неё получилось."
    cs_narrator "Я кивнула."
    cs_ls "Тогда пойдём вместе."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась чуть заметнее."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я и не собиралась идти без тебя."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "На этот раз не стала немедленно придумывать ответную шутку."
    cs_narrator "Просто улыбнулась."
    cs_th "Надо же."
    cs_th "Иногда действительно достаточно нескольких слов."
    # cs_director_begin: REFLECTIVE_SHOT: Evening panorama and people beyond the game
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_2d636a7bba:
    # cs_director_end
    cs_narrator "Впереди снова показалась знакомая дорожка."
    cs_narrator "Где-то в лагере готовились к ужину."
    cs_narrator "Кто-то переносил стулья."
    cs_narrator "Кто-то репетировал."
    cs_narrator "Кто-то, наверное, уже обсуждал, каким будет вечер."
    cs_narrator "А мы просто шли рядом."
    cs_narrator "И это было удивительно хорошо."
    cs_th "После сегодняшней дороги мне хотелось хотя бы несколько часов провести без новых открытий."
    cs_th "После падения — без новых происшествий."
    cs_th "А после разговора с Семёном я неожиданно поняла, что начинаю привыкать к людям вокруг."
    cs_narrator "Не к персонажам."
    cs_narrator "Не к знакомым изображениям."
    cs_narrator "К людям."
    cs_narrator "И, пожалуй, именно это было самым необычным открытием дня."
    stop music fadeout 3.0
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    $ cs_day02_part08_complete = True
    label cs_check_part08_ready:
    pause 0.5
    return
