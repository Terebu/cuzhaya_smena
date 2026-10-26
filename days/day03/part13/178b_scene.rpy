# -*- coding: utf-8 -*-
label cs_day03_178b:
    $ save_name = "Чужая смена — День 3: Не всякая тишина требует объяснения"
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Потом на дорожку."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Нет."
    cs_th "Сейчас не хочется начинать серьёзный разговор."
    cs_th "Не потому, что я боюсь."
    cs_th "Просто вечер получился хорошим."
    cs_th "И, пожалуй, хочется оставить его таким."
    cs_narrator "Я чуть крепче взяла Дашу под руку."
    cs_narrator "Она повернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ничего. Просто пойдём."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Несколько секунд молчала."
    cs_narrator "Потом кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Хорошо."
    cs_narrator "Мы прошли ещё немного."
    cs_narrator "За деревьями показались знакомые домики."
    cs_narrator "Воздух стал прохладнее."
    cs_narrator "Я посмотрела на небо."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Надо же."
    cs_th "Даже сейчас мне совершенно не хочется ничего комментировать."
    cs_th "Просто идти рядом."
    cs_narrator "Дарья вдруг тихо сказала:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Мне нравится."
    cs_narrator "Я повернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Что?"
    cs_narrator "Она слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Вот так гулять. Без спешки."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Мне тоже."
    cs_narrator "Она немного помолчала."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Можем как-нибудь повторить."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Договорились."
    cs_th "Вот и всё."
    cs_th "Иногда хороший разговор состоит всего из нескольких слов."
    return
