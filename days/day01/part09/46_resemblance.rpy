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
    cs_narrator "Мы с Дарьей продолжали идти по дорожке."
    cs_narrator "После разговора на площади между нами установилось какое-то новое, непривычное спокойствие."
    cs_narrator "Я больше не пыталась придумать удачную шутку."
    cs_narrator "Она не требовала объяснений."
    cs_narrator "Мы просто шли рядом."
    cs_narrator "И, пожалуй, впервые за весь день мне этого вполне хватало."
    cs_narrator "Я взглянула на Дарью."
    cs_narrator "Красные волосы."
    cs_narrator "Белая рубашка."
    cs_narrator "Красный галстук."
    cs_narrator "На закатном солнце её волосы казались ещё ярче."
    cs_th "Всё-таки форма ей идёт."
    cs_narrator "Я едва заметно улыбнулась."
    cs_narrator "Дарья сразу заметила."
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
    cs_narrator "Я задумалась."
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
    cs_narrator "Мы произнесли это почти одновременно."
    cs_narrator "Я подняла глаза."
    cs_narrator "И замерла."
    show un normal pioneer at cs_actor_left zorder 10
    # cs_composition: regroup
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Передо мной стояла девушка с фиолетовыми волосами, собранными в два хвоста."
    cs_narrator "Зелёные глаза."
    cs_narrator "Светлая кожа."
    cs_narrator "Пионерская форма."
    cs_narrator "И совершенно знакомое лицо."
    cs_th "Да ладно."
    cs_narrator "Я несколько секунд молчала."
    cs_narrator "Она тоже."
    cs_narrator "Потом девушка слегка опустила взгляд, явно не понимая, почему незнакомка так пристально её рассматривает."
    cs_narrator "И тут до меня окончательно дошло."
    cs_th "Лена."
    cs_th "Та самая."
    cs_th "Только не Соколова."
    cs_narrator "Я невольно посмотрела на её волосы."
    cs_narrator "Затем на собственную фиолетовую прядь."
    cs_narrator "Похожий оттенок."
    cs_narrator "Почти одинаковый цвет глаз."
    cs_narrator "Но совершенно разная манера держаться."
    cs_narrator "Она выглядела тихой и немного настороженной."
    cs_narrator "А я, судя по её выражению лица, уже успела поставить человека в неловкое положение."
    cs_th "Отлично."
    cs_th "Встретила тёзку и немедленно начала вести себя подозрительно."
    cs_narrator "Дарья остановилась рядом."
    cs_narrator "Перевела взгляд с девушки на меня."
    cs_narrator "Потом обратно."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен?"
    cs_narrator "Я не ответила сразу."
    cs_narrator "Потому что вспомнила кое-что ещё."
    cs_narrator "Я знала эту девушку по оригинальной истории."
    cs_narrator "Её характер."
    cs_narrator "Некоторые события, связанные с ней."
    cs_narrator "И несколько вариантов будущего, о которых сейчас совершенно не хотелось думать."
    cs_narrator "На экране компьютера всё воспринималось иначе."
    cs_narrator "Там можно было вернуться к сохранению."
    cs_narrator "Попробовать другой выбор."
    cs_narrator "Посмотреть, как изменится история."
    cs_narrator "А здесь передо мной стоял человек."
    cs_narrator "Живой."
    cs_narrator "Настоящий."
    cs_narrator "И явно не обязанный соответствовать тому, что я помнила."
    cs_th "Я сама говорила Семёну не относиться к ним как к персонажам."
    cs_th "Пора выполнять собственные рекомендации."
    cs_narrator "Девушка осторожно произнесла:"
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Всё нормально?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Просто задумалась."
    stop music fadeout 2.5
    pause 0.7
    cs_narrator "И тут я поняла, что могу сделать."
    cs_narrator "Остановиться."
    cs_narrator "Попробовать познакомиться."
    cs_narrator "Или просто извиниться и пойти дальше."
    cs_narrator "В конце концов, никто не обязан дружить со мной только потому, что я знаю его историю."
    return
