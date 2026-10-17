# -*- coding: utf-8 -*-
label cs_day02_67:
    $ save_name = "Чужая смена — День 2: Последние страницы"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    stop music fadeout 2.0
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    play ambience "sound/ambiences/library_day.ogg" fadeout 1.5 fadein 1.5
    $ renpy.music.set_volume(0.055, channel="ambience")
    label cs_check_finale_67:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "В библиотеке было тихо."
    cs_narrator "За окнами уже сгущались вечерние тени."
    cs_narrator "Солнечные полосы на полу стали длиннее, а привычный запах старой бумаги казался особенно заметным после свежего воздуха."
    cs_narrator "Женя сидела за столом и что-то записывала."
    cs_narrator "Услышав дверь, она подняла голову."
    cs_narrator "Посмотрела на нас."
    cs_narrator "Затем на книгу в моей руке."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Соколова?"
    cs_narrator "Я кивнула."
    cs_ls "Привет."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ты опять здесь?"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "На несколько минут. Хочу дочитать и вернуть книгу, если не помешаю."
    cs_narrator "Она посмотрела на часы."
    cs_narrator "Потом на стопку бумаг перед собой."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Я как раз заканчиваю с журналами. Через некоторое время буду закрывать."
    cs_ls "Тогда постараюсь уложиться."
    cs_narrator "Женя кивнула."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Хорошо."
    cs_narrator "Я прошла к знакомому столу."
    cs_narrator "Дарья присела рядом."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я пока подожду тебя."
    cs_ls "Спасибо."
    # cs_director_begin: Last pages, independent reading
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_ed66cb23a2:
    # cs_director_end
    cs_narrator "Я открыла книгу."
    cs_narrator "Закладка лежала почти у самого конца."
    cs_narrator "Несколько страниц."
    cs_narrator "Один разговор между персонажами."
    cs_narrator "Развязка конфликта."
    cs_narrator "И финал, к которому история постепенно шла всё это время."
    cs_th "Ну что ж."
    cs_th "Посмотрим, чем всё закончится."
    cs_narrator "Я углубилась в чтение."
    cs_narrator "Сначала немного мешали звуки с площади."
    cs_narrator "Потом они перестали привлекать внимание."
    cs_narrator "Я дошла до последней главы."
    cs_narrator "Читать стала медленнее."
    cs_narrator "Не потому, что устала."
    cs_narrator "Просто не любила торопиться с финалами."
    cs_narrator "Особенно если к персонажам уже успела привыкнуть."
    cs_narrator "Последние несколько страниц оказались совсем не такими, как я ожидала."
    cs_narrator "Автор не стал устраивать грандиозное примирение."
    cs_narrator "Не решил все проблемы одной красивой речью."
    cs_narrator "Не сделал вид, будто прежние поступки персонажей ничего не значили."
    cs_narrator "Кое-что осталось недосказанным."
    cs_narrator "Кое-кто так и не решился произнести самые нужные слова."
    cs_narrator "И всё же финал не казался оборванным."
    cs_narrator "Скорее честным."
    cs_narrator "Я дочитала последнее предложение."
    cs_narrator "Не сразу закрыла книгу."
    cs_narrator "Несколько секунд просто смотрела на страницу."
    cs_th "Вот и всё."
    cs_narrator "Потом осторожно вложила закладку внутрь."
    cs_narrator "Закрыла обложку."
    cs_narrator "И положила ладонь на книгу."
    cs_th "Хорошая история."
    cs_th "Не идеальная."
    cs_th "Но, пожалуй, именно поэтому и хорошая."
    # cs_director_begin: Darya starts talking, seated portrait remains
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_cc185e76a2:
    # cs_director_end
    cs_narrator "Дарья заметила, что я перестала читать."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Закончила?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну как?"
    cs_narrator "Я посмотрела на обложку."
    cs_narrator "Немного подумала."
    cs_ls "Мне понравилось."
    cs_narrator "Она улыбнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Сильно?"
    cs_narrator "Я кивнула."
    cs_ls "Особенно вторая половина."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда не зря читала."
    cs_narrator "Я посмотрела на неё."
    cs_th "Да."
    cs_th "Определённо не зря."
    cs_narrator "Мы поднялись и подошли к столу Жени."
    return
