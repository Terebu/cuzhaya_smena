# -*- coding: utf-8 -*-
label cs_day01_53:
    $ save_name = "Чужая смена — День 1: Последний посетитель"
    scene bg ext_dining_hall_near_sunset
    # cs_focus_suppressed: show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.5 fadein 1.5
    # cs_focus: camera
    hide cs_darya with Dissolve(0.25)
    cs_narrator "После ужина на улице стало немного прохладнее."
    cs_narrator "Солнце медленно опускалось за деревья, окрашивая дорожки мягким оранжевым светом."
    cs_narrator "Я шла рядом с Дарьей, поглядывая по сторонам."
    cs_narrator "Дорогу до библиотеки я помнила."
    cs_narrator "По крайней мере, примерно."
    cs_narrator "А после дневных прогулок начинала ориентироваться уже не только по игровым фонам."
    # cs_darya_variety: reaction
    # cs_focus_suppressed: show cs_darya thinking pioneer normal at cs_darya_normal_center
    # cs_focus: camera
    show cs_darya thinking pioneer normal at cs_darya_normal_center with Dissolve(0.25)
    cs_da "Ты знаешь, какая здесь библиотека?"
    cs_ls "Была одна в оригинальной истории."
    cs_da "Значит, опять проверяем совпадения?"
    cs_ls "На этот раз с пользой для образования."
    cs_narrator "Я ненадолго замолчала."
    cs_narrator "Затем добавила:"
    cs_ls "И ещё мне любопытно познакомиться с местной библиотекаршей."
    cs_narrator "Дарья бросила на меня подозрительный взгляд."
    cs_da "Почему?"
    cs_ls "Женя."
    cs_da "Это имя?"
    cs_ls "Да. Она довольно строгая."
    cs_da "И?"
    cs_ls "Не особенно любит шум, беспорядок и людей, которые отвлекают её от работы."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Потом медленно улыбнулась."
    # cs_darya_variety: reaction
    show cs_darya explaining pioneer normal at cs_darya_normal_center
    cs_da "То есть ты решила пойти именно туда?"
    cs_ls "Почему бы и нет?"
    cs_da "Лен, пожалуйста, не пытайся специально её раздражать."
    cs_narrator "Я пожала плечами."
    cs_ls "Постараюсь."
    cs_da "Это не очень убедительный ответ."
    cs_ls "Другого пока не подготовила."
    scene cs_library_exterior_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.2)
    label cs_check_day01_part10_exterior:
    cs_narrator "Мы свернули к библиотеке."
    if cs_met_un and cs_friend_un > 0:
        $ cs_un_name_known = True
        show un smile pioneer at cs_actor_left zorder 10
        # cs_composition: regroup
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        label cs_check_day01_part10_un_friend:
        cs_narrator "Возле библиотеки я заметила знакомую фиолетовую причёску."
        cs_th "О."
        cs_th "Тёзка."
        cs_narrator "Лена Тихонова стояла на крыльце с книгой в руках."
        cs_narrator "Увидев нас, она слегка улыбнулась."
        show un smile pioneer at cs_actor_left zorder 10
        # cs_speaker: present
        show un smile pioneer at cs_actor_left zorder 10
        cs_un "Привет."
        cs_ls "Привет, Лена."
        cs_narrator "Она чуть смутилась."
        # cs_darya_variety: reaction
        show cs_darya smile pioneer normal at cs_darya_normal_right
        cs_narrator "Дарья улыбнулась."
        cs_da "Уже успела взять новую книгу?"
        show un smile pioneer at cs_actor_left zorder 10
        # cs_speaker: present
        show un smile pioneer at cs_actor_left zorder 10
        cs_un "Да. Я после ужина вернулась. Хотела ещё кое-что посмотреть."
        cs_narrator "Я кивнула на дверь."
        cs_ls "А мы как раз туда."
        cs_narrator "Тёзка немного помолчала."
        show un shy pioneer at cs_actor_left zorder 10
        # cs_speaker: present
        show un shy pioneer at cs_actor_left zorder 10
        cs_un "Только… с Женей лучше разговаривать потише."
        cs_narrator "Я улыбнулась."
        cs_ls "Принято."
        show un smile pioneer at cs_actor_left zorder 10
        # cs_speaker: present
        show un smile pioneer at cs_actor_left zorder 10
        cs_un "Она не злая. Просто любит порядок."
        cs_ls "Это я уже поняла."
        cs_narrator "Лена осторожно кивнула."
        show un smile pioneer at cs_actor_left zorder 10
        # cs_speaker: present
        show un smile pioneer at cs_actor_left zorder 10
        cs_un "Тогда увидимся."
        cs_ls "Увидимся."
        hide un
        # cs_composition: regroup
        show cs_darya smile pioneer normal at cs_darya_normal_center
        # cs_focus: camera
        hide cs_darya with Dissolve(0.25)
        cs_narrator "Она направилась по дорожке с книгой под мышкой."
        cs_narrator "Я проводила её взглядом."
        cs_th "Интересная девушка."
        cs_th "И явно гораздо спокойнее меня."
        hide un
    elif cs_met_un:
        # cs_focus: camera
        show cs_darya smile pioneer normal at cs_darya_normal_center with Dissolve(0.25)
        show un normal pioneer at cs_actor_left zorder 10
        # cs_composition: regroup
        show cs_darya smile pioneer normal at cs_darya_normal_right
        label cs_check_day01_part10_un_neutral:
        # cs_speaker: present
        show un normal pioneer at cs_actor_left zorder 10
        cs_un "Добрый вечер."
        cs_ls "Добрый вечер, Лена. Мы ненадолго в библиотеку."
        # cs_speaker: present
        show un normal pioneer at cs_actor_left zorder 10
        cs_un "Женя скоро закрывает. Лучше поторопитесь."
        hide un
        # cs_composition: regroup
        show cs_darya smile pioneer normal at cs_darya_normal_center
    # cs_focus: camera
    hide cs_darya with Dissolve(0.25)
    cs_narrator "Перед нами стояла библиотека."
    cs_narrator "Знакомое здание."
    cs_narrator "Знакомые окна."
    cs_narrator "Знакомая дверь."
    cs_narrator "И совершенно незнакомая перспектива разговора с человеком, который мог оказаться не таким, каким я привыкла видеть его на экране."
    cs_narrator "Я остановилась у входа."
    # cs_darya_variety: reaction
    # cs_focus_suppressed: show cs_darya thinking pioneer normal at cs_darya_normal_center
    # cs_focus: camera
    show cs_darya thinking pioneer normal at cs_darya_normal_center with Dissolve(0.25)
    cs_da "Ты чего?"
    cs_ls "Думаю."
    cs_da "О чём?"
    cs_ls "О том, как не испортить первое впечатление."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Пауза."
    cs_da "Начни с обычного «здравствуйте»."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Радикальное предложение."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    cs_narrator "Она рассмеялась."
    cs_narrator "Я открыла дверь."
    play sound cs_day_sfx_door
    stop music fadeout 2.0
    return
