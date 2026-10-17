# -*- coding: utf-8 -*-
label cs_day02_24b:
    $ save_name = "Чужая смена — День 2: У каждого свои дела"
    $ cs_part03_live = True
    $ cs_part02_live = False
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part03_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part03_s24b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на коробку."
    cs_narrator "Потом на Дарью."
    cs_ls "Мы тогда пока подготовим место для объявления, если ты не против."
    cs_narrator "Славя кивнула."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Конечно. Я сейчас быстро отнесу материалы и вернусь."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Точно справишься?"
    cs_sl "Да. Тут недалеко."
    cs_narrator "Я посмотрела на папку."
    cs_ls "Тогда можно взять несколько чистых листов и карандаши?"
    cs_narrator "Славя открыла её."
    cs_narrator "Отделила нужное."
    cs_sl "Вот. Только пока ничего не начинайте писать крупно — я ещё уточню, во сколько будет выступление."
    cs_ls "Хорошо. Сначала соберём исходные данные, затем перейдём к производству."
    cs_narrator "Славя улыбнулась."
    cs_sl "Именно."
    cs_narrator "Дарья взяла бумагу."
    cs_narrator "Я — карандаши."
    cs_narrator "Семён посмотрел на нас."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    $ cs_part03_cast = []
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    $ cs_part03_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Значит, идём искать стол?"
    cs_ls "Да. И желательно такой, который не развалится под тяжестью нашего творческого замысла."
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Мы попрощались со Славей."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    $ cs_part03_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она направилась к кладовой."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["sl"])
    with cs_sprite_leave
    label cs_director_check_026413f428:
    # cs_director_end
    cs_narrator "А мы пошли в сторону клубов, где, как я помнила, было достаточно места для работы."
    cs_th "Славя и сама прекрасно справится."
    cs_th "А у нас уже появилось первое официальное поручение."
    return
