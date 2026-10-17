# -*- coding: utf-8 -*-
label cs_day02_58:
    $ save_name = "Чужая смена — День 2: Знакомые очки"
    $ cs_part07_live = False
    $ cs_part08_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part08_s58:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Через некоторое время я осторожно поднялась с лавочки."
    cs_narrator "Локоть уже почти не беспокоил, если его не задевать."
    cs_narrator "Впрочем, проверять это специально я не собиралась."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Куда теперь?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Хороший вопрос."
    cs_da "Опасное начало ответа."
    cs_narrator "Я улыбнулась."
    cs_ls "Вообще-то собиралась предложить ещё немного погулять."
    cs_sy "Без пробежек?"
    cs_ls "С медицинской точки зрения — да."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он усмехнулся."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Тогда звучит разумно."
    cs_narrator "Я уже собиралась что-нибудь ответить, когда заметила знакомую фигуру."
    cs_narrator "Со стороны библиотеки шла девушка в очках."
    cs_narrator "Тёмные волосы."
    cs_narrator "Пионерская форма."
    cs_narrator "Несколько книг под мышкой."
    cs_narrator "Походка человека, который точно знает, куда направляется, и не особенно любит, когда его задерживают без причины."
    cs_th "О."
    cs_th "Женя."
    cs_narrator "Я замедлила шаг."
    cs_narrator "Дарья проследила за моим взглядом."
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не говори, что собираешься снова устраивать библиотечное расследование."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Никаких расследований."
    cs_narrator "Она приподняла бровь."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Правда?"
    cs_ls "Ну, почти никаких."
    cs_narrator "Семён заметил Женю."
    cs_narrator "Потом посмотрел на меня."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А что с Женей?"
    cs_narrator "Я задумалась."
    cs_th "Вот ведь."
    cs_narrator "Вчера мы провели довольно необычный разговор."
    cs_narrator "Я рассказала ей о знакомой игре."
    cs_narrator "Она вполне справедливо потребовала перестать говорить загадками."
    cs_narrator "И, что самое удивительное, даже не выгнала нас из библиотеки."
    cs_narrator "Хотя причин у неё было достаточно."
    cs_th "Может, стоит подойти и нормально поздороваться?"
    cs_th "Без шуток про книжную полицию."
    cs_th "Без рассказов о будущем."
    cs_th "Просто поблагодарить человека, который вчера нашёл время меня выслушать."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она ждала."
    cs_narrator "Не мешала."
    cs_narrator "Не пыталась решить за меня."
    cs_narrator "Семён тоже ничего не сказал."
    cs_th "А ведь это хорошая возможность."
    cs_th "Можно спокойно пройти дальше."
    cs_th "А можно попытаться сделать ещё один маленький шаг навстречу человеку, которого пока знаю совсем плохо."
    return
