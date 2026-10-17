# -*- coding: utf-8 -*-
label cs_day02_29:
    $ save_name = "Чужая смена — День 2: Медицинский персонал"
    $ cs_part03_live = False
    $ cs_part04_live = True
    $ cs_director_scene("bg int_aidpost_day")
    scene bg int_aidpost_day
    $ cs_part04_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/medstation_inside_day.ogg":
        play ambience "sound/ambiences/medstation_inside_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.1, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/get_to_know_me_better.ogg":
        play music "sound/music/get_to_know_me_better.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part04_s29:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Внутри было прохладнее, чем на улице."
    cs_narrator "Пахло лекарствами и чем-то резким, напоминавшим антисептик."
    cs_narrator "Белые шкафчики."
    cs_narrator "Кушетка."
    cs_narrator "Стол."
    cs_narrator "Медицинские принадлежности."
    cs_narrator "И за столом сидела женщина в белом халате."
    cs_narrator "Она что-то записывала в журнал."
    cs_narrator "Услышав наши шаги, подняла глаза."
    cs_th "Виола."
    cs_narrator "Я узнала её сразу."
    cs_narrator "Впрочем, после знакомства с остальными жителями «Совёнка» это уже не должно было удивлять."
    cs_narrator "Она посмотрела сначала на меня, потом на Дарью."
    cs_vi "Доброе утро, девочки. С чем пожаловали?"
    cs_narrator "Я невольно улыбнулась."
    cs_ls "Доброе. У нас небольшое происшествие."
    cs_narrator "Виола отложила ручку."
    cs_vi "Надеюсь, действительно небольшое."
    cs_narrator "Я показала локоть."
    cs_ls "Несанкционированное взаимодействие с деревянным дверным косяком."
    cs_narrator "Виола посмотрела на руку."
    cs_narrator "Затем на меня."
    cs_narrator "Уголки её губ слегка приподнялись."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "И кто победил?"
    cs_ls "Судя по состоянию косяка, он."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья негромко рассмеялась."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Ну-ка, иди сюда."
    cs_narrator "Я подошла к столу."
    cs_narrator "Она внимательно осмотрела повреждение."
    cs_vi "Обычная царапина. Глубокой не выглядит. Где задела?"
    cs_ls "У кружка электроники."
    cs_vi "Понятно. Давай обработаем."
    cs_narrator "Она подготовила необходимые принадлежности."
    cs_narrator "Я села на стул."
    cs_narrator "Дарья осталась рядом."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я ей сразу сказала, что лучше зайти."
    cs_vi "И правильно сказала."
    cs_narrator "Я посмотрела на Дашу."
    cs_ls "Кажется, медицинский совет единогласно поддержал твоё предложение."
    cs_da "Бывает."
    cs_narrator "Виола усмехнулась и начала обрабатывать царапину."
    cs_narrator "Я немного поморщилась."
    cs_vi "Щиплет?"
    cs_ls "Есть такое."
    cs_vi "Потерпишь. Ничего страшного."
    cs_narrator "Я кивнула."
    cs_narrator "Виола закрыла царапину лёгкой повязкой."
    $ cs_lena_elbow_bandaged = True
    cs_narrator "Через некоторое время она закончила."
    cs_vi "Всё. Держи в чистоте. Если начнёт воспаляться или появятся другие жалобы, приходи."
    cs_ls "Спасибо."
    cs_narrator "Виола посмотрела на Дарью."
    cs_vi "А у тебя всё в порядке?"
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да, спасибо. Я за компанию."
    cs_vi "Ну и хорошо."
    cs_narrator "Она убрала принадлежности."
    cs_narrator "Затем посмотрела на нас внимательнее."
    cs_vi "Вы ведь те самые новенькие?"
    cs_narrator "Я кивнула."
    cs_ls "Лена Соколова. А это Даша."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Дарья. Очень приятно."
    $ cs_met_viola = True
    cs_vi "Виола. Можно просто по имени."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Так даже удобнее."
    cs_narrator "Виола осмотрела мою пионерскую форму."
    cs_vi "Уже успели освоиться?"
    cs_narrator "Я задумалась."
    cs_ls "Частично."
    cs_vi "Это как?"
    cs_ls "Столовую нашли. Домик получили. С местной электротехникой познакомились. Теперь вот изучаем медицинское обеспечение."
    cs_narrator "Виола рассмеялась."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Насыщенная программа."
    cs_da "И это только начало второго дня."
    cs_narrator "Виола приподняла бровь."
    cs_vi "Тогда постарайтесь хотя бы до обеда больше ничего себе не повредить."
    cs_narrator "Я кивнула."
    cs_ls "Приложим все усилия."
    cs_th "Надо же."
    cs_th "Пока медицинская комиссия настроена исключительно доброжелательно."
    cs_narrator "Я уже собиралась подняться, когда взгляд случайно зацепился за изображение на стене."
    cs_narrator "И вот тут мне стало не до шуток."
    return
