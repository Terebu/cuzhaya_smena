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
    cs_narrator "Где-то там жили Алиса, Лена Тихонова, Ульяна, Мику, Женя, Виола, Электроник, Шурик. Люди, которых я знала как персонажей."
    cs_narrator "И, возможно, Семён. Но главного я не знала."
    cs_th "Мы приехали вместо него? Или вместе с ним?"
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
    cs_ls "…чью роль в этой истории теперь играет автобус."
    pause 1.0
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.65, channel="sound")
    play sound cs_day_sfx_horn
    label cs_check_day01_part03_horn:
    cs_narrator "Раздался горн. На дорожках появились пионеры, направлявшиеся к столовой."
    $ renpy.music.set_volume(0.5, delay=1.0, channel="ambience")
    cs_narrator "Ольга Дмитриевна посмотрела на часы."
    cs_mt "Скоро обед. Потом разберёмся, куда вас определить."
    cs_narrator "Я повернулась."
    cs_ls "В смысле «куда»?"
    cs_mt "В отряд."
    cs_narrator "Я остановилась, потом улыбнулась."
    cs_ls "Подождите."
    cs_narrator "Вожатая заранее насторожилась."
    cs_mt "Что ещё?"
    cs_ls "То есть вы сейчас действительно предлагаете нам здесь жить?"
    cs_mt "Пока не выясним, откуда вы взялись, куда ещё вас девать?"
    cs_narrator "Мы с Дарьей переглянулись."
    cs_ls "Ну что."
    cs_narrator "Я оглядела свой галстук, рубашку, летний лагерь за окном."
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_everyday fadeout 1.5 fadein 2.5
    cs_ls "Сходила за продуктами. Вернусь, видимо, к следующей пятилетке."
    pause 1.0
    cs_th "Молодец, Лена. Обычная двадцатиминутная поездка. Никаких непредвиденных обстоятельств."
    return
