# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_04:
    $ save_name = u"Чужая смена — День 1: Отражение"
    $ renpy.music.set_volume(0.65, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.65, delay=2.0, channel="ambience")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "И именно в этот момент мне пришло в голову кое-что ещё."
    # cs_director_begin: Hands and bus mirror
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_08af6135f7:
    # cs_director_end
    cs_narrator "Я опустила взгляд на свои руки."
    cs_narrator "Пальцы."
    cs_narrator "Кожа."
    cs_narrator "Ноги."
    cs_narrator "Одежда оставалась моей."
    cs_narrator "Но что-то неуловимо изменилось."
    cs_narrator "Я подошла к боковому зеркалу автобуса."
    label cs_check_day01_reflection:
    cs_narrator "Посмотрела на отражение."
    cs_narrator "Длинные фиолетовые волосы."
    cs_narrator "Зелёные глаза."
    cs_narrator "Знакомое лицо."
    cs_narrator "Моё."
    cs_narrator "Только…"
    cs_narrator "Я наклонилась ближе."
    cs_ls "Интересно."
    # cs_director_begin: Conversation at the mirror
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_94e3b0b768:
    # cs_director_end
    cs_narrator "Дарья подошла ко мне."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что теперь?"
    cs_ls "Кажется, я помолодела."
    cs_da "Насколько?"
    cs_ls "Не знаю. На несколько лет, наверное."
    cs_narrator "Я коснулась щеки, затем подбородка."
    cs_narrator "Отражение повторило движения."
    cs_ls "Потрясающе. Даже косметолог не понадобился."
    cs_da "Ты уверена?"
    cs_ls "Не особенно. Но паспорт у зеркала спрашивать бесполезно."
    cs_narrator "Я ещё раз посмотрела на своё лицо."
    cs_narrator "Внешне я по-прежнему оставалась собой."
    cs_narrator "Просто черты казались чуть моложе."
    cs_narrator "Слишком мало, чтобы делать окончательные выводы."
    cs_narrator "Но достаточно, чтобы насторожиться."
    cs_ls "Если это действительно связано с игрой, такое уже подозрительно похоже на канон."
    cs_da "На что?"
    cs_ls "Долго объяснять."
    cs_narrator "Я отошла от автобуса."
    cs_narrator "И тут вспомнила о телефоне."
    show screen cs_phone(0, "off")
    cs_narrator "Достала его из кармана."
    label cs_check_day01_phone:
    cs_narrator "Разумеется, экран оставался чёрным."
    cs_narrator "Нажала кнопку питания."
    cs_narrator "Ничего."
    cs_narrator "Повторила попытку."
    cs_narrator "Безрезультатно."
    cs_ls "Отлично."
    cs_narrator "Я машинально принялась искать пауэрбанк."
    cs_narrator "И почти сразу вспомнила, что оставила его дома."
    cs_narrator "Разумеется."
    cs_narrator "Зачем брать внешний аккумулятор, когда собираешься всего лишь на двадцать минут в супермаркет?"
    cs_th "Молодец, Лена. Предусмотрительность на высшем уровне."
    hide screen cs_phone
    cs_narrator "Дарья наблюдала за мной."
    cs_da "Связи нет?"
    cs_ls "Для начала неплохо было бы получить работающий телефон."
    cs_narrator "Я повертела аппарат в руке."
    cs_ls "Хотя, если он вдруг включится, первая фотография будет называться «Сходила за хлебом»."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "У тебя странные приоритеты."
    cs_ls "У меня двести сорок семь тысяч подписчиков. Кто-то должен документировать эту катастрофу."
    hide screen cs_phone
    cs_narrator "Я убрала телефон обратно в карман."
    cs_narrator "И вдруг остановилась."
    stop music fadeout 3.0
    label cs_check_day01_silence:
    cs_ls "Если они вообще сейчас существуют."
    pause 1.5
    cs_narrator "Последнюю фразу я произнесла гораздо тише."
    cs_narrator "Дарья ничего не ответила."
    cs_narrator "И за это я была ей благодарна."
    return
