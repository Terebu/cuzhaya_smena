# -*- coding: utf-8 -*-
label cs_day01_37:
    $ save_name = "Чужая смена — День 1: Миллиарды транзисторов"
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "sh", "el"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Шурик пододвинул стул."
    show sh normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "А что внутри?"
    cs_ls "Процессор. Память. Аккумулятор. Камеры. Различные датчики и модули связи."
    cs_sh "Какой процессор?"
    cs_ls "Многоядерный."
    cs_sh "Сколько транзисторов?"
    cs_narrator "Я ненадолго задумалась."
    cs_ls "Если не ошибаюсь, в современных мобильных чипах их уже миллиарды."
    cs_narrator "Шурик снял очки."
    cs_narrator "Протёр их."
    cs_narrator "Надел обратно."
    show sh surprise pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Миллиарды?"
    cs_ls "Да."
    show sh normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "В одном процессоре?"
    cs_ls "Именно."
    cs_narrator "Он посмотрел на телефон так, словно пытался обнаружить в нём спрятанный шкаф с вычислительной аппаратурой."
    cs_sh "Это невозможно."
    cs_ls "Для вашего времени — пожалуй."
    cs_narrator "Электроник оживился."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "А сколько памяти?"
    cs_narrator "Я назвала приблизительный объём памяти устройства."
    cs_narrator "Шурик переспросил."
    cs_narrator "Затем ещё раз внимательно осмотрел корпус."
    cs_sh "И всё здесь?"
    cs_ls "Всё здесь."
    cs_narrator "Он покачал головой."
    cs_sh "С такой техникой можно решать невероятно сложные задачи."
    cs_ls "Можно."
    cs_sh "Моделировать процессы. Выполнять расчёты. Обрабатывать огромные объёмы информации…"
    cs_narrator "Я кивнула."
    cs_ls "А я чаще всего смотрю фотографии котов."
    cs_narrator "Электроник замер."
    show cs_darya amused pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо засмеялась."
    cs_narrator "Шурик посмотрел на меня с почти искренним разочарованием."
    cs_sh "Серьёзно?"
    cs_ls "Абсолютно."
    cs_sh "На таком устройстве?"
    cs_ls "Добро пожаловать в будущее."
    cs_narrator "Я развела руками."
    cs_ls "Научно-технический прогресс привёл нас к возможности обмениваться фотографиями домашних животных практически мгновенно."
    show el laugh pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник рассмеялся."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Не верю!"
    cs_ls "Я бы тоже не поверила."
    cs_narrator "Шурик всё ещё смотрел на телефон."
    cs_sh "И ведь наверняка можно было бы использовать его гораздо полезнее."
    cs_narrator "Я немного подумала."
    cs_ls "Можно. И используют. Просто человечество не обязано постоянно заниматься великими открытиями."
    cs_narrator "Дарья добавила:"
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Иногда хочется просто отдохнуть."
    cs_ls "Именно. Даже владельцам миллиардов транзисторов."
    return
