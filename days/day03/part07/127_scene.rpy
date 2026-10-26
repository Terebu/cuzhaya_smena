# -*- coding: utf-8 -*-
label cs_day03_127:
    $ save_name = "Чужая смена — День 3: Возвращение привычной Соколовой"
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    play music "sound/music/my_daily_life.ogg" fadein 2.0
    $ renpy.music.set_volume(0.12,delay=1.0,channel="music")
    cs_narrator "Дарья отложила ложку."
    cs_narrator "Посмотрела на меня."
    cs_narrator "Потом в сторону выхода."
    cs_narrator "И медленно улыбнулась."
    cs_da "Ну?"
    cs_narrator "Я подняла бровь."
    cs_ls "Что?"
    cs_narrator "Она кивнула на дверь."
    cs_da "Женя ушла."
    cs_narrator "Я посмотрела в ту же сторону."
    cs_narrator "Убедилась, что она действительно уже далеко."
    cs_narrator "Потом снова повернулась к Даше."
    cs_ls "И?"
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Ты ведь сейчас что-нибудь скажешь."
    cs_narrator "Я задумалась."
    cs_th "Вообще-то собиралась."
    cs_th "Но теперь возникло любопытное желание немного подержать паузу."
    cs_narrator "Я совершенно серьёзно посмотрела на неё."
    cs_ls "Дарья Еретикова."
    cs_narrator "Она выпрямилась."
    cs_da "Да?"
    cs_narrator "Я медленно придвинулась чуть ближе."
    cs_ls "Должна сообщить, что у меня возникли серьёзные вопросы к вашему сегодняшнему поведению."
    cs_narrator "Она приподняла бровь."
    cs_da "Какие именно?"
    cs_narrator "Я указала на место, где прежде лежал её поднос."
    cs_ls "Вы отсутствовали у раздачи значительно дольше, чем предусматривал мой предварительный план обеда."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Я же сказала, что меня остановила Ольга Дмитриевна."
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_narrator "Пауза."
    cs_ls "О чём и хотелось бы поговорить."
    if renpy.showing("cs_darya"):
        show cs_darya arms_crossed pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья закрыла глаза."
    cs_da "Лена."
    cs_narrator "Я придала лицу чрезвычайно задумчивое выражение."
    cs_ls "Две девушки. Одна вожатая. Отсутствие независимых свидетелей. Подозрительно долгая беседа…"
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Подозрительно долгая? Мы говорили минуты три."
    cs_narrator "Я подняла палец."
    cs_ls "С точки зрения голодного человека — целая вечность."
    cs_narrator "Она покачала головой."
    cs_da "Ты же сама решила не ждать."
    cs_narrator "Я кивнула."
    cs_ls "И это было исключительно разумное решение, которым я горжусь."
    cs_da "Тогда в чём претензия?"
    cs_narrator "Я задумалась."
    cs_th "Проклятье."
    cs_th "Слишком хороший вопрос."
    cs_ls "Претензий нет. Просто хочется немного поиграть в обиженную девушку."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "А-а. Вот теперь понятно."
    cs_narrator "Я театрально вздохнула."
    cs_ls "Ты даже не представляешь, сколько сил требуется, чтобы поддерживать репутацию человека с драматической личной жизнью, когда самой личной жизни практически не было."
    cs_narrator "Она улыбнулась."
    cs_da "Может, тогда и не нужно?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "На секунду задумалась."
    cs_narrator "Потом слегка улыбнулась."
    cs_ls "Возможно."
    cs_narrator "Дарья немного удивилась."
    cs_narrator "Я продолжила:"
    cs_ls "Но поддевать тебя всё равно весело."
    cs_narrator "Она рассмеялась."
    cs_da "Это я уже поняла."
    cs_narrator "Я улыбнулась шире."
    cs_ls "А теперь серьёзно. Ольга Дмитриевна только про руку спрашивала?"
    cs_narrator "Дарья кивнула."
    cs_da "Да. Ещё попросила, чтобы мы не забывали предупреждать, если собираемся куда-нибудь надолго."
    cs_da "И отдельно сказала — к старому корпусу не ходить. Даже не спросила, собираемся ли."
    cs_th "Не «будьте осторожны». Сразу «не ходить»."
    cs_narrator "Я немного помолчала."
    cs_th "Ну вот."
    cs_th "После вчерашнего она, кажется, действительно за нас переживает."
    cs_ls "Понятно."
    cs_da "И всё?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Это вполне разумно."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Тогда больше никаких расследований?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом вздохнула."
    cs_ls "Закрываем дело за отсутствием состава преступления."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я тоже."
    cs_narrator "Некоторое время мы сидели рядом."
    cs_narrator "Потом я поднялась."
    cs_ls "Ну что, пойдём?"
    cs_narrator "Дарья кивнула."
    cs_da "Пойдём."
    cs_narrator "Мы отнесли подносы."
    if cs_day03_poster_location == "dining_chair":
        cs_narrator "Дарья забрала папку с плакатом со стула и прижала к боку."
        $ cs_day03_poster_location = "darya_folder"
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.5 fadein 1.5
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    with Dissolve(0.8)
    cs_narrator "И вышли на улицу."
    cs_narrator "Солнце всё ещё ярко освещало площадь."
    cs_narrator "По дорожкам ходили пионеры."
    cs_narrator "Где-то слышалась музыка."
    cs_narrator "Я глубоко вдохнула."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Третий день."
    cs_th "И всё чаще мне кажется, что жизнь здесь начинает приобретать какой-то собственный ритм."
    cs_th "Не тот, который я выбирала."
    cs_th "Но уже не совсем чужой."
    $ cs_pov_end()
    with cs_sprite_change
    cs_da "Ты сейчас в библиотеку?"
    cs_narrator "Я кивнула."
    if cs_mz_book_prepared_day3:
        cs_ls "Немного прогуляюсь и зайду к Жене. Она обещала подобрать книгу."
    else:
        cs_ls "Немного прогуляюсь и зайду к Жене. Посмотрю, что есть почитать."
    cs_da "А я хотела к Мику."
    cs_narrator "Я улыбнулась."
    cs_ls "Тогда иди. Может, сегодня она всё-таки убедит тебя сыграть что-нибудь подольше."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Только не начинай."
    cs_narrator "Я кивнула."
    cs_ls "Даже не собиралась."
    cs_narrator "Она усмехнулась."
    cs_da "Не верю."
    cs_narrator "Я улыбнулась."
    cs_ls "И правильно."
    cs_narrator "Мы рассмеялись."
    if cs_friend_mi >= 2 and cs_mi_day3_arrangement_help:
        cs_narrator "Дарья вдруг вспомнила:"
        cs_da "Кстати, Мику просила передать, что хочет ещё раз показать тебе то вступление, которое вы сегодня обсуждали."
        cs_narrator "Я заинтересовалась."
        cs_ls "Правда?"
        cs_narrator "Она кивнула."
        cs_da "Да. Сказала, что немного его изменила."
        cs_narrator "Я улыбнулась."
        cs_ls "Тогда после библиотеки загляну."
        $ cs_mi_followup_invitation_day3 = True
    if cs_friend_dv >= 2 and cs_dv_music_talk_day3:
        cs_narrator "Дарья посмотрела в сторону музыкального клуба."
        cs_da "Алиса, кстати, тоже спрашивала, придёшь ли ты ещё."
        cs_narrator "Я удивилась."
        cs_ls "Серьёзно?"
        cs_da "Да. Кажется, хотела что-то показать на гитаре."
        cs_narrator "Я задумалась."
        cs_ls "Надо же. Меня начинают приглашать на музыкальные консультации."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
        $ cs_dv_followup_invitation_day3 = True
    cs_narrator "Мы остановились у развилки."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Тогда увидимся позже."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    $ cs_day03_darya_destination = "music_club"
    $ cs_actor_exit(["cs_darya"])
    with cs_sprite_leave
    label cs_check_day03_127_darya_left:
    cs_narrator "Она направилась к музыкальному клубу."
    cs_narrator "Я некоторое время смотрела ей вслед."
    cs_th "Хорошо."
    cs_th "Всё-таки приятно, когда у каждого из нас появляются собственные занятия."
    cs_th "Не потому, что мы хотим проводить меньше времени вместе."
    cs_th "А потому, что теперь есть о чём рассказать друг другу вечером."
    cs_narrator "Я повернулась к библиотеке."
    cs_th "Ну что ж."
    if cs_mz_book_prepared_day3:
        cs_th "Пора узнать, какую книгу мне приготовила Женя."
    else:
        cs_th "Пора выбрать что-нибудь почитать."
    return
