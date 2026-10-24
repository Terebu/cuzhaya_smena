# -*- coding: utf-8 -*-
label cs_day03_118:
    $ save_name = "Чужая смена — День 3: Две Лены и один карандаш"
    $ cs_frame_focus(["mi", "dv", "cs_darya"])
    with cs_sprite_change
    cs_narrator "Когда мы уже собирались уходить, Мику снова помахала нам рукой."
    cs_mi "Спасибо, что заглянули! Приходите ещё!"
    cs_narrator "Я улыбнулась."
    cs_ls "Обязательно."
    cs_narrator "Дарья кивнула."
    cs_da "До встречи."
    cs_narrator "Алиса подняла руку, не отрываясь от гитары."
    cs_dv "Бывайте."
    if cs_day03_poster_location == "music_club_chair":
        cs_narrator "Дарья забрала со стула папку с плакатом и прижала её к боку."
        $ cs_day03_poster_location = "darya_folder"
    $ cs_actor_exit(["mi","dv"])
    $ cs_director_scene("bg ext_musclub_day")
    scene bg ext_musclub_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    play music "sound/music/my_daily_life.ogg" fadein 2.0
    $ renpy.music.set_volume(0.15,delay=1.0,channel="music")
    label cs_check_day03_118_music_left:
    cs_narrator "Мы вышли из клуба."
    cs_narrator "На улице было заметно жарче, чем утром."
    cs_narrator "Я остановилась в тени."
    cs_narrator "Поправила галстук."
    cs_narrator "И почти сразу заметила знакомую фигуру на скамейке неподалёку."
    cs_narrator "Тёмные волосы."
    cs_narrator "Пионерская форма."
    cs_narrator "Альбом на коленях."
    cs_th "О."
    cs_th "Ещё одна художница."
    cs_ls "Даш, смотри."
    cs_narrator "Она проследила за моим взглядом."
    if cs_un_name_known:
        cs_da "Лена?"
    else:
        cs_da "Та девушка тоже рисует?"
    cs_narrator "Я кивнула."
    if cs_un_name_known:
        cs_ls "Именно. Та, которую не нужно отличать от меня исключительно по фамилии, пока мы не оказались в одной комнате."
    else:
        cs_ls "Да. Давай подойдём и познакомимся."
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Хочешь подойти?"
    cs_narrator "Я немного подумала."
    cs_ls "Да."
    cs_narrator "Мы направились к скамейке."
    $ cs_frame_focus(["cs_darya", "un"])
    with cs_sprite_change
    if renpy.showing("un"):
        show un normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    label cs_check_day03_118_un:
    cs_narrator "Лена Тихонова сидела, чуть наклонившись над альбомом."
    cs_narrator "Она что-то рисовала."
    cs_narrator "Настолько увлечённо, что заметила нас только после моего осторожного приветствия."
    if cs_un_name_known:
        cs_ls "Привет, тёзка."
    else:
        cs_ls "Привет. Я Лена Соколова, а это Даша."
        cs_un "Лена. Тихонова."
        $ cs_un_name_known = True
        $ cs_met_un = True
    cs_narrator "Тихонова подняла голову."
    cs_un "Привет."
    cs_narrator "Посмотрела на Дарью."
    cs_un "И тебе привет."
    cs_da "Привет."
    cs_narrator "Я кивнула на альбом."
    cs_ls "Рисуешь?"
    cs_narrator "Тихонова немного смутилась."
    cs_un "Да."
    cs_ls "Можно посмотреть?"
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом на альбом."
    cs_narrator "Несколько секунд сомневалась."
    if cs_friend_un >= 2:
        cs_narrator "Тихонова немного улыбнулась."
        cs_un "Можно. Только я ещё не закончила."
        cs_narrator "Я кивнула."
        cs_ls "Ничего. Незаконченные работы иногда даже интереснее."
        cs_narrator "Она развернула альбом чуть в мою сторону."
    elif cs_friend_un == 1:
        cs_narrator "Тихонова поколебалась."
        cs_narrator "Потом слегка повернула альбом."
        cs_un "Только не смейся."
        cs_narrator "Я покачала головой."
        cs_ls "Не собираюсь."
    else:
        cs_narrator "Тихонова прижала альбом к себе."
        cs_un "Там ничего особенного."
        cs_narrator "Я остановилась."
        cs_ls "Хорошо. Не буду настаивать."
        cs_narrator "Она посмотрела на меня."
        cs_narrator "Кажется, немного удивилась."
        cs_narrator "Я улыбнулась."
        cs_ls "Просто сама рисую, вот и заинтересовалась."
        cs_narrator "Тихонова немного помолчала."
        cs_narrator "Затем осторожно повернула к нам верхний лист."
        cs_un "Только этот можно."
        cs_ls "Конечно."
    if cs_un_concert_sketch_seen:
        cs_narrator "Вчера Лена показала мне лишь быстрый набросок музыкантов. Теперь вокруг них появились сцена, скамейки и зрители."
    cs_narrator "На рисунке была вчерашняя концертная площадка."
    cs_narrator "Несколько скамеек."
    cs_narrator "Фигуры пионеров."
    cs_narrator "Сцена."
    cs_narrator "Две девушки с музыкальными инструментами."
    cs_narrator "Штрихи ещё не везде были завершены, но композицию уже можно было рассмотреть."
    cs_narrator "Я невольно улыбнулась."
    cs_th "Надо же."
    if cs_un_concert_sketch_seen:
        cs_th "Вчерашний быстрый набросок превращался в целую сцену."
    else:
        cs_th "Она тоже решила сохранить вчерашний вечер."
    cs_th "Только по-своему."
    cs_ls "Красиво."
    if renpy.showing("un"):
        show un shy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Тихонова смутилась."
    cs_un "Да там ещё много чего не готово."
    cs_narrator "Я кивнула."
    cs_ls "Вижу. Но мне нравится, как ты расположила сцену и зрителей."
    if renpy.showing("un"):
        show un normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_un "Правда?"
    cs_ls "Да. Глаз сразу понимает, куда смотреть."
    cs_narrator "Дарья тоже заглянула в альбом."
    cs_da "И вчерашний вечер узнаётся."
    cs_narrator "Тихонова немного улыбнулась."
    cs_un "Я хотела нарисовать Мику и Алису, но потом подумала, что без людей вокруг получится не то."
    cs_narrator "Я кивнула."
    cs_ls "Согласна. Концерт — это ведь не только те, кто выступает."
    cs_narrator "Она посмотрела на рисунок."
    cs_un "Вот именно."
    cs_narrator "Я улыбнулась."
    cs_th "Кажется, мы нашли тему для разговора."
    cs_th "Причём без необходимости объяснять, почему я знаю о существовании графических планшетов."
    return
