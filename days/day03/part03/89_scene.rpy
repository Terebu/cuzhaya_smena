# -*- coding: utf-8 -*-
label cs_day03_89:
    $ save_name = "Чужая смена — День 3: Режим повышенной культурности"
    label cs_check_day03_89:
    $ cs_frame_focus(["cs_darya"])
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    $ renpy.music.set_volume(0.17, channel="ambience")
    if cs_day03_at_dining_door:
        cs_narrator "У самого входа в столовую мне в голову пришла совершенно замечательная мысль."
    else:
        cs_narrator "До столовой оставалось каких-то тридцать метров, когда мне в голову пришла совершенно замечательная мысль."
    cs_narrator "Я остановилась."
    cs_narrator "Дарья прошла ещё пару шагов, заметила моё отсутствие и обернулась."
    cs_da "Что случилось?"
    cs_narrator "Я поправила галстук."
    cs_narrator "Разгладила юбку."
    cs_narrator "Выпрямилась."
    cs_narrator "И придала лицу максимально серьёзное выражение."
    cs_ls "Всё."
    if renpy.showing("cs_darya"):
        show cs_darya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья приподняла бровь."
    cs_da "Что «всё»?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Режим серьёзной советской женщины активирован."
    cs_narrator "Она несколько секунд молчала."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом медленно улыбнулась."
    cs_da "Мне уже интересно."
    cs_narrator "Я кивнула."
    cs_ls "Минимум лишних слов. Никаких сомнительных шуток. Исключительно культурное общение."
    cs_narrator "Дарья задумалась."
    cs_da "И надолго?"
    cs_ls "Пока нахожусь рядом с Женей."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_da "А почему нельзя просто нормально с ней разговаривать, не объявляя об этом?"
    cs_narrator "Я посмотрела на неё."
    cs_th "Хороший вопрос."
    cs_th "Даже слишком хороший."
    cs_ls "Потому что реформы требуют официального объявления."
    cs_da "Ага. То есть сарказм всё-таки разрешён?"
    cs_narrator "Я на секунду задумалась."
    cs_ls "Только в служебных целях."
    cs_narrator "Дарья покачала головой."
    cs_da "Удивительная у тебя система."
    cs_narrator "Я кивнула."
    cs_ls "Спасибо. Разрабатывала лично."
    cs_narrator "Она улыбнулась."
    cs_narrator "Мы продолжили путь."
    $ cs_reflective_focus()
    with cs_sprite_leave
    label cs_check_day03_89_reflection:
    cs_th "Если серьёзно, дело было вовсе не в каком-то особенном режиме."
    cs_narrator "Я просто вспомнила вчерашний вечер."
    cs_narrator "Библиотеку."
    if cs_lena_book_returned:
        cs_narrator "Наш разговор о книге."
    else:
        cs_narrator "Наши вчерашние спокойные разговоры."
    cs_narrator "То, как Женя постепенно перестала ждать от меня очередного подвоха."
    cs_narrator "И поняла, что совершенно не хочу возвращаться к прежней привычке постоянно её поддевать."
    cs_narrator "Семён, например, сам охотно участвовал в словесных перепалках."
    cs_narrator "Славя уже научилась отвечать так, что мне порой оставалось только признать поражение."
    cs_narrator "А Женя предпочитала другое общение."
    cs_narrator "И, что особенно приятно, оно тоже оказалось мне по душе."
    cs_th "В конце концов, не обязательно проводить каждый разговор так, будто участвуешь в соревновании по остроумию."
    cs_th "Хотя некоторые люди в этом лагере явно обладают выдающимися способностями."
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    label cs_check_day03_89_dialogue:
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она заметила мой взгляд."
    cs_da "Что?"
    cs_narrator "Я улыбнулась."
    cs_ls "Ничего. Просто подумала, что ты за два дня слишком хорошо научилась отвечать мне моими же шутками."
    cs_da "Хороший учитель попался."
    cs_narrator "Я вздохнула."
    cs_ls "Вот об этом и говорю."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    return
