# -*- coding: utf-8 -*-
label cs_day02_70:
    $ save_name = "Чужая смена — День 2: После музыки"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    $ night_time()
    $ persistent.sprite_time = "night"
    $ cs_director_scene("bg ext_square_night")
    scene bg ext_square_night
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    stop cs_piano fadeout 3.0
    play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0
    $ renpy.music.set_volume(0.12, channel="music")
    play ambience "sound/ambiences/camp_center_night.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.10, channel="ambience")
    label cs_check_finale_70:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После выступления площадь ещё некоторое время оставалась оживлённой."
    cs_narrator "Пионеры обсуждали услышанное."
    cs_narrator "Кто-то помогал убирать стулья."
    cs_narrator "Возле музыкальной площадки разговаривали Мику и Алиса."
    cs_narrator "А я стояла рядом с Дарьей и пыталась вспомнить, когда в последний раз так внимательно слушала музыку."
    cs_narrator "Без телефона в руке."
    cs_narrator "Без желания немедленно что-нибудь записать."
    cs_narrator "Без мысли о том, что потом обязательно нужно будет поделиться впечатлениями с подписчиками."
    cs_narrator "Просто слушала."
    cs_narrator "И это оказалось удивительно приятно."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну как тебе?"
    cs_narrator "Я повернулась."
    cs_ls "Очень понравилось."
    cs_narrator "Она улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне тоже."
    cs_narrator "Я посмотрела на сцену."
    cs_narrator "Потом на неё."
    cs_ls "Забавно. Утром мы ещё видели, как Мику разбиралась с отдельными кусочками мелодии."
    if cs_mi_intro_revised == True:
        cs_narrator "Дарья кивнула."
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "И ведь она действительно изменила вступление."
        cs_narrator "Я улыбнулась."
        cs_ls "Ага. Получилось хорошо."
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Думаю, она сама это почувствовала."
        cs_narrator "Я посмотрела на Мику."
        cs_narrator "Та оживлённо рассказывала что-то Алисе."
        cs_th "Возможно."
        cs_th "И, пожалуй, именно это было самое приятное: увидеть, как маленькая утренняя репетиция превратилась в настоящий вечерний концерт."
    else:
        cs_narrator "Дарья задумалась."
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Интересно, сколько они репетировали перед выступлением?"
        cs_narrator "Я пожала плечами."
        cs_ls "Судя по результату, достаточно."
        cs_narrator "Она улыбнулась."
    cs_narrator "Дарья посмотрела в сторону домиков."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я, наверное, пойду. Устала за сегодня."
    cs_narrator "Я кивнула."
    cs_ls "Конечно. Я немного постою и тоже приду."
    cs_narrator "Она посмотрела на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только без дополнительных приключений."
    cs_narrator "Я улыбнулась."
    cs_ls "Сегодня мой лимит приключений исчерпан."
    cs_narrator "Дарья негромко рассмеялась."
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда увидимся дома."
    # Presence rule: keep Darya until the next location, per user request.
    cs_narrator "Она направилась к нашему домику."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_darya"])
    with cs_sprite_leave
    label cs_director_check_c7fd37f7e0:
    # cs_director_end
    cs_narrator "Я ещё несколько минут постояла возле площади."
    cs_narrator "Посмотрела на опустевшие скамейки."
    cs_narrator "На темнеющие деревья."
    cs_narrator "На звёзды, постепенно появлявшиеся над лагерем."
    cs_th "Ну что ж."
    cs_th "День действительно заканчивается."
    cs_th "И впервые за всё время здесь я даже не пытаюсь придумать новую проверку."
    cs_th "Возможно, на сегодня достаточно."
    cs_narrator "Я направилась домой."
    return
