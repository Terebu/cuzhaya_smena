# -*- coding: utf-8 -*-
label cs_day01_38:
    $ save_name = "Чужая смена — День 1: Пять вольт и немного надежды"
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.5 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "sh", "el"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Шурик снова вернулся к вопросу питания."
    show sh serious pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Пять вольт, говоришь?"
    cs_ls "Для стандартного режима зарядки — да."
    cs_sh "Стабилизированный источник мы собрать можем."
    cs_ls "Верю."
    cs_narrator "Я указала на порт смартфона."
    cs_ls "Но вот подключение придётся продумать отдельно."
    cs_narrator "Шурик кивнул."
    cs_sh "Разъём незнакомый."
    cs_ls "Именно. И я не хочу рисковать телефоном, пока мы не проверим всё на другом устройстве или эквивалентной нагрузке."
    cs_narrator "Электроник посмотрел на меня."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Настолько он тебе дорог?"
    cs_narrator "Я взяла смартфон в руку."
    cs_narrator "Несколько секунд рассматривала тёмный экран."
    cs_ls "Дело не в цене."
    cs_narrator "Я провела пальцем по корпусу."
    cs_ls "Там фотографии. Заметки. Некоторые мои работы. Кое-что из моей обычной жизни."
    cs_narrator "Шурик перестал возиться с инструментами."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Я продолжила значительно тише:"
    label cs_check_day01_part07_home:
    cs_ls "Возможно, это единственная вещь, которая у меня осталась от дома и которую ещё можно заставить работать."
    pause 1.0
    cs_narrator "В помещении стало непривычно тихо."
    cs_narrator "Я почувствовала, что сказала больше, чем собиралась."
    cs_narrator "Поэтому аккуратно положила телефон обратно на стол."
    cs_ls "В общем, хотелось бы сохранить его в рабочем состоянии."
    cs_narrator "Шурик кивнул."
    cs_narrator "На этот раз без улыбки."
    cs_sh "Понимаю."
    cs_narrator "Электроник посмотрел на него."
    cs_el "Может, попробуем?"
    cs_sh "Сегодня лучше не спешить. Сначала нужно разобраться с подключением и проверить источник питания."
    cs_narrator "Я подняла взгляд."
    cs_ls "То есть?"
    cs_sh "Если найдём подходящие детали, завтра попробуем подготовить безопасное подключение. Но обещать, что всё заработает, я не могу."
    cs_narrator "Я несколько секунд смотрела на него."
    cs_ls "Завтра?"
    cs_sh "Да."
    cs_narrator "Я вздохнула."
    cs_th "Ну конечно."
    cs_th "Будущее столкнулось с плановым ремонтом."
    cs_narrator "Но спорить было бессмысленно."
    cs_narrator "Более того, впервые за день мне предложили решение, которое не требовало верить в мистику."
    cs_narrator "Обычная техническая задача."
    cs_narrator "Неизвестный разъём."
    cs_narrator "Блок питания."
    cs_narrator "Проверка."
    cs_narrator "Всё вполне материальное."
    cs_ls "Хорошо. Завтра так завтра."
    cs_narrator "Шурик заметно расслабился."
    cs_sh "Тогда оставишь устройство?"
    cs_narrator "Я тут же убрала смартфон в карман."
    cs_ls "Нет."
    cs_sh "Почему?"
    cs_ls "Завтра принесу. Сегодня оно останется у меня."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник усмехнулся."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Совсем нам не доверяешь?"
    cs_ls "Пока мы знакомы около получаса. Предлагаю не торопить развитие отношений."
    show cs_darya amused pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Шурик кивнул."
    cs_sh "Ладно. Тогда завтра приходи."
    stop music fadeout 2.0
    return
