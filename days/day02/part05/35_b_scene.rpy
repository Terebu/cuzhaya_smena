# -*- coding: utf-8 -*-
label cs_day02_35b:
    $ save_name = "Чужая смена — День 2: Разделение труда"
    $ cs_part04_live = False
    $ cs_part05_live = True
    if not renpy.showing("cs_cg_poster_planning_day"):
        $ cs_director_scene("cs_cg_poster_planning_day")
        scene cs_cg_poster_planning_day
    $ cs_part05_cg = True
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
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
    $ cs_part05_cast = []
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() is None:
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    label cs_check_part05_s35b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на незаконченный рисунок."
    cs_narrator "Затем на Семёна."
    cs_ls "Давай ты займёшься заголовком, а я закончу иллюстрацию."
    cs_narrator "Он кивнул."
    cs_sy "Хорошо."
    cs_narrator "Дарья придвинула ему линейку."
    cs_da "Только сначала наметь расположение букв. Иначе они могут не поместиться."
    cs_sy "Понял."
    cs_narrator "Он начал аккуратно размечать заголовок."
    cs_narrator "А я вернулась к рисунку гитары."
    cs_narrator "Нужно было сделать его достаточно заметным, но не перегрузить лист."
    cs_narrator "Я набросала корпус."
    cs_narrator "Потом гриф."
    cs_narrator "Добавила несколько небольших нот сбоку."
    cs_narrator "Не особенно подробно."
    cs_narrator "Главное, чтобы с расстояния всё легко узнавалось."
    cs_narrator "Через некоторое время Семён поднял лист."
    cs_sy "Ну как?"
    cs_narrator "Я посмотрела на надпись."
    cs_narrator "Буквы были немного неровными, но читались вполне хорошо."
    cs_ls "Отлично."
    cs_narrator "Он удивился."
    cs_sy "Серьёзно?"
    cs_ls "Ага. Особенно если учесть, что мы не собираемся печатать это в типографии."
    cs_narrator "Дарья улыбнулась."
    cs_da "Главное, что видно издалека."
    cs_narrator "Семён кивнул."
    cs_sy "Значит, справился."
    cs_narrator "Я посмотрела на общий результат."
    cs_ls "Справились."
    cs_narrator "Мы отложили карандаши."
    return
