# -*- coding: utf-8 -*-
label cs_day03_170:
    $ save_name = "Чужая смена — День 3: Соколова и литературная тишина"
    $ cs_pov_end()
    with cs_sprite_change
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_narrator "Я читала, а Женя изредка поглядывала на меня поверх журнала."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Наверное, привыкает к посетительнице, которая не начинает разговор после каждой страницы."
    cs_narrator "Я перевернула страницу. Потом остановилась. Посмотрела на Женю."
    $ cs_pov_end()
    with cs_sprite_change
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_ls "Слушай."
    cs_narrator "Она подняла голову."
    cs_mz "Что?"
    cs_narrator "Я немного улыбнулась."
    cs_ls "А тебе не мешает, что я здесь сижу?"
    cs_narrator "Женя посмотрела на меня, потом на книгу."
    if cs_mz_open_library_invitation_day3:
        cs_mz "Соколова, мы вроде уже обсуждали этот вопрос."
        cs_ls "Да. Было дело."
        cs_narrator "Она приподняла бровь."
        cs_mz "Я сама сказала, что можешь приходить."
        cs_ls "Уточняю, вдруг ты уже передумала."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Не изменилось."
        cs_narrator "Пауза."
        cs_mz "Пока ты не разговариваешь без остановки."
        cs_ls "Значит, всё хорошо."
        cs_narrator "Она улыбнулась."
        cs_mz "Да."
    elif cs_friend_mz >= 2:
        cs_narrator "Женя пожала плечами."
        cs_mz "Нет. Ты читаешь спокойно."
        cs_ls "Хорошо."
        cs_narrator "Она чуть усмехнулась."
        cs_mz "А чего спрашиваешь?"
        cs_ls "Просто не хочу задерживать тебя после работы."
        cs_narrator "Она посмотрела на часы."
        cs_mz "Когда буду закрывать, скажу."
        cs_ls "Договорились."
    else:
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Пока не мешаешь. Читай."
        cs_ls "Конечно. Тогда ещё несколько страниц и пойду."
        cs_narrator "Она вернулась к журналу."
    cs_narrator "Я снова открыла книгу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "И через некоторое время поймала себя на странной мысли."
    cs_th "За этот день мы успели поговорить обо всём на свете. А сейчас мне было хорошо просто читать."
    cs_narrator "Я посмотрела на страницу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Я всё ещё хотела понять, как устроен лагерь и как вернуться домой."
    cs_narrator "Я чуть улыбнулась."
    cs_th "Кажется, именно так и происходит привыкание. Не когда перестаёшь замечать странности. А когда среди них появляются знакомые мелочи."
    $ cs_pov_end()
    with cs_sprite_change
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_narrator "Женя закрыла журнал. Я услышала негромкий звук. Подняла голову. Она посмотрела на часы."
    cs_mz "Лена."
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_mz "Скоро закрываю."
    cs_ls "Хорошо. Уже заканчиваю главу."
    cs_narrator "Она посмотрела на мою книгу."
    cs_mz "Ты ведь не собираешься дочитать её сегодня целиком?"
    cs_ls "Нет. До конца ещё далеко, а читать наспех не хочется."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Вот и правильно. Книга никуда не денется."
    cs_ls "Надеюсь. А то будет обидно, если завтра она решит уехать без меня."
    cs_narrator "Она посмотрела на меня поверх очков."
    cs_mz "Соколова."
    cs_ls "Всё. Последняя литературная шутка на сегодня."
    cs_narrator "Женя покачала головой. Но улыбалась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я снова посмотрела на страницу. И вдруг поняла, что сегодня мне действительно хорошо. Не потому, что удалось кого-то рассмешить. Не потому, что я снова добралась до книги."
    cs_narrator "И даже не потому, что начала привыкать к лагерю. Просто у меня появилось место, куда хотелось возвращаться."
    cs_th "И человек, с которым там было спокойно."
    cs_narrator "Я перевернула страницу. За окном становилось темнее. Где-то далеко, на площади, Семён, наверное, уже закончил своё совещание со Славей. Возможно, даже успел забыть мою небольшую постановку."
    cs_th "Хотя зная его…"
    cs_narrator "Я едва заметно улыбнулась."
    cs_th "Нет."
    cs_th "Не буду продолжать. Сегодня и так достаточно."
    cs_narrator "Женя снова опустила взгляд к записям. Я продолжила читать. И библиотека вернулась к привычной тишине."
    return
