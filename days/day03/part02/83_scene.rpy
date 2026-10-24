# -*- coding: utf-8 -*-
label cs_day03_83:
    $ save_name = "Чужая смена — День 3: Не самое удачное возвращение"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    with Dissolve(0.8)
    $ cs_frame_focus([])
    play music "sound/music/my_daily_life.ogg" fadein 2.0
    $ renpy.music.set_volume(0.2,channel="music")
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    $ renpy.music.set_volume(0.17,channel="ambience")
    label cs_check_day03_83:
    cs_narrator "До домика я добралась уже после утреннего горна."
    cs_narrator "Не бегом."
    cs_narrator "Не вприпрыжку."
    cs_narrator "И даже без попытки устроить соревнование с собственным временем."
    cs_th "Посмотрите-ка."
    cs_th "Третий день в лагере, а я уже демонстрирую признаки здравого смысла."
    cs_th "Виола была бы довольна."
    cs_narrator "В голове ещё крутились утренние шутки со Славей."
    cs_narrator "Та, оказывается, за два дня освоила искусство отвечать мне с таким невозмутимым видом, что порой я даже не успевала придумать достойную контратаку."
    cs_narrator "Особенно обидно было то, что теперь Славя умела использовать против меня реальные факты."
    cs_th "Некрасиво."
    cs_th "Совершенно нечестная форма ведения дискуссии."
    cs_narrator "Я поднялась на крыльцо."
    cs_narrator "Поправила спортивную футболку."
    cs_narrator "Осторожно взялась за ручку двери."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
    with Dissolve(0.8)
    play ambience "sound/ambiences/int_cabin_day.ogg" fadein 1.0
    label cs_check_day03_83_door:
    cs_narrator "И вошла."
    cs_ls "Я верну…"
    cs_narrator "Остановилась."
    show cs_darya neutral underwear normal at cs_day03_darya_enter
    $ renpy.pause(0.30, hard=True)
    with None
    $ cs_frame_focus(["cs_darya"])
    label cs_check_day03_83_underwear:
    cs_narrator "Дарья стояла возле своей кровати."
    cs_narrator "Пионерская форма лежала рядом: белая рубашка, юбка и галстук."
    cs_narrator "А сама Даша как раз переодевалась после сна."
    cs_narrator "Всё произошло настолько неожиданно, что мой мозг на несколько секунд прекратил выполнять обязанности."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она — на меня."
    cs_th "Так."
    cs_th "Кажется, сейчас мне следовало постучать."
    cs_th "Желательно до открытия двери."
    cs_narrator "Дарья первой нарушила молчание."
    cs_da "Лена?"
    cs_narrator "Я моргнула."
    cs_ls "Ага."
    cs_narrator "Пауза."
    cs_ls "Доброе утро."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Потом на одежду, которую держала в руках."
    cs_da "Доброе."
    cs_narrator "Я медленно подняла здоровую руку."
    cs_ls "Прошу прощения. Кажется, я несколько опередила расписание приёма посетителей."
    show cs_darya hair_touch underwear normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_check_day03_83_hair_touch:
    cs_narrator "Дарья улыбнулась."
    cs_da "Лен, отвернись, пожалуйста."
    $ cs_reflective_focus()
    with cs_sprite_leave
    label cs_check_day03_83_turned_away:
    cs_narrator "Я немедленно повернулась к двери."
    cs_ls "Есть."
    cs_th "Вот так."
    cs_th "Спокойно."
    cs_th "Воспитанный человек должен уважать личное пространство окружающих."
    cs_th "Особенно когда окружающие — красивые рыжеволосые девушки."
    cs_narrator "За спиной зашуршала одежда."
    cs_narrator "Я уставилась на дверную ручку."
    cs_th "Хорошая ручка."
    cs_th "Деревянная дверь."
    cs_th "Удивительно интересная архитектура."
    cs_th "Никогда раньше не замечала, насколько занимательно рассматривать дверные петли."
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Ты чего так замерла?"
    cs_ls "Изучаю местное столярное производство."
    cs_da "Правда?"
    cs_ls "Очень качественная работа. Рекомендую."
    cs_narrator "Она рассмеялась сильнее."
    cs_da "Лена."
    cs_ls "Что?"
    cs_da "Ты смутилась?"
    cs_narrator "Я выпрямилась."
    cs_ls "Нет."
    cs_narrator "Несколько секунд молчания."
    cs_da "Совсем?"
    cs_narrator "Я посмотрела на потолок."
    cs_th "Вот ведь."
    cs_th "Два дня назад я практически в одиночку устраивала дипломатические скандалы в этом лагере."
    cs_th "А теперь меня допрашивают в собственном домике."
    cs_ls "Допускаю незначительное нарушение эмоционального равновесия."
    cs_narrator "Дарья засмеялась."
    cs_da "То есть да."
    cs_narrator "Я вздохнула."
    cs_ls "Немного."
    cs_narrator "Она ничего не ответила."
    cs_narrator "Только продолжила одеваться."
    cs_narrator "Я ещё некоторое время рассматривала дверь."
    cs_narrator "Потом тихо добавила:"
    cs_ls "Кстати, в следующий раз я постучу."
    cs_narrator "Дарья ответила уже серьёзнее."
    cs_da "Спасибо."
    cs_narrator "Я кивнула."
    cs_th "Всё-таки есть вещи, которые лучше не превращать в шутку."
    cs_narrator "За спиной снова зашуршала ткань."
    cs_narrator "Через некоторое время Даша произнесла:"
    cs_da "Всё, можешь поворачиваться."
    cs_narrator "Я обернулась."
    with None
    show cs_darya neutral pioneer normal at cs_day03_darya_enter
    label cs_check_day03_83_enter:
    $ renpy.pause(0.30, hard=True)
    with None
    $ cs_frame_focus(["cs_darya"])
    label cs_check_day03_83_dressed:
    cs_narrator "Она уже была в пионерской форме."
    cs_narrator "Только галстук ещё держала в руках."
    cs_narrator "Я окинула её взглядом."
    cs_narrator "Потом театрально вздохнула."
    cs_ls "Всё. Советская цензура снова одержала победу."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Что?"
    cs_narrator "Я подняла палец."
    cs_ls "Ничего. Просто отмечаю, что утро началось весьма неожиданно."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она усмехнулась."
    cs_da "Ты же сама вошла."
    cs_narrator "Я кивнула."
    cs_ls "Согласна. Происшествие полностью организовано моими силами."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Затем посмотрела на меня внимательнее."
    cs_da "А если серьёзно, ты правда так растерялась?"
    cs_narrator "Я немного помолчала."
    cs_ls "Да."
    show cs_darya neutral pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она слегка удивилась."
    cs_ls "У меня ведь раньше не было отношений. Да и к совместному проживанию с девушкой я как-то не готовилась."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Теперь придётся привыкать."
    cs_narrator "Я посмотрела на неё."
    cs_ls "К совместному проживанию?"
    cs_da "К тому, что мы обе здесь живём. И иногда друг другу мешаем."
    cs_narrator "Я кивнула."
    show cs_darya thinking pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_ls "Тогда предлагаю ввести небольшой свод правил."
    cs_da "Например?"
    cs_ls "Не открывать дверь без предупреждения, когда другой человек переодевается."
    cs_da "Хорошее правило."
    cs_ls "Не занимать чужую кровать без разрешения."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она усмехнулась."
    cs_da "Особенно актуально."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "И не пользоваться чужим смущением в целях получения психологического преимущества."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Потом медленно улыбнулась."
    cs_da "Последнее ты сама не выдержишь."
    cs_narrator "Я замолчала."
    cs_th "Проклятье."
    cs_th "Она права."
    cs_ls "Предлагаю третий пункт считать рекомендательным."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    return
