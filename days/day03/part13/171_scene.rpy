# -*- coding: utf-8 -*-
label cs_day03_171:
    $ save_name = "Чужая смена — День 3: Ещё пять минут, товарищ библиотекарь"
    $ cs_director_scene("cs_library_interior_night")
    scene cs_library_interior_night
    $ cs_frame_focus([])
    with Dissolve(0.7)
    $ night_time()
    $ persistent.sprite_time = "night"
    stop music fadeout 3.0
    cs_narrator "Я перевернула страницу."
    cs_narrator "Потом ещё одну."
    cs_narrator "Пока я читала, на улице окончательно стемнело."
    cs_narrator "За окнами уже не было привычных солнечных бликов, а дорожку освещал только фонарь неподалёку от входа."
    cs_narrator "В библиотеке горела лампа."
    cs_narrator "Не особенно яркая, но вполне достаточная, чтобы разобрать строчки."
    cs_th "Ну вот."
    cs_th "За чтением прошло больше времени, чем я собиралась здесь провести."
    cs_th "Пара страниц, одна глава — а потом ещё одна."
    cs_th "Очень хороший план."
    cs_th "Не учла только одну незначительную подробность: книга оказалась интересной."
    cs_narrator "Я поправила закладку, которая уже почти не требовалась."
    cs_narrator "Незаметно я добралась до последних страниц."
    cs_th "Так."
    cs_th "Ещё несколько страниц."
    cs_th "А потом можно будет наконец сформулировать собственное мнение об этом несчастном Александре."
    cs_narrator "Со стороны рабочего стола раздался тихий стук."
    if cs_mz_evening_help_completed_day3 and not cs_da_waiting_outside_library_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
    else:
        $ cs_frame_focus(["cs_zhenya"])
        with cs_sprite_change
    cs_narrator "Женя закрыла журнал."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Лена."
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "М?"
    cs_narrator "Она показала на часы."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Я скоро закрываю."
    cs_narrator "Я посмотрела на время."
    cs_narrator "Потом в окно."
    cs_th "О."
    cs_th "А день-то действительно закончился."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ничего себе."
    cs_narrator "Женя приподняла бровь."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Только заметила?"
    cs_narrator "Я слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Вообще, по моим расчётам, на улице ещё должно быть часов шесть вечера."
    cs_narrator "Она посмотрела на тёмное окно."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Расчёты явно неправильные."
    cs_narrator "Я вздохнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "К сожалению, у меня нет оснований оспаривать данные наблюдения."
    cs_narrator "Женя усмехнулась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом посмотрела на книгу."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Много осталось?"
    cs_narrator "Я перевернула несколько страниц."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Совсем немного. Эпилог заканчиваю."
    if cs_friend_mz >= 3 and cs_mz_open_library_invitation_day3:
        cs_narrator "Женя посмотрела на часы ещё раз."
        cs_narrator "Потом на стол."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Ладно. Дочитывай."
        cs_narrator "Я удивилась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Серьёзно?"
        cs_narrator "Она кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Мне ещё несколько вещей убрать. Только не начинай новую книгу."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Даже не собиралась."
        cs_narrator "Она посмотрела на меня поверх очков."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "И это именно те слова, которым я должна поверить?"
        cs_narrator "Я задумалась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Возможно, стоило сформулировать убедительнее."
        cs_narrator "Женя покачала головой."
        cs_narrator "Но улыбалась."
    elif cs_mz_evening_help_completed_day3:
        cs_narrator "Женя немного подумала."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Хорошо, последние страницы дочитай. Только потом сразу уходим."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Конечно."
        cs_narrator "Она посмотрела на проверенные нами карточки."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Вы сегодня помогли, так что несколько минут я переживу."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Весьма щедрая система поощрения сотрудников."
        cs_narrator "Женя усмехнулась."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Не привыкай."
    else:
        cs_narrator "Женя посмотрела на книгу."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Если осталось несколько страниц, заканчивай. Но не засиживайся. Мне ещё библиотеку закрывать."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Поняла. Не задержу."
    if cs_mz_evening_help_completed_day3:
        cs_narrator "Дарья, сидевшая неподалёку, закончила листать небольшую книжку о музыке."
        cs_narrator "Посмотрела на нас."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "А я, наверное, выйду ненадолго на воздух."
        cs_narrator "Я повернулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Устала?"
        cs_narrator "Она кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Немного. И после целого дня в помещениях хочется посидеть снаружи."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Хорошо. Тут совсем чуть-чуть осталось."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Не спеши. Я на скамейке у входа."
        cs_narrator "Женя посмотрела на часы."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_mz "Только действительно недолго."
        cs_narrator "Я кивнула."
        $ cs_actor_exit(["cs_darya"])
        with cs_sprite_leave
        $ cs_da_waiting_outside_library_day3 = True
        $ cs_day03_darya_destination = "library_entrance"
        cs_narrator "Дарья улыбнулась нам обеим и вышла."
    else:
        cs_narrator "Я вспомнила, что Даша после ужина собиралась ненадолго зайти к Мику."
        cs_th "Надеюсь, она уже закончила."
        cs_th "Хотя если Мику снова увлеклась разговором, даже мне будет сложно определить, кто из нас задержался дольше."
        cs_narrator "Я едва заметно улыбнулась."
    cs_narrator "Женя вернулась к рабочему столу."
    cs_narrator "Я снова посмотрела на книгу."
    cs_th "Ладно."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Последние страницы."
    cs_th "Без отвлечений."
    return
