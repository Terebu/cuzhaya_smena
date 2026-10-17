# -*- coding: utf-8 -*-
label cs_day01_60:
    $ save_name = "Чужая смена — День 1: Человек за столом"
    label cs_check_d1_s60:
    play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Она собрала газеты в ровную стопку."
    cs_narrator "Женя оставила газеты возле себя. Я поймала себя на желании немедленно помочь и остановилась: после такого рассказа можно было хотя бы не трогать чужие вещи без спроса."
    cs_ls "Мне не нужно, чтобы ты сейчас согласилась со всем."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Хорошо. Потому что соглашаться я пока не собираюсь."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда мы хотя бы правильно друг друга поняли."
    cs_narrator "В её голосе не было обиды. От этого разговор почему-то стал легче, хотя убедительнее наша история не сделалась."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ты там про меня многое знаешь?"
    cs_narrator "Я поняла, что вопрос был важнее всех предыдущих."
    cs_ls "Про героиню той истории — кое-что. Про тебя — почти ничего."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Но сравнивать будешь."
    cs_ls "Наверное. Мне трудно совсем перестать узнавать знакомое. Но я постараюсь не делать из этого выводов за тебя."
    cs_narrator "Женя помолчала."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда не рассказывай, что я должна сказать или сделать. Даже если тебе кажется, что знаешь."
    cs_ls "Хорошо."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И не нужно проверять на мне свои воспоминания."
    cs_ls "Это тоже хорошо."
    cs_narrator "Я ответила без привычного добавления. Кажется, она заметила."
    cs_narrator "Дарья отошла к полке и поставила на место книгу, которую держала всё это время. Женя проследила за её рукой, убедилась, что корешок оказался там, где нужно, и немного расслабилась."
    if cs_friend_mz >= 1:
        show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Книги сегодня вы разобрали нормально. С этим, по крайней мере, разобрались."
        cs_ls "Предлагаю пока оценивать нас по книгам."
        show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Так и собираюсь."
    else:
        show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Если завтра придёте ещё, сначала говорите, что ищете. Я покажу, где лежит."
        cs_ls "Договорились."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Женя, можно попросить тебя пока не пересказывать это остальным?"
    cs_narrator "Женя подняла глаза."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Не потому, что мы хотим устроить тайный клуб. Просто у нас самих ещё нет нормального объяснения."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Сплетни я не собираю. Но если вам станет плохо, я позову вожатую."
    cs_ls "Да. Конечно."
    cs_narrator "Обещания хранить нашу тайну любой ценой не прозвучало. И требовать его от человека, который знал нас меньше часа, было бы довольно нагло."
    cs_narrator "Женя встала."
    show cs_zhenya shy pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Всё, на сегодня хватит. Завтра приходите за книгами. Можно даже без путешествий во времени."
    cs_ls "Постараемся выбрать более короткий маршрут."
    cs_narrator "Она посмотрела на меня поверх очков."
    cs_narrator "Я поднялась, поставила стул на место и на этот раз удержалась от комментария."
    return
