# -*- coding: utf-8 -*-
label cs_day03_113a:
    $ save_name = "Чужая смена — День 3: Каталог не является картой"
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_113_library_exterior:
    cs_narrator "Мы поднялись на библиотечное крыльцо."
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ renpy.music.set_volume(0.05,delay=1.0,channel="ambience")
    $ renpy.music.set_volume(0.08,delay=1.0,channel="music")
    label cs_check_day03_113_catalog:
    cs_narrator "В библиотеке было тихо."
    cs_narrator "Настолько тихо, что после шумных дорожек лагеря мне показалось, будто кто-то убавил громкость окружающего мира."
    cs_narrator "Я остановилась возле двери."
    cs_th "Вот."
    cs_th "Прекрасное место."
    cs_th "Никаких чрезвычайных происшествий."
    cs_th "Никто не требует тащить коробки."
    cs_th "И даже разговаривать можно шёпотом, не вызывая подозрений."
    cs_narrator "Женя сидела за столом."
    cs_narrator "Перед ней лежало несколько ящичков с карточками."
    cs_narrator "Услышав наши шаги, она подняла голову."
    cs_mz "Пришли?"
    cs_narrator "Я кивнула."
    cs_ls "Как и обещали."
    cs_narrator "Она посмотрела на мою повязку."
    cs_mz "У Виолы были?"
    cs_ls "Да. Повязку поменяли, жить разрешили."
    cs_narrator "Женя слегка улыбнулась."
    cs_mz "Уже хорошо."
    cs_narrator "Дарья подошла ближе к столу."
    cs_da "Что-нибудь нашлось?"
    cs_narrator "Женя посмотрела на карточки."
    cs_mz "Пока ничего особенно полезного. Я подняла старые каталоги и несколько списков библиотечного фонда."
    cs_narrator "Я заинтересованно наклонилась."
    cs_ls "Можно посмотреть?"
    cs_narrator "Женя кивнула."
    cs_mz "Только карточки не перемешивай. Я их уже рассортировала."
    cs_narrator "Я приложила здоровую ладонь к груди."
    cs_ls "Женя, я художник. У меня сложные отношения с порядком, но чужую систему хранения я уважаю."
    cs_narrator "Она усмехнулась."
    cs_mz "Вот и замечательно."
    cs_narrator "Я устроилась рядом со столом."
    cs_narrator "Дарья заглянула через моё плечо."
    cs_narrator "На карточках значились названия книг, фамилии авторов, инвентарные номера."
    cs_narrator "Часть записей была сделана аккуратным почерком."
    cs_narrator "Другие выглядели так, будто их заполняли в последние минуты рабочего дня."
    cs_th "Ничего сверхъестественного."
    cs_th "Обычная библиотека."
    cs_th "Обычные документы."
    cs_th "Удивительно успокаивающая вещь."
    cs_da "А что именно мы ищем?"
    cs_narrator "Женя посмотрела на неё."
    cs_mz "Если вам нужен план лагеря, то в каталоге книг его, скорее всего, не будет."
    cs_narrator "Я кивнула."
    cs_ls "Понимаем. Но вдруг есть какие-нибудь старые справочники, материалы о районе или что-то подобное?"
    cs_narrator "Она задумалась."
    cs_mz "Это можно проверить. Только тут всё записано по изданиям, а не по содержанию каждой главы."
    cs_narrator "Я посмотрела на длинный ряд карточек."
    cs_ls "То есть система хорошая, но мои поисковые запросы не поддерживает."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя приподняла бровь."
    cs_mz "Какие ещё запросы?"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Неважно. Профессиональная привычка."
    cs_narrator "Дарья тихо усмехнулась."
    cs_narrator "Мы потратили некоторое время на просмотр записей."
    cs_narrator "Женя объясняла, как устроен каталог."
    cs_narrator "Я сверяла названия."
    cs_narrator "Дарья выписывала на листок те издания, которые теоретически могли оказаться полезными."
    cs_narrator "В итоге у нас получилось несколько названий."
    cs_narrator "Но ничего, что прямо отвечало бы на наши вопросы."
    cs_narrator "Женя посмотрела на лист."
    cs_mz "Эти книги можно поискать на полках. Только часть справочников могла оказаться в других кабинетах."
    cs_narrator "Женя задержала палец на одной из карточек."
    cs_mz "Странная запись. В общую систему её так и не внесли."
    cs_ls "Что там?"
    cs_mz "«Фотоальбом старых смен. Передан в старый корпус.»"
    cs_ls "В старый корпус?"
    $ cs_day03_hint_album_seen = True
    cs_mz "Его давно закрыли. Туда не ходят. Альбом, наверное, так там и остался."
    cs_narrator "Я кивнула."
    cs_ls "Значит, пока без результатов."
    cs_mz "Пока без карты. А не без результатов."
    cs_narrator "Я повернулась к ней."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она поправила очки."
    cs_mz "Теперь хотя бы понятно, где искать дальше и чего в этом каталоге точно нет."
    cs_narrator "Я улыбнулась."
    cs_ls "Справедливо. Поправку принимаю."
    cs_narrator "Дарья кивнула."
    cs_da "И мы хотя бы перестанем искать план лагеря среди художественной литературы."
    cs_narrator "Я задумалась."
    cs_ls "Хотя было бы забавно обнаружить его между приключенческими романами."
    cs_narrator "Женя посмотрела на меня."
    cs_mz "Ты ещё предложи искать секретный проход за шкафом."
    cs_narrator "Я медленно повернулась к ней."
    cs_th "О."
    cs_th "А вот это уже неожиданный уровень участия в разговоре."
    cs_ls "Женя, не подсказывай. Я ведь могу воспринять это как приглашение."
    cs_narrator "Она усмехнулась."
    cs_mz "Именно поэтому сразу говорю: никаких шкафов двигать не будем."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я кивнула."
    cs_ls "Принято. Исследовательская деятельность ограничена бумажными носителями."
    cs_narrator "Женя закрыла один из ящичков."
    cs_mz "И правильно."
    $ cs_mz_catalog_checked_day3 = True
    $ cs_day03_library_visit_time = "after_lunch" if cs_mz_book_requested_day3 else None
    label cs_check_day03_113_catalog_done:
    cs_narrator "Мы аккуратно вернули карточки на места."
    cs_narrator "Я посмотрела на часы."
    cs_ls "Спасибо, что помогла."
    cs_narrator "Женя кивнула."
    cs_mz "Если найду что-нибудь ещё, скажу."
    cs_ls "Хорошо. Только не трать на это весь день."
    cs_narrator "Она чуть улыбнулась."
    cs_mz "Соколова, я и без тебя умею распоряжаться своим временем."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Всё. Не вмешиваюсь."
    if cs_mz_book_requested_day3:
        cs_narrator "Женя остановила меня у выхода."
        cs_mz "И про книгу я помню."
        cs_narrator "Я улыбнулась."
        cs_ls "Правда?"
        cs_mz "Да. Приходи после обеда. Я выберу пару вариантов."
        cs_ls "Договорились."
    else:
        cs_narrator "Женя вернулась к своему столу."
        cs_mz "Если захочешь ещё почитать, заходи."
        cs_narrator "Я кивнула."
        cs_ls "Обязательно."
    cs_narrator "Мы попрощались."
    $ cs_actor_exit(["cs_zhenya"])
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    label cs_check_day03_113_library_left:
    cs_narrator "Вышли на улицу."
    cs_th "Ну что ж."
    cs_th "Ответа на главный вопрос снова нет."
    cs_th "Зато теперь я хотя бы знаю, как устроен местный библиотечный каталог."
    cs_th "Не самый впечатляющий результат экспедиции."
    cs_th "Но значительно приятнее, чем очередная встреча локтя с землёй."
    return
