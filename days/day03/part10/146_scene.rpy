# -*- coding: utf-8 -*-
label cs_day03_146:
    $ save_name = "Чужая смена — День 3: Литературное предательство"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    $ cs_day03_darya_destination = "home"
    $ cs_day03_sketchbook_location = "house_table"
    play ambience "sound/ambiences/int_cabin_day.ogg" fadeout 1.5 fadein 1.5
    play music cs_day_music_home fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.08,delay=1.0,channel="music")
    cs_narrator "Когда я вернулась в домик, на улице всё ещё было светло."
    cs_narrator "Воздух заметно остыл по сравнению с полуднем, но в помещении сохранилось дневное тепло."
    cs_narrator "Дарья сидела на своей кровати, поджав под себя одну ногу, и что-то записывала в небольшой тетради."
    cs_narrator "Услышав дверь, она подняла голову."
    cs_da "О, вернулась."
    cs_narrator "Я кивнула."
    cs_ls "Как видишь. Причём без новых повреждений."
    cs_narrator "Она улыбнулась."
    cs_da "Уже достижение."
    cs_narrator "Я остановилась посреди комнаты."
    cs_narrator "Посмотрела на неё."
    cs_ls "Мне начинает казаться, что мою биографию теперь будут делить на два периода: до знакомства с местной медициной и после."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Просто сегодня ты наконец решила слушать Виолу."
    cs_ls "К сожалению, она оказалась слишком убедительной. Даже спорить неинтересно."
    cs_narrator "Я подошла к столу."
    cs_narrator "Там лежала книга, которую мне выдала Женя."
    cs_narrator "Гончаров."
    cs_narrator "Моя новая возможность ненадолго забыть о существовании лагерных проблем."
    cs_narrator "Рядом лежал блокнот с набросками."
    if cs_un_sketch_completed_day3:
        if not cs_reflective_shot:
            $ cs_pov_begin()
            with cs_sprite_leave
        cs_narrator "Я осторожно положила рядом ещё несколько листов."
        cs_narrator "Надо же."
        cs_narrator "Совместное рисование получилось куда приятнее, чем я ожидала."
        cs_narrator "Особенно учитывая, что мы с Тихоновой почти не отвлекались от рисунков на разговоры."
        if cs_un_private_drawing_shown_day3:
            cs_narrator "А ещё она показала мне один из своих личных рисунков."
            cs_narrator "Не ради похвалы."
            cs_narrator "Просто потому, что захотела."
            cs_narrator "И почему-то это оказалось важнее обычного разговора о технике."
            cs_narrator "Я невольно улыбнулась."
    else:
        cs_narrator "Набросок, конечно, ещё требовал доработки."
        cs_narrator "Но на сегодня мне хватило и этого."
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_day03_reading_book_location = "lena"
    cs_narrator "Я взяла роман со стола."
    cs_narrator "Посмотрела на закладку."
    cs_narrator "Потом на Дарью."
    cs_narrator "И неожиданно вспомнила, что у меня впереди ещё немало непрочитанных страниц."
    cs_th "Так."
    cs_narrator "Кажется, на ближайшее время планы определились."
    cs_narrator "Я повернулась к Даше."
    cs_narrator "Выпрямилась."
    cs_narrator "Прижала книгу к груди здоровой рукой."
    cs_narrator "И с совершенно серьёзным выражением произнесла:"
    cs_ls "Извини, женщина."
    cs_narrator "Она подняла бровь."
    cs_da "Что?"
    cs_narrator "Я показала обложку."
    cs_ls "Сегодня в моей жизни появился Гончаров."
    cs_narrator "Дарья несколько секунд смотрела на меня."
    cs_narrator "Потом медленно улыбнулась."
    cs_da "Поздравляю вас обоих."
    cs_narrator "Я кивнула."
    cs_ls "Спасибо. Надеюсь, ты отнесёшься к нашим отношениям с пониманием."
    cs_narrator "Она рассмеялась."
    cs_da "Уже отношения?"
    cs_narrator "Я задумалась."
    cs_ls "Пока на этапе серьёзного знакомства. Но перспективы весьма благоприятные."
    cs_narrator "Дарья отложила тетрадь."
    cs_da "А мне теперь что делать?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Затем на книгу."
    cs_ls "Принять неизбежное."
    cs_narrator "Она прищурилась."
    cs_da "Даже если я начну ревновать?"
    cs_narrator "Я тяжело вздохнула."
    cs_ls "Даша, ты пытаешься конкурировать с русской классикой."
    cs_da "И?"
    cs_ls "Это очень самоуверенно."
    cs_narrator "Она засмеялась."
    cs_narrator "Я тоже не удержалась от улыбки."
    cs_narrator "Затем положила роман на кровать и осторожно присела рядом."
    cs_da "И насколько всё серьёзно?"
    cs_narrator "Я посмотрела на обложку."
    cs_ls "Пока не знаю. Если окажется скучно, вернусь к тебе."
    cs_narrator "Дарья приложила ладонь к груди."
    cs_da "Какая честь."
    cs_narrator "Я кивнула."
    cs_ls "Цени. Не каждому выпадает возможность стать альтернативой Гончарову."
    cs_narrator "Она покачала головой."
    cs_narrator "Но улыбалась."
    cs_narrator "Вот за что я люблю наши разговоры."
    cs_narrator "Не нужно объяснять, что всё это шутка."
    cs_narrator "Даша и сама умеет продолжить её так, что я иногда оказываюсь в проигрыше."
    cs_narrator "Я устроилась поудобнее."
    cs_narrator "Открыла книгу."
    cs_narrator "Нашла закладку."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "И погрузилась в чтение."
    return
