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
    cs_narrator "Я посмотрела на телефон."
    cs_narrator "Потом на Шурика."
    cs_narrator "На Электроника."
    cs_narrator "Наконец на Дарью."
    cs_narrator "Она сразу заметила мою нерешительность."
    show cs_darya thinking pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен. Ты уверена, что хочешь всё рассказывать?"
    cs_narrator "Справедливый вопрос."
    cs_narrator "Всего час назад я просила Семёна не распространяться о нашем происхождении."
    cs_narrator "А теперь сама стояла в кружке электроники с устройством, которого здесь ещё не должно было существовать."
    cs_th "Молодец, Соколова."
    cs_th "Последовательность действий на высшем уровне."
    cs_narrator "Я медленно выдохнула."
    cs_ls "Нет, не уверена."
    cs_narrator "Шурик перевёл взгляд с одной на другую."
    show sh serious pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Что рассказывать?"
    cs_narrator "Я посмотрела на него."
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
    cs_narrator "Я медленно кивнула."
    label cs_check_day01_part07_year:
    cs_th "Тысяча девятьсот восьмидесятый."
    cs_th "Наконец хоть одна конкретная дата."
    cs_narrator "Это всё ещё не доказывало, что мы действительно попали в прошлое."
    cs_narrator "Но по крайней мере теперь я знала, какой год считают настоящим местные жители."
    cs_narrator "Я снова посмотрела на парней."
    cs_ls "Хорошо. Тогда объясню одну вещь. Только прошу пока не рассказывать об этом всему лагерю."
    cs_narrator "Шурик насторожился."
    cs_sh "О чём?"
    cs_narrator "Я коснулась пальцем телефона."
    cs_ls "Это устройство из 2026 года."
    cs_narrator "Тишина."
    cs_narrator "Электроник моргнул."
    cs_narrator "Шурик медленно выпрямился."
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
    cs_narrator "Я сделала паузу."
    cs_ls "А уж верить моей биографии или нет — ваше личное дело."
    cs_narrator "Шурик задумчиво посмотрел на корпус."
    cs_narrator "Электроник сел на край соседнего стула."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "И что он умеет?"
    cs_narrator "Я усмехнулась."
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
    cs_narrator "Я задумалась."
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
    cs_narrator "Я посмотрела на них."
    cs_th "Вот теперь стало интересно."
    cs_narrator "Электроник наконец спросил:"
    cs_el "И для чего люди используют такую сеть?"
    cs_narrator "Я начала загибать пальцы."
    cs_ls "Для научных исследований. Учёбы. Работы. Связи. Покупок. Просмотра фильмов. Общения."
    cs_narrator "Ненадолго задумалась."
    cs_ls "И, конечно, для споров в комментариях о совершенно незначительных вещах."
    cs_narrator "Шурик нахмурился."
    cs_sh "Зачем?"
    cs_narrator "Я подняла указательный палец."
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
