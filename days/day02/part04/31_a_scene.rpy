# -*- coding: utf-8 -*-
label cs_day02_31a:
    $ save_name = "Чужая смена — День 2: Врачебная помощь наоборот"
    $ cs_part03_live = False
    $ cs_part04_live = True
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
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part04_s31a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я остановилась."
    cs_ls "Виола, помочь?"
    cs_narrator "Она подняла голову."
    cs_vi "С чем?"
    cs_narrator "Я указала на коробку."
    cs_ls "Убрать это в шкаф."
    cs_narrator "Виола посмотрела на упаковки."
    cs_vi "Если не трудно. Только ничего не вскрывай. Просто поставь закрытые пачки на верхнюю полку."
    cs_ls "Принято."
    $ cs_director_scene("cs_cg_lena_darya_help_viola_day")
    scene cs_cg_lena_darya_help_viola_day
    $ cs_part04_cg = True
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
    $ cs_part04_cast = []
    with Dissolve(0.8)
    label cs_check_cg_help_viola:
    cs_narrator "Я взяла коробку."
    cs_narrator "Она оказалась довольно лёгкой."
    cs_narrator "Дарья придержала дверцу шкафа."
    cs_narrator "Мы аккуратно поставили упаковки на место."
    cs_vi "Спасибо. А то с утра всё никак руки не доходили."
    cs_da "Не за что."
    cs_narrator "Я закрыла шкаф."
    cs_narrator "Посмотрела на Виолу."
    cs_ls "Медицинское обеспечение лагеря успешно реорганизовано."
    cs_narrator "Виола усмехнулась."
    cs_vi "Всего-то несколько пачек бинтов."
    cs_ls "Большие преобразования начинаются с малого."
    cs_narrator "Она рассмеялась."
    cs_vi "Ты всегда так разговариваешь?"
    cs_narrator "Я задумалась."
    cs_ls "К сожалению для окружающих, довольно часто."
    cs_da "Подтверждаю."
    cs_narrator "Я медленно повернулась к ней."
    cs_ls "У нас здесь какая-то организованная система свидетельских показаний?"
    cs_narrator "Дарья улыбнулась."
    cs_da "Просто сообщаю факты."
    cs_narrator "Виола покачала головой."
    cs_narrator "Но теперь смотрела на нас заметно теплее."
    cs_vi "Ну что ж. Заходите, если понадобится помощь. Только постарайтесь без новых царапин."
    cs_narrator "Я кивнула."
    cs_ls "Это уже сложнее, но попробуем."
    return
