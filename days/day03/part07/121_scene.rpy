# -*- coding: utf-8 -*-
label cs_day03_121:
    $ save_name = "Чужая смена — День 3: Обед без обязательной культурной программы"
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    $ cs_day03_part07_book_promised_before = cs_mz_book_requested_day3
    cs_narrator "У входа Ольга Дмитриевна на минуту остановила Дашу. Та махнула нам: идите, догоню."
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.12,delay=1.0,channel="music")
    label cs_check_day03_121_queue:
    cs_narrator "Мы с Женей направились к раздаче."
    cs_narrator "Очередь двигалась не особенно быстро, но и торопиться было некуда."
    cs_narrator "Я взяла поднос."
    cs_narrator "Посмотрела на Женю."
    cs_narrator "Потом на людей впереди."
    cs_narrator "И спокойно осталась стоять рядом."
    cs_th "Надо же."
    cs_th "Ещё два дня назад я бы непременно начала комментировать организацию общественного питания."
    cs_th "Сегодня, кажется, мне вполне достаточно того, что здесь вообще кормят."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя поправила очки."
    cs_narrator "Я заметила, что она всё ещё держит книгу под мышкой."
    cs_ls "Женя."
    cs_narrator "Она повернулась."
    cs_mz "Что?"
    cs_ls "Ты после обеда будешь в библиотеке?"
    cs_mz "А где ещё?"
    cs_narrator "Я задумалась."
    cs_ls "Справедливо. Не учла профессиональную специфику."
    cs_narrator "Она слегка усмехнулась."
    cs_mz "Тебе что-то нужно?"
    cs_narrator "Я кивнула."
    cs_ls "Хотела снова зайти почитать. Если можно."
    if cs_friend_mz >= 2:
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Я так и подумала."
        cs_narrator "Я приподняла бровь."
        cs_ls "Настолько предсказуема?"
        cs_mz "В этом отношении — да."
        cs_narrator "Она немного помолчала."
        if cs_mz_day3_book_awarded:
            cs_mz "Я уже отложила пару книг. Утром мы говорили об историях, где важнее люди и их решения. Помнишь?"
        else:
            cs_mz "Я уже отложила пару книг. Подумала, тебе могут подойти истории про людей и их решения."
        $ cs_mz_book_prepared_day3 = True
        cs_narrator "Я удивилась."
        cs_ls "Ты запомнила?"
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя поправила очки."
        cs_mz "У меня с памятью всё нормально, Соколова."
        cs_narrator "Я тихо рассмеялась."
        cs_ls "Не сомневалась."
        cs_narrator "Немного помолчала."
        cs_ls "Спасибо, что подумала об этом."
        cs_narrator "Она кивнула."
        cs_mz "Посмотришь после обеда."
    elif cs_friend_mz >= 1:
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя слегка улыбнулась."
        if cs_lena_book_returned:
            cs_mz "Вчерашнюю книгу ты уже вернула. Хочешь ещё что-нибудь?"
        else:
            cs_mz "Хочешь ещё что-нибудь посмотреть?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Хотела попробовать что-нибудь ещё."
        cs_mz "Тогда приходи. Посмотрим, что есть."
        cs_ls "Хорошо."
    else:
        cs_narrator "Женя кивнула."
        cs_mz "Приходи. Только не мешай посетителям."
        cs_narrator "Я улыбнулась."
        cs_ls "Договорились."
        cs_mz "И книги возвращай на места."
        cs_ls "Это уже звучит как чрезвычайно серьёзное предупреждение."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya arms_crossed pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Она посмотрела на меня поверх очков."
        cs_mz "Потому что оно серьёзное."
        cs_narrator "Я кивнула."
        cs_ls "Принято."
    cs_narrator "Очередь немного продвинулась."
    cs_narrator "Я посмотрела на свободные места у окон."
    cs_narrator "Потом снова на Женю."
    cs_ls "Много сегодня народу в библиотеке было?"
    cs_narrator "Она задумалась."
    cs_mz "Не очень. Шурик приходил за справочником. Мику ненадолго заглядывала. Ещё несколько человек брали книги."
    cs_ls "Значит, спокойно."
    cs_mz "В основном."
    cs_narrator "Пауза."
    cs_narrator "Она посмотрела на меня."
    cs_mz "Пока ты не пришла."
    cs_narrator "Я медленно повернула голову."
    cs_th "Ого."
    cs_th "Прекрасно."
    cs_th "Уважаемый сотрудник библиотеки начинает осваивать наступательную тактику."
    cs_ls "Очень неприятно слышать подобное от представителя культурного учреждения."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя слегка улыбнулась."
    cs_mz "Зато честно."
    cs_narrator "Я кивнула."
    cs_ls "Тут не поспоришь."
    cs_narrator "Мы снова замолчали."
    cs_narrator "И тишина между нами не требовала никаких объяснений."
    $ cs_mz_book_requested_day3 = True
    $ cs_day03_library_visit_time = "after_lunch"
    return
