# -*- coding: utf-8 -*-
label cs_day02_reading_07c:
    $ save_name = "Чужая смена — Тишина на троих: О книге — если есть доверие"
    $ cs_part08_live = False
    $ cs_reading_live = True
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_07c:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя посмотрела на книгу."
    cs_narrator "Потом на пустой стул напротив."
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Можно?"
    cs_narrator "Я удивлённо подняла глаза."
    cs_ls "Конечно."
    cs_narrator "Она села."
    cs_narrator "Некоторое время Женя разглядывала обложку."
    cs_mz "Ну и как тебе?"
    cs_narrator "Я немного подумала."
    cs_ls "Хорошо написано. Но главный герой меня временами раздражает."
    cs_narrator "Женя сразу подняла взгляд."
    cs_mz "Чем?"
    cs_ls "Он всё время делает вид, что не понимает очевидных вещей. Хотя, по-моему, просто боится принять решение."
    cs_narrator "Женя кивнула."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вот! Я тоже об этом думала."
    cs_narrator "Я улыбнулась."
    cs_ls "Только автор, кажется, специально тянет с этим."
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
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Может быть. Но если бы он всё сразу решил, книга закончилась бы слишком быстро."
    cs_narrator "Дарья, до этого молча слушавшая нас, улыбнулась."
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
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Значит, половина сюжета держится на том, что люди не умеют нормально разговаривать?"
    cs_narrator "Я рассмеялась."
    cs_ls "Даш, это сейчас было очень точное литературное наблюдение."
    cs_narrator "Женя тоже улыбнулась."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Иногда действительно так."
    cs_narrator "Она немного подумала."
    cs_mz "Хотя мне нравится, что автор не делает персонажей идеальными."
    cs_narrator "Я кивнула."
    cs_ls "Согласна. Если человек постоянно поступает правильно, за ним быстро становится неинтересно наблюдать."
    cs_mz "Именно."
    cs_narrator "На некоторое время мы замолчали."
    cs_narrator "Женя посмотрела на книгу."
    cs_narrator "Потом на меня."
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
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А ты сама обычно много читаешь?"
    cs_narrator "Я пожала плечами."
    cs_ls "Периодами. Иногда могу за пару дней прочитать целую книгу, а потом месяц ничего не открывать."
    cs_mz "Почему?"
    cs_narrator "Я немного подумала."
    cs_ls "Другие дела. Рисование. Работа. Интернет."
    cs_narrator "Она задумчиво кивнула."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А мне наоборот. Если день прошёл без чтения, кажется, будто чего-то не хватает."
    cs_narrator "Я посмотрела на неё."
    cs_th "Вот теперь я действительно начинала её понимать."
    cs_narrator "Для меня таким занятием чаще было рисование."
    cs_narrator "Не обязательно ради результата."
    cs_narrator "Иногда просто хотелось сесть, взять планшет и несколько часов заниматься линиями."
    cs_narrator "Без чужих вопросов."
    cs_narrator "Без необходимости быть интересной кому-нибудь ещё."
    cs_ls "У меня с рисованием примерно так же."
    cs_narrator "Женя улыбнулась."
    cs_mz "Тогда понимаешь."
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_narrator "Мы снова немного помолчали."
    cs_narrator "И это молчание совершенно не казалось неловким."
    cs_narrator "Женя не пыталась немедленно продолжить разговор."
    cs_narrator "Я тоже."
    cs_narrator "Дарья спокойно читала рядом."
    cs_narrator "Через некоторое время Женя поднялась."
    cs_mz "Ладно. Мне ещё бумаги разобрать надо."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо."
    cs_narrator "Она сделала несколько шагов."
    cs_narrator "Потом остановилась."
    cs_mz "Соколова."
    cs_narrator "Я подняла голову."
    cs_ls "Да?"
    cs_narrator "Она немного помолчала."
    cs_mz "Можешь иногда приходить сюда просто почитать."
    cs_narrator "Я удивилась."
    cs_ls "Разве я не могу и так?"
    cs_narrator "Женя вздохнула."
    cs_mz "Можешь, конечно."
    cs_narrator "Потом поправила очки."
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
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Я имею в виду… не обязательно каждый раз приходить с вопросами про странные автобусы и другие загадки."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И улыбнулась."
    cs_ls "Поняла."
    cs_narrator "Немного помолчала."
    cs_ls "Спасибо."
    cs_narrator "Она кивнула."
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
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только не разговаривай на всю библиотеку."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Постараюсь."
    # cs_presence_keep: hide cs_zhenya
    $ cs_reading_cast = ["cs_darya"]
    cs_narrator "Женя вернулась за свой стол."
    # cs_director_begin: Zhenya finishes conversation and resumes work
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_d73dcb29fc:
    # cs_director_end
    cs_th "Ну вот."
    cs_th "Кажется, это и было настоящее приглашение."
    cs_narrator "Не на прогулку."
    cs_narrator "Не на какое-нибудь мероприятие."
    cs_narrator "Просто прийти и посидеть в тишине."
    cs_narrator "И, пожалуй, именно от Жени оно значило особенно много."
    $ cs_mz_reading_invite = True
    label cs_check_reading_invited:
    label cs_check_reading_desk_07c:
    pause 0.5
    return
