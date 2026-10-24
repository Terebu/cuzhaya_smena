# -*- coding: utf-8 -*-
label cs_day03_128:
    $ save_name = "Чужая смена — День 3: После обеда"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    with Dissolve(0.8)
    cs_narrator "Я пошла к библиотеке не торопясь. Торопиться после обеда вообще казалось дурной привычкой."
    cs_th "Ни новых экспедиций, ни обязательного поиска ответов. Просто книга."
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    with dissolve
    cs_narrator "Дверь библиотеки была открыта. Я поднялась на крыльцо."
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    stop ambience fadeout 1.5
    stop music fadeout 2.0
    $ cs_frame_focus(["cs_zhenya"])
    with Dissolve(0.8)
    label cs_check_day03_128_library:
    cs_narrator "Женя уже сидела за своим столом. Здесь было тихо даже после столовой."
    # Also covers an old save made after the former version of the lunch.
    if cs_friend_mz >= 2:
        $ cs_mz_book_prepared_day3 = True
    if cs_day03_reading_book_selected:
        cs_mz "Твоя книга на столе. Я её никуда не убирала."
    else:
        if cs_mz_book_prepared_day3:
            cs_narrator "Она подвинула ко мне два небольших томика."
            cs_mz "Вот, посмотри. Я бы начала с Паустовского. Здесь есть «Тёплый хлеб»."
            cs_ls "Почему именно с него?"
            show cs_zhenya thoughtful pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
            cs_mz "Он короткий. Но дело не в этом. Там человек сначала делает гадость, а потом приходится что-то исправлять. Не словами."
            cs_ls "То есть лёгкого чтения после обеда не обещаешь?"
            cs_mz "Читать легко. А дальше сама решишь."
            cs_narrator "Я взяла предложенный сборник и посмотрела оглавление."
        else:
            cs_ls "Я всё-таки дошла. Можно посмотреть рассказы?"
            cs_mz "Вон тот стеллаж, средняя полка. Только не перемешивай."
            cs_narrator "Я нашла сборник Паустовского и раскрыла на оглавлении. Среди названий попалось знакомое: «Тёплый хлеб»."
            cs_ls "Начну с этого. Здесь посижу, выносить не буду."
            cs_mz "Хорошо."
        $ cs_day03_reading_book_selected = True
        $ cs_day03_reading_book_id = "paustovsky_warm_bread"
        $ cs_day03_reading_book_location = "library_reading_table"
    if cs_mz_quiet_reading_place_day3:
        cs_narrator "Я устроилась за дальним столом у окна, который Женя предложила за обедом. Заново спрашивать разрешения не понадобилось."
        cs_mz "Если свет будет мешать, штору можно поправить. Только не дёргай."
        cs_ls "Разберусь. Спасибо."
    else:
        cs_ls "За свободным столом можно?"
        cs_mz "Да. Садись."
        cs_narrator "Я выбрала свободное место и осторожно положила локоть рядом с книгой."
    if cs_mz_map_lead and cs_mz_catalog_checked_day3:
        cs_th "Каталоги мы уже проверили утром. Сейчас можно оставить их в покое."
    $ cs_reflective_focus()
    with cs_sprite_leave
    cs_narrator "Я раскрыла сборник на первой странице рассказа. Из окна тянуло тёплым воздухом."
    cs_th "Пожалуй, начну."
    return
