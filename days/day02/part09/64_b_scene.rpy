# -*- coding: utf-8 -*-
label cs_day02_64b:
    $ save_name = "Чужая смена — День 2: Разрешение на присутствие"
    $ cs_part09_live = True
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_dinner64b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я остановилась возле стола."
    cs_ls "Женя, можно к тебе?"
    cs_narrator "Она посмотрела на свободный стул."
    cs_narrator "Затем на меня."
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А других мест нет?"
    cs_narrator "Я оглянулась."
    cs_ls "Есть."
    cs_narrator "Она приподняла бровь."
    cs_mz "Тогда почему здесь?"
    cs_narrator "Я немного подумала."
    cs_ls "Потому что мы знакомы. Но если хочешь посидеть одна, не будем мешать."
    cs_narrator "Женя замолчала."
    cs_narrator "Посмотрела на Дарью."
    cs_narrator "Та спокойно ждала."
    cs_narrator "Не вмешивалась."
    cs_narrator "Женя снова перевела взгляд на меня."
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ладно. Садитесь."
    cs_narrator "Я улыбнулась."
    cs_ls "Спасибо."
    cs_mz "Только без вчерашнего разговора на полчаса."
    cs_narrator "Я кивнула."
    cs_ls "Сегодня исключительно бытовые темы."
    cs_mz "Посмотрим."
    cs_narrator "Дарья села первой."
    cs_narrator "Я осторожно опустила поднос на стол."
    cs_narrator "Женя вернулась к ужину."
    cs_th "Вот и всё."
    cs_th "Никаких торжественных переговоров."
    cs_th "Просто человеку не помешала наша компания."
    cs_th "Пожалуй, для начала вполне достаточно."
    return
