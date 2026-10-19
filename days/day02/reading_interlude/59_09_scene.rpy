# -*- coding: utf-8 -*-
label cs_day02_reading_09:
    $ save_name = "Чужая смена — Тишина на троих: Не два разных человека"
    $ cs_part08_live = False
    $ cs_reading_live = True
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ cs_reading_book_location = "lena_hand"
    play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)
    play music "sound/music/a_promise_from_distant_days.ogg" fadein 2.5
    $ renpy.music.set_volume(0.12, channel="music", delay=1.0)
    label cs_check_reading_09:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Снаружи воздух показался неожиданно тёплым."
    cs_narrator "После прохладной библиотеки даже обычный ветер ощущался иначе."
    cs_narrator "Я осторожно прижала книгу к боку здоровой рукой."
    cs_narrator "Дарья шла рядом."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Не потому, что не знали, о чём говорить."
    cs_narrator "Просто после библиотеки совершенно не хотелось сразу возвращаться к бесконечному потоку слов."
    cs_narrator "Даша первой нарушила тишину."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_narrator "Она немного улыбнулась."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я сегодня увидела тебя совсем другой."
    cs_narrator "Я задумалась."
    cs_ls "В каком смысле?"
    cs_da "Ну… вчера ты постоянно разговаривала. Шутила. Задавала вопросы. Сегодня утром тоже."
    cs_narrator "Она посмотрела на книгу в моей руке."
    cs_da "А в библиотеке просто сидела и читала."
    cs_narrator "Я кивнула."
    cs_ls "Обычно я и бываю такой."
    cs_narrator "Дарья посмотрела на меня."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Правда?"
    cs_narrator "Я улыбнулась."
    cs_ls "Угу."
    cs_narrator "Немного подумала."
    cs_ls "Могу часами рисовать, слушать музыку, читать. Иногда мне вообще не хочется ни с кем разговаривать."
    cs_narrator "Она задумалась."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А последние два дня?"
    cs_narrator "Я посмотрела на деревья."
    cs_narrator "Потом на дорожку."
    cs_th "Хороший вопрос."
    cs_ls "Последние два дня у меня, кажется, не было ни одной нормальной возможности всё обдумать."
    cs_narrator "Я чуть улыбнулась."
    cs_ls "Зима. Автобус. Лето. Лагерь. Люди, которых я узнавала по игре."
    cs_narrator "Пауза."
    cs_ls "И ты."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Я?"
    cs_narrator "Я кивнула."
    cs_ls "Угу. Девушка, с которой я познакомилась буквально вчера, а сегодня уже делю домик и пытаюсь разобраться в совершенно невероятной ситуации."
    cs_narrator "Она немного помолчала."
    cs_narrator "Затем улыбнулась."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Если честно, для меня всё примерно так же."
    cs_narrator "Я посмотрела на неё."
    cs_da "Просто я, наверное, немного иначе реагирую."
    cs_ls "Ты чаще сначала думаешь, а потом говоришь."
    cs_narrator "Она тихо рассмеялась."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А ты наоборот?"
    cs_narrator "Я задумалась."
    cs_ls "Иногда."
    cs_narrator "Потом улыбнулась."
    cs_ls "Довольно часто."
    cs_narrator "Дарья тоже улыбнулась."
    cs_narrator "Мы продолжили идти."
    cs_narrator "Через некоторое время она сказала:"
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Знаешь, мне понравилось сидеть рядом с тобой в библиотеке."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даже без разговоров?"
    cs_narrator "Она кивнула."
    cs_da "Особенно без необходимости всё время о чём-то говорить."
    cs_narrator "Я немного помолчала."
    cs_th "Вот это было неожиданно приятно слышать."
    cs_ls "Мне тоже."
    cs_narrator "Дарья улыбнулась."
    cs_narrator "Мы прошли ещё немного."
    cs_narrator "Потом она посмотрела на мою книгу."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Будешь читать вечером?"
    cs_narrator "Я задумалась."
    cs_ls "Наверное. Хотя сначала концерт."
    cs_da "А потом?"
    cs_ls "Посмотрим. Может, немного почитаю перед сном."
    cs_narrator "Она кивнула."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не засиживайся допоздна."
    cs_narrator "Я посмотрела на неё."
    cs_ls "И ты туда же?"
    cs_narrator "Дарья рассмеялась."
    cs_da "Просто хочу, чтобы ты завтра не уснула за завтраком."
    cs_narrator "Я немного подумала."
    cs_ls "После сегодняшнего это было бы вполне заслуженно."
    cs_narrator "Она улыбнулась."
    cs_narrator "И вдруг я поняла, что весь этот разговор ощущается совершенно иначе, чем наши вчерашние перепалки."
    cs_narrator "Никакого напряжения."
    cs_narrator "Никакой необходимости немедленно пошутить."
    cs_narrator "Никаких попыток превратить каждую фразу в намёк."
    cs_narrator "Мы просто узнавали друг друга."
    cs_narrator "Медленно."
    cs_narrator "Без спешки."
    cs_th "Возможно, именно так и должно быть."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Даш."
    cs_narrator "Она повернулась."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да?"
    cs_ls "Если я иногда буду молчать, это не значит, что мне с тобой скучно."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_narrator "Потом улыбнулась."
    # cs_presence_keep: hide cs_zhenya
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я поняла."
    cs_narrator "Немного помолчала."
    cs_da "И тебе не обязательно постоянно меня развлекать."
    cs_narrator "Я усмехнулась."
    cs_ls "Но иногда можно?"
    cs_narrator "Она рассмеялась."
    cs_da "Иногда можно."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    cs_narrator "Мы продолжили идти к столовой."
    # cs_director_begin: REFLECTIVE_SHOT: Evening camp and accepting quietness
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_39ee63d976:
    # cs_director_end
    cs_narrator "Мимо уже проходили пионеры, собиравшиеся к ужину."
    cs_narrator "Лагерь постепенно переходил от дневных занятий к вечерним."
    cs_narrator "А я несла под мышкой книгу и думала, что за последние полчаса узнала о себе не меньше, чем о людях вокруг."
    cs_th "Мне действительно нравится шутить."
    cs_th "Нравится разговаривать."
    cs_th "Нравится иногда выводить Семёна из равновесия."
    cs_th "Но ещё мне нравится тишина."
    cs_th "И, оказывается, это совершенно не противоречит одно другому."
    stop music fadeout 2.0
    label cs_check_reading_walk_done:
    pause 0.5
    return
