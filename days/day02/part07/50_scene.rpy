# -*- coding: utf-8 -*-
label cs_day02_50:
    $ save_name = "Чужая смена — День 2: Повязка номер два"
    $ cs_part06_live = False
    $ cs_part07_live = True
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
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.13, channel="music", delay=1.0)
    label cs_check_part07_s50:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Через некоторое время Виола закончила."
    $ cs_lena_elbow_bandaged = True
    $ cs_lena_bandage_damaged = False
    $ cs_lena_no_sport_day2 = True
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
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_bandaged:
    cs_narrator "Повреждённый участок закрывала свежая повязка."
    cs_narrator "Рука выглядела значительно аккуратнее, чем десять минут назад."
    cs_narrator "Я осторожно посмотрела на результат."
    cs_ls "Надо же. Теперь даже похоже на нормальную медицинскую помощь."
    cs_narrator "Виола посмотрела на меня."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "А раньше было похоже на что?"
    cs_ls "На последствия неудачного знакомства с местной флорой."
    cs_narrator "Она улыбнулась."
    cs_vi "Тогда постарайся больше с ней так близко не знакомиться."
    cs_narrator "Я кивнула."
    cs_ls "Учту."
    cs_narrator "Виола убрала использованные материалы."
    cs_narrator "Потом снова посмотрела на меня."
    show cs custom arms_crossed medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Сегодня без пробежек, турников и прочих подвигов. Повязку не трогай, руку лишний раз не травмируй. Если боль усилится, появится выраженный отёк или что-нибудь ещё начнёт беспокоить — сразу приходи."
    cs_ls "То есть спортивная карьера временно приостановлена?"
    show cs custom stern medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "На сегодня — определённо."
    cs_narrator "Я вздохнула."
    cs_ls "Объявляю минуту молчания по утреннему физкультурному плану."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты уже сегодня успела побегать."
    cs_ls "Тем более обидно завершать карьеру на пике формы."
    cs_narrator "Виола покачала головой."
    show cs custom amused medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Лена, ты удивительно разговорчивая пациентка."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Обычно меня считают необщительной."
    cs_vi "Правда?"
    cs_da "Это она сама так считает."
    cs_narrator "Я повернулась к Даше."
    cs_ls "Я вижу, свидетельские показания продолжаются."
    cs_narrator "Она улыбнулась."
    cs_da "Просто уточняю обстоятельства."
    cs_narrator "Виола рассмеялась."
    cs_narrator "Я осторожно пошевелила рукой."
    cs_narrator "Повязка держалась."
    cs_narrator "Боль полностью не исчезла, но стала значительно терпимее."
    cs_ls "А если серьёзно… спасибо."
    cs_narrator "Виола посмотрела на меня."
    cs_ls "За то, что снова пришлось со мной возиться."
    cs_narrator "Она слегка улыбнулась."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Для этого я здесь и работаю."
    cs_narrator "Я кивнула."
    cs_th "И всё-таки."
    cs_th "Теперь, когда самое неприятное осталось позади, захотелось не просто уйти, а хотя бы нормально поговорить."
    cs_th "Хотя Виола, наверное, и без того потратила на меня сегодня слишком много времени."
    return
