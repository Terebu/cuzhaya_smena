# -*- coding: utf-8 -*-
label cs_day03_75:
    $ save_name = "Чужая смена — День 3: Утро без согласования"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_day03_dawn
    with Dissolve(0.8)
    $ cs_frame_focus([])
    play ambience "sound/ambiences/int_cabin_day.ogg" fadein 2.0
    $ renpy.music.set_volume(0.16, channel="ambience")
    play music "sound/music/my_daily_life.ogg" fadein 3.0
    $ renpy.music.set_volume(0.2, channel="music")
    label cs_check_day03_75:
    cs_narrator "Проснулась я раньше горна."
    cs_narrator "Опять."
    cs_narrator "Судя по всему, за два дня организм решил, что вставать по утрам в советском пионерском лагере — вполне приемлемая альтернатива нормальной человеческой жизни."
    cs_narrator "Я открыла глаза."
    cs_narrator "Несколько секунд смотрела в потолок."
    cs_narrator "Потом повернула голову к окну."
    cs_narrator "За стеклом едва светлело."
    cs_narrator "Деревья стояли неподвижно."
    cs_narrator "Где-то неуверенно запела птица."
    cs_th "Ну здравствуй, третий день."
    cs_th "Посмотрим, чем ты собираешься меня удивлять."
    cs_narrator "Я осторожно села."
    cs_narrator "И практически сразу почувствовала неприятное натяжение кожи возле локтя."
    cs_th "Ах да."
    cs_th "Моё вчерашнее выдающееся достижение."
    cs_narrator "Посмотрела на повязку."
    cs_narrator "Она оставалась на месте."
    cs_narrator "Никаких заметных новых следов крови не было."
    cs_narrator "Но рука ещё побаливала, особенно если пытаться полностью согнуть её."
    cs_th "Прекрасно."
    cs_th "Вчера мне объяснили, что человеческое тело не особенно любит знакомиться с асфальтом."
    cs_th "Сегодня проведём повторную проверку, но желательно без практической части."
    cs_narrator "Я осторожно пошевелила пальцами."
    cs_narrator "Потом плечом."
    cs_narrator "Локоть отозвался слабой ноющей болью."
    cs_th "Бегать в обычном темпе сегодня, пожалуй, рановато."
    cs_th "Но прогуляться никто не запрещал."
    cs_narrator "Я посмотрела на соседнюю кровать."
    cs_narrator "Дарья спала."
    cs_narrator "Рыжие волосы немного растрепались по подушке."
    cs_narrator "Одеяло сползло почти до плеча."
    cs_narrator "Она лежала на боку, совершенно не подозревая, что я уже мысленно составляю список мероприятий на третьи сутки нашего пребывания здесь."
    cs_narrator "Я невольно улыбнулась."
    cs_narrator "Вчера она сказала, что, возможно, составит мне компанию на утренней прогулке."
    cs_narrator "Но будить её сейчас не хотелось."
    cs_th "Пусть спит."
    cs_th "Вчера у неё тоже был не самый простой день."
    cs_narrator "Я осторожно встала."
    cs_narrator "Достала спортивную одежду."
    cs_narrator "Футболку."
    cs_narrator "Шорты."
    cs_narrator "Кроссовки."
    cs_narrator "Переоделась, стараясь не задевать повязку."
    cs_narrator "Собрала волосы так, чтобы они не мешали."
    $ cs_director_scene("cs_cg_lena_sport_mirror_bandaged_morning")
    scene cs_cg_lena_sport_mirror_bandaged_morning at cs_day03_dawn
    with Dissolve(0.8)
    label cs_check_day03_mirror:
    cs_narrator "Потом посмотрела на себя."
    cs_th "Неплохо."
    cs_th "Фиолетовые волосы, спортивная форма, забинтованный локоть."
    cs_th "Образ человека, который активно пропагандирует здоровый образ жизни, но пока несколько путается в его практической реализации."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_day03_dawn
    with Dissolve(0.8)
    cs_narrator "Я тихо усмехнулась."
    cs_narrator "Подошла к двери."
    cs_narrator "Остановилась."
    cs_narrator "Ещё раз посмотрела на Дарью."
    cs_ls "Я ненадолго. Скоро вернусь."
    cs_narrator "Она не проснулась."
    cs_narrator "Я и не ожидала ответа."
    cs_th "Хотя записку, наверное, оставить стоит."
    cs_narrator "Вчерашнее исследование дороги убедительно показало, что исчезать без предупреждения — не лучшая идея."
    cs_narrator "Я нашла небольшой листок и карандаш."
    cs_narrator "Здоровой рукой написала:"
    cs_narrator "«Даш, я вышла прогуляться по лагерю. За ворота не хожу, подвиги не совершаю. Скоро вернусь. Лена»."
    cs_narrator "Посмотрела на написанное."
    cs_th "Слово «подвиги», конечно, несколько снижает юридическую силу документа."
    cs_th "Но сойдёт."
    cs_narrator "Оставила записку на тумбочке, где Дарья наверняка её заметит."
    cs_narrator "Потом осторожно открыла дверь."
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day at cs_day03_dawn
    with Dissolve(0.8)
    cs_narrator "И вышла наружу."
    return
