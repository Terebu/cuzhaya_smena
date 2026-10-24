# -*- coding: utf-8 -*-
label cs_day03_94a:
    $ save_name = "Чужая смена — День 3: Разговор о книгах"
    label cs_check_day03_94a:
    cs_narrator "Я посмотрела на Женю."
    cs_ls "Женя, можно один вопрос?"
    cs_narrator "Она подняла голову."
    cs_mz "Какой?"
    cs_ls "Что бы ты посоветовала мне почитать?"
    if renpy.showing("cs_zhenya"):
        show cs_zhenya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя ненадолго задумалась."
    cs_mz "А что тебе нравится?"
    cs_narrator "Я улыбнулась."
    cs_ls "Вот как раз поэтому и спрашиваю. Интересно узнать, что нравится тебе."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya thoughtful pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_mz "То есть ты хочешь книгу на мой вкус?"
    cs_narrator "Я кивнула."
    if cs_lena_book_returned:
        cs_ls "Да. Вчерашняя мне понравилась. Думаю, можно попробовать ещё что-нибудь из того, что ты считаешь хорошим."
    else:
        cs_ls "Да. Хочу попробовать что-нибудь из того, что ты считаешь хорошим."
    cs_narrator "Женя немного помолчала."
    cs_narrator "Потом осторожно положила свою книгу на стол."
    cs_mz "Тогда я бы посоветовала что-нибудь, где важнее люди и их решения, а не просто приключения."
    cs_narrator "Я заинтересованно кивнула."
    cs_ls "Звучит хорошо."
    cs_mz "Только не уверена, что тебе понравится."
    cs_narrator "Я пожала плечами."
    cs_ls "Так ведь в этом и смысл. Не обязательно читать только то, что заранее кажется знакомым."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shy pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она слегка улыбнулась."
    cs_mz "Ладно."
    cs_narrator "Немного подумала."
    cs_mz "У меня есть несколько вариантов. Посмотрим, что сейчас свободно."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    if cs_mz_map_lead:
        cs_narrator "Женя вдруг вспомнила ещё кое-что."
        cs_mz "И насчёт старых каталогов. Ты ведь сегодня собиралась зайти?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Только сначала хочу показаться Виоле с локтем."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя посмотрела на повязку."
        cs_mz "Правильно. Тогда приходи после медпункта, ближе к концу утра."
        cs_ls "Хорошо."
        cs_mz "Сначала посмотрим документы, а потом уже книги."
        cs_narrator "Я улыбнулась."
        cs_ls "Разумное распределение рабочего времени."
        cs_narrator "Женя усмехнулась."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya arms_crossed pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_mz "И никаких самовольных исследований шкафов."
        cs_narrator "Я кивнула."
        cs_ls "Без разрешения начальника библиотеки — ни шагу."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Она покачала головой."
        cs_narrator "Но улыбнулась."
    else:
        cs_narrator "Женя посмотрела на часы."
        cs_mz "Можешь зайти после обеда. Я посмотрю, какие книги сейчас есть."
        cs_narrator "Я кивнула."
        cs_ls "Хорошо. Тогда до встречи."
    cs_narrator "Женя взяла книгу."
    cs_mz "И, Соколова…"
    cs_narrator "Я подняла взгляд."
    cs_ls "Да?"
    cs_narrator "Она немного помолчала."
    cs_mz "Спасибо, что действительно интересуешься. А не просто пытаешься меня разговорить."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Мне правда интересно."
    cs_narrator "Женя кивнула."
    cs_mz "Тогда хорошо."
    cs_th "Вот и всё."
    cs_th "Никаких особенных обещаний."
    cs_th "Просто ещё одна книга."
    cs_th "И ещё одна причина вернуться."
    return
