# -*- coding: utf-8 -*-
label cs_day03_115b:
    $ save_name = "Чужая смена — День 3: Хорошая музыка не требует комментариев"
    cs_narrator "Я улыбнулась."
    cs_ls "Давай я просто послушаю. Боюсь, с музыкальной теорией у меня отношения не настолько близкие, чтобы уверенно выбирать варианты."
    cs_narrator "Мику покачала головой."
    cs_mi "Да ничего страшного! Можно ведь просто сказать, какой больше нравится."
    cs_narrator "Я кивнула."
    cs_ls "Тогда слушаю."
    label cs_check_day03_115_both:
    cs_narrator "Она сыграла оба вступления."
    cs_narrator "Я внимательно прислушалась."
    cs_narrator "Первое прозвучало мягче."
    cs_narrator "Второе — энергичнее."
    cs_narrator "Разница ощущалась даже без специальных знаний."
    cs_narrator "Но я не стала изображать эксперта."
    cs_ls "Оба по-своему хороши."
    if renpy.showing("mi"):
        show mi smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику улыбнулась."
    cs_mi "Спасибо!"
    cs_narrator "Алиса посмотрела на неё."
    cs_dv "Всё, теперь выбирай сама."
    if renpy.showing("mi"):
        show mi laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику рассмеялась."
    cs_mi "Ладно, ладно."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Мне понравилось первое."
    cs_narrator "Мику заинтересованно повернулась к ней."
    cs_narrator "Они ещё немного обсудили звучание."
    cs_narrator "Я просто слушала."
    cs_th "И, пожалуй, это тоже было приятно."
    cs_th "Необязательно участвовать во всём, что происходит вокруг."
    cs_th "Иногда можно просто быть зрителем."
    return
