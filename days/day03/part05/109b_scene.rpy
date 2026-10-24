# -*- coding: utf-8 -*-
label cs_day03_109b:
    $ save_name = "Чужая смена — День 3: Иногда достаточно честного ответа"
    cs_narrator "Я посмотрела на список."
    cs_narrator "Потом на Славю."
    cs_ls "Славя, мы бы с удовольствием, но у нас сегодня ещё есть дела."
    cs_narrator "Она кивнула."
    cs_sl "Ничего страшного. Я почти закончила."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Извини."
    cs_sl "Да всё хорошо."
    cs_narrator "Я немного подумала."
    cs_ls "Мы хотя бы документы Ольги Дмитриевны уже доставили. Значит, день нельзя считать полностью бездельным."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_sl "Конечно нельзя."
    cs_narrator "Я посмотрела на коробки."
    cs_ls "И, честно говоря, я бы не хотела снова перегружать руку."
    if renpy.showing("sl"):
        show sl normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она посмотрела на повязку."
    cs_sl "Правильно. Лучше побереги себя."
    cs_narrator "Я кивнула."
    cs_ls "Спасибо. Сегодня это самая популярная рекомендация в лагере."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя улыбнулась."
    cs_narrator "Мы ещё немного поговорили."
    cs_narrator "Потом попрощались."
    return
