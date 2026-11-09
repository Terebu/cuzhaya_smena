# -*- coding: utf-8 -*-
label cs_day05_18:
    $ cs_d5_scene = 18
    $ save_name = "Чужая смена — День 5: Без одной минуты"
    $ cs_bus_scene_enter(18)
    $ cs_d5_room("bg ext_house_of_mt_night")
    with Dissolve(0.7)
    $ night_time()
    $ persistent.sprite_time = "night"
    stop music fadeout 1.0
    $ cs_rev_sfx('sound/sfx/open_door_1.ogg',0.35)
    cs_narrator "Ольга Дмитриевна открыла дверь почти сразу."
    cs_narrator "В комнате уже сидела Виола."
    cs_narrator "На столе стояли чайник и несколько кружек."
    cs_narrator "Увидев нас, вожатая отступила, пропуская внутрь."
    $ cs_d5_room("bg int_house_of_mt_night")
    $ cs_d5_documents_location = "olga"
    $ cs_bus_cue('calm')
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Вы немного рано."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Мы решили проявить ответственность."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Что-то случилось?"
    cs_narrator "Я вздохнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вы слишком хорошо меня знаете."
    cs_narrator "Семён вошёл следом."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 7c3df99f26b38dce2025
    cs_sy "На площади были какие-то удары."
    cs_sy "Шесть раз."
    cs_narrator "Виола подняла голову."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Шесть?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 7c6acc45e15d1e45e08b
    cs_da "Да."
    cs_da "Мы не стали проверять, откуда звук."
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.35)
    cs_narrator "Ольга Дмитриевна закрыла дверь."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Правильно сделали."
    cs_narrator "Мы расселись."
    cs_narrator "Я заняла свободный стул возле окна."
    cs_narrator "Даша устроилась рядом."
    cs_narrator "Женя достала тетрадь и положила её на стол."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Во сколько вы услышали стуки?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 91a0431817d28bc3eec1
    cs_sy "После ужина."
    cs_sy "Точнее не скажу."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 75073667f3e0e171b52f
    cs_ls "Мы не засекали."
    cs_ls "Поэтому давай без точного времени."
    cs_narrator "Женя кивнула и записала примерный промежуток."
    cs_narrator "Виола некоторое время смотрела на свои руки."
    cs_narrator "Потом заговорила."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "А мне снились часы."
    cs_narrator "Я повернулась к ней."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Какие?"
    $ cs_d5_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 18321ab887ac145fdffa
    cs_vi "Обычные настенные."
    cs_vi "В медпункте."
    cs_narrator "Она посмотрела на часы над дверью."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Во сне они останавливались без одной минуты двенадцать."
    cs_narrator "Семён откинулся на спинку стула."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "И что было дальше?"
    $ cs_d5_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: d2801de5e6c67a4532f7
    cs_vi "Становилось тихо."
    cs_vi "Совсем."
    cs_vi "А потом сразу наступало утро."
    cs_narrator "Я посмотрела на Ольгу Дмитриевну."
    cs_narrator "Вожатая не выглядела удивлённой."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вы тоже что-то подобное помните?"
    cs_narrator "Она кивнула."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: d012dbf48acc5d1002b5
    cs_mt "Иногда мне снится человек возле ворот."
    cs_mt "Он спрашивает, который час."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "И что вы отвечаете?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Что часы остановились."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "А он?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Говорит: «Значит, ещё не началось»."
    cs_narrator "Я опустила взгляд на стол."
    cs_narrator "Вот уж спасибо."
    cs_narrator "Если раньше мне не нравилась автобусная остановка, теперь к списку неприятных вещей добавились настенные часы."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Почему вы раньше не рассказали?"
    cs_narrator "Ольга Дмитриевна посмотрела на него."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Потому что до сегодняшнего утра это был обычный дурной сон."
    cs_narrator "Она немного помолчала."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "И я до сих пор не уверена, что он имеет отношение к происходящему."
    cs_narrator "Я кивнула."
    cs_narrator "Справедливо."
    cs_narrator "Мы уже достаточно натерпелись от попыток связать между собой всё подряд."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Есть ещё кое-что."
    cs_narrator "Мы посмотрели на неё."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: a5035db79f12981e0e35
    cs_vi "Иногда мне снится, что утром в лагере кого-то не хватает."
    cs_vi "Я нахожу чужую вещь, но не могу вспомнить, кому она принадлежала."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "А самого человека помните?"
    $ cs_d5_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 0061ab66633ae9153fe1
    cs_vi "Нет."
    cs_vi "Только ощущение, что он здесь был."
    cs_narrator "В комнате стало тихо."
    cs_narrator "Я сунула руку в карман и нащупала свои записи."
    cs_narrator "Тонкая бумага."
    cs_narrator "Несколько листков, на которых мы весь день старательно записывали то, чему не находили объяснения."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Тогда нужно сделать ещё несколько копий."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Согласна."
    cs_narrator "Я достала листок."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Если завтра кто-нибудь начнёт утверждать, что автобуса не было, хотя бы останется письменное свидетельство."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Если листки тоже не исчезнут."
    cs_narrator "Я посмотрела на него."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c3d8aa9d4e3c8068ae44
    cs_ls "Семён, я сегодня пытаюсь быть оптимисткой."
    cs_ls "Не мешай."
    cs_narrator "Он слабо улыбнулся."
    if cs_friend_viola >= 4:
        cs_narrator "Виола достала из блокнота страницу."
        $ cs_d5_focus("vi")
        with cs_sprite_change
        # cs_page_anchor: b2638659d351627d9445
        cs_vi "Я утром записала свой сон."
        cs_vi "До того, как вы пришли."
        cs_narrator "Она протянула мне лист."
        $ cs_d5_focus("vi")
        with cs_sprite_change
        # cs_page_anchor: b591cb6c45a48e01fe31
        cs_vi "Можешь переписать."
        cs_vi "Оригинал пока оставлю у себя."
        cs_narrator "Я посмотрела на запись."
        cs_narrator "Внизу стояла её подпись."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Спасибо."
        $ cs_d5_focus("vi")
        with cs_sprite_change
        cs_vi "Только не пытайся из каждого слова сделать вывод."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Я уже учусь."
        $ cs_d5_focus("vi")
        with cs_sprite_change
        cs_vi "Надеюсь."
        cs_narrator "Я переписала время и основные подробности."
        $ cs_d5_viola_early_note = True
    else:
        cs_narrator "Виола сама записала свой сон на отдельном листе."
        $ cs_d5_focus("vi")
        with cs_sprite_change
        # cs_page_anchor: 553bfef3ab80ce332dd6
        cs_vi "Оригинал пока будет у меня."
        cs_vi "В своих записях укажите, что услышали это сегодня от меня."
        cs_narrator "Женя кивнула."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        cs_mz "Хорошо."
        $ cs_d5_viola_early_note = False
    cs_narrator "Я посмотрела на часы."
    cs_narrator "Было немного за восемь."
    cs_narrator "Секундная стрелка двигалась совершенно нормально."
    cs_narrator "За окном кто-то смеялся."
    cs_narrator "Вдалеке слышались шаги."
    cs_narrator "Никаких признаков того, что через несколько часов может произойти что-то необычное."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У вас чайник работает?"
    cs_narrator "Ольга Дмитриевна посмотрела на меня."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Работает."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 419c34da16932423a5e2
    cs_ls "Замечательно."
    cs_ls "Тогда предлагаю начать подготовку с чая."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Неожиданно разумное предложение."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я сегодня в ударе."
    cs_narrator "Даша поднялась."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Я помогу."
    cs_narrator "Мы достали кружки."
    cs_narrator "Семён освободил место на столе."
    cs_narrator "Женя сложила записи в одну стопку."
    cs_narrator "Виола немного приоткрыла окно."
    cs_narrator "На несколько минут комната снова стала самым обычным жилым домиком."
    cs_narrator "И мне хотелось сохранить это ощущение как можно дольше."
    return
