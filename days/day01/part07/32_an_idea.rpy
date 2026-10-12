# -*- coding: utf-8 -*-
label cs_day01_32:
    $ save_name = "Чужая смена — День 1: Идея"
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    label cs_check_day01_part07_idea:
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    cs_narrator "Я прилегла на кровать."
    cs_narrator "Несколько секунд смотрела в потолок."
    cs_narrator "Деревянные балки."
    cs_narrator "Белая краска."
    cs_narrator "Никакого вентилятора."
    cs_narrator "Никакого кондиционера."
    cs_th "Прекрасно."
    cs_th "Технологический отпуск продолжается."
    cs_narrator "Потом мой взгляд остановился на телефоне, лежавшем на тумбочке."
    cs_narrator "Экран по-прежнему оставался чёрным."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Затем в окно."
    cs_narrator "И вдруг села."
    cs_ls "Электроника."
    cs_narrator "Дарья даже не вздрогнула."
    cs_narrator "Кажется, она уже начинала привыкать к моим внезапным идеям."
    cs_narrator "Что, вероятно, было тревожным признаком."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Что электроника?"
    cs_ls "Здесь есть кружок электроники."
    cs_da "И?"
    cs_narrator "Я выпрямилась."
    cs_ls "А в нём два местных специалиста по всему, что можно разобрать, спаять или случайно заставить дымиться."
    cs_narrator "Дарья посмотрела на телефон."
    cs_narrator "Потом на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    cs_da "Ты хочешь его зарядить."
    cs_narrator "Я указала на неё пальцем."
    cs_ls "Именно."
    cs_da "Лен, ты же сама сказала, что здесь нет подходящей зарядки."
    cs_ls "Зато здесь есть люди, которые умеют работать с электричеством."
    cs_da "И которые впервые увидят твой телефон."
    cs_narrator "Я задумалась."
    cs_ls "Небольшое техническое затруднение."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Небольшое?"
    cs_ls "Хорошо. Существенное."
    cs_narrator "Дарья посмотрела на меня с сомнением."
    # cs_darya_variety: reaction
    show cs_darya surprised pioneer normal at cs_darya_normal_center
    cs_da "А ты уверена, что это хорошая идея?"
    cs_narrator "Я взяла телефон."
    cs_narrator "Повертела в руке."
    cs_ls "Пока нет. Но если он заработает, у меня хотя бы останутся фотографии, заметки и документы."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "А связь?"
    cs_ls "С ней всё гораздо хуже. Заряженный телефон ещё не означает, что здесь появится мобильная сеть."
    cs_narrator "Дарья кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    cs_da "Хотя бы это понимаешь."
    cs_ls "Спасибо за доверие."
    cs_narrator "Я поднялась с кровати."
    cs_ls "Пойдём?"
    cs_narrator "Дарья вздохнула."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Куда теперь?"
    cs_ls "К местным инженерам."
    stop music fadeout 2.0
    return
