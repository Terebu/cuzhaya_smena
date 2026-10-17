# -*- coding: utf-8 -*-
label cs_day02_35:
    $ save_name = "Чужая смена — День 2: Распределение обязанностей"
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
    label cs_check_part05_s35:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Дарья посмотрела на верхнюю часть листа."
    cs_da "Нам ещё нужен заголовок."
    cs_narrator "Я кивнула."
    cs_ls "«Музыкальный вечер»."
    cs_sy "Хорошо. Крупно напишем."
    cs_narrator "Он взял карандаш."
    cs_narrator "Потом посмотрел на меня."
    cs_sy "Только предупреждаю: красивого почерка не обещаю."
    cs_narrator "Я улыбнулась."
    cs_ls "Не переживай. Комиссия пока не утверждала стандарт каллиграфии."
    cs_sy "Звучит обнадёживающе."
    cs_narrator "Дарья пододвинула нам линейку."
    cs_da "Вот. Хотя бы буквы ровно расположите."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Потом на свободное место для надписи."
    cs_narrator "Мы вполне могли сделать её вместе."
    cs_narrator "Или я могла оставить заголовок ему, пока сама закончила бы рисунок."
    cs_narrator "Оба решения выглядели разумными."
    cs_narrator "Вопрос был скорее в том, как распределить работу."
    cs_th "Ну что, Соколова."
    cs_th "Потренируешься работать в команде?"
    return
