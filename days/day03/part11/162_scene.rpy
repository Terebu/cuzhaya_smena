# -*- coding: utf-8 -*-
label cs_day03_162:
    $ save_name = "Чужая смена — День 3: Тихая победа"
    $ cs_day03_darya_destination = "home"
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "Мы шли неторопливо."
    cs_narrator "Вечерний лагерь постепенно становился тише."
    cs_narrator "Пионеры расходились по домикам."
    cs_narrator "У клубов ещё слышались голоса."
    cs_narrator "Где-то вдалеке смеялись."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она заметила."
    cs_da "Что?"
    cs_narrator "Я улыбнулась."
    cs_ls "Думаю, что сегодня хорошо получилось."
    cs_da "Что именно?"
    cs_narrator "Я немного задумалась."
    cs_ls "Общаться."
    cs_narrator "Она приподняла бровь."
    cs_da "Ты же и раньше умела."
    cs_narrator "Я кивнула."
    cs_ls "Умела. Только иногда слишком увлекалась."
    cs_narrator "Она улыбнулась."
    cs_da "Это мягко сказано."
    cs_narrator "Я вздохнула."
    cs_ls "Спасибо за поддержку."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Мы прошли ещё немного."
    cs_narrator "Потом она тихо спросила:"
    cs_da "А тебе правда нравится Женя?"
    cs_narrator "Я повернулась."
    cs_ls "Конечно."
    cs_narrator "Она немного улыбнулась."
    cs_da "Как человек?"
    cs_narrator "Я задумалась."
    cs_ls "Да. Мне нравится, что с ней не нужно постоянно разговаривать."
    cs_narrator "Пауза."
    cs_ls "И что она не пытается изображать кого-то другого. Если ей что-то не нравится, она так и скажет."
    cs_narrator "Дарья кивнула."
    cs_da "Это удобно."
    cs_narrator "Я улыбнулась."
    cs_ls "Очень. Хотя иногда весьма болезненно для моего самолюбия."
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "А мне нравится, что ты сегодня несколько раз сама останавливалась."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на неё."
    cs_ls "В каком смысле?"
    cs_narrator "Она немного подумала."
    cs_da "Ну, раньше ты бы обязательно пошутила ещё раз. Потом ещё. Даже когда было понятно, что человеку уже достаточно."
    cs_narrator "Я кивнула."
    cs_da "А сегодня как-то иначе."
    cs_narrator "Я задумалась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Наверное, она права."
    cs_th "Просто за эти дни я уже успела понять, что не обязательно проверять терпение человека до самого предела."
    cs_th "Иногда лучше оставить хорошую шутку единственной."
    cs_th "А иногда — вообще ничего не говорить."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Зато теперь, когда я всё-таки шучу, эффект получается лучше."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Вот! Опять."
    cs_narrator "Я кивнула."
    cs_ls "Конечно. Ты же не думала, что я превращусь в образцовую советскую женщину за три дня?"
    cs_narrator "Она покачала головой."
    cs_da "Нет. На такое даже я не рассчитываю."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Медленно прищурилась."
    cs_ls "Дарья Еретикова. Я начинаю подозревать, что ты сегодня слишком много времени провела с Алисой."
    cs_narrator "Она засмеялась."
    cs_da "Может быть."
    cs_narrator "Я кивнула."
    cs_ls "Влияние заметно. Сарказм начал передаваться воздушно-капельным путём."
    cs_narrator "Она снова рассмеялась."
    cs_narrator "Я тоже улыбнулась."
    cs_narrator "Мы продолжили идти рядом."
    cs_narrator "И вдруг я поймала себя на простой мысли."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Мне действительно нравится этот лагерь."
    cs_th "Не всё, конечно."
    cs_th "Я по-прежнему хочу домой."
    cs_th "Хочу снова увидеть свою комнату."
    cs_th "Включить компьютер."
    cs_th "Сесть за привычный графический планшет."
    cs_th "И хотя бы раз проснуться утром без горна."
    cs_narrator "Но теперь здесь были люди, которых мне хотелось увидеть завтра."
    cs_narrator "Женя."
    cs_narrator "Мику."
    cs_narrator "Алиса."
    cs_narrator "Славя."
    cs_narrator "Тихонова."
    cs_narrator "Семён."
    cs_narrator "И Даша, которая шла рядом."
    cs_th "Странная компания."
    cs_th "Очень странная."
    cs_th "Но уже не чужая."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она улыбнулась."
    cs_da "Лен?"
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_da "Пойдём в домик?"
    cs_narrator "Я кивнула."
    cs_ls "Пойдём."
    cs_narrator "Потом задумалась."
    cs_ls "Только сначала предупреждаю."
    cs_narrator "Она приподняла бровь."
    cs_da "О чём?"
    cs_narrator "Я посмотрела куда-то вдаль."
    cs_narrator "И совершенно серьёзно произнесла:"
    cs_ls "Дома меня ждёт мужчина."
    cs_narrator "Дарья остановилась."
    cs_narrator "Медленно посмотрела на меня."
    cs_narrator "Потом на домики."
    cs_da "Какой ещё мужчина?"
    cs_narrator "Я выдержала паузу."
    cs_ls "Иван Александрович Гончаров."
    cs_narrator "Она закрыла лицо ладонью."
    cs_da "Лена…"
    cs_narrator "Я кивнула."
    cs_ls "Наши отношения с русской литературой ещё не закончены."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я тоже."
    $ cs_director_scene("cs_house_lena_darya_ext_sunset")
    scene cs_house_lena_darya_ext_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "И мы направились к нашему домику."
    cs_th "Вот теперь вечер действительно можно считать удачным."
    return
