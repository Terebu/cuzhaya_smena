# -*- coding: utf-8 -*-
label cs_day02_42:
    $ save_name = "Чужая смена — День 2: По ту сторону ворот"
    $ cs_part05_live = False
    $ cs_part06_live = True
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    stop music fadeout 2.0
    $ cs_road_visual_trace = []
    $ cs_road_loop_observations = 0
    label cs_check_part06_s42:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После обеда мы ненадолго разошлись по делам."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
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
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/int_cabin_day.ogg":
        play ambience "sound/ambiences/int_cabin_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.12, channel="ambience", delay=1.0)
    cs_narrator "Я и Дарья зашли в наш домик за водой."
    cs_narrator "Семён отправился взять свою флягу и договорился встретить нас у ворот."
    cs_narrator "Я проверила карманы."
    cs_narrator "Сложенный листок с заметками."
    cs_narrator "Карандаш."
    cs_narrator "Резинка для волос."
    cs_narrator "И телефон."
    cs_narrator "Я вынула его, посмотрела на тёмный экран и положила обратно."
    cs_th "Зачем беру?"
    cs_th "Не знаю."
    cs_th "Наверное, привычка."
    cs_narrator "Шурик и Электроник по-прежнему не нашли способа безопасно зарядить его, но оставлять единственную вещь из моей привычной жизни почему-то не хотелось."
    cs_narrator "Дарья закрутила крышку бутылки."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Всё взяла?"
    cs_ls "Кажется, да."
    cs_narrator "Она посмотрела на меня."
    cs_da "Точно не собираешься сегодня устраивать одиночные эксперименты?"
    cs_narrator "Я повернулась."
    cs_ls "Даш, мы уже договорились."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я знаю. Просто уточняю."
    cs_narrator "Я немного помолчала."
    cs_narrator "Затем улыбнулась."
    cs_ls "Не переживай. Если пространство решит нас куда-нибудь отправить, будем возмущаться коллективно."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Очень утешительно."
    $ cs_director_scene("bg ext_camp_entrance_day")
    scene bg ext_camp_entrance_day
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_entrance_day.ogg":
        play ambience "sound/ambiences/camp_entrance_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    cs_narrator "Через несколько минут мы дошли до ворот."
    cs_narrator "Семён уже ждал нас."
    cs_narrator "Он стоял возле ограды и смотрел на дорогу."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ну что, готовы?"
    cs_narrator "Я кивнула."
    cs_ls "В теории."
    cs_sy "А на практике?"
    cs_narrator "Я посмотрела наружу."
    cs_narrator "Асфальт."
    cs_narrator "Деревья."
    cs_narrator "Пустая обочина."
    $ cs_director_scene("bg ext_no_bus")
    scene bg ext_no_bus
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
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part06_empty_bus_stop:
    cs_narrator "Никакого автобуса."
    cs_ls "Сейчас проверим."
    $ cs_director_scene("bg ext_no_bus")
    scene bg ext_no_bus
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
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы прошли под вывеской «Совёнок»."
    cs_narrator "Я остановилась почти сразу за воротами."
    cs_narrator "Посмотрела назад."
    cs_narrator "Они стояли на месте."
    cs_narrator "Ничего не произошло."
    cs_narrator "Никакой вспышки."
    cs_narrator "Никакого странного звука."
    cs_narrator "Лагерь никуда не исчез."
    cs_th "Ну что ж."
    cs_th "Первые несколько метров существования внешнего мира успешно подтверждены."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен?"
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_da "Ты опять что-то проверяешь?"
    cs_ls "Факт нашего физического существования за воротами."
    cs_narrator "Семён усмехнулся."
    cs_sy "И как результат?"
    cs_ls "Пока положительный."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья покачала головой."
    $ cs_director_scene("bg ext_road_day")
    scene bg ext_road_day
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
    show cs_semen thinking pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/forest_day.ogg":
        play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    cs_narrator "Мы продолжили путь."
    cs_narrator "Сначала всё выглядело абсолютно обычно."
    cs_narrator "Невысокая трава по обочинам."
    cs_narrator "Лес с обеих сторон."
    cs_narrator "Птицы."
    cs_narrator "Солнечные пятна на асфальте."
    cs_narrator "Я оглянулась ещё раз."
    cs_narrator "Ворота постепенно скрывались за деревьями."
    cs_th "Странно."
    cs_th "Всё настолько нормально, что даже обидно."
    cs_th "Я почти ожидала встретить табличку «За пределами сюжетной области проход запрещён»."
    cs_narrator "Но никакой таблички не было."
    cs_narrator "Лес у дороги не менялся: те же сосны, тот же асфальт, тот же ровный шум листвы."
    $ cs_director_scene("cs_road_powerlines_day")
    scene cs_road_powerlines_day
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
    show cs_semen thinking pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("approach")
    cs_narrator "Только дорога."
    cs_narrator "И трое людей, которые совершенно не представляли, куда она ведёт."
    return
