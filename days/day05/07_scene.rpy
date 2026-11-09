# -*- coding: utf-8 -*-
label cs_day05_07:
    $ cs_d5_scene = 7
    $ save_name = "Чужая смена — День 5: Не под конвоем"
    $ cs_bus_scene_enter(7)
    $ cs_d5_room("cs_camp_path_day")
    with Dissolve(0.7)
    cs_narrator "Мы прошли несколько десятков метров."
    cs_narrator "За воротами остался автобус, которого уже не было."
    cs_narrator "Впереди — обычный лагерь."
    cs_narrator "На дорожке кто-то смеялся."
    cs_narrator "Со стороны спортивной площадки доносились удары мяча."
    cs_narrator "Я никак не могла решить, что раздражает сильнее: происходящее у ворот или то, насколько быстро всё вокруг снова становится нормальным."
    cs_narrator "Семён остановился у развилки."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Слушайте."
    cs_narrator "Мы повернулись к нему."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 1f97bf0a04cb666f2e48
    cs_sy "Я понимаю, что после всего этого вы будете переживать."
    cs_sy "Но давайте без постоянного надзора."
    cs_narrator "Я открыла рот."
    cs_narrator "И закрыла."
    cs_narrator "Потому что именно это собиралась предложить."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "А я уже почти заказала полосатую будку."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Лена, я серьёзно."
    cs_narrator "Я посмотрела на него внимательнее."
    cs_narrator "Он действительно выглядел уставшим."
    cs_narrator "Не от прогулки."
    cs_narrator "От того, что происходило."
    cs_narrator "И, наверное, ещё от мысли, что теперь за ним будут следить все знакомые."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: ebb2a6d33b88b9da09e0
    cs_sy "Я не хочу оставаться один."
    cs_sy "Но и не хочу, чтобы меня каждые пять минут спрашивали, где я был и что делал."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Это понятно."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 037c10bb1a563c83488e
    cs_mz "И правильно."
    cs_mz "После такого утра каждому нужно хоть немного личного пространства."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Он ждал моего ответа."
    menu:
        "Скажи сам, как тебе будет спокойнее":
            $ cs_d5_choose(3, 0)
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: d21d1c55ccc65ad9b426
            cs_ls "Хорошо."
            cs_ls "Тогда скажи сам, как тебе будет спокойнее."
            cs_narrator "Семён немного удивился."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 0f2bd4b0c75ae0ace535
            cs_sy "Просто ходить вместе."
            cs_sy "Без допросов."
            cs_sy "Если мне понадобится побыть одному, я предупрежу."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Договорились."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "И если я что-нибудь замечу, сразу скажу."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Вот это главное."
            cs_narrator "Он посмотрел на меня."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Спасибо."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 4e29c708ec4c7da83058
            cs_ls "Не за что."
            cs_ls "Полосатую будку отменяем."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Очень благородно с твоей стороны."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: edd9c929ed2689f37167
            cs_ls "Я сегодня добрая."
            cs_ls "Пользуйся."
            cs_narrator "Он наконец улыбнулся."
        "Сегодня лучше держись рядом. Остальное обсудим позже":
            $ cs_d5_choose(3, 1)
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 6bb1f9f5ce6fd736a7b2
            cs_ls "Семён, сегодня лучше держись рядом."
            cs_ls "После автобуса мне совсем не нравится идея отпускать тебя одного."
            cs_narrator "Он нахмурился."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Ты меня не отпускаешь?"
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Я не это имела в виду."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Именно это и прозвучало."
            cs_narrator "Я вздохнула."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Я просто переживаю."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 9b57d7115ebe8fc3361b
            cs_sy "Я понимаю."
            cs_sy "Но ты сейчас решаешь за меня."
            cs_narrator "Он посмотрел на Дашу."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Скажите ей хоть вы."
            $ cs_d5_focus("da")
            with cs_sprite_change
            # cs_page_anchor: f94880bfca932199dca5
            cs_da "Лена, он прав."
            cs_da "Мы можем договориться, как быть дальше, но командовать им не нужно."
            cs_narrator "Я отвела взгляд."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: b581b11e4fe27e4069d2
            cs_ls "Хорошо."
            cs_ls "Давайте поговорим с Ольгой Дмитриевной."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Вот это нормальный вариант."
            cs_narrator "Он пошёл рядом с Женей."
            cs_narrator "Я осталась чуть позади."
            cs_narrator "Неприятно было признавать, что Даша права."
            cs_narrator "Хотя после нескольких дней в лагере я уже начала привыкать к этому обстоятельству."
    $ cs_d5_room("bg ext_square_day")
    cs_narrator "Ольгу Дмитриевну мы нашли возле административного корпуса."
    cs_narrator "Она разговаривала со Славей, но, заметив нас, сразу поняла, что спокойное утро закончилось."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Вы уже вернулись?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1d4a9b5dcbb72eeeab20
    cs_ls "Да."
    cs_ls "И у нас новости."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Почему мне не нравится, как это звучит?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "К остановке приезжал автобус."
    cs_narrator "Вожатая перестала улыбаться."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 88000b48e78ee7a0e2bf
    cs_sy "Четыреста десятый."
    cs_sy "Без водителя."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: dc714e8e74e27a129a78
    cs_mz "Мы все его видели."
    cs_mz "Потом был голос."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Чей?"
    cs_narrator "Я посмотрела на неё."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 11268199058742fd3818
    cs_ls "Мой."
    cs_ls "По крайней мере, звучал точно так же."
    cs_narrator "Ольга Дмитриевна несколько секунд молчала."
    cs_narrator "Потом повернулась к Славе."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: e9439082512430e41932
    cs_mt "Отнеси, пожалуйста, бумаги в администрацию."
    cs_mt "Я подойду позже."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Хорошо."
    $ cs_actor_exit(["sl"])
    $ cs_d5_cast = []
    cs_narrator "Вожатая снова посмотрела на нас."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 68dd68030f329d0498a8
    cs_mt "Покажете место."
    cs_mt "Только идём вместе."
    $ cs_d5_room("bg ext_no_bus")
    cs_narrator "Мы вернулись к воротам."
    cs_narrator "Автобуса, разумеется, уже не было."
    cs_narrator "Зато надпись на стойке осталась."
    cs_narrator "Женя показала её Ольге Дмитриевне."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Сегодня это появилось?"
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 8c06dfb21d93cc8d8a4d
    cs_mz "Не знаем."
    cs_mz "Раньше мы с этой стороны не смотрели."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Но теперь можем точно сказать, что надпись здесь есть."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "И больше ничего не предпринимайте самостоятельно."
    cs_narrator "Я кивнула."
    cs_narrator "На этот раз спорить не хотелось."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 371ddfab34fbe450669d
    cs_mt "К обеду я подойду в библиотеку."
    cs_mt "Соберите там все записи."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Хорошо."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: fe505ba1c0ea0374af77
    cs_mt "И, пожалуйста, не ходите к старому корпусу."
    cs_mt "Сегодня достаточно приключений."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У меня даже не было планов."
    cs_narrator "Ольга Дмитриевна посмотрела на меня."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Серьёзно."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Вот и замечательно."
    cs_narrator "Мы отправились обратно."
    cs_narrator "По дороге Семён попросил зайти к умывальникам."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Я не стала спрашивать зачем."
    cs_narrator "После такого утра мне тоже хотелось просто умыться."
    cs_narrator "И немного прийти в себя."
    return
