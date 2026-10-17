# -*- coding: utf-8 -*-
label cs_day02_38:
    $ save_name = "Чужая смена — День 2: Немного ревности"
    $ cs_part04_live = False
    $ cs_part05_live = True
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part05_cg = False
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
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.1, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/get_to_know_me_better.ogg":
        play music "sound/music/get_to_know_me_better.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part05_s38:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Некоторое время мы шли молча."
    cs_narrator "Дорожка была почти пустой."
    cs_narrator "Солнце пробивалось через листья, оставляя на земле небольшие светлые пятна."
    cs_narrator "Я ещё размышляла о том, насколько странно выглядит готовое объявление среди совершенно обычных лагерных расписаний, когда Даша неожиданно спросила:"
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я повернулась."
    cs_ls "М?"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тебе Виола понравилась?"
    cs_narrator "Я остановилась."
    cs_th "О."
    cs_th "Вот это интересный поворот."
    cs_ls "Как медработник?"
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Как человек."
    cs_narrator "Я немного подумала."
    cs_ls "Да. Она спокойная, внимательная. И с чувством юмора у неё всё хорошо."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И красивая?"
    cs_narrator "Я медленно повернулась к ней."
    cs_narrator "Даша смотрела на меня совершенно невинно."
    cs_narrator "Слишком невинно."
    cs_ls "Кажется, меня пытаются подвести к определённому ответу."
    cs_narrator "Она улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я просто спросила."
    cs_narrator "Я вздохнула."
    cs_ls "Да, красивая."
    cs_narrator "Пауза."
    cs_ls "Но если это допрос, прошу предоставить мне адвоката."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да нет же. Просто вспомнила, как внимательно ты её рассматривала."
    cs_narrator "Я задумалась."
    cs_th "Вот ведь."
    cs_th "А я думала, делаю это незаметно."
    cs_ls "Профессиональная наблюдательность художника."
    cs_da "Конечно."
    cs_ls "Я изучала композицию, освещение и особенности внешности."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "В медицинском кабинете?"
    cs_ls "Особенно там."
    cs_narrator "Она тихо засмеялась."
    cs_narrator "Я тоже не смогла сдержать улыбку."
    cs_narrator "Потом немного помолчала."
    cs_ls "Даш, если серьёзно, я ведь уже говорила, кто мне нравится."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Улыбка стала мягче."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Помню."
    cs_ls "И с тех пор ничего не изменилось."
    cs_narrator "Дарья некоторое время молчала."
    cs_narrator "Затем кивнула."
    cs_da "Я и не думала, что изменилось."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Тогда зачем спрашивала?"
    cs_narrator "Она слегка пожала плечами."
    cs_da "Хотела немного тебя подразнить."
    cs_narrator "Я замерла."
    cs_narrator "Потом медленно подняла палец."
    cs_ls "Так."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Это уже злоупотребление моими собственными методами."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Учитель хороший."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Несколько секунд молчала."
    cs_narrator "Потом тоже рассмеялась."
    cs_th "Надо же."
    cs_th "За два дня она уже научилась отвечать мне моими же шутками."
    cs_th "Опасная тенденция."
    cs_narrator "Мы продолжили идти."
    cs_narrator "Я ненадолго задумалась."
    cs_narrator "И всё же один вопрос не давал покоя."
    cs_ls "А ты не ревновала?"
    cs_narrator "Дарья повернулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "К Виоле?"
    cs_narrator "Я кивнула."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом слегка покачала головой."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Нет."
    cs_narrator "Я задумалась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты ведь просто разговаривала с ней. Почему я должна ревновать?"
    cs_narrator "Я отвела взгляд."
    cs_ls "Не знаю. Наверное, потому что сама иногда немного ревную."
    cs_narrator "Она остановилась."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Правда?"
    cs_narrator "Я посмотрела на неё."
    cs_th "Прекрасно."
    cs_th "Соколова снова сказала вслух то, что можно было бы сначала обдумать."
    cs_narrator "Я медленно кивнула."
    cs_ls "Иногда. Но понимаю, что это моя проблема, а не твоя."
    cs_narrator "Дарья немного помолчала."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен, мы ведь пока даже не решили, что между нами будет."
    cs_narrator "Я кивнула."
    cs_ls "Знаю."
    cs_da "И мне действительно приятно, что ты сказала о своих чувствах."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_da "Но я не хочу, чтобы мы из-за этого начинали контролировать, с кем каждая разговаривает."
    cs_narrator "Я покачала головой."
    cs_ls "И я не хочу."
    cs_narrator "Пауза."
    cs_ls "Прости. Наверное, у меня просто совсем нет опыта в таких вещах."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья чуть улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я заметила."
    cs_narrator "Я приложила ладонь к груди."
    cs_ls "Как жестоко."
    cs_narrator "Она рассмеялась."
    cs_da "Зато честно."
    cs_narrator "Я тоже улыбнулась."
    cs_narrator "Несколько секунд мы стояли рядом."
    cs_narrator "Потом Дарья произнесла:"
    cs_da "Знаешь, мне нравится, что ты можешь говорить прямо."
    cs_narrator "Я посмотрела на неё."
    cs_da "Даже если иногда сначала говоришь, а потом думаешь."
    cs_ls "Это моя профессиональная особенность."
    cs_da "Вот только иногда можно немного подумать заранее."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Попробую внедрить в следующем обновлении."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья усмехнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Главное, чтобы оно когда-нибудь вышло."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И рассмеялась."
    cs_th "Всё."
    cs_th "Она окончательно освоила мои методы."
    cs_narrator "Но почему-то меня это совершенно не раздражало."
    cs_narrator "Наоборот."
    cs_narrator "Мне нравилось, что она больше не боялась отвечать."
    cs_narrator "Что могла спокойно пошутить."
    cs_narrator "Не согласиться."
    cs_narrator "Сказать, когда ей что-то не нравится."
    cs_narrator "И при этом продолжала идти рядом."
    cs_th "Вчера я боялась даже произнести вслух, что она мне нравится."
    cs_th "Сегодня мы уже можем смеяться над моей неопытностью."
    cs_th "Пожалуй, это тоже прогресс."
    return
