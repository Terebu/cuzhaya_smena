# -*- coding: utf-8 -*-
label cs_day03_94b:
    $ save_name = "Чужая смена — День 3: Разговор о книгах"
    label cs_check_day03_94b:
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Она уже собиралась уходить."
    cs_narrator "Похоже, в библиотеке её ждали обычные утренние дела."
    cs_th "Не буду задерживать."
    cs_ls "Тогда до встречи, Женя."
    cs_narrator "Она кивнула."
    cs_mz "До встречи."
    if cs_mz_map_lead:
        cs_narrator "Женя остановилась."
        cs_mz "Кстати, не забудь про каталоги."
        cs_narrator "Я кивнула."
        cs_ls "Помню. Сначала зайду к Виоле, потом в библиотеку."
        cs_narrator "Она посмотрела на мою руку."
        cs_mz "Хорошо. Тогда ближе к концу утра."
        cs_ls "Договорились."
    elif cs_friend_mz >= 1:
        if renpy.showing("cs_zhenya"):
            show cs_zhenya normal pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя слегка улыбнулась."
        cs_mz "Если захочешь ещё что-нибудь почитать, заходи."
        cs_narrator "Я кивнула."
        cs_ls "Спасибо. Возможно, после обеда."
    else:
        cs_narrator "Женя просто кивнула и посмотрела в сторону выхода."
        cs_th "Ничего страшного."
        cs_th "Мы ещё наверняка увидимся."
    cs_narrator "Я вернулась к своему подносу."
    cs_narrator "И спокойно закончила завтрак."
    return
