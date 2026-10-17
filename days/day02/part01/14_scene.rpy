# -*- coding: utf-8 -*-
label cs_day02_14:
    $ save_name = "Чужая смена — День 2: Завтрак всё-таки состоялся"
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
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/dining_hall_full.ogg":
        play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    label cs_check_breakfast_s14:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Остаток завтрака прошёл неожиданно спокойно."
    cs_narrator "Семён рассказывал о вчерашних поручениях."
    cs_narrator "Дарья поинтересовалась, где в лагере можно достать бумагу и карандаши."
    cs_narrator "Я вспомнила, что в собственном домике у нас лежит журнал наблюдений, который хотелось бы продолжать."
    cs_narrator "Разговор постепенно перешёл на обычные вещи."
    cs_narrator "И я поймала себя на странной мысли."
    cs_narrator "Мы сидели втроём за столом."
    cs_narrator "Ели кашу."
    cs_narrator "Обсуждали планы."
    cs_narrator "Иногда шутили."
    cs_narrator "Совершенно обычный завтрак."
    cs_narrator "Если не считать того, что все трое оказались здесь после поездки на одном и том же автобусе из разных лет."
    cs_th "Мелкая техническая особенность."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она что-то объясняла Семёну, слегка жестикулируя."
    cs_narrator "Иногда поправляла красные волосы, падавшие на лицо."
    cs_narrator "И больше не казалась той незнакомой девушкой, с которой я вчера случайно оказалась рядом в автобусе."
    cs_narrator "Мы действительно начинали узнавать друг друга."
    cs_narrator "Не по воспоминаниям об игре."
    cs_narrator "Не по заранее известному сценарию."
    cs_narrator "Просто разговаривая."
    cs_th "Пожалуй, Даша была права."
    cs_th "Не каждую минуту нужно пытаться разгадать загадку."
    cs_th "Иногда можно просто позавтракать."
    cs_narrator "Семён поднялся первым."
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
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
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
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ладно, пойдёмте? Скоро линейка."
    cs_narrator "Я посмотрела на пустую тарелку."
    cs_ls "Секунду."
    cs_narrator "Допила напиток."
    cs_narrator "Поставила стакан на поднос."
    cs_narrator "Поднялась."
    cs_ls "Всё. Граждане, приём пищи завершён успешно."
    cs_narrator "Дарья усмехнулась."
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
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Без чрезвычайных происшествий?"
    cs_narrator "Я задумалась."
    cs_ls "Почти."
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
    show cs_semen smile pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что значит «почти»?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Ты едва не стал участником утреннего физкультурного соревнования."
    cs_narrator "Он закрыл глаза."
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
    cs_sy "Господи."
    cs_narrator "Я улыбнулась."
    cs_ls "Не переживай. Заявку пока не утвердили."
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Мы отнесли подносы."
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
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
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    cs_narrator "Затем направились к выходу."
    cs_narrator "Солнце уже поднялось достаточно высоко."
    label cs_check_breakfast_square:
    cs_narrator "На площади постепенно собирались пионеры."
    cs_narrator "Где-то впереди слышался голос Ольги Дмитриевны."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Потом на Дарью."
    cs_th "Ну что ж."
    cs_th "Первое утреннее дело завершено."
    cs_th "Теперь посмотрим, какой план на день подготовило местное руководство."
    # cs_presence_keep: hide cs_darya
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
    $ cs_breakfast_live = False
    return
