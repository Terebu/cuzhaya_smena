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
    cs_narrator "Я читала уже некоторое время, когда заметила, что Женя периодически поглядывает в мою сторону."
    cs_narrator "Не пристально."
    cs_narrator "Не так, будто следит за каждым движением."
    cs_narrator "Просто иногда поднимает глаза от журнала."
    cs_narrator "Смотрит на меня."
    cs_narrator "И возвращается к работе."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Интересно."
    cs_th "Неужели я действительно настолько необычный посетитель?"
    cs_th "Хотя, если вспомнить мои первые появления в библиотеке…"
    cs_th "Вопрос, пожалуй, снимается."
    cs_narrator "Я перевернула страницу."
    cs_narrator "Потом остановилась."
    cs_narrator "Посмотрела на Женю."
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
    cs_narrator "Женя посмотрела на меня."
    cs_narrator "Потом на книгу."
    if cs_mz_open_library_invitation_day3:
        cs_mz "Соколова, мы вроде уже обсуждали этот вопрос."
        cs_narrator "Я задумалась."
        cs_ls "Да. Было дело."
        cs_narrator "Она чуть приподняла бровь."
        cs_mz "Я сама сказала, что можешь приходить."
        cs_narrator "Я улыбнулась."
        cs_ls "Просто уточняю, не изменилось ли официальное постановление."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Не изменилось."
        cs_narrator "Пауза."
        cs_mz "Пока ты не разговариваешь без остановки."
        cs_narrator "Я кивнула."
        cs_ls "Значит, всё хорошо."
        cs_narrator "Она слегка улыбнулась."
        cs_mz "Да."
    elif cs_friend_mz >= 2:
        cs_narrator "Женя пожала плечами."
        cs_mz "Нет. Ты читаешь спокойно."
        cs_narrator "Я кивнула."
        cs_ls "Хорошо."
        cs_narrator "Она чуть усмехнулась."
        cs_mz "А чего спрашиваешь?"
        cs_narrator "Я немного подумала."
        cs_ls "Просто не хочу задерживать тебя после работы."
        cs_narrator "Она посмотрела на часы."
        cs_mz "Когда буду закрывать, скажу."
        cs_narrator "Я улыбнулась."
        cs_ls "Договорились."
    else:
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Пока не мешаешь. Но скоро закрываю."
        cs_narrator "Я кивнула."
        cs_ls "Конечно. Тогда ещё несколько страниц и пойду."
        cs_narrator "Она вернулась к журналу."
    cs_narrator "Я снова открыла книгу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "И через некоторое время поймала себя на странной мысли."
    cs_th "Вообще-то за сегодняшний день произошло довольно много всего."
    cs_th "Не таких событий, которые попадут в лагерную летопись."
    cs_th "Не каких-нибудь невероятных приключений."
    cs_th "Просто разговоры."
    cs_th "Небольшие поручения."
    cs_th "Книга."
    cs_th "Рисунки."
    cs_th "Пара удачных шуток."
    cs_th "И несколько людей, которые постепенно начинают вести себя рядом со мной немного свободнее."
    cs_narrator "Я посмотрела на страницу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Интересно."
    cs_th "Раньше мне казалось, что нужно как можно быстрее узнать об этом месте всё."
    cs_th "Понять правила."
    cs_th "Найти выход."
    cs_th "Выяснить, почему мы вообще здесь."
    cs_th "А теперь я начинаю замечать совершенно другие вещи."
    cs_th "Кто как улыбается."
    cs_th "Кто любит тишину."
    cs_th "Кто умеет поддержать разговор."
    cs_th "И кто способен ответить на мою глупую шутку собственной, иногда даже более удачной."
    cs_narrator "Я чуть улыбнулась."
    cs_th "Кажется, именно так и происходит привыкание."
    cs_th "Не когда перестаёшь замечать странности."
    cs_th "А когда среди них появляются знакомые мелочи."
    $ cs_pov_end()
    with cs_sprite_change
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_narrator "Женя закрыла журнал."
    cs_narrator "Я услышала негромкий звук."
    cs_narrator "Подняла голову."
    cs_narrator "Она посмотрела на часы."
    cs_mz "Лена."
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_mz "Скоро закрываю."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо. Уже заканчиваю главу."
    cs_narrator "Она посмотрела на мою книгу."
    cs_mz "Ты ведь не собираешься дочитать её сегодня целиком?"
    cs_narrator "Я задумалась."
    cs_ls "Нет. До конца ещё далеко, а читать наспех не хочется."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Вот и правильно. Книга никуда не денется."
    cs_narrator "Я улыбнулась."
    cs_ls "Надеюсь. А то будет обидно, если завтра она решит уехать без меня."
    cs_narrator "Она посмотрела на меня поверх очков."
    cs_mz "Соколова."
    cs_narrator "Я кивнула."
    cs_ls "Всё. Последняя литературная шутка на сегодня."
    cs_narrator "Женя покачала головой."
    cs_narrator "Но улыбалась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я снова посмотрела на страницу."
    cs_narrator "И вдруг поняла, что сегодня мне действительно хорошо."
    cs_narrator "Не потому, что удалось кого-то рассмешить."
    cs_narrator "Не потому, что я снова добралась до книги."
    cs_narrator "И даже не потому, что начала привыкать к лагерю."
    cs_narrator "Просто у меня появилось место, куда хотелось возвращаться."
    cs_th "И человек, с которым там было спокойно."
    cs_narrator "Я перевернула страницу."
    cs_narrator "За окном становилось темнее."
    cs_narrator "Где-то далеко, на площади, Семён, наверное, уже закончил своё совещание со Славей."
    cs_narrator "Возможно, даже успел забыть мою небольшую постановку."
    cs_th "Хотя зная его…"
    cs_narrator "Я едва заметно улыбнулась."
    cs_th "Нет."
    cs_th "Не буду продолжать."
    cs_th "Сегодня и так достаточно."
    cs_narrator "Женя снова опустила взгляд к записям."
    cs_narrator "Я продолжила читать."
    cs_narrator "И библиотека вернулась к привычной тишине."
    return
