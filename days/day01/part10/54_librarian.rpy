# -*- coding: utf-8 -*-
label cs_day01_54:
    $ save_name = "Чужая смена — День 1: Хранительница книжного фонда"
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    show cs_zhenya normal pioneer normal at cs_darya_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(1.0)
    label cs_check_day01_part10_library:
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/library_day.ogg":
        play ambience "sound/ambiences/library_day.ogg" fadeout 1.5 fadein 1.5
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Пахло бумагой, деревом, старой краской — библиотекой."
    # cs_authored_pov_0: Lena examines the room, not her companions
    $ cs_frame_focus([])
    with cs_sprite_change
    cs_narrator "Я огляделась."
    cs_narrator "Стеллажи, читательские столы, каталожные ящики. Ни компьютеров, ни электронного поиска. Очень много бумаги."
    cs_th "Поисковая система 1980-го года. Индексация ручная, время ответа зависит от настроения библиотекаря."
    # cs_authored_pov_1: Lena finds the librarian at her desk
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "За столом сидела девушка в очках."
    cs_narrator "Она читала книгу, придерживая страницу пальцем."
    cs_narrator "Услышав дверь, подняла глаза."
    cs_th "Женя."
    cs_narrator "И пока мы не вошли, она явно собиралась заниматься своими делами."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Здравствуйте. Что-то хотели?"
    cs_narrator "Я шагнула вперёд."
    cs_ls "Добрый вечер."
    # cs_authored_pov_2: Darya joins the greeting; keep both throughout the conversation
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    cs_narrator "Дарья поздоровалась следом."
    cs_narrator "Женя посмотрела на часы."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Если за книгами, то лучше не затягивайте. Скоро буду закрывать."
    cs_ls "Мы ненадолго."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Что ищете?"
    cs_ls "Газеты. Или календарь."
    cs_narrator "Женя приподняла бровь."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Календарь?"
    cs_ls "Желательно текущего года."
    cs_narrator "Женя посмотрела на меня внимательнее."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А зачем?"
    cs_th "Вот и начались вопросы."
    cs_ls "Хотим кое-что проверить."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Например?"
    cs_ls "Дату."
    cs_narrator "Несколько секунд Женя молчала."
    # cs_speaker: present
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ты не знаешь сегодняшнее число?"
    cs_ls "Пока не совсем уверена."
    cs_narrator "Она перевела взгляд на Дарью."
    # cs_speaker: present
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вы новенькие?"
    cs_da "Да, сегодня приехали."
    cs_narrator "Женя снова посмотрела на меня."
    # cs_speaker: present
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Понятно."
    cs_narrator "Судя по тону, понятно ей было не всё. Она закрыла книгу."
    $ cs_met_mz = True
    # cs_speaker: present
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Я Женя. За библиотеку отвечаю. Если хотите что-нибудь взять, сначала запишу вас."
    cs_ls "Лена Соколова. А это Дарья."
    cs_da "Дарья Еретикова. Можно Даша."
    cs_narrator "Женя оглядела наши волосы и форму."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Понятно. Про двух новеньких уже говорили."
    cs_narrator "Я усмехнулась."
    cs_ls "Надеюсь, исключительно хорошее."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Разное."
    cs_ls "Обнадёживающее начало."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она не улыбнулась, но в глазах мелькнул интерес."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только, пожалуйста, потише. Здесь библиотека."
    cs_ls "Договорились."
    cs_narrator "Дарья посмотрела на меня."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Видишь? Нормально получается."
    cs_ls "Не спугни."
    cs_narrator "Женя подняла голову."
    # cs_speaker: present
    show cs_zhenya shrug pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вы что-то сказали?"
    cs_ls "Нет. Обсуждаем соблюдение правил."
    cs_narrator "Женя вздохнула и вернулась к столу."
    # cs_director_begin: Zhenya works at the desk offscreen
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_4d6f0716e1:
    # cs_director_end
    cs_narrator "Возле неё лежали возвращённые книги с инвентарными номерами на корешках. Часть уже была рассортирована."
    cs_th "Помочь и познакомиться поближе — или заняться своими поисками?"
    return
