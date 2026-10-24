# -*- coding: utf-8 -*-
label cs_day03_111:
    $ save_name = "Чужая смена — День 3: Свидетель без обвинения"
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    cs_narrator "У поворота мы снова увидели Семёна."
    cs_narrator "Он как раз выходил со стороны клубов."
    cs_narrator "В руках у него был какой-то небольшой свёрток."
    with None
    show cs_semen neutral pioneer normal at cs_day03_p3_actor_enter(0.25)
    $ renpy.pause(0.30,hard=True)
    show cs_semen neutral pioneer normal at Transform(xpos=0.25,xanchor=0.5,ypos=1.60,yanchor=1.0,zoom=1.0,alpha=1.0)
    $ cs_presence_stage()
    with None
    label cs_check_day03_111_semen:
    cs_narrator "Увидев нас, он остановился."
    cs_sy "О, вы ещё здесь?"
    cs_narrator "Я улыбнулась."
    cs_ls "А ты всё ещё выполняешь хозяйственные поручения?"
    cs_narrator "Он кивнул на свёрток."
    cs_sy "Ага. Отнести кое-что попросили."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Понимаю. Сегодня, кажется, весь лагерь работает в службе доставки."
    cs_narrator "Он посмотрел на меня."
    cs_narrator "Потом на Дарью."
    cs_sy "Вы куда ходили?"
    cs_narrator "Я совершенно спокойно ответила:"
    cs_ls "К Ольге Дмитриевне."
    cs_narrator "Он остановился."
    cs_narrator "Несколько секунд смотрел на меня."
    cs_sy "Зачем?"
    cs_narrator "Я поправила галстук."
    cs_ls "Предлагала помощь."
    if renpy.showing("cs_semen"):
        show cs_semen thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он прищурился."
    cs_sy "И всё?"
    cs_narrator "Я улыбнулась."
    cs_ls "Потом отнесли документы. Заглянули к Славе."
    cs_narrator "Семён продолжал смотреть с подозрением."
    cs_sy "Ты точно ничего не спрашивала про меня?"
    cs_narrator "Я задумалась."
    cs_th "Вот ведь."
    cs_th "Сам заинтересовался."
    cs_ls "Семён, ты сам сейчас поднял эту тему."
    cs_narrator "Он вздохнул."
    cs_sy "Значит, спрашивала."
    cs_narrator "Дарья отвернулась, пряча улыбку."
    cs_narrator "Я посмотрела на него."
    cs_ls "Только о том, как вы уживаетесь в одном домике."
    if renpy.showing("cs_semen"):
        show cs_semen awkward pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он закрыл глаза."
    cs_sy "Господи…"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Спокойно. Никаких компрометирующих сведений получено не было."
    cs_narrator "Он посмотрел на меня."
    cs_sy "А зачем они тебе вообще?"
    cs_narrator "Я совершенно серьёзно ответила:"
    cs_ls "Интересуюсь организацией быта трудящихся."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Семён несколько секунд смотрел на меня."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом неожиданно улыбнулся."
    cs_sy "Тогда начни с собственного домика."
    cs_narrator "Я приподняла бровь."
    cs_ls "В смысле?"
    cs_narrator "Он посмотрел на Дарью."
    cs_narrator "Потом снова на меня."
    cs_sy "Как вы там уживаетесь? Никто никого не будит раньше времени?"
    cs_narrator "Я замолчала."
    cs_th "О."
    cs_th "Контратака."
    cs_narrator "Дарья довольно улыбнулась."
    cs_da "Между прочим, сегодня Лена ушла гулять, пока я спала."
    cs_narrator "Семён посмотрел на меня."
    cs_sy "Вот как?"
    cs_narrator "Я выпрямилась."
    cs_ls "Оставила записку."
    cs_da "С обещанием не совершать подвигов."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён рассмеялся."
    cs_sy "И как, сдержала?"
    cs_narrator "Я кивнула."
    cs_ls "Полностью."
    cs_narrator "Он посмотрел на мою повязку."
    cs_sy "Надо же. Бывают чудеса."
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Неприятно видеть, как близкие знакомые так быстро осваивают искусство публичной критики."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Семён тоже."
    cs_narrator "Некоторое время мы стояли возле дорожки, обмениваясь вполне безобидными замечаниями."
    cs_narrator "Потом Семён посмотрел на свёрток."
    cs_sy "Ладно, мне пора. А то опять заставят искать меня по всему лагерю."
    cs_narrator "Я кивнула."
    cs_ls "Удачи."
    cs_narrator "Он посмотрел на меня."
    cs_sy "Спасибо."
    cs_narrator "Потом немного помолчал."
    cs_sy "Только, Лен…"
    cs_narrator "Я подняла взгляд."
    cs_ls "Да?"
    cs_sy "Давай всё-таки без расспросов о том, как я живу с Ольгой Дмитриевной."
    cs_narrator "Я посмотрела на него."
    if renpy.showing("cs_semen"):
        show cs_semen serious pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он говорил спокойно, но вполне серьёзно."
    cs_th "Ладно."
    cs_th "Кажется, шутка действительно исчерпала себя."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо. Больше не буду."
    if renpy.showing("cs_semen"):
        show cs_semen surprised pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён удивился."
    cs_sy "Серьёзно?"
    $ cs_semen_privacy_respected_day3 = True
    label cs_check_day03_111_boundary:
    cs_ls "Да. Ты попросил — я услышала."
    cs_narrator "Он немного помолчал."
    cs_narrator "Затем улыбнулся."
    cs_sy "Спасибо."
    cs_narrator "Я улыбнулась в ответ."
    cs_ls "Не за что."
    cs_narrator "Пауза."
    cs_narrator "Потом я добавила:"
    cs_ls "Но право шутить над твоей трудовой дисциплиной оставляю за собой."
    cs_narrator "Он рассмеялся."
    cs_sy "А вот это пожалуйста. Тут у меня хотя бы есть чем ответить."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    cs_narrator "Мы попрощались."
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_check_day03_111_semen_left:
    cs_narrator "Семён направился по дорожке."
    cs_narrator "Я проводила его взглядом."
    cs_th "Пожалуй, это было даже неплохо."
    cs_th "Необязательно выжимать из одной шутки всё, что только возможно."
    cs_th "Тем более теперь у меня есть достаточно материала для новых."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Ты действительно больше не будешь его этим дразнить?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_narrator "Она улыбнулась."
    cs_da "Растёшь."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Удивительно, правда? Всего третий день, а уже появляются признаки социальной адаптации."
    cs_narrator "Она рассмеялась."
    cs_narrator "Мы пошли дальше."
    return
