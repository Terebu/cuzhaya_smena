# -*- coding: utf-8 -*-
label cs_day01_55_b:
    $ save_name = "Чужая смена — День 1: Не мешать"
    show cs_zhenya normal pioneer normal at cs_darya_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на стопку книг."
    cs_narrator "Потом на Женю, которая уже принялась разбирать их."
    cs_th "Пожалуй, не стоит мешать."
    cs_narrator "Я повернулась к Дарье."
    cs_ls "Давай просто посмотрим полки."
    cs_narrator "Она кивнула."
    cs_narrator "Мы прошли к ближайшему стеллажу."
    cs_narrator "Через несколько секунд Женя подняла голову."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вы нашли то, что искали?"
    cs_ls "Пока нет."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Газеты на дальней полке. А каталожные карточки здесь, возле стола."
    cs_narrator "Я посмотрела туда, куда она указала."
    cs_ls "Спасибо."
    cs_narrator "Женя кивнула."
    cs_narrator "И снова занялась книгами."
    cs_narrator "Дарья подошла ко мне."
    cs_da "Кажется, она не очень разговорчивая."
    cs_ls "Или просто занята."
    cs_da "Тоже возможно."
    cs_narrator "Я взяла с полки книгу."
    cs_narrator "Посмотрела на обложку."
    cs_th "Не каждое знакомство обязательно должно начинаться с долгого разговора."
    cs_th "Особенно когда человек работает."
    cs_narrator "Мы продолжили осматривать полки."
    return
