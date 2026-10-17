# -*- coding: utf-8 -*-
label cs_day01_43:
    $ save_name = "Чужая смена — День 1: На площади"
    $ cs_director_scene("bg ext_square_sunset")
    scene bg ext_square_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.5)
    label cs_check_day01_part08_square:
    $ renpy.music.set_volume(0.28,delay=1.0,channel="music")
    play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 3.0
    $ renpy.music.set_volume(0.22,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда мы вышли на площадь, солнце уже опустилось достаточно низко."
    cs_narrator "Тени деревьев вытянулись почти до противоположного края дорожки."
    cs_narrator "На площади было заметно спокойнее, чем днём."
    cs_narrator "Несколько пионеров сидели на скамейках."
    cs_narrator "Кто-то направлялся к домикам."
    cs_narrator "У памятника разговаривали две девочки."
    cs_narrator "А неподалёку, на одной из скамеек, сидел знакомый парень."
    cs_narrator "Семён."
    cs_narrator "Он смотрел куда-то в сторону лагеря, задумчиво подперев щёку рукой."
    cs_narrator "Я остановилась."
    cs_th "О."
    cs_th "Председатель нашей рабочей группы обнаружен."
    cs_narrator "Дарья заметила, куда я смотрю."
    # cs_darya_variety: reaction
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не начинай."
    cs_narrator "Я повернулась к ней."
    cs_ls "Что именно?"
    cs_da "У тебя опять такое выражение лица."
    cs_ls "Какое?"
    cs_da "Как будто придумала что-то, о чём окружающие скоро пожалеют."
    cs_narrator "Я задумалась."
    cs_ls "Несправедливая характеристика."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Зато точная."
    cs_narrator "Я усмехнулась."
    cs_narrator "Потом негромко спросила:"
    cs_ls "Даш, можно я немного его помучаю вопросами? Только без подробностей нашего разговора."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Несколько секунд размышляла."
    cs_da "Если действительно без подробностей."
    cs_ls "Договорились."
    show cs_semen thinking_down pioneer normal at cs_semen_normal_left
    # cs_composition: regroup
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_part08_semen:
    cs_narrator "Мы подошли к скамейке."
    cs_ls "Товарищ Семён."
    cs_narrator "Он поднял голову."
    cs_narrator "Увидел меня."
    cs_narrator "Затем Дарью."
    cs_narrator "После чего вздохнул с таким выражением лица, будто заранее приготовился к очередному необычному разговору."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что на этот раз?"
    cs_ls "Почему сразу «на этот раз»?"
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Потому что каждый раз, когда ты ко мне подходишь, у тебя возникает какой-нибудь странный вопрос."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Наблюдательность развита прекрасно."
    cs_narrator "Семён посмотрел на Дарью."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вы откуда?"
    cs_da "Из кружка электроники."
    cs_narrator "Он перевёл взгляд на меня."
    cs_sy "Зачем?"
    cs_ls "Проводили консультацию по восстановлению связи с цивилизацией."
    cs_sy "То есть?"
    cs_narrator "Я достала телефон."
    cs_narrator "Показала его."
    cs_ls "Пытаемся зарядить."
    cs_narrator "Семён удивился."
    cs_sy "Здесь?"
    cs_ls "Представь себе. Электричество в этой эпохе уже изобрели."
    cs_narrator "Он усмехнулся."
    cs_sy "А зарядка?"
    cs_ls "Пока на стадии проектирования."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ясно."
    cs_narrator "Я убрала телефон обратно."
    cs_ls "Завтра продолжим технические испытания."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "И что, Шурик согласился?"
    cs_ls "Даже слишком заинтересовался."
    cs_narrator "Семён покачал головой."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что-то мне подсказывает, что теперь он до завтра не успокоится."
    cs_ls "Прекрасно. Значит, вопрос поставлен на контроль."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    return
