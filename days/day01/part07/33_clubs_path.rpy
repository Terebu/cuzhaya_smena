# -*- coding: utf-8 -*-
label cs_day01_33:
    $ save_name = "Чужая смена — День 1: Клубы"
    scene bg ext_houses_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    cs_narrator "Мы вышли из домика."
    cs_narrator "Солнце по-прежнему ярко освещало дорожки."
    cs_narrator "После обеда лагерь немного опустел: кто-то разошёлся по кружкам, кто-то отдыхал, а кто-то продолжал носиться по территории с такой энергией, будто жара совершенно не существовала."
    cs_narrator "Я шла впереди, стараясь сопоставить дорожки с картой из игры."
    cs_narrator "Дарья держалась рядом."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    cs_da "Лен."
    cs_ls "М?"
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Ты точно знаешь дорогу?"
    cs_ls "Приблизительно."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    cs_da "Меня немного беспокоит это слово."
    cs_ls "Меня тоже. Но пока мы движемся в верном направлении."
    scene cs_camp_path_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.0)
    cs_narrator "Мы свернули за один из домиков."
    cs_narrator "Потом ещё раз."
    scene bg ext_clubs_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.0)
    cs_narrator "Через несколько минут показалось знакомое здание."
    cs_narrator "Я сразу указала на него."
    cs_ls "Вот."
    cs_narrator "Дарья посмотрела на фасад."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Уверена?"
    cs_ls "Теперь да."
    cs_narrator "На двери висела табличка кружков."
    cs_narrator "Изнутри доносились голоса."
    cs_narrator "Я остановилась перед входом."
    cs_th "Ну здравствуйте, товарищи инженеры."
    cs_th "Посмотрим, насколько далеко продвинулся местный научно-технический прогресс."
    stop music fadeout 2.0
    play sound "sound/sfx/knock_door7_polite.ogg"
    cs_narrator "Я постучала."
    cs_narrator "Изнутри послышалось:"
    show el smile pioneer far at cs_actor_right
    # cs_composition: regroup
    show cs_darya thinking pioneer normal at cs_darya_normal_left
    cs_el "Входите!"
    play sound "sound/sfx/open_door_clubs.ogg"
    scene bg int_clubs_male_day
    show cs_darya shrug pioneer far at cs_darya_far_center
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.5 fadein 2.0
    return
