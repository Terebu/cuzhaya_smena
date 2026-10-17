# -*- coding: utf-8 -*-
label cs_day02_43:
    $ save_name = "Чужая смена — День 2: Контрольная точка"
    $ cs_part05_live = False
    $ cs_part06_live = True
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
    show cs_semen neutral pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/forest_day.ogg":
        play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/into_the_unknown.ogg":
        play music "sound/music/into_the_unknown.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.11, channel="music", delay=1.0)
    label cs_check_part06_s43:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Первое время мы шли молча."
    cs_narrator "Дорога постепенно уходила дальше между деревьями."
    cs_narrator "Никаких машин."
    cs_narrator "Никаких указателей."
    cs_narrator "Ни одного встречного человека."
    cs_narrator "Минут через десять я остановилась."
    cs_ls "Подождите."
    cs_narrator "Семён обернулся."
    show cs_semen thinking pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что случилось?"
    cs_narrator "Я посмотрела на обочину."
    cs_ls "Хочу кое-что отметить."
    show cs_darya thinking pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ориентир?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Если эта дорога окажется обычной, ничего не потеряем. А если нет, будет с чем сравнивать."
    cs_narrator "Я подошла к кусту у обочины."
    cs_narrator "Достала из кармана резинку для волос."
    cs_narrator "Яркую, хорошо заметную на фоне зелёных листьев."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_marked_verge_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("control_created")
    label cs_check_part06_control_created:
    cs_narrator "Аккуратно закрепила её на тонкой ветке."
    cs_sy "И что это докажет?"
    cs_ls "Пока ничего. Но если мы почему-нибудь снова увидим этот куст, сможем хотя бы его узнать."
    cs_narrator "Дарья осмотрелась."
    cs_narrator "Затем взяла небольшую палочку и начертила в пыли у края дороги стрелку."
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда добавим направление, в котором идём."
    cs_narrator "Я посмотрела на стрелку."
    cs_ls "Хорошая мысль."
    cs_narrator "Семён присел рядом."
    cs_narrator "Проверил, куда она направлена."
    cs_narrator "Затем выпрямился."
    cs_sy "Запомнил. Куст с резинкой справа, стрелка в сторону от лагеря."
    cs_narrator "Я достала листок."
    cs_narrator "Записала несколько слов."
    cs_th "Контрольная точка."
    cs_th "Куст справа."
    cs_th "Стрелка по направлению движения."
    cs_narrator "Потом посмотрела на них обоих."
    cs_ls "Ну что, продолжаем?"
    cs_da "Подожди."
    cs_narrator "Она указала на часы Семёна."
    cs_da "Засеки время, чтобы потом не спорить, сколько прошли."
    cs_narrator "Он кивнул."
    show cs_semen smile pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Хорошо. Начали."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_powerlines_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap1_a")
    label cs_check_part06_lap1_a:
    cs_narrator "Мы отправились дальше."
    cs_narrator "Сначала ничего необычного не происходило."
    cs_narrator "Дорога по-прежнему шла между деревьями."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_left_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap1_b")
    label cs_check_part06_lap1_b:
    cs_narrator "Иногда слегка изгибалась, но крупных поворотов не было."
    cs_narrator "Мы видели одни и те же породы деревьев."
    cs_narrator "Одну и ту же траву."
    cs_narrator "Похожие кусты."
    cs_narrator "Я начала замечать, что все попытки найти хотя бы один действительно выразительный ориентир заканчиваются одинаково."
    cs_th "Сосна."
    cs_th "Ещё сосна."
    cs_th "Куст."
    cs_th "Камень."
    cs_th "Прекрасно."
    cs_th "Пейзажный художник решил сэкономить на разнообразии."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она шла чуть впереди, внимательно осматривая дорогу."
    cs_narrator "Семён время от времени поглядывал на часы."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_right_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap1_c")
    label cs_check_part06_lap1_c:
    cs_narrator "Через несколько минут он произнёс:"
    cs_sy "Уже почти пятнадцать минут."
    cs_narrator "Я кивнула."
    cs_ls "Тогда ещё немного — и поворачиваем назад."
    cs_da "Подожди."
    cs_narrator "Она остановилась."
    cs_narrator "Я тоже."
    cs_narrator "Семён поднял голову."
    show cs_semen thinking pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что?"
    cs_narrator "Дарья смотрела вперёд."
    cs_narrator "На правую обочину."
    cs_narrator "На куст, который выделялся среди остальных маленьким ярким пятном."
    cs_narrator "Я проследила за её взглядом."
    cs_narrator "И почувствовала, как неприятно сжался живот."
    cs_th "Нет."
    cs_th "Только не говори…"
    cs_narrator "Я подошла ближе."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_marked_verge_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap1_return")
    label cs_check_part06_lap1_return:
    $ cs_road_loop_observations = 1
    $ renpy.music.set_volume(0.18, channel="music", delay=1.5)
    cs_narrator "На ветке висела моя резинка."
    cs_narrator "Та самая."
    cs_narrator "Я узнала цвет."
    cs_narrator "И узел."
    cs_narrator "А на пыльной земле у края асфальта осталась стрелка."
    cs_narrator "Она по-прежнему указывала вперёд."
    cs_narrator "В том же направлении, в котором мы шли."
    cs_narrator "Я медленно выдохнула."
    cs_ls "Так."
    cs_narrator "Семён посмотрел на куст."
    cs_narrator "Потом на дорогу за нашими спинами."
    cs_sy "Подожди. Мы же здесь уже были."
    cs_da "Были."
    cs_narrator "Я присела возле стрелки."
    cs_narrator "Провела пальцем по её краю."
    cs_narrator "Пыль немного осыпалась."
    cs_ls "Это наша отметка."
    cs_narrator "Семён нахмурился."
    cs_sy "Может, мы где-то свернули и не заметили?"
    cs_da "Мы всё время оставались на дороге."
    cs_sy "Я знаю. Просто…"
    cs_narrator "Он замолчал."
    cs_narrator "Я поднялась."
    cs_narrator "Посмотрела назад."
    cs_narrator "Потом вперёд."
    cs_narrator "Лес выглядел совершенно обычным."
    cs_narrator "Никакого перехода."
    cs_narrator "Никакой очевидной границы."
    cs_narrator "Мы просто шли вперёд."
    cs_narrator "И оказались там, где уже были."
    cs_ls "Либо мы каким-то образом прошли круг, либо наши наблюдения гораздо менее надёжны, чем хотелось бы."
    show cs_darya explaining pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А ещё надо исключить, что здесь есть второй похожий куст."
    cs_narrator "Я посмотрела на резинку."
    cs_ls "С моей резинкой?"
    cs_narrator "Она покачала головой."
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нет. Ты права. Но лучше всё равно перепроверить."
    cs_narrator "Я кивнула."
    cs_th "Именно."
    cs_th "Потому что сейчас мне очень хотелось немедленно объявить об открытии новой геометрии."
    cs_th "А это, возможно, худший момент для поспешных выводов."
    return
