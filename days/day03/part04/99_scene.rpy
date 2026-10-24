# -*- coding: utf-8 -*-
label cs_day03_99:
    $ save_name = "Чужая смена — День 3: Медицинское заключение"
    if renpy.showing("cs"):
        show cs custom serious medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    label cs_check_day03_99_examination:
    cs_narrator "Виола сняла старый бинт."
    cs_narrator "Внимательно осмотрела ссадину."
    cs_narrator "Проверила кожу вокруг."
    cs_narrator "Я старалась сидеть спокойно."
    cs_narrator "Хотя, когда она коснулась особенно чувствительного места, всё-таки немного поморщилась."
    cs_vi "Больно?"
    cs_narrator "Я покачала головой."
    cs_ls "Терпимо. Просто неприятно."
    cs_narrator "Она кивнула."
    cs_vi "Выглядит лучше, чем вчера. Но до полного заживления ещё далеко."
    cs_narrator "Я посмотрела на локоть."
    cs_ls "Значит, возвращение в большой спорт откладывается?"
    if renpy.showing("cs"):
        show cs custom warm_smile medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола улыбнулась."
    cs_vi "Именно."
    cs_ls "Какая трагедия. А ведь я уже готовила речь для церемонии награждения."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Виола взяла чистые материалы."
    cs_narrator "Начала обработку."
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "Потом она неожиданно спросила:"
    cs_vi "Кстати, это ты возле столовой очередь ко мне распределяла?"
    cs_narrator "Я замерла."
    cs_th "Ага."
    cs_th "Новостное агентство «Совёнок» работает без выходных."
    cs_ls "А что именно?"
    if renpy.showing("cs"):
        show cs custom amused medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола усмехнулась."
    cs_vi "Что-то про очередь ко мне."
    cs_narrator "Дарья немедленно отвернулась."
    cs_narrator "Плечи у неё подозрительно задрожали."
    cs_narrator "Я посмотрела на неё."
    cs_th "Предательница."
    cs_ls "Ничего серьёзного. Просто обсуждали с Семёном порядок посещения медицинских учреждений."
    cs_narrator "Виола подняла бровь."
    cs_vi "Вот как?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Я даже сообщила ему, что сегодня пришла первой."
    cs_narrator "Она улыбнулась."
    cs_vi "А он собирался?"
    cs_narrator "Я задумалась."
    cs_ls "Утверждает, что нет."
    cs_vi "Тогда непонятно, зачем вы делили очередь."
    cs_narrator "Я вздохнула."
    cs_ls "Виола, не требуйте от моих шуток такого высокого уровня логической обоснованности."
    cs_narrator "Она рассмеялась."
    cs_narrator "Дарья тоже."
    cs_vi "Хорошо. Но если у вас появятся новые споры, медпункт в качестве арбитража не предлагать."
    cs_narrator "Я кивнула."
    cs_ls "Принято. Досудебное урегулирование."
    cs_narrator "Виола покачала головой."
    cs_narrator "Но улыбалась."
    cs_narrator "Она закончила обработку."
    $ cs_day03_viola_check_done = True
    $ cs_lena_elbow_bandaged = True
    label cs_check_day03_99_dressed:
    cs_narrator "Наложила новую повязку."
    cs_narrator "Проверила, удобно ли она сидит."
    cs_vi "Ну вот. Готово."
    cs_narrator "Я осторожно посмотрела на локоть."
    cs_ls "Аккуратно получилось."
    cs_vi "Постарайся сохранить в таком виде хотя бы до вечера."
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Сделаю всё возможное."
    cs_narrator "Она посмотрела на меня."
    cs_vi "И без новых падений."
    cs_ls "Это уже сложнее. Деревья пока не подтвердили готовность к прекращению боевых действий."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    if renpy.showing("cs"):
        show cs custom amused medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола усмехнулась."
    cs_vi "Тогда хотя бы смотри под ноги."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    cs_th "Ну вот."
    cs_th "Плановый осмотр после вчерашних приключений."
    cs_th "И впервые я ухожу не потому, что больше нечего перевязывать, а потому, что всё в порядке."
    cs_th "Пожалуй, прогресс."
    return
