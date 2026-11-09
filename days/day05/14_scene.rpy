# -*- coding: utf-8 -*-
label cs_day05_14:
    $ cs_d5_scene = 14
    $ save_name = "Чужая смена — День 5: Семь стуков"
    $ cs_bus_scene_enter(14)
    $ cs_d5_room("bg int_library_day")
    with Dissolve(0.7)
    stop music fadeout 1.0
    cs_narrator "Когда мы вернулись в библиотеку, на столе уже лежала знакомая папка."
    cs_narrator "Ольга Дмитриевна стояла возле окна."
    cs_narrator "Женя раскладывала записи по порядку."
    cs_narrator "Тихонова сидела немного в стороне и рассматривала одну из фотографий."
    $ cs_d5_documents_location = "library"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Все пришли?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: f0d69dbc53bcf5e07f31
    cs_sy "Да."
    cs_sy "Мы ещё у Мику были."
    if not cs_d5_miku_volunteer:
        cs_narrator "Он положил на стол листок, который передала Мику."
    else:
        $ cs_d5_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: bade06a6df081523360e
        cs_sy "Мику свой сон хотела рассказать вам сама."
        cs_sy "Вечером."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 0546e7dbcbabda45fc94
    cs_mt "Хорошо."
    cs_mt "Я сейчас схожу за Виолой."
    cs_mt "Она тоже должна это услышать."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 85ae2d4dae30133110cd
    cs_ls "Давайте."
    cs_ls "Мы пока разберём бумаги."
    cs_narrator "Вожатая кивнула."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Только ничего никуда не уносите."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Я прослежу."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У меня даже желания нет."
    cs_narrator "Ольга Дмитриевна посмотрела на меня с явным недоверием, но спорить не стала."
    $ cs_actor_exit(["mt"])
    $ cs_d5_cast = []
    cs_narrator "Когда она ушла, мы заняли места за столом."
    cs_narrator "Фотографии из старого корпуса лежали перед нами."
    cs_narrator "Я взяла один снимок."
    cs_narrator "Посмотрела на лица."
    cs_narrator "Потом перевернула его."
    cs_narrator "Старая бумага была шероховатой."
    cs_narrator "На обороте оставались выцветшие надписи."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Можно посмотреть?"
    cs_narrator "Я протянула ей фотографию."
    cs_narrator "Она держала её очень осторожно, за самый край."
    $ cs_d5_focus("un")
    with cs_sprite_change
    # cs_page_anchor: 05100170f20791d4c2fd
    cs_un "Девушка здесь…"
    cs_un "Правда похожа на меня."
    cs_narrator "Женя подняла глаза."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 431a336eb6b71e6a7a1c
    cs_mz "Похожа."
    cs_mz "Но качество фотографии плохое."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "И мы не знаем, кто именно на ней изображён."
    cs_narrator "Тихонова кивнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вот и не будем пока никого назначать персонажем старой фотографии."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Я улыбнулась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У меня сегодня курс по воздержанию от поспешных выводов."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Тебе ещё учиться и учиться."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Зато преподаватель хороший."
    cs_narrator "Женя едва заметно улыбнулась."
    cs_narrator "Мы продолжили работу."
    cs_narrator "Тихонова достала альбом и начала перерисовывать расположение людей на фотографии."
    cs_narrator "Я придвинулась ближе."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Хорошая идея."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Так проще понять, кто где стоял."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 742fe504386a9808e38a
    cs_ls "Да."
    cs_ls "Только имена пока не подписывай."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Я и не собиралась."
    cs_narrator "Она аккуратно провела линию."
    cs_narrator "Я посмотрела на её рисунок."
    # cs_page_anchor: 0cd8f201949972a6f5cf
    cs_narrator "Тихонова работала спокойно, без лишних движений."
    cs_narrator "Несколько раз стирала контур, если он получался неточным."
    cs_narrator "Мне нравилось наблюдать за ней."
    cs_narrator "В отличие от большинства людей, она действительно умела терпеливо рисовать."
    cs_narrator "Я иногда начинала злиться на собственный эскиз уже через десять минут."
    cs_narrator "Женя заметила, что я смотрю через плечо Тихоновой, а не в свои записи."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 66af8a5e558420714614
    cs_mz "Соколова."
    cs_mz "Твоя часть — остановка."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я изучаю методы работы коллег."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Изучай свою страницу."
    if cs_friend_mz >= 4:
        cs_narrator "Женя протянула мне тетрадь."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        cs_mz "Посмотри, я ничего не пропустила про остановку?"
        cs_narrator "Я пробежала записи глазами."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Здесь лучше уточнить, что голос сначала звучал из салона, а потом за спиной."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 572af611579da602d59e
        cs_mz "Точно."
        cs_mz "Спасибо."
        cs_narrator "Она исправила строку."
        cs_narrator "Я неожиданно почувствовала себя не просто человеком, которому позволяют сидеть в библиотеке, а полноценным участником её работы."
        cs_narrator "Приятная перемена."
    else:
        cs_narrator "Женя прочитала запись про остановку вслух."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        cs_mz "Есть исправления?"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 4a12adf85ca31e3bc237
        cs_ls "Только одно."
        cs_ls "Конверт исчез до того, как автобус уехал."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        cs_mz "Хорошо."
        cs_narrator "Она внесла поправку."
    cs_narrator "Мы ещё несколько минут разбирали документы."
    cs_narrator "Семён пытался понять, какой именно край фотографии был повреждён."
    cs_narrator "Тихонова рисовала."
    cs_narrator "Даша сверяла листки."
    cs_narrator "Я наконец перестала ждать, что каждая строчка обязательно приведёт к новому открытию."
    $ cs_d5_knocks(7)
    $ cs_bus_cue('warning')
    cs_narrator "А потом в дверь постучали."
    cs_narrator "Сначала я даже не обратила внимания."
    cs_narrator "Мало ли кто пришёл в библиотеку."
    cs_narrator "Женя поднялась."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Сейчас открою."
    cs_narrator "Стук повторился."
    cs_narrator "Ровно."
    cs_narrator "Без спешки."
    cs_narrator "Ещё раз."
    cs_narrator "Я подняла голову."
    cs_narrator "Женя остановилась возле стола."
    cs_narrator "Стук продолжался."
    cs_narrator "Семён начал считать про себя."
    cs_narrator "На седьмом ударе стало тихо."
    if cs_d5_miku_volunteer:
        cs_narrator "Семён медленно повернулся ко мне."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: 2988e9ee02846206ff90
        cs_sy "Семь стуков."
        cs_sy "Мику утром именно это рассказывала."
    else:
        cs_narrator "Семён медленно повернулся к листку Мику."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: bcfcd6f90bee4251bc40
        cs_sy "Семь стуков."
        cs_sy "Она же именно это написала."
    $ cs_rev_sfx('sound/sfx/campus_door_rattle.ogg',0.3)
    cs_narrator "Дверная ручка опустилась."
    cs_narrator "Даша резко встала."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Не открывайте."
    cs_narrator "Я тоже поднялась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я не собиралась."
    cs_narrator "Ручка вернулась на место."
    cs_narrator "За дверью раздался голос."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Семён."
    cs_narrator "Он крепко сжал край стола."
    cs_narrator "Голос продолжил."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Сегодня."
    cs_narrator "Несколько секунд никто не двигался."
    $ cs_rev_sfx('sound/sfx/far_steps.ogg',0.25)
    cs_narrator "Затем по крыльцу прошли шаги."
    cs_narrator "Они оборвались раньше, чем достигли ступенек."
    cs_narrator "Я посмотрела на свои руки."
    cs_narrator "В правой всё ещё был карандаш."
    cs_narrator "Я сжимала его так сильно, что грифель сломался."
    cs_narrator "Чёрный кусочек упал рядом с фотографией."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ну вот."
    cs_narrator "Даша повернулась ко мне."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я положила карандаш на стол."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Даже канцелярия сегодня против меня."
    cs_narrator "Никто не засмеялся."
    cs_narrator "И я сама не стала продолжать."
    return
