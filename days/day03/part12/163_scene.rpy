# -*- coding: utf-8 -*-
label cs_day03_163:
    $ save_name = "Чужая смена — День 3: Пять минут, которые ничего не обещают"
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("bg int_dining_hall_sunset")
    scene bg int_dining_hall_sunset
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with Dissolve(0.7)
    play music cs_day_music_home fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.08,channel="music")
    cs_narrator "Я закончила ужин и отставила тарелку. Я посмотрела на Женю."
    cs_ls "Женя."
    cs_narrator "Она подняла голову."
    cs_mz "Что?"
    cs_ls "Я на несколько минут до домика."
    cs_narrator "Она кивнула."
    cs_mz "Хорошо."
    cs_ls "Заберу книгу и вернусь. Ты ведь ещё собиралась в библиотеку?"
    cs_narrator "Женя посмотрела на часы."
    cs_mz "Да. Мне нужно закончить кое-какие дела. Но долго сидеть сегодня не буду."
    cs_ls "Поняла. Тогда хотя бы немного почитаю, если успею."
    cs_narrator "Она посмотрела на меня."
    if cs_mz_open_library_invitation_day3:
        if cs_mz_quiet_reading_place_day3:
            cs_mz "Можешь занимать свой стол, когда придёшь."
        else:
            cs_mz "Можешь занимать свободный стол, когда придёшь."
        cs_narrator "Я улыбнулась."
        cs_ls "Даже не нужно подавать заявление?"
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Только если тебе самой очень хочется заниматься бумажной работой."
        cs_ls "Нет. Сегодня мой лимит административных подвигов уже исчерпан."
        cs_narrator "Она покачала головой. Но улыбалась."
    elif cs_friend_mz >= 1:
        cs_mz "Приходи. Если освободится стол у окна, садись там."
        cs_ls "Хорошо. Спасибо."
    else:
        cs_mz "Если библиотека ещё будет открыта, сможешь немного почитать."
        cs_ls "Конечно."
    cs_narrator "Я уже собиралась отнести поднос, но задержалась."
    cs_ls "Только место специально не занимай. Если кто-нибудь сядет раньше, я это переживу."
    cs_narrator "Женя посмотрела на меня."
    cs_mz "Соколова."
    cs_narrator "Я подняла бровь."
    cs_ls "Да?"
    cs_narrator "Она едва заметно улыбнулась."
    cs_mz "Иди уже."
    cs_narrator "Я торжественно кивнула."
    cs_ls "Есть."
    cs_narrator "Даша наблюдала за нами. Потом улыбнулась."
    cs_da "Только не задерживайся по дороге."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даша, от столовой до нашего домика вполне определённое расстояние."
    cs_narrator "Она прищурилась."
    cs_da "Я не про расстояние."
    cs_narrator "Я задумалась."
    cs_th "А. Понятно."
    cs_ls "Прошу не ставить под сомнение мою способность выполнить простейшее поручение."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша рассмеялась."
    cs_da "Ладно. Тогда увидимся позже."
    if cs_mz_evening_help_day3:
        cs_narrator "Даша повернулась к Жене."
        cs_da "Я могу пока пойти с тобой и посмотреть, что нужно подготовить?"
        cs_narrator "Женя кивнула."
        if cs_mz_evening_help_completed_day3:
            cs_mz "Можешь. Мы уже всё сверили, теперь я только закончу записи."
        else:
            cs_mz "Можешь. Только начнём, когда Лена вернётся. Она же тоже собиралась помогать."
        cs_ls "Разумеется. Библиотечная служба не останется без одного из своих лучших сотрудников."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя посмотрела на меня поверх очков."
        cs_mz "Ты ещё ни минуты там не проработала."
        cs_ls "Тогда одного из самых перспективных."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя вздохнула."
        cs_mz "Иди за книгой."
    else:
        cs_narrator "Даша посмотрела в сторону музыкального клуба."
        cs_da "А я тогда ненадолго загляну к Мику. Хотела уточнить кое-что насчёт завтрашнего дня."
        cs_ls "Хорошо. Тогда встретимся у домика, если освободишься раньше меня."
        cs_narrator "Она улыбнулась."
        cs_da "Договорились."
    if cs_mz_evening_help_day3:
        $ cs_day03_darya_destination = "library"
    else:
        $ cs_day03_darya_destination = "music_club"
    cs_narrator "Я попрощалась с ними. Отнесла поднос."
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "И вышла на улицу. Воздух оказался прохладнее, чем днём. Солнце уже опустилось достаточно низко, чтобы дорожки начали покрываться длинными тенями. Я глубоко вдохнула."
    cs_th "Ну что ж. Обычное дело. Нужно дойти до домика. Забрать книгу."
    cs_th "Вернуться. Три действия. Даже я должна справиться без дополнительных сюжетных линий."
    cs_narrator "Я поправила галстук. И направилась к площади."
    $ cs_day03_dinner_finished = True
    return
