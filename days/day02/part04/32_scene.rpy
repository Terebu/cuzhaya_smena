# -*- coding: utf-8 -*-
label cs_day02_32:
    $ save_name = "Чужая смена — День 2: За дверью медпункта"
    $ cs_part03_live = False
    $ cs_part04_live = True
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    $ cs_part04_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/just_think.ogg":
        play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    label cs_check_part04_s32:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы вышли из медпункта."
    cs_narrator "Солнечный свет после прохладного помещения показался особенно ярким."
    cs_narrator "Я остановилась на крыльце."
    cs_narrator "Посмотрела на обработанный локоть."
    cs_narrator "Потом на дверь."
    cs_narrator "И наконец на Дарью."
    cs_ls "Интересное заведение."
    cs_narrator "Она усмехнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Медпункт?"
    cs_ls "Угу."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А мне понравилось. Виола вполне приятная."
    cs_narrator "Я кивнула."
    cs_ls "И наблюдательная."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part04_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы спустились с крыльца."
    cs_narrator "Несколько секунд шли молча."
    cs_narrator "Потом Дарья спросила:"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты действительно думаешь, что тот рисунок связан с историей из девяностых?"
    cs_narrator "Я задумалась."
    cs_ls "Не знаю."
    cs_da "Но узнала его?"
    cs_ls "Мне показалось, что узнала."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_da "А разве это не то же самое, что ты говорила о других людях в лагере?"
    cs_narrator "Я замедлила шаг."
    cs_ls "В каком смысле?"
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты видишь что-то похожее на то, что помнишь по игре. И сразу начинаешь думать, что знаешь, что это такое."
    cs_narrator "Я остановилась."
    cs_th "Вот ведь."
    cs_th "Опять она права."
    cs_narrator "Я посмотрела в сторону медпункта."
    cs_ls "Да. Похоже, я опять тороплюсь с выводами."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ничего страшного. Просто лучше сначала разобраться."
    cs_narrator "Я кивнула."
    cs_ls "Тогда запишем как наблюдение, а не как доказательство."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вот это уже разумнее."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Ты ведь понимаешь, что постепенно превращаешься в руководителя нашей исследовательской группы?"
    cs_narrator "Она тихо рассмеялась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А ты кем будешь?"
    cs_narrator "Я задумалась."
    cs_ls "Специалистом по обнаружению подозрительных плакатов."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Очень узкая специальность."
    cs_ls "Зато востребованная именно здесь."
    cs_narrator "Дарья покачала головой."
    cs_narrator "Но улыбаться не перестала."
    cs_narrator "Мы свернули на дорожку к клубам."
    return
