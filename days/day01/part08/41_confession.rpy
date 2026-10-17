# -*- coding: utf-8 -*-
label cs_day01_41:
    $ save_name = "Чужая смена — День 1: Неожиданное признание"
    label cs_check_day01_part08_private:
    $ renpy.music.set_volume(0.28,delay=1.0,channel="music")
    play music "sound/music/get_to_know_me_better.ogg" fadeout 2.0 fadein 3.0
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы остановились у края дорожки."
    cs_narrator "Солнце медленно опускалось за деревья."
    cs_narrator "На земле вытянулись длинные тени."
    cs_narrator "Где-то неподалёку разговаривали пионеры, но сам участок дорожки оставался почти пустым."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Затем отвела взгляд."
    cs_th "Ну давай, Соколова."
    cs_th "С Ольгой Дмитриевной спорить можешь."
    cs_th "Семёна вопросами засыпать можешь."
    cs_th "Даже советским инженерам рассказать о технологиях будущего не постеснялась."
    cs_th "А сейчас внезапно закончились слова."
    cs_narrator "Я тихо вздохнула."
    cs_ls "У меня никогда не было отношений."
    # cs_darya_variety: reaction
    show cs_darya surprise_hand pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья моргнула."
    cs_narrator "Кажется, такого начала она не ожидала."
    cs_da "Совсем?"
    cs_ls "Угу."
    cs_narrator "Я пожала плечами."
    cs_ls "Как-то не сложилось."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему?"
    cs_narrator "Я задумалась."
    cs_ls "Не знаю. Наверное, мне слишком хорошо было одной."
    cs_narrator "Немного помолчала."
    cs_ls "Или просто не встречался человек, ради которого хотелось бы что-то менять."
    cs_narrator "Дарья внимательно смотрела на меня."
    cs_narrator "На этот раз без улыбки."
    cs_da "Но у тебя ведь много знакомых?"
    cs_ls "В основном в интернете."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это другое."
    cs_ls "Вот именно."
    cs_narrator "Я поправила галстук."
    cs_narrator "Не потому, что он мешал."
    cs_narrator "Просто нужно было чем-то занять руки."
    label cs_check_day01_part08_confession:
    cs_ls "В общем… Кажется, ты мне нравишься."
    pause 1.0
    show cs_darya surprise_hand pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья остановилась совершенно неподвижно."
    cs_narrator "Несколько секунд она просто смотрела на меня."
    cs_narrator "Потом чуть наклонила голову."
    cs_da "В каком смысле?"
    cs_narrator "Я усмехнулась."
    cs_ls "Боюсь, в самом очевидном."
    pause 0.5
    cs_ls "Не только как соседка по домику."
    # cs_darya_variety: reaction
    show cs_darya shy_bend pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья отвела взгляд."
    cs_narrator "На её лице появилось выражение человека, которому только что сообщили нечто неожиданное, но не обязательно неприятное."
    cs_da "Лен…"
    cs_ls "Да?"
    # cs_darya_variety: reaction
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы знакомы всего один день."
    cs_ls "Знаю."
    cs_da "Даже меньше."
    cs_ls "Формально — несколько часов. Статистика неумолима."
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она чуть улыбнулась."
    cs_da "И ты уже говоришь такие вещи?"
    cs_narrator "Я ненадолго задумалась."
    cs_ls "Ну… Если учитывать обычное знакомство, наверное, рановато."
    cs_narrator "Я посмотрела на дорожку."
    cs_ls "Но сегодня у нас получилось далеко не обычное знакомство."
    cs_narrator "Дарья ничего не ответила."
    cs_narrator "Я продолжила:"
    cs_ls "Хотя это не означает, что ты обязана что-то отвечать прямо сейчас."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда почему решила сказать?"
    cs_narrator "Вот здесь уже пришлось подумать серьёзнее."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Потому что не хочу делать вид, будто ничего не чувствую."
    pause 0.8
    cs_ls "Сама ещё не до конца понимаю, что с этим делать."
    cs_narrator "Дарья немного расслабилась."
    cs_da "Похоже, впервые за день ты действительно растерялась."
    cs_ls "Не распространяй эту информацию. Пострадает репутация."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она тихо рассмеялась."
    cs_narrator "И мне тоже стало немного легче."
    return
