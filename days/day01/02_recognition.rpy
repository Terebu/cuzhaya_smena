# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_02:
    $ save_name = u"Чужая смена — День 1: Знакомое место"
    $ cs_director_scene("bg ext_bus")
    scene bg ext_bus
    with dissolve
    $ renpy.music.set_volume(0.65, delay=2.0, channel="ambience")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Двери автобуса оставались открытыми."
    cs_narrator "Я остановилась перед ступеньками."
    cs_narrator "Снаружи стрекотали насекомые, вдали раздавались детские голоса. В шелесте листвы растворялась негромкая старомодная музыка."
    cs_narrator "В голове неприятно шевельнулось чувство узнавания. Не страх. Пока ещё нет."
    cs_narrator "Я посмотрела через лобовое стекло."
    cs_narrator "Две статуи возле ворот, кирпичные тумбы, металлические створки. Дорожка вглубь лагеря."
    cs_narrator "Всё выглядело слишком знакомо."
    $ cs_director_scene("bg ext_camp_entrance_day")
    scene bg ext_camp_entrance_day
    with Dissolve(1.5)
    cs_narrator "Я медленно спустилась на землю."
    label cs_check_day01_outside:
    cs_narrator "Снаружи оказалось ещё жарче."
    cs_narrator "Под подошвами зимних ботинок хрустнула сухая земля."
    cs_narrator "Куртку я перекинула через руку."
    cs_narrator "Несколько секунд просто стояла, оглядываясь."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья вышла следом. В своей одежде она выглядела менее несчастной, хотя для такой погоды мы обе были одеты нелепо."
    cs_narrator "Я подошла к воротам и прищурилась."
    cs_ls "Где-то я это уже видела."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Здесь?"
    cs_ls "Нет."
    cs_narrator "Я подошла ближе."
    cs_narrator "Сердце почему-то забилось быстрее."
    cs_ls "На компьютере."
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 2.0 fadein 3.0
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    # cs_director_begin: REFLECTIVE_SHOT: Recognition of game scenery and bus number
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_4205df3c28:
    # cs_director_end
    cs_narrator "Я почти не услышала вопроса. Ворота, статуи, лес за оградой — даже ракурс был знакомым."
    cs_narrator "Даже автобус позади стоял подозрительно знакомо."
    cs_narrator "В памяти начали всплывать образы."
    $ renpy.music.set_volume(0.2, delay=2.0, channel="ambience")
    cs_narrator "Главное меню, музыка, фоны, диалоги, спрайты."
    cs_narrator "Семён, Славя, Алиса, Ульяна, Лена Тихонова, Женя, Мику, Ольга Дмитриевна."
    cs_narrator "Пионер."
    cs_narrator "Юля."
    cs_narrator "Я медленно повернулась к автобусу."
    cs_narrator "На маршрутной табличке по-прежнему значилось:"
    cs_narrator "{b}410.{/b}"
    stop music fadeout 1.5
    pause 1.5
    # cs_director_begin: Return to direct interaction: Recognition of game scenery and bus number
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_93ae1e4b14:
    # cs_director_end
    cs_ls "Нет."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена?"
    cs_ls "Подожди. Мне надо это переварить."
    cs_narrator "Я вернулась к автобусу. Четыреста десять. Номер никуда не исчез."
    cs_narrator "Я провела ладонью по лицу."
    cs_ls "Так. Спокойно."
    cs_da "Что случилось?"
    cs_narrator "Как объяснить это нормальными словами?"
    cs_ls "В общем, есть одна игра."
    cs_da "Игра?"
    cs_ls "Визуальная новелла."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо."
    cs_ls "Там один парень зимой садится в автобус номер четыреста десять."
    cs_narrator "Дарья посмотрела на автобус, потом на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Продолжай."
    cs_ls "Засыпает."
    cs_narrator "Она стала слушать внимательнее."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И?"
    cs_narrator "Я указала на ворота."
    cs_ls "Просыпается здесь."
    pause 2.0
    cs_narrator "Мы помолчали. В траве стрекотал кузнечик, за воротами раздался детский смех."
    play sound "<from 0 to 3>sound/ambiences/grasshoper_clean.ogg" volume 0.25 fadein 0.5 fadeout 0.5
    cs_narrator "Дарья снова посмотрела на вывеску."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "«Совёнок»…"
    cs_ls "Именно."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И ты знаешь это место?"
    cs_narrator "Я коротко усмехнулась."
    cs_ls "К сожалению, значительно лучше, чем хотелось бы."
    return
