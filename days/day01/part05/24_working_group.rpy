# -*- coding: utf-8 -*-
# Source: source/day01_part05.md.
label cs_day01_24:
    $ save_name = "Чужая смена — День 1: Рабочая группа"
    stop music fadeout 2.0
    label cs_check_day01_part05_home:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_semen"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Дарья подвинула ко мне хлебницу."
    cs_narrator "Я взяла кусок и почти сразу отложила."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А домой из этой истории можно вернуться?"
    cs_narrator "Отвечать хотелось осторожнее, чем на все предыдущие вопросы."
    cs_ls "В знакомых мне вариантах истории возвращение возможно."
    cs_narrator "Он поднял глаза."
    cs_ls "Но я не знаю, работают ли они здесь. И не собираюсь выдавать какой-нибудь вариант концовки за проверенный способ."
    show cs_darya shrug pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Особенно если он зависит от того, что сделает кто-то другой."
    cs_ls "Именно."
    cs_narrator "Семён некоторое время смотрел на стакан."
    cs_sy "Тогда что нам делать?"
    cs_ls "Сначала выяснить, где мы и какая здесь дата. Потом сравнить то, что помним про дорогу. И искать возможность связаться с внешним миром."
    show cs_darya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Без того, чтобы каждый по отдельности куда-нибудь уходил?"
    cs_ls "Желательно."
    cs_narrator "Я посмотрела на обоих."
    cs_ls "И ещё. Если я говорю «помню из игры», это пока только источник предположения. Если мы сами что-то увидели — уже наблюдение. Лучше их не смешивать."
    cs_narrator "Семён чуть кивнул."
    show cs_semen grateful pioneer normal at cs_semen_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Звучит разумно."
    show cs_darya shrug pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Записи бы тоже не помешали."
    cs_ls "Как только найдём бумагу."
    show cs_semen serious pioneer far at cs_semen_far_right
    # cs_composition: regroup
    show mt normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show cs_darya thinking pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    with None
    label cs_check_day01_part05_olga:
    cs_narrator "Рядом со столом остановилась Ольга Дмитриевна."
    cs_narrator "Я заметила её раньше, чем Семён успел задать следующий вопрос."
    show mt smile pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Ну что, познакомились?"
    cs_ls "Да. Нашли несколько общих тем."
    show mt normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Судя по вашим лицам, очень серьёзных."
    show cs_semen tie_touch pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Просто разговариваем."
    cs_narrator "Вожатая посмотрела на него."
    cs_narrator "Потом на нас с Дарьей."
    show mt normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Разговаривайте. Только обед не пропускайте. Девочки, ваш домик уже готов, после еды Славя вас проводит."
    show cs_darya smile pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Спасибо."
    show mt normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "А ты, Семён, не забудь: после обеда мне понадобится твоя помощь."
    cs_sy "Хорошо."
    # cs_presence_keep: hide mt
    # cs_composition: regroup
    show cs_darya smile pioneer far at cs_darya_far_left
    show cs_semen tie_touch pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она ещё раз оглядела стол и пошла дальше."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["mt"])
    with cs_sprite_leave
    label cs_director_check_40706f08b7:
    # cs_director_end
    cs_narrator "Мы подождали, пока она отойдёт."
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ей вы про автобус рассказали?"
    cs_ls "Про прибытие — да. Про всё остальное пока нет."
    cs_narrator "Дарья посмотрела вслед вожатой."
    show cs_darya worried pioneer far at cs_darya_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лучше сначала самим понять, что можно объяснить."
    cs_narrator "Семён помолчал."
    cs_narrator "Затем кивнул."
    show cs_semen grateful pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Если что-нибудь узнаю, скажу вам."
    cs_da "Мы тоже."
    cs_narrator "Я поставила локти на стол и сложила ладони."
    $ renpy.music.set_volume(0.35,delay=1.0,channel="music")
    play music cs_day_music_home fadeout 2.0 fadein 2.5
    label cs_check_day01_part05_agreement:
    cs_ls "Значит, ищем ответы вместе. Без обещаний, что завтра всё выяснится."
    cs_sy "Вместе."
    show cs_darya smile pioneer far at cs_darya_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Договорились."
    cs_narrator "Я позволила себе немного улыбнуться."
    cs_ls "Рабочая группа сформирована. Председателя выбирать не будем."
    show cs_darya amused pioneer far at cs_darya_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья усмехнулась."
    cs_narrator "Семён тоже, хотя улыбка получилась не особенно уверенной."
    cs_narrator "Тревога никуда не делась."
    cs_narrator "Зато теперь её не приходилось держать при себе целиком."
    cs_narrator "Я посмотрела на стакан с немного остывшим компотом."
    cs_th "Автобус привёз нас по отдельности."
    cs_th "Но искать выход поодиночке уже необязательно."
    return
