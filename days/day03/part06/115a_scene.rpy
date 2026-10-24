# -*- coding: utf-8 -*-
label cs_day03_115a:
    $ save_name = "Чужая смена — День 3: Звучание имеет значение"
    cs_narrator "Я подошла чуть ближе."
    cs_ls "Давай. Мне интересно."
    if renpy.showing("mi"):
        show mi happy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику обрадовалась."
    cs_mi "Правда? Отлично!"
    cs_narrator "Она быстро перелистнула страницу."
    cs_mi "Тогда сначала послушайте вот это."
    label cs_check_day03_115_first:
    cs_narrator "Она сыграла короткое вступление."
    cs_narrator "Несколько плавных нот."
    cs_narrator "Потом немного более быстрый переход."
    cs_narrator "И завершила маленькой паузой."
    cs_mi "Это первый вариант."
    cs_narrator "Я кивнула."
    cs_ls "Понятно."
    cs_mi "А теперь второй."
    label cs_check_day03_115_second:
    cs_narrator "Она сыграла почти ту же последовательность."
    cs_narrator "Но на этот раз мелодия начиналась более резко."
    cs_narrator "Первые ноты звучали ярче."
    cs_narrator "А переход получился короче."
    cs_narrator "Мику подняла взгляд."
    cs_mi "Ну как?"
    cs_narrator "Я задумалась."
    cs_th "Забавно."
    cs_th "Я ведь не музыкант."
    cs_th "Но ощущение действительно разное."
    cs_ls "Мне первый понравился больше."
    cs_narrator "Мику заинтересовалась."
    cs_mi "Почему?"
    cs_narrator "Я немного помолчала, подбирая слова."
    cs_ls "Второй быстрее привлекает внимание. Но первый будто оставляет место для ожидания."
    cs_narrator "Она посмотрела на меня."
    cs_mi "Для ожидания?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Словно сначала видишь только часть рисунка, а потом постепенно понимаешь, что на нём изображено."
    if renpy.showing("mi"):
        show mi normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику задумалась."
    if renpy.showing("mi"):
        show mi happy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом улыбнулась."
    cs_mi "Интересное сравнение!"
    if renpy.showing("dv"):
        show dv grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса усмехнулась."
    cs_dv "Ну, по крайней мере, понятнее, чем «сделаем чуть красивее»."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Как художник хочу отметить, что фраза «сделаем чуть красивее» иногда заменяет трёхчасовое техническое задание."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Мику тоже."
    cs_mi "Тогда первый вариант тебе нравится из-за более плавного начала?"
    cs_ls "Да. Но это просто моё впечатление."
    cs_narrator "Мику кивнула."
    cs_mi "Оно полезное. Я ведь иногда так долго работаю над одной мелодией, что перестаю слышать её как человек, который включил музыку впервые."
    cs_narrator "Я улыбнулась."
    cs_ls "Очень знакомая проблема. Когда долго рисуешь, глаз тоже привыкает ко всем ошибкам."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Поэтому ты иногда переворачиваешь рисунок?"
    cs_narrator "Я удивлённо подняла бровь."
    cs_ls "Ты запомнила?"
    if renpy.showing("mi"):
        show mi happy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_da "Ты рассказывала."
    cs_narrator "Я кивнула."
    cs_ls "Вот. У каждого искусства свои способы обмануть собственное восприятие."
    cs_narrator "Мику задумчиво посмотрела на ноты."
    cs_narrator "Потом снова сыграла первый вариант."
    cs_narrator "Тише."
    cs_narrator "Чуть медленнее."
    cs_mi "Да. Кажется, понимаю."
    cs_narrator "Она улыбнулась мне."
    cs_mi "Спасибо, Лена."
    cs_narrator "Я покачала головой."
    cs_ls "Не за что. В конце концов, от меня потребовалось только послушать музыку и высказать мнение."
    cs_mi "Это иногда самое полезное!"
    cs_narrator "Она посмотрела на Дарью."
    cs_mi "А ты что думаешь?"
    cs_narrator "Дарья немного помолчала."
    cs_narrator "Потом снова коснулась клавиш и осторожно повторила начало первого варианта."
    cs_da "Мне тоже кажется, что так мелодия звучит спокойнее."
    if renpy.showing("mi"):
        show mi smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику улыбнулась."
    cs_mi "Тогда, пожалуй, попробую развить именно его!"
    cs_narrator "Алиса взяла гитару."
    cs_dv "Только давай без ещё десяти вступлений."
    if renpy.showing("mi"):
        show mi laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику рассмеялась."
    cs_mi "Постараюсь!"
    cs_th "Надо же."
    cs_th "Вчера я рисовала объявление для концерта."
    cs_th "А сегодня уже обсуждаю музыкальное вступление."
    cs_th "Если так пойдёт дальше, к концу смены меня примут в кружок за выдающиеся способности сидеть рядом и выражать заинтересованность."
    return
