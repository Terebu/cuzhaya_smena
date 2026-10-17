# -*- coding: utf-8 -*-
label cs_day02_26:
    $ save_name = "Чужая смена — День 2: Пять вольт без чуда"
    $ cs_part03_live = False
    $ cs_part04_live = True
    if not renpy.showing("bg int_clubs_male_day"):
        $ cs_director_scene("bg int_clubs_male_day")
        scene bg int_clubs_male_day
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
    # cs_presence_keep: hide cs
    show sh normal pioneer at cs_actor_left zorder 10
    show el normal pioneer at cs_actor_right zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    if renpy.music.get_playing() is None:
        play music "sound/music/smooth_machine.ogg" fadein 2.5
    $ renpy.music.set_volume(0.20, channel="music", delay=1.0)
    label cs_check_part04_s26:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sh", "el"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "В кружке ничего не изменилось."
    cs_narrator "Точнее, изменилось всё, что вчера ещё лежало на столе в относительно упорядоченном виде."
    cs_narrator "Теперь его поверхность занимали провода, измерительные приборы и небольшая самодельная конструкция, которую я не рискнула бы назвать зарядным устройством без соответствующего заключения специалистов."
    cs_narrator "Шурик сидел за столом, сосредоточенно рассматривая показания прибора."
    cs_narrator "Электроник стоял рядом."
    cs_narrator "Услышав дверь, оба повернулись."
    cs_el "О, привет! Мы как раз тебя вспоминали!"
    cs_narrator "Я посмотрела на стол."
    cs_narrator "Потом на них."
    cs_ls "Надеюсь, исключительно в рамках научной деятельности."
    show el grin pioneer at cs_actor_right zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Ага. Мы тут кое-что собрали!"
    cs_narrator "Шурик указал на небольшой блок."
    cs_sh "Источник питания. Напряжение регулируется, под нагрузкой работает стабильно."
    cs_narrator "Я подошла ближе."
    cs_ls "Уже неплохо."
    cs_narrator "Электроник улыбнулся."
    show el normal pioneer at cs_actor_right zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Мы вчера ещё немного посидели. Хотели попробовать сделать переходник, но с разъёмом ничего не получилось."
    cs_narrator "Я достала телефон."
    cs_narrator "Положила на свободный участок стола."
    cs_ls "Ожидаемо."
    # cs_director_begin: Semen joins the technical question
    $ cs_frame_focus(["sh", "el", "cs_semen"])
    with cs_sprite_change
    label cs_director_check_401d38087f:
    # cs_director_end
    cs_narrator "Семён заглянул через моё плечо."
    cs_sy "И что теперь?"
    cs_narrator "Шурик посмотрел на телефон."
    show sh serious pioneer at cs_actor_left zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Нужно понять, как правильно подключить питание. Сам разъём мне незнаком, а вскрывать устройство Лена запретила."
    cs_ls "И продолжает запрещать."
    cs_el "Мы даже не собирались!"
    cs_narrator "Шурик посмотрел на него."
    cs_narrator "Электроник немного помолчал."
    cs_el "Ну, почти."
    cs_narrator "Я усмехнулась."
    cs_ls "Приятно иметь дело с откровенными людьми."
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
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: Reverse shot for Darya, Shurik and Semen
    $ cs_frame_focus(["sh", "cs_semen", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_72aa9a23cc:
    # cs_director_end
    cs_narrator "Дарья подошла к столу."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Получается, проблема уже не в том, чтобы найти электричество?"
    cs_sh "Именно. Электричество есть. А вот безопасного способа подать его на это устройство пока нет."
    cs_narrator "Он указал на порт смартфона."
    cs_sh "Если подключить неправильно, можно испортить то, что находится внутри."
    cs_narrator "Я кивнула."
    cs_ls "Поэтому никаких опытов непосредственно на телефоне."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Может, подходящий провод где-нибудь найдётся?"
    cs_narrator "Я покачала головой."
    cs_ls "Сомневаюсь. Этот тип разъёма появился намного позже вашего оборудования."
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
    # cs_presence_keep: hide cs
    show sh serious pioneer at cs_actor_left zorder 10
    show el normal pioneer at cs_actor_right zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: Keep the technical reverse shot limited to three
    $ cs_frame_focus(["sh", "cs_semen", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_97a03e8a73:
    # cs_director_end
    cs_narrator "Шурик нахмурился."
    cs_sh "Тогда придётся искать другое решение."
    # cs_director_begin: Phone inspection after the technical discussion
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_22177c15d9:
    # cs_director_end
    cs_narrator "Я посмотрела на телефон."
    cs_narrator "Чёрный экран."
    cs_narrator "Ни одного признака жизни."
    cs_th "Ну что, Соколова."
    cs_th "Научно-техническая революция откладывается."
    cs_narrator "И всё же я не чувствовала особенного разочарования."
    cs_narrator "Вчера мне казалось, что отсутствие зарядки — почти неразрешимая проблема."
    cs_narrator "Сегодня хотя бы стало понятно, из каких частей она состоит."
    cs_narrator "Есть источник питания."
    cs_narrator "Есть устройство."
    cs_narrator "Между ними нет подходящего подключения."
    cs_narrator "Задача неприятная."
    cs_narrator "Но вполне определённая."
    # cs_director_begin: Return to engineers and Darya
    $ cs_frame_focus(["sh", "el", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_8513a3bcf0:
    # cs_director_end
    cs_ls "Ладно. Торопиться не будем."
    cs_narrator "Электроник удивился."
    show el surprise pioneer at cs_actor_right zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "А ты не расстроилась?"
    cs_narrator "Я пожала плечами."
    cs_ls "Немного. Но лучше ещё один день без телефона, чем окончательно испорченный телефон."
    cs_narrator "Шурик одобрительно кивнул."
    show sh normal_smile pioneer at cs_actor_left zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Вот именно."
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
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: Darya concludes the technical conversation; Semen listens offscreen
    $ cs_frame_focus(["sh", "el", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_c04cb9832e:
    # cs_director_end
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Значит, пока ничего?"
    cs_ls "Пока ничего."
    cs_narrator "Я взяла смартфон."
    cs_ls "Но заявка остаётся открытой."
    cs_narrator "Электроник рассмеялся."
    cs_el "Обязательно что-нибудь придумаем!"
    cs_narrator "Я улыбнулась."
    cs_ls "Только без героических подвигов с проводами."
    cs_sh "Договорились."
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
    # cs_presence_keep: hide cs
    show sh normal_smile pioneer at cs_actor_left zorder 10
    show el surprise pioneer at cs_actor_right zorder 10
    $ cs_part04_cast = ["sh", "el"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Мы ещё немного поговорили об инструментах, после чего стало ясно, что сегодня нам больше нечего здесь делать."
    # cs_director_begin: Companions plan the next errand
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_9b8b3479e0:
    # cs_director_end
    cs_narrator "Семён вспомнил об объявлении."
    cs_sy "Кстати, надо бы уточнить у Ольги Дмитриевны время музыкального вечера."
    cs_narrator "Я кивнула."
    cs_ls "Хорошая мысль."
    cs_sy "Я тогда схожу к ней, а вы пока можете подготовить рисунок."
    cs_da "Только не потеряй папку."
    cs_sy "Не потеряю."
    cs_ls "Напоминаю, товарищ Семён: утрата государственного художественного имущества карается общественным порицанием."
    cs_narrator "Он усмехнулся."
    cs_sy "Очень страшно."
    cs_narrator "Я улыбнулась."
    cs_ls "Мы ещё не утвердили полный перечень санкций."
    return
