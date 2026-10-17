# -*- coding: utf-8 -*-
label cs_day02_reading_07a:
    $ save_name = "Чужая смена — Тишина на троих: О книге — если есть доверие"
    $ cs_part08_live = False
    $ cs_reading_live = True
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
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_07a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя ещё немного посмотрела на меня."
    cs_narrator "Затем на книгу."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ладно. Если собираешься читать дальше, только не загибай страницы."
    cs_narrator "Я кивнула."
    cs_ls "Не буду."
    cs_mz "И не оставляй её где попало."
    cs_ls "Конечно."
    cs_narrator "Она поправила очки."
    cs_mz "Хорошо."
    # cs_presence_keep: hide cs_zhenya
    $ cs_reading_cast = ["cs_darya"]
    cs_narrator "И вернулась к своему столу."
    # cs_director_begin: Zhenya finishes conversation and resumes work
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_8d8b719ab8:
    # cs_director_end
    cs_narrator "Я некоторое время смотрела ей вслед."
    cs_th "Никакой особенной теплоты."
    cs_th "Но и прежнего раздражения уже не было."
    cs_th "Во всяком случае, сейчас."
    cs_narrator "Я открыла книгу."
    cs_narrator "И продолжила читать."
    label cs_check_reading_desk_07a:
    pause 0.5
    return
