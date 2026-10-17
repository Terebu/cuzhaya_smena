# -*- coding: utf-8 -*-
label cs_day01_48_b:
    $ save_name = "Чужая смена — День 1: Пройти мимо"
    show un normal pioneer at cs_actor_left zorder 10
    # cs_composition: regroup
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    stop music fadeout 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["un", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я чуть отступила в сторону."
    cs_ls "Извини, задумалась и не посмотрела под ноги."
    cs_narrator "Девушка покачала головой."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Ничего страшного."
    cs_narrator "Я вежливо улыбнулась."
    cs_ls "Тогда хорошего вечера."
    cs_narrator "Она слегка кивнула."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "И тебе…"
    cs_narrator "Я отошла, пропуская её."
    # cs_presence_keep: hide un
    # cs_composition: regroup
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Девушка направилась дальше, в сторону библиотеки."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["un"])
    with cs_sprite_leave
    label cs_director_check_ef7eca6473:
    # cs_director_end
    cs_narrator "Дарья пошла рядом со мной."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом она спросила:"
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты её узнала?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_da "Тоже из той игры?"
    cs_ls "Угу."
    cs_da "И кто она?"
    cs_narrator "Я проводила девушку взглядом."
    cs_ls "Лена. Представляешь?"
    cs_narrator "Дарья удивилась."
    cs_narrator "Потом посмотрела на мои волосы."
    cs_narrator "На удалявшуюся девушку."
    cs_narrator "И улыбнулась."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Забавное совпадение."
    cs_ls "И не говори."
    # cs_director_begin: Independent reflection after declining the acquaintance
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_e99f943927:
    # cs_director_end
    cs_narrator "Я поправила галстук."
    cs_th "Можно было познакомиться."
    cs_th "Но, пожалуй, сегодня и так достаточно неожиданных встреч."
    cs_th "У нас ещё будет время."
    cs_narrator "Если, конечно, это место вообще позволяет строить планы на будущее."
    # cs_presence_keep: hide un
    return
