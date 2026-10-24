# -*- coding: utf-8 -*-
label cs_day03_94:
    $ save_name = "Чужая смена — День 3: Развилка — литературный интерес"
    cs_narrator "К тому времени большая часть пионеров уже собиралась расходиться."
    cs_narrator "Кто-то относил подносы."
    cs_narrator "Кто-то торопился по своим делам."
    if not cs_day03_mz_breakfast_together:
        cs_narrator "Закончив есть, Женя прошла мимо нашего стола с книгой в руках."
        cs_narrator "Я обернулась к ней, не вставая."
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    label cs_check_day03_94_contact:
    cs_narrator "Женя тоже закончила завтрак."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Поправила очки."
    cs_narrator "Взяла книгу."
    cs_narrator "Я посмотрела на неё."
    if cs_lena_book_returned and cs_friend_mz >= 1:
        cs_th "Вчера она сама предложила мне ещё что-нибудь почитать."
    else:
        cs_th "После нашего вчерашнего разговора мне стало любопытно, какие книги она любит."
    cs_th "И теперь мне действительно стало интересно, что она выберет."
    cs_narrator "Но у Жени наверняка были свои дела."
    cs_narrator "Можно было просто попрощаться."
    cs_narrator "А можно спросить о книгах."
    cs_narrator "Только без долгих вступлений и шуточных намёков."
    cs_narrator "Нормально."
    cs_narrator "По-человечески."
    call cs_day03_zhenya_book_choice from cs_return_cefe88a3545f45e37129
    return
