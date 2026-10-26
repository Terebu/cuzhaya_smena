# -*- coding: utf-8 -*-
label cs_day03_168:
    $ save_name = "Чужая смена — День 3: Библиотека не является филиалом площади"
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "Я подошла к библиотеке."
    cs_narrator "Остановилась у двери."
    cs_narrator "Посмотрела на книгу."
    cs_narrator "Потом на табличку."
    cs_th "Так."
    cs_th "Площадь осталась позади."
    cs_th "Семён цел."
    cs_th "Славя тоже."
    cs_th "Общественный порядок, насколько мне известно, не нарушен."
    cs_th "Теперь можно заняться действительно важными вещами."
    cs_narrator "Я осторожно открыла дверь."
    $ cs_director_scene("cs_library_interior_evening")
    scene cs_library_interior_evening
    $ cs_frame_focus([])
    with Dissolve(0.7)
    if cs_mz_evening_help_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_narrator "Внутри было тихо."
    cs_narrator "Женя сидела за своим столом."
    cs_narrator "Перед ней лежали несколько книг и журнал выдачи."
    cs_narrator "Она подняла голову."
    cs_narrator "Увидела меня."
    cs_narrator "Потом книгу."
    cs_mz "Вернулась?"
    cs_narrator "Я кивнула."
    cs_ls "Как обещала."
    cs_narrator "Она посмотрела на часы."
    cs_mz "Даже довольно быстро."
    cs_narrator "Я задумалась."
    cs_ls "На обратном пути уже не задерживалась."
    cs_narrator "Женя приподняла бровь."
    cs_mz "А на пути туда?"
    cs_narrator "Я замолчала."
    cs_th "Так."
    cs_th "Вот теперь действительно опасный вопрос."
    cs_ls "Там произошла небольшая остановка."
    cs_narrator "Она посмотрела внимательнее."
    cs_mz "Какая?"
    cs_narrator "Я вздохнула."
    cs_ls "Семён."
    cs_narrator "Женя несколько секунд смотрела на меня."
    cs_narrator "Потом кивнула."
    cs_mz "Понятно."
    cs_narrator "Я удивлённо подняла бровь."
    cs_ls "И всё?"
    cs_narrator "Она вернулась к журналу."
    cs_mz "А что ещё нужно знать?"
    cs_narrator "Я задумалась."
    cs_narrator "Потом улыбнулась."
    cs_ls "Вообще-то ничего. Ты удивительно быстро разобралась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    if cs_mz_dinner_friend_on_arrival >= 1:
        cs_mz "Учитывая твои сегодняшние разговоры, это несложно."
    else:
        cs_mz "После твоего объяснения догадаться несложно."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Справедливо."
    if cs_mz_evening_help_day3:
        cs_narrator "Дарья сидела за соседним столом."
        cs_narrator "Перед ней лежали несколько библиотечных карточек."
        cs_narrator "Увидев меня, она подняла голову."
        cs_da "Нашла?"
        cs_narrator "Я показала книгу."
        cs_ls "Разумеется."
        cs_narrator "Она посмотрела на меня."
        cs_da "И Семёна тоже?"
        cs_narrator "Я остановилась."
        cs_narrator "Потом медленно повернулась к ней."
        cs_ls "Даша."
        cs_narrator "Она невинно улыбнулась."
        cs_da "Что?"
        cs_ls "У меня такое чувство, что вы с Женей уже обсудили моё отсутствие."
        cs_narrator "Женя, не поднимая головы, ответила:"
        cs_mz "Мы пока не успели. Но теперь можно."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
        cs_narrator "Я закрыла глаза."
        cs_th "Всё."
        cs_th "Библиотечная коалиция окончательно сформирована."
        cs_ls "Прекрасно. Теперь меня будут обсуждать даже в моё отсутствие."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        if cs_mz_evening_help_completed_day3:
            cs_mz "Работу мы уже закончили. Если хочешь, можешь спокойно почитать."
        else:
            cs_mz "Если не хочешь, можешь сразу приступить к работе."
        cs_narrator "Я кивнула."
        cs_ls "Разумное предложение."
    else:
        cs_narrator "Я огляделась."
        cs_narrator "Кроме Жени, в библиотеке почти никого не было."
        cs_narrator "На одном столе лежала стопка возвращённых книг."
        cs_narrator "Возле окна свободно стояли несколько стульев."
        if cs_mz_open_library_invitation_day3:
            cs_narrator "Женя кивнула в сторону дальнего стола."
            cs_mz "Можешь садиться. Там свободно."
            cs_narrator "Я улыбнулась."
            cs_ls "Спасибо."
        else:
            cs_narrator "Я посмотрела на свободные места."
            cs_ls "Можно немного почитать у окна?"
            cs_narrator "Женя кивнула."
            cs_mz "Да. Только ненадолго, скоро закрываю."
            cs_narrator "Я улыбнулась."
            cs_ls "Конечно."
    cs_narrator "Я подошла к столу."
    cs_narrator "Положила книгу."
    cs_narrator "И на секунду остановилась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Вот и хорошо."
    cs_th "Можно больше никуда не спешить."
    return
