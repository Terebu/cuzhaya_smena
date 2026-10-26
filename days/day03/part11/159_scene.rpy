# -*- coding: utf-8 -*-
label cs_day03_159:
    $ save_name = "Чужая смена — День 3: Развилка — помочь или оставить в покое"
    cs_narrator "Женя закончила есть."
    cs_narrator "Осторожно отодвинула тарелку."
    cs_narrator "Посмотрела на часы."
    cs_narrator "Потом на книгу, которую положила рядом с собой."
    cs_narrator "Я заметила это."
    cs_ls "Ты куда-то спешишь?"
    cs_narrator "Она покачала головой."
    cs_mz "Не особенно. Просто нужно ещё ненадолго заглянуть в библиотеку."
    cs_narrator "Я заинтересовалась."
    cs_ls "По делу?"
    cs_narrator "Женя посмотрела на меня поверх очков."
    cs_mz "Нет, Соколова. Исключительно ради того, чтобы убедиться, что книги за моё отсутствие не разбежались."
    cs_narrator "Я замолчала."
    cs_narrator "Потом медленно улыбнулась."
    cs_ls "Слушай, а ты сегодня опасная."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Нужно проверить несколько возвратов и подготовить книги к завтрашней выдаче."
    cs_narrator "Я кивнула."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Понятно."
    cs_th "Обычные библиотечные дела."
    cs_th "Ничего особенно сложного."
    cs_th "И, кажется, у меня есть возможность немного помочь."
    cs_narrator "Но я также помнила, что Женя не особенно любит, когда кто-нибудь без спроса вмешивается в её работу."
    cs_th "Так."
    cs_th "Можно предложить помощь."
    cs_th "А можно просто пожелать хорошего вечера."
    cs_th "И оба варианта, вообще-то, нормальные."
    return
