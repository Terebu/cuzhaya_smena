# -*- coding: utf-8 -*-
# Source: source/day01_part03.md.
label cs_day01_14:
    $ save_name = u"Чужая смена — День 1: Третий лишний"
    # cs_presence_keep: hide sl
    show mt normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 1.5 fadein 3.0
    $ renpy.music.set_volume(0.28, delay=1.0, channel="ambience")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mt", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    # cs_director_begin: REFLECTIVE_SHOT: Camp seen through the window and absent protagonist
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_894164c81a:
    # cs_director_end
    cs_narrator "За стеклом виднелся залитый солнцем лагерь."
    cs_narrator "Где-то там уже жили все те люди, которых я знала как персонажей."
    cs_narrator "Алиса."
    cs_narrator "Лена."
    cs_narrator "Ульяна."
    cs_narrator "Мику."
    cs_narrator "Женя."
    cs_narrator "Виола."
    cs_narrator "Электроник."
    cs_narrator "Шурик."
    cs_narrator "И где-то, возможно, существовал Семён."
    cs_narrator "Вот это было особенно интересно."
    cs_narrator "Потому что я совершенно не знала главного."
    cs_th "Мы приехали вместо него?"
    cs_th "Или вместе с ним?"
    cs_narrator "Я подошла к окну."
    cs_narrator "На площади вдали мелькали пионеры."
    # cs_director_begin: Return to direct interaction: Camp seen through the window and absent protagonist
    $ cs_frame_focus(["mt", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_1b254a9f1e:
    # cs_director_end
    cs_ls "Если сейчас ещё и Семён где-нибудь ходит…"
    cs_narrator "Дарья встала рядом."
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Тогда нас здесь уже минимум трое, кто не должен здесь находиться."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А если его нет?"
    cs_ls "Тогда ещё интереснее."
    cs_da "Почему?"
    cs_narrator "Я снова посмотрела на лагерь."
    cs_ls "Потому что тогда возникает вопрос…"
    cs_narrator "Ненадолго замолчала."
    cs_ls "…чью роль в этой истории теперь играет автобус."
    pause 1.0
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.65, channel="sound")
    play sound cs_day_sfx_horn
    label cs_check_day01_part03_horn:
    cs_narrator "Снаружи раздался сигнал горна."
    cs_narrator "Практически сразу лагерь ожил."
    cs_narrator "Из домиков начали выходить люди."
    cs_narrator "Где-то послышались голоса."
    cs_narrator "На дорожках появились пионеры, направлявшиеся к столовой."
    $ renpy.music.set_volume(0.5, delay=1.0, channel="ambience")
    cs_narrator "Ольга Дмитриевна посмотрела на часы."
    cs_mt "Скоро обед. Потом разберёмся, куда вас определить."
    cs_narrator "Я повернулась."
    cs_ls "В смысле «куда»?"
    cs_mt "В отряд."
    cs_narrator "Я остановилась."
    cs_narrator "Затем медленно улыбнулась."
    cs_ls "Подождите."
    cs_narrator "Ольга Дмитриевна посмотрела на меня с выражением человека, который уже заранее подозревает, что услышит что-нибудь необычное."
    cs_mt "Что ещё?"
    cs_ls "То есть вы сейчас действительно предлагаете нам здесь жить?"
    cs_mt "Пока не выясним, откуда вы взялись, куда ещё вас девать?"
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Я развела руками."
    cs_ls "Ну что."
    cs_narrator "Потом опустила взгляд на красный галстук."
    cs_narrator "На белую рубашку."
    cs_narrator "На летний лагерь за окном."
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_everyday fadeout 1.5 fadein 2.5
    cs_narrator "И совершенно серьёзно добавила:"
    cs_ls "Сходила за продуктами. Вернусь, видимо, к следующей пятилетке."
    pause 1.0
    cs_th "Молодец, Лена."
    cs_th "Обычная двадцатиминутная поездка."
    cs_th "Никаких непредвиденных обстоятельств."
    return
