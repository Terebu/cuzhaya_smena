# -*- coding: utf-8 -*-
label cs_day02_01:
    $ save_name = "Чужая смена — День 2: Когда лагерь ещё спит"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_early_morning
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
    play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    stop music fadeout 1.0
    label cs_check_new_d2_s01:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Проснулась я ещё до того, как лагерь начал подавать признаки жизни."
    cs_narrator "Сначала даже не поняла, почему открыла глаза."
    cs_narrator "Никто не разговаривал за окном. Не хлопали двери. Не звучал горн, которому здесь, кажется, доверили обязанности всех будильников разом."
    cs_narrator "Было тихо."
    cs_narrator "Я лежала на спине и смотрела в потолок."
    cs_narrator "Деревянные доски."
    cs_narrator "Светлая краска."
    cs_narrator "Узкая полоска солнечного света, пробивавшаяся сквозь занавеску."
    cs_narrator "Никакого привычного шума московской улицы."
    cs_narrator "Никакого компьютера, тихо гудящего после ночной работы."
    cs_narrator "И телефона на тумбочке, который мог бы показать время."
    cs_narrator "Точнее, телефон был."
    cs_narrator "Только толку от него примерно столько же, сколько от выключенного кирпича."
    cs_narrator "Я повернула голову."
    cs_narrator "Дарья спала на соседней кровати."
    cs_narrator "Устроилась на боку, подтянув одеяло почти до плеч. Красные волосы немного растрепались, несколько прядей упали на лицо."
    cs_narrator "Она выглядела так спокойно, будто вчерашний день прошёл совершенно обычно."
    cs_narrator "Будто не было зимней Москвы."
    cs_narrator "Автобуса."
    cs_narrator "Пионерского лагеря."
    cs_narrator "И разговора, в котором я неожиданно для самой себя призналась ей в симпатии."
    cs_th "Интересно, как ей удаётся так спать?"
    cs_narrator "Я посмотрела на неё ещё немного."
    cs_narrator "Потом отвернулась."
    cs_th "Соколова, перестань рассматривать человека."
    cs_th "Он вообще-то спит."
    cs_narrator "И всё же я улыбнулась."
    cs_narrator "Вчера вечером Даша сама разрешила себя приобнять."
    cs_narrator "Ничего особенно торжественного в этом не было."
    cs_narrator "Мы просто поговорили."
    cs_narrator "Она сказала, что не хочет торопиться, и я согласилась."
    cs_narrator "Но почему-то именно этот небольшой разговор теперь вспоминался гораздо отчётливее многих событий первого дня."
    cs_narrator "Я снова посмотрела в потолок."
    cs_narrator "Попробовала закрыть глаза."
    cs_narrator "Подождала."
    cs_narrator "Прошла, наверное, минута."
    cs_narrator "Затем ещё одна."
    cs_narrator "Ничего."
    cs_th "Ну конечно."
    cs_narrator "Мой организм решил, что выспался."
    cs_narrator "А если он так решил, спорить бесполезно."
    cs_narrator "Я всегда была жаворонком."
    cs_narrator "Не из тех людей, которые иногда просыпаются в семь утра и потом неделю рассказывают об этом как о подвиге."
    cs_narrator "Нет."
    cs_narrator "Если выспалась — значит, пора вставать."
    cs_narrator "Можно, конечно, продолжать лежать."
    cs_narrator "Но тогда через десять минут мне станет скучно, а через двадцать я начну придумывать себе занятие."
    cs_narrator "Причём качество этих занятий уже неоднократно вызывало вопросы у окружающих."
    cs_narrator "Я посмотрела на спящую Дашу."
    cs_th "Нет."
    cs_th "Сегодня попробуем без жертв."
    cs_narrator "Осторожно откинула одеяло и села."
    cs_narrator "Пол под босыми ногами оказался прохладным."
    cs_narrator "Я прислушалась."
    cs_narrator "Дарья не проснулась."
    cs_narrator "Хорошо."
    cs_th "Значит, утренняя операция начинается успешно."
    return
