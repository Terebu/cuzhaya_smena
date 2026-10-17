# -*- coding: utf-8 -*-
label cs_day02_51:
    $ save_name = "Чужая смена — День 2: Развилка — ещё несколько минут"
    $ cs_part06_live = False
    $ cs_part07_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_check_part07_s51:
    return
