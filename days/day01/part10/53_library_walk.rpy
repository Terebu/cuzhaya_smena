# -*- coding: utf-8 -*-
label cs_day01_53:
    $ save_name = "Чужая смена — День 1: Последний посетитель"
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "На улице похолодало. Закат окрашивал дорожки оранжевым."
    cs_narrator "До библиотеки я теперь добиралась и без игровых фонов: дневная прогулка помогла."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты знаешь, какая здесь библиотека?"
    cs_ls "Была одна в оригинальной истории."
    cs_da "Значит, опять проверяем совпадения?"
    cs_ls "На этот раз с пользой для образования."
    cs_ls "И ещё мне любопытно познакомиться с местной библиотекаршей."
    cs_narrator "Дарья бросила на меня подозрительный взгляд."
    cs_da "Почему?"
    cs_ls "Женя."
    cs_da "Это имя?"
    cs_ls "Да. Она довольно строгая."
    cs_da "И?"
    cs_ls "Не особенно любит шум, беспорядок и людей, которые отвлекают её от работы."
    cs_narrator "Дарья медленно улыбнулась."
    # cs_darya_variety: reaction
    show cs_darya explaining pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "То есть ты решила пойти именно туда?"
    cs_ls "Почему бы и нет?"
    cs_da "Лен, пожалуйста, не пытайся специально её раздражать."
    cs_narrator "Я пожала плечами."
    cs_ls "Постараюсь."
    cs_da "Это не очень убедительный ответ."
    cs_ls "Другого пока не подготовила."
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.2)
    label cs_check_day01_part10_exterior:
    cs_narrator "Мы свернули к библиотеке."
    # cs_presence_keep: hide cs_darya
    cs_narrator "Здание, окна, дверь — всё знакомое. А вот разговор с человеком по ту сторону экрана предстоял впервые."
    cs_narrator "Я остановилась у входа."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты чего?"
    cs_ls "Думаю."
    cs_da "О чём?"
    cs_ls "О том, как не испортить первое впечатление."
    cs_da "Начни с обычного «здравствуйте»."
    cs_ls "Радикальное предложение."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_narrator "Я открыла дверь."
    play sound cs_day_sfx_door
    stop music fadeout 2.0
    return
