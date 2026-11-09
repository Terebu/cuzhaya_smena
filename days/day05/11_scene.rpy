# -*- coding: utf-8 -*-
label cs_day05_11:
    $ cs_d5_scene = 11
    $ save_name = "Чужая смена — День 5: Обычный обед"
    $ cs_bus_scene_enter(11)
    $ cs_d5_room("bg int_dining_hall_people_day")
    with Dissolve(0.7)
    cs_narrator "К обеду я успела проголодаться так, словно утренняя пробежка длилась не несколько минут, а пару часов."
    cs_narrator "Хотя, если честно, куда больше сил отняли разговоры."
    cs_narrator "В столовой было шумно."
    cs_narrator "У раздачи снова образовалась очередь."
    cs_narrator "Один пионер пытался получить добавку раньше остальных."
    $ cs_d5_focus("d5_cook")
    with cs_sprite_change
    cs_d5_cook "Сначала всем раздадим!"
    $ cs_d5_focus("d5_pioneer")
    with cs_sprite_change
    cs_d5_pioneer "Ну я же немного!"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вот человек знает, чего хочет от жизни."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 92ae8666ee4353276ace
    cs_da "Ты тоже."
    cs_da "Еды."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "И чтобы мне хотя бы полчаса никто не рассказывал про автобусы."
    cs_narrator "Семён, стоявший впереди, обернулся."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Вот тут поддерживаю."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Тогда давайте договоримся: за обедом об этом не говорим."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Женя, я готова назначить тебя ответственной за соблюдение режима."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 11b46fef9295e6db1d15
    cs_mz "Не надо."
    cs_mz "Я и так библиотекой занимаюсь."
    cs_narrator "Мы взяли обед и направились к свободному столу."
    cs_narrator "Тихонова выбрала место возле окна."
    cs_narrator "Я села рядом с Дашей."
    cs_narrator "Семён устроился напротив."
    cs_narrator "Женя поставила поднос с таким видом, будто наконец добралась до единственного тихого места в столовой."
    cs_narrator "К сожалению, тихим оно оставалось недолго."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Лен, осторожнее со стаканом."
    cs_narrator "Она передвинула компот чуть дальше от моего локтя."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 7cb411732356740b2873
    cs_ls "Спасибо."
    cs_ls "Теперь я официально человек, которому нельзя доверять напитки."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "После того, как ты утром застряла рукавом в двери столовой, я бы не спорила."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Один раз!"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Удивительно, что ты ещё ведёшь подсчёт."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Кто-то должен защищать мою репутацию."
    cs_narrator "Тихонова улыбнулась."
    cs_narrator "Мы принялись за суп."
    cs_narrator "Некоторое время действительно говорили только о еде."
    cs_narrator "Я даже успела выяснить, что Семён терпеть не может слишком разваренные макароны, а Женя предпочитает чай без сахара."
    cs_narrator "Великие открытия."
    cs_narrator "И ни одного сверхъестественного явления."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Кстати, Лена, хлеб передай."
    cs_narrator "Я пододвинула ему хлебницу."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 5490b5cc53f41f844217
    cs_ls "Пожалуйста."
    cs_ls "Запомни этот момент."
    cs_ls "Я иногда бываю полезной."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Обязательно отмечу в отчёте."
    cs_narrator "Даша пыталась открыть солонку."
    cs_narrator "Крышка не поддавалась."
    cs_narrator "Тихонова взяла её, чуть повернула и без труда открыла."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Спасибо!"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Сила коллектива."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Там просто крышка перекосилась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Не лишай нас красивой легенды."
    cs_narrator "Тихонова рассмеялась."
    cs_narrator "Я посмотрела на неё и неожиданно подумала, что разговаривать с тёзкой стало гораздо легче."
    cs_narrator "Она всё ещё была тихой."
    cs_narrator "Но иногда сама включалась в разговор."
    cs_narrator "И мне нравилось, что рядом с нами ей уже не обязательно молчать."
    if cs_d5_lena_dream_shared_early:
        cs_narrator "Тихонова осторожно повернулась к Жене."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Можно потом поговорить про мой сон?"
        $ cs_d5_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 121c6ba666f23a5b3abd
        cs_mz "Конечно."
        cs_mz "Только после обеда."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Хорошо."
        cs_narrator "Я не стала вмешиваться."
        cs_narrator "Она уже решила рассказать сама."
    else:
        cs_narrator "Тихонова почти весь обед молчала."
        # cs_page_anchor: 690f2a6d3d60a3f368dc
        cs_narrator "Один раз мне показалось, что она хочет что-то сказать Жене."
        cs_narrator "Даже повернулась к ней."
        cs_narrator "Но потом передумала и снова взялась за ложку."
        cs_narrator "Я сделала вид, что ничего не заметила."
        cs_narrator "После утреннего разговора давить на неё было бы худшим из возможных решений."
    cs_narrator "Когда я почти доела, в столовую вошла Славя."
    cs_narrator "Она огляделась, заметила свободный стул возле Даши и подошла к нам."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Здесь свободно?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Да, садись."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: dd7f9386ef379aa0e7a5
    cs_ls "У нас сегодня мирные переговоры с обедом."
    cs_ls "Присоединяйся."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "А бывают другие?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "С кашей отношения сложнее."
    cs_narrator "Славя поставила поднос."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Ольга Дмитриевна просила передать, что после обеда принесёт бумаги в библиотеку."
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Та кивнула."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 1bd49e149cb3d4eb2dbe
    cs_mz "Хорошо."
    cs_mz "Мы там будем."
    cs_narrator "Славя заметила наши взгляды."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "А что у вас происходит?"
    cs_narrator "Никто сразу не ответил."
    # cs_page_anchor: c56cd66641d45ab99d18
    cs_narrator "Женя посмотрела на меня."
    cs_narrator "Её правило про обед продержалось ровно до второго блюда."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 8ee3f26ed2993ceb5d7a
    cs_mz "Ладно."
    cs_mz "Только коротко и тихо."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "После утреннего разговора не хотелось снова говорить за него."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Семён, расскажешь?"
    cs_narrator "Он немного помолчал."
    cs_narrator "Потом кивнул."
    return
