# -*- coding: utf-8 -*-
label cs_day03_168:
    $ save_name = "Чужая смена — День 3: Библиотека не является филиалом площади"
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "Я дошла до библиотеки и остановилась у двери. Я осторожно открыла дверь."
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
    cs_narrator "Внутри было тихо. Женя сидела за своим столом. Перед ней лежали несколько книг и журнал выдачи. Она подняла голову."
    cs_narrator "Увидела меня. Потом книгу."
    cs_mz "Вернулась?"
    cs_ls "Как обещала. Только на площади задержалась из-за Семёна."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    if cs_mz_dinner_friend_on_arrival >= 1:
        cs_mz "Семён, конечно. Теперь понятно."
    else:
        cs_mz "Понятно, Соколова."
    if cs_mz_evening_help_day3:
        cs_narrator "Даша сидела за соседним столом. Перед ней лежали несколько библиотечных карточек. Увидев меня, она подняла голову."
        cs_da "Нашла?"
        cs_narrator "Я показала книгу."
        cs_ls "Разумеется."
        cs_ls "Вы уже обсудили моё отсутствие?"
        cs_narrator "Женя, не поднимая головы, ответила:"
        cs_mz "Мы пока не успели. Но теперь можно."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Даша рассмеялась."
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
        cs_ls "Разумное предложение."
    else:
        cs_narrator "Я огляделась. Кроме Жени, в библиотеке почти никого не было. На одном столе лежала стопка возвращённых книг. Возле окна свободно стояли несколько стульев."
        if cs_mz_open_library_invitation_day3:
            cs_narrator "Женя кивнула в сторону дальнего стола."
            cs_mz "Можешь садиться. Там свободно."
            cs_narrator "Я улыбнулась."
            cs_ls "Спасибо."
        else:
            cs_narrator "Я посмотрела на свободные места."
            cs_ls "Можно немного почитать у окна?"
            cs_narrator "Женя кивнула."
            cs_mz "Да, садись."
            cs_narrator "Я улыбнулась."
            cs_ls "Конечно."
    cs_narrator "Я подошла к столу. Положила книгу. И на секунду остановилась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Вот и хорошо. Можно больше никуда не спешить."
    return
