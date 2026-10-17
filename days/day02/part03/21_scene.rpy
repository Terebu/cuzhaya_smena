# -*- coding: utf-8 -*-
label cs_day02_21:
    $ save_name = "Чужая смена — День 2: Архитектурное поражение"
    $ cs_part03_live = True
    if cs_day02_miku_listened is not True:
        return
    $ cs_part02_live = False
    $ cs_director_scene("bg int_musclub_day")
    scene bg int_musclub_day
    $ cs_part03_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    stop music fadeout 1.0
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/music_club_day.ogg":
        play ambience "sound/ambiences/music_club_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.1, channel="ambience", delay=1.0)
    play cs_piano cs_miku_piano_track noloop fadein 0.5
    label cs_check_part03_s21:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Пока Мику доигрывала мелодию, я решила немного посидеть."
    cs_narrator "У стены нашлась длинная деревянная лавка."
    cs_narrator "Выглядела она вполне обыкновенно, если не считать довольно высоких ножек."
    cs_narrator "Я села, откинулась назад и привычно вытянула ноги."
    cs_narrator "И обнаружила неожиданную проблему."
    cs_narrator "Ступни не доставали до пола."
    cs_narrator "Точнее, если очень постараться, можно было коснуться его носками."
    cs_narrator "Но сидеть нормально всё равно не получалось."
    cs_narrator "Я посмотрела вниз."
    cs_narrator "Потом на лавку."
    cs_narrator "Потом снова вниз."
    cs_th "Ну прекрасно."
    cs_th "Советский Союз впервые одержал надо мной архитектурную победу."
    cs_narrator "Я осторожно вытянула ноги ещё немного."
    cs_narrator "Не помогло."
    cs_narrator "Дарья заметила мои упражнения."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что ты делаешь?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Проверяю соответствие местной мебели антропометрическим характеристикам населения."
    cs_narrator "Она проследила за моим взглядом."
    cs_narrator "Посмотрела на ноги."
    cs_narrator "Затем на лавку."
    cs_narrator "И улыбнулась."
    cs_da "Ты до пола не достаёшь?"
    cs_ls "Благодарю за точную диагностику."
    cs_narrator "Дарья рассмеялась."
    cs_da "Может, просто сядешь ближе к краю?"
    cs_narrator "Я попробовала."
    cs_narrator "Теперь носки касались пола, но сидеть стало неудобно."
    cs_narrator "Я вернулась обратно."
    cs_ls "Нет. Предпочитаю признать поражение."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Разумно."
    cs_narrator "Я сложила руки на коленях."
    cs_narrator "Несколько секунд смотрела перед собой."
    cs_narrator "Потом начала слегка покачивать ногами."
    cs_narrator "Вперёд."
    cs_narrator "Назад."
    cs_narrator "В ритм мелодии."
    cs_narrator "Мику продолжала играть."
    cs_narrator "Звуки пианино наполняли комнату, смешиваясь с тихим шелестом листьев за окном."
    cs_narrator "Дарья некоторое время наблюдала за мной."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    $ cs_part03_cast = []
    cs_narrator "Затем присела рядом."
    cs_da "Тебе удобно?"
    cs_ls "Удивительно, но да."
    cs_da "Несмотря на отсутствие контакта с землёй?"
    cs_ls "Иногда человеку полезно немного потерять связь с реальностью."
    cs_narrator "Она усмехнулась."
    cs_da "По-моему, в последние два дня у нас с этим и так всё прекрасно."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на собственные ноги."
    cs_narrator "И тихо рассмеялась."
    cs_ls "Справедливое замечание."
    cs_narrator "Мы замолчали."
    cs_narrator "Мику играла что-то спокойное."
    cs_narrator "Я слушала, слегка покачивая ногами."
    cs_narrator "И постепенно поймала себя на странном ощущении."
    cs_narrator "Мне действительно было хорошо."
    cs_narrator "Не потому, что мы нашли способ вернуться домой."
    cs_narrator "Не потому, что Шурик с Электроником внезапно придумали зарядку для смартфона."
    cs_narrator "И даже не потому, что я начала понимать устройство этого лагеря."
    cs_narrator "Ничего подобного."
    cs_narrator "Автобус по-прежнему оставался загадкой."
    cs_narrator "Телефон не работал."
    cs_narrator "И я понятия не имела, сколько времени мы здесь проведём."
    cs_narrator "Но сейчас можно было просто сидеть."
    cs_narrator "Слушать музыку."
    cs_narrator "Чувствовать тепло солнечного света на руках."
    cs_narrator "И иногда поглядывать на Дарью, которая устроилась рядом."
    cs_th "Вот ведь."
    cs_th "Вчера я пыталась просчитать чуть ли не каждую минуту."
    cs_th "А сегодня мне достаточно обычной деревянной лавки."
    cs_narrator "Я снова покачала ногами."
    cs_ls "Вот так и деградирует человек из две тысячи двадцать шестого."
    cs_narrator "Дарья повернулась ко мне."
    cs_da "Что?"
    cs_ls "Вчера смартфон, компьютер и графический планшет. Сегодня — лавка и бесплатный концерт."
    cs_narrator "Она улыбнулась."
    cs_da "И что, плохо?"
    cs_narrator "Я посмотрела на Мику."
    cs_narrator "Потом снова на неё."
    cs_ls "Нет."
    cs_narrator "Немного помолчала."
    cs_ls "Как ни странно, совсем неплохо."
    cs_narrator "Дарья не стала ничего добавлять."
    cs_narrator "Просто осталась сидеть рядом."
    stop cs_piano fadeout 0.8
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show mi normal pioneer at cs_actor_left zorder 10
    $ cs_part03_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Мику закончила мелодию и подняла голову."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    $ cs_part03_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Ну как? Лучше получилось?"
    cs_narrator "Я подняла большой палец."
    cs_ls "Мне понравилось."
    cs_da "Мне тоже. Особенно концовка."
    cs_narrator "Мику улыбнулась."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    $ cs_part03_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Спасибо! Я её как раз немного переделала. Хотя ещё не уверена, что оставлю именно так."
    cs_narrator "Она посмотрела на часы."
    cs_mi "Ой. Нам ведь уже пора на линейку!"
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Я наконец слезла с лавки."
    cs_narrator "Поставила обе ноги на пол."
    cs_narrator "Облегчённо вздохнула."
    cs_ls "Связь с землёй восстановлена."
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Мику собрала ноты и аккуратно закрыла папку."
    cs_mi "Тогда пойдёмте. А то Ольга Дмитриевна опять скажет, что я засиделась в кружке."
    cs_ls "Заодно выясним, какие обязанности нам сегодня подготовили."
    cs_da "Звучит не слишком обнадёживающе."
    cs_narrator "Я улыбнулась."
    cs_ls "Добро пожаловать в организованный отдых."
    stop cs_piano fadeout 1.0
    $ cs_part03_live = False
    $ cs_part02_live = True
    return
