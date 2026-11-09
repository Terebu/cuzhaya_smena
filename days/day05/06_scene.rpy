# -*- coding: utf-8 -*-
label cs_day05_06:
    $ cs_d5_scene = 6
    $ save_name = "Чужая смена — День 5: Пассажирка"
    $ cs_bus_scene_enter(6)
    $ cs_d5_room("cs_bus410_closed_day")
    with Dissolve(0.7)
    stop music fadeout 1.0
    $ cs_bus_cue('stop')
    cs_narrator "Автобус остановился."
    cs_narrator "Двигатель продолжал работать."
    cs_narrator "Мы стояли возле ворот и смотрели на него."
    cs_narrator "Я снова перевела взгляд на место водителя."
    cs_narrator "Пусто."
    # cs_page_anchor: cc8c42a1af8f413f6719
    cs_narrator "Никаких рук на руле."
    cs_narrator "Никакой фигуры за стеклом."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Вы тоже это видите?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Да."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Там никого нет."
    cs_narrator "Я не сразу ответила."
    cs_narrator "Хотелось найти какое-нибудь простое объяснение."
    cs_narrator "Например, что я неправильно смотрю."
    cs_narrator "Или что водитель просто сидит слишком низко."
    cs_narrator "Но автобус только что подъехал к остановке."
    cs_narrator "Сам."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9068819f9e0546f96f27
    cs_ls "Потрясающе."
    cs_ls "Теперь у нас ещё и беспилотный транспорт."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Лена."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я вижу."
    cs_narrator "Двери оставались закрытыми."
    cs_narrator "На боковых стёклах отражались деревья, ограда и мы четверо."
    cs_narrator "Я посмотрела на своё отражение."
    cs_narrator "Поправила волосы."
    cs_narrator "И замерла."
    cs_narrator "Девушка в стекле не повторила движение."
    cs_narrator "Я медленно опустила руку."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Отражение продолжало стоять неподвижно."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Даша."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Что?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: cbdf4d08f82a1784d228
    cs_ls "Посмотри на окно."
    cs_ls "Только скажи, что видишь."
    cs_narrator "Она подошла ближе, но за линию ворот не вышла."
    cs_narrator "Несколько секунд смотрела на стекло."
    cs_narrator "Потом взяла меня за рукав."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Там кто-то стоит."
    cs_narrator "Я сглотнула."
    cs_narrator "В отражении виднелись фиолетовые пряди."
    cs_narrator "Плечи."
    cs_narrator "Часть руки."
    cs_narrator "Лицо скрывалось за солнечным бликом."
    cs_narrator "Я не могла понять, стояла девушка внутри салона или её изображение существовало только на стекле."
    cs_narrator "А потом она подняла руку."
    cs_narrator "Приложила палец к губам."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Это не ты."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Очень надеюсь."
    cs_narrator "Женя молча отступила на шаг."
    $ cs_bus_cue('open')
    $ cs_d5_room("cs_bus410_open_day", duration=0.8, force=True)
    cs_narrator "Двери автобуса открылись."
    cs_narrator "Внутри было пусто."
    cs_narrator "Ни водителя, ни пассажиров."
    cs_narrator "На одном из сидений лежал белый конверт."
    cs_narrator "Я заметила его почти сразу."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Лена, даже не думай подходить."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я ещё ничего не сделала."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Ты уже рассматриваешь, как туда добраться."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Удивительно, насколько хорошо вы меня изучили."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А если там что-то написано?"
    cs_narrator "Я посмотрела на конверт."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Тогда придётся признать, что у нас очень плохой способ доставки писем."
    cs_narrator "Из салона раздался женский голос."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Семён."
    cs_narrator "Он вздрогнул."
    cs_narrator "Даша сильнее сжала мой рукав."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Остался один."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Он не двигался."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Один кто?"
    cs_narrator "Ответа не последовало."
    cs_narrator "Я сделала осторожный шаг в сторону, пытаясь разглядеть источник звука."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я остановилась."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Что тебе от меня нужно?"
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Он должен выбрать."
    cs_narrator "Семён нахмурился."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Что выбрать?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Вы хотя бы объясните, о чём говорите."
    cs_narrator "Салон молчал."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Я посмотрела на неподвижные сиденья."
    cs_narrator "Теперь хотелось не столько узнать ответ, сколько заставить неизвестную собеседницу произнести хоть одну нормальную фразу."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2869fb6cc66bb630bf34
    cs_ls "Слушай, мы тебя слышим."
    cs_ls "Но если собираешься что-то предлагать, начни с условий."
    $ cs_bus_cue('close')
    $ cs_d5_room("cs_bus410_closed_day", duration=0.8, force=True)
    cs_narrator "Вместо ответа двери начали закрываться."
    cs_narrator "Я посмотрела на конверт."
    cs_narrator "В последнюю секунду он исчез."
    cs_narrator "Просто пропал с сиденья."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Вы видели?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Да."
    $ cs_bus_cue('depart')
    cs_narrator "Автобус тронулся."
    cs_narrator "Медленно выехал с остановки и направился к повороту."
    cs_narrator "Мы провожали его взглядом."
    cs_narrator "Никто не пытался догонять."
    $ cs_d5_room("bg ext_no_bus", duration=1.25, force=True)
    $ cs_bus_cue('gone')
    cs_narrator "Когда красная полоса скрылась за деревьями, я вспомнила надпись."
    cs_narrator "Не оглядывайся."
    cs_narrator "Я посмотрела на остальных."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Давайте пока не будем поворачиваться."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Серьёзно?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 775ee3801c81dad57018
    cs_ls "Не знаю, кто написал эти слова."
    cs_ls "Но проверять, шутка это или нет, сейчас не хочется."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Согласна."
    cs_narrator "Мы остались стоять лицом к дороге."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Вокруг было тихо."
    cs_narrator "Я слышала собственное дыхание."
    cs_narrator "Где-то за спиной хрустнул гравий."
    cs_narrator "Потом раздался голос."
    cs_narrator "Мой голос."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Лена."
    cs_narrator "Я застыла."
    cs_narrator "Даша стояла слева, Семён справа."
    cs_narrator "Женя стояла рядом с Семёном, на полшага позади."
    cs_narrator "Это говорила не я."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Ты уже делала это."
    cs_narrator "Я почувствовала, как по спине пробежал холод."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Посмотри."
    cs_narrator "Очень хотелось обернуться."
    cs_narrator "Даже не из храбрости."
    cs_narrator "Просто человеку трудно стоять спиной к тому, кто зовёт его по имени."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Не надо."
    cs_narrator "Я посмотрела на её руку."
    cs_narrator "Она держала мой рукав."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Не буду."
    $ cs_bus_cue('chuckle')
    cs_narrator "За спиной послышался тихий смешок."
    $ cs_bus_cue('hush')
    cs_narrator "Затем всё стихло."
    cs_narrator "Мы подождали ещё немного."
    cs_narrator "Первой заговорила Женя."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Кто-нибудь что-нибудь слышит?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Нет."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Кажется, всё."
    cs_narrator "Мы осторожно повернулись."
    cs_narrator "Позади никого не было."
    cs_narrator "Только ворота."
    cs_narrator "Дорожка."
    $ cs_bus_cue('calm')
    cs_narrator "Обычный солнечный день."
    cs_narrator "Я смотрела на пустое место ещё несколько секунд."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Прекрасно."
    cs_narrator "Семён повернулся ко мне."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Что прекрасного?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0a56dadb5aa5120e7417
    cs_ls "У местного транспорта не только проблемы с расписанием."
    cs_ls "Здесь ещё и служба поддержки хамит."
    cs_narrator "Он нервно рассмеялся."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Лучше возвращаться."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: bc7d8933b2c4ce46655c
    cs_da "Да."
    cs_da "И рассказать Ольге Дмитриевне."
    cs_narrator "Я кивнула."
    cs_narrator "Мы пошли обратно в лагерь."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Ноги слушались не сразу."
    cs_narrator "Мне казалось, что стоит обернуться ещё раз — и я снова услышу собственный голос."
    cs_narrator "Но я не обернулась."
    cs_narrator "И впервые за всё утро была этому рада."
    return
