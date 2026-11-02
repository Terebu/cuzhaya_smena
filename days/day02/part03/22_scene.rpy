# -*- coding: utf-8 -*-
label cs_day02_22:
    $ save_name = "Чужая смена — День 2: Утренние распоряжения"
    $ cs_part03_live = True
    $ cs_part02_live = False
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_part03_cg = False
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
    $ cs_part03_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part03_s22:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда мы пришли на площадь, пионеры уже собирались перед памятником. Некоторые стояли небольшими группами. Кто-то пытался успеть закончить разговор. Ульяна что-то оживлённо объясняла Алисе, размахивая руками."
    cs_narrator "Алиса слушала с видом человека, который уже пожалел, что не ушёл раньше. Я улыбнулась."
    cs_th "Всё-таки утро здесь начинается предсказуемо. Половина лагеря пытается заняться своими делами. Вторая половина мешает первой."
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
    show cs_semen wave pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Семён заметил нас и махнул рукой."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вы куда пропали?"
    cs_ls "Участвовали в развитии международных культурных связей."
    cs_narrator "Он посмотрел на меня, потом на Дарью."
    cs_sy "Можно обычными словами?"
    cs_da "Были в музыкальном кружке. Познакомились с Мику."
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
    show cs_semen smile pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А, понятно."
    cs_ls "Второй вариант формулировки действительно значительно короче."
    cs_narrator "Семён усмехнулся."
    cs_sy "И понятнее."
    $ cs_director_scene("cs_cg_morning_lineup_day")
    scene cs_cg_morning_lineup_day
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
    $ cs_part03_cast = []
    $ cs_part03_cg = True
    with Dissolve(0.8)
    label cs_check_cg_lineup:
    cs_narrator "В этот момент Ольга Дмитриевна попросила всех перестать разговаривать. Мы повернулись к ней."
    cs_mt "Так, ребята. Сегодня у нас достаточно дел, поэтому прошу внимательно послушать."
    cs_narrator "Я выпрямилась."
    cs_th "Начинается. Утреннее совещание руководящего состава."
    cs_narrator "Ольга Дмитриевна напомнила о порядке возле домиков, дежурствах и работе кружков. Потом перешла к вечерней программе."
    cs_mt "После ужина у нас будет небольшой музыкальный вечер на площади. Поэтому нужно подготовить место и объявление, чтобы все знали, когда приходить."
    cs_narrator "Я посмотрела на Дарью. Она уже смотрела на меня."
    cs_th "Кажется, нас сейчас назначат ответственными."
    cs_mt "Кто у нас умеет рисовать?"
    cs_narrator "Я помолчала. А затем подняла руку."
    cs_ls "Могу попробовать."
    cs_narrator "Ольга Дмитриевна улыбнулась."
    cs_mt "Отлично. Как раз пригодится. Сделаете объявление, а Славя поможет с материалами."
    cs_ls "Хорошо."
    cs_mt "Только, Лена, не увлекайся. Главное — чтобы все могли прочитать время и место."
    cs_ls "Постараюсь не превращать объявление в дипломную работу."
    cs_narrator "Она приподняла бровь."
    cs_mt "Вот и прекрасно."
    cs_narrator "Рядом Дарья тихо усмехнулась. Я повернулась к ней."
    cs_ls "Ничего не говори."
    cs_da "Я даже не собиралась."
    cs_narrator "Но выражение её лица говорило обратное."
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_part03_cg = False
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
    $ cs_part03_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Через несколько минут линейка закончилась. Пионеры начали расходиться. Кто-то направился к кружкам. Кто-то — к домикам."
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Семён подошёл к нам."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Значит, теперь ты у нас художник-оформитель?"
    cs_ls "А ты, видимо, назначаешься ответственным за моральную поддержку."
    cs_sy "А можно отказаться?"
    cs_ls "Заявление принимается в письменном виде."
    cs_narrator "Дарья рассмеялась."
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
    show cs_semen smile pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Понятно."
    cs_narrator "Я улыбнулась. Но прежде чем успела придумать ему ещё какую-нибудь должность, Дарья указала на дорожку."
    cs_da "Смотрите, Славя."
    cs_narrator "Я повернулась."
    return
