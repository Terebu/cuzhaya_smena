# -*- coding: utf-8 -*-
label cs_day03_86:
    $ save_name = "Чужая смена — День 3: Новый человек. На двадцать секунд"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    cs_narrator "По дорожкам уже шли пионеры."
    cs_narrator "Кто-то направлялся к столовой."
    cs_narrator "Кто-то торопился от домиков."
    cs_narrator "Издали доносились голоса."
    cs_narrator "Солнце поднялось достаточно высоко, чтобы обычное утро постепенно превращалось в очередной жаркий летний день."
    cs_narrator "Я шагала рядом с Дарьей."
    cs_narrator "Старалась смотреть под ноги."
    cs_narrator "Причём настолько старательно, что она в какой-то момент это заметила."
    cs_da "Лен, ты теперь специально каждую ветку рассматриваешь?"
    cs_narrator "Я подняла голову."
    cs_ls "После вчерашнего решила пересмотреть отношение к растительному миру."
    cs_narrator "Она улыбнулась."
    cs_da "И как результаты?"
    cs_ls "Деревья по-прежнему вызывают доверие. Корни временно находятся под подозрением."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И вдруг вспомнила, что хотела кое-что проверить."
    cs_ls "Кстати, Даш."
    cs_da "Да?"
    cs_narrator "Я выпрямилась."
    cs_ls "Сегодня я решила стать более воспитанным человеком."
    show cs_darya thinking pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она остановилась."
    cs_narrator "Посмотрела на меня."
    cs_da "Сегодня?"
    cs_ls "Именно."
    cs_narrator "Она немного задумалась."
    cs_da "А вчера что мешало?"
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Вчера происходил процесс подготовки реформ."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "И в чём заключается сегодняшняя реформа?"
    cs_narrator "Я немного помолчала."
    cs_narrator "Потом сообщила:"
    cs_ls "До завтрака ни разу не подколоть Семёна."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Потом медленно улыбнулась."
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
    cs_narrator "Я замолчала."
    cs_narrator "Потом медленно кивнула."
    cs_ls "Хорошо. Засчитано."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Мы прошли ещё немного."
    cs_narrator "И именно в этот момент на дорожке впереди появился Семён."
    cs_th "Ну конечно."
    cs_th "Мироздание услышало моё заявление."
    cs_th "И решило немедленно провести независимую проверку."
    cs_narrator "Он шёл навстречу нам."
    cs_narrator "В пионерской форме."
    cs_narrator "С немного сонным выражением лица."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_enter
    label cs_check_day03_86_semen:
    cs_narrator "Заметив нас, остановился."
    cs_sy "О, привет."
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела на него."
    cs_narrator "Потом на Дарью."
    cs_narrator "Она посмотрела на меня с выражением человека, который уже приготовился наблюдать за провалом исторического эксперимента."
    cs_narrator "Я выпрямилась."
    cs_ls "Доброе утро, Семён."
    show cs_semen thinking pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Он прищурился."
    cs_sy "Доброе."
    cs_narrator "Пауза."
    cs_narrator "Он посмотрел на Дарью."
    cs_narrator "Потом на меня."
    cs_sy "Что-то случилось?"
    cs_narrator "Я удивлённо подняла бровь."
    cs_ls "А должно?"
    cs_sy "Ты поздоровалась и пока ни разу не попыталась меня задеть."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она уже улыбалась."
    cs_ls "Чудовищно. Теперь даже обычная вежливость вызывает подозрения."
    show cs_semen smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Семён усмехнулся."
    cs_sy "Просто непривычно."
    cs_narrator "Я кивнула."
    cs_ls "Понимаю. Третий день в лагере, а репутация уже сформирована."
    cs_narrator "Он рассмеялся."
    cs_narrator "Дарья тоже."
    cs_th "Так."
    cs_th "Пока держусь."
    cs_th "Удивительно."
    return
