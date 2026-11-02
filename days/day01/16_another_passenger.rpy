# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_16:
    $ save_name = u"Чужая смена — День 1: Ещё один пассажир"
    stop music fadeout 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mt", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Ольга Дмитриевна уже собиралась закончить разговор, но вдруг словно что-то вспомнила."
    cs_mt "Кстати, вы не первые новенькие."
    cs_narrator "Я подняла взгляд. Догадывалась, что услышу, но всё равно ждала с волнением."
    cs_ls "Да?"
    cs_mt "Вчера приехал ещё один молодой человек."
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 1.5 fadein 2.0
    cs_narrator "Дарья посмотрела на меня. Я постаралась сохранить невинный вид."
    cs_ls "Как интересно."
    label cs_check_day01_part04_passenger:
    cs_mt "Семён."
    stop music fadeout 1.0
    pause 1.0
    cs_th "Ну разумеется."
    label cs_check_day01_part04_silence:
    cs_narrator "Я медленно опустила взгляд."
    cs_ls "Ну конечно."
    cs_mt "Что?"
    cs_ls "Говорю, интересное совпадение."
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это тот самый?"
    cs_ls "Тот самый."
    cs_narrator "Ольга Дмитриевна нахмурилась."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Вы знакомы?"
    cs_ls "Нет."
    cs_mt "Тогда откуда ты знаешь, кто он?"
    cs_narrator "Я посмотрела ей прямо в глаза."
    cs_ls "Из того же источника, откуда мне известны ваши имена и расположение лагеря."
    cs_narrator "Повисла тишина."
    # cs_camp_emotion: text reaction
    show mt angry pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Ты опять за своё?"
    cs_ls "Сама не в восторге."
    cs_narrator "Я повернулась к Дарье."
    cs_ls "Значит, Семён уже сутки здесь."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
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
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Какой ещё истории?"
    cs_ls "Длинной. И местами весьма запутанной."
    cs_narrator "Я взглянула на часы в комнате."
    cs_ls "Обед ведь скоро?"
    # cs_camp_emotion: text reaction
    show mt smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Да. Пойдёмте, заодно познакомлю вас с остальными."
    cs_ls "Вот и замечательно."
    cs_narrator "Я направилась к двери."
    # cs_director_begin: REFLECTIVE_SHOT: Unanswered question about another passenger
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_ce7afeb1d8:
    # cs_director_end
    cs_th "Семён здесь. Значит, мы приехали не вместо него."
    cs_narrator "Но зачем мы появились на сутки позже?"
    stop music fadeout 2.0
    return
