# -*- coding: utf-8 -*-
label cs_day02_reading_04b:
    $ save_name = "Чужая смена — Тишина на троих: Первая реакция Жени"
    $ cs_part08_live = False
    $ cs_reading_live = True
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_04b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя уже собиралась вернуться за стол, когда снова посмотрела на мою книгу."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Подожди. Это ведь та, что я вчера читала?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_mz "Нашла второй экземпляр?"
    cs_ls "Угу. На полке стояли два."
    cs_narrator "Она немного улыбнулась."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Там интереснее дальше становится."
    cs_narrator "Я посмотрела на страницу."
    cs_ls "Пока тоже неплохо."
    cs_mz "Только не заглядывай в конец."
    cs_narrator "Я подняла взгляд."
    cs_ls "Даже не собиралась."
    cs_mz "Хорошо."
    cs_narrator "Она поправила очки."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда читай."
    # cs_presence_keep: hide cs_zhenya
    $ cs_reading_cast = []
    cs_narrator "И вернулась за стол."
    # cs_director_begin: Zhenya returns to desk; Lena reads
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_f2371b7c05:
    # cs_director_end
    cs_th "Небольшой разговор."
    cs_th "Никаких попыток доказать друг другу собственную правоту."
    cs_th "Пожалуй, именно таким наше знакомство могло бы быть с самого начала."
    label cs_check_reading_desk_04b:
    pause 0.5
    return
