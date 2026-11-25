# -*- coding: utf-8 -*-

label cs_epilogue_02:
    $ cs_d7_ambience(cs_lena_apartment_ambience, 0.13)
    window hide dissolve
    $ cs_d7_scene("cs_bg_epi_darya_room")
    scene cs_bg_epi_darya_room with dissolve
    pause 0.45
    $ cs_d7_hide_portraits()
    show cs_cg_epi_darya_wake with dissolve
    pause 2.0
    jump cs_epilogue_03
