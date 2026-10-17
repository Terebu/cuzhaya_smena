# -*- coding: utf-8 -*-
label cs_day02_64a:
    $ save_name = "Чужая смена — День 2: Приглашение, которого не ожидали"
    $ cs_part09_live = True
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_dinner64a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя посмотрела на наши подносы."
    cs_narrator "Потом на свободные места."
    cs_narrator "И совершенно неожиданно кивнула на соседние стулья."
    cs_mz "Ну садитесь, раз уж пришли."
    cs_narrator "Я замерла."
    cs_th "Подождите."
    cs_th "Что?"
    cs_ls "Это сейчас было приглашение?"
    cs_narrator "Она посмотрела на меня."
    cs_mz "Нет, приказ немедленно покинуть столовую."
    cs_narrator "Я медленно улыбнулась."
    cs_ls "Женя, ты меня поражаешь."
    cs_mz "Соколова, либо садись, либо дай мне спокойно поесть."
    cs_narrator "Я моментально поставила поднос."
    cs_narrator "Дарья устроилась рядом."
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
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Спасибо."
    cs_narrator "Женя кивнула."
    cs_mz "Только предупреждаю: я сюда села, потому что здесь тихо."
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Торжественно обещаю не разрушать атмосферу."
    cs_narrator "Женя посмотрела на Дарью."
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ты ей веришь?"
    cs_narrator "Дарья задумалась."
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Минут на пять."
    cs_narrator "Я возмущённо повернулась."
    cs_ls "Даша!"
    cs_narrator "Та рассмеялась."
    cs_narrator "Женя тоже едва заметно улыбнулась."
    cs_th "Надо же."
    cs_th "Она сама предложила нам сесть."
    cs_th "Причём даже не выглядела так, будто немедленно пожалела об этом."
    cs_narrator "Мне стало неожиданно приятно."
    return
