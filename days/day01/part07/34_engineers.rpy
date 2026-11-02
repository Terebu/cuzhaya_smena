# -*- coding: utf-8 -*-
label cs_day01_34:
    $ save_name = "Чужая смена — День 1: Товарищи инженеры"
    # cs_composition: regroup
    # cs_composition: regroup
    show sh normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show el normal pioneer far at cs_actor_far_right
    # cs_composition: regroup
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    with None
    label cs_check_day01_part07_engineers:
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/smooth_machine.ogg" fadeout 2.0 fadein 2.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sh", "el", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "За столом сидел Шурик и рассматривал деталь. Электроник что-то ему объяснял. Оба повернулись."
    cs_narrator "Я остановилась у порога, поправила галстук."
    cs_ls "Добрый день, товарищи инженеры."
    cs_narrator "Электроник моргнул."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Э-э… привет."
    cs_narrator "Шурик отложил деталь."
    show sh normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Вы к кому?"
    cs_ls "Лена Соколова."
    cs_narrator "Я указала на Дарью."
    cs_ls "А это Даша."
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Дарья."
    cs_narrator "Электроник улыбнулся."
    cs_el "Я Сергей. Но все зовут Электроником."
    cs_sh "А я Шурик."
    cs_th "Какая неожиданность."
    cs_ls "Очень приятно."
    cs_narrator "Шурик посмотрел на нас внимательнее."
    cs_sh "Вы новенькие?"
    cs_ls "Совершенно верно. Прибыли сегодня."
    cs_narrator "Электроник сразу оживился."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "А записаться в кружок хотите?"
    # cs_director_begin: REFLECTIVE_SHOT: Electronics workbench focus
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_1f82f2504d:
    # cs_director_end
    cs_narrator "На столе лежали провода, инструменты, платы и недособранные устройства."
    cs_narrator "Вот это интересно: можно посмотреть маркировку, измерить напряжение. Может, даже заставить что-нибудь работать."
    # cs_director_begin: Return to direct interaction: Electronics workbench focus
    $ cs_frame_focus(["sh", "el", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_4fcbe05cb6:
    # cs_director_end
    cs_ls "Пока скорее за консультацией."
    cs_narrator "Шурик приподнял бровь."
    cs_sh "По какому вопросу?"
    cs_narrator "Я подошла к столу."
    cs_ls "Для начала хочу отметить, что здесь весьма прилично оборудовано."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник довольно улыбнулся."
    cs_el "Мы стараемся!"
    cs_narrator "Я оглядела инструменты, паяльник, блок питания в углу."
    cs_ls "Даже лаборатория почти полноценная."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "А ты разбираешься в электронике?"
    cs_ls "На уровне человека, который понимает, что телефон нельзя подключать напрямую к розетке."
    show sh smile pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Шурик усмехнулся."
    show sh normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Уже неплохо."
    cs_ls "Спасибо. Родители были бы мной горды."
    cs_narrator "Дарья тихо добавила:"
    cs_da "Особенно если вспомнить, зачем мы сюда пришли."
    cs_ls "Не мешай научному процессу."
    cs_da "Я пока только наблюдаю."
    show el laugh pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник рассмеялся."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Так что у вас случилось?"
    cs_narrator "Пора переходить к делу."
    return
