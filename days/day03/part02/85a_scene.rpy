# -*- coding: utf-8 -*-
label cs_day03_85a:
    $ save_name = "Чужая смена — День 3: Первый советский сувенир"
    cs_narrator "Я вдруг вспомнила ещё кое-что."
    cs_ls "А знаешь, что самое приятное?"
    cs_narrator "Дарья заинтересованно посмотрела на меня."
    cs_da "Что?"
    cs_ls "Славя сохранила наш вчерашний плакат."
    show cs_darya neutral pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она удивилась."
    cs_da "Правда?"
    cs_ls "Да. Сняла после концерта и убрала отдельно от остальных материалов."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Здорово."
    cs_ls "Потом можно будет забрать."
    cs_narrator "Она подумала."
    cs_da "Мне бы хотелось. Мы ведь все вместе его рисовали."
    cs_ls "Вот именно."
    cs_narrator "Потом усмехнулась."
    cs_ls "Первый официальный сувенир нашего пребывания в «Совёнке». Бесплатный, уникальный, изготовлен вручную. Без возможности возврата."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Звучит как рекламное объявление."
    cs_ls "Профессиональная привычка."
    cs_narrator "Она улыбнулась."
    cs_da "Тогда заберём после завтрака или позже."
    cs_ls "Договорились."
    cs_th "Забавная вещь. Мы ещё не знаем, сколько пробудем в лагере. Но уже успели сделать здесь что-то, что хочется сохранить."
    return
