# -*- coding: utf-8 -*-
label cs_day03_120:
    $ save_name = "Чужая смена — День 3: Ностальгия по лапше"
    $ cs_actor_exit(["un"])
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_120_bench_left:
    cs_narrator "Мы отошли от скамейки. Дарья шла рядом."
    # cs_inward_beat_10: attention turns inward
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_narrator "Солнце поднялось высоко — утро пролетело незаметно."
    # Return to the same conversation, with the same cast and placement.
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Довольна?"
    cs_narrator "Я улыбнулась."
    cs_ls "Очень."
    cs_da "Что больше всего понравилось?"
    cs_ls "Сложный вопрос."
    cs_narrator "Она приподняла бровь."
    cs_da "Настолько?"
    cs_ls "Сегодня мы снова зашли в музыкальный клуб без обязательства уметь играть. А потом ещё и поговорили о рисунках."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Звучит неплохо."
    cs_ls "Очень неплохо."
    cs_narrator "Немного помолчала."
    cs_ls "А тебе понравилось снова посидеть за пианино?"
    cs_narrator "Дарья посмотрела вперёд. На секунду задумалась."
    cs_da "Да."
    cs_narrator "Потом добавила:"
    cs_da "После долгого перерыва приятно снова привыкать к клавишам."
    cs_narrator "Я повернулась к ней."
    cs_ls "Тогда надо будет повторить."
    cs_narrator "Она улыбнулась."
    cs_da "Может быть."
    cs_narrator "Я прищурилась."
    cs_ls "У тебя это любимая формулировка?"
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Какая?"
    cs_ls "«Может быть»."
    cs_narrator "Она немного помолчала. Потом улыбнулась."
    cs_da "А тебе не нравится?"
    cs_ls "Наоборот. Начинаю понимать, что у неё довольно широкий диапазон значений."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась. Я тоже улыбнулась. Мы продолжили идти."
    $ renpy.music.set_volume(0.06,delay=1.0,channel="music")
    if not cs_day03_lunch_horn_played:
        play sound "sound/sfx/dinner_horn_processed.ogg"
        $ cs_day03_lunch_horn_played = True
    label cs_check_day03_120_horn:
    cs_narrator "И в этот момент над лагерем раздался горн. Я остановилась. Прислушалась. Потом посмотрела в сторону столовой."
    cs_ls "О."
    cs_narrator "Дарья повернулась ко мне."
    cs_da "Что?"
    cs_ls "Обед."
    cs_narrator "Она усмехнулась."
    cs_da "Очень наблюдательно."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Спасибо. Опыт трёх дней позволяет уверенно распознавать основные звуковые сигналы лагеря."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мы пошли в сторону столовой. По дороге я рассказала Дарье, как порой ужинала «Мивиной» над очередным незаконченным рисунком."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она слушала с выражением вежливого антрополога. Мы миновали очередной поворот."
    $ cs_director_scene("bg ext_dining_hall_away_day")
    scene bg ext_dining_hall_away_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ renpy.music.set_volume(0.13,delay=1.0,channel="music")
    label cs_check_day03_120_dining:
    cs_narrator "Возле столовой уже собирались пионеры. Среди них я заметила знакомые светлые косы. Славя. Она разговаривала с Мику."
    cs_narrator "Чуть дальше стояла Алиса. Ульяна что-то оживлённо рассказывала Семёну."
    cs_th "Обычный день. Обычный обед. И, судя по всему, совершенно необычное количество людей, с которыми мне уже хотелось поздороваться."
    cs_narrator "Славя заметила нас. Улыбнулась."
    $ cs_frame_focus(["cs_darya", "sl"])
    with cs_sprite_change
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    label cs_check_day03_120_sl:
    cs_sl "О, вы уже здесь!"
    cs_ls "Конечно. Гастрономические мероприятия стараюсь не пропускать."
    cs_narrator "Она рассмеялась."
    cs_sl "Как рука?"
    cs_narrator "Я посмотрела на повязку."
    cs_ls "Всё ещё на месте. Причём на своём законном."
    cs_narrator "Славя улыбнулась."
    cs_sl "Хорошо."
    cs_narrator "Я вздохнула."
    cs_ls "Похоже, локоть сегодня популярнее меня."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя тоже. Потом посмотрела на нас."
    cs_sl "А что вы обсуждали?"
    cs_narrator "Я серьёзно ответила:"
    cs_ls "Лапшу."
    cs_narrator "Она удивилась."
    cs_sl "Какую?"
    cs_ls "Быстрого приготовления. Заливаешь кипятком, немного ждёшь — и готово."
    cs_narrator "Славя задумалась."
    cs_sl "Как макароны?"
    cs_ls "Отчасти."
    cs_sl "И вкусно?"
    cs_narrator "Я посмотрела куда-то вдаль."
    cs_ls "Иногда замечательно. Иногда хочется потребовать объяснений от производителя."
    cs_narrator "Дарья тихо рассмеялась. Славя улыбнулась."
    cs_sl "А почему ты сейчас о ней вспомнила?"
    cs_narrator "Я задумалась."
    cs_th "Хороший вопрос. Наверное, просто соскучилась по чему-то привычному."
    cs_ls "Иногда хочется еды, которая напоминает о доме."
    cs_narrator "Славя кивнула."
    cs_sl "Понимаю."
    cs_ls "Хотя, если подумать, домашняя еда, пожалуй, вкуснее."
    cs_narrator "Дарья посмотрела на меня. И едва заметно улыбнулась."
    cs_th "Она поняла. Не столько про лапшу, сколько про саму мысль. Про Москву. Про привычные мелочи, которых здесь нет."
    cs_narrator "Славя посмотрела в сторону входа."
    cs_sl "Скоро начнут пускать."
    cs_ls "Отлично. Посмотрим, чем сегодня решил удивить нас общепит."
    if cs_friend_sl >= 2 and cs_helped_sl_day3:
        cs_narrator "Славя чуть понизила голос."
        cs_sl "Кстати, спасибо ещё раз за помощь сегодня."
        cs_ls "Не за что."
        cs_sl "Правда. С вами даже скучная работа проходит веселее."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Осторожнее с такими заявлениями. А то я решу, что меня теперь обязаны приглашать на любую инвентаризацию."
        cs_narrator "Она рассмеялась."
        cs_sl "Тогда буду знать, к кому обращаться."
    else:
        cs_narrator "Славя кивнула на столовую."
        cs_sl "Ладно, пойдём ближе. А то очередь будет большая."
        cs_ls "Разумно."
    cs_narrator "Мы подошли ко входу. Вокруг становилось шумнее. Мику продолжала что-то рассказывать. Алиса лениво прислонилась к ограждению."
    cs_narrator "Семён выглядел так, будто уже успел устать от разговора с Ульяной. Я едва заметно улыбнулась."
    cs_th "Ещё позавчера я бы увидела здесь просто знакомые образы. А теперь каждый из них постепенно становился человеком, которого я знала чуть лучше, чем вчера. И это, пожалуй, было самым интересным."
    cs_narrator "В стороне от общего шума стояла Женя. С книгой под мышкой."
    cs_th "Ну конечно. Единственный человек, способный даже в очереди за обедом создать вокруг себя небольшой островок тишины."
    cs_narrator "Я повернулась к Дарье. Она проследила за моим взглядом. И улыбнулась."
    cs_da "Пойдёшь поздороваться?"
    cs_ls "Да."
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    label cs_check_day03_120_mz:
    cs_narrator "Я подошла к Жене. Остановилась на удобном расстоянии."
    cs_ls "Привет."
    cs_narrator "Она подняла голову."
    cs_mz "Привет."
    cs_ls "На обед?"
    cs_narrator "Женя посмотрела на дверь столовой, потом на меня."
    cs_mz "Нет, просто пришла проверить, существует ли здесь еда."
    cs_narrator "Я замерла. Медленно подняла бровь."
    cs_th "Неплохо."
    cs_narrator "Женя заметила моё выражение. И слегка улыбнулась."
    cs_ls "Понятно. Значит, исследовательские задачи у нас совпадают."
    cs_narrator "Она усмехнулась."
    cs_mz "Похоже на то."
    cs_narrator "Некоторое время мы молчали. Я не стала начинать длинный разговор. Просто стояла рядом."
    if cs_mz_map_lead and cs_mz_catalog_checked_day3:
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Надеюсь, ты не расстроилась из-за каталогов?"
        cs_narrator "Я покачала головой."
        cs_ls "Нет. Мы ведь ничего конкретного не обещали найти."
        cs_narrator "Она кивнула."
        cs_mz "Вот и хорошо. Если появится что-то подходящее, я скажу."
        cs_ls "Спасибо."
    elif cs_mz_book_requested_day3:
        cs_narrator "Женя поправила книгу."
        cs_mz "Насчёт книги помню. После обеда загляни."
        cs_ls "Хорошо."
    else:
        cs_narrator "Женя посмотрела на мою повязку."
        cs_mz "У Виолы была?"
        cs_ls "Да. Всё нормально."
        cs_narrator "Она улыбнулась."
        cs_mz "Хорошо."
    cs_narrator "Дарья остановилась чуть поодаль. Она наблюдала за нами с лёгкой улыбкой. Я посмотрела на неё. Потом снова на Женю."
    cs_narrator "Двери столовой открылись. Пионеры начали заходить. Женя поправила книгу. Посмотрела на нас."
    cs_mz "Ну что, идём?"
    cs_ls "Идём."
    cs_narrator "Дарья подошла ближе."
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/dining_hall_full.ogg" fadein 1.5
    $ renpy.music.set_volume(0.20,delay=1.0,channel="ambience")
    $ cs_day03_lunch_arrived = True
    label cs_check_day03_120_inside:
    cs_narrator "И мы вместе направились внутрь."
    cs_th "Ну что ж."
    return
