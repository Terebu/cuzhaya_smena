# -*- coding: utf-8 -*-
label cs_day05_02:
    $ cs_d5_scene = 2
    $ save_name = "Чужая смена — День 5: Сон Семёна"
    $ cs_bus_scene_enter(2)
    $ cs_d5_room("bg ext_house_of_mt_day")
    with Dissolve(0.7)
    cs_narrator "Мы отошли к свободной скамейке."
    # cs_page_anchor: fa9087937d3f6ea02165
    cs_narrator "Семён сел первым и положил полотенце на колени."
    cs_narrator "Даша устроилась рядом, а я осталась стоять."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Вы никуда не торопитесь?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d6a5f6235a2ec1ca015f
    cs_ls "Пока нет."
    cs_ls "Но если предложишь разгрузить грузовик, я резко вспомню о важных делах."
    cs_narrator "Он даже не улыбнулся."
    cs_narrator "Я села."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Что случилось?"
    cs_narrator "Семён несколько секунд смотрел на полотенце."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 282cfd2b29c1be086d8f
    cs_sy "Мне сегодня сон приснился."
    cs_sy "Про автобус."
    cs_narrator "Я выпрямилась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Четыреста десятый?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: b8d5e5b87fca8b0d9f91
    cs_sy "Да."
    cs_sy "Стоял у ворот."
    cs_sy "Тот самый, на котором я сюда приехал."
    cs_narrator "Даша повернулась к нему."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Ты был внутри?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 73b354fb48e76717db9e
    cs_sy "Нет."
    cs_sy "Я стоял на остановке."
    cs_narrator "Он поднял глаза."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А в автобусе сидела Лена."
    cs_narrator "Я невольно посмотрела на него."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 29aa941b2fae3e38783f
    cs_sy "Ты."
    cs_sy "У окна."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Надеюсь, хоть место удобное досталось."
    cs_narrator "Семён покачал головой."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 1108fb26d432d071638f
    cs_sy "Она просто сидела и смотрела на меня."
    cs_sy "Вообще не двигалась."
    cs_narrator "После этого шутить расхотелось."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Дальше что было?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "На стекле появилась надпись."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Какая?"
    play music cs_day_music_think fadein 1.2
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "«Остался один»."
    cs_narrator "Я почувствовала неприятный холод где-то под рёбрами."
    cs_narrator "Этот сон я уже знала."
    $ cs_pov_begin()
    with cs_sprite_leave
    # cs_page_anchor: d8d709139750662fa108
    cs_th "Только в моей версии на остановке стояла я сама."
    cs_th "А в салоне сидела ещё одна я."
    cs_narrator "И на стекле было написано другое."
    cs_narrator "Не садись второй раз."
    cs_narrator "Даша медленно повернулась ко мне."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 9cc8f580581e79e01642
    cs_da "Лен."
    cs_da "Это же твой сон."
    cs_da "Тот, который ты вчера рассказывала."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: abe243295e7ac9c58446
    cs_ls "Почти."
    cs_ls "Только у меня снаружи стояла я, а у Семёна — он."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А внутри в обоих случаях ты."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Спасибо, я заметила."
    cs_narrator "Семён опустил голову."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Прекрасно."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: fdf53313d07c49219695
    cs_ls "Согласна."
    cs_ls "У местного транспорта отвратительная рекламная кампания."
    cs_narrator "Шутка вышла слабой."
    cs_narrator "Потому что я вспомнила ещё одно."
    # cs_page_anchor: ccab946a197b8d596e00
    cs_narrator "Вчера вечером я сама считала дни."
    cs_narrator "У Семёна сегодня шестой."
    cs_narrator "Завтра — седьмой."
    cs_narrator "Остался один."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: db0d1939c7ec2b0c3286
    cs_ls "Семён."
    cs_ls "У тебя ведь сегодня шестой день?"
    cs_narrator "Он посмотрел на меня так, будто я сказала что-то неприличное."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Думаешь, я не посчитал?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "«Остался один» — это может быть про день."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Или про человека."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: b2f71db30d047e821411
    cs_sy "Или про то и другое."
    cs_sy "Очень утешает."
    cs_narrator "Даша взглянула на нас."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 588614baaac95d2f5291
    cs_da "Давайте сначала разберёмся, что каждый видел."
    cs_da "Без теорий."
    cs_narrator "Она была права."
    cs_narrator "Мы ещё не успели поесть, а уже собирались строить объяснение тому, чего сами не понимали."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Семён, двери автобуса открывались?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 311811b85895646d47a6
    cs_sy "Нет."
    cs_sy "Кажется, только в самом конце."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "А надпись появилась до этого?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Да."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ты видел водителя?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 2fef252199387f012a53
    cs_sy "Нет."
    cs_sy "С того места не было видно."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "И чем всё закончилось?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 5ef2f8dae1cea4a1eced
    cs_sy "Стало темно."
    cs_sy "А потом я проснулся."
    cs_narrator "Он потёр лицо ладонями."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Вот и всё."
    cs_narrator "Некоторое время мы молчали."
    # cs_page_anchor: fb25b8b90c6d8e7b4b66
    cs_narrator "За кустами проехала тележка."
    cs_narrator "Кто-то поздоровался с проходившим мимо пионером."
    cs_narrator "Лагерь продолжал жить своей жизнью."
    cs_narrator "И от этого рассказ Семёна звучал ещё страннее."
    if cs_friend_se >= 4:
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Я сначала хотел вообще ничего не говорить."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Почему?"
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Не хотел, чтобы вы опять начали за мной следить."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Справедливо."
        cs_narrator "Он посмотрел на меня с удивлением."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "И всё?"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 0c6c57be49fa6565e80e
        cs_ls "А что ты хотел?"
        cs_ls "Торжественную речь?"
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "От тебя можно ожидать."
        cs_narrator "Я улыбнулась."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Сегодня воздержусь."
        cs_narrator "Семён достал из кармана сложенную бумажку."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: be0cd5e00279cd00cdde
        cs_sy "Кстати."
        cs_sy "Если вы с Дашей правда когда-нибудь вернётесь домой…"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "То что?"
        $ cs_d5_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: b944fdaa10dcacd06c5a
        cs_sy "Я записал адрес и фамилию."
        cs_sy "Своего времени."
        cs_sy "На случай, если захочешь проверить, что я тебе не приснился."
        cs_narrator "Я взяла листок."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Спасибо."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Только не надо устраивать из этого событие."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 1f9f87da33a2a52760b2
        cs_ls "Поздно."
        cs_ls "Уже мысленно заказала салют."
        cs_narrator "Он наконец улыбнулся."
        cs_narrator "Я спрятала листок, не разворачивая."
        $ cs_d5_semyon_address = True
    elif cs_friend_se >= 1:
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Только давай без того, чтобы ты весь день ходила за мной по пятам."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Я настолько страшная?"
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Настолько навязчивая."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 46a82c44b0e416344cdf
        cs_ls "Ладно."
        cs_ls "Начнём с завтрака, а потом решим, насколько тебе нужна охрана."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Меня устроит просто компания."
        cs_narrator "Я кивнула."
    else:
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Я рассказал, потому что это связано с тем, что мы нашли вчера."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Понимаю."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "И не надо делать из этого очередное представление."
        cs_narrator "Я посмотрела на него."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 9eb486e2387bf5a12925
        cs_ls "Не буду."
        cs_ls "Сейчас не до того."
        cs_narrator "Он отвёл взгляд, но заметно расслабился."
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    cs_narrator "С площади донёсся горн."
    cs_narrator "Семён поморщился."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Наконец-то что-нибудь предсказуемое."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 4f170e674c5b4b95978e
    cs_sy "Не радуйся раньше времени."
    cs_sy "Мы ещё завтрак не видели."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 6edb418f216d2f768318
    cs_da "Сначала умоемся."
    cs_da "Потом позавтракаем и спокойно поговорим с Ольгой Дмитриевной."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Согласна."
    cs_narrator "Я поднялась со скамейки."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "До завтрака никаких расследований."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Обещаешь?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Торжественно."
    cs_narrator "Он посмотрел на Дашу."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 532e297c7647b4bd462c
    cs_sy "Запомни."
    cs_sy "Будешь свидетелем."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Уже запомнила."
    stop music fadeout 1.0
    $ cs_d5_room("bg ext_washstand_day")
    cs_narrator "Мы пошли к умывальникам."
    cs_narrator "Я старалась не возвращаться мыслями к надписи на стекле."
    cs_narrator "Получалось плохо."
    $ cs_rev_sfx('sound/sfx/water_splash.ogg',0.35)
    cs_narrator "Зато когда холодная вода попала на лицо, голова немного прояснилась."
    cs_narrator "В конце концов, у нас было достаточно времени, чтобы поговорить."
    $ cs_d5_room("cs_house_lena_darya_int_day")
    # cs_page_anchor: cca74dd7e0a0896b08c1
    cs_narrator "Семён подождал снаружи, пока мы с Дашей вернулись в домик."
    cs_narrator "Она сменила спортивную форму на пионерскую, и мы догнали его у столовой."
    $ cs_d5_run_finished = True
    $ cs_d5_costume("pioneer")
    cs_narrator "По крайней мере, очень хотелось в это верить."
    return
