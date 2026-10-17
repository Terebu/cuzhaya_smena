# -*- coding: utf-8 -*-
label cs_day02_15:
    $ save_name = "Чужая смена — День 2: Бирюзовые хвосты"
    $ cs_part02_live = True
    hide screen cs_day02_continue_screen
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    $ cs_part02_cg = False
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
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part02_s15:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Из столовой мы вышли втроём."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part02_cg = False
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
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Семён задержался на крыльце, пытаясь выяснить у одного из пионеров, во сколько начнётся линейка, а мы с Дарьей отошли в сторону дорожки."
    cs_narrator "После завтрака мне стало заметно лучше."
    cs_narrator "Хотя, если честно, особой усталости я не чувствовала и до него."
    cs_narrator "Утренняя пробежка окончательно разбудила организм, турники добавили приятной тяжести в руках, а каша завершила программу физкультурно-оздоровительных мероприятий."
    cs_th "Можно считать, что организм успешно прошёл техническое обслуживание."
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она шла рядом, поправляя выбившуюся красную прядь."
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
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Ну что, как тебе второе утро в «Совёнке»?"
    cs_da "Пока неплохо. Если не считать того, что ты успела прожить отдельный маленький день, пока я спала."
    cs_ls "Кто рано встаёт, тому достаются турники."
    cs_da "Очень сомнительная награда."
    cs_narrator "Я усмехнулась."
    cs_ls "Зато бесплатная."
    cs_narrator "Она покачала головой."
    cs_da "Иногда мне кажется, что ты способна найти положительную сторону даже в отсутствии горячей воды."
    cs_ls "Не надо. Здесь уже начинаются вопросы к качеству обслуживания."
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я уже собиралась предложить пойти к площади, когда заметила девушку, шедшую нам навстречу."
    cs_narrator "Бирюзовые волосы."
    cs_narrator "Два длинных хвоста, покачивавшихся при каждом шаге."
    cs_narrator "Папка с бумагами под мышкой."
    cs_narrator "Она что-то негромко напевала, иногда заглядывая в один из листов."
    cs_narrator "Я замедлила шаг."
    cs_th "О."
    cs_th "Вот это знакомое лицо."
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
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    $ cs_part02_cast = ["cs_darya"]
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
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что такое?"
    cs_narrator "Я указала взглядом вперёд."
    cs_ls "Кажется, сейчас будет ещё одно знакомство."
    cs_narrator "Дарья проследила за моим взглядом."
    cs_da "Ты её знаешь?"
    cs_narrator "Я ненадолго задумалась."
    cs_ls "По игре. Лично — нет."
    cs_narrator "Вчера я сказала примерно то же самое о Жене."
    cs_narrator "И в результате устроила разговор, к которому никто из нас не был готов."
    cs_th "Сегодня попробуем иначе."
    cs_th "Без рассказов о будущем."
    cs_th "Без объяснения чужих биографий."
    cs_th "Просто познакомимся."
    # cs_presence_keep: hide cs_darya
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
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    cs_narrator "Девушка заметила нас и приветливо улыбнулась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    $ cs_part02_cast = ["mi", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_miku_15:
    cs_mi "Доброе утро!"
    cs_narrator "Я ответила почти автоматически:"
    label cs_check_part02_japanese:
    cs_ls "{font=mods/chuzaya_smena/fonts/NotoSansCJKjp-Regular.otf}おはようございます。元気ですか？{/font}"
    cs_th "Доброе утро. Как дела?"
    cs_narrator "Мику остановилась."
    cs_narrator "На мгновение она даже перестала улыбаться."
    cs_narrator "А потом её лицо буквально озарилось."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    $ cs_part02_cast = ["mi", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "{font=mods/chuzaya_smena/fonts/NotoSansCJKjp-Regular.otf}えっ、日本語が話せるの？{/font}"
    cs_th "Ой, ты говоришь по-японски?"
    cs_narrator "Я улыбнулась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "{font=mods/chuzaya_smena/fonts/NotoSansCJKjp-Regular.otf}少しだけ。{/font}"
    cs_th "Немного."
    cs_narrator "И тут Мику действительно заговорила быстрее."
    cs_narrator "Слишком быстро."
    cs_narrator "Я поняла первые несколько слов, уловила вопрос про учёбу, а затем окончательно потеряла нить разговора."
    cs_th "Так."
    cs_th "Кажется, учебники меня к этому не готовили."
    cs_narrator "Я подняла ладонь."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Подожди. {font=mods/chuzaya_smena/fonts/NotoSansCJKjp-Regular.otf}ゆっくり話してくれる？{/font}"
    cs_th "Можешь говорить помедленнее?"
    cs_narrator "Мику остановилась."
    cs_narrator "Потом рассмеялась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    $ cs_part02_cast = ["mi", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi shy pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Ой, извини! Просто я так обрадовалась! Здесь почти никто не говорит по-японски, а тут ты вдруг подходишь и сразу здороваешься! Я даже растерялась!"
    cs_narrator "Я тоже рассмеялась."
    cs_ls "Ничего. Я японский учила, но до свободного разговора мне ещё далеко."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Правда? А где учила? И давно? А читать умеешь? А писать? Хотя писать гораздо сложнее, особенно иероглифы…"
    cs_narrator "Она остановилась."
    cs_narrator "Внимательно посмотрела на меня."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi shy pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Я опять слишком быстро говорю?"
    cs_ls "Немного."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Ой."
    cs_ls "Зато теперь понимаю, почему тебе понравилось услышать японский."
    cs_narrator "Мику улыбнулась."
    cs_narrator "Дарья, до этого молча наблюдавшая за разговором, слегка наклонилась ко мне."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я поняла только «доброе утро»."
    cs_narrator "Я повернулась к ней."
    cs_ls "Значит, примерно четверть переговоров прошла успешно."
    cs_da "Очень высокий дипломатический результат."
    cs_narrator "Мику засмеялась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "А вы, наверное, те самые новенькие? Мне уже рассказывали, что приехали две девушки с необычными волосами!"
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она на меня."
    cs_ls "Кажется, цвет волос стал нашим официальным удостоверением личности."
    cs_da "По крайней мере, нас трудно перепутать."
    $ cs_met_mi = True
    $ cs_mi_name_known = True
    cs_mi "Ой, простите, я же даже не представилась! Меня Мику зовут."
    cs_narrator "Я кивнула."
    cs_ls "Лена Соколова."
    cs_da "А я Даша."
    cs_mi "Очень приятно!"
    cs_ls "Взаимно."
    cs_th "Вот так."
    cs_th "Нормальное знакомство."
    cs_th "Пожалуй, я всё-таки обучаемая."
    return
