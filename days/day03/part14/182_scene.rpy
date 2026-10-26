# -*- coding: utf-8 -*-
label cs_day03_182:
    $ save_name = "Чужая смена — День 3: Развилка — попросить или не торопить"
    cs_th "Вчера она хотела спать отдельно."
    cs_th "Я это помню."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "И сегодняшняя близость ничего не обязывает."
    cs_th "Но спросить честно всё-таки хочется."
    return
