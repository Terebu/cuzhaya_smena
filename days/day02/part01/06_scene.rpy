# -*- coding: utf-8 -*-
label cs_day02_06:
    $ save_name = "Чужая смена — День 2: Человек, которого разбудили раньше времени"
    $ cs_director_scene("bg ext_house_of_mt_day")
    scene bg ext_house_of_mt_day
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_s06:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "На обратном пути я заметила, что лагерь уже почти проснулся."
    cs_narrator "Возле одного домика кто-то вытряхивал полотенце."
    cs_narrator "Вдалеке разговаривали пионеры."
    cs_narrator "На дорожке появилась девочка с ведром."
    cs_narrator "Я невольно улыбнулась."
    cs_th "Ну всё."
    cs_th "Режим невидимого исследователя завершён."
    cs_narrator "Я свернула к домику Ольги Дмитриевны."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "И почти сразу увидела Семёна."
    cs_narrator "Он стоял на крыльце."
    cs_narrator "Волосы растрёпаны."
    cs_narrator "Рубашка ещё не застёгнута до конца."
    cs_narrator "Лицо человека, который определённо не давал согласия на наступление утра."
    cs_narrator "Я замедлила шаг."
    cs_th "О."
    cs_th "Коллега по временному перемещению."
    cs_narrator "Подошла ближе."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Доброе утро, товарищ Семён."
    cs_narrator "Он поднял голову."
    cs_narrator "Посмотрел на меня."
    cs_narrator "Потом на мою спортивную одежду."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_new_d2_semen:
    cs_sy "Привет. Ты откуда?"
    cs_ls "С пробежки."
    cs_narrator "Он посмотрел на солнце."
    cs_narrator "Затем снова на меня."
    cs_sy "Сейчас?"
    cs_ls "Нет, вчера. Просто решила добежать только сегодня."
    cs_narrator "Семён недовольно усмехнулся."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Очень смешно."
    cs_narrator "Я улыбнулась."
    cs_ls "Спасибо. Старалась."
    cs_narrator "Он спустился с крыльца."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А если серьёзно, ты всегда так рано встаёшь?"
    cs_ls "Почти всегда. Привычка."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Завидую."
    cs_narrator "Я посмотрела на него."
    cs_ls "По твоему лицу не заметно."
    cs_sy "Просто я бы предпочёл ещё поспать."
    cs_narrator "Я понимающе кивнула."
    cs_ls "Сочувствую. Тяжёлая жизнь главного героя."
    cs_narrator "Семён нахмурился."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты опять за своё?"
    cs_narrator "Я замерла."
    cs_th "Точно."
    cs_th "Сколько можно?"
    cs_narrator "Вчера мы обсуждали, что он живой человек, а не персонаж, которому можно бесконечно напоминать о компьютерной игре."
    cs_narrator "Я немного смутилась."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Извини. Неудачная шутка."
    cs_narrator "Семён посмотрел на меня с лёгким удивлением."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Да ладно. Ничего страшного."
    cs_narrator "Я кивнула."
    cs_ls "Слушай, я кое-что заметила."
    cs_narrator "Его выражение лица изменилось."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что именно?"
    cs_narrator "Я понизила голос."
    cs_ls "Автобуса у ворот больше нет."
    cs_narrator "Он замолчал."
    cs_sy "Какого автобуса?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Четыреста десятого."
    cs_narrator "Он сразу стал серьёзнее."
    cs_sy "Ты ходила туда?"
    cs_ls "Во время пробежки. До ворот."
    cs_sy "И его там нет?"
    cs_ls "Нет. Хотя вчера, когда мы приехали, он стоял неподалёку."
    cs_narrator "Семён задумчиво посмотрел в сторону дороги."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я после своего приезда тоже не видел его снова."
    cs_ls "Значит, пока мы даже не знаем, когда именно он исчез."
    cs_sy "И куда."
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_narrator "Он помолчал."
    cs_narrator "Потом спросил:"
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты за ворота выходила?"
    cs_ls "Нет."
    cs_sy "Почему?"
    cs_narrator "Я пожала плечами."
    cs_ls "Мы с Дашей договорились не проверять дорогу поодиночке."
    cs_narrator "Семён медленно кивнул."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Разумно."
    cs_ls "Не скрывай удивления."
    cs_narrator "Он усмехнулся."
    cs_sy "Просто неожиданно услышать от тебя что-то настолько осторожное."
    cs_narrator "Я приложила ладонь к груди."
    cs_ls "Считаю это необоснованным обвинением."
    cs_narrator "Он улыбнулся."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом Семён посмотрел в сторону лагеря."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Может, после завтрака сходим втроём?"
    cs_narrator "Я задумалась."
    cs_ls "Давай сначала обсудим это с Дашей. И не обязательно идти за ворота прямо сегодня."
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Хорошо."
    cs_narrator "Я кивнула."
    cs_ls "Тогда до завтрака."
    # cs_presence_keep: hide cs_darya
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
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Увидимся."
    cs_narrator "Я развернулась к своему домику."
    cs_narrator "За спиной он добавил:"
    # cs_presence_keep: hide cs_darya
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Лена!"
    cs_narrator "Я обернулась."
    cs_ls "М?"
    cs_sy "Ты только не начинай всем подряд рассказывать про исчезнувший автобус."
    cs_narrator "Я несколько секунд смотрела на него."
    cs_narrator "Потом кивнула."
    cs_ls "Договорились. Пока только наша рабочая группа."
    cs_narrator "Он усмехнулся."
    # cs_presence_keep: hide cs_darya
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
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вот и отлично."
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
    with Dissolve(0.4)
    # cs_director_begin: Lena leaves Semen on the camp path
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_director_check_519facaa9c:
    # cs_director_end
    cs_narrator "Я продолжила путь."
    cs_th "Забавно."
    cs_th "Ещё вчера я считала его героем чужой истории."
    cs_th "А сегодня он уже помогает мне не принимать слишком поспешных решений."
    cs_narrator "Пожалуй, прогресс действительно наблюдался."
    return
