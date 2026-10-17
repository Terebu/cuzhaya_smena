# -*- coding: utf-8 -*-
label cs_day02_68b:
    $ save_name = "Чужая смена — День 2: Честный финал"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_68b:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя ненадолго задумалась."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А мне показалось, что автор слишком мягко обошёлся с главным героем."
    cs_narrator "Я подняла взгляд."
    cs_ls "В каком смысле?"
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Он ведь долго ничего не предпринимал. А потом всё равно получил возможность исправить ситуацию."
    cs_narrator "Я кивнула."
    cs_ls "Согласна. Но, по-моему, финал как раз показывает, что исправить всё полностью уже нельзя."
    cs_narrator "Женя посмотрела на меня внимательнее."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "То есть ты считаешь, что это не счастливый конец?"
    cs_narrator "Я немного подумала."
    cs_ls "Скорее конец, в котором люди наконец начали отвечать за собственные решения."
    cs_narrator "Она улыбнулась."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Интересная мысль."
    cs_narrator "Затем открыла журнал выдачи."
    cs_narrator "Отметила возвращение книги."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Если будешь ещё что-нибудь брать, скажи. Могу посоветовать несколько похожих произведений."
    cs_narrator "Я улыбнулась."
    cs_ls "С удовольствием."
    cs_th "Надо же."
    cs_th "Первый настоящий разговор о литературе."
    cs_th "И, кажется, мы даже не пытались друг друга переубедить."
    $ cs_reading_book_borrowed = False
    $ cs_lena_book_returned = True
    $ cs_reading_book_location = "library_shelf"
    label cs_check_finale_returned_b:
    return
