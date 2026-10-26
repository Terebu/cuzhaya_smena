# -*- coding: utf-8 -*-
label cs_day03_145:
    $ save_name = "Чужая смена — День 3: Если встреча не была назначена"
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    cs_narrator "Я немного посидела над блокнотом."
    cs_narrator "Сделала несколько набросков."
    cs_narrator "Проверила, насколько удобно работать здоровой рукой."
    cs_narrator "Всё оказалось вполне нормально."
    cs_narrator "Дарья тем временем собралась снова заглянуть к музыкальному клубу."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Ну что, идёшь покорять музыкальные вершины?"
    cs_narrator "Она усмехнулась."
    cs_da "Просто хочу ещё немного позаниматься."
    cs_narrator "Я кивнула."
    cs_ls "Тогда удачи."
    cs_narrator "Она улыбнулась."
    cs_da "А ты?"
    cs_narrator "Я посмотрела на блокнот."
    cs_ls "Думаю прогуляться и порисовать с натуры."
    cs_narrator "Дарья кивнула."
    cs_da "Увидимся позже."
    cs_narrator "Я вздохнула."
    cs_ls "Постараюсь не потеряться."
    cs_narrator "Она рассмеялась."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "Мы вышли из домика."
    cs_narrator "На дорожке ненадолго остановились."
    cs_da "Тогда встретимся перед ужином?"
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    $ cs_day03_darya_destination = "music_club"
    $ cs_actor_exit(["cs_darya"])
    with cs_sprite_leave
    cs_narrator "Она направилась к клубам."
    cs_narrator "Я пошла в сторону площади."
    cs_narrator "Что ж."
    cs_narrator "Сегодня у меня не было договорённости о совместном рисовании."
    cs_narrator "Но это совершенно не мешало немного поработать самой."
    cs_narrator "В конце концов, художнику иногда стоит рисовать просто для себя."
    cs_narrator "Я улыбнулась."
    cs_narrator "И продолжила путь."
    $ cs_day03_solo_sketch_done = True
    label cs_check_day03_145_solo:
    pass
    return
