# -*- coding: utf-8 -*-
label cs_day03_161a:
    $ save_name = "Чужая смена — День 3: Пятнадцать минут библиотечной службы"
    if cs_mz_evening_help_completed_day3:
        return
    $ cs_day03_darya_destination = "library"
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with Dissolve(0.7)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5
    cs_narrator "После ужина мы направились к библиотеке."
    cs_narrator "Женя шла немного впереди."
    cs_narrator "Дарья рядом со мной."
    cs_narrator "Я осторожно поправила повязку."
    cs_th "Ну что ж."
    if cs_helped_viola_day3 and cs_helped_sl_day3:
        cs_th "Сегодня мне довелось поработать в медпункте, помочь с лагерными делами и теперь ещё попробовать себя в библиотечном хозяйстве."
    else:
        cs_th "Сегодня лагерных дел и без того хватило. А теперь ещё попробую себя в библиотечном хозяйстве."
    cs_th "Если завтра предложат вести кружок юных авиамоделистов, пожалуй, придётся официально потребовать выходной."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Женя открыла дверь."
    $ cs_director_scene("cs_library_interior_evening")
    scene cs_library_interior_evening
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with Dissolve(0.7)
    stop ambience fadeout 1.5
    cs_narrator "Пропустила нас внутрь."
    cs_narrator "Затем положила книгу на стол."
    cs_mz "Так. Сначала вот эти карточки."
    cs_narrator "Я подошла ближе."
    cs_narrator "Она показала несколько записей в журнале."
    cs_mz "Нужно сверить номера с возвращёнными книгами. Только не переставляйте ничего на полках без меня."
    cs_narrator "Я кивнула."
    cs_ls "Есть."
    cs_narrator "Дарья взяла карандаш."
    cs_da "Я могу отмечать номера."
    cs_narrator "Женя кивнула."
    cs_mz "Хорошо."
    cs_narrator "Мы принялись за работу."
    cs_narrator "Я проверяла номера на обложках и форзацах, Дарья сверяла их со списком."
    cs_narrator "Женя периодически проверяла наши записи и раскладывала книги по нужным местам."
    cs_narrator "Работа оказалась довольно простой."
    cs_narrator "Но требовала внимательности."
    cs_th "Вот."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Наконец-то задача, в которой всё зависит от того, насколько хорошо умеешь читать цифры."
    cs_th "Никаких загадок."
    cs_th "Никаких подозрительных дорог."
    cs_th "Никаких деревьев, которые неожиданно появляются на пути."
    cs_narrator "Женя посмотрела на нас."
    $ cs_pov_end()
    with cs_sprite_change
    cs_mz "Всё сходится?"
    cs_narrator "Дарья кивнула."
    cs_da "Почти. Вот здесь один номер отличается."
    cs_narrator "Женя подошла."
    cs_narrator "Посмотрела на запись."
    cs_narrator "Затем на книгу."
    cs_mz "Ага. Это я в журнале цифры местами поменяла."
    cs_narrator "Я приподняла бровь."
    cs_ls "Надо же. Оказывается, библиотечная система тоже допускает человеческий фактор."
    cs_narrator "Женя посмотрела на меня."
    cs_mz "Соколова, если сейчас начнёшь делать из этого событие государственного масштаба…"
    cs_narrator "Я сразу подняла здоровую руку."
    cs_ls "Ни слова."
    cs_narrator "Пауза."
    cs_ls "Просто запомним исторический момент."
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Женя покачала головой."
    cs_narrator "Но тоже улыбнулась."
    cs_narrator "Через некоторое время всё было готово."
    cs_narrator "Женя закрыла журнал."
    cs_mz "Спасибо. Быстрее закончила, чем рассчитывала."
    cs_narrator "Я улыбнулась."
    cs_ls "Не за что."
    cs_narrator "Дарья кивнула."
    cs_da "Рады помочь."
    if cs_mz_dinner_friend_on_arrival >= 3:
        cs_narrator "Женя немного помолчала."
        cs_narrator "Затем посмотрела на меня."
        cs_mz "Слушай, Лена."
        cs_narrator "Я подняла голову."
        cs_ls "Да?"
        cs_narrator "Она поправила очки."
        cs_mz "Спасибо, что не стала сегодня устраивать из этого представление."
        cs_narrator "Я немного удивилась."
        cs_narrator "Потом улыбнулась."
        cs_ls "Вообще-то очень хотелось."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Я заметила."
        cs_narrator "Я кивнула."
        cs_ls "Но решила, что тебе полезнее помощь, чем очередная торжественная речь."
        cs_narrator "Она чуть улыбнулась."
        cs_mz "Правильно решила."
        cs_narrator "Немного помолчала."
        if cs_mz_quiet_reading_place_day3:
            cs_mz "И если завтра снова придёшь почитать, можешь не ждать, пока я освобожусь. Просто занимай своё место."
        else:
            cs_mz "Если завтра придёшь читать, выбирай свободный стол. Пока я занята журналом, можешь спокойно начинать."
        cs_narrator "Я улыбнулась."
        cs_ls "Хорошо."
        cs_th "Вот и всё."
        cs_th "Никаких громких признаний."
        cs_th "Просто ещё немного доверия."
    else:
        cs_narrator "Женя посмотрела на нас."
        cs_mz "Спасибо. С задачей справились."
        cs_narrator "Я кивнула."
        cs_ls "Рада помочь."
        cs_narrator "Она улыбнулась."
        cs_mz "Если завтра придёшь читать, увидимся."
        cs_ls "Обязательно."
    cs_narrator "Мы попрощались."
    cs_narrator "Женя осталась закрывать библиотеку."
    $ cs_mz_evening_help_completed_day3 = True
    label cs_check_day03_161_help_completed:
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadein 1.5
    cs_narrator "Мы с Дарьей вышли наружу."
    return
