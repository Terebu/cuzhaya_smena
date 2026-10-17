# -*- coding: utf-8 -*-
label cs_day02_68:
    $ save_name = "Чужая смена — День 2: Честный финал"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_68:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя как раз закрывала журнал."
    cs_narrator "Когда я подошла, она подняла голову."
    cs_narrator "Посмотрела на книгу."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Всё?"
    cs_narrator "Я кивнула."
    cs_ls "Дочитала."
    cs_narrator "Она протянула руку."
    cs_narrator "Я аккуратно передала ей экземпляр."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И как?"
    cs_narrator "Я немного подумала."
    cs_ls "Хорошая книга."
    cs_narrator "Женя приподняла бровь."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только хорошая?"
    cs_narrator "Я улыбнулась."
    cs_ls "Очень хорошая."
    cs_narrator "Потом немного помолчала."
    cs_ls "Вторая половина понравилась больше первой. Сначала история будто слишком осторожно двигалась вперёд, но потом я начала понимать, зачем автор уделял столько внимания мелочам."
    cs_narrator "Женя внимательно слушала."
    cs_ls "И финал получился не совсем таким, как я ожидала."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тебе не понравился?"
    cs_narrator "Я покачала головой."
    cs_ls "Наоборот."
    cs_narrator "Немного задумалась."
    cs_ls "Он не идеальный. Но честный. Персонажи не стали внезапно другими людьми только потому, что история подошла к концу."
    cs_narrator "Женя посмотрела на обложку."
    cs_narrator "Потом на меня."
    cs_narrator "И чуть заметно улыбнулась."
    return
