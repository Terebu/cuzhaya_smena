# -*- coding: utf-8 -*-
label cs_day02_40:
    $ save_name = "Чужая смена — День 2: Обеденная передышка"
    $ cs_part05_live = False
    $ cs_part06_live = True
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
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
    # cs_presence_keep: hide cs
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part06_s40:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "К столовой мы подошли уже после того, как основная работа над объявлением осталась позади."
    cs_narrator "Я всё ещё мысленно возвращалась к разговору с Дарьей."
    cs_narrator "Она только что совершенно спокойно призналась, что пыталась меня подразнить, и сделала это настолько успешно, что я впервые за долгое время осталась без подходящей реплики."
    cs_th "Непорядок."
    cs_th "Я здесь, между прочим, отвечаю за сомнительный юмор."
    cs_th "Неужели у меня появился конкурент?"
    cs_narrator "Дарья шла рядом, придерживая выбившуюся прядь волос."
    cs_narrator "Кажется, она заметила моё выражение лица."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты всё ещё обдумываешь наш разговор?"
    cs_ls "Провожу анализ причин собственного поражения."
    cs_da "Серьёзная задача?"
    cs_ls "Потребуется не менее трёх рабочих дней."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я посмотрела на неё и тоже улыбнулась."
    cs_narrator "На крыльце столовой уже собирались пионеры. Из открытой двери доносились голоса, звон посуды и запах еды."
    cs_narrator "После утренней пробежки, клубов, медпункта и рисования организм начал недвусмысленно напоминать, что хорошее настроение не заменяет обед."
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
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
    # cs_presence_keep: hide cs
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/dining_hall_full.ogg":
        play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.2, channel="ambience", delay=1.0)
    cs_narrator "Мы вошли внутрь."
    cs_narrator "Заняли очередь, получили подносы и нашли свободный столик."
    cs_narrator "Я поставила тарелку перед собой."
    cs_th "Надо же."
    cs_th "Второй день."
    cs_th "А я уже начинаю воспринимать здешнюю столовую как часть обычного расписания."
    cs_narrator "Дарья развернула салфетку."
    cs_da "После обеда куда?"
    cs_narrator "Я уже собиралась ответить, что никуда."
    cs_narrator "Действительно собиралась."
    cs_narrator "Но потом вспомнила утреннюю пробежку."
    cs_narrator "Пустое место возле ворот."
    cs_narrator "Исчезнувший автобус."
    cs_narrator "И разговор с Семёном."
    cs_th "Ах да."
    cs_th "Есть же ещё одна небольшая нерешённая проблема."
    cs_narrator "Я медленно положила ложку."
    cs_ls "У меня появилась мысль."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Судя по выражению лица, опять что-то связанное с расследованием."
    cs_ls "Ты начинаешь слишком хорошо меня понимать."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я уже знаю как минимум три твоих выражения лица. Одно означает, что ты шутишь. Второе — что собираешься пошутить. А третье — что придумала что-то сомнительное."
    cs_narrator "Я задумалась."
    cs_ls "Сейчас какое?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Третье."
    cs_narrator "Я вздохнула."
    cs_ls "И опять правильно."
    cs_narrator "Она улыбнулась, но затем стала серьёзнее."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты о дороге?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Утром я видела ворота, но за них не выходила. Автобуса нет. А что дальше по дороге, мы не знаем."
    cs_da "И ты хочешь проверить это сегодня?"
    cs_ls "Хотя бы немного пройтись. Сначала посмотреть, есть ли там перекрёстки, указатели или какие-нибудь здания."
    cs_narrator "Дарья задумалась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я не против. Но только вместе с Семёном, как договаривались. И не будем уходить в лес."
    cs_narrator "Я кивнула."
    cs_ls "Согласна."
    cs_da "И возьмём воду. А ещё заранее решим, когда поворачивать обратно."
    cs_narrator "Я улыбнулась."
    cs_ls "Тебе определённо нужно руководить этой экспедицией."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Потому что я вспомнила про воду?"
    cs_ls "Для нашей научной группы это уже выдающийся уровень организации."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part06_semen_arrived:
    cs_narrator "В этот момент возле столика появился Семён с подносом."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Место свободно?"
    cs_narrator "Я посмотрела на него."
    cs_narrator "Затем на Дарью."
    cs_ls "А вот и третий участник экспедиции."
    cs_narrator "Семён остановился."
    cs_sy "Какой ещё экспедиции?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена предлагает после обеда сходить к воротам и проверить дорогу."
    cs_narrator "Семён стал серьёзнее."
    cs_sy "Наконец-то. Я утром как раз об этом говорил."
    cs_narrator "Он поставил поднос и сел напротив."
    cs_sy "Только далеко уходить не надо. Мы ведь понятия не имеем, что там."
    cs_ls "Именно поэтому и хочется посмотреть."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Хорошо. Тогда сначала доедим."
    cs_narrator "Я подняла ложку."
    cs_ls "Прекрасный план. Научные открытия требуют полноценного питания."
    cs_narrator "Семён усмехнулся."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "А я всё-таки принялась за обед."
    cs_th "Ну вот."
    cs_th "Уже лучше."
    cs_th "Не одна."
    cs_th "Не на эмоциях."
    cs_th "И хотя бы с минимальным представлением о том, что собираемся делать."
    return
