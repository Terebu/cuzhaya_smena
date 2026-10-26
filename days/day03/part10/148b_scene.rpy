# -*- coding: utf-8 -*-
label cs_day03_148b:
    $ save_name = "Чужая смена — День 3: Хорошая компания не обязана разговаривать"
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я ещё несколько секунд смотрела на Дашу."
    cs_narrator "Потом закрыла книгу, оставив между страницами закладку."
    cs_narrator "Она заметила."
    cs_da "Что-то случилось?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Просто подумала, что мы с тобой сегодня почти не отдыхали."
    cs_narrator "Она немного удивилась."
    cs_da "А сейчас разве не отдыхаем?"
    cs_narrator "Я посмотрела на книгу."
    cs_narrator "Потом на её тетрадь."
    cs_narrator "И улыбнулась."
    cs_ls "Вот именно."
    cs_narrator "Немного помолчала."
    cs_ls "Давай просто посидим спокойно. Ты займёшься своим, я почитаю."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "И всё?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_narrator "Она улыбнулась."
    cs_da "Мне нравится."
    cs_narrator "Я чуть усмехнулась."
    cs_ls "Правда? А я уже приготовилась защищать право гражданина на добровольное молчание."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Не придётся."
    cs_narrator "Я устроилась поудобнее."
    cs_narrator "Дарья вернулась к тетради."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Некоторое время мы занимались своими делами."
    cs_narrator "Не разговаривали."
    cs_narrator "Не пытались друг друга развлекать."
    cs_narrator "Иногда кто-то шевелился."
    cs_narrator "Иногда переворачивалась страница."
    cs_narrator "Иногда за окном проходили пионеры."
    cs_narrator "И всё."
    cs_narrator "Вообще-то удивительно."
    cs_narrator "Сколько разговоров люди придумывают только потому, что боятся показаться скучными."
    cs_narrator "А ведь можно просто находиться рядом."
    cs_narrator "Без обязательной программы."
    cs_narrator "Без необходимости постоянно доказывать, что друг другу интересны."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Через некоторое время Даша подняла голову."
    cs_da "Лен."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Да?"
    cs_narrator "Она немного улыбнулась."
    cs_da "Спасибо, что не пытаешься постоянно меня развлекать."
    cs_narrator "Я задумалась."
    cs_narrator "Затем совершенно серьёзно ответила:"
    cs_ls "Это временно. У меня сегодня производственный перерыв."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Ну конечно."
    cs_narrator "Я улыбнулась."
    cs_narrator "И снова открыла книгу."
    return
