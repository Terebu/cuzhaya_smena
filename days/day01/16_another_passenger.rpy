# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_16:
    $ save_name = u"Чужая смена — День 1: Ещё один пассажир"
    stop music fadeout 2.0
    cs_narrator "Ольга Дмитриевна уже собиралась закончить разговор, но вдруг словно что-то вспомнила."
    cs_mt "Кстати, вы не первые новенькие."
    cs_narrator "Я подняла взгляд."
    cs_narrator "Мне казалось, что я уже знаю продолжение."
    cs_narrator "Но услышать его всё равно оказалось неожиданно волнительно."
    cs_ls "Да?"
    cs_mt "Вчера приехал ещё один молодой человек."
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 1.5 fadein 2.0
    cs_narrator "Дарья сразу посмотрела на меня."
    cs_narrator "Я же постаралась сохранить максимально невинное выражение лица."
    cs_ls "Как интересно."
    label cs_check_day01_part04_passenger:
    cs_mt "Семён."
    stop music fadeout 1.0
    pause 1.0
    cs_th "Ну разумеется."
    label cs_check_day01_part04_silence:
    cs_narrator "Я медленно опустила взгляд."
    cs_ls "Прекрасно."
    cs_mt "Что?"
    cs_ls "Говорю, интересное совпадение."
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    cs_da "Это тот самый?"
    cs_narrator "Я едва заметно кивнула."
    cs_ls "Тот самый."
    cs_narrator "Ольга Дмитриевна нахмурилась."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    cs_mt "Вы знакомы?"
    cs_ls "Нет."
    cs_mt "Тогда откуда ты знаешь, кто он?"
    cs_narrator "Я посмотрела ей прямо в глаза."
    cs_ls "Из того же источника, откуда мне известны ваши имена и расположение лагеря."
    cs_narrator "Повисла тишина."
    # cs_camp_emotion: text reaction
    show mt angry pioneer at cs_actor_left
    cs_mt "Ты опять за своё?"
    cs_ls "Сама не в восторге."
    cs_narrator "Я повернулась к Дарье."
    cs_ls "Значит, Семён уже сутки здесь."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    cs_da "Это важно?"
    cs_ls "Очень."
    cs_da "Почему?"
    cs_narrator "Я поправила галстук."
    cs_ls "Теперь я хотя бы приблизительно понимаю, в какой точке истории мы оказались."
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 1.5 fadein 2.5
    cs_narrator "Ольга Дмитриевна посмотрела на меня ещё подозрительнее."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    cs_mt "Какой ещё истории?"
    cs_ls "Длинной. И местами весьма запутанной."
    cs_narrator "Я взглянула на часы в комнате."
    cs_ls "Обед ведь скоро?"
    # cs_camp_emotion: text reaction
    show mt smile pioneer at cs_actor_left
    cs_mt "Да. Пойдёмте, заодно познакомлю вас с остальными."
    cs_ls "Вот и замечательно."
    cs_narrator "Я направилась к двери."
    cs_th "Семён."
    cs_th "Значит, он действительно здесь."
    cs_th "В таком случае моя теория о том, что мы прибыли вместо него, только что отправилась в архив."
    cs_narrator "Но что означало наше появление спустя сутки после него?"
    cs_narrator "Этого я пока не знала."
    stop music fadeout 2.0
    return
