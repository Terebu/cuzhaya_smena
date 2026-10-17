# -*- coding: utf-8 -*-
label cs_day02_39:
    $ save_name = "Чужая смена — День 2: Небольшое обещание"
    $ cs_part04_live = False
    $ cs_part05_live = True
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
    # cs_global_transition
    with cs_sprite_change
    $ cs_part05_cg = False
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.1, channel="ambience", delay=1.0)
    label cs_check_part05_s39:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы свернули в сторону площади."
    cs_narrator "Вдалеке уже слышались голоса пионеров, возвращавшихся с утренних занятий."
    cs_narrator "Солнце стояло почти над деревьями."
    cs_narrator "До обеда оставалось не так много времени."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Знаешь, я сегодня кое-что поняла."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что именно?"
    cs_narrator "Я немного подумала."
    cs_ls "Вчера я почти всё время пыталась выяснить, как вернуться домой."
    cs_narrator "Она кивнула."
    cs_ls "А сегодня успела порисовать, познакомиться с Мику, пообщаться со Славей и даже посетить медпункт."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Довольно насыщенная программа."
    cs_ls "И всё это без работающего телефона."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Удивительно, правда?"
    cs_narrator "Я рассмеялась."
    cs_ls "Не то слово."
    cs_narrator "Некоторое время мы шли молча."
    cs_narrator "Затем я посмотрела на неё серьёзнее."
    cs_ls "Даш."
    cs_narrator "Она повернулась."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да?"
    cs_ls "Я всё ещё хочу домой."
    cs_narrator "Она кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я тоже."
    cs_ls "И не собираюсь делать вид, будто этот лагерь — просто длинные каникулы."
    cs_da "Я понимаю."
    cs_narrator "Я ненадолго остановилась."
    cs_ls "Но, наверное, пока мы здесь, можно хотя бы иногда позволять себе обычные вещи."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Например?"
    cs_narrator "Я задумалась."
    cs_ls "Рисовать. Слушать музыку. Общаться с людьми."
    cs_narrator "Пауза."
    cs_ls "И не превращать каждую прогулку в экспедицию по поиску пространственно-временных аномалий."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне нравится этот план."
    cs_narrator "Я кивнула."
    cs_ls "Тогда договорились."
    if renpy.music.get_playing() != "sound/music/a_promise_from_distant_days.ogg":
        play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.17, channel="music", delay=1.0)
    cs_narrator "Она протянула мне руку."
    cs_narrator "Не торжественно."
    cs_narrator "Просто чуть повернула ладонь навстречу."
    cs_narrator "Я посмотрела на неё."
    $ cs_director_scene("cs_cg_lena_darya_hand_in_hand_day")
    scene cs_cg_lena_darya_hand_in_hand_day
    $ cs_part05_cg = True
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
    $ cs_part05_cast = []
    with Dissolve(1.0)
    label cs_check_part05_hand_in_hand:
    cs_narrator "Потом осторожно взяла."
    cs_narrator "Мы прошли несколько шагов рядом."
    cs_narrator "И я почувствовала, что снова начинаю улыбаться."
    cs_th "Интересно."
    cs_th "Оказывается, мне нравится не только рассказывать о собственных чувствах."
    cs_th "Иногда гораздо приятнее просто услышать другого человека."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Лен?"
    cs_ls "М?"
    cs_da "Только одна просьба."
    cs_narrator "Я насторожилась."
    cs_ls "Какая?"
    cs_narrator "Она сделала совершенно серьёзное лицо."
    cs_da "Если ещё раз решишь провести научное исследование чужой красоты, предупреждай заранее."
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела на неё."
    cs_narrator "Несколько секунд пыталась придумать достойный ответ."
    cs_narrator "Не получилось."
    cs_narrator "Дарья рассмеялась первой."
    cs_narrator "Я тоже."
    cs_ls "Всё. Признаю поражение."
    cs_da "Второе за утро?"
    cs_narrator "Я задумалась."
    if cs_day02_miku_listened:
        cs_narrator "Вспомнила высокую лавку в музыкальном кружке."
    else:
        cs_narrator "Вспомнила утренний спор с карандашом."
    cs_narrator "Потом улыбнулась."
    if cs_day02_miku_listened:
        cs_ls "Да. Сначала советская мебель, теперь ты."
    else:
        cs_ls "Да. Сначала бумага без Ctrl+Z, теперь ты."
    cs_narrator "Она пожала мою руку чуть крепче."
    cs_da "Насыщенный день."
    cs_narrator "Я кивнула."
    cs_ls "И ведь ещё даже не обед."
    cs_narrator "Мы продолжили путь."
    cs_narrator "Впереди показалась знакомая площадь."
    cs_narrator "Издалека виднелось наше объявление."
    cs_narrator "Семён со Славей уже ушли по своим делам."
    cs_narrator "А мне впервые за долгое время совершенно не хотелось никуда торопиться."
    cs_th "Пусть сегодня хотя бы немного всё идёт своим чередом."
    cs_th "У нас ещё будет время для вопросов."
    cs_th "А пока…"
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она улыбнулась мне в ответ."
    cs_th "Пока можно просто идти рядом."
    stop music fadeout 3.0
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    $ cs_day02_part05_complete = True
    label cs_check_part05_walk_ready:
    pause 0.5
    return
