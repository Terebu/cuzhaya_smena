# -*- coding: utf-8 -*-
label cs_day03_178b:
    $ save_name = "Чужая смена — День 3: Не всякая тишина требует объяснения"
    cs_narrator "Я посмотрела на Дашу, потом на дорожку."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Нет."
    cs_th "Сейчас не хочется начинать серьёзный разговор. Не потому, что я боюсь. Просто вечер получился хорошим. И, пожалуй, хочется оставить его таким."
    cs_narrator "Я чуть крепче взяла Дашу под руку. Она повернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ничего. Просто пойдём."
    cs_narrator "Она посмотрела на меня. Несколько секунд молчала. Потом кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Хорошо."
    cs_narrator "Мы прошли ещё немного. За деревьями показались знакомые домики. Воздух стал прохладнее. Я посмотрела на небо."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Надо же. Даже сейчас мне совершенно не хочется ничего комментировать. Просто идти рядом."
    cs_narrator "Даша вдруг тихо сказала:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Мне нравится."
    cs_narrator "Я повернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Что?"
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Вот так гулять. Без спешки."
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
    return
