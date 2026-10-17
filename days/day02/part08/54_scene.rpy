# -*- coding: utf-8 -*-
label cs_day02_54:
    $ save_name = "Чужая смена — День 2: Знакомая площадь"
    $ cs_part07_live = False
    $ cs_part08_live = True
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
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    $ renpy.music.set_volume(0.14, channel="ambience", delay=1.0)
    label cs_check_part08_s54:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "На площадь мы вышли медленно."
    cs_narrator "Не потому, что мне хотелось любоваться местными архитектурными достижениями."
    cs_narrator "И даже не потому, что я решила внезапно пересмотреть своё отношение к размеренным прогулкам."
    cs_narrator "Просто после второго за день посещения медпункта Дарья совершенно справедливо отказалась поддерживать любые мои попытки двигаться быстрее обычного человека."
    cs_narrator "Особенно когда я начинала отвлекаться на разговор."
    cs_ls "Даш, я вообще-то могу ходить самостоятельно."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом на повязку."
    cs_da "Никто и не спорит. Просто не нужно снова бежать."
    cs_ls "Это был один несчастный корень."
    cs_da "На дорожке, по которой ты уже проходила."
    cs_narrator "Я задумалась."
    cs_th "Вот ведь."
    cs_th "Формально всё правильно."
    cs_th "Но насколько неприятно слышать собственную статистику происшествий."
    cs_ls "Считаю необходимым уточнить: причиной падения стала недостаточная видимость препятствия."
    cs_da "А причиной недостаточной видимости — то, что ты смотрела на меня, а не под ноги."
    cs_narrator "Я медленно повернула голову."
    cs_narrator "Она улыбалась."
    cs_narrator "Совершенно невинно."
    cs_ls "Ты сейчас используешь против меня мои же объяснения?"
    cs_da "Учусь у лучших."
    cs_narrator "Я покачала головой."
    cs_ls "Страшно представить, что будет к концу недели."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Для начала попробуй дожить до ужина без третьей повязки."
    cs_narrator "Я не выдержала и рассмеялась."
    cs_th "Всё."
    cs_th "Официально потеряла монополию на сарказм."
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
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
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part08_square:
    cs_narrator "Мы прошли мимо доски объявлений."
    cs_narrator "Наше творение по-прежнему висело на своём месте."
    cs_narrator "Большая надпись «МУЗЫКАЛЬНЫЙ ВЕЧЕР»."
    cs_narrator "Гитара."
    cs_narrator "Ноты."
    cs_narrator "Небольшая звёздочка в углу."
    cs_narrator "Я остановилась на несколько секунд."
    cs_th "А ведь неплохо получилось."
    cs_narrator "Конечно, дома я бы сделала всё совершенно иначе."
    cs_narrator "Нормальные шрифты."
    cs_narrator "Несколько слоёв."
    cs_narrator "Подобрала бы цветовую палитру."
    cs_narrator "Возможно, ещё минут сорок двигала бы заголовок на два пикселя вправо, а потом обратно."
    cs_narrator "Но здесь такой возможности не было."
    cs_narrator "И почему-то это совершенно не мешало мне получать удовольствие от результата."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Всё ещё рассматриваешь?"
    cs_ls "Оцениваю качество исполнения государственного заказа."
    cs_narrator "Она усмехнулась."
    cs_da "И как оценка?"
    cs_ls "Работа принята. Премия не выплачена."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Какая трагедия."
    cs_narrator "Я улыбнулась."
    cs_narrator "Мы двинулись дальше."
    cs_narrator "Возле памятника несколько пионеров обсуждали предстоящее выступление."
    cs_narrator "Ульяна куда-то бежала с таким видом, будто опаздывала одновременно на три разных мероприятия."
    cs_narrator "Неподалёку стояла Алиса, разговаривая с девочкой из младшего отряда."
    cs_narrator "А возле одной из лавочек…"
    cs_narrator "Я замедлила шаг."
    cs_th "О."
    cs_th "Знакомое лицо."
    cs_narrator "Семён."
    cs_narrator "Он сидел спиной к нам и что-то задумчиво вертел в руках."
    cs_narrator "Кажется, обычный карандаш."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Затем на Дарью."
    cs_narrator "Она проследила за моим взглядом."
    cs_narrator "И сразу вздохнула."
    cs_da "Лена."
    cs_ls "Что?"
    cs_da "Я знаю это выражение лица."
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Неужели?"
    cs_da "Ты сейчас собираешься сделать что-нибудь совершенно необязательное."
    cs_narrator "Я задумалась."
    cs_narrator "Потом улыбнулась."
    cs_ls "Но потенциально очень весёлое."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Для кого?"
    cs_ls "Это мы сейчас и выясним."
    cs_narrator "Она покачала головой."
    cs_narrator "Но уже улыбалась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только осторожнее с рукой."
    cs_narrator "Я кивнула."
    cs_ls "Никаких экстремальных видов спорта."
    cs_narrator "И направилась к лавочке."
    cs_th "В конце концов, не каждый день выпадает возможность провести небольшой психологический эксперимент над собственным другом."
    cs_th "Хотя…"
    cs_th "Второй день подряд."
    cs_th "Определённая систематичность уже наблюдается."
    return
