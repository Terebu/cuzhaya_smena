# -*- coding: utf-8 -*-
label cs_day02_10:
    $ save_name = "Чужая смена — День 2: Утреннее население «Совёнка»"
    $ cs_breakfast_live = True
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_breakfast_s10:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "К столовой мы подошли как раз тогда, когда лагерь окончательно проснулся."
    cs_narrator "На крыльце толпились пионеры. Кто-то обсуждал предстоящие занятия, кто-то жаловался на ранний подъём, а несколько девочек оживлённо спорили о чём-то настолько важном, что даже не заметили, как мы прошли мимо."
    cs_narrator "Я вдохнула запах свежего хлеба."
    cs_th "Вот."
    cs_th "Наконец-то первое действительно понятное событие за утро."
    cs_narrator "После пробежки, турников и незапланированного осмотра ворот организм вполне справедливо напоминал, что одной физической активностью сыт не будешь."
    cs_narrator "Дарья шла рядом."
    cs_narrator "В отличие от меня, она не выглядела человеком, готовым прямо сейчас повторить утреннюю тренировку."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты всё ещё слишком бодрая."
    cs_narrator "Я повернулась к ней."
    cs_ls "А ты всё ещё прекрасно выглядишь. Предлагаю считать это взаимной компенсацией."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом едва заметно улыбнулась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "С утра уже начинаешь?"
    cs_ls "Вообще-то я начала значительно раньше."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я заметила."
    cs_narrator "Я придержала перед ней дверь."
    cs_ls "Прошу, товарищ соседка. Завтрак подан."
    cs_da "Спасибо, товарищ спортсменка."
    play sound "sound/sfx/open_door_1.ogg"
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/dining_hall_full.ogg":
        play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/feeling_good.ogg":
        play music "sound/music/feeling_good.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_breakfast:
    cs_narrator "Мы вошли."
    cs_narrator "Внутри уже было шумно."
    cs_narrator "Звенели ложки."
    cs_narrator "Кто-то двигал стулья."
    cs_narrator "В дальнем конце зала разговаривали несколько пионеров, а возле раздачи постепенно собиралась очередь."
    cs_narrator "Мы взяли подносы и получили завтрак."
    cs_narrator "Я посмотрела на кашу."
    cs_narrator "Потом на хлеб."
    cs_narrator "Потом на стакан с напитком."
    cs_th "Неплохо."
    cs_th "Сервис без интернета, зато питание включено."
    cs_narrator "Дарья заметила моё выражение лица."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Думаю, что бесплатный завтрак — пока одно из наиболее убедительных преимуществ нашего пребывания здесь."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    $ cs_breakfast_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Если не считать того, что нас никто не спрашивал, хотим ли мы здесь оставаться."
    cs_narrator "Я кивнула."
    cs_ls "Это, безусловно, портит оценку обслуживания."
    cs_narrator "Она тихо рассмеялась."
    cs_narrator "Я начала искать свободный стол."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    $ cs_breakfast_un_here = cs_met_un and cs_friend_un >= 1
    cs_narrator "И почти сразу увидела Семёна."
    cs_narrator "Он уже сидел с завтраком, разглядывая содержимое тарелки с таким видом, будто пытался выяснить, насколько серьёзно настроено местное общественное питание."
    if cs_breakfast_un_here:
        cs_narrator "Рядом с ним сидела Лена Тихонова. Она подняла взгляд и приветственно кивнула нам."
    cs_th "О."
    cs_th "Рабочая группа в сборе."
    cs_narrator "Я направилась к нему."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Доброе утро ещё раз."
    cs_narrator "Семён поднял голову."
    cs_narrator "Увидел меня."
    cs_narrator "Затем Дарью."
    cs_narrator "И немного обречённо вздохнул."
    cs_sy "Привет."
    cs_narrator "Я остановилась."
    cs_ls "Какое выразительное приветствие."
    cs_sy "Просто я с утра тебя уже видел."
    cs_ls "И до сих пор не восстановился?"
    cs_sy "Ты тогда выглядела так, будто уже прожила половину дня."
    cs_narrator "Я кивнула."
    cs_ls "Почти так и есть."
    cs_narrator "Дарья поставила поднос на свободное место."
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
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Можно к тебе?"
    cs_sy "Конечно."
    label cs_check_breakfast_table:
    cs_narrator "Я устроилась рядом с ней."
    cs_th "Ну что ж."
    cs_th "Второй день официально перешёл к фазе коллективного завтрака."
    return
