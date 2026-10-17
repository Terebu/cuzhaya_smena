# -*- coding: utf-8 -*-
label cs_day02_08:
    $ save_name = "Чужая смена — День 2: Общий подъём"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/int_cabin_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    stop music fadeout 2.0
    label cs_check_new_d2_s08:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я подошла к шкафу."
    cs_narrator "Достала чистую пионерскую рубашку."
    cs_narrator "Положила рядом с юбкой."
    cs_narrator "Спортивную одежду пока решила не снимать: сначала нужно было дойти до умывальников."
    cs_narrator "Дарья тем временем заправляла кровать."
    cs_narrator "Движения у неё были спокойные."
    cs_narrator "Никакой спешки."
    cs_narrator "Я посмотрела на неё и невольно задумалась."
    cs_narrator "Ещё два дня назад мы даже не знали друг друга."
    cs_narrator "А теперь жили в одном домике, собирались вместе на завтрак и обсуждали исчезновение автобуса так, будто это обычная бытовая проблема."
    cs_th "Хорошо хоть не коммунальные платежи."
    cs_narrator "Я усмехнулась."
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
    cs_da "Что?"
    cs_ls "Думаю, насколько быстро меняется жизнь."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_da "В хорошем смысле?"
    cs_narrator "Я немного помолчала."
    cs_ls "Пока не знаю."
    cs_narrator "Потом улыбнулась."
    cs_ls "Но кое-что в ней мне уже нравится."
    cs_narrator "Дарья отвела взгляд."
    cs_narrator "На губах появилась лёгкая улыбка."
    cs_narrator "Она ничего не ответила."
    cs_narrator "И я не стала требовать ответа."
    cs_narrator "Мы уже достаточно поговорили об этом вчера."
    cs_narrator "А сегодня хотелось просто начать день."
    play sound "sound/sfx/dinner_horn_processed.ogg"
    cs_narrator "В этот момент снаружи раздался горн."
    cs_narrator "Я невольно вздрогнула."
    cs_ls "Ох."
    cs_narrator "Дарья посмотрела в сторону окна."
    cs_da "Полагаю, это подъём."
    cs_narrator "Я кивнула."
    cs_ls "Полагаю, да."
    cs_narrator "Она улыбнулась."
    cs_da "А ты уже успела столько всего сделать."
    cs_narrator "Я задумалась."
    cs_narrator "Пробежка."
    cs_narrator "Турники."
    cs_narrator "Ольга Дмитриевна."
    cs_narrator "Семён."
    cs_narrator "Исчезнувший автобус."
    cs_narrator "И ни одного окончательного ответа."
    cs_ls "Утро оказалось продуктивным."
    cs_da "Особенно для человека, который ещё даже не позавтракал."
    cs_narrator "Я рассмеялась."
    cs_ls "Согласна. Пора исправлять."
    cs_narrator "Даша уже переоделась в пионерскую форму. Я пока осталась в спортивной одежде: чистую рубашку решила надеть после умывания."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья взяла полотенце."
    cs_narrator "Я — своё."
    cs_narrator "Перед выходом ещё раз посмотрела на телефон, лежавший на тумбочке."
    cs_th "Подожди немного."
    cs_th "Сегодня до тебя тоже доберёмся."
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    play music "sound/music/feeling_good.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    cs_narrator "Мы вышли на крыльцо."
    cs_narrator "Лагерь окончательно проснулся."
    cs_narrator "По дорожкам уже шли пионеры."
    cs_narrator "Откуда-то доносился смех."
    cs_narrator "Вдалеке хлопнула дверь."
    cs_narrator "А рядом со мной стояла Дарья."
    cs_narrator "Обычная девушка из Москвы, с которой я вчера совершенно случайно оказалась в совершенно необычном месте."
    cs_narrator "И почему-то именно это сейчас казалось самым надёжным обстоятельством."
    cs_narrator "Я повернулась к ней."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Ну что, товарищ соседка. Пойдём приводить себя в порядок?"
    cs_narrator "Дарья усмехнулась."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Пойдём, товарищ спортсменка."
    cs_narrator "Мы спустились с крыльца."
    cs_th "Второй день начался."
    cs_th "И, кажется, скучным он уже не будет."
    return
