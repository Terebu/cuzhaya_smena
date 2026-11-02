# -*- coding: utf-8 -*-
label cs_day02_04:
    $ save_name = "Чужая смена — День 2: Турники и советская физкультура"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day at cs_early_morning
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    label cs_check_new_d2_s04:
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day at cs_early_morning
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
    with Dissolve(0.8)
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я пробежала мимо площади. Памятник стоял на своём месте, величественный и совершенно равнодушный к моим личным проблемам."
    cs_th "Хорошо ему. Никаких вопросов о возвращении домой."
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day at cs_early_morning
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
    with Dissolve(0.8)
    cs_narrator "Затем свернула к столовой. Двери ещё были закрыты."
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day at cs_early_morning
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
    with Dissolve(0.8)
    cs_narrator "Дальше показались клубы. Я автоматически повернула голову в сторону здания."
    cs_th "Шурик. Электроник. Надеюсь, вы хотя бы выспались перед очередной встречей с технологиями будущего."
    cs_narrator "Телефон остался в домике. После завтрака всё равно придётся вернуться к вопросу зарядки. Я свернула на дорожку, ведущую к спортивной площадке."
    $ cs_director_scene("bg ext_playground_day")
    scene bg ext_playground_day at cs_early_morning
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
    with Dissolve(0.8)
    label cs_check_new_d2_sport:
    cs_narrator "За спортивной площадкой стояли турники. Я проверила перекладину. Сделала два подхода, спрыгнула на землю и перешла к растяжке."
    cs_th "Вчера это был фон из игры. Сегодня — мой турник."
    cs_narrator "Я потянулась к носку, когда за спиной раздался голос:"
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
    cs_mt "Лена?"
    cs_narrator "Я выпрямилась. Обернулась."
    $ cs_olga_seen = True
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt surprise pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "На дорожке стояла Ольга Дмитриевна. Перевела взгляд с меня на турник."
    cs_ls "Доброе утро, Ольга Дмитриевна."
    label cs_check_new_d2_olga:
    cs_mt "Доброе. А ты что здесь делаешь в такую рань?"
    cs_narrator "Я указала на перекладину."
    cs_ls "Провожу добровольные физкультурно-оздоровительные мероприятия."
    cs_narrator "Она приподняла бровь."
    cs_mt "Я вижу, что занимаешься. Почему до подъёма?"
    cs_ls "Рано проснулась. Решила не будить Дашу."
    cs_narrator "Ольга Дмитриевна посмотрела на часы."
    cs_mt "И давно ты здесь?"
    cs_ls "Минут десять. До этого бегала по дорожкам."
    cs_mt "Одна?"
    cs_ls "Да. Но далеко не уходила."
    cs_narrator "Она несколько секунд смотрела на меня."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt smile pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Вообще-то хорошо, что любишь спорт. Только смотри под ноги. После ночи дорожки ещё сырые."
    cs_ls "Уже заметила."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt normal pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "И не переусердствуй. Завтрак скоро, а у тебя впереди целый день."
    cs_narrator "Я усмехнулась."
    cs_ls "Вы так говорите, будто у вас на меня уже есть планы."
    cs_narrator "Ольга Дмитриевна улыбнулась."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt smile pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "А ты как думала? В лагере без дела долго не сидят."
    cs_th "Вот теперь немного тревожно."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt smile pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Предупреждение принято."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt surprise pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Даша где?"
    cs_ls "Спит. Я её предупредила, что выйду."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt normal pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "И правильно. К общему подъёму возвращайся, чтобы не опоздать."
    cs_ls "Хорошо."
    cs_narrator "Она собиралась уходить, но ненадолго задержалась."
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
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt smile pioneer at cs_actor_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "А вообще молодец. Не каждый согласится добровольно заниматься физкультурой с утра."
    cs_narrator "Я улыбнулась."
    cs_ls "Спасибо. Только Семёну не рассказывайте. Ещё заставит проводить для него занятия."
    cs_narrator "Ольга Дмитриевна рассмеялась."
    cs_mt "Вот и была бы тебе работа."
    cs_th "Отлично. Сама предложила."
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
    with Dissolve(0.4)
    cs_narrator "Она пошла дальше по дорожке."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["mt"])
    with cs_sprite_leave
    label cs_director_check_cd3f6ba0fb:
    # cs_director_end
    cs_narrator "Я посмотрела ей вслед. Вчера она знала моё имя ещё до знакомства. А сейчас обсуждала со мной зарядку, будто я всегда здесь жила."
    cs_th "Вопросов к ней становится только больше."
    cs_narrator "Я снова посмотрела на турник. Пожалуй, хватит. Впереди ещё оставалась пробежка обратно. И одна дорожка, которую мне очень хотелось увидеть."
    return
