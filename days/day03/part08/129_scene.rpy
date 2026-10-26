# -*- coding: utf-8 -*-
label cs_day03_129:
    $ save_name = "Чужая смена — День 3: Библиотечный режим"
    if cs_mz_friend_on_arrival_day3 is None:
        $ cs_mz_friend_on_arrival_day3 = cs_friend_mz
    $ cs_day03_library_legacy_bridge = cs_day03_reading_book_id == "paustovsky_warm_bread"
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    $ cs_frame_focus(["cs_zhenya"])
    with Dissolve(0.7)
    stop ambience fadeout 1.5
    play music cs_day_music_home fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.08,delay=1.0,channel="music")
    label cs_check_day03_128_library:
    if cs_day03_library_legacy_bridge:
        cs_narrator "Я отложила сборник Паустовского, который только успела полистать. Женя подняла голову от записей."
        cs_mz "Можешь посмотреть ещё один вариант. Роман Гончарова. Только первый сборник оставь здесь."
        jump cs_day03_129_seated
    cs_narrator "В библиотеке было прохладнее, чем на улице."
    cs_narrator "Солнечный свет проходил через окна и ложился длинными полосами на пол."
    cs_narrator "Где-то негромко шелестели страницы."
    cs_narrator "Пахло бумагой и старыми книгами."
    cs_narrator "Я прикрыла дверь."
    cs_narrator "Постаралась сделать это как можно тише."
    cs_narrator "Женя сидела за столом и что-то записывала."
    cs_narrator "Услышав шаги, она подняла голову."
    cs_mz "Пришла?"
    cs_narrator "Я кивнула."
    cs_ls "Как и обещала."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом на часы."
    cs_mz "Даже без опоздания."
    cs_narrator "Я задумалась."
    cs_ls "Теперь мне немного обидно. Кажется, окружающие совершенно не верят в мою пунктуальность."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя поправила очки."
    cs_mz "Я ничего такого не сказала."
    cs_ls "Но интонация была крайне подозрительная."
    cs_narrator "Она едва заметно улыбнулась."
    cs_mz "Соколова, ты пришла читать или анализировать мои интонации?"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Читать."
    cs_mz "Тогда проходи."
    cs_narrator "Я улыбнулась."
    cs_th "Кратко."
    cs_th "Убедительно."
    cs_th "Вполне в её стиле."
    if cs_mz_friend_on_arrival_day3 >= 3 and cs_mz_quiet_reading_place_day3:
        cs_narrator "Я уже направилась к свободному столу, но Женя окликнула меня."
        cs_mz "Лена."
        cs_narrator "Я обернулась."
        cs_ls "Да?"
        cs_narrator "Она указала на дальнее окно."
        cs_mz "Твой стол там."
        cs_narrator "Я остановилась."
        cs_narrator "Посмотрела на неё."
        cs_narrator "Потом в указанную сторону."
        cs_ls "Мой?"
        cs_narrator "Женя вздохнула."
        cs_mz "Не в смысле собственности. Просто там тебе будет удобнее."
        cs_narrator "Я улыбнулась."
        cs_ls "Уже хотела спросить, когда оформлять документы на приватизацию."
        cs_narrator "Она покачала головой."
        cs_mz "Даже не начинай."
        cs_narrator "Я тихо рассмеялась."
        cs_ls "Хорошо."
        cs_narrator "На дальнем столе не было ничего лишнего."
        cs_narrator "Только небольшая стопка книг, аккуратно сложенная у края."
        cs_narrator "Стул стоял так, чтобы свет падал сбоку."
        cs_narrator "И никто из посетителей не проходил постоянно за спиной."
        cs_narrator "Надо же."
        cs_narrator "Она действительно подумала о том, где мне будет удобнее."
        cs_narrator "Я посмотрела на Женю."
        cs_ls "Спасибо."
        cs_narrator "Она лишь кивнула."
        cs_mz "Только не занимай его своими рисунками на весь день."
        cs_narrator "Я улыбнулась."
        cs_ls "Никаких незаконных художественных мастерских."
    elif cs_mz_friend_on_arrival_day3 >= 1:
        cs_narrator "Я огляделась."
        cs_narrator "У окна было несколько свободных столов."
        cs_ls "Можно у дальнего окна?"
        cs_narrator "Женя посмотрела в ту сторону."
        cs_mz "Садись. Там обычно спокойно."
        cs_narrator "Я кивнула."
        cs_ls "Отлично."
        cs_narrator "Она вернулась к записям."
    else:
        cs_narrator "Я выбрала свободный стол у окна."
        cs_narrator "Женя подняла голову."
        cs_mz "Только книги не оставляй где попало."
        cs_narrator "Я улыбнулась."
        cs_ls "Верну на место."
        cs_mz "Вот и хорошо."
    cs_narrator "Я сняла с плеча небольшую сумку, положила её рядом со стулом и осторожно села."
    cs_th "Ну что ж."
    cs_th "Рабочее место организовано."
    cs_th "Осталось главное — книга."
    label cs_day03_129_seated:
    pass
    return
