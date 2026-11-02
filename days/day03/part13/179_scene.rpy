# -*- coding: utf-8 -*-
label cs_day03_179:
    $ save_name = "Чужая смена — День 3: День, который оказался не чужим"
    $ cs_director_scene("cs_house_lena_darya_ext_night")
    scene cs_house_lena_darya_ext_night
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "Мы свернули на знакомую дорожку. Наш домик уже виднелся между деревьями. Ветки отбрасывали на стену подвижные тени. На крыльце лежала узкая полоска света от ближайшего фонаря."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Вот и пришли. Третий день почти закончился. И, кажется, я впервые не чувствую необходимости срочно разложить всё произошедшее по полочкам."
    cs_narrator "Я посмотрела на Дашу. Она шла рядом. Спокойная. Немного уставшая."
    cs_narrator "Но улыбалась."
    if cs_da_day3_music_talk or cs_mz_evening_help_completed_day3 == False:
        cs_th "Сегодня она снова играла на пианино."
    else:
        cs_th "Сегодня она снова нашла время для музыки."
    if cs_un_sketch_completed_day3:
        cs_th "Я рисовала."
    else:
        cs_th "Я успела выбрать место для рисунков."
    if cs_mi_followup_invitation_day3:
        cs_th "Мику ждёт нас завтра в музыкальном клубе — мы обещали зайти."
    if cs_dv_followup_invitation_day3:
        cs_th "И Алисе я обещала послушать её новый переход."
    cs_th "А Женя теперь знает, что я способна не только болтать, но и действительно читать."
    cs_narrator "Я усмехнулась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Мы остановились возле крыльца. Даша отпустила мою руку, чтобы подняться по ступенькам. Потом обернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "М?"
    cs_narrator "Она немного улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты сегодня довольна?"
    cs_narrator "Я посмотрела на неё. Задумалась. А потом кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она улыбнулась шире."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Хорошо."
    cs_narrator "Я поднялась следом. Осторожно поправила повязку."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Только у меня есть одна серьёзная проблема."
    cs_narrator "Даша остановилась. Посмотрела на меня с лёгким подозрением."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Какая?"
    cs_narrator "Я вздохнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Теперь придётся искать следующую книгу."
    cs_narrator "Она закрыла глаза. Потом рассмеялась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Лена!"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Что? Нельзя же оставить культурное развитие населения на половине пути."
    cs_narrator "Даша покачала головой."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Тогда завтра опять к Жене?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Возможно."
    cs_narrator "Посмотрела на неё."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Но сначала обещаю позавтракать."
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Уже неплохо."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Видишь? Постепенно становлюсь ответственным членом общества."
    cs_narrator "Даша тихо рассмеялась. Потом придержала дверь, пропуская меня. Из домика пахнуло привычным тёплым воздухом. Я остановилась на пороге."
    cs_narrator "Оглянулась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Ночной лагерь оставался позади. Тихий. Спокойный. Почти обыкновенный."
    cs_th "И всё-таки совершенно невозможный."
    cs_narrator "Я помолчала."
    cs_th "Когда-нибудь мы узнаем, что здесь происходит. Обязательно. Но сегодня…"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_narrator "Я посмотрела на Дашу, которая ждала меня у двери."
    cs_th "Сегодня достаточно просто быть здесь."
    cs_narrator "Я улыбнулась."
    $ cs_director_scene("cs_house_lena_darya_int_night")
    scene cs_house_lena_darya_int_night
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    play sound "sound/sfx/close_door_1.ogg"
    stop music fadeout 3.0
    $ cs_day03_darya_destination = "house"
    cs_narrator "И вошла в домик."
    return
