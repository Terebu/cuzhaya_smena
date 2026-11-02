# -*- coding: utf-8 -*-
label cs_day03_85c:
    $ save_name = "Чужая смена — День 3: Выход к завтраку"
    cs_narrator "Мы закончили собираться. Дарья подошла к двери. Я окинула комнату последним взглядом."
    cs_th "Всё на месте. Никто не пострадал. Утро проходит подозрительно благополучно."
    cs_ls "Ну что, на завтрак?"
    cs_narrator "Дарья улыбнулась."
    cs_da "Пойдём."
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.8)
    cs_narrator "Я открыла дверь. И мы вышли наружу."
    return
