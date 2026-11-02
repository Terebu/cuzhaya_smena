# -*- coding: utf-8 -*-
label cs_day03_86:
    $ save_name = "Чужая смена — День 3: Новый человек. На двадцать секунд"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    cs_narrator "По дорожкам уже шли пионеры. Кто-то направлялся к столовой. Кто-то торопился от домиков. Издали доносились голоса."
    cs_narrator "Солнце поднялось достаточно высоко, чтобы обычное утро постепенно превращалось в очередной жаркий летний день. Я шагала рядом с Дарьей. Старалась смотреть под ноги. Причём настолько старательно, что она в какой-то момент это заметила."
    cs_da "Лен, ты теперь специально каждую ветку рассматриваешь?"
    cs_narrator "Я подняла голову."
    cs_ls "После вчерашнего решила пересмотреть отношение к растительному миру."
    cs_narrator "Она улыбнулась."
    cs_da "И как результаты?"
    cs_ls "Деревья по-прежнему вызывают доверие. Корни временно находятся под подозрением."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась. Я посмотрела на неё. И вдруг вспомнила, что хотела кое-что проверить."
    cs_ls "Кстати, Даш."
    cs_da "Да?"
    cs_narrator "Я выпрямилась."
    cs_ls "Сегодня я решила стать более воспитанным человеком."
    show cs_darya thinking pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она остановилась. Посмотрела на меня."
    cs_da "Сегодня?"
    cs_ls "Именно."
    cs_narrator "Она немного задумалась."
    cs_da "А вчера что мешало?"
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Вчера происходил процесс подготовки реформ."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_da "И в чём заключается сегодняшняя реформа?"
    cs_narrator "Я помолчала. Потом сообщила:"
    cs_ls "До завтрака ни разу не подколоть Семёна."
    cs_narrator "Дарья посмотрела на меня. Потом медленно улыбнулась."
    cs_da "Не получится."
    cs_narrator "Я возмутилась."
    cs_ls "Почему такое недоверие?"
    cs_da "Потому что я видела, как вы вчера разговаривали."
    cs_ls "Это было вчера."
    cs_da "И что изменилось?"
    cs_narrator "Я подняла палец."
    cs_ls "Сегодня я новый человек."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья усмехнулась."
    cs_da "Угу."
    cs_narrator "Я прищурилась."
    cs_ls "Твой скептицизм ранит."
    cs_narrator "Она посмотрела на повязку."
    cs_da "Надеюсь, не настолько, чтобы снова идти к Виоле."
    cs_narrator "Я замолчала. Потом медленно кивнула."
    cs_ls "Хорошо. Засчитано."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась. Мы прошли ещё немного. И именно в этот момент на дорожке впереди появился Семён."
    cs_th "Ну конечно. Мироздание услышало моё заявление. И решило немедленно провести независимую проверку."
    cs_narrator "Он шёл навстречу нам. В пионерской форме. С немного сонным выражением лица."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_enter
    label cs_check_day03_86_semen:
    cs_narrator "Заметив нас, остановился."
    cs_sy "О, привет."
    cs_narrator "Я остановилась. Посмотрела на него, потом на Дарью. Она посмотрела на меня с выражением человека, который уже приготовился наблюдать за провалом исторического эксперимента."
    cs_narrator "Я выпрямилась."
    cs_ls "Доброе утро, Семён."
    show cs_semen thinking pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Он прищурился."
    cs_sy "Доброе."
    cs_narrator "Пауза."
    cs_narrator "Он посмотрел на Дарью, потом на меня."
    cs_sy "Ты сегодня рано."
    cs_narrator "Я удивлённо подняла бровь."
    cs_ls "Уже успела прогуляться."
    cs_sy "Я ещё не проснулся, а вы уже по лагерю гуляете."
    cs_narrator "Я посмотрела на Дарью. Она уже улыбалась."
    cs_ls "Можем помолчать до завтрака. Если очень попросишь."
    show cs_semen smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Семён усмехнулся."
    cs_sy "Думаешь, получится?"
    cs_ls "Слишком поздно. Ты уже начал разговор."
    cs_narrator "Он рассмеялся. Дарья тоже."
    cs_th "Так. Пока держусь. Удивительно."
    return
