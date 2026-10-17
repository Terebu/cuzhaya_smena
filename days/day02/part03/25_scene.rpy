# -*- coding: utf-8 -*-
label cs_day02_25:
    $ save_name = "Чужая смена — День 2: Художественный отдел приступает к работе"
    $ cs_part03_live = True
    $ cs_part02_live = False
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part03_cg = False
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
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part03_s25:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы направились к клубам."
    cs_narrator "Дарья несла бумагу."
    cs_narrator "Я — карандаши."
    cs_narrator "Семён шёл рядом и время от времени поглядывал на мои руки."
    cs_sy "Только не потеряй."
    cs_narrator "Я посмотрела на него."
    cs_ls "Что именно?"
    cs_sy "Карандаши."
    cs_ls "Спасибо за напоминание. Без тебя художественный отдел понёс бы невосполнимые потери."
    cs_narrator "Он усмехнулся."
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
    cs_sy "Всегда пожалуйста."
    cs_narrator "Дарья посмотрела на нас обоих."
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вы понимаете, что объявление ещё даже не начали, а уже спорите?"
    cs_narrator "Я задумалась."
    cs_ls "Творческая дискуссия."
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Необходимый этап."
    cs_narrator "Дарья закатила глаза."
    cs_narrator "Но улыбнулась."
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    $ cs_part03_cg = False
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Возле клубов мы нашли стол под навесом."
    cs_narrator "Я положила карандаши рядом."
    $ cs_director_scene("cs_cg_poster_planning_day")
    scene cs_cg_poster_planning_day
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
    label cs_check_cg_poster_planning:
    cs_narrator "Дарья разложила бумагу, прижав края ладонями."
    cs_narrator "Несколько секунд мы просто смотрели на чистый лист."
    cs_th "Вот."
    cs_th "Знакомое чувство."
    cs_narrator "В Москве оно обычно возникало перед экраном графического планшета."
    cs_narrator "Чистый холст."
    cs_narrator "Никаких ограничений."
    cs_narrator "Кроме того, что начинать почему-то всегда сложнее, чем продолжать."
    cs_narrator "Сейчас планшета не было."
    cs_narrator "Был обычный лист бумаги."
    cs_narrator "Несколько карандашей."
    cs_narrator "И Семён, который, кажется, искренне верил, что мы сейчас нарисуем шедевр лагерной полиграфии."
    cs_sy "Ну что, с чего начнём?"
    cs_narrator "Я задумчиво посмотрела на лист."
    cs_ls "Предлагаю сначала определить содержание."
    cs_da "Музыкальный вечер. Площадь. После ужина."
    cs_sy "Время ещё уточняется."
    cs_narrator "Я кивнула."
    cs_ls "Значит, пока можно сделать композицию."
    cs_narrator "Семён приподнял бровь."
    cs_sy "Композицию?"
    cs_ls "Расположение текста и рисунка."
    cs_sy "А."
    cs_narrator "Дарья указала на верхнюю часть листа."
    cs_da "Название лучше сделать крупнее. Чтобы издалека читалось."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Согласна."
    cs_da "А рисунок можно разместить по краям."
    cs_ls "Ты сегодня удивительно успешно выполняешь обязанности художественного редактора."
    cs_narrator "Она улыбнулась."
    cs_da "Я просто хочу, чтобы люди могли прочитать объявление."
    cs_ls "Разумное требование."
    cs_narrator "Я взяла карандаш."
    cs_narrator "Наметила несколько лёгких линий."
    cs_narrator "Затем остановилась."
    cs_narrator "Посмотрела на Семёна."
    cs_ls "Кстати, нам ведь ещё нужно к Шурику и Электронику."
    cs_narrator "Он кивнул."
    cs_sy "Помню."
    cs_da "Может, сначала зайдём к ним? Пока не начали рисовать всерьёз."
    cs_narrator "Я посмотрела на чистый лист."
    cs_narrator "Потом в сторону двери клубов."
    cs_th "И правда."
    cs_th "Художественный проект подождёт несколько минут."
    cs_th "А вот телефон…"
    cs_narrator "Я машинально коснулась кармана."
    cs_narrator "Он по-прежнему был там."
    cs_narrator "Выключенный."
    cs_narrator "Но целый."
    cs_ls "Хорошо. Давайте сначала посмотрим, что получилось у ребят."
    cs_narrator "Я аккуратно положила карандаш на стол."
    cs_narrator "Дарья собрала листы в папку, чтобы их не унесло ветром."
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    $ cs_part03_cg = False
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Семён подошёл к двери."
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
    cs_sy "Идём?"
    cs_narrator "Я кивнула."
    cs_ls "Идём."
    cs_narrator "Мы направились внутрь."
    cs_th "Вот и весь план."
    cs_th "Проверить телефон."
    cs_th "Сделать объявление."
    cs_th "Попробовать не устроить дополнительных происшествий."
    cs_th "Последний пункт, пожалуй, самый сложный."
    $ cs_director_scene("bg int_clubs_male_day")
    scene bg int_clubs_male_day
    $ cs_part03_cg = False
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
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/smooth_machine.ogg":
        play music "sound/music/smooth_machine.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part03_clubs:
    pause 0.5
    $ cs_part03_live = False
    return
