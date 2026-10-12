# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_02:
    $ save_name = u"Чужая смена — День 1: Знакомое место"
    scene bg ext_bus with dissolve
    $ renpy.music.set_volume(0.65, delay=2.0, channel="ambience")
    cs_narrator "Двери автобуса оставались открытыми."
    cs_narrator "Я остановилась перед ступеньками."
    cs_narrator "Снаружи стрекотали насекомые."
    cs_narrator "Где-то вдалеке раздавались детские голоса."
    cs_narrator "В воздухе едва различимо звучала музыка."
    cs_narrator "Негромкая, старомодная, почти растворяющаяся в шелесте листвы."
    cs_narrator "И тут в голове что-то неприятно шевельнулось."
    cs_narrator "Не страх."
    cs_narrator "Пока ещё нет."
    cs_narrator "Скорее чувство узнавания."
    cs_narrator "Я посмотрела через лобовое стекло."
    cs_narrator "Две статуи возле ворот."
    cs_narrator "Кирпичные тумбы."
    cs_narrator "Металлические створки."
    cs_narrator "Дорожка, уходящая вглубь лагеря."
    cs_narrator "Всё это выглядело слишком знакомо."
    scene bg ext_camp_entrance_day with Dissolve(1.5)
    cs_narrator "Я медленно спустилась на землю."
    label cs_check_day01_outside:
    cs_narrator "Снаружи оказалось ещё жарче."
    cs_narrator "Под подошвами зимних ботинок хрустнула сухая земля."
    cs_narrator "Куртку я перекинула через руку."
    cs_narrator "Несколько секунд просто стояла, оглядываясь."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_narrator "Дарья вышла следом."
    cs_narrator "Она, по крайней мере, выглядела менее несчастной в своей одежде."
    cs_narrator "Хотя назвать наши наряды подходящими для такой погоды было бы довольно смелым заявлением."
    cs_narrator "Я сделала несколько шагов к воротам."
    cs_narrator "Остановилась."
    cs_narrator "Прищурилась."
    cs_ls "Где-то я это уже видела."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "Здесь?"
    cs_ls "Нет."
    cs_narrator "Я подошла ближе."
    cs_narrator "Сердце почему-то забилось быстрее."
    cs_ls "На компьютере."
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 2.0 fadein 3.0
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    cs_da "Что?"
    cs_narrator "Я почти не услышала вопроса."
    cs_narrator "Смотрела на ворота."
    cs_narrator "На статуи."
    cs_narrator "На дорогу."
    cs_narrator "На лес за оградой."
    cs_narrator "На сам ракурс, с которого всё это открывалось."
    cs_narrator "Даже автобус позади стоял подозрительно знакомо."
    cs_narrator "В памяти начали всплывать образы."
    $ renpy.music.set_volume(0.2, delay=2.0, channel="ambience")
    cs_narrator "Главное меню."
    cs_narrator "Музыка."
    cs_narrator "Фоны."
    cs_narrator "Диалоги."
    cs_narrator "Спрайты."
    cs_narrator "Семён."
    cs_narrator "Славя."
    cs_narrator "Алиса."
    cs_narrator "Ульяна."
    cs_narrator "Лена."
    cs_narrator "Женя."
    cs_narrator "Мику."
    cs_narrator "Ольга Дмитриевна."
    cs_narrator "Пионер."
    cs_narrator "Юля."
    cs_narrator "Я медленно повернулась к автобусу."
    cs_narrator "На маршрутной табличке по-прежнему значилось:"
    cs_narrator "{b}410.{/b}"
    stop music fadeout 1.5
    pause 1.5
    cs_ls "Нет."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "Лена?"
    cs_ls "Любопытно."
    cs_narrator "Я вернулась к автобусу и ещё раз посмотрела на номер."
    cs_narrator "Четыреста десять."
    cs_narrator "Он никуда не исчез."
    cs_narrator "Я провела ладонью по лицу."
    cs_ls "Прекрасно. Просто замечательно."
    cs_da "Что случилось?"
    cs_narrator "Я повернулась к ней."
    cs_narrator "Объяснить происходящее нормальными словами представлялось практически невозможным."
    cs_ls "В общем, есть одна игра."
    cs_da "Игра?"
    cs_ls "Визуальная новелла."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_da "Хорошо."
    cs_ls "Там один парень зимой садится в автобус номер четыреста десять."
    cs_narrator "Дарья медленно посмотрела на автобус."
    cs_narrator "Затем на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_da "Продолжай."
    cs_ls "Засыпает."
    cs_narrator "Она стала слушать внимательнее."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "И?"
    cs_narrator "Я указала на ворота."
    cs_ls "Просыпается здесь."
    pause 2.0
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "В траве стрекотал кузнечик."
    cs_narrator "Где-то за воротами раздался детский смех."
    play sound "<from 0 to 3>sound/ambiences/grasshoper_clean.ogg" volume 0.25 fadein 0.5 fadeout 0.5
    cs_narrator "Дарья снова посмотрела на вывеску."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_da "«Совёнок»…"
    cs_ls "Именно."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "И ты знаешь это место?"
    cs_narrator "Я коротко усмехнулась."
    cs_ls "К сожалению, значительно лучше, чем хотелось бы."
    return
