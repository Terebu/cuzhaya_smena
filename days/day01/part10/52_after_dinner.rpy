# -*- coding: utf-8 -*-
label cs_day01_52:
    $ save_name = "Чужая смена — День 1: После ужина"
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("bg int_dining_hall_sunset")
    scene bg int_dining_hall_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    label cs_check_day01_part10_start:
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/dining_hall_full.ogg":
        play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.5 fadein 1.5
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Ужин закончился без происшествий."
    cs_narrator "Что, учитывая события последних нескольких часов, уже можно было считать достижением."
    cs_narrator "Я отодвинула пустую тарелку и допила компот."
    cs_narrator "Дарья сидела напротив, наблюдая за тем, как пионеры постепенно расходятся по своим делам."
    cs_narrator "За соседним столом кто-то спорил о предстоящих соревнованиях. У выхода смеялись девочки. Где-то звякнула посуда."
    cs_narrator "Всё было совершенно обыкновенным."
    cs_th "Никаких путешествий во времени."
    cs_th "Никаких загадочных автобусов."
    cs_th "Просто ужин в пионерском лагере."
    cs_th "По крайней мере, для всех остальных."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну что, теперь в домик?"
    cs_narrator "Я задумалась."
    cs_ls "Вообще-то у меня появилась ещё одна идея."
    cs_narrator "Дарья медленно положила ложку."
    # cs_darya_variety: reaction
    show cs_darya serious pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_ls "Что?"
    cs_da "Мы сегодня уже ходили к двум инженерам и пытались объяснить им устройство смартфона."
    cs_ls "Вполне плодотворный визит."
    cs_da "А потом ты полчаса рассказывала, как работают компьютерные сети."
    cs_ls "Просветительская деятельность."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Я улыбнулась."
    cs_ls "Хорошо. В этот раз никаких лекций."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И куда ты собралась?"
    cs_ls "В библиотеку."
    # cs_darya_variety: reaction
    show cs_darya surprise_hand pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья удивлённо моргнула."
    cs_da "Зачем?"
    cs_narrator "Я поставила стакан на стол."
    cs_ls "Хочу посмотреть местные газеты, журналы. Может, найти календарь."
    cs_da "Мы ведь уже узнали год."
    cs_ls "Узнали, какой год называют местные жители. Это немного другое."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она задумалась."
    cs_ls "Шурик и Электроник сказали, что сейчас тысяча девятьсот восьмидесятый. Но я бы хотела проверить ещё несколько независимых источников."
    cs_da "Думаешь, они могли ошибиться?"
    cs_ls "Скорее думаю, что нам стоит перестать воспринимать любое совпадение с игрой как окончательное доказательство."
    cs_narrator "Дарья кивнула."
    cs_da "Разумно."
    cs_narrator "Я поднялась."
    cs_ls "Вот. Иногда мои идеи бывают полезными."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Иногда."
    cs_ls "Прошу зафиксировать положительную оценку."
    cs_narrator "Она рассмеялась."
    cs_narrator "Мы направились к выходу."
    return
