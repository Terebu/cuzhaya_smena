# -*- coding: utf-8 -*-
# Source: source/day01_part05.md.
label cs_day01_23:
    $ save_name = "Чужая смена — День 1: Знакомая история"
    $ renpy.music.set_volume(0.3,delay=1.0,channel="music")
    play music cs_day_music_think fadeout 2.0 fadein 2.5
    label cs_check_day01_part05_story:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_semen"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Несколько минут мы ели молча."
    cs_narrator "Потом Семён посмотрел на меня."
    show cs_semen serious pioneer normal at cs_semen_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты сказала, что знаешь этот лагерь."
    cs_narrator "Я отложила ложку."
    cs_ls "Да."
    cs_sy "И меня?"
    cs_narrator "Дарья чуть повернула голову."
    cs_narrator "Она уже знала, какой ответ последует."
    cs_narrator "Я — насколько странно он прозвучит."
    label cs_check_day01_part05_novel:
    cs_ls "У меня дома есть визуальная новелла. Компьютерная игра, в которой читают историю и иногда выбирают ответы."
    cs_sy "И?"
    cs_ls "Она называется «Бесконечное лето». В ней есть этот лагерь. Те же домики, та же вожатая, Славя. И парень по имени Семён, который садится зимой в автобус, а просыпается здесь."
    cs_narrator "Он перестал двигаться."
    cs_sy "Ты сейчас шутишь?"
    cs_ls "Нет."
    cs_narrator "Я впервые за весь обед пожалела, что у меня настолько хорошо получалось говорить ровным голосом."
    cs_narrator "Наверное, от этого объяснение звучало ещё хуже."
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Она назвала Славю по имени, прежде чем та представилась. И знала, куда идти к вожатой."
    cs_sy "Это ничего не доказывает."
    cs_ls "Согласна. Поэтому я и не предлагаю тебе сразу поверить."
    cs_narrator "Он посмотрел на меня внимательнее."
    cs_sy "Но ты ждала, что я буду здесь?"
    cs_ls "Допускала. Не знала, приехали мы вместо тебя или после. Ольга Дмитриевна сказала, что ты уже в лагере."
    cs_sy "Значит, ты знаешь, что будет дальше?"
    cs_narrator "Я медленно покачала головой."
    cs_ls "Знаю варианты знакомой мне истории. Это не одно и то же."
    cs_sy "Какие варианты?"
    cs_ls "Там события зависят от решений. Но самое важное сейчас другое: нас с Дарьей в этой истории не было."
    cs_narrator "Я кивнула на неё."
    cs_ls "А здесь мы есть. Уже одно это означает, что воспоминания об игре нельзя считать расписанием будущего."
    cs_narrator "Дарья чуть расслабила плечи."
    # cs_darya_variety: reaction
    show cs_darya explaining pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "То есть ты можешь ошибаться даже в том, что хорошо помнишь."
    cs_ls "Да."
    cs_narrator "Семён провёл ладонью по лицу."
    cs_sy "Если всё это правда, получается, я…"
    cs_narrator "Он не закончил."
    cs_narrator "Я не стала заканчивать за него."
    cs_ls "Сейчас передо мной человек, который сидит за столом, задаёт вопросы и так же хочет понять, где оказался. С этого и начнём."
    cs_narrator "Некоторое время он смотрел на меня."
    cs_narrator "Потом опустил взгляд на тарелку."
    cs_sy "Мне нужно подумать."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нам всем нужно."
    cs_narrator "Я кивнула."
    cs_ls "И не обязательно решать всё за один обед."
    cs_narrator "Семён наконец доел оставшееся."
    cs_narrator "Я постаралась дать ему несколько минут без новых сведений."
    cs_narrator "Для разнообразия."
    return
