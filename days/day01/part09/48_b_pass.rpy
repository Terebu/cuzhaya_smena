# -*- coding: utf-8 -*-
label cs_day01_48_b:
    $ save_name = "Чужая смена — День 1: Пройти мимо"
    show un normal pioneer at cs_actor_left zorder 10
    # cs_composition: regroup
    show cs_darya amused pioneer normal at cs_darya_normal_right
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    stop music fadeout 2.0
    cs_narrator "Я чуть отступила в сторону."
    cs_ls "Извини, задумалась и не посмотрела под ноги."
    cs_narrator "Девушка покачала головой."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Ничего страшного."
    cs_narrator "Я вежливо улыбнулась."
    cs_ls "Тогда хорошего вечера."
    cs_narrator "Она слегка кивнула."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "И тебе…"
    cs_narrator "Я отошла, пропуская её."
    hide un with Dissolve(0.7)
    # cs_composition: regroup
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    cs_narrator "Девушка направилась дальше, в сторону библиотеки."
    cs_narrator "Дарья пошла рядом со мной."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом она спросила:"
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
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
    cs_da "Забавное совпадение."
    cs_ls "И не говори."
    cs_narrator "Я поправила галстук."
    cs_th "Можно было познакомиться."
    cs_th "Но, пожалуй, сегодня и так достаточно неожиданных встреч."
    cs_th "У нас ещё будет время."
    cs_narrator "Если, конечно, это место вообще позволяет строить планы на будущее."
    hide un with Dissolve(0.7)
    return
