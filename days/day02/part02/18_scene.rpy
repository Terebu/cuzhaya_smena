# -*- coding: utf-8 -*-
label cs_day02_18:
    $ save_name = "Чужая смена — День 2: Знакомая мелодия"
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    show mi normal pioneer at cs_actor_left zorder 10
    $ cs_part02_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    stop music fadeout 1.0
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/music_club_day.ogg":
        play ambience "sound/ambiences/music_club_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.08, channel="ambience", delay=1.0)
    label cs_check_part02_s18:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mi", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Дарья несколько секунд сидела неподвижно. Посмотрела на клавиши. Потом осторожно положила на них пальцы. Нажала одну."
    cs_narrator "Прислушалась. Нажала вторую. На третьей немного поморщилась."
    cs_da "Вот. Уже забыла."
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    $ cs_part02_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_miku_18:
    cs_mi "Ничего! Начни медленнее. Руки вспомнят."
    cs_narrator "Дарья кивнула. Снова посмотрела на клавиши."
    $ cs_director_scene("cs_cg_darya_piano_day")
    scene cs_cg_darya_piano_day
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    $ cs_part02_cg = True
    with Dissolve(0.8)
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.58, channel="cs_piano", delay=0.3)
    play cs_piano cs_darya_piano_track noloop fadein 1.0
    label cs_check_d2_piano_darya:
    pause 1.5
    cs_narrator "И начала играть. Сначала очень осторожно. Отдельные ноты. Небольшая пауза."
    cs_narrator "Потом короткая последовательность звуков. Мелодия была простой. Я не знала её названия. Возможно, это было обычное учебное произведение."
    cs_narrator "Возможно, Дарья просто играла по памяти небольшой фрагмент, который когда-то разучивала. Но постепенно ноты сложились во что-то цельное. Негромкое. Немного задумчивое."
    cs_narrator "С несколькими неровными переходами. Дарья на секунду остановилась, улыбнулась своей ошибке и попробовала ещё раз. Теперь получилось лучше. Я стояла возле стола и слушала."
    cs_narrator "И неожиданно для себя совсем забыла, что собиралась комментировать происходящее."
    cs_th "Вот ведь. Мы знакомы меньше двух дней. А я уже успела решить, что примерно понимаю её характер."
    cs_narrator "Спокойная. Внимательная. Иногда ироничная. Человек, который умеет вовремя остановить меня, когда я начинаю говорить слишком много."
    cs_narrator "Но сейчас обнаружилось кое-что ещё. Она когда-то училась играть. Помнила мелодию. И, судя по тому, как внимательно смотрела на клавиши, ей действительно хотелось восстановить её в памяти."
    cs_narrator "Я посмотрела на Дарью. Красные волосы слегка закрывали щёку. Она подалась вперёд, прислушиваясь к собственной игре. Никакой показной уверенности."
    cs_narrator "Никакого желания произвести впечатление. Просто пыталась сыграть то, что помнила."
    cs_th "И почему-то именно это было особенно красиво."
    stop cs_piano fadeout 0.8
    $ cs_director_scene("bg int_musclub_day")
    scene bg int_musclub_day
    $ cs_part02_cg = False
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    with Dissolve(0.8)
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    # cs_director_begin: Return from piano CG to both interlocutors
    $ cs_frame_focus(["mi", "cs_darya"])
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_748577bc95:
    # cs_director_end
    cs_narrator "Мелодия закончилась негромким аккордом. Дарья убрала руки с клавиш. Несколько секунд никто не произносил ни слова. Потом Мику первой улыбнулась."
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    $ cs_part02_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Очень мило получилось!"
    cs_narrator "Дарья слегка смутилась."
    cs_da "Правда? Я половину забыла."
    cs_mi "Да! Середина немного сбилась, но начало очень красивое. И ты хорошо выдержала последние ноты."
    cs_narrator "Дарья посмотрела на клавиши."
    cs_da "Кажется, раньше я играла быстрее."
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    show mi smile pioneer at cs_actor_left zorder 10
    $ cs_part02_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Быстрее необязательно лучше."
    cs_narrator "Я невольно кивнула."
    cs_ls "Согласна."
    cs_narrator "Дарья подняла на меня взгляд."
    cs_da "Ну что, обещание не смеяться выполнила?"
    cs_narrator "Я улыбнулась."
    cs_ls "Более чем."
    cs_da "Настолько плохо?"
    cs_narrator "Я покачала головой."
    cs_ls "Наоборот. Мне очень понравилось."
    cs_narrator "Она несколько секунд смотрела на меня."
    cs_da "Даже с ошибками?"
    cs_ls "Особенно потому, что ты не бросила на первой."
    cs_narrator "Дарья опустила взгляд. На губах появилась лёгкая улыбка."
    cs_da "Спасибо."
    cs_narrator "Я кивнула. И не стала добавлять ничего лишнего."
    cs_th "Надо же. Кажется, я постепенно учусь вовремя замолкать."
    cs_narrator "Мику тем временем подошла к пианино."
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    $ cs_part02_cast = ["mi"]
    # cs_presence_keep: hide cs_darya
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
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    $ cs_part02_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Можно я попробую свой кусочек? Я как раз хотела понять, не слишком ли растянула вступление."
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
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья поднялась, освобождая место."
    cs_da "Конечно."
    cs_narrator "Мику открыла папку с нотами. Положила лист на подставку. Потом посмотрела на нас."
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
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Только я ещё не решила, как лучше. Поэтому если что-то покажется странным, говорите!"
    cs_narrator "Я посмотрела в сторону окна. Времени до линейки оставалось немного. Можно было остаться и внимательно послушать её репетицию. А можно поблагодарить за знакомство и отправиться к площади."
    cs_narrator "Мику не выглядела человеком, который обидится, если мы сейчас уйдём. Но, кажется, ей действительно хотелось услышать мнение со стороны."
    return
