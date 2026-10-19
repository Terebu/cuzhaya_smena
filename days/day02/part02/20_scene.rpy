# -*- coding: utf-8 -*-
label cs_day02_20:
    $ save_name = "Чужая смена — День 2: Перед линейкой"
    stop cs_piano fadeout 1.0
    $ cs_director_scene("bg ext_musclub_day")
    scene bg ext_musclub_day
    $ cs_part02_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part02_s20:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы вышли из музыкального кружка."
    cs_narrator "Солнце уже поднялось выше."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part02_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "На дорожках становилось заметно оживлённее."
    cs_narrator "Кто-то торопился к площади."
    cs_narrator "Кто-то разговаривал у домиков."
    cs_narrator "Издалека доносился голос вожатой, призывавшей пионеров не задерживаться."
    cs_narrator "Я взглянула на Дарью."
    cs_ls "Ну что, товарищ пианистка."
    cs_narrator "Она посмотрела на меня."
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
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не начинай."
    cs_ls "Я всего лишь хотела спросить, почему ты вчера не рассказала, что умеешь играть."
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
    show cs_darya explaining pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Потому что ты вчера была занята куда более важными вопросами."
    cs_narrator "Я задумалась."
    cs_ls "Автобус. Будущее. Советская электроника."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И собственное признание."
    cs_narrator "Я покосилась на неё."
    cs_narrator "Она слегка улыбнулась."
    cs_ls "Это тоже было важное событие."
    cs_da "Я заметила."
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "Затем я спросила:"
    cs_ls "А почему перестала играть?"
    cs_narrator "Даша немного подумала."
    cs_da "Не знаю. Другие дела появились. Потом просто не возвращалась к этому."
    cs_narrator "Я кивнула."
    cs_ls "Понимаю."
    cs_narrator "Она посмотрела на меня."
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
    show cs_darya ear_touch pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Правда?"
    cs_ls "Конечно. У меня тоже были рисунки, которые я откладывала на месяц, а потом находила спустя полгода."
    cs_narrator "Дарья улыбнулась."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только пианино сложнее убрать в папку."
    cs_narrator "Я рассмеялась."
    cs_ls "Аргумент принят."
    cs_narrator "Она взглянула в сторону клуба."
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
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Знаешь, я рада, что попробовала."
    cs_ls "Я тоже."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хотя пальцы действительно почти всё забыли."
    cs_narrator "Я чуть улыбнулась."
    cs_ls "Значит, будет повод попробовать ещё раз."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Если у Мику найдётся время."
    cs_ls "Думаю, с её энтузиазмом это вопрос скорее к нам."
    cs_narrator "Она рассмеялась."
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_part02_cg = False
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part02_square:
    cs_narrator "Мы подошли к площади."
    cs_narrator "Пионеры постепенно выстраивались перед Ольгой Дмитриевной."
    cs_narrator "Семён стоял немного в стороне, оглядывая собравшихся."
    cs_narrator "Увидев нас, он помахал рукой."
    cs_narrator "Я ответила."
    cs_narrator "И тут заметила кое-что любопытное."
    cs_narrator "Ещё вчера весь лагерь казался мне набором знакомых персонажей и событий."
    cs_narrator "Сегодня же я уже успела обнаружить, что Даша умеет играть на пианино."
    cs_narrator "Познакомиться с девушкой, которая может говорить почти без остановки и совершенно искренне любит музыку."
    cs_narrator "И провести с ними время, вообще не обсуждая возвращение домой."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она стояла рядом, поправляя галстук."
    cs_narrator "Потом улыбнулась мне."
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
    $ cs_part02_cast = ["cs_darya"]
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
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я покачала головой."
    cs_ls "Ничего. Просто хорошее получилось утро."
    cs_da "Даже с исчезнувшим автобусом?"
    cs_narrator "Я ненадолго задумалась."
    cs_ls "Хорошее утро и хорошие новости — не всегда одно и то же."
    cs_narrator "Дарья кивнула."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_part02_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "С этим согласна."
    cs_narrator "Со стороны площади раздался голос Ольги Дмитриевны."
    cs_mt "Ребята, не задерживаемся! Начинаем!"
    cs_narrator "Я вздохнула."
    cs_ls "Всё. Музыкальная часть закончилась. Начинается административная."
    cs_narrator "Дарья усмехнулась."
    cs_narrator "Мы направились к остальным."
    cs_th "Второй день продолжался."
    cs_th "И впереди, судя по выражению лица Ольги Дмитриевны, нас уже ждали новые поручения."
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
    $ cs_part02_live = False
    return
