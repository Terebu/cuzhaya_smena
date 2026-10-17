# -*- coding: utf-8 -*-
label cs_day02_64c:
    $ save_name = "Чужая смена — День 2: Иногда одиночество — это выбор"
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
    label cs_check_dinner64c:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я остановилась возле стола."
    cs_ls "Женя, можно к тебе присоединиться?"
    cs_narrator "Она посмотрела на свободные места."
    cs_narrator "Затем на меня."
    cs_mz "Я вообще-то хотела спокойно поесть одна."
    cs_narrator "Я немного помолчала."
    cs_th "Ну вот."
    cs_th "Предельно понятный ответ."
    cs_ls "Хорошо. Не будем мешать."
    cs_narrator "Женя слегка удивилась."
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
    cs_mz "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Конечно."
    cs_narrator "Потом улыбнулась."
    cs_ls "Но приятного аппетита желать всё-таки можно?"
    cs_narrator "Она вздохнула."
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
    cs_mz "Можно."
    cs_ls "Тогда приятного аппетита."
    cs_narrator "Дарья кивнула ей."
    cs_da "Хорошего вечера."
    cs_mz "И вам."
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_dinner64_separate:
    # cs_director_begin: Girls choose a separate table; Zhenya remains at her own table
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_d3d3e02a81:
    # cs_director_end
    cs_narrator "Мы отошли к свободному столику возле окна."
    cs_narrator "Дарья поставила поднос."
    cs_narrator "Я устроилась напротив."
    cs_narrator "Она посмотрела на меня."
    cs_da "Я думала, ты будешь настаивать."
    cs_narrator "Я усмехнулась."
    cs_ls "Было такое намерение."
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И что изменилось?"
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Та уже спокойно занималась ужином."
    cs_ls "Она прямо сказала, что хочет побыть одна."
    cs_narrator "Пожала плечами."
    cs_ls "Странно было бы обижаться на человека за то, что он знает, чего хочет."
    cs_narrator "Дарья улыбнулась."
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Согласна."
    cs_narrator "Я взяла ложку."
    cs_th "Надо же."
    cs_th "Кажется, я действительно начинаю понимать простую вещь."
    cs_th "Общение — это не соревнование на количество сказанных слов."
    cs_th "И не всякую социальную дистанцию нужно немедленно сокращать."
    cs_narrator "Возможно, когда-нибудь Женя сама захочет посидеть с нами."
    cs_narrator "А если нет — тоже ничего страшного."
    return
