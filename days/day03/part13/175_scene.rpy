# -*- coding: utf-8 -*-
label cs_day03_175:
    $ save_name = "Чужая смена — День 3: Прощание без торжественных речей"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Я повернулась к Жене."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Тогда пойду."
    cs_narrator "Она кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Давай. И локоть береги."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Кажется, весь лагерь заключил соглашение о постоянном наблюдении за моей рукой."
    cs_narrator "Женя усмехнулась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Может, тогда наконец начнёшь слушаться?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Есть определённые успехи."
    cs_narrator "Она посмотрела на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Вижу."
    cs_narrator "Я улыбнулась."
    cs_narrator "Сделала несколько шагов к двери."
    cs_narrator "Потом остановилась."
    cs_narrator "Обернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Женя."
    cs_narrator "Она подняла взгляд."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Что?"
    cs_narrator "Я немного помолчала."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Правда спасибо за сегодня."
    cs_narrator "Женя посмотрела на меня внимательнее."
    if cs_mz_hug_allowed_day3:
        cs_narrator "Она едва заметно улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Ты уже благодарила."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Знаю."
        cs_narrator "Она посмотрела на меня."
        cs_narrator "Потом усмехнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "И обнимала тоже."
        cs_narrator "Я немного смутилась."
        cs_narrator "Потом улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Это ты тоже запомнила?"
        cs_narrator "Женя поправила очки."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "У меня хорошая память, Соколова."
        cs_narrator "Я тихо рассмеялась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Тогда не буду повторяться."
        cs_narrator "Она кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Вот и правильно."
        cs_narrator "Но через секунду добавила мягче:"
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Мне тоже понравилось сегодня с тобой разговаривать."
        cs_narrator "Я замерла."
        cs_th "О."
        cs_th "А вот это уже действительно приятно."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Тогда до завтра."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "До завтра."
    elif cs_friend_mz >= 3 and cs_mz_hug_allowed_day3 == False:
        cs_narrator "Я немного помолчала."
        cs_narrator "Потом осторожно спросила:"
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Можно тебя обнять на прощание?"
        cs_narrator "Женя удивлённо посмотрела на меня."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Неожиданный вопрос."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Поэтому и спрашиваю."
        cs_narrator "Она немного подумала."
        cs_narrator "Потом кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Ладно. Только недолго."
        cs_narrator "Я подошла."
        cs_narrator "Осторожно обняла её здоровой рукой."
        cs_narrator "Без попытки удержать."
        cs_narrator "Без шуточных комментариев."
        cs_narrator "Всего на пару секунд."
        $ cs_mz_hug_allowed_day3 = True
        label cs_check_day03_175_first_hug:
        cs_narrator "И сама отпустила."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Спасибо."
        cs_narrator "Женя поправила очки."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Пожалуйста."
        cs_narrator "Потом добавила:"
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Только не делай из этого лагерную традицию."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Не буду."
        cs_narrator "Она едва заметно улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Тогда до завтра."
    else:
        cs_narrator "Женя кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Не за что. Хорошего вечера."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "И тебе."
    cs_narrator "Я подошла к двери."
    cs_narrator "Положила руку на ручку."
    cs_narrator "Потом обернулась ещё раз."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "До завтра, Женя."
    cs_narrator "Она посмотрела на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "До завтра, Лена."
    cs_narrator "Я открыла дверь."
    cs_narrator "Вышла наружу."
    $ cs_director_scene("cs_library_exterior_night")
    scene cs_library_exterior_night
    $ cs_frame_focus([])
    with Dissolve(0.7)
    play sound "sound/sfx/close_door_1.ogg"
    cs_narrator "И осторожно закрыла её за собой."
    cs_narrator "Ночной воздух оказался прохладным."
    cs_narrator "Я остановилась на крыльце."
    cs_narrator "Глубоко вдохнула."
    cs_narrator "Посмотрела на освещённую фонарём дорожку."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Ну вот."
    cs_th "Третий день."
    cs_th "Книга дочитана."
    cs_th "Женя не выгнала."
    if cs_friend_mz >= 2:
        cs_th "Более того, кажется, завтра меня там снова будут рады видеть."
    else:
        cs_th "Завтра сюда опять можно будет прийти за книгой."
    cs_narrator "Я улыбнулась."
    cs_th "Пожалуй, неплохой результат."
    return
