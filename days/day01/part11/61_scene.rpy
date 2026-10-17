# -*- coding: utf-8 -*-
label cs_day01_61:
    $ save_name = "Чужая смена — День 1: На крыльце библиотеки"
    label cs_check_d1_s61:
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("cs_library_exterior_sunset")
    scene cs_library_exterior_sunset
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 1.0 fadein 1.0
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    stop music fadeout 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Снаружи воздух показался прохладным. После библиотеки захотелось потянуться и хотя бы минуту ничего не объяснять."
    cs_narrator "Женя проверила дверь, пожелала нам спокойной ночи и пошла к домикам. Я смотрела ей вслед, пока Дарья не тронула меня за рукав."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_zhenya"])
    with cs_sprite_leave
    label cs_director_check_73461dc812:
    # cs_director_end
    # cs_presence_keep: hide cs_zhenya
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Теперь домой?"
    cs_ls "Теперь точно."
    # cs_presence_keep: hide cs_zhenya
    if cs_met_un and cs_friend_un >= 1:
        show un smile pioneer at cs_actor_left zorder 10
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_narrator "На скамейке чуть в стороне сидела моя тёзка. Книга лежала у неё на коленях, но смотрела она на листок, вложенный между страницами."
        cs_narrator "Увидев нас, Лена поднялась."
        show un smile pioneer at cs_actor_left zorder 10
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_un "Вы уже уходите?"
        cs_ls "Да. Библиотеку закрыли. А ты?"
        show un smile pioneer at cs_actor_left zorder 10
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_un "Я тоже. Просто… хотела тебе кое-что показать."
        cs_narrator "Она осторожно вытащила листок. На нём был нарисован угол домика: крыльцо, перила и ветка, закрывающая половину окна."
        cs_narrator "Я вспомнила наш разговор о рисовании. Тогда её «может быть» было достаточно легко принять за вежливый отказ."
        cs_ls "Можно посмотреть поближе?"
        cs_narrator "Она протянула рисунок."
        show un smile pioneer at cs_actor_left zorder 10
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_un "Он ещё не закончен."
        cs_ls "Вижу. Мне нравится, как у тебя ветка уходит вперёд. Из-за неё домик кажется дальше."
        cs_narrator "Лена посмотрела на листок, будто проверяя, действительно ли там была эта ветка."
        show un smile pioneer at cs_actor_left zorder 10
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_un "Я боялась, что она всё закрывает."
        cs_ls "Немного закрывает. Но ты же именно так его видела?"
        cs_narrator "Она кивнула."
        cs_ls "Тогда всё честно."
        cs_narrator "Дарья заглянула через моё плечо."
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Даже ступенька похожа. Я сегодня о такую споткнулась."
        cs_narrator "Лена улыбнулась. Я вернула ей рисунок, стараясь не замять край."
        cs_ls "Завтра хочу сама что-нибудь нарисовать. Без планшета. Посмотрим, вспомнят ли руки старые обязанности."
        show un smile pioneer at cs_actor_left zorder 10
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_un "Если нужны карандаши, у меня есть."
        cs_ls "Спасибо. Если встретимся, спрошу."
        cs_narrator "Мы немного прошли вместе и расстались у развилки. Лена убрала рисунок обратно в книгу. Мне было приятно, что она решила показать его сама."
        cs_narrator "Я вернула лист двумя руками, стараясь не загнуть угол. Тёзка сразу прижала его к книге, но прятать рисунок с прежней поспешностью уже не стала."
        cs_ls "Спасибо, что показала. Я бы, наверное, ещё долго собиралась."
        show un smile pioneer at cs_actor_left zorder 10
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_un "Я тоже собиралась."
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Значит, успели вовремя."
        cs_narrator "Мы улыбнулись друг другу. Продолжать разговор только ради того, чтобы он не закончился, было уже необязательно."
        # cs_director_begin: Tikhonova farewell at the branch of the paths
        $ cs_actor_exit(["un"])
        with cs_sprite_leave
        label cs_director_check_08c2c7b38c:
        # cs_director_end
        # cs_presence_keep: hide un
    return
