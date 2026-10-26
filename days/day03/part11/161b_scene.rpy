# -*- coding: utf-8 -*-
label cs_day03_161b:
    $ save_name = "Чужая смена — День 3: Вечер без дополнительных поручений"
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5
    cs_narrator "Мы вышли из столовой."
    cs_narrator "Солнце постепенно опускалось за деревья."
    cs_narrator "Воздух стал прохладнее."
    cs_narrator "Я глубоко вдохнула."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Ну что ж."
    cs_th "Ужин завершён."
    cs_th "Литературная дипломатия прошла успешно."
    cs_th "Никаких чрезвычайных происшествий."
    cs_th "Пожалуй, редкий случай."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Ты довольна?"
    cs_narrator "Я улыбнулась."
    cs_ls "Очень."
    cs_narrator "Она немного прищурилась."
    cs_da "Даже без очередной шутки про Семёна?"
    cs_narrator "Я задумалась."
    cs_ls "Даша, сегодня я уже достаточно поработала над его душевным равновесием."
    cs_narrator "Она рассмеялась."
    cs_da "Значит, вечер будет спокойным?"
    cs_narrator "Я посмотрела на дорожку."
    cs_narrator "Потом на неё."
    cs_ls "Планирую именно так."
    cs_narrator "Она улыбнулась."
    cs_da "Хороший план."
    cs_narrator "Я кивнула."
    cs_ls "Главное, чтобы лагерь его согласовал."
    cs_narrator "Дарья тихо рассмеялась."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "Мы направились к площади."
    return
