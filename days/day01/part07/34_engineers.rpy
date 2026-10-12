# -*- coding: utf-8 -*-
label cs_day01_34:
    $ save_name = "Чужая смена — День 1: Товарищи инженеры"
    show sh normal pioneer far at cs_actor_left
    # cs_composition: regroup
    show cs_darya shrug pioneer far at cs_darya_far_right
    show el normal pioneer far at cs_actor_right
    # cs_composition: regroup
    show sh normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show el normal pioneer far at cs_actor_far_right
    # cs_composition: regroup
    show cs_darya shrug pioneer far at cs_darya_far_center
    show cs_darya shrug pioneer far at cs_darya_far_center
    with None
    label cs_check_day01_part07_engineers:
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/smooth_machine.ogg" fadeout 2.0 fadein 2.5
    cs_narrator "В помещении находились двое."
    cs_narrator "Один сидел за столом, внимательно рассматривая какую-то деталь."
    cs_narrator "Другой стоял рядом и что-то ему объяснял."
    cs_narrator "Шурик."
    cs_narrator "Электроник."
    cs_narrator "Оба повернулись к нам."
    cs_narrator "Я остановилась у порога."
    cs_narrator "Поправила галстук."
    cs_narrator "И с совершенно серьёзным видом произнесла:"
    cs_ls "Добрый день, товарищи инженеры."
    cs_narrator "Электроник моргнул."
    show el smile pioneer far at cs_actor_far_right
    cs_el "Э-э… привет."
    cs_narrator "Шурик отложил деталь."
    show sh normal pioneer far at cs_actor_far_left
    cs_sh "Вы к кому?"
    cs_ls "Лена Соколова."
    cs_narrator "Я указала на Дарью."
    cs_ls "А это Даша."
    show cs_darya shrug pioneer far at cs_darya_far_center
    cs_da "Дарья."
    cs_narrator "Электроник улыбнулся."
    cs_el "Я Сергей. Но все зовут Электроником."
    cs_sh "А я Шурик."
    cs_th "Какая неожиданность."
    cs_narrator "Я кивнула."
    cs_ls "Очень приятно."
    cs_narrator "Шурик посмотрел на нас внимательнее."
    cs_sh "Вы новенькие?"
    cs_ls "Совершенно верно. Прибыли сегодня."
    cs_narrator "Электроник сразу оживился."
    show el surprise pioneer far at cs_actor_far_right
    cs_el "А записаться в кружок хотите?"
    cs_narrator "Я перевела взгляд на рабочий стол."
    cs_narrator "На нём лежали провода, инструменты, платы, резисторы, транзисторы и какие-то недособранные устройства."
    cs_narrator "И вот тут мне стало действительно интересно."
    cs_narrator "Не потому, что передо мной находились персонажи знакомой игры."
    cs_narrator "А потому, что всё это была настоящая техника."
    cs_narrator "Можно было взять деталь."
    cs_narrator "Посмотреть маркировку."
    cs_narrator "Измерить напряжение."
    cs_narrator "И, возможно, даже заставить что-нибудь работать."
    cs_ls "Пока скорее за консультацией."
    cs_narrator "Шурик приподнял бровь."
    cs_sh "По какому вопросу?"
    cs_narrator "Я подошла к столу."
    cs_ls "Для начала хочу отметить, что здесь весьма прилично оборудовано."
    show el smile pioneer far at cs_actor_far_right
    cs_narrator "Электроник довольно улыбнулся."
    cs_el "Мы стараемся!"
    cs_narrator "Я посмотрела на паяльник."
    cs_narrator "На инструменты."
    cs_narrator "На стоявший в углу блок питания."
    cs_ls "Даже лаборатория почти полноценная."
    show el surprise pioneer far at cs_actor_far_right
    cs_el "А ты разбираешься в электронике?"
    cs_narrator "Я выдержала небольшую паузу."
    cs_ls "На уровне человека, который понимает, что телефон нельзя подключать напрямую к розетке."
    show sh smile pioneer far at cs_actor_far_left
    cs_narrator "Шурик усмехнулся."
    show sh normal pioneer far at cs_actor_far_left
    cs_sh "Уже неплохо."
    cs_ls "Спасибо. Родители были бы мной горды."
    cs_narrator "Дарья тихо добавила:"
    cs_da "Особенно если вспомнить, зачем мы сюда пришли."
    cs_narrator "Я взглянула на неё."
    cs_ls "Не мешай научному процессу."
    cs_da "Я пока только наблюдаю."
    show el laugh pioneer far at cs_actor_far_right
    cs_narrator "Электроник рассмеялся."
    show el surprise pioneer far at cs_actor_far_right
    cs_el "Так что у вас случилось?"
    cs_narrator "Я посмотрела на Шурика."
    cs_narrator "Затем на Электроника."
    cs_narrator "Пожалуй, пора было переходить к делу."
    return
