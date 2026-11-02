# -*- coding: utf-8 -*-
label cs_day01_33:
    $ save_name = "Чужая смена — День 1: Клубы"
    $ cs_director_scene("bg ext_houses_day")
    scene bg ext_houses_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы вышли из домика."
    cs_narrator "После обеда лагерь опустел: кто-то разошёлся по кружкам, кто-то отдыхал. Лишь немногие носились по жаре."
    cs_narrator "Я сверялась с памятью, Дарья шла рядом."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_ls "М?"
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты точно знаешь дорогу?"
    cs_ls "Приблизительно."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Меня немного беспокоит это слово."
    cs_ls "Меня тоже. Но пока мы движемся в верном направлении."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    cs_narrator "Мы сделали ещё два поворота."
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    cs_narrator "Показалось знакомое здание. Я указала на него."
    cs_ls "Вот."
    cs_narrator "Дарья посмотрела на фасад."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Уверена?"
    cs_ls "Теперь да."
    cs_narrator "На двери висела табличка кружков, изнутри доносились голоса."
    cs_th "Здравствуйте, товарищи инженеры. Посмотрим, что вы умеете."
    stop music fadeout 2.0
    play sound "sound/sfx/knock_door7_polite.ogg"
    cs_narrator "Я постучала."
    show cs_darya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Входите!"
    play sound "sound/sfx/open_door_clubs.ogg"
    $ cs_director_scene("bg int_clubs_male_day")
    scene bg int_clubs_male_day
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.5 fadein 2.0
    return
