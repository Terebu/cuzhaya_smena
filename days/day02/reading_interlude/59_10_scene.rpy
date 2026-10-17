# -*- coding: utf-8 -*-
label cs_day02_reading_book_drop:
    $ save_name = "Чужая смена — Книга до вечера"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "По дороге мы ненадолго свернули к нашему домику."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_house_full_frame
    $ cs_reading_cast = []
    with Dissolve(0.8)
    cs_narrator "Я положила библиотечную книгу на тумбочку возле своей кровати, оставив закладку между страницами."
    cs_narrator "До конца оставалось всего несколько страниц. Их можно было дочитать перед возвращением книги."
    $ cs_reading_book_location = "cabin_table"
    label cs_check_reading_book_stored:
    cs_narrator "Пусть ждёт вечера здесь. На ужин и концерт брать её с собой незачем."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Через минуту мы снова шли к столовой."
    return
