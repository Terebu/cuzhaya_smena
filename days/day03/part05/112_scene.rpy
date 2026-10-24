# -*- coding: utf-8 -*-
label cs_day03_112:
    $ save_name = "Чужая смена — День 3: Не все дела одинаково важны"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "На развилке мы остановились."
    cs_narrator "Одна дорожка вела к библиотеке."
    cs_narrator "Другая — к музыкальному кружку."
    cs_narrator "Я посмотрела сначала в одну сторону."
    cs_narrator "Потом в другую."
    cs_th "Что ж."
    cs_th "Общественно полезная деятельность завершена."
    cs_th "Теперь можно наконец заняться собственными делами."
    $ cs_reflective_focus()
    with cs_sprite_leave
    label cs_check_day03_112_reflection:
    cs_narrator "Хотя слово «собственными» здесь всё ещё звучало немного странно."
    cs_narrator "В Москве у меня была квартира, компьютер, графический планшет и куча проектов, часть которых я благополучно откладывала до неопределённого будущего."
    cs_narrator "Здесь — домик, несколько комплектов одежды, неработающий телефон и совершенно непонятные перспективы возвращения."
    cs_narrator "Зато уже появились дела, которые хотелось сделать."
    cs_narrator "Не потому, что нужно."
    cs_narrator "А просто потому, что интересно."
    cs_narrator "Я улыбнулась."
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_check_day03_112_dialogue:
    cs_da "О чём задумалась?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "О том, что мы начинаем обзаводиться расписанием."
    cs_narrator "Она приподняла бровь."
    cs_da "В смысле?"
    cs_narrator "Я загнула пальцы здоровой рукой."
    cs_ls "Утром медпункт. Потом вожатая. Потом поручения. Ещё книги, музыка и какие-нибудь лагерные мероприятия."
    cs_narrator "Немного помолчала."
    cs_ls "Я приехала в совершенно непонятное место и за три дня умудрилась организовать себе полноценную занятость."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Тебе ведь нравится."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И кивнула."
    cs_ls "Некоторые части — очень."
    cs_narrator "Она улыбнулась."
    cs_da "Например?"
    cs_narrator "Я задумалась."
    cs_narrator "Потом посмотрела на неё с совершенно серьёзным выражением."
    cs_ls "Компания."
    cs_narrator "Дарья на секунду замолчала."
    cs_narrator "Затем улыбнулась чуть мягче."
    cs_da "Мне тоже."
    cs_narrator "Некоторое время мы просто стояли рядом."
    cs_narrator "Вокруг шумел лагерь."
    cs_narrator "Кто-то пробежал по дорожке."
    cs_narrator "Где-то засмеялись пионеры."
    cs_narrator "Ничего особенного не происходило."
    cs_narrator "И это было приятно."
    return
