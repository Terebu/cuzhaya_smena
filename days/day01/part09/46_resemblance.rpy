# -*- coding: utf-8 -*-
label cs_day01_46:
    $ save_name = "Чужая смена — День 1: Неожиданное сходство"
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(0.7)
    $ renpy.music.set_volume(0.35,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы шли молча. После разговора на площади ни шуток, ни объяснений не требовалось."
    cs_narrator "В закатном солнце волосы Дарьи казались ещё ярче."
    cs_th "Всё-таки форма ей идёт."
    cs_narrator "Дарья заметила мою улыбку."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Ничего."
    cs_da "У тебя опять такое выражение лица."
    cs_ls "Какое?"
    cs_da "Довольное."
    cs_ls "Прошу занести в протокол. Подозреваемая впервые за день довольна происходящим."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Ты когда-нибудь перестанешь разговаривать протоколами?"
    cs_ls "Не исключено. Но пока экспериментальная программа продолжается."
    cs_narrator "Мы свернули за один из домиков."
    cs_narrator "Я на секунду отвлеклась на вывеску впереди и едва не столкнулась с девушкой, выходившей нам навстречу."
    cs_ls "Ой, извини!"
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Извини…"
    cs_narrator "Мы извинились одновременно. Я подняла глаза и замерла."
    show un normal pioneer at cs_actor_left zorder 10
    # cs_composition: regroup
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Два фиолетовых хвоста, зелёные глаза, знакомое лицо."
    cs_th "Да ладно."
    cs_narrator "Девушка опустила взгляд, не понимая, зачем я её разглядываю."
    cs_th "Лена Тихонова. Та самая."
    cs_narrator "Похожие волосы, почти одинаковые глаза. Но она держалась тихо и настороженно, а я уже поставила её в неловкое положение."
    cs_th "Встретила тёзку и немедленно начала вести себя подозрительно."
    cs_narrator "Дарья остановилась рядом и оглядела нас обеих."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен?"
    cs_narrator "Я знала её характер, события её истории, варианты будущего, о которых не хотелось думать."
    cs_narrator "На компьютере можно загрузить сохранение и попробовать другой выбор. Здесь она не обязана жить по моим воспоминаниям."
    cs_th "Сама просила Семёна не относиться к людям как к персонажам. Пора выполнять собственные рекомендации."
    cs_narrator "Девушка осторожно произнесла:"
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Всё нормально?"
    cs_ls "Да. Просто задумалась."
    stop music fadeout 2.5
    pause 0.7
    cs_narrator "Можно познакомиться или просто извиниться и идти дальше. Знание чужой истории не даёт права на дружбу."
    return
