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
    cs_narrator "Столовая встретила нас гулом голосов."
    cs_narrator "Звенела посуда."
    cs_narrator "Кто-то смеялся."
    cs_narrator "Пионеры переговаривались через столы."
    cs_narrator "Всё выглядело удивительно обыденно."
    cs_narrator "И почти сразу я увидела его."
    cs_narrator "За одним из столов сидел парень."
    cs_narrator "Тёмные волосы."
    cs_narrator "Пионерская форма."
    cs_narrator "И слегка потерянное выражение лица человека, который всё ещё не до конца принял окружающую действительность."
    cs_narrator "{b}Семён.{/b}"
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.25, delay=1.0, channel="ambience")
    cs_narrator "Не стилизованный рисунок."
    cs_narrator "Не изображение из меню игры."
    cs_narrator "Обычный живой человек."
    cs_narrator "Он поднял глаза."
    cs_narrator "Увидел Ольгу Дмитриевну."
    cs_narrator "Потом меня."
    cs_narrator "Затем Дарью."
    cs_narrator "И застыл."
    cs_narrator "Я тоже остановилась."
    cs_th "Ну здравствуй, главный герой."
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 1.5 fadein 2.0
    cs_narrator "Семён явно понятия не имел, кто мы такие."
    cs_narrator "Зато я знала о нём слишком много."
    cs_narrator "Его прежнюю жизнь."
    cs_narrator "Зимнюю Москву."
    cs_narrator "Автобус."
    cs_narrator "Возможные отношения."
    cs_narrator "Разные варианты будущего."
    cs_narrator "И даже то, кем могли стать некоторые его версии после множества повторений."
    cs_narrator "Всё это были сведения, которые сейчас категорически не стоило произносить вслух."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Он?"
    cs_narrator "Я кивнула."
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
    cs_narrator "Мне пришлось приложить некоторое усилие, чтобы не улыбнуться."
    cs_narrator "Ситуация была по-настоящему нелепой."
    cs_narrator "Человек, который по правилам знакомой мне истории должен был быть единственным пришельцем из будущего, теперь смотрел на двух девушек, прибывших тем же автобусом сутки спустя."
    cs_narrator "Причём одна знала его историю почти наизусть."
    cs_narrator "А другая тоже была обычной девушкой из Москвы 2026 года и так же не понимала, как мы сюда попали."
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
    cs_th "И что теперь?"
    cs_th "Спросить, как дела?"
    cs_th "Пожелать удачного прохождения?"
    cs_th "Предупредить про концовки?"
    cs_narrator "Нет."
    cs_narrator "Начнём с простого."
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
    cs_narrator "Его лицо изменилось мгновенно."
    cs_narrator "Словно я только что произнесла пароль от чего-то, о существовании чего он предпочёл бы никому не рассказывать."
    cs_narrator "Семён застыл."
    label cs_check_day01_part04_reaction:
    cs_sy "Откуда ты…"
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 1.5 fadein 2.5
    cs_narrator "Я едва заметно улыбнулась."
    cs_ls "А вот теперь, товарищ Семён…"
    cs_narrator "Дарья рядом тихо вздохнула."
    cs_narrator "Кажется, она уже догадывалась, куда я веду."
    cs_narrator "Я продолжила, сохраняя абсолютно серьёзное выражение лица:"
    label cs_check_day01_part04_final:
    cs_ls "…у нас с тобой есть о чём поговорить."
    pause 1.0
    cs_narrator "Он продолжал смотреть на меня."
    cs_narrator "А я впервые за всё время почувствовала, что могу получить ответ от человека, который действительно понимает хотя бы часть происходящего."
    cs_th "По крайней мере, очень на это надеюсь."
    return
