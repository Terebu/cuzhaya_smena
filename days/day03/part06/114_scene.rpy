# -*- coding: utf-8 -*-
label cs_day03_114:
    $ save_name = "Чужая смена — День 3: Музыка после концерта"
    $ cs_director_scene("bg ext_musclub_day")
    scene bg ext_musclub_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    stop music fadeout 1.5
    stop cs_piano fadeout 0.5
    label cs_check_day03_114_exterior:
    cs_narrator "Ещё подходя к музыкальному клубу, я услышала знакомые звуки."
    cs_narrator "Сначала несколько отдельных нот."
    cs_narrator "Потом короткий перебор гитары."
    cs_narrator "Затем ещё одну попытку, на этот раз чуть увереннее."
    cs_narrator "Я остановилась возле двери."
    cs_th "Так."
    cs_th "Кажется, творческая деятельность здесь вообще не прекращается."
    cs_th "Вчера концерт, сегодня уже репетиция."
    cs_th "У музыкантов, видимо, собственное представление о выходных."
    cs_narrator "Дарья прислушалась."
    cs_narrator "И почти сразу улыбнулась."
    cs_da "Кто-то играет."
    cs_narrator "Я повернулась к ней."
    cs_ls "Неужели? А я подумала, что у нас в клубе поселился очень музыкальный дятел."
    cs_narrator "Она рассмеялась."
    cs_da "Лен."
    cs_narrator "Я улыбнулась."
    cs_ls "Ладно, идём."
    cs_narrator "Я постучала."
    cs_narrator "Изнутри раздалось:"
    cs_mi "Входите!"
    $ cs_director_scene("bg int_musclub_day")
    scene bg int_musclub_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show mi normal pioneer at cs_actor_left
    show dv normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ renpy.music.set_volume(0.07,delay=1.0,channel="ambience")
    label cs_check_day03_114_cast:
    cs_narrator "Мы открыли дверь."
    cs_narrator "Мику сидела возле пианино с несколькими листами нот."
    cs_narrator "Алиса расположилась неподалёку с гитарой."
    cs_narrator "Она как раз проверяла настройку одной из струн."
    cs_narrator "Увидев нас, Мику радостно подняла голову."
    cs_mi "Ой, Лена! Даша! Привет!"
    cs_ls "Привет."
    cs_da "Доброе утро."
    cs_narrator "Алиса посмотрела на нас."
    cs_dv "Здорово."
    cs_narrator "Я кивнула."
    cs_ls "И тебе привет, главная гитаристка вчерашнего вечера."
    if renpy.showing("dv"):
        show dv normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса прищурилась."
    cs_dv "Это сейчас было серьёзно или ты опять что-нибудь придумала?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Алиса, иногда я говорю совершенно нормальные вещи."
    cs_dv "Вот именно это и настораживает."
    cs_narrator "Дарья тихо рассмеялась."
    if renpy.showing("mi"):
        show mi smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику улыбнулась."
    cs_mi "Мы как раз обсуждали вчерашнее выступление! Получилось ведь хорошо, правда? Конечно, некоторые места можно было сыграть чуть иначе, но в целом мне понравилось, и Алиса тоже сказала, что было неплохо, хотя она сначала вообще не хотела обсуждать…"
    cs_dv "Мику."
    cs_mi "Что?"
    cs_dv "Дай людям хотя бы войти."
    cs_narrator "Мику моргнула."
    cs_narrator "Потом засмеялась."
    cs_mi "Ой, точно! Проходите, конечно!"
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Видишь? В некоторых вопросах я всё-таки образец сдержанности."
    if renpy.showing("dv"):
        show dv grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса усмехнулась."
    cs_dv "Не обольщайся."
    cs_th "Ага."
    cs_th "Кажется, у нас появился ещё один человек, который не собирается подыгрывать моим заявлениям."
    cs_narrator "Мы прошли внутрь."
    cs_narrator "Я посмотрела на пианино."
    cs_narrator "Потом на разложенные ноты."
    cs_ls "А что вы теперь репетируете? Концерт ведь уже состоялся."
    cs_narrator "Мику кивнула."
    cs_mi "Да, но это не значит, что нужно переставать играть! Иногда после выступления даже интереснее заниматься, потому что сразу слышишь, что получилось хорошо, а что хочется исправить. Вот, например, вчера мы начинали одну песню с короткого вступления, а сейчас я думаю, что его можно немного изменить…"
    if renpy.showing("dv"):
        show dv grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса усмехнулась."
    cs_dv "А я думаю, что песню сначала стоит просто сыграть без десяти новых вариантов."
    cs_mi "Но варианты тоже интересны!"
    cs_dv "Не спорю."
    cs_narrator "Я посмотрела на них."
    cs_th "Прекрасно."
    cs_th "Творческие разногласия."
    cs_th "Удивительно знакомая ситуация."
    cs_ls "Как художник официально сообщаю: спор о том, какой вариант лучше, может продолжаться бесконечно."
    cs_narrator "Алиса посмотрела на меня."
    cs_dv "Ты рисуешь?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Собственно, плакат для вчерашнего концерта мы тоже делали вместе."
    cs_dv "А, тот самый."
    cs_narrator "Она слегка улыбнулась."
    cs_dv "Нормально получилось."
    cs_narrator "Я приподняла бровь."
    cs_ls "Из твоих уст это звучит почти как премия."
    if renpy.showing("mi"):
        show mi laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику рассмеялась."
    cs_mi "А мне очень понравился! Я хотела потом сказать, но мы вчера столько всего делали, а после концерта уже было поздно…"
    if cs_mi_intro_revised:
        cs_narrator "Мику посмотрела на Дарью."
        cs_mi "И ещё спасибо за то, что вы тогда послушали наше вступление. Помните, мы немного изменили его перед концертом?"
        cs_narrator "Дарья кивнула."
        cs_da "Конечно."
        cs_narrator "Я улыбнулась."
        cs_ls "Помню. Ты тогда так увлеклась, что я уже начала подозревать: мы случайно попали на закрытую репетицию."
        cs_narrator "Мику засмеялась."
        cs_mi "Но вы ведь не против были!"
        cs_ls "Конечно нет. Мне понравилось."
        cs_narrator "Она улыбнулась ещё шире."
    else:
        cs_narrator "Мику аккуратно сложила часть нот."
        cs_mi "Жалко только, что вчера у нас было не так много времени спокойно поговорить после концерта."
        cs_narrator "Я кивнула."
        cs_ls "Зато сегодня, кажется, никто никуда не торопится."
        cs_narrator "Она улыбнулась."
        cs_mi "Вот именно!"
    if cs_sl_poster_collected_day3 and cs_day03_poster_location == "darya_folder":
        cs_narrator "Перед тем как подойти к клавишам, Дарья положила папку с плакатом на свободный чистый стул."
        $ cs_day03_poster_location = "music_club_chair"
    cs_narrator "Дарья подошла к пианино."
    cs_narrator "Провела взглядом по клавишам."
    cs_narrator "Мику сразу заметила это."
    cs_mi "Даша, хочешь ещё поиграть? Вчера у тебя хорошо получилось."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья немного смутилась."
    cs_da "Да я не уверена, что хорошо помню."
    cs_mi "Ну и ничего! Можно просто попробовать."
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она на секунду встретилась со мной взглядом."
    cs_da "Только без комментариев, ладно?"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Обещаю не проводить публичную экспертизу."
    if renpy.showing("dv"):
        show dv grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса усмехнулась."
    cs_dv "Уже звучит подозрительно."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    label cs_check_day03_114_darya_piano:
    cs_narrator "И осторожно коснулась клавиш."
    cs_narrator "Раздались несколько нот."
    cs_narrator "Поначалу немного неуверенных."
    cs_narrator "Затем она повторила последовательность."
    cs_narrator "На этот раз ровнее."
    cs_narrator "Мику внимательно слушала."
    cs_narrator "Алиса перестала перебирать струны."
    cs_narrator "Я тоже замолчала."
    cs_th "Вот ведь."
    cs_th "Она снова говорит, что почти ничего не помнит."
    cs_th "А потом садится и делает то, на что я способна разве что в воображении."
    label cs_check_day03_114_darya_finished:
    cs_narrator "Дарья закончила короткую мелодию."
    cs_narrator "Посмотрела на Мику."
    cs_da "Примерно так."
    if renpy.showing("mi"):
        show mi smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мику улыбнулась."
    cs_mi "Очень хорошо! Ты просто давно не занималась."
    cs_narrator "Дарья пожала плечами."
    cs_da "Возможно."
    cs_narrator "Я чуть улыбнулась."
    cs_ls "Мне понравилось."
    cs_narrator "Она посмотрела на меня."
    cs_da "Спасибо."
    cs_narrator "На этот раз я не стала ничего добавлять."
    cs_narrator "Иногда этого действительно достаточно."
    return
