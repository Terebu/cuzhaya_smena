# -*- coding: utf-8 -*-
label cs_day02_33:
    $ save_name = "Чужая смена — День 2: Возвращение к обычным делам"
    $ cs_part03_live = False
    $ cs_part04_live = True
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part04_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.2, channel="music", delay=1.0)
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    $ cs_part04_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part04_s33:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда мы вернулись к клубам, Семён уже ждал возле рабочего стола."
    cs_narrator "Папка лежала перед ним."
    cs_narrator "Рядом находились карандаши."
    cs_th "Отлично."
    cs_th "Художественное имущество пережило отсутствие руководства."
    cs_narrator "Он заметил нас."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А вот и вы. Всё нормально?"
    cs_narrator "Я показала локоть."
    cs_ls "Медицинская помощь оказана. Пациентка допущена к выполнению общественно полезных работ."
    cs_narrator "Семён усмехнулся."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Тогда хорошо."
    cs_narrator "Дарья подошла к столу."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Узнал время выступления?"
    cs_sy "Да. Ольга Дмитриевна сказала, что всё начнётся после ужина. Точное время пока лучше не писать, она ещё уточнит расписание."
    cs_narrator "Я кивнула."
    cs_ls "Тогда пока сделаем основную композицию."
    cs_narrator "Семён посмотрел на нас."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Кстати, что-нибудь ещё интересное узнали?"
    cs_narrator "Я вспомнила плакат."
    cs_narrator "Виолу."
    cs_narrator "Наш разговор с Дашей."
    cs_narrator "И собственное обещание не превращать каждую необычную деталь в невероятную теорию."
    cs_ls "Нашли одну странность в медпункте."
    cs_narrator "Семён приподнял бровь."
    cs_sy "Какую?"
    cs_narrator "Я немного подумала."
    cs_ls "На стене висит рисунок, который напоминает мне изображение из более поздней истории. Но я пока не уверена, что это одно и то же."
    cs_narrator "Он задумался."
    cs_sy "То есть ещё одно совпадение?"
    cs_ls "Возможно."
    cs_narrator "Дарья кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Пока мы решили ничего не утверждать без проверки."
    cs_narrator "Семён посмотрел на неё."
    cs_narrator "Потом на меня."
    cs_sy "По-моему, правильно."
    cs_narrator "Я улыбнулась."
    cs_ls "Удивительное единодушие."
    cs_narrator "Он рассмеялся."
    cs_sy "Теперь можно всё-таки заняться объявлением?"
    cs_narrator "Я посмотрела на лежавший перед нами лист."
    cs_narrator "Белая бумага."
    cs_narrator "Обычные карандаши."
    cs_narrator "Никаких технологий будущего."
    cs_narrator "Никаких загадочных артефактов."
    cs_narrator "Просто задание, которое нужно выполнить."
    $ cs_director_scene("cs_cg_poster_planning_day")
    scene cs_cg_poster_planning_day
    $ cs_part04_cg = True
    # cs_presence_keep: hide cs_darya
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
    $ cs_part04_cast = []
    with Dissolve(0.8)
    label cs_check_part04_poster_work:
    cs_narrator "Я села."
    cs_narrator "Взяла карандаш."
    cs_narrator "Несколько секунд рассматривала чистый лист."
    cs_th "Пожалуй, Семён прав."
    cs_th "За сегодняшнее утро мы и так успели собрать достаточно вопросов."
    cs_th "Теперь можно сделать что-нибудь, на что действительно способны повлиять."
    cs_narrator "Дарья придвинула ко мне лист с наброском надписи."
    cs_da "А если название сделать вот здесь?"
    cs_narrator "Я посмотрела."
    cs_narrator "Кивнула."
    cs_ls "Да. Так будет лучше."
    cs_narrator "Семён сел с другой стороны стола."
    cs_sy "А мне что делать?"
    cs_narrator "Я подняла взгляд."
    cs_narrator "Улыбнулась."
    cs_ls "Для начала не мешать художнику."
    cs_narrator "Он закатил глаза."
    cs_sy "Прекрасно."
    cs_narrator "Я рассмеялась."
    cs_ls "Ладно. Что-нибудь тебе найдём."
    cs_sy "Вот это уже больше похоже на работу."
    cs_narrator "Мы принялись за дело."
    cs_narrator "Где-то за стеной клубов продолжали возиться с проводами Шурик и Электроник."
    cs_narrator "В медпункте Виола занималась своими обычными обязанностями."
    cs_narrator "А на площади пионеры готовились к вечернему мероприятию."
    cs_narrator "Лагерь жил."
    cs_narrator "Совершенно независимо от того, сколько странностей мне удастся обнаружить за день."
    cs_narrator "И, пожалуй, сейчас это казалось самым важным."
    cs_th "«Совёнок» не собирался останавливаться, пока я разбираюсь с его загадками."
    cs_th "Значит, придётся учиться жить здесь параллельно с расследованием."
    $ cs_day02_part04_complete = True
    label cs_check_part04_work_ready:
    pause 0.5
    return
