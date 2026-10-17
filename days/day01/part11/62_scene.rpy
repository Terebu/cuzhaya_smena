# -*- coding: utf-8 -*-
label cs_day01_62:
    $ save_name = "Чужая смена — День 1: Дорога к домику"
    label cs_check_d1_s62:
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.0 fadein 1.0
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "По дороге мы почти не разговаривали. Из одного домика доносилось радио; возле другого кто-то вытряхивал полотенце. Лагерь готовился ко сну с такой уверенностью, будто сегодняшний день не мог закончиться ничем другим."
    cs_narrator "По дороге мы заглянули к Ольге Дмитриевне и забрали оставленные у неё зимние куртки и сапоги. До нашего домика вещи донесли вместе."
    cs_narrator "Нести зимние вещи было неудобно: рукава цеплялись за сапоги, и я всё время меняла хват. Даша молча забрала у меня одну куртку."
    cs_ls "Наша первая лагерная коллекция одежды не очень подходит к сезону."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Зато легко понять, где наши вещи."
    cs_narrator "Мы обошли лужицу у колонки. Я впервые заметила, что Даша тоже смотрит под ноги и выбирает дорогу сама, а не просто идёт следом за мной."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне кажется, Жене было неприятно."
    cs_ls "Про игру?"
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да. Особенно когда она спросила, много ли ты о ней знаешь."
    cs_narrator "Я посмотрела под ноги."
    cs_ls "Мне бы тоже было неприятно."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты потом хорошо ответила."
    cs_ls "Лучше бы сначала хорошо подумала."
    cs_narrator "Даша не стала спорить. Мы прошли несколько шагов, и она добавила:"
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Завтра я хочу иногда сама задавать вопросы."
    cs_narrator "Я повернулась к ней."
    cs_ls "Я мешаю?"
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Иногда ты успеваешь спросить, ответить и сделать вывод раньше, чем я открываю рот."
    cs_narrator "С этим спорить было трудно."
    cs_ls "Принято. Постараюсь оставлять воздух."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Просто дай мне договорить."
    $ night_time()
    $ persistent.sprite_time = "night"
    $ cs_director_scene("cs_house_lena_darya_ext_night")
    scene cs_house_lena_darya_ext_night
    with Dissolve(1.0)
    play ambience "sound/ambiences/camp_center_night.ogg" fadeout 1.0 fadein 1.0
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "У нашего крыльца я придержала дверь. Дарья прошла внутрь и на ходу поблагодарила меня."
    cs_narrator "Обычное движение. Обычное слово. Почему-то именно сейчас мне стало немного спокойнее."
    return
