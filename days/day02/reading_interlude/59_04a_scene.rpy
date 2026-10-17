# -*- coding: utf-8 -*-
label cs_day02_reading_04a:
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
    label cs_check_reading_04a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя посмотрела на часы."
    cs_narrator "Затем на книгу."
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
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только предупреждаю: если собираешься читать здесь, не нужно снова разговаривать на всю библиотеку."
    cs_narrator "Я подняла глаза."
    cs_ls "Не собираюсь."
    cs_narrator "Она немного помолчала."
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
    cs_mz "И книги с полок лучше брать аккуратно."
    cs_ls "Конечно."
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
    cs_mz "Ладно."
    # cs_presence_keep: hide cs_zhenya
    $ cs_reading_cast = []
    cs_narrator "Она направилась к своему столу."
    # cs_director_begin: Zhenya returns to desk; Lena reads
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_059ae39e0c:
    # cs_director_end
    cs_narrator "Я проводила её взглядом."
    cs_th "Вот и всё."
    cs_th "Никакого конфликта."
    cs_th "Человек обозначил правила."
    cs_th "Я согласилась."
    cs_th "Оказывается, это довольно простая система."
    cs_narrator "Я вернулась к книге."
    label cs_check_reading_desk_04a:
    pause 0.5
    return
