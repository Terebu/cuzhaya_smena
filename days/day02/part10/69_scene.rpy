# -*- coding: utf-8 -*-
label cs_day02_69:
    $ save_name = "Чужая смена — День 2: Пожелание спокойного вечера"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_69:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на стопку книг, потом на Женю."
    cs_ls "Спасибо, что дала мне спокойно дочитать."
    cs_narrator "Она слегка удивилась."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ты ведь сама попросила."
    cs_ls "Знаю."
    cs_narrator "Немного помолчала."
    cs_ls "Просто спасибо."
    cs_narrator "Женя посмотрела на меня. Затем чуть улыбнулась."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Пожалуйста."
    cs_narrator "Издалека донеслись новые голоса. Кто-то явно собирался на музыкальный вечер. Женя посмотрела в окно."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вам, наверное, уже пора. И мне закрываться."
    cs_narrator "Дарья кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да, не хотим пропустить выступление."
    cs_narrator "Я посмотрела на Женю."
    cs_ls "Тогда до завтра."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "До завтра."
    cs_narrator "Пауза."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И, Лена…"
    cs_narrator "Я остановилась."
    cs_ls "Да?"
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Хорошего вечера."
    cs_ls "Тебе тоже."
    cs_narrator "Мы вышли."
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "На крыльце я ненадолго остановилась. Посмотрела в сторону библиотеки."
    # cs_inward_beat_5: attention turns inward
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Забавно. Вчера я пришла сюда с намерением проверить, насколько Женя похожа на знакомого персонажа. Сегодня просто вернула книгу. И, кажется, этот визит оказался для нас гораздо важнее."
    # Return to the same conversation, with the same cast and placement.
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Дарья подошла ближе."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну что, теперь на концерт?"
    cs_ls "Теперь точно."
    cs_narrator "Она улыбнулась. Мы направились к площади."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    return
