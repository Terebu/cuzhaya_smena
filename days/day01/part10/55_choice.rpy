# -*- coding: utf-8 -*-
label cs_day01_55:
    $ save_name = "Чужая смена — День 1: Развилка — знакомство с Женей"
    label cs_check_day01_part10_choice_text:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на стопку книг."
    cs_narrator "Затем на Женю."
    cs_narrator "Она уже собиралась приступить к сортировке."
    cs_th "Можно предложить помощь."
    cs_th "А можно не вмешиваться и просто поискать нужные издания."
    label cs_check_day01_part10_choice:
    if cs_part10_choice is None:
        menu:
            "Предложить Жене помощь с книгами":
                $ cs_friend_mz += 1
                $ cs_part10_choice = "help"
            "Не отвлекать Женю от работы":
                $ cs_part10_choice = "search"
    if cs_part10_choice == "help":
        call cs_day01_55_a from cs_return_cdb19a449ee98af5128b
    else:
        call cs_day01_55_b from cs_return_77806b4b6d72f616b051
    return
