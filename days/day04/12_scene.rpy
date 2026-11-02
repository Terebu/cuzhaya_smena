# -*- coding: utf-8 -*-
label cs_day04_12:
    $ save_name = "Чужая смена — День 4: Вечерний разговор в библиотеке"
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0
    cs_narrator "До библиотеки мы дошли вчетвером."
    cs_narrator "На площади уже почти никого не было."
    cs_narrator "Свет из окон домиков ложился на дорожки узкими прямоугольниками, а между деревьями постепенно сгущались сумерки."
    cs_narrator "У крыльца Семён остановился и посмотрел на Женю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Слушай, а правила какие?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Правила?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Да. Не хочу, чтобы меня выгнали через пять минут."
    cs_narrator "Женя поправила очки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Не кричать. Не мешать другим. Книги без спроса с полок не переставлять."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Понятно."
    cs_narrator "Я приложила руку к груди."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка…"
    cs_narrator "Он закрыл глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты добровольно спросил правила поведения в библиотеке."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "И?"
    cs_narrator "Я перевела взгляд с Жени на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я тронута."
    cs_narrator "Он покачал головой."
    cs_narrator "Женя усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Заходите уже, пока она не начала произносить торжественную речь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Предложение принимается."
    cs_narrator "Женя открыла дверь."
    $ night_time()
    $ persistent.sprite_time = "night"
    $ cs_director_scene("cs_library_interior_night")
    scene cs_library_interior_night
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы вошли."
    cs_narrator "Внутри было уже заметно темнее, чем днём."
    cs_narrator "Она включила свет, прошла к своему столу и положила ключи рядом с журналом."
    cs_narrator "Знакомые полки погрузились в мягкий свет ламп."
    cs_narrator "За окнами медленно темнело."
    cs_narrator "Рядом были Даша, Женя и Семён. От этого стало спокойнее. Правда, Семён всё ещё пытался понять, как его записали на добровольное вечернее чтение."
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты что-нибудь читать будешь?"
    cs_narrator "Он пожал плечами."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Наверное."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что любишь?"
    cs_narrator "Он задумался."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Фантастику."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Отличный выбор."
    cs_narrator "Женя повернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Могу подобрать."
    cs_narrator "Потом кивнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Давай."
    cs_narrator "Она прошла между стеллажами."
    cs_narrator "Некоторое время изучала корешки."
    cs_narrator "Затем сняла с полки сборник научно-фантастических рассказов."
    cs_narrator "Вернулась."
    cs_narrator "Протянула ему."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Попробуй это."
    cs_narrator "Семён посмотрел на обложку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Спасибо."
    cs_narrator "Культурное развитие населения принимает угрожающие масштабы. Я промолчала, но Женя заметила улыбку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Соколова."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Даже не начинай."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не собиралась."
    cs_narrator "Она продолжала смотреть."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Просто очень горжусь успехами наших читателей."
    cs_narrator "Семён тяжело выдохнул."
    cs_narrator "Даша рассмеялась."
    cs_narrator "Мы расселись."
    cs_narrator "Я вернулась к книге, начатой после обеда."
    cs_narrator "Даша взяла небольшой сборник и устроилась рядом."
    cs_narrator "Семён занял место возле окна."
    cs_narrator "Женя вернулась к своему столу."
    cs_narrator "Разговоры стихли. Теперь слышались только страницы и редкий скрип стула."
    cs_narrator "Иногда со стороны улицы доносились шаги, но они быстро затихали."
    cs_narrator "Я перевернула страницу."
    cs_narrator "И вдруг поняла, насколько сильно устала."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Не физически."
    cs_narrator "Хотя утренний поход и продолжительные прогулки по лагерю тоже давали о себе знать."
    cs_narrator "Скорее от постоянного ожидания."
    cs_narrator "От ощущения, что за каждым новым поворотом обязательно должно скрываться что-то неизвестное."
    cs_narrator "А здесь ничего не происходило."
    cs_narrator "И это было прекрасно."
    cs_narrator "Через некоторое время Семён поднял голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Лен."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "М?"
    cs_narrator "Он показал на раскрытую страницу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Иди сюда на минуту."
    cs_narrator "Я положила закладку и подошла."
    cs_narrator "Он указал на абзац."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Здесь герой возвращается к месту, которое помнил совсем другим. Невольно сравниваю с нашим лагерем."
    cs_narrator "Я прочитала несколько строк."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Совпадение."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Я понимаю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Но неприятное."
    cs_narrator "Я присела рядом."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Только не начинай теперь искать подсказки во всех книгах подряд."
    cs_narrator "Семён усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А ты бы не начала?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "После сегодняшнего утра стараюсь хотя бы иногда включать критическое мышление."
    cs_narrator "Он рассмеялся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Успешно?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "С переменным результатом."
    cs_narrator "Он улыбнулся."
    cs_narrator "Я показала на книгу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Это художественная история. Сама по себе она ничего не доказывает."
    cs_narrator "Потом перевела взгляд на стол Жени."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А вот фотографии с неправильной датой можно изучать."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Понял."
    cs_narrator "Я поднялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Поэтому сегодня никаких дополнительных экспедиций."
    cs_narrator "Он посмотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Это ты себе говоришь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "В первую очередь."
    cs_narrator "Он тихо рассмеялся."
    cs_narrator "Я вернулась за стол."
    cs_narrator "Даша подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Всё нормально?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты стала осторожнее с выводами."
    cs_narrator "Я посмотрела на неё."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Приходится."
    cs_narrator "Я провела пальцем по краю книги."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Когда знаешь какую-нибудь историю, очень легко начать считать, что здесь всё должно происходить точно так же."
    cs_narrator "Даша кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А люди могут вести себя иначе."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Я посмотрела на Женю и Семёна. Оба всё меньше походили на мои представления о них. Здесь шла их жизнь, а я слишком долго сверялась со сценарием."
    cs_narrator "В этот момент Женя подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Лена."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да?"
    cs_narrator "Она держала лист бумаги."
    cs_narrator "Тот самый, на котором после обеда записывала воспоминания."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("thoughtful pioneer normal".split()):
        show cs_zhenya thoughtful pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Я вспомнила ещё кое-что."
    cs_narrator "Мы с Дашей отложили книги."
    cs_narrator "Семён тоже поднялся и подошёл ближе."
    cs_narrator "Женя положила лист перед нами."
    cs_narrator "На бумаге было несколько коротких строк."
    cs_narrator "Дорога."
    cs_narrator "Красный свет."
    cs_narrator "Четвёртый день."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Она пришла раньше."
    cs_narrator "Не буди вторую."
    cs_narrator "Я перечитала последнюю строку. Потом ещё раз."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Подожди."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты уверена в последней фразе?"
    cs_narrator "Она помолчала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Не полностью. Но мне кажется, именно так."
    cs_narrator "Даша нахмурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "«Вторую»?"
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Он тоже заметно напрягся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Лен, тебе же снились две версии себя."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Женя посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Думаешь, речь о тебе?"
    cs_narrator "Потом покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не знаю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Это может относиться к кому угодно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Потом снова на запись."
    cs_narrator "Не буди вторую."
    cs_narrator "Кого нельзя будить? И кто это сказал? Чем дольше я смотрела на запись, тем сильнее хотелось оглянуться."
    cs_narrator "Вспомнились коридор, голос, фотографии. И сон, в котором за стеклом автобуса сидела другая я."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Всё словно пыталось сложиться в одну картину."
    cs_narrator "Но пока не хватало слишком многих деталей."
    cs_narrator "Я осторожно отодвинула лист."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не будем подгонять ответы под знакомые обстоятельства."
    cs_narrator "Семён приподнял бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Соколова, это действительно ты?"
    cs_narrator "Я усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да. Сегодня у меня день личностного роста."
    cs_narrator "Женя тихо рассмеялась."
    cs_narrator "Потом снова посмотрела на запись."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "А если речь о четвёртом дне?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Возможно, событие уже произошло."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Например, твой поход в старый лагерь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Может быть."
    cs_narrator "Даша посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Или речь вообще о чём-то другом."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот поэтому и нужно записывать."
    cs_narrator "Я взяла отдельный лист. «Кто „она“? Кто „вторая“? Что значит „раньше“? Почему четвёртый день?»"
    cs_narrator "Подумала и дописала: «Не считать предположения фактами»."
    cs_narrator "Женя посмотрела на запись."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Это особенно полезно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мне показалось, что ты сейчас намекнула на кого-то конкретного."
    cs_narrator "Она спокойно ответила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Возможно."
    cs_narrator "Семён рассмеялся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Всё. Даже здесь от тебя не спрячешься."
    cs_narrator "Женя усмехнулась."
    cs_narrator "Но потом внимательно посмотрела на лист."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Я сохраню оба."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Хорошо."
    cs_narrator "Она достала папку с фотографией 1971 года и списком, вложила записи. Убрала папку обратно в ящик и заперла его."
    $ cs_d4_dream_phrase_second = True
    $ cs_d4_dream_notes_location = "library_locked_drawer"
    cs_narrator "На сегодня договорились закончить с находками. Всем требовался отдых."
    cs_narrator "Женя вернулась к своему журналу."
    cs_narrator "Семён устроился возле окна."
    cs_narrator "Даша снова открыла книгу."
    cs_narrator "А я попыталась продолжить чтение."
    cs_narrator "Сначала это давалось трудно."
    cs_narrator "Последняя фраза Жени продолжала крутиться в голове."
    cs_narrator "Не буди вторую."
    cs_narrator "Я несколько раз перечитывала один и тот же абзац, пока не поняла, что совершенно не воспринимаю написанное."
    cs_narrator "Пришлось закрыть книгу."
    cs_narrator "Я посмотрела в окно."
    cs_narrator "За стеклом уже стало темно."
    cs_narrator "Вдалеке горел фонарь, освещавший узкую дорожку."
    cs_narrator "Где-то слышались сверчки."
    cs_narrator "Всё было спокойно."
    cs_narrator "И всё-таки я невольно прислушивалась."
    cs_narrator "Словно ожидала снова услышать своё имя."
    cs_narrator "Но никто не звал."
    cs_narrator "Я выдохнула."
    cs_narrator "Хватит, Соколова."
    cs_narrator "Сегодня действительно хватит."
    cs_narrator "Я снова открыла книгу."
    cs_narrator "И на этот раз постепенно смогла сосредоточиться."
    cs_narrator "Следующие полчаса мы действительно просто читали."
    cs_narrator "Без разговоров."
    cs_narrator "Без попыток объяснить происходящее."
    cs_narrator "Иногда Семён переворачивал страницу."
    cs_narrator "Даша чуть меняла положение на стуле."
    cs_narrator "Женя что-то записывала."
    cs_narrator "Обычные мелочи."
    cs_narrator "И почему-то именно они теперь казались особенно важными."
    cs_narrator "Я посмотрела на окружающих."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Вот бы так ещё немного."
    cs_narrator "Без голосов и загадок. Без необходимости проверять, не исчез ли кто-нибудь."
    cs_narrator "Семён поднял голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ничего."
    cs_narrator "Он прищурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Опять?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Просто рада, что мы все здесь."
    cs_narrator "Он немного помолчал."
    cs_narrator "Потом кивнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Я тоже."
    cs_narrator "И снова опустил взгляд в книгу."
    cs_narrator "Ближе к отбою Женя закрыла журнал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Всё. Пора заканчивать."
    cs_narrator "Я посмотрела на часы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Уже?"
    cs_narrator "Она усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Да. И на этот раз никаких дополнительных пяти минут."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Жестокая женщина."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Зато последовательная."
    cs_narrator "Мы начали собираться."
    cs_narrator "Семён подошёл к Жене со своей книгой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Можно завтра дочитать?"
    cs_narrator "Она кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Конечно. Только не потеряй."
    cs_narrator "Я повернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка…"
    cs_narrator "Он немедленно поднял палец."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я просто хотела сказать, что горжусь тобой."
    cs_narrator "Он вздохнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Спасибо. Теперь можно идти?"
    cs_narrator "Женя рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Можно."
    $ cs_director_scene("cs_library_exterior_night")
    scene cs_library_exterior_night
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы вышли на крыльцо."
    cs_narrator "Ночной воздух встретил приятной прохладой."
    cs_narrator "Женя закрыла библиотеку и повернулась к нам."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Если завтра кому-нибудь приснится что-то ещё, расскажете?"
    cs_narrator "Семён кивнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Конечно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Обязательно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И, Женя…"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Если сама вспомнишь что-нибудь новое, тоже скажи."
    cs_narrator "Женя кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Скажу."
    cs_narrator "Даша слегка коснулась моей руки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И ты тоже."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да. Первой услышишь ты."
    if cs_d4_mz_friend_before_choice >= 3 and cs_mz_hug_allowed_day3 == True:
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Можно на прощание?"
        cs_narrator "Она поняла."
        cs_narrator "Чуть улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("shy pioneer normal".split()):
            show cs_zhenya shy pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_mz "Можно. Только недолго."
        cs_narrator "Я осторожно обняла её."
        $ cs_d4_mz_hug_12 = True
        cs_narrator "Она ответила."
        cs_narrator "Потом сама отступила."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Спокойной ночи."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Спокойной."
    else:
        cs_narrator "Я просто кивнула."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "До завтра, Женя."
        cs_narrator "Она улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "До завтра."
    cs_narrator "Женя направилась к своему домику."
    $ cs_director_scene("bg ext_square_night")
    scene bg ext_square_night
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы остались втроём."
    cs_narrator "Ночная площадь выглядела совсем иначе, чем днём."
    cs_narrator "Деревья отбрасывали длинные тени. Окна столовой уже погасли, а издалека доносился звук закрывающейся двери."
    cs_narrator "Семён шёл рядом, держа книгу под мышкой."
    cs_narrator "В какой-то момент он остановился."
    cs_narrator "Посмотрел в сторону домика вожатой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ну, мне туда."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Семён."
    cs_narrator "Он повернулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Если ночью проснёшься и вдруг захочешь куда-нибудь пойти, сначала подумай."
    cs_narrator "Он усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ты тоже."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Договорились."
    cs_narrator "Он посмотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "И завтра утром встречаемся?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "До завтрака."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Хорошо."
    cs_narrator "Я протянула ему руку."
    cs_narrator "Он пожал."
    cs_narrator "Я уже собиралась отпустить, но вдруг тихо сказала:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спокойной ночи, Сёмочка."
    cs_narrator "Он закрыл глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Лена…"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что?"
    cs_narrator "Он посмотрел на меня и усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Спокойной ночи, ненормальная."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот. Совсем другое дело."
    cs_narrator "Он рассмеялся."
    cs_narrator "Потом развернулся и направился к домику Ольги Дмитриевны."
    cs_narrator "Я некоторое время смотрела ему вслед."
    cs_narrator "До тех пор, пока он не скрылся за поворотом."
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Даша стояла рядом."
    cs_narrator "Наконец она тихо спросила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Пойдём?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пойдём."
    $ cs_director_scene("cs_camp_path_night")
    scene cs_camp_path_night
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы направились к своему домику."
    if not cs_d4_choice_12_done:
        menu:
            "Спросить Дашу, что она почувствовала, когда не нашла меня утром":
                $ cs_friend_da += 1
                $ cs_d4_da_talked_about_fear = True
                cs_narrator "Мы прошли несколько метров молча."
                cs_narrator "Даша смотрела на дорожку, осторожно обходя небольшие лужи."
                cs_narrator "Я несколько раз собиралась заговорить."
                cs_narrator "Но никак не могла подобрать подходящие слова."
                cs_narrator "В конце концов просто замедлила шаг."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Даш."
                cs_narrator "Она повернулась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Да?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Можно кое-что спросить?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Конечно."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Ты утром сильно испугалась?"
                cs_narrator "Даша не ответила сразу."
                cs_narrator "Сначала посмотрела на меня."
                cs_narrator "Потом перевела взгляд на тёмные деревья."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Да."
                cs_narrator "Я опустила глаза."
                cs_narrator "Она продолжила:"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Сначала подумала, что ты просто вышла побегать."
                cs_narrator "Даша помолчала."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "А потом поняла, что тебя нигде нет."
                cs_narrator "Утром я думала только о том, куда пойду. А о Даше, которая проснётся и не найдёт меня, — ни разу."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Мне стало страшно, что ты могла уйти куда-нибудь, откуда не сможешь вернуться."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Понимаю."
                cs_narrator "Даша повернулась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Правда?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Да. Особенно после того, что произошло под землёй."
                cs_narrator "Мы остановились под фонарём."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Знаешь, я не могу обещать, что больше никогда не совершу глупость."
                cs_narrator "Даша улыбнулась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Это было бы слишком смелое обещание."
                cs_narrator "Я усмехнулась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Особенно с моей биографией."
                cs_narrator "Потом стала серьёзнее."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Но могу обещать, что больше не стану исчезать, ничего тебе не сказав."
                cs_narrator "Даша смотрела на меня, потом улыбнулась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Мне этого достаточно."
                cs_narrator "Я осторожно взяла её за руку."
                cs_narrator "Чуть сильнее сжала ладонь. Больше ничего обещать не стала."
            "Не возвращаться к утреннему происшествию и дать Даше отдохнуть":
                $ cs_d4_da_quiet_evening = True
                cs_narrator "Даша выглядела уставшей. За день хватило фотографий, снов и разговоров о том, что случится завтра."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Слушай, а давай сегодня больше не будем говорить о подземельях."
                cs_narrator "Она повернулась ко мне."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "С удовольствием."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Отлично. Режим тревоги отменяется до утра."
                cs_narrator "Даша рассмеялась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "А завтра?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Завтра посмотрим."
                cs_narrator "Она улыбнулась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Договорились."
                cs_narrator "Мы пошли дальше."
                cs_narrator "У меня оставалось сорок вопросов. Они могли подождать."
        $ cs_d4_choice_12_done = True
    $ cs_director_scene("cs_house_lena_darya_ext_night")
    scene cs_house_lena_darya_ext_night
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Домик уже виднелся между деревьями."
    cs_narrator "Из соседнего окна пробивалась узкая полоска света."
    cs_narrator "Где-то в траве стрекотали сверчки."
    if cs_da_shared_bed_day3 == True:
        cs_narrator "У самого крыльца она неожиданно остановилась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Лен."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "М?"
        cs_narrator "Она улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        if renpy.showing("cs_darya") and renpy.get_attributes("cs_darya") != tuple("shy_smile pioneer normal".split()):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_da "Сегодня опять вместе?"
        cs_narrator "Я улыбнулась, не сразу найдя ответ."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Ты сама предлагаешь?"
        cs_narrator "Даша кивнула."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Да."
        cs_narrator "Я почувствовала приятное тепло."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Тогда с удовольствием."
        cs_narrator "Она взяла меня за руку."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Только без побегов до рассвета."
        cs_narrator "Я тихо рассмеялась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Обещаю."
        cs_narrator "Потом посмотрела на неё внимательнее."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Сегодня я сама не хочу просыпаться одна."
        cs_narrator "Даша ничего не ответила."
        cs_narrator "Просто подошла чуть ближе."
    if cs_da_shared_bed_day3 == True and cs_da_love_confession_day3 == True:
        cs_narrator "Помолчав, Даша тихо добавила:"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "И, Лен…"
        cs_narrator "Я повернулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "М?"
        cs_narrator "Даша улыбнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Я помню наш вчерашний разговор."
        cs_narrator "Щёки снова потеплели. Второй раз за день — уже статистика."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Просто хотела, чтобы ты знала."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Спасибо."
    if cs_da_shared_bed_day3 == False:
        cs_narrator "Даша посмотрела на меня."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Надеюсь, завтра утром ты не собираешься снова исчезать?"
        cs_narrator "Я покачала головой."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Нет."
        cs_narrator "Она кивнула."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Даже если приснится ещё один автобус, обещаю сначала проснуться, а уже потом делать выводы."
        cs_narrator "Даша рассмеялась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Уже неплохо."
        if cs_friend_da >= 3:
            cs_narrator "Даша помолчала, глядя на меня."
            if cs_reflective_shot:
                $ cs_frame_focus(cs_d4_scene_cast)
                with cs_sprite_change
            cs_da "И если захочешь поговорить перед сном, я не против."
            if cs_reflective_shot:
                $ cs_frame_focus(cs_d4_scene_cast)
                with cs_sprite_change
            cs_ls "Спасибо."
    cs_narrator "Мы поднялись на крыльцо."
    cs_narrator "Я остановилась перед дверью."
    cs_narrator "Вечерний воздух стал прохладнее."
    cs_narrator "Сквозь ветви деревьев виднелось тёмное небо."
    cs_narrator "Где-то далеко ещё горели окна домиков."
    cs_narrator "Лагерь постепенно засыпал."
    cs_narrator "Я обернулась."
    cs_narrator "Посмотрела в сторону площади."
    cs_narrator "Потом туда, где за лесом находился старый корпус."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Сегодня утром я отправилась туда одна."
    cs_narrator "Хотела найти ответы. Принесла фотографии, списки и голос, знающий обо мне слишком много."
    cs_narrator "«Ты не должна была проснуться здесь». Кто это сказал? Почему велел уйти?"
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она стояла рядом."
    cs_narrator "Немного уставшая."
    cs_narrator "Но спокойная."
    cs_narrator "И почему-то именно сейчас я поняла, насколько сильно за последние дни изменилась моя жизнь."
    cs_narrator "В Москве остались работа, рисунки, подписчики, знакомые улицы. И люди, с которыми я могла встретиться в любой момент."
    cs_narrator "А здесь появились другие люди."
    cs_narrator "Женя, с которой можно спорить и молчать."
    cs_narrator "Семён, который упорно делает вид, что не рад меня видеть."
    cs_narrator "Славя, способная найти поручение даже для человека, который только что чудом выбрался из подземелья."
    cs_narrator "И Даша."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она заметила мой взгляд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ничего."
    cs_narrator "Она прищурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Опять?"
    cs_narrator "Я тихо рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Просто подумала, что за четыре дня успела привыкнуть к этому месту сильнее, чем ожидала."
    cs_narrator "Даша оглянулась на дорожку и посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Я тоже."
    cs_narrator "Мы некоторое время молчали."
    cs_narrator "Ветер тихо шевелил листья над головой."
    cs_narrator "И впервые за весь день я не чувствовала необходимости немедленно что-нибудь выяснять."
    cs_narrator "Завтра у Семёна шестой день. Послезавтра седьмой. Может, всё изменится. Может, будем помогать Славе, слушать музыку и спорить о книгах. Я не знала."
    cs_narrator "Но сейчас Семён и Женя разошлись по домикам, а Даша была рядом. Я повернулась к ней."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пойдём домой?"
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Пойдём."
    $ cs_director_scene("cs_house_lena_darya_int_night")
    scene cs_house_lena_darya_int_night
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Я открыла дверь."
    cs_narrator "Внутри было темно и тихо."
    cs_narrator "Кровати, стол, наши вещи на стульях. Всё на месте."
    cs_narrator "Я переступила порог."
    cs_narrator "Даша вошла следом."
    cs_narrator "За спиной тихо закрылась дверь."
    cs_narrator "И впервые за весь день мне совершенно не захотелось проверять, что скрывается за следующим поворотом."
    $ cs_d4_shared_bed = cs_da_shared_bed_day3
    cs_narrator "Мы по очереди умылись и переоделись ко сну. Разговоры наконец стихли."
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    if cs_d4_shared_bed:
        $ cs_director_scene("cs_cg_lena_darya_shared_sleep_night")
        scene cs_cg_lena_darya_shared_sleep_night
        $ cs_d4_scene_cast = []
        $ cs_frame_focus(cs_d4_scene_cast)
        with Dissolve(0.7)
        cs_narrator "Даша устроилась рядом. Я почувствовала её спокойное дыхание и закрыла глаза."
    else:
        cs_narrator "Мы легли каждая на свою кровать. Я пожелала Даше спокойной ночи и закрыла глаза."
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    window hide dissolve
    $ cs_director_scene("black")
    scene black
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    show text "Конец четвёртого дня" at truecenter
    with Dissolve(0.8)
    $ renpy.pause(2.0)
    hide text
    with Dissolve(0.8)
    return
