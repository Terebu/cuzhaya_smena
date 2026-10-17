# -*- coding: utf-8 -*-
label cs_day02_68a:
    $ save_name = "Чужая смена — День 2: Честный финал"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_68a:
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_mz "Понятно. Хорошо, что понравилась."
    cs_narrator "Она открыла журнал выдачи."
    cs_narrator "Нашла мою запись."
    cs_narrator "Поставила отметку о возврате."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Всё, книга возвращена."
    cs_narrator "Я кивнула."
    cs_ls "Спасибо."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Не за что."
    cs_narrator "Она ненадолго посмотрела на перевязанный локоть."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только в следующий раз осторожнее с книгами. И с собой тоже."
    cs_narrator "Я усмехнулась."
    cs_ls "Постараюсь."
    cs_th "Спокойный разговор."
    cs_th "Без прежнего раздражения."
    cs_th "И, пожалуй, для нашего знакомства это уже неплохо."
    $ cs_reading_book_borrowed = False
    $ cs_lena_book_returned = True
    $ cs_reading_book_location = "library_shelf"
    label cs_check_finale_returned_a:
    return
