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
    cs_narrator "Первое время мы шли молча. Дорога постепенно уходила дальше между деревьями. Никаких машин. Никаких указателей."
    cs_narrator "Ни одного встречного человека. Минут через десять я остановилась."
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
    cs_ls "Да. Если эта дорога окажется обычной, ничего не потеряем. А если нет, будет с чем сравнивать."
    cs_narrator "Я подошла к кусту у обочины. Достала из кармана резинку для волос. Яркую, хорошо заметную на фоне зелёных листьев."
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
    cs_narrator "Дарья осмотрелась. Затем взяла небольшую палочку и начертила в пыли у края дороги стрелку."
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда добавим направление, в котором идём."
    cs_narrator "Я посмотрела на стрелку."
    cs_ls "Хорошая мысль."
    cs_narrator "Семён присел рядом. Проверил, куда она направлена. Затем выпрямился."
    cs_sy "Запомнил. Куст с резинкой справа, стрелка в сторону от лагеря."
    cs_narrator "Я достала листок. Записала несколько слов."
    cs_th "Контрольная точка. Куст справа. Стрелка по направлению движения."
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
    cs_narrator "Мы отправились дальше. Сначала ничего необычного не происходило. Дорога по-прежнему шла между деревьями."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_left_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap1_b")
    label cs_check_part06_lap1_b:
    cs_narrator "Иногда слегка изгибалась, но крупных поворотов не было. Мы видели одни и те же породы деревьев. Одну и ту же траву. Похожие кусты."
    cs_narrator "Я начала замечать, что все попытки найти хотя бы один действительно выразительный ориентир заканчиваются одинаково."
    cs_th "Сосна, ещё сосна, куст, камень. Пейзажный художник явно сэкономил на разнообразии."
    cs_narrator "Я посмотрела на Дарью. Она шла чуть впереди, внимательно осматривая дорогу. Семён время от времени поглядывал на часы."
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
    cs_ls "Тогда ещё немного — и поворачиваем назад."
    cs_da "Подожди."
    cs_narrator "Она остановилась. Я тоже. Семён поднял голову."
    show cs_semen thinking pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что?"
    cs_narrator "Дарья смотрела вперёд. На правую обочину. На куст, который выделялся среди остальных маленьким ярким пятном. Я проследила за её взглядом."
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
    cs_narrator "На ветке висела моя резинка. Та самая. Я узнала цвет. И узел."
    cs_narrator "А на пыльной земле у края асфальта осталась стрелка. Она по-прежнему указывала вперёд. В том же направлении, в котором мы шли. Я медленно выдохнула."
    cs_ls "Так."
    cs_narrator "Семён посмотрел на куст, потом на дорогу за нашими спинами."
    cs_sy "Подожди. Мы же здесь уже были."
    cs_da "Были."
    cs_narrator "Я присела возле стрелки. Провела пальцем по её краю. Пыль немного осыпалась."
    cs_ls "Это наша отметка."
    cs_narrator "Семён нахмурился."
    cs_sy "Может, мы где-то свернули и не заметили?"
    cs_da "Мы всё время оставались на дороге."
    cs_sy "Я знаю. Просто…"
    cs_narrator "Он замолчал. Я поднялась. Посмотрела назад. Потом вперёд."
    cs_narrator "Лес выглядел обычным. Никакого перехода. Никакой очевидной границы. Мы просто шли вперёд."
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
    cs_th "Именно. Потому что сейчас мне очень хотелось немедленно объявить об открытии новой геометрии. А это, возможно, худший момент для поспешных выводов."
    return
