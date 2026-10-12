# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_15:
    $ save_name = u"Чужая смена — День 1: Две новенькие"
    hide screen cs_day01_pending
    hide screen cs_phone
    $ day_time()
    $ persistent.sprite_time = "day"
    window show dissolve
    if not renpy.showing("bg int_house_of_mt_day"):
        scene bg int_house_of_mt_day with dissolve
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_daily fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.25, delay=1.0, channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_cabin:
        play ambience cs_day_cabin fadeout 1.0 fadein 2.0
    hide mt
    show mt normal pioneer at cs_actor_left
    label cs_check_day01_part04_housing:
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_narrator "Ольга Дмитриевна ещё раз окинула нас взглядом."
    cs_narrator "Сначала меня."
    cs_narrator "Потом Дарью."
    cs_narrator "Затем — оставшуюся на стуле гору моей зимней одежды."
    cs_mt "Значит, пока решим так. Остаётесь в лагере. После обеда разберёмся с остальным."
    cs_narrator "Я подняла руку."
    cs_ls "Есть одно пожелание."
    cs_narrator "По выражению её лица было видно, что после знакомства со мной слово «пожелание» уже начало вызывать некоторую настороженность."
    cs_mt "Какое?"
    cs_narrator "Я указала на Дарью."
    cs_ls "Домик нам, пожалуйста, один на двоих."
    cs_narrator "Дарья повернула голову."
    # cs_darya_stage: present in story
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    label cs_check_darya_housing_talk:
    cs_da "Ты даже не спросила меня."
    cs_ls "Предпочитаешь жить с совершенно незнакомым человеком?"
    cs_narrator "Она задумалась буквально на секунду."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_da "Продолжай."
    cs_narrator "Я снова посмотрела на вожатую."
    label cs_check_darya_housing_hide:
    cs_ls "Вот. Демократическое голосование завершено единогласно."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    cs_mt "Какое ещё голосование?"
    cs_ls "Советское. Всё в соответствии с текущей обстановкой."
    # cs_camp_emotion: text reaction
    show mt angry pioneer at cs_actor_left
    cs_mt "Лена."
    cs_ls "Всё, молчу."
    # cs_camp_emotion: text reaction
    show mt sad pioneer at cs_actor_left
    cs_narrator "Ольга Дмитриевна вздохнула."
    # cs_camp_emotion: text reaction
    show mt normal pioneer at cs_actor_left
    cs_mt "Вообще-то пионеров распределяют не так."
    cs_narrator "Я сложила ладони."
    cs_ls "Ольга Дмитриевна, пожалуйста."
    cs_narrator "На этот раз я говорила совершенно серьёзно."
    cs_ls "Мы проснулись неизвестно где и неизвестно когда. Дарья — единственный человек здесь, которого я знаю хотя бы час."
    # cs_darya_stage: present in story
    show cs_darya worried pioneer normal at cs_darya_normal_right
    cs_da "И мне тоже было бы спокойнее остаться с Леной."
    cs_narrator "Вожатая посмотрела на неё."
    cs_narrator "Кажется, наличие в нашей компании человека, способного излагать просьбы без сомнительных исторических аналогий, существенно улучшало переговорную позицию."
    pause 0.7
    # cs_camp_emotion: text reaction
    show mt smile pioneer at cs_actor_left
    label cs_check_camp_olga_smile:
    cs_mt "Хорошо. Есть один свободный домик на двоих."
    cs_narrator "Я подняла большой палец."
    cs_ls "Ольга Дмитриевна, вы прекрасный человек."
    cs_mt "Через несколько часов ты ещё можешь изменить своё мнение."
    cs_narrator "Я замерла."
    cs_th "Любопытная формулировка."
    cs_narrator "В контексте «Совёнка» её можно было истолковать несколькими совершенно неприятными способами."
    cs_narrator "Впрочем, кажется, она просто пошутила."
    cs_th "Кажется."
    cs_narrator "Я слегка прищурилась."
    cs_narrator "Ольга Дмитриевна заметила."
    cs_mt "Что?"
    cs_ls "Ничего."
    cs_mt "Опять что-то знаешь?"
    cs_ls "Боюсь, теперь это будет универсальным объяснением моего выражения лица."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_narrator "Она покачала головой."
    # cs_camp_emotion: text reaction
    show mt normal pioneer at cs_actor_left
    cs_mt "Ваши вещи пока оставьте здесь. После обеда Славя покажет вам домик."
    cs_ls "Отлично. Первый жилищный вопрос успешно решён."
    cs_narrator "Дарья едва заметно улыбнулась."
    cs_narrator "А мне впервые за всё время стало чуточку спокойнее."
    cs_narrator "По крайней мере, сегодня нам не придётся ночевать в автобусе."
    return
