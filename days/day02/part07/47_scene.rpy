# -*- coding: utf-8 -*-
label cs_day02_47:
    $ save_name = "Чужая смена — День 2: Когда разговор интереснее дороги"
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
    # cs_presence_keep: hide cs
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.17, channel="music", delay=1.0)
    if cs_met_viola and cs_lena_elbow_injury_day2 == 0:
        $ cs_lena_elbow_bandaged = True
        $ cs_lena_elbow_injury_day2 = 1
    label cs_check_part07_s47:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После разговора о дороге мы некоторое время шли молча."
    cs_narrator "Семён уже отправился по своим делам, а мы с Дашей свернули на дорожку, ведущую к домикам."
    # cs_director_begin: REFLECTIVE_SHOT: Camp panorama and repeated road result
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_26d6918502:
    # cs_director_end
    cs_narrator "Лагерь продолжал жить обычной жизнью."
    cs_narrator "Где-то за деревьями смеялись пионеры."
    cs_narrator "Возле площади слышались голоса."
    cs_narrator "Ветер лениво шевелил листья, и солнечный свет то появлялся на дорожке, то снова исчезал в тени."
    cs_narrator "Всё выглядело настолько обыкновенно, что иногда хотелось усомниться в собственных воспоминаниях."
    cs_th "Может, мы действительно что-то перепутали?"
    cs_th "Два раза?"
    cs_th "Втроём?"
    cs_narrator "Я вздохнула."
    cs_narrator "Нет."
    cs_narrator "Что бы ни происходило с дорогой, нам удалось повторить результат."
    cs_narrator "Контрольная точка появлялась перед нами после движения в одном направлении."
    cs_narrator "И никакой понятной причины этого мы пока не нашли."
    # cs_director_begin: Return to direct interaction: Camp panorama and repeated road result
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_f19bef7987:
    # cs_director_end
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она шла рядом, задумчиво разглядывая деревья."
    cs_ls "Слушай."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "М?"
    cs_ls "А ведь есть у всей этой истории одна положительная сторона."
    cs_narrator "Она медленно повернулась ко мне."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "После дороги я уже начинаю бояться твоих положительных сторон."
    cs_narrator "Я приложила ладонь к груди."
    cs_ls "Какое недоверие."
    cs_da "За два дня у меня накопилось достаточно наблюдений."
    cs_narrator "Я задумалась."
    cs_ls "Тогда ты прекрасно подходишь для нашей научной группы."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И всё-таки. Какая сторона?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Немного помолчала."
    cs_ls "Мы хотя бы выяснили, что не можем просто сесть в первый попавшийся автобус и уехать."
    cs_da "Это положительная сторона?"
    cs_ls "Ну… теперь не будем тратить время на поиски автобусной остановки."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Несколько секунд молчала."
    cs_narrator "А потом рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен, у тебя совершенно особенное представление об оптимизме."
    cs_ls "Приходится приспосабливаться."
    cs_narrator "Мы прошли ещё немного."
    cs_narrator "Даша задумчиво произнесла:"
    cs_da "Но ведь не обязательно, что из лагеря вообще нет выхода."
    cs_narrator "Я кивнула."
    cs_ls "Конечно. Мы проверили только одну дорогу и только одним способом."
    cs_da "Значит, пока не стоит делать окончательные выводы."
    cs_ls "Согласна."
    cs_narrator "Я улыбнулась."
    cs_ls "Представляешь, мы теперь даже умеем соглашаться с неопределённостью."
    cs_da "Грандиозное достижение."
    cs_ls "Следующий этап — перестать находить новые загадки каждые полчаса."
    cs_da "А вот в это я уже не верю."
    cs_narrator "Я рассмеялась."
    cs_narrator "Она улыбнулась в ответ."
    cs_narrator "И пошла чуть впереди, обходя выступавший из травы камень."
    cs_narrator "Я ускорила шаг, чтобы догнать её."
    cs_ls "Эй, я ещё не закончила свой аргумент!"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Он у тебя вообще когда-нибудь заканчивается?"
    cs_ls "Иногда. Обычно когда заканчиваются слушатели."
    cs_narrator "Она рассмеялась, не оборачиваясь."
    cs_narrator "Я тоже улыбнулась."
    cs_narrator "Повернула голову в её сторону."
    cs_narrator "И совершенно перестала смотреть под ноги."
    cs_th "Как выяснилось, зря."
    return
