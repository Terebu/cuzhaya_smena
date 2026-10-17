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
    cs_narrator "Я пробежала мимо площади."
    cs_narrator "Памятник стоял на своём месте, величественный и совершенно равнодушный к моим личным проблемам."
    cs_th "Хорошо ему."
    cs_th "Никаких вопросов о возвращении домой."
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
    cs_narrator "Затем свернула к столовой."
    cs_narrator "Двери были закрыты."
    cs_narrator "Возле входа никого."
    cs_narrator "На секунду стало интересно, во сколько здесь вообще начинают готовить завтрак."
    cs_narrator "Но проверять это сейчас я не собиралась."
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
    cs_narrator "Дальше показались клубы."
    cs_narrator "Я автоматически повернула голову в сторону здания."
    cs_th "Шурик."
    cs_th "Электроник."
    cs_th "Надеюсь, вы хотя бы выспались перед очередной встречей с технологиями будущего."
    cs_narrator "Телефон оставался в домике."
    cs_narrator "Идея его зарядки за ночь никуда не исчезла."
    cs_narrator "А вот уверенности в том, что это вообще получится, стало меньше."
    cs_narrator "Незнакомый разъём."
    cs_narrator "Подходящий источник питания."
    cs_narrator "Отсутствие нужных деталей."
    cs_narrator "Даже если Шурик сумеет собрать всё необходимое, никто не гарантирует, что батарея пережила полную разрядку без последствий."
    cs_th "Ладно."
    cs_th "Этим займёмся после завтрака."
    cs_narrator "Я свернула на дорожку, ведущую к спортивной площадке."
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
    cs_narrator "И через несколько минут увидела турники."
    cs_narrator "Остановилась."
    cs_narrator "Посмотрела на перекладину."
    cs_th "О."
    cs_th "Вот это уже предложение."
    cs_narrator "Я подошла ближе."
    cs_narrator "Проверила, насколько прочно закреплена конструкция."
    cs_narrator "Несколько раз потянула перекладину вниз."
    cs_narrator "Выглядела вполне надёжно."
    cs_th "Отлично."
    cs_narrator "Я подпрыгнула и взялась за неё."
    cs_narrator "Первое подтягивание далось легко."
    cs_narrator "Второе."
    cs_narrator "Третье."
    cs_narrator "На следующих повторениях пришлось уже внимательнее следить за движением."
    cs_narrator "Я закончила подход, спрыгнула на землю и встряхнула кистями."
    cs_th "Нормально."
    cs_narrator "Несколько секунд постояла, восстанавливая дыхание."
    cs_narrator "Затем снова подошла к турнику."
    cs_narrator "Сделала ещё один подход."
    cs_narrator "После него немного повисела, подняла колени к груди и осторожно опустилась на землю."
    cs_narrator "Руки приятно устали."
    cs_narrator "Я отошла к краю площадки и начала растяжку."
    cs_th "Надо же."
    cs_th "Вчера я считала это место декорацией из компьютерной игры."
    cs_th "А сегодня уже использую местный спортивный инвентарь по прямому назначению."
    cs_narrator "Прогресс."
    cs_narrator "Хотя и весьма специфический."
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
    cs_narrator "Я выпрямилась."
    cs_narrator "Обернулась."
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
    cs_narrator "На дорожке стояла Ольга Дмитриевна."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом на турник."
    cs_narrator "Потом снова на меня."
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
    cs_narrator "Я кивнула."
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
    cs_narrator "Я кивнула."
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
    cs_th "Отлично."
    cs_th "Сама предложила."
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
    cs_narrator "Я посмотрела ей вслед."
    cs_narrator "Вчера эта женщина знала моё имя ещё до знакомства."
    cs_narrator "Сегодня спокойно обсуждала со мной турники и утреннюю зарядку."
    cs_narrator "И вела себя так, будто моё появление в лагере совершенно естественно."
    cs_th "Интересная женщина."
    cs_th "Вопросов к ней становится только больше."
    cs_narrator "Я снова взглянула на перекладину."
    cs_narrator "Пожалуй, хватит."
    cs_narrator "Впереди ещё оставалась пробежка обратно."
    cs_narrator "И одна дорожка, которую мне очень хотелось увидеть."
    return
