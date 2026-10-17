# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_03:
    $ save_name = u"Чужая смена — День 1: Не просто игра"
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    play music cs_day_music_doubt fadeout 2.0 fadein 3.0
    $ renpy.music.set_volume(0.35, delay=2.0, channel="ambience")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Впервые выражение её лица заметно изменилось."
    cs_da "Насколько хорошо?"
    cs_narrator "Я начала загибать пальцы."
    cs_ls "Примерное расположение зданий. Местные жители. Распорядок дня. Некоторые события."
    cs_narrator "Я ненадолго задумалась."
    cs_ls "Люди, с которыми лучше не ссориться. И люди, которым не стоит безоговорочно доверять."
    cs_narrator "Пауза."
    cs_ls "А ещё здесь должна быть кошкодевочка."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Разумеется."
    cs_ls "Я серьёзно."
    # cs_darya_stage: present in story
    show cs_dasha_winter worried normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это меня и беспокоит."
    # cs_director_begin: REFLECTIVE_SHOT: Rules of the remembered game
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_73161bfb32:
    # cs_director_end
    cs_narrator "Я снова повернулась к лагерю."
    cs_narrator "Ещё несколько минут назад он выглядел просто уютным, немного старомодным местом."
    cs_narrator "Теперь всё воспринималось иначе."
    cs_narrator "Потому что я кое-что знала."
    cs_narrator "При первом прохождении «Бесконечного лета» можно довольно долго считать «Совёнок» обычным пионерлагерем, в который главный герой каким-то образом попал из будущего."
    cs_narrator "У меня такой роскоши не было."
    cs_narrator "Я помнила, что события здесь могут повторяться."
    cs_narrator "Что один и тот же человек способен оказаться в совершенно разных обстоятельствах."
    cs_narrator "Что некоторые обитатели лагеря знают куда больше, чем говорят."
    cs_narrator "И что автобус номер четыреста десять — далеко не обычный общественный транспорт."
    # cs_director_begin: Return to direct interaction: Rules of the remembered game
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_9a7409ab4c:
    # cs_director_end
    cs_narrator "Я медленно вдохнула."
    cs_ls "Так."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что будем делать?"
    cs_ls "Для начала не паниковать."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты нервничаешь."
    cs_ls "Я заметила."
    cs_narrator "Я ещё раз посмотрела на ворота."
    cs_ls "Но пока предпочитаю считать происходящее крайне неудачно организованной экскурсией."
    # cs_darya_variety: reaction
    show cs_dasha_winter smile normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо усмехнулась."
    cs_narrator "Я стянула свитер."
    cs_narrator "Под ним осталась футболка."
    cs_narrator "Стало немного легче."
    cs_narrator "Куртку и свитер пришлось связать вместе и перекинуть через плечо."
    cs_ls "Во-вторых, нужно понять, насколько здешний лагерь соответствует тому, который я знаю."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Здешний?"
    cs_ls "Вот здесь начинается самое интересное."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему-то я не удивлена."
    cs_ls "Если правила те же, этот лагерь может быть не единственным."
    cs_narrator "Дарья повернулась ко мне."
    # cs_darya_stage: present in story
    # cs_darya_variety: reaction
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "В каком смысле?"
    cs_narrator "Я кивнула на ворота."
    cs_ls "В самом буквальном. Возможно, существует несколько таких мест. И не факт, что во всех события развиваются одинаково."
    cs_narrator "Она некоторое время молчала."
    # cs_darya_variety: reaction
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И ты узнала об этом из игры?"
    cs_ls "Да."
    cs_da "Которая существовала в твоём мире?"
    cs_ls "Совершенно верно."
    cs_da "А теперь мы оказались в месте, которое выглядит точно так же?"
    cs_ls "Пока совпадений достаточно для весьма неприятных выводов."
    cs_narrator "Дарья задумалась."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда я вижу два возможных объяснения."
    cs_ls "Слушаю."
    cs_da "Либо твоя игра каким-то образом описывала место, существующее независимо от неё."
    cs_narrator "Я кивнула."
    cs_ls "А второе?"
    cs_da "Либо происходящее здесь формируется на основе того, что тебе известно."
    stop music fadeout 2.0
    pause 1.5
    cs_narrator "Я замолчала."
    cs_narrator "Это предположение мне совершенно не понравилось."
    cs_narrator "Я посмотрела на лагерь."
    cs_narrator "На собственные руки."
    cs_narrator "На Дарью."
    cs_ls "Спасибо. Теперь у нас ещё и философская проблема с реальностью."
    cs_da "Ты спросила."
    cs_ls "Я уже жалею."
    cs_narrator "Она чуть пожала плечами."
    return
