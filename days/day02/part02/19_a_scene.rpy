# -*- coding: utf-8 -*-
label cs_day02_19a:
    $ save_name = "Чужая смена — День 2: Внимательные слушатели"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_s19a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mi", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Думаю, ещё несколько минут у нас есть."
    cs_narrator "Она кивнула."
    cs_da "Я тоже хочу послушать."
    cs_narrator "Мику просияла."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_miku_19a:
    cs_mi "Правда? Тогда сейчас!"
    cs_narrator "Она поправила ноты."
    cs_narrator "Села ровнее."
    $ cs_director_scene("cs_cg_miku_piano_day")
    scene cs_cg_miku_piano_day
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
    $ cs_part02_cast = []
    $ cs_part02_cg = True
    with Dissolve(0.8)
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.58, channel="cs_piano", delay=0.3)
    play cs_piano cs_miku_piano_track noloop fadein 1.0
    label cs_check_d2_piano_miku:
    pause 1.5
    cs_narrator "И начала играть."
    cs_narrator "На этот раз мелодия была значительно увереннее."
    cs_narrator "Мику не приходилось искать клавиши."
    cs_narrator "Она двигалась быстрее, иногда едва заметно покачиваясь в такт."
    cs_narrator "В середине несколько раз повторилась одна и та же музыкальная фраза."
    cs_narrator "Затем она перешла к следующей части."
    stop cs_piano fadeout 0.8
    $ cs_director_scene("bg int_musclub_day")
    scene bg int_musclub_day
    $ cs_part02_cg = False
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "И неожиданно остановилась."
    cs_mi "Вот здесь!"
    cs_narrator "Она повернулась к нам."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Вам не кажется, что вступление слишком долгое? Я всё время думаю, что надо что-то убрать, но потом мне жалко, потому что каждая часть сама по себе нравится."
    cs_narrator "Я ненадолго задумалась."
    cs_ls "Мне кажется, мелодия хорошая. Но когда одна фраза повторяется несколько раз, начинаешь ждать, что дальше произойдёт что-нибудь новое."
    cs_narrator "Мику кивнула."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Да! Именно!"
    cs_narrator "Она посмотрела на Дарью."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "А тебе?"
    cs_da "Я бы попробовала сократить второе повторение. Тогда переход прозвучит неожиданнее."
    cs_narrator "Мику задумчиво посмотрела на ноты."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Может, и правда…"
    cs_narrator "Она взяла карандаш."
    cs_narrator "Сделала небольшую пометку."
    $ cs_director_scene("cs_cg_miku_piano_day")
    scene cs_cg_miku_piano_day
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
    $ cs_part02_cast = []
    $ cs_part02_cg = True
    with Dissolve(0.8)
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.58, channel="cs_piano", delay=0.3)
    play cs_piano "<from 12>sound/music/miku_song_voice.ogg" noloop fadein 1.0
    label cs_check_d2_piano_miku_again:
    pause 1.5
    cs_narrator "Потом сыграла фрагмент ещё раз."
    cs_narrator "Теперь с более коротким вступлением."
    cs_narrator "Я не особенно разбиралась в музыкальной композиции."
    cs_narrator "Но разница ощущалась."
    cs_narrator "Мелодия будто быстрее находила своё направление."
    stop cs_piano fadeout 0.8
    $ cs_director_scene("bg int_musclub_day")
    scene bg int_musclub_day
    $ cs_part02_cg = False
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_ls "Вот так мне нравится больше."
    cs_da "Мне тоже."
    cs_narrator "Мику улыбнулась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Спасибо! А то я уже третий раз сегодня переделываю и никак не могла решить."
    cs_narrator "Я рассмеялась."
    cs_ls "Иногда нужен кто-нибудь, кто просто послушает со стороны."
    cs_narrator "Она кивнула."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Да. Знаешь, самой всё время кажется, что раз я это придумала, значит, всё понятно. А потом кто-нибудь послушает и оказывается, что нет."
    cs_narrator "Я посмотрела на неё."
    cs_th "Знакомое чувство."
    cs_narrator "С рисунками у меня происходило почти то же самое."
    cs_narrator "Часами рассматриваешь собственную работу."
    cs_narrator "Уже перестаёшь видеть ошибки."
    cs_narrator "А потом кто-нибудь показывает на простую вещь, которую ты почему-то совершенно не замечала."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "С рисунками такая же история."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Правда? Ты рисуешь?"
    cs_ls "Да."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Ой, как здорово! Тогда, если захочешь, можешь как-нибудь прийти и порисовать здесь. У нас иногда ребята делают плакаты для выступлений."
    cs_narrator "Я улыбнулась."
    cs_ls "Интересное предложение."
    call cs_day02_21 from cs_return_6423aa415f7a21fea889
    return
