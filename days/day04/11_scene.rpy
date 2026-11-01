# -*- coding: utf-8 -*-
label cs_day04_11:
    $ save_name = "Чужая смена — День 4: Ужин с Семёном"
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    cs_narrator "Мы вышли из библиотеки втроём."
    cs_narrator "Женя закрыла дверь и убрала ключи."
    cs_narrator "Даша посмотрела в сторону столовой."
    cs_narrator "А я неожиданно поймала себя на том, что ищу глазами одного конкретного человека."
    cs_narrator "Семёна."
    cs_narrator "Вот ведь."
    cs_narrator "Ещё недавно я искала его исключительно ради очередной дурацкой шутки."
    cs_narrator "Теперь хотелось просто убедиться, что он ходит где-то неподалёку."
    cs_narrator "Живой."
    cs_narrator "Здоровый."
    cs_narrator "И желательно недовольный моим присутствием."
    $ cs_director_scene("bg ext_square_sunset")
    scene bg ext_square_sunset
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Я оглядела площадь."
    cs_narrator "Возле столовой стояли несколько пионеров."
    cs_narrator "Кто-то разговаривал."
    cs_narrator "Кто-то уже направлялся внутрь."
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen', 'el']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "И наконец я увидела знакомую фигуру."
    cs_narrator "Семён беседовал с Электроником."
    cs_narrator "Тот что-то оживлённо объяснял, размахивая руками. Семён слушал с выражением лица человека, который уже несколько раз пожалел, что вообще остановился."
    cs_narrator "Я улыбнулась."
    cs_narrator "Вот."
    cs_narrator "Нормальный Семён."
    cs_narrator "Даша заметила мой взгляд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Нашла?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Женя посмотрела в ту же сторону."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Он ведь сегодня никуда не собирался пропадать."
    cs_narrator "Я немного помолчала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Знаю."
    cs_narrator "И добавила тише:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Просто хочу, чтобы так и продолжалось."
    cs_narrator "Женя ничего не ответила."
    cs_narrator "Мы подошли ближе."
    cs_narrator "Семён заметил меня первым."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Соколова."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Добрый вечер, Сёмочка."
    cs_narrator "Он прищурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что-то случилось?"
    cs_narrator "Я подняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Почему обязательно должно что-то случиться?"
    cs_narrator "Он посмотрел на Дашу."
    cs_narrator "Потом на Женю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Опыт."
    cs_narrator "Я вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Весь лагерь уже составил обо мне крайне несправедливое мнение."
    cs_narrator "Электроник заинтересованно повернулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    el "А что ты сделала?"
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сегодня пока ничего, о чём следовало бы рассказывать перед ужином."
    cs_narrator "Семён негромко кашлянул."
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Семён, это называется сохранение общественного спокойствия."
    cs_narrator "Электроник пожал плечами."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    el "Ну ладно. Я пойду, а то Шурик ждёт."
    cs_narrator "Он попрощался и направился к столовой."
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Мы остались вчетвером."
    cs_narrator "Семён посмотрел на Женю."
    cs_narrator "Потом на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ну и как разговор?"
    cs_narrator "Я немного помолчала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Есть новости."
    cs_narrator "Он сразу стал серьёзнее."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Плохие?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пока не знаю. Но определённо странные."
    cs_narrator "Женя посмотрела на нас обоих."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Давайте сначала поедим."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот. Товарищ библиотекарь совершенно правильно расставила приоритеты."
    cs_narrator "Она вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Соколова, не надо."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Всё. Молчу."
    $ cs_director_scene("bg int_dining_hall_sunset")
    scene bg int_dining_hall_sunset
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы вошли в столовую."
    cs_narrator "Внутри было шумно и тепло."
    cs_narrator "Возле раздачи уже собралась небольшая очередь. Откуда-то доносился смех, звенела посуда, а воздух был наполнен запахом горячей еды."
    cs_narrator "Семён оказался передо мной."
    cs_narrator "Он взял тарелку, повернулся и заметил, что я смотрю на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Лена."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "М?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Перестань."
    cs_narrator "Я удивилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что?"
    cs_narrator "Он тяжело вздохнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ты опять проверяешь, на месте ли я."
    cs_narrator "Я несколько секунд смотрела на него."
    cs_narrator "Потом кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Он немного помолчал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_semen") and renpy.get_attributes("cs_semen") != tuple("serious pioneer normal".split()):
        show cs_semen serious pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_sy "Я здесь."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вижу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Тогда хватит."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Постараюсь."
    cs_narrator "Он посмотрел на меня ещё несколько секунд."
    cs_narrator "Потом усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ты хотя бы честная."
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Иногда это мой единственный положительный профессиональный навык."
    cs_narrator "Он рассмеялся."
    cs_narrator "Мы устроились за столом у окна."
    cs_narrator "Женя села напротив Семёна."
    cs_narrator "Даша рядом со мной."
    cs_narrator "Некоторое время никто не поднимал тему старого лагеря."
    cs_narrator "Мы просто ели."
    cs_narrator "Семён рассказал, что после завтрака помогал Электронику и Шурику в кружке."
    cs_narrator "По словам Семёна, Электроник пытался что-то починить, а Шурик объяснял, как оно должно работать."
    cs_narrator "Я сочувственно кивала. Мой компьютер тоже любил теоретические беседы посреди срочного проекта."
    cs_narrator "Женя поинтересовалась, не собирается ли Семён записаться в кружок."
    cs_narrator "Он посмотрел на неё."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Не знаю. Может быть."
    cs_narrator "Я подняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка, а ты удивляешь."
    cs_narrator "Он прищурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что теперь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сначала библиотека, теперь технический кружок. Ещё немного — и станешь образцовым пионером."
    cs_narrator "Он вздохнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Я просто помогал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Скромность тоже засчитывается."
    cs_narrator "Даша рассмеялась."
    cs_narrator "Женя улыбнулась."
    cs_narrator "Потом разговор постепенно стих."
    cs_narrator "Семён отложил ложку."
    cs_narrator "Посмотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Слушай, Лен."
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да?"
    cs_narrator "Он немного помолчал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А если завтра ничего не произойдёт?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тогда проживём обычный день."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А послезавтра?"
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тогда будем решать по обстоятельствам."
    cs_narrator "Он нахмурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ты ведь знаешь, что в оригинальной истории это был важный момент."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Знаю."
    cs_narrator "Он продолжал смотреть."
    cs_narrator "Я медленно положила ложку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Но больше не хочу обращаться с этим знанием как с инструкцией."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Почему?"
    cs_narrator "Я показала на Женю."
    cs_narrator "Потом на Дашу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Потому что здесь уже происходят события, которых я не помню."
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И если буду уверять тебя, что точно знаю, чем всё закончится, просто обману."
    cs_narrator "Семён некоторое время молчал."
    cs_narrator "Потом кивнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Хорошо."
    cs_narrator "Женя задумчиво посмотрела на нас."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "То есть седьмой день может оказаться важным?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Но может пройти совершенно обычно?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Она вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Ненавижу такие ответы."
    cs_narrator "Я слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я тоже. Но пока других нет."
    cs_narrator "Некоторое время мы молчали."
    $ renpy.music.set_volume(0.13,channel="music",delay=1.5)
    cs_narrator "Потом я вспомнила разговор в библиотеке."
    cs_narrator "Посмотрела на Семёна."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Слушай, а тебе здесь снилось что-нибудь странное?"
    cs_narrator "Он поднял бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Кроме самого лагеря?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Семён задумался."
    cs_narrator "Он отложил ложку и посмотрел в окно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_semen") and renpy.get_attributes("cs_semen") != tuple("thinking pioneer normal".split()):
        show cs_semen thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_sy "Была дорога."
    cs_narrator "Я замерла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Какая?"
    cs_narrator "Он немного помолчал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Та, возле ворот."
    cs_narrator "Даша подняла голову."
    cs_narrator "Женя тоже перестала есть."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Я шёл по ней. Долго. Но сколько ни шёл, всё равно оказывался возле лагеря."
    cs_narrator "Я медленно выдохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Когда тебе это приснилось?"
    cs_narrator "Семён задумался."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Один раз ещё до того, как мы вместе проверили дорогу."
    cs_narrator "Я почувствовала неприятный холодок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А второй?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Уже после."
    cs_narrator "Мы переглянулись."
    cs_narrator "Значит, дорога приснилась ему раньше, чем он попробовал по ней уйти."
    cs_narrator "Даша осторожно спросила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Там был кто-нибудь ещё?"
    cs_narrator "Семён немного помолчал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Кажется, у ворот стояла девушка."
    cs_narrator "Я почувствовала, как внутри всё сжалось."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты видел лицо?"
    cs_narrator "Он покачал головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "А волосы?"
    cs_narrator "Семён задумался."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Тёмные. Но было плохо видно."
    cs_narrator "Я переглянулась с Дашей."
    cs_narrator "Два хвостика, тёмные волосы. Я прикусила язык: пока слишком мало, чтобы делать выводы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Она что-нибудь сказала?"
    cs_narrator "Семён кивнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Во втором сне."
    cs_narrator "Он опустил взгляд."
    cs_narrator "Несколько секунд молчал."
    cs_narrator "Потом произнёс:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "«Ты опять вернулся»."
    cs_narrator "За столом стало тихо. Слишком часто сегодня мы слышали это «опять»."
    cs_narrator "Женя медленно подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "А я слышала: «Она пришла раньше»."
    cs_narrator "Семён повернулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Кто?"
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Не знаю."
    cs_narrator "Даша задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Получается, во всех этих словах есть намёк на то, что что-то уже происходило."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Потом осторожно добавила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Но пока это только слова из снов. И голос, который мы слышали под землёй."
    cs_narrator "Семён посмотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А у тебя?"
    cs_narrator "Я удивилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Сны."
    cs_narrator "Я задумалась."
    cs_narrator "События последних ночей путались в голове. И вдруг всплыла остановка: солнечный свет, стекло и моё лицо по ту сторону."
    cs_narrator "Я замерла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Был один."
    cs_narrator "Даша повернулась ко мне."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Какой?"
    cs_narrator "Я закрыла глаза."
    cs_narrator "Попыталась восстановить картину."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мне снилась остановка."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Наша?"
    cs_narrator "Я немного подумала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не уверена. Но на табличке был маршрут 410."
    cs_narrator "Женя нахмурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Автобус стоял?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты в него садилась?"
    cs_narrator "Я покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нет."
    cs_narrator "Я попыталась разглядеть воспоминание яснее: стекло, отражение, собственное лицо."
    cs_narrator "Я медленно открыла глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я стояла снаружи."
    cs_narrator "Семён смотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А внутри?"
    cs_narrator "Я почувствовала, как неприятно похолодели пальцы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Внутри сидела я."
    cs_narrator "Никто не ответил."
    cs_narrator "Я продолжила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Другая я. С тем же лицом."
    cs_narrator "Даша нахмурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты уверена?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Насколько вообще можно быть уверенной в собственном сне."
    cs_narrator "В памяти возникла ещё одна деталь."
    cs_narrator "Я резко подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И на стекле была надпись."
    cs_narrator "Женя посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Какая?"
    cs_narrator "Я тихо произнесла:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "«Не садись второй раз»."
    cs_narrator "Семён откинулся на спинку стула."
    cs_narrator "Долго смотрел на меня."
    cs_narrator "Потом тяжело выдохнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "И ты только сейчас об этом вспомнила?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Соколова…"
    cs_narrator "Я подняла руку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Знаю. Надо было рассказать раньше."
    cs_narrator "Женя задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "А может, ты вспомнила потому, что мы начали обсуждать сны?"
    cs_narrator "Я посмотрела на неё."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Возможно."
    cs_narrator "Даша кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Тогда нужно записывать всё сразу после пробуждения."
    cs_narrator "Я задумалась."
    cs_narrator "Хорошая мысль."
    cs_narrator "Особенно учитывая, что завтра утром мне совершенно не хочется повторять сегодняшние подвиги."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Согласна."
    cs_narrator "Я посмотрела на остальных."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Даже если кажется полной бессмыслицей."
    cs_narrator "Семён усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "У меня тогда будет довольно длинный список."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ничего. Женя предоставит методологию архивирования."
    cs_narrator "Она посмотрела на меня поверх очков."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Я ещё не соглашалась."
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тогда прошу содействия в культурно-просветительских целях."
    cs_narrator "Женя вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Соколова, записывать сны вы и сами можете."
    cs_narrator "Семён рассмеялся."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Справедливо. Библиотечная администрация отказалась принимать дополнительные обязательства."
    if cs_d4_se_honest_fear == True:
        cs_narrator "Семён посмотрел на меня внимательнее."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sy "Лен."
        cs_narrator "Я повернулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Да?"
        cs_narrator "Он немного помолчал."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sy "Ты ведь не собираешься завтра ходить за мной по пятам?"
        cs_narrator "Я задумалась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Нет."
        cs_narrator "Он заметно расслабился."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Но если понадобится помощь, скажи."
        cs_narrator "Семён кивнул."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sy "Скажу."
        cs_narrator "Несколько секунд мы смотрели друг на друга."
        cs_narrator "Потом он усмехнулся."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sy "И всё-таки спасибо."
        cs_narrator "Я чуть улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Не за что, Сёмочка."
        cs_narrator "Вот."
        cs_narrator "Кажется, нормальный разговор иногда работает лучше двадцати шуток подряд."
    else:
        cs_narrator "Семён посмотрел на меня."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sy "Только не превращай меня завтра в подопытного."
        cs_narrator "Я покачала головой."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Не буду."
        cs_narrator "Потом слегка улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Хотя право иногда проверить, на месте ли ты, оставляю за собой."
        cs_narrator "Он вздохнул."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sy "Неисправима."
        cs_narrator "Я развела руками."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "У каждого свои недостатки."
    cs_narrator "Мы закончили ужин."
    cs_narrator "Собрали подносы."
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "И вышли из столовой."
    cs_narrator "Вечерний воздух был заметно прохладнее дневного."
    cs_narrator "Небо постепенно темнело, а деревья отбрасывали длинные тени на дорожки."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Потом на Женю."
    cs_narrator "На Дашу."
    cs_narrator "Ещё вчера мы могли спокойно обсуждать книги, музыку и обычные лагерные дела."
    cs_narrator "Сегодня обсуждаем, кто сколько раз мог оказаться возле одних и тех же ворот."
    cs_narrator "Я вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ну что?"
    cs_narrator "Семён повернулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что?"
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Предлагаю провести остаток вечера максимально нормально."
    cs_narrator "Женя приподняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "В твоём понимании?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Например, почитать книги."
    cs_narrator "Она несколько секунд смотрела на меня."
    cs_narrator "Потом усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Вот это действительно неожиданно разумное предложение."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пользуйтесь моментом. Второй раз за день здравый смысл может и не появиться."
    cs_narrator "Семён рассмеялся."
    cs_narrator "Даша улыбнулась."
    cs_narrator "И мы направились к библиотеке."
    return
