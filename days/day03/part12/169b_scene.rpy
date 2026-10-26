# -*- coding: utf-8 -*-
label cs_day03_169b:
    $ save_name = "Чужая смена — День 3: Если помощь не была выбрана"
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Я устроилась за свободным столом."
    cs_narrator "Положила книгу перед собой."
    cs_narrator "Женя тем временем продолжала работу."
    cs_narrator "В библиотеке было достаточно тихо, чтобы слышать шелест страниц."
    cs_narrator "Я осторожно открыла роман на закладке."
    cs_narrator "Нашла нужный абзац."
    cs_narrator "И начала читать."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Ну вот."
    cs_th "Вернулась."
    cs_th "Никакой необходимости обсуждать произошедшее с Семёном прямо сейчас."
    cs_th "Никакой необходимости немедленно устраивать разговор."
    cs_th "Просто книга."
    cs_th "Стол."
    cs_th "И тихий вечер."
    cs_narrator "Я постепенно углубилась в текст."
    cs_narrator "В какой-то момент Женя прошла мимо."
    cs_narrator "Посмотрела на обложку."
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_mz "Всё тот же роман?"
    cs_narrator "Я подняла глаза."
    cs_ls "Ага. Решила сегодня ещё немного продвинуться."
    cs_narrator "Она кивнула."
    cs_mz "Только не засиживайся. Я скоро закрываю."
    cs_narrator "Я улыбнулась."
    cs_ls "Конечно."
    cs_narrator "Она направилась к своему столу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я вернулась к книге."
    cs_narrator "Прошло несколько минут."
    cs_th "Интересно."
    if cs_mz_friend_on_arrival_day3 >= 1:
        cs_th "Всё-таки она действительно правильно выбрала произведение."
    else:
        cs_th "Всё-таки я удачно выбрала произведение."
    cs_th "И чем дальше, тем больше мне хочется с ней его обсудить."
    if cs_mz_day3_honest_book_talk:
        cs_th "Особенно после нашего разговора о решениях."
        if cs_mz_friend_on_arrival_day3 >= 1:
            cs_th "Возможно, она уже тогда понимала, что я начну смотреть на эту историю немного иначе."
        else:
            cs_th "После того разговора я сама стала смотреть на эту историю немного иначе."
    cs_narrator "Я перевернула страницу."
    cs_narrator "И незаметно для себя улыбнулась."
    return
