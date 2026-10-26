# -*- coding: utf-8 -*-
label cs_day03_143:
    $ save_name = "Чужая смена — День 3: Культурные ценности под охраной"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "До домика мы добрались без приключений."
    cs_narrator "Уже достижение."
    cs_narrator "Я открыла дверь."
    cs_narrator "Пропустила Дарью вперёд."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    cs_narrator "И вошла следом."
    cs_narrator "Внутри было немного душно."
    cs_narrator "Солнечный свет падал на пол через окно."
    cs_narrator "На моей кровати лежало аккуратно сложенное полотенце."
    cs_narrator "На столе — оставленные утром вещи."
    cs_narrator "Дом милый дом."
    cs_narrator "Ну, почти."
    cs_narrator "Я подошла к столу."
    $ cs_day03_reading_book_location = "house_table"
    cs_narrator "Положила книгу."
    cs_narrator "Осторожно подвинула её подальше от края."
    cs_ls "Всё. Литературное достояние помещено на ответственное хранение."
    cs_narrator "Дарья посмотрела на обложку."
    cs_da "Ты ведь ещё не дочитала?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Продолжу вечером."
    cs_narrator "Она кивнула."
    cs_da "Понравилось?"
    cs_narrator "Я улыбнулась."
    cs_ls "Очень. Особенно нравится, что у героев есть неприятная привычка считать себя правыми."
    cs_narrator "Дарья усмехнулась."
    cs_da "Знакомо."
    cs_narrator "Я медленно повернулась к ней."
    cs_ls "Дарья Еретикова, мне кажется, сейчас прозвучал намёк."
    cs_narrator "Она совершенно невинно улыбнулась."
    cs_da "Правда?"
    cs_narrator "Я задумалась."
    cs_ls "Никак не могу доказать. Но подозрения крайне серьёзные."
    cs_narrator "Она рассмеялась."
    if cs_sl_poster_collected_day3 and cs_day03_poster_location == "darya_folder":
        $ cs_day03_poster_location = "house_table"
        $ cs_day03_poster_stored_home = True
        cs_narrator "Дарья положила на стол папку с нашим концертным плакатом."
        cs_narrator "Осторожно открыла."
        cs_narrator "Проверила рисунок."
        cs_narrator "Потом снова закрыла."
        cs_da "Вот. Теперь точно не потеряем."
        cs_narrator "Я подошла ближе."
        cs_narrator "Посмотрела на папку."
        cs_narrator "Надо же."
        cs_narrator "Вчера ещё готовили этот плакат и спорили о надписях."
        cs_narrator "А сегодня он уже лежит у нас как небольшой сувенир."
        cs_ls "Хорошо бы потом забрать его домой."
        cs_narrator "Дарья посмотрела на меня."
        cs_da "В Москву?"
        cs_narrator "Я кивнула."
        cs_ls "Ага. Представляешь, повесить его где-нибудь рядом с компьютером?"
        cs_narrator "Она улыбнулась."
        cs_da "И что скажешь людям, если спросят, откуда он?"
        cs_narrator "Я задумалась."
        cs_ls "Что провела крайне необычные летние каникулы."
        cs_narrator "Дарья тихо рассмеялась."
        cs_da "Очень уклончивый ответ."
        cs_narrator "Я кивнула."
        cs_ls "Зато почти без неправды."
        cs_narrator "Мы переглянулись."
        cs_narrator "И ненадолго замолчали."
        $ cs_pov_begin()
        with cs_sprite_leave
        cs_th "Если вернёмся."
        cs_th "Нет."
        cs_th "Когда вернёмся."
        cs_th "Я посмотрела на папку ещё раз."
        cs_th "Хочется верить, что однажды мы действительно сможем поставить её у себя дома."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я достала из своих вещей небольшой блокнот."
    cs_narrator "Проверила карандаш."
    cs_narrator "Положила рядом ластик."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Собираешься рисовать?"
    cs_narrator "Я кивнула."
    if cs_un_sketch_time_agreed_day3:
        cs_ls "Да. Если договорённость с Тихоновой ещё в силе."
    else:
        cs_ls "Да. Немного порисую сама."
    if cs_un_sketch_time_agreed_day3:
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Вы же условились ближе к вечеру."
        cs_narrator "Я посмотрела на часы."
        cs_ls "Тогда как раз успею. Только переоденусь во что-нибудь поудобнее."
        cs_narrator "Она кивнула."
        cs_da "А я, наверное, ещё ненадолго схожу к Мику."
        cs_narrator "Я улыбнулась."
        cs_ls "Конечно."
        cs_narrator "Немного подумала."
        cs_ls "Только не соглашайся играть весь вечер, если сама не хочешь."
        cs_narrator "Дарья удивлённо посмотрела на меня."
        cs_da "Это ты сейчас серьёзно?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Ты же говорила, что давно не занималась."
        cs_narrator "Она немного улыбнулась."
        cs_da "Не переживай. Я сама разберусь."
        cs_narrator "Я кивнула."
        cs_ls "Вот и хорошо."
    else:
        cs_narrator "Дарья посмотрела на блокнот."
        cs_da "Ты ведь пока не договорилась с Леной о времени?"
        cs_narrator "Я покачала головой."
        cs_ls "Нет. Просто подумала, что можно немного порисовать самой."
        cs_narrator "Она улыбнулась."
        cs_da "Тогда хорошая идея."
        cs_ls "Спасибо."
    cs_narrator "Я осторожно поправила повязку."
    cs_narrator "Только бы локоть не начал снова напоминать о себе."
    cs_narrator "Впрочем, карандаш я держу другой рукой."
    cs_narrator "Так что на этот раз медицина и искусство вполне способны сосуществовать."
    if cs_un_sketch_time_agreed_day3:
        cs_da "Тогда увидимся перед ужином. Я к Мику, а ты не забудь блокнот."
        cs_narrator "Даша вышла первой. Я немного отдохнула, взяла карандаш и собралась на встречу."
        $ cs_day03_darya_destination = "music_club"
        $ cs_actor_exit(["cs_darya"])
        with cs_sprite_leave
    return
