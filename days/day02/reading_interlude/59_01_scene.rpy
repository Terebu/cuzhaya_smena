# -*- coding: utf-8 -*-
label cs_day02_reading_01:
    $ save_name = "Чужая смена — Тишина на троих: Необязательные разговоры"
    $ cs_part08_live = False
    $ cs_reading_live = True
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    play music "sound/music/my_daily_life.ogg" fadein 2.0
    $ renpy.music.set_volume(0.11, channel="music", delay=1.0)
    label cs_check_reading_01:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После разговора с Семёном мы ещё немного прошлись по площади."
    cs_narrator "Я не стала никого искать."
    if cs_talked_mz_square_day2:
        cs_narrator "Не стала догонять Женю, с которой мы только что поговорили на площади."
    else:
        cs_narrator "Не стала догонять Женю, которую незадолго до этого заметила с книгами."
    cs_narrator "Не предложила Дарье заглянуть к Шурику."
    cs_narrator "И даже не попыталась придумать ещё один способ проверить дорогу, из-за которой сегодня у нас и без того хватило впечатлений."
    cs_narrator "Вместо этого я просто шла."
    cs_narrator "Медленно."
    cs_narrator "Глядя под ноги."
    cs_narrator "Последнее, разумеется, стало вынужденной мерой после знакомства с местной растительностью."
    cs_narrator "Дарья шагала рядом."
    cs_narrator "Иногда поглядывала на мой перевязанный локоть, но ничего не говорила."
    cs_narrator "И я была ей за это благодарна."
    cs_th "Если честно, мне уже самой немного надоело быть главным происшествием дня."
    cs_narrator "Мы свернули на знакомую дорожку."
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Впереди виднелась библиотека."
    cs_narrator "Я посмотрела на её окна."
    cs_narrator "И неожиданно поняла, что хочу именно туда."
    cs_narrator "Не за картами."
    cs_narrator "Не за старым каталогом."
    cs_narrator "И даже не ради очередного разговора с Женей."
    cs_narrator "Просто туда, где можно сесть и некоторое время ничего не объяснять."
    cs_ls "Даш, кажется, я нашла себе занятие до ужина."
    cs_narrator "Она повернулась."
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Какое?"
    cs_narrator "Я кивнула в сторону библиотеки."
    cs_ls "Хочу немного почитать."
    cs_narrator "Дарья посмотрела на здание."
    cs_narrator "Потом снова на меня."
    cs_da "Просто почитать?"
    cs_narrator "Я усмехнулась."
    cs_ls "Да. Представляешь, я иногда так делаю."
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "После сегодняшнего дня я уже готова ко всему."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Никаких расследований. Никаких приключений. Даже не собираюсь никого расспрашивать."
    cs_narrator "Она слегка улыбнулась."
    cs_da "Звучит почти неправдоподобно."
    cs_ls "Вот и проверим."
    cs_narrator "Дарья ненадолго задумалась."
    cs_da "Тогда я сначала зайду в домик. Хочу попить воды и немного отдохнуть."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо."
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Потом найду тебя здесь?"
    cs_ls "Если не засну над книгой."
    cs_narrator "Она улыбнулась."
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не переутомляйся."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Чтением?"
    cs_da "Я уже ничему не удивлюсь."
    cs_narrator "Мы рассмеялись."
    # cs_presence_keep: hide cs_darya
    $ cs_reading_cast = []
    label cs_check_reading_darya_left:
    cs_narrator "Дарья направилась к домикам."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_darya"])
    with cs_sprite_leave
    label cs_director_check_af997fb038:
    # cs_director_end
    cs_narrator "Я осталась на дорожке."
    cs_narrator "Некоторое время смотрела на библиотеку."
    cs_th "Ну что, Соколова."
    cs_th "Один день без телефона ты уже пережила."
    cs_th "Второй, судя по всему, тоже переживёшь."
    cs_th "Попробуй теперь ещё и полчаса провести без разговоров."
    cs_narrator "Я поправила галстук."
    cs_narrator "И направилась к двери."
    return
