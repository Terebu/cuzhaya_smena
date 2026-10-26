# -*- coding: utf-8 -*-
label cs_day03_169a:
    $ save_name = "Чужая смена — День 3: Если выбрана помощь Жене"
    if cs_mz_evening_help_completed_day3:
        return
    $ cs_pov_end()
    with cs_sprite_change
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_narrator "Женя подошла к столу."
    cs_narrator "Положила перед нами небольшой список."
    cs_mz "Тогда давайте закончим, пока не стало совсем поздно."
    cs_narrator "Я кивнула."
    cs_ls "Что делать?"
    cs_narrator "Она указала на несколько карточек."
    cs_mz "Нужно сверить их с журналом. Я потом сама уберу книги на полки."
    cs_narrator "Дарья взяла карандаш."
    cs_da "Я могу отмечать номера."
    cs_narrator "Женя кивнула."
    cs_mz "Хорошо."
    cs_narrator "Я осторожно придвинула одну карточку."
    cs_narrator "Посмотрела на запись."
    cs_ls "Так. Первая совпадает."
    cs_narrator "Дарья поставила отметку."
    cs_narrator "Я взяла следующую."
    cs_th "Вот."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Вполне нормальная работа."
    cs_th "Не нужно никуда бегать."
    cs_th "Не нужно тащить коробки."
    cs_th "Не нужно даже спорить с собственным локтем."
    cs_narrator "Через несколько минут мы обнаружили одну карточку, на которой номер не совпадал с записью."
    cs_narrator "Я показала её Жене."
    $ cs_pov_end()
    with cs_sprite_change
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_ls "Слушай, здесь, кажется, цифры перепутаны."
    cs_narrator "Она подошла ближе."
    cs_narrator "Посмотрела."
    cs_narrator "Потом открыла журнал."
    cs_mz "Ага. Действительно."
    cs_narrator "Дарья посмотрела на неё."
    cs_da "Записать исправление?"
    cs_narrator "Женя кивнула."
    cs_mz "Да. Только сначала я сама сверю с книгой."
    cs_narrator "Она проверила номер."
    cs_narrator "Исправила запись."
    cs_narrator "Потом посмотрела на нас."
    cs_mz "Всё правильно. Спасибо."
    cs_narrator "Я улыбнулась."
    cs_ls "Не за что."
    cs_mz "И, между прочим, хорошо, что заметила."
    cs_narrator "Я задумалась."
    cs_ls "Наконец-то мои способности замечать странные мелочи получили общественное признание."
    cs_narrator "Она посмотрела на меня."
    cs_mz "Только не делай из этого праздник."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Уже отменяю торжественный концерт."
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Женя покачала головой."
    cs_narrator "Но улыбалась."
    cs_narrator "Через некоторое время все записи были проверены."
    cs_narrator "Женя закрыла журнал."
    cs_mz "Готово."
    cs_narrator "Я посмотрела на часы."
    cs_th "И правда не так долго."
    cs_narrator "Женя немного помолчала."
    if cs_mz_dinner_friend_on_arrival >= 3:
        cs_mz "Спасибо. С вами получилось быстрее."
        cs_narrator "Я улыбнулась."
        cs_ls "Значит, временный библиотечный персонал оправдал ожидания?"
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Вполне."
        cs_narrator "Она посмотрела на книгу."
        cs_mz "Если хочешь, можешь ещё немного почитать. Я пока закончу свои записи."
        cs_narrator "Я кивнула."
        cs_ls "С удовольствием."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "А я, наверное, посижу рядом."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Только предупреждаю: сегодня у меня по-прежнему серьёзные отношения с Гончаровым."
        cs_narrator "Она рассмеялась."
        cs_da "Я уже смирилась."
    else:
        cs_mz "Спасибо за помощь. Теперь осталось только закрыть журнал."
        cs_narrator "Я кивнула."
        cs_ls "Не за что."
        cs_narrator "Она посмотрела на книгу в моих руках."
        cs_mz "Можешь прочитать ещё несколько страниц, если хочешь. Но скоро будем уходить."
        cs_narrator "Я улыбнулась."
        cs_ls "Конечно."
    $ cs_mz_evening_help_completed_day3 = True
    label cs_check_day03_169_help_completed:
    cs_narrator "Я вернулась к столу."
    cs_narrator "Открыла роман на закладке."
    cs_narrator "Дарья устроилась неподалёку."
    cs_narrator "Женя продолжила свои записи."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Идеально."
    cs_th "Все чем-то заняты."
    cs_th "И никто не пытается сделать из этого событие государственного масштаба."
    cs_th "Кроме меня."
    cs_th "Но я пока молчу."
    return
