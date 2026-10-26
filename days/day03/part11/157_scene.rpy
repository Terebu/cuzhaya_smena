# -*- coding: utf-8 -*-
label cs_day03_157:
    $ save_name = "Чужая смена — День 3: Место, которое уже не нужно выпрашивать"
    cs_narrator "Женя привычно направилась к столу возле окна."
    cs_narrator "Я уже собиралась спросить, можно ли присесть рядом, но она остановилась первой."
    if cs_mz_dinner_friend_on_arrival >= 2:
        cs_narrator "Женя поставила поднос."
        cs_narrator "Посмотрела на свободный стул."
        cs_mz "Садись."
        cs_narrator "Я слегка удивилась."
        cs_ls "Даже без официального заявления?"
        cs_narrator "Она приподняла бровь."
        cs_mz "Тебе бумагу выдать?"
        cs_narrator "Я задумалась."
        cs_ls "Желательно с печатью."
        cs_narrator "Женя закатила глаза."
        cs_mz "Соколова."
        cs_narrator "Я улыбнулась."
        cs_ls "Всё. Сажусь."
        cs_narrator "Дарья тихо рассмеялась."
        cs_narrator "Я устроилась рядом с Женей."
        cs_narrator "Даша — напротив."
        cs_th "Надо же."
        cs_th "Кажется, вопрос о том, можно ли мне сидеть рядом, постепенно перестаёт существовать."
    else:
        cs_narrator "Женя поставила поднос возле окна."
        cs_narrator "Я остановилась рядом."
        cs_ls "Можно к тебе?"
        cs_narrator "Женя посмотрела на свободное место."
        cs_mz "Садись. Только без представлений."
        cs_narrator "Я улыбнулась."
        cs_ls "Постараюсь."
        cs_narrator "Дарья устроилась напротив."
        cs_narrator "Мы начали ужинать."
    cs_narrator "Несколько минут мы ели молча."
    cs_narrator "У столовой были собственные законы."
    cs_narrator "За одним столом кто-нибудь обязательно смеялся."
    cs_narrator "За другим спорили о планах на вечер."
    cs_narrator "Возле выхода уже появились первые пионеры, закончившие есть быстрее остальных."
    cs_narrator "А у нас было спокойно."
    cs_narrator "Я неторопливо ела."
    cs_narrator "Иногда смотрела в окно."
    cs_narrator "Иногда прислушивалась к окружающим голосам."
    cs_narrator "Женя тоже никуда не спешила."
    cs_narrator "Даша, кажется, окончательно привыкла к тому, что за этим столом не требуется непрерывно разговаривать."
    cs_th "Хорошо."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Поразительно хорошо."
    cs_th "При первом знакомстве я бы обязательно попыталась расшевелить Женю."
    cs_th "Сегодня же мне вполне нравится просто сидеть рядом."
    if cs_mz_dinner_friend_on_arrival >= 1:
        $ cs_pov_end()
        with cs_sprite_change
        cs_narrator "Через некоторое время Дарья подняла голову."
        cs_narrator "Посмотрела на меня."
        cs_narrator "Потом на Женю."
        cs_da "Лен."
        cs_narrator "Я повернулась."
        cs_ls "Да?"
        cs_narrator "Она слегка улыбнулась."
        cs_da "Ты сегодня уже не первый раз оказываешься рядом с Женей."
        cs_narrator "Я задумалась."
        cs_ls "И что?"
        cs_da "Ничего. Просто наблюдение."
        cs_narrator "Я приподняла бровь."
        cs_ls "Надеюсь, в научных целях?"
        cs_narrator "Дарья кивнула."
        cs_da "Исключительно."
        cs_narrator "Женя посмотрела на неё."
        cs_narrator "Потом на меня."
        cs_mz "Мне уже начинать беспокоиться?"
        cs_narrator "Я повернулась к ней."
        cs_ls "Пока нет. Следственный комитет ещё не сформирован."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        if cs_mz_dinner_friend_on_arrival >= 2:
            cs_da "Я вообще хотела сказать, что ты сегодня получила приглашение уже несколько раз."
        else:
            cs_da "Я вообще хотела сказать, что вы уже нашли общую тему."
        cs_narrator "Я задумалась."
        cs_ls "Справедливо."
        cs_da "И всё?"
        cs_narrator "Я посмотрела на неё."
        cs_narrator "Потом на Женю."
        cs_narrator "И совершенно серьёзно ответила:"
        cs_ls "Внутри я уже провела парад."
        cs_narrator "Женя фыркнула."
        cs_mz "Я так и думала."
        cs_narrator "Я кивнула."
        cs_ls "Но наружу не выпускаю. Во избежание нарушения библиотечного порядка."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя поправила очки."
        cs_mz "Мы вообще-то в столовой."
        cs_narrator "Я замолчала."
        cs_narrator "Медленно повернулась к ней."
        cs_narrator "Потом улыбнулась."
        cs_ls "Вот видишь. Теперь даже ты начинаешь подсказывать мне поводы для шуток."
        cs_narrator "Дарья засмеялась."
        cs_narrator "Женя покачала головой."
        cs_narrator "Но тоже улыбалась."
    else:
        $ cs_pov_end()
        with cs_sprite_change
        cs_narrator "Дарья кивнула мне и вернулась к ужину."
    return
