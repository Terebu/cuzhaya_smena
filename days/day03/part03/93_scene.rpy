# -*- coding: utf-8 -*-
label cs_day03_93:
    $ save_name = "Чужая смена — День 3: Какая-то слишком тихая Соколова"
    cs_narrator "Завтрак оказался вполне приличным."
    cs_narrator "Каша была горячей."
    cs_narrator "Хлеб — свежим."
    cs_narrator "А чай, к моему удивлению, даже не пытался изображать универсальный растворитель неизвестного происхождения."
    cs_narrator "Я спокойно ела."
    $ cs_reflective_focus()
    with cs_sprite_leave
    label cs_check_day03_93_reflection:
    cs_narrator "Время от времени смотрела в окно."
    cs_narrator "На площадь."
    cs_narrator "На проходящих мимо пионеров."
    cs_narrator "На солнце, которое постепенно поднималось выше деревьев."
    cs_th "Забавно."
    cs_th "Ещё позавчера мне хотелось постоянно проверять, настоящие ли здесь люди и вещи."
    cs_th "А теперь я просто сижу и завтракаю."
    $ cs_frame_focus(cs_day03_p3_breakfast_cast())
    with cs_sprite_change
    label cs_check_day03_93_dialogue:
    cs_da "Лен."
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_da "Ты сегодня действительно какая-то задумчивая."
    cs_narrator "Я немного улыбнулась."
    cs_ls "Просто завтракаю."
    cs_narrator "Она приподняла бровь."
    cs_da "Без дополнительной культурной программы?"
    cs_ls "Представляешь себе."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_ls "К тому же я обещала сегодня вести себя немного спокойнее."
    cs_da "А я думала, это касается только Жени."
    cs_narrator "Я задумалась."
    cs_ls "Вообще да."
    cs_narrator "Потом посмотрела на неё."
    cs_ls "Но ты ведь не станешь жаловаться, если я пять минут не буду тебя поддевать?"
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Не стану."
    cs_ls "Вот и прекрасно."
    if cs_day03_mz_breakfast_together:
        if renpy.showing("cs_zhenya"):
            show cs_zhenya thoughtful pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя отложила ложку."
        cs_narrator "Посмотрела на меня."
        cs_mz "А почему ты вообще решила так себя вести?"
        cs_narrator "Я подняла взгляд."
        cs_ls "Как?"
        cs_mz "Спокойнее."
        cs_narrator "Я немного подумала."
        cs_ls "Наверное, потому что за два дня успела немного привыкнуть к лагерю."
        cs_narrator "Она кивнула."
        cs_mz "А раньше?"
        cs_narrator "Я улыбнулась."
        cs_ls "Раньше я слишком много всего пыталась понять одновременно."
        cs_narrator "Немного помолчала."
        cs_ls "Когда нервничаю, часто начинаю много говорить. Иногда даже больше, чем нужно."
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Это заметно."
        cs_narrator "Я усмехнулась."
        cs_ls "Спасибо за профессиональное заключение."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Она слегка улыбнулась."
        cs_mz "Пожалуйста."
        cs_narrator "Дарья тихо рассмеялась."
        cs_narrator "Я продолжила уже серьёзнее."
        cs_ls "Но вообще я люблю тишину. И книги. И возможность какое-то время ни с кем не разговаривать."
        cs_narrator "Женя кивнула."
        cs_mz "Вот это мне понятно."
        cs_narrator "Я улыбнулась."
        cs_ls "Я заметила."
        cs_narrator "Она вернулась к завтраку."
        cs_narrator "И разговор на некоторое время закончился."
        cs_narrator "Без неловкости."
        cs_narrator "Без ощущения, что кто-то обязан немедленно продолжить."
    cs_narrator "Через несколько минут мимо нашего стола прошёл Семён."
    cs_narrator "Он уже успел получить завтрак."
    cs_narrator "Заметил нас."
    cs_narrator "И остановился."
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    with None
    show cs_semen neutral pioneer normal at cs_day03_p3_actor_enter(0.25)
    $ renpy.pause(0.30, hard=True)
    show cs_semen neutral pioneer normal at Transform(xpos=0.25, xanchor=0.5, ypos=1.60, yanchor=1.0, zoom=1.0, alpha=1.0)
    $ cs_presence_stage()
    with None
    label cs_check_day03_93_semen:
    cs_sy "Вы здесь."
    cs_narrator "Я посмотрела на него."
    cs_ls "Доброе утро ещё раз."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он усмехнулся."
    cs_sy "Да, мы уже виделись."
    cs_narrator "Я кивнула."
    cs_ls "Приятно, что ты запомнил."
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Семён посмотрел на неё."
    cs_narrator "Потом снова на меня."
    cs_sy "Сегодня с тобой действительно что-то необычное."
    cs_narrator "Я приподняла бровь."
    cs_ls "И что же?"
    cs_sy "Ты уже второй раз разговариваешь со мной практически нормально."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Совершенно серьёзно."
    cs_ls "Семён, ты сейчас жалуешься на недостаточное количество шуток в свой адрес?"
    cs_narrator "Он замолчал."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_sy "Нет. Просто удивляюсь."
    cs_narrator "Я кивнула."
    cs_ls "Тогда привыкай."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он усмехнулся."
    cs_sy "Постараюсь."
    $ cs_day03_semen_breakfast_joined = cs_friend_se >= 3
    if cs_day03_semen_breakfast_joined:
        label cs_check_day03_93_joined:
        cs_narrator "Семён посмотрел на свободный стул."
        cs_sy "Можно к вам?"
        cs_narrator "Я кивнула."
        cs_ls "Конечно."
        cs_narrator "Он устроился рядом."
        cs_narrator "Некоторое время мы ели молча."
        cs_narrator "Потом Семён посмотрел на меня."
        cs_sy "Кстати, спасибо, что утром спросила, как у меня дела."
        cs_narrator "Я подняла взгляд."
        cs_ls "Не за что."
        cs_narrator "Он немного помолчал."
        cs_sy "Просто… приятно знать, что можно нормально поговорить."
        cs_narrator "Я кивнула."
        cs_ls "Взаимно."
        cs_narrator "Немного подумала."
        cs_ls "Но если ты сейчас рассчитываешь, что я навсегда откажусь от шуток, вынуждена разочаровать."
        cs_narrator "Он улыбнулся."
        cs_sy "Даже не надеялся."
        cs_narrator "Дарья тихо рассмеялась."
        cs_th "Вот и хорошо."
        cs_th "Кажется, мы постепенно начинаем понимать друг друга."
    else:
        if renpy.showing("cs_semen"):
            show cs_semen smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Семён улыбнулся."
        cs_sy "Ладно, приятного аппетита."
        cs_da "И тебе."
        cs_ls "Спасибо."
        $ cs_frame_focus(cs_day03_p3_breakfast_cast())
        with cs_sprite_change
        label cs_check_day03_93_separate_semen:
        cs_narrator "Он направился к своему столу."
    cs_narrator "Я вернулась к завтраку."
    cs_th "Ну что ж."
    cs_th "Уже довольно неплохо."
    cs_th "Семён жив."
    cs_th "Мои шутки — тоже."
    cs_th "А Женя, кажется, даже начала привыкать к тому, что я способна не разговаривать каждые десять секунд."
    if cs_day03_semen_breakfast_joined:
        cs_narrator "Семён первым отложил ложку и поднялся."
        cs_sy "Я пока отнесу поднос."
        cs_narrator "Он забрал посуду и отошёл к стойке у выхода."
        $ cs_frame_focus(cs_day03_p3_breakfast_cast())
        with cs_sprite_leave
    label cs_check_day03_93_semen_offscreen:
    return
