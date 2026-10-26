# -*- coding: utf-8 -*-
label cs_day03_174:
    $ save_name = "Чужая смена — День 3: Книга возвращена, разговор остаётся"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Я положила книгу перед Женей."
    cs_narrator "Аккуратно."
    cs_narrator "Не захлопывая и не бросая."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Спасибо."
    cs_narrator "Она посмотрела на роман."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "За книгу?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "И за то, что разрешила закончить."
    cs_narrator "Женя слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Пожалуйста."
    cs_narrator "Она открыла журнал выдачи."
    cs_narrator "Нашла нужную запись."
    $ cs_mz_book_borrowed_day3 = False
    $ cs_day03_reading_book_location = "library"
    label cs_check_day03_174_book_returned:
    cs_narrator "Сделала пометку о возврате."
    cs_th "Вот."
    cs_th "Всё официально."
    cs_th "Книга прочитана."
    cs_th "Экземпляр возвращён."
    cs_th "Культурно-просветительская операция успешно завершена."
    cs_narrator "Я посмотрела на книжные полки."
    cs_narrator "На стол."
    cs_narrator "На знакомое окно."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Странно."
    cs_th "Ещё вчера это место казалось просто библиотекой."
    cs_th "Сегодня — уже чем-то большим."
    cs_narrator "Женя заметила, что я не ухожу."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Что-то ещё?"
    cs_narrator "Я немного помолчала."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да нет."
    cs_narrator "Потом посмотрела в окно."
    cs_narrator "За стеклом был настоящий вечер."
    cs_narrator "Тёмные деревья."
    cs_narrator "Свет фонаря."
    cs_narrator "Тихая дорожка."
    cs_narrator "Я подошла немного ближе."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Красиво."
    cs_narrator "Женя поднялась со стула."
    cs_narrator "Посмотрела туда же."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Ночью здесь спокойно."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Даже непривычно."
    cs_narrator "Она чуть улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Ты же сама любишь тишину."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Люблю. Просто днём лагерь постоянно пытается напомнить, что он существует."
    cs_narrator "Женя усмехнулась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Это называется жизнь."
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Пожалуй. Довольно шумная её разновидность."
    cs_narrator "Она тихо рассмеялась."
    cs_narrator "Некоторое время мы смотрели в окно."
    cs_narrator "За ним никого не было видно."
    cs_narrator "Только фонарь освещал небольшой участок дорожки."
    cs_narrator "Женя вдруг спросила:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Ты темноты не боишься?"
    cs_narrator "Я повернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Нет. А почему спрашиваешь?"
    cs_narrator "Она пожала плечами."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Некоторые пионеры не любят ходить по лагерю после отбоя."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Я скорее боюсь людей, которые внезапно появляются из темноты."
    cs_narrator "Женя усмехнулась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Ульяны, например?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Особенно Ульяны. Её вообще следует снабдить предупреждающим звуковым сигналом."
    cs_narrator "Женя рассмеялась."
    cs_narrator "Я тоже улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "А если серьёзно, сама по себе темнота мне не мешает."
    cs_narrator "Она кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Тогда хорошо. Только по дорожкам ходи, а не через кусты."
    cs_narrator "Я посмотрела на локоть."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "После вчерашнего я решила временно прекратить исследование местной растительности методом личного столкновения."
    cs_narrator "Женя покачала головой."
    cs_narrator "Но улыбалась."
    cs_narrator "Я снова повернулась к окну."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Всё-таки здесь красиво."
    cs_th "Днём лагерь выглядит почти слишком ярким."
    cs_th "Солнце, зелень, пионеры, музыка."
    cs_th "А вечером становится другим."
    cs_th "Более спокойным."
    cs_th "И, пожалуй, немного более настоящим."
    cs_narrator "Женя посмотрела на часы."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Лена, мне всё-таки нужно закрывать."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да. Конечно."
    cs_narrator "Но ещё на секунду задержалась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Не хочется нарушать эту тишину."
    cs_th "Хотя, наверное, в этом и смысл."
    cs_th "Нельзя оставить хороший момент навсегда."
    cs_th "Можно только запомнить его."
    return
