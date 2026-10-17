# -*- coding: utf-8 -*-
label cs_day02_19b:
    $ save_name = "Чужая смена — День 2: До следующего раза"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_s19b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mi", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела в сторону окна."
    cs_narrator "Потом на Мику."
    cs_ls "Слушай, нам, наверное, уже пора к площади. Не хочется опоздать на линейку."
    cs_narrator "Мику подняла взгляд на часы."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_miku_19b:
    cs_mi "Ой, точно! Я совсем про время забыла."
    cs_narrator "Дарья улыбнулась."
    cs_da "Спасибо, что показала кружок. Мне понравилось."
    cs_narrator "Мику оживилась."
    cs_mi "Приходите ещё! В следующий раз можно будет нормально посидеть и послушать что-нибудь."
    cs_ls "Обязательно заглянем, если получится."
    cs_mi "Хорошо!"
    cs_narrator "Она аккуратно собрала ноты."
    cs_narrator "Я посмотрела на пианино."
    cs_narrator "Затем на Дарью."
    cs_ls "А тебе отдельное спасибо за выступление."
    cs_narrator "Дарья усмехнулась."
    cs_da "Оно едва на выступление потянуло."
    cs_ls "Тогда за неожиданную демонстрацию скрытых талантов."
    cs_da "Так уже лучше."
    cs_narrator "Мику рассмеялась."
    cs_narrator "Мы попрощались и направились к двери."
    return
