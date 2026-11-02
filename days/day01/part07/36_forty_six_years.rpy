# -*- coding: utf-8 -*-
label cs_day01_36:
    $ save_name = "Чужая смена — День 1: Сорок шесть лет разницы"
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.5 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "sh", "el"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я оглядела парней и остановилась на Дарье. Она заметила мою нерешительность."
    show cs_darya thinking pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен. Ты уверена, что хочешь всё рассказывать?"
    cs_narrator "Час назад я просила Семёна молчать. Теперь сама стою здесь с устройством, которого ещё не должно существовать."
    cs_th "Последовательность действий на высшем уровне, Соколова."
    cs_narrator "Я медленно выдохнула."
    cs_ls "Нет, не уверена."
    cs_narrator "Шурик перевёл взгляд с одной на другую."
    show sh serious pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Что рассказывать?"
    cs_ls "Сначала ответьте на один вопрос."
    cs_sh "Какой?"
    cs_ls "Какой сейчас год?"
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник удивлённо усмехнулся."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Ты шутишь?"
    cs_ls "Не в этот раз."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_part07_year_spoken:
    cs_el "Тысяча девятьсот восьмидесятый."
    pause 1.0
    label cs_check_day01_part07_year:
    cs_th "1980-й. Наконец конкретная дата."
    cs_narrator "Не доказательство путешествия в прошлое, но теперь я знала, какой год здесь считают настоящим."
    cs_ls "Хорошо. Тогда объясню одну вещь. Только прошу пока не рассказывать об этом всему лагерю."
    cs_narrator "Шурик насторожился."
    cs_sh "О чём?"
    cs_narrator "Я коснулась пальцем телефона."
    cs_ls "Это устройство из 2026 года."
    cs_narrator "Электроник моргнул. Шурик молча выпрямился."
    show sh surprise pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Из какого?"
    cs_ls "Две тысячи двадцать шестого."
    cs_narrator "Он посмотрел на Дарью."
    cs_narrator "Та кивнула."
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы обе оттуда. Хотя пока сами не понимаем, как здесь оказались."
    show el laugh pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник недоверчиво рассмеялся."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Да ладно вам!"
    cs_narrator "Я пожала плечами."
    cs_ls "Вполне нормальная реакция."
    cs_narrator "Шурик указал на телефон."
    show sh serious pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Значит, это техника будущего?"
    cs_ls "Если верить календарю — да."
    cs_sh "И ты хочешь, чтобы мы тебе поверили?"
    cs_ls "Нет. Для начала я хочу, чтобы вы помогли понять, можно ли его безопасно зарядить."
    cs_ls "А уж верить моей биографии или нет — ваше личное дело."
    cs_narrator "Шурик задумчиво посмотрел на корпус."
    cs_narrator "Электроник сел на край соседнего стула."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "И что он умеет?"
    cs_ls "Сколько у вас времени?"
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "До ужина ещё есть."
    cs_ls "Тогда начнём с простого."
    cs_narrator "Я подняла смартфон."
    cs_ls "Это телефон."
    cs_sh "Телефон? Но где трубка?"
    cs_ls "Здесь она не нужна."
    cs_narrator "Я показала на экран."
    cs_ls "На нём можно звонить, писать сообщения, фотографировать, снимать видео, слушать музыку, читать книги и работать с программами."
    cs_narrator "Электроник наклонился вперёд."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Всё в одном устройстве?"
    cs_ls "Да."
    cs_el "А телевизор?"
    cs_ls "В некотором смысле и телевизор. Если есть подключение к сети."
    cs_narrator "Шурик нахмурился."
    cs_sh "К какой сети?"
    cs_ls "Компьютерной."
    cs_sh "У вас компьютеры объединены в сеть?"
    cs_ls "Да."
    show sh surprise pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Сколько?"
    cs_ls "Очень много. Миллиарды устройств по всему миру."
    pause 1.0
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник перестал улыбаться."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Миллиарды?"
    cs_ls "Да."
    cs_narrator "Шурик подался вперёд."
    show sh serious pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "И они могут обмениваться информацией?"
    cs_ls "Именно."
    cs_sh "На каком расстоянии?"
    cs_ls "Практически по всему миру, если инфраструктура позволяет."
    cs_narrator "Оба замолчали."
    cs_el "И для чего люди используют такую сеть?"
    cs_narrator "Я начала загибать пальцы."
    cs_ls "Для научных исследований. Учёбы. Работы. Связи. Покупок. Просмотра фильмов. Общения."
    cs_ls "И, конечно, для споров в комментариях о совершенно незначительных вещах."
    cs_narrator "Шурик нахмурился."
    cs_sh "Зачем?"
    cs_ls "Вот. Первый по-настоящему сложный вопрос."
    show cs_darya amused pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Электроник тоже не удержался от улыбки."
    return
