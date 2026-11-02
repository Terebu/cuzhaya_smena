# -*- coding: utf-8 -*-
label cs_day03_135:
    $ save_name = "Чужая смена — День 3: Можно приходить просто так"
    if cs_mz_book_borrowed_day3:
        return
    $ cs_reflective_focus()
    with cs_sprite_leave
    cs_narrator "Прошло ещё некоторое время. Я закончила главу. Положила закладку. Закрыла книгу."
    cs_narrator "Потянулась. И почти сразу пожалела об этом, когда повреждённый локоть неприятно напомнил о себе. Ай. Ладно."
    cs_narrator "Даже чтение требует соблюдения техники безопасности. Я осторожно опустила руку. Посмотрела на часы. Кажется, пора сделать перерыв."
    cs_narrator "Я поднялась. Взяла роман. И подошла к Жене."
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Она что-то записывала. Услышав шаги, подняла голову."
    cs_mz "Уже уходишь?"
    cs_ls "Да. Хочу немного пройтись."
    cs_narrator "Она посмотрела на книгу."
    cs_mz "Не понравилась?"
    cs_narrator "Я покачала головой."
    cs_ls "Наоборот. Можно взять с собой?"
    cs_mz "Конечно. Только я запишу."
    cs_narrator "Я протянула ей том."
    label cs_check_day03_135_loan:
    $ cs_mz_book_borrowed_day3 = True
    $ cs_day03_reading_book_location = "lena"
    cs_narrator "Она внесла запись. Потом вернула книгу."
    cs_mz "Не торопись возвращать. Сначала дочитай."
    cs_narrator "Я улыбнулась."
    cs_ls "Хорошо."
    if cs_mz_friend_on_arrival_day3 >= 3 and cs_mz_quiet_reading_place_day3:
        cs_narrator "Женя немного помолчала. Затем посмотрела на меня."
        cs_mz "Ты завтра придёшь?"
        cs_narrator "Я удивилась."
        cs_ls "Если можно."
        cs_narrator "Она кивнула."
        cs_mz "Можно."
        cs_ls "Тогда приду."
        cs_narrator "Женя снова опустила взгляд к журналу. Но через секунду добавила:"
        cs_mz "И вообще можешь заходить, даже если не собираешься брать книгу."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Просто посидеть?"
        cs_narrator "Она кивнула."
        cs_mz "Да. Иногда мне тоже приятнее, когда рядом кто-то есть."
        cs_narrator "Потом сразу уточнила:"
        cs_mz "Если этот кто-то умеет не разговаривать без остановки."
        cs_narrator "Я невольно улыбнулась."
        cs_ls "Кажется, одного такого человека я знаю."
        cs_narrator "Женя посмотрела поверх очков."
        cs_mz "Посмотрим, надолго ли его хватит."
        cs_narrator "Я тихо рассмеялась. Потом немного помолчала."
        cs_ls "Спасибо, Женя."
        cs_narrator "Она кивнула."
        cs_mz "Не за что."
        $ cs_pov_begin()
        with cs_sprite_leave
        cs_narrator "Просто разрешение приходить даже без повода. И почему-то именно это казалось особенно важным."
        $ cs_mz_open_library_invitation_day3 = True
    elif cs_mz_friend_on_arrival_day3 >= 2:
        cs_narrator "Женя посмотрела на книгу."
        cs_mz "Потом расскажешь, что думаешь о конце."
        cs_ls "Обязательно."
        cs_narrator "Она приподняла бровь."
        cs_mz "Только без пересказа всего романа. Я его уже читала."
        cs_ls "Тогда ограничусь претензиями к автору."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Вот это уже интереснее."
    else:
        cs_narrator "Женя вернулась к журналу."
        cs_mz "Когда дочитаешь, вернёшь."
        cs_ls "Конечно."
        cs_mz "И не испачкай страницы."
        cs_ls "Буду обращаться бережно."
        cs_narrator "Она кивнула."
        cs_mz "Хорошо."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я направилась к выходу. Остановилась возле двери. Обернулась."
    cs_ls "Женя."
    cs_narrator "Она подняла голову."
    cs_mz "Что?"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Хороший выбор."
    cs_narrator "Женя посмотрела на книгу у меня в руках. И ответила чуть мягче, чем обычно:"
    cs_mz "Рада, что понравилась."
    cs_ls "Спасибо за книгу."
    cs_mz "Приходи ещё."
    cs_narrator "Я вышла."
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    $ cs_frame_focus([])
    with Dissolve(0.7)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.5
    cs_narrator "Дверь тихо закрылась за моей спиной."
    return
