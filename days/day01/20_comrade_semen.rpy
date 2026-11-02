# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_20:
    $ save_name = u"Чужая смена — День 1: Товарищ Семён"
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.45, delay=1.0, channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_dining_full:
        play ambience cs_day_dining_full fadeout 1.0 fadein 2.0
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Столовая встретила гулом голосов и звоном посуды. Пионеры переговаривались через столы — самый обыкновенный обед."
    cs_narrator "Я почти сразу увидела парня в форме: тёмные волосы, потерянное лицо человека, который ещё не освоился."
    cs_narrator "{b}Семён.{/b}"
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.25, delay=1.0, channel="ambience")
    cs_narrator "Обычный живой человек."
    cs_narrator "Он увидел вожатую, нас с Дарьей — и застыл. Я тоже остановилась."
    cs_th "Ну здравствуй, главный герой."
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 1.5 fadein 2.0
    cs_narrator "Он понятия не имел, кто мы. А я знала его прежнюю жизнь, зимнюю Москву, автобус. Возможные концовки. Даже то, кем стали некоторые его версии после множества повторений."
    cs_narrator "Сведения, которые сейчас категорически не стоило произносить вслух."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Он?"
    cs_ls "Ага."
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тот самый Семён?"
    cs_ls "Он самый."
    show mt normal pioneer at cs_actor_left
    # cs_composition: regroup
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Ольга Дмитриевна помахала ему рукой."
    # cs_camp_emotion: text reaction
    show mt smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_darya_semen_focus:
    cs_mt "Семён! Познакомься. У нас ещё две новенькие."
    show cs_semen neutral pioneer far at cs_semen_far_right
    # cs_composition: regroup
    show mt normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Парень медленно поднялся."
    label cs_check_day01_part04_semen:
    cs_narrator "Пришлось сдержать улыбку: единственный пришелец из будущего смотрел на двух новых пассажирок того же автобуса."
    cs_narrator "Одна знала его историю почти наизусть. Другая понимала происходящее не больше него."
    cs_narrator "Я протянула руку."
    cs_ls "Лена."
    cs_narrator "Он пожал её."
    # cs_camp_emotion: text reaction
    show cs_semen awkward pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_camp_semen_awkward:
    cs_sy "Семён."
    cs_narrator "Несколько секунд я смотрела ему в глаза."
    cs_th "И что теперь? Спросить, как дела? Пожелать удачного прохождения? Предупредить про концовки?"
    cs_narrator "Нет. Начнём с простого."
    cs_ls "Слушай."
    # cs_camp_emotion: text reaction
    show cs_semen serious pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Да?"
    cs_ls "Очень странный вопрос."
    show cs_semen thinking pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он слегка напрягся."
    cs_sy "Какой?"
    cs_narrator "Я указала большим пальцем через плечо, примерно в сторону ворот."
    label cs_check_day01_part04_bus_question:
    cs_ls "Ты случайно не на четыреста десятом сюда приехал?"
    stop music fadeout 1.0
    pause 1.5
    show cs_semen surprised pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Семён застыл, будто я произнесла пароль от чего-то, о чём он предпочёл бы молчать."
    label cs_check_day01_part04_reaction:
    cs_sy "Откуда ты…"
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 1.5 fadein 2.5
    cs_narrator "Я едва заметно улыбнулась."
    cs_ls "А вот теперь, товарищ Семён…"
    cs_narrator "Дарья рядом вздохнула. Уже догадалась, куда я веду."
    label cs_check_day01_part04_final:
    cs_ls "…у нас с тобой есть о чём поговорить."
    pause 1.0
    cs_narrator "Впервые мне показалось, что я смогу получить ответ от человека, который понимает хотя бы часть происходящего."
    cs_th "По крайней мере, очень на это надеюсь."
    return
