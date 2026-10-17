# -*- coding: utf-8 -*-
label cs_day02_58a:
    $ save_name = "Чужая смена — День 2: Без библиотечной полиции"
    $ cs_part07_live = False
    $ cs_part08_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part08_s58a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Подожди меня минуту. Я только поздороваюсь."
    cs_narrator "Она улыбнулась."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо."
    cs_narrator "Семён устроился обратно на лавочке."
    cs_sy "Мы здесь."
    cs_narrator "Я кивнула."
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
    $ cs_part08_cast = []
    cs_narrator "И направилась к Жене."
    cs_narrator "На этот раз без попыток подкрасться."
    cs_narrator "Без специальных голосов."
    cs_narrator "Даже без предварительного торжественного объявления."
    cs_narrator "Просто подошла немного ближе."
    cs_ls "Женя, привет."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part08_zhenya:
    cs_narrator "Она подняла взгляд."
    cs_narrator "Узнала меня."
    cs_narrator "И остановилась."
    cs_mz "А, Соколова. Привет."
    cs_narrator "Она посмотрела на мою руку."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Что случилось?"
    cs_narrator "Я подняла перевязанный локоть."
    cs_ls "Неудачно споткнулась. Виола уже обработала."
    cs_narrator "Женя нахмурилась."
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда осторожнее ходи."
    cs_ls "Сегодня это самое популярное пожелание в мой адрес."
    cs_narrator "Она чуть заметно улыбнулась."
    cs_mz "Значит, не зря желают."
    cs_narrator "Я усмехнулась."
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "Потом я всё-таки произнесла то, ради чего подошла."
    cs_ls "Слушай, я вообще-то хотела сказать спасибо."
    cs_narrator "Женя посмотрела на меня с явным удивлением."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "За что?"
    cs_ls "За вчерашний разговор."
    cs_narrator "Она приподняла бровь."
    cs_mz "За тот, где ты рассказывала, что приехала из будущего?"
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_narrator "Женя немного помолчала."
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Я ведь так тебе и не поверила."
    cs_ls "Знаю."
    cs_narrator "Я посмотрела на книги в её руках."
    cs_narrator "Потом снова на неё."
    cs_ls "Но ты хотя бы выслушала. И не стала делать вид, будто я обязана немедленно доказать каждое слово."
    cs_narrator "Она поправила очки."
    cs_mz "Потому что доказательств у тебя не было."
    cs_narrator "Я улыбнулась."
    cs_ls "И сейчас нет."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда что изменилось?"
    cs_narrator "Я немного подумала."
    cs_ls "Наверное, то, что я начинаю понимать: для остальных всё это звучит гораздо страннее, чем для меня."
    cs_narrator "Женя некоторое время смотрела на меня."
    cs_narrator "Затем вздохнула."
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вот это уже похоже на здравую мысль."
    cs_narrator "Я кивнула."
    cs_ls "Иногда они у меня появляются."
    cs_narrator "Она чуть заметно улыбнулась."
    cs_mz "Я заметила."
    cs_narrator "Потом посмотрела на книги."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ладно, мне надо идти. Ты ведь ничего не хотела взять?"
    cs_narrator "Я покачала головой."
    cs_ls "Сегодня нет. Но, возможно, завтра загляну. Хотела узнать, есть ли у вас карты окрестностей."
    cs_narrator "Женя задумалась."
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Карты? Не помню. Можешь зайти, посмотрим по каталогу. Только не обещаю, что найдётся именно то, что нужно."
    cs_narrator "Я улыбнулась."
    cs_ls "Этого вполне достаточно."
    cs_narrator "Она кивнула."
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_part08_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда до завтра. И руку береги."
    cs_ls "Постараюсь. Пока."
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
    $ cs_part08_cast = []
    label cs_check_part08_zhenya_left:
    cs_narrator "Женя пошла дальше."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_zhenya"])
    with cs_sprite_leave
    label cs_director_check_cfa97b59ef:
    # cs_director_end
    cs_narrator "Я проводила её взглядом."
    cs_th "Вот так."
    cs_th "Без скандалов."
    cs_th "Без споров об устройстве мироздания."
    cs_th "И даже с приглашением прийти в библиотеку."
    cs_narrator "Кажется, нормальное человеческое общение постепенно переставало быть для меня чем-то совершенно непостижимым."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part08_rejoined:
    cs_narrator "Я вернулась к лавочке."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну как?"
    cs_narrator "Я улыбнулась."
    cs_ls "Представляешь, меня не выгнали."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Семён рассмеялся."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вы даже не в библиотеке были."
    cs_narrator "Я посмотрела на него."
    cs_ls "Не разрушай достижение."
    return
