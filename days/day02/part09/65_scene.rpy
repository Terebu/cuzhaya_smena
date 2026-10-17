# -*- coding: utf-8 -*-
label cs_day02_65:
    $ save_name = "Чужая смена — День 2: Кто-то уже ждёт"
    $ cs_part08_live = False
    $ cs_part09_live = True
    $ cs_day02_seating_done = True
    $ cs_director_scene("bg ext_square_sunset")
    scene bg ext_square_sunset
    with Dissolve(0.8)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/lets_be_friends.ogg":
        play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    label cs_check_part09_s65:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "К этому времени солнце уже клонилось к деревьям."
    cs_narrator "Воздух стал прохладнее."
    label cs_check_part09_square:
    cs_narrator "На площади заметно прибавилось народу."
    cs_narrator "Несколько скамеек стояли перед небольшим местом, отведённым для выступления."
    cs_narrator "Кто-то разговаривал."
    cs_narrator "Кто-то рассаживался."
    cs_narrator "Издалека доносились обрывки звуков гитары."
    cs_narrator "Я посмотрела в сторону музыки."
    cs_th "Ага."
    cs_th "Значит, подготовка почти закончена."
    cs_narrator "Дарья остановилась рядом."
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Куда сядем?"
    cs_narrator "Я осмотрела скамейки."
    cs_ls "Желательно туда, откуда хорошо видно."
    cs_narrator "Посмотрела на локоть."
    cs_ls "И куда можно дойти без преодоления полосы препятствий."
    cs_narrator "Она рассмеялась."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "После сегодняшнего это разумное требование."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show sl normal pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part09_slavya:
    cs_narrator "В этот момент к нам подошла Славя."
    if cs_friend_sl >= 1:
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Лена! Даша! А я вас как раз искала."
        cs_narrator "Я удивилась."
        cs_ls "Что-то случилось?"
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Нет, всё хорошо. Просто хотела показать вам места, которые мы оставили возле края первого ряда."
        cs_narrator "Она указала на две свободные скамейки."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Там удобнее сидеть, и Лене не придётся протискиваться через остальных с больной рукой."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Ты специально подумала об этом?"
        cs_narrator "Славя немного смутилась."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl shy pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        if cs_helped_sl_day2:
            cs_sl "Ну, вы ведь утром помогли с материалами. Да и ты сегодня поранилась. Я решила, что так будет удобнее."
        else:
            cs_sl "Мы ведь уже успели познакомиться. А сегодня ты поранилась. Я решила, что так будет удобнее."
        cs_narrator "Дарья улыбнулась."
        cs_da "Спасибо, Славя."
        cs_ls "Правда, спасибо."
        cs_narrator "Славя улыбнулась в ответ."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Не за что. Только далеко не уходите, скоро начинаем."
        $ cs_sl_good_seats = True
    else:
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Девочки, привет! Уже пришли на концерт?"
        cs_da "Да. Как раз выбираем, где сесть."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Тогда лучше поторопиться. Скоро начнём, а свободных мест становится меньше."
        cs_narrator "Я посмотрела на скамейки."
        cs_ls "Поняла. Спасибо."
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        # cs_presence_keep: hide cs_semen
        # cs_presence_keep: hide cs_zhenya
        # cs_presence_keep: hide mz
        # cs_presence_keep: hide un
        # cs_presence_keep: hide mi
        # cs_presence_keep: hide dv
        # cs_presence_keep: hide us
        # cs_presence_keep: hide mt
        # cs_presence_keep: hide sh
        # cs_presence_keep: hide el
        # cs_presence_keep: hide cs
        show sl smile pioneer at cs_actor_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["sl", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_sl "Не за что!"
        cs_narrator "Мы выбрали два свободных места немного сбоку."
        cs_narrator "Оттуда было хорошо видно площадку для выступления, хотя сидели мы дальше от музыкантов."
        $ cs_sl_good_seats = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part09_seats:
    cs_narrator "Славя отправилась помогать остальным."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["sl"])
    with cs_sprite_leave
    label cs_director_check_da24651655:
    # cs_director_end
    cs_narrator "Я осторожно села."
    cs_narrator "Дарья устроилась рядом."
    # cs_director_begin: REFLECTIVE_SHOT: Watching the prepared stage and completed work
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_975cacab44:
    # cs_director_end
    cs_narrator "На сценической площадке кто-то передвигал стул."
    cs_narrator "Послышался тихий звук гитарной струны."
    cs_narrator "Я огляделась."
    cs_th "И всё-таки наш плакат сработал."
    cs_th "Люди пришли."
    cs_th "Места приготовили."
    cs_th "Музыканты готовятся."
    cs_th "Удивительное чувство: сделать что-то небольшое, а потом увидеть результат в реальной жизни."
    # cs_director_begin: Return to direct interaction: Watching the prepared stage and completed work
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_cb07c17dfa:
    # cs_director_end
    cs_narrator "Дарья посмотрела на меня."
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Довольна?"
    cs_narrator "Я повернулась."
    cs_ls "Очень."
    cs_narrator "Она улыбнулась."
    cs_da "Даже без компьютера?"
    cs_narrator "Я рассмеялась."
    cs_ls "Представь себе."
    cs_narrator "В этот момент из-за площадки показалась Мику."
    cs_narrator "Она держала папку с нотами."
    cs_narrator "Осматривалась, словно кого-то искала."
    if cs_friend_mi >= 1:
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
        show mi smile pioneer at cs_actor_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        label cs_check_part09_miku:
        cs_narrator "Увидев нас, Мику сразу оживилась."
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
        show mi smile pioneer at cs_actor_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mi "Лена! Даша! Вы пришли!"
        cs_narrator "Я помахала здоровой рукой."
        cs_ls "Конечно. Мы же обещали."
        cs_narrator "Мику подошла ближе."
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
        show mi smile pioneer at cs_actor_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mi "Я сегодня ещё раз попробовала то вступление, о котором мы утром говорили. Помните? Где я слишком долго повторяла одну фразу?"
        cs_narrator "Дарья улыбнулась."
        cs_da "Помню. Ты сократила её?"
        cs_narrator "Мику энергично кивнула."
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
        show mi smile pioneer at cs_actor_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mi "Да! И теперь переход звучит гораздо лучше. По крайней мере, мне так кажется. Алиса тоже сказала, что так интереснее."
        cs_narrator "Я улыбнулась."
        cs_ls "Тогда тем более хочется послушать."
        cs_narrator "Мику посмотрела на нас обеих."
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
        show mi shy pioneer at cs_actor_left
        show cs_darya thinking pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mi "Только не судите слишком строго! Я всё равно немного волнуюсь."
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
        show mi shy pioneer at cs_actor_left
        show cs_darya smile pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Всё будет хорошо."
        cs_narrator "Мику улыбнулась."
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
        show mi smile pioneer at cs_actor_left
        show cs_darya smile pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["mi", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mi "Спасибо. Ладно, мне пора готовиться!"
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
        show cs_darya smile pioneer normal at cs_darya_normal_right
        $ cs_part09_cast = ["cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_narrator "Она помахала нам и поспешила обратно."
        # cs_director_begin: Physical departure in the authored scene
        $ cs_actor_exit(["mi"])
        with cs_sprite_leave
        label cs_director_check_c732427990:
        # cs_director_end
        $ cs_mi_intro_revised = True
    else:
        cs_narrator "Мику заметила нас среди зрителей."
        cs_narrator "Приветливо помахала рукой."
        cs_narrator "Я ответила."
        cs_narrator "Она улыбнулась и вернулась к подготовке."
        # cs_director_begin: Miku returns to stage; audience viewpoint
        $ cs_frame_focus(["cs_darya"])
        with cs_sprite_change
        label cs_director_check_ff17e6298b:
        # cs_director_end
        $ cs_mi_intro_revised = False
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она следила за тем, как Мику исчезает за площадкой."
    cs_ls "Ну что, готова?"
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "К чему?"
    cs_ls "К первому настоящему концерту в «Совёнке»."
    cs_narrator "Она задумалась."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Думаю, да."
    cs_narrator "Я кивнула."
    cs_narrator "А затем немного понизила голос."
    cs_ls "Кстати, если Мику начнёт играть что-нибудь знакомое, постарайся не подсказывать мне заранее. Хочу сама услышать."
    cs_narrator "Дарья улыбнулась."
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
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо."
    cs_narrator "Мы устроились поудобнее."
    # cs_director_begin: Conversation ended; attention turns to the stage
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_45c6fdba52:
    # cs_director_end
    cs_narrator "Впереди уже собирались остальные зрители."
    cs_narrator "Я осторожно положила перебинтованную руку на колени."
    cs_narrator "Дарья сидела рядом."
    cs_narrator "Никаких новых расследований."
    cs_narrator "Никаких поисков выхода."
    cs_narrator "И, очень хотелось надеяться, никаких неожиданных встреч с медицинским персоналом."
    cs_th "Просто музыка."
    cs_th "Обычный вечер."
    cs_th "Хотя бы на час."
    stop music fadeout 3.0
    $ cs_day02_part09_complete = True
    label cs_check_part09_ready:
    pause 0.5
    return
