# -*- coding: utf-8 -*-
label cs_rev_d2_01:
    $ cs_rev_begin(2,1,['cs_darya'])
    $ save_name = "Чужая смена — День 2: Жаворонок"
    $ cs_rev_time("day")
    $ cs_rev_costume("sport")
    $ cs_rev_room("cs_house_lena_darya_int_day")
    $ cs_rev_darya_offscreen = True
    cs_narrator "Проснулась я раньше лагеря."
    # cs_page_anchor: b34fe093f2820411ca1d
    cs_narrator "За окном было тихо."
    cs_narrator "Ни московской улицы, ни гудения компьютера."
    cs_narrator "Только доски над головой и разряженный телефон на тумбочке — самый бесполезный предмет в радиусе нескольких десятилетий."
    # cs_page_anchor: b53bf3e55f508fccc7df
    cs_narrator "Дарья спала на соседней кровати."
    cs_narrator "Красные пряди упали на лицо, одеяло подтянуто к самым плечам."
    cs_narrator "Как ей удаётся так спокойно спать после вчерашнего?"
    # cs_page_anchor: c19115d4500f4e5a3b7b
    cs_narrator "Я поймала себя на том, что смотрю на неё слишком долго, и отвернулась."
    cs_narrator "Соколова, человек спит."
    cs_narrator "Это не повод для этюда."
    # cs_page_anchor: c7c63541d5632c8bcb3a
    cs_narrator "И всё-таки улыбнулась."
    cs_narrator "Вчера она разрешила себя обнять."
    cs_narrator "Сказала, что не хочет торопиться, — и я согласилась."
    cs_narrator "Это было, пожалуй, самое взрослое решение за весь первый день."
    # cs_page_anchor: 0495232c8b30ae1d5f6c
    cs_narrator "Уснуть снова не получилось."
    cs_narrator "Я всегда была жаворонком: могу полежать ещё, но через десять минут начну искать себе занятие."
    # cs_page_anchor: e255e977e1f37decb2e0
    cs_narrator "В шкафу под пионерской формой нашлись лагерные шорты и футболка."
    cs_narrator "Для пробежки — то, что нужно."
    cs_narrator "Тренировки были одной из немногих привычек, которые мне никогда не приходилось себе навязывать: бег, растяжка, турник."
    cs_narrator "С телом договариваться всегда было проще, чем с характером."
    cs_narrator "У двери я остановилась и вернулась к кровати Дарьи."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f750d88ba213db3201c5
    cs_ls "Даш, я ненадолго выйду."
    cs_ls "Хочу пробежаться."
    # cs_page_anchor: 1a8ce35c90b0f1ab1337
    cs_narrator "Тишина."
    cs_narrator "Я поправила сползший край её одеяла и уже взялась за ручку двери, когда услышала сонное:"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты всегда так рано встаёшь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Обычно да."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Добровольно?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Представь себе."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Удивительная женщина."
    # cs_page_anchor: c7eea87d71509b31abc3
    cs_narrator "Глаза она так и не открыла."
    cs_narrator "Потом добавила совсем другим голосом:"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Только не уходи за территорию одна."
    cs_narrator "Я перестала улыбаться."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Не уйду."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Обещаешь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f86b2ab5a473b9315381
    cs_ls "Обещаю."
    cs_ls "Обычная пробежка по дорожкам."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И не пытайся заодно разгадать все загадки лагеря."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: e59cab896494b2495404
    cs_ls "Про загадки гарантий не даю."
    cs_ls "Про ворота — даю."
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.25)
    # cs_page_anchor: 5d4358be91344516a7e7
    cs_narrator "Она негромко усмехнулась в подушку."
    cs_narrator "Я закрыла дверь так осторожно, как только позволяли старые петли."
    return

label cs_rev_d2_02:
    $ cs_rev_begin(2,2,['mt'])
    $ save_name = "Чужая смена — День 2: Турник"
    $ cs_rev_time("day")
    $ cs_rev_costume("sport")
    $ cs_rev_room("cs_house_lena_darya_ext_day")
    $ cs_rev_music(cs_day_music_daily,0.16,2.5)
    # cs_page_anchor: 3bf5498c7f8be28230cb
    cs_narrator "Снаружи были пустые дорожки, роса и прохладный воздух."
    cs_narrator "Ни Алисы с Ульяной, ни Слави с поручениями."
    cs_narrator "«Совёнок» без населения — редкая возможность спокойно осмотреть декорации."
    cs_narrator "Я размялась на крыльце и побежала."
    # cs_page_anchor: f57a5db2516c744cee8c
    cs_narrator "После росы корни и камни оставались скользкими, поэтому спешить не стоило."
    cs_narrator "И неожиданно оказалось, насколько мне этого не хватало."
    cs_narrator "Весь вчерашний день приходилось думать: куда мы попали, почему, кому здесь можно верить."
    cs_narrator "А на бегу думать не нужно."
    cs_narrator "Вдох, выдох, следующий шаг."
    # cs_page_anchor: 8377f211b3f1e53e099d
    cs_narrator "Площадь."
    cs_narrator "Памятник — величественный и совершенно равнодушный к моим проблемам."
    cs_narrator "Закрытая столовая."
    cs_narrator "Клубы."
    cs_narrator "Где-то там Шурик с Электроником, надеюсь, выспались перед очередной встречей с технологиями будущего."
    $ cs_rev_room('bg ext_playground_day')
    # cs_page_anchor: 885f1cddc3060c4dc6ec
    cs_narrator "За спортплощадкой стояли турники."
    cs_narrator "Вчера это был фон из игры."
    cs_narrator "Сегодня — мой турник."
    cs_narrator "Два подхода, растяжка."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Лена?"
    # cs_page_anchor: 2b7b45ffd9a0b6965428
    cs_narrator "Я выпрямилась."
    cs_narrator "На дорожке стояла Ольга Дмитриевна и переводила взгляд с меня на перекладину."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Доброе утро, Ольга Дмитриевна."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: b38b52d5e3f7f0b9ee37
    cs_mt "Доброе."
    cs_mt "Опять до подъёма на турнике?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Опять?"
    cs_narrator "Она чуть заметно запнулась."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 9c7101d80344e72dd8da
    cs_mt "Снова, я хотела сказать."
    cs_mt "Ты ведь и вчера…"
    cs_mt "Нет."
    cs_mt "Вчера вы только приехали."
    cs_mt "Показалось."
    cs_narrator "Она посмотрела на часы — быстрее, чем это было нужно."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Давно ты здесь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 16e39e5dd1734818cb55
    cs_ls "Минут десять."
    cs_ls "До этого бегала по дорожкам."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Одна?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f0bc36c48adbc6176fe8
    cs_ls "Одна."
    cs_ls "Но далеко не уходила."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 25458d7953806025478d
    cs_mt "Спорт — это хорошо."
    cs_mt "Только смотри под ноги, дорожки после ночи сырые."
    cs_mt "И к подъёму возвращайся."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 631d7deabd05041627fd
    cs_ls "Хорошо."
    cs_ls "Только Семёну не рассказывайте."
    cs_ls "Ещё заставит проводить для него занятия."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Вот и была бы тебе работа."
    cs_narrator "Она пошла дальше по дорожке."
    # cs_page_anchor: 381b4441516680aa58d4
    cs_narrator "Вчера она знала моё имя ещё до знакомства."
    cs_narrator "А сейчас обсуждала со мной зарядку так, будто я всегда здесь жила."
    cs_narrator "Вопросов к ней становилось только больше."
    return

label cs_rev_d2_03:
    $ cs_rev_begin(2,3,['cs_semen'])
    $ save_name = "Чужая смена — День 2: Пустая стоянка"
    $ cs_rev_time("day")
    $ cs_rev_costume("sport")
    $ cs_rev_room("bg ext_no_bus")
    stop music fadeout 1.5
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.12)
    # cs_page_anchor: b7403014efacf3c66907
    cs_narrator "Лагерь просыпался: хлопали двери, слышались первые голоса."
    cs_narrator "Автобус оставался единственной понятной связью с Москвой."
    cs_narrator "Стоило хотя бы проверить, на месте ли он."
    # cs_page_anchor: 0e071b81af66fd32922c
    cs_narrator "Я свернула к воротам."
    cs_narrator "И остановилась."
    # cs_page_anchor: 23a5aafdd7d571ac8c64
    cs_narrator "Между деревьями уходила обычная асфальтовая дорога."
    cs_narrator "А там, где вчера стоял «Икарус», было пусто."
    # cs_page_anchor: 6049d9b19eed5aef58de
    cs_narrator "Я подошла к обочине и присела."
    cs_narrator "Мокрый асфальт."
    cs_narrator "Песок у края."
    cs_narrator "И след шин — один, широкий, отпечатавшийся в песке у обочины."
    cs_narrator "Он выходил на дорогу, тянулся метра три и обрывался."
    cs_narrator "Не сворачивал, не стирался постепенно."
    cs_narrator "Просто заканчивался, как будто автобус не уехал, а в какой-то момент перестал ехать."
    # cs_page_anchor: dc61346af783b855a749
    cs_narrator "Транспортное средство, доставившее нас сюда, решило закончить смену раньше пассажиров."
    cs_narrator "Очень мило с его стороны."
    # cs_page_anchor: 583c61395670f23deee9
    cs_narrator "За воротами не было ни стены, ни тумана."
    cs_narrator "Лес, асфальт, утреннее солнце."
    cs_narrator "Именно от этого было не по себе: вчерашняя остановка в Москве тоже выглядела совершенно обычно."
    # cs_page_anchor: 02aa6513a33e146a4c47
    cs_narrator "Я сделала шаг к воротам."
    cs_narrator "Хотя бы до первого поворота…"
    cs_narrator "И вспомнила сонный голос Дарьи."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0157e78d2056442955c8
    cs_ls "Нет."
    cs_ls "Сегодня без самостоятельных экспедиций."
    # cs_page_anchor: 35ef5e8899f1c4dfbc9e
    cs_narrator "Вчера мы попали сюда вместе."
    cs_narrator "Значит, и разбираться будем вместе."
    $ cs_rev_room('bg ext_house_of_mt_day')
    cs_narrator "Возле домиков Семён стоял на крыльце: волосы растрёпаны, рубашка застёгнута через пуговицу, лицо человека, который не давал согласия на наступление утра."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Доброе утро."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 9d08e6cec145004b3340
    cs_sy "Привет."
    cs_sy "Ты откуда такая?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "С пробежки."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Сейчас?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 5dc9749cead813c2886f
    cs_ls "Нет, вчера."
    cs_ls "Просто добежала только сегодня."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Очень смешно."
    # cs_page_anchor: 1aa39940a52406082e4c
    cs_narrator "Он спустился с крыльца."
    cs_narrator "Я понизила голос:"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Автобуса у ворот больше нет."
    cs_narrator "Семён сразу проснулся."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Четыреста десятого?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ec5497ebed9e4d2191bb
    cs_ls "Да."
    cs_ls "И след у него странный."
    cs_ls "Обрывается посреди дороги."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 489b7216beddb6c6c248
    cs_sy "Я после своего приезда его тоже больше не видел."
    cs_sy "Ты за ворота выходила?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: baa80a35b46b68f6ad2d
    cs_ls "Нет."
    cs_ls "Мы с Дашей договорились не проверять дорогу поодиночке."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 2d0fcab4cd9822f3c5c5
    cs_sy "Разумно."
    cs_sy "Даже неожиданно разумно."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Считаю это необоснованным обвинением."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Может, после завтрака сходим втроём?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 375d9bebf390a089cb39
    cs_ls "Сначала обсудим с Дашей."
    cs_ls "И не обязательно идти прямо сегодня."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: f97c68abebbeafecc624
    cs_sy "Ладно."
    cs_sy "И, Лена… не рассказывай пока всем про автобус."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c2622eecc74ba762d767
    cs_ls "Договорились."
    cs_ls "Только наша рабочая группа."
    return

label cs_rev_d2_04:
    $ cs_rev_begin(2,4,['cs_darya', 'cs_semen', 'un'])
    $ save_name = "Чужая смена — День 2: Обычный завтрак"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_house_lena_darya_int_day")
    # cs_page_anchor: 2872c9a23dcc2160a470
    cs_narrator "Дарья уже не спала."
    cs_narrator "Она приподнялась на локте и оглядела меня."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты вся мокрая."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Экспедиция завершена успешно."
    # cs_page_anchor: 46ed68deb3f5e8e68f7c
    cs_narrator "Я рассказала про турник, Ольгу Дмитриевну, Семёна и пустую стоянку."
    cs_narrator "Про след шин — тоже."
    cs_narrator "Дарья выслушала молча, а потом спросила главное:"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "За территорию выходила?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 74d28735d756e394195a
    cs_ls "Нет."
    cs_ls "Обещала ведь."
    cs_narrator "Она ненадолго опустила взгляд."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Спасибо."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Семён предлагает сходить к воротам втроём."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 16a46ba6a5364fa57456
    cs_da "Я не против посмотреть."
    cs_da "Но далеко не уходить."
    cs_da "И сначала завтрак, потом клубы — ты ведь хотела к Шурику с Электроником."
    cs_da "А с дорогой решим, когда будем знать, сколько у нас времени."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Хороший план."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И ты вчера обещала мне обычный завтрак."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Помню."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Без расследований за столом."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b773cdb8cb30b57c22af
    cs_ls "Даш, я с утра уже нашла исчезнувший автобус."
    cs_ls "Совсем без расследований не получится."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Тогда хотя бы сначала умойся."
    $ cs_rev_room('bg ext_washstand_day')
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    # cs_page_anchor: c8624094e13195abd1e7
    cs_narrator "Снаружи раздался горн."
    cs_narrator "Вода в умывальниках оказалась такой, будто её добывали прямо из ледника."
    $ cs_rev_sfx('sound/sfx/water_sink_stream.ogg',0.3)
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 8dc3e7cadf30e213155f
    cs_ls "Меня уже пробежка взбодрила."
    cs_ls "Это контрольный выстрел."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Пойдём, товарищ спортсменка."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Пойдём, товарищ соседка."
    $ cs_rev_room('bg int_dining_hall_people_day')
    $ cs_rev_music(cs_day_music_everyday,0.14,2.5)
    # cs_page_anchor: 53eeed9243a4f662a0a6
    cs_narrator "В столовой было шумно."
    cs_narrator "Звенели ложки, у раздачи собиралась очередь."
    cs_narrator "Каша, хлеб, стакан компота."
    cs_narrator "Сервис без интернета, зато питание включено."
    cs_narrator "Семён уже сидел за столом."
    if cs_met_un and cs_friend_un >= 1:
        # cs_page_anchor: 6e1a8b10ed21b8845737
        cs_narrator "Рядом с ним сидела Лена Тихонова."
        cs_narrator "Она подняла взгляд и тихо кивнула нам."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 41d3b97b0cad447b9425
    cs_sy "Привет."
    cs_sy "Ещё раз."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Какое выразительное приветствие."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: d7fe39f4d7557d453551
    cs_sy "Я тебя с утра уже видел."
    cs_sy "До сих пор не восстановился."
    # cs_page_anchor: b87da0cbef27e4fbcc10
    cs_narrator "Дарья поставила поднос рядом с ним, я — рядом с ней."
    cs_narrator "Семён пожаловался на вчерашний вечер: Ольга Дмитриевна нагрузила его коробками, и стоило закончить одно дело, как находилось другое."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: eba59af76d543946c091
    cs_sy "Но знаешь, как ни странно, помогло."
    cs_sy "Пока таскал, хотя бы не думал всё время об автобусе."
    # cs_page_anchor: 25c850ca7e722bcb2cde
    cs_narrator "У меня для этого была пробежка."
    cs_narrator "У него — поручения."
    cs_narrator "Разные методы, а результат один: когда занимаешься чем-то понятным, мысли перестают ходить по кругу."
    if cs_met_un and cs_friend_un >= 1:
        $ cs_un_name_known = True
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 9c2e6e83b501c4597aed
        cs_un "Доброе утро, Лена."
        cs_un "Ты правда бегала до подъёма?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Правда."
        $ cs_rev_focus("un")
        with cs_sprite_change
        cs_un "А я в это время ещё сплю."
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "Я тоже."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Чувствую себя в меньшинстве."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Лена, передай хлеб, пожалуйста."
        cs_narrator "Мы с Тихоновой одновременно повернулись к нему."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Мне?"
        $ cs_rev_focus("un")
        with cs_sprite_change
        cs_un "Мне?"
        # cs_page_anchor: 4ddc5cc6f0b0858c88e7
        cs_narrator "Семён замер."
        cs_narrator "Посмотрел на одну, потом на другую."
        cs_narrator "Дарья опустила голову, пряча улыбку."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Э-э…"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Товарищ Семён, у нас недостаточная точность идентификации адресата."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Я просто хлеб попросил!"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: a0d9c37944d8b2a572c5
        cs_ls "Предлагаю решение."
        cs_ls "Меня можно звать Соколовой."
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: fb14abb1937d4e193fdf
        cs_un "Тогда меня…"
        cs_un "Тихоновой, наверное."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Спасибо, Соколова."
        # cs_page_anchor: b82b1aecb907ebf4b7ca
        cs_narrator "Я передала ему хлеб."
        cs_narrator "Тихонова снова улыбнулась — и не стала прятать улыбку."
        cs_narrator "Вчера мы успели поговорить о рисовании: о карандашах, бумаге и о том, как нарисовать ветку, чтобы она не закрывала половину домика."
        cs_narrator "Хорошая тема."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 1770285a3fa546f4e62c
        cs_ls "Кстати, твой вчерашний рисунок мне правда понравился."
        cs_ls "Особенно перспектива."
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 9c99c553b2e5be7e061f
        cs_un "Крыша получилась низкой."
        cs_un "И ветка закрывает окно."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: b3e9ba86a39a03cb4136
        cs_ls "Сделай сначала маленький набросок отдельно."
        cs_ls "Посмотри композицию, а потом переноси."
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 62f34b2118ddaa493c0b
        cs_un "Хорошо."
        cs_un "Может… потом порисуем вместе?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 86e3fee8e602a123ebf8
        cs_ls "Обязательно."
        cs_ls "Когда будет свободное время."
        cs_narrator "Она взяла поднос и ушла в библиотеку."
    else:
        pass
    cs_narrator "Когда завтрак подходил к концу, Семён наклонился к нам."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 477c879d18a32569d290
    cs_sy "Насчёт автобуса."
    cs_sy "Я всё думаю, куда ведёт эта дорога."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мы пока даже не знаем, что за воротами."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 7da1820dd276962f362b
    cs_ls "После линейки я хотела в клубы — узнать, что с зарядкой для телефона."
    cs_ls "А с дорогой решим потом."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Можно с вами?"
    # cs_page_anchor: 9948486f520322098f55
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Решать за двоих я сегодня не собиралась."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: a4cbcd98931e84a59c38
    cs_da "Конечно."
    cs_da "Вместе проще."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 8c1bb4cc404a5a518592
    cs_ls "Кстати, Семён."
    cs_ls "У тебя ведь сегодня третий день?"
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Да."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А у нас второй."
    # cs_page_anchor: d904771c75ac5c617ef2
    cs_narrator "Разница в один день."
    cs_narrator "Пока небольшая."
    cs_narrator "Я машинально потянулась к карману за листом наблюдений — он остался в домике."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 430ea06dfd0655d9d142
    cs_da "Запишешь потом."
    cs_da "Два и три — не такие уж сложные числа."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Пока мы втроём, можно просто спросить друг друга."
    # cs_page_anchor: fe0b64a4d0a622060d34
    cs_narrator "А ведь верно."
    cs_narrator "Не каждую мысль нужно сразу превращать в отчёт."
    cs_narrator "Иногда достаточно, чтобы рядом были люди, которые помнят то же самое."
    # cs_page_anchor: e796f668947c5d25b578
    cs_narrator "Остаток завтрака прошёл неожиданно спокойно."
    cs_narrator "Дарья спросила, где в лагере достать бумагу."
    cs_narrator "Семён вспомнил, сколько раз вчера ронял одну и ту же коробку."
    cs_narrator "Совершенно обычный завтрак — если не считать того, что все трое приехали сюда на одном автобусе из разных лет."
    cs_narrator "Мелкая техническая особенность."
    cs_narrator "До линейки оставалось минут двадцать."
    return

label cs_rev_d2_05:
    $ cs_rev_begin(2,5,['cs_darya', 'mi'])
    $ save_name = "Чужая смена — День 2: Ohayou gozaimasu"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_camp_path_day")
    $ cs_rev_music(cs_day_music_friends,0.16,2.5)
    cs_narrator "Семён задержался на крыльце столовой — выяснял у кого-то время линейки, — а мы с Дарьей пошли по дорожке."
    # cs_page_anchor: d8e9999677d45415ff86
    cs_narrator "Навстречу шла девушка с бирюзовыми волосами."
    cs_narrator "Два длинных хвоста покачивались при каждом шаге, под мышкой папка с нотами."
    cs_narrator "Она что-то негромко напевала, заглядывая в лист."
    # cs_page_anchor: c577884927bbf77ac41e
    cs_narrator "Вчера я сказала Дарье про Женю: «знаю по игре»."
    cs_narrator "И в результате устроила разговор, к которому никто из нас не был готов."
    cs_narrator "Сегодня попробуем иначе."
    cs_narrator "Без рассказов о будущем."
    cs_narrator "Просто познакомимся."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    cs_mi "Доброе утро!"
    cs_narrator "Я ответила почти автоматически:"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "{font=[cs_japanese_font]}おはようございます。元気ですか？{/font}"
    # cs_page_anchor: 18e90f9a6d5cd86f9bb7
    cs_th "Доброе утро."
    cs_th "Как дела?"
    # cs_page_anchor: 8a8a2d069c342020d9f8
    cs_narrator "Мику остановилась."
    cs_narrator "А потом её лицо буквально озарилось."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    cs_mi "{font=[cs_japanese_font]}えっ、日本語が話せるの？{/font}"
    cs_th "Ой, ты говоришь по-японски?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "{font=[cs_japanese_font]}少しだけ。{/font}"
    cs_th "Немного."
    # cs_page_anchor: d150f32f8b1b02ea67f1
    cs_narrator "И тут Мику заговорила быстро."
    cs_narrator "Очень быстро."
    cs_narrator "Я уловила вопрос про учёбу, а дальше потеряла нить."
    cs_narrator "Учебники меня к такому не готовили."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "{font=[cs_japanese_font]}Подожди. ゆっくり話してくれる？{/font}"
    cs_th "Можешь помедленнее?"
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: d3fbd75ddbff316be55d
    cs_mi "Ой, извини!"
    cs_mi "Просто здесь почти никто не говорит по-японски, а ты вдруг подходишь и сразу здороваешься!"
    cs_mi "Мама у меня японка, папа русский, я дома слышала оба языка и иногда даже не замечаю, на какой перехожу."
    cs_mi "А где ты учила?"
    cs_mi "А читать умеешь?"
    cs_mi "А писать?"
    cs_mi "Хотя иероглифы гораздо сложнее…"
    cs_narrator "Она осеклась."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    cs_mi "Я опять слишком быстро говорю?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9e45384661a59acf3630
    cs_ls "Немного."
    cs_ls "Зато теперь понимаю, почему ты так обрадовалась."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я поняла только «доброе утро»."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Значит, четверть переговоров прошла успешно."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: a86540aedf8367f1231d
    cs_mi "Вы же те самые новенькие?"
    cs_mi "Мне рассказывали — две девушки с необычными волосами!"
    cs_mi "Ой, я даже не представилась."
    cs_mi "Мику."
    $ cs_met_mi = True
    $ cs_mi_name_known = True
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Лена Соколова."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Даша."
    # cs_page_anchor: 02d326765cfd3eac03ce
    cs_narrator "Из папки выглядывали нотные листы."
    cs_narrator "Мику объяснила, что вечером на площади будет музыкальный вечер, а свою мелодию — она сочинила её сама, этим летом, — она то ли играет слишком быстро, то ли нет, и перед линейкой хотела это проверить."
    cs_narrator "И спросила, интересуемся ли мы музыкой."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: a0b6444c5584120b8745
    cs_da "Люблю слушать."
    cs_da "Когда-то училась играть на пианино."
    cs_da "Но это было давно."
    # cs_page_anchor: 5891602fe8d4657be24a
    cs_narrator "Пианино?"
    cs_narrator "Об этом я не знала."
    cs_narrator "Странно: мы успели обсудить возвращение домой, автобус и даже мои чувства к ней."
    cs_narrator "А про музыку я не спросила ни разу."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "И молчала?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты не спрашивала."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Справедливо."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 51e2e2a888affe61202c
    cs_mi "Тогда заходите!"
    cs_mi "Тут рядом."
    cs_mi "Я только папку оставлю — и вместе на линейку!"
    $ cs_rev_room('bg int_musclub_day')
    stop music fadeout 1.5
    $ cs_rev_sfx('sound/sfx/open_door_clubs.ogg',0.3)
    # cs_page_anchor: 361ffe88929821ba5f10
    cs_narrator "В кружке пахло деревом и старым лаком."
    cs_narrator "Потёртые края инструментов, следы карандаша на нотах, один неровно поставленный стул — всё то, чего не видно на игровом фоне."
    # cs_page_anchor: 2575cd5f931ccef41f61
    cs_narrator "Мику положила папку на стол."
    cs_narrator "Та немедленно раскрылась, и листы поехали к краю."
    cs_narrator "Один поймала Мику, второй — Дарья, третий я подняла с пола."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    cs_mi "Хочешь попробовать?"
    # cs_page_anchor: caa55d09757794a7547c
    cs_narrator "Она кивнула Дарье на пианино."
    cs_narrator "Дарья посмотрела на клавиши, потом на меня."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Не смейся, если я перепутаю ноты."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Торжественно обещаю."
    # cs_page_anchor: 3a375006c73a010c9289
    cs_narrator "Она села."
    cs_narrator "Нажала одну клавишу."
    cs_narrator "Вторую."
    cs_narrator "На третьей поморщилась."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Уже забыла."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 46743230ce7d7a514a95
    cs_mi "Начни медленнее."
    cs_mi "Руки вспомнят."
    $ cs_rev_music(cs_darya_piano_track,0.22)
    $ cs_rev_room('cs_cg_darya_piano_day')
    # cs_page_anchor: 70549a0392f56dcb3137
    cs_narrator "И Дарья начала играть."
    cs_narrator "Сначала отдельные ноты, потом короткая фраза."
    cs_narrator "Простая мелодия, немного задумчивая, с неровными переходами."
    cs_narrator "В середине она сбилась, улыбнулась своей ошибке и сыграла этот кусок ещё раз — уже лучше."
    cs_narrator "Я стояла у стола и совершенно забыла, что собиралась комментировать."
    # cs_page_anchor: 778433f981a818ccc43b
    cs_narrator "Мы знакомы меньше двух дней, а я уже решила, что понимаю её характер."
    cs_narrator "Спокойная."
    cs_narrator "Внимательная."
    cs_narrator "Иногда ироничная."
    cs_narrator "Умеет вовремя меня остановить."
    # cs_page_anchor: e457ec424b4988486d92
    cs_narrator "А сейчас она просто пыталась сыграть то, что помнила."
    cs_narrator "Без всякой попытки произвести впечатление."
    cs_narrator "И почему-то именно это было особенно красиво."
    stop music fadeout 1.5
    cs_narrator "Мелодия закончилась тихим аккордом."
    $ cs_rev_room('bg int_musclub_day')
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 6692830b4d5035ef8022
    cs_mi "Очень мило!"
    cs_mi "Середина немного сбилась, но начало красивое."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ну что, обещание не смеяться выполнила?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 3fabd96da8c3cfd45926
    cs_ls "Более чем."
    cs_ls "Мне очень понравилось."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Даже с ошибками?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Особенно потому, что ты не бросила на первой."
    # cs_page_anchor: 4e190a5598ec2931194e
    cs_narrator "Она опустила взгляд."
    cs_narrator "На губах появилась лёгкая улыбка."
    cs_narrator "Я не стала добавлять ничего лишнего — кажется, постепенно учусь вовремя замолкать."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 6c2609be992f203d74e4
    cs_mi "А можно я теперь свой кусочек?"
    cs_mi "Я не знаю, не слишком ли растянула вступление."
    cs_mi "Если что-то покажется странным — говорите!"
    cs_narrator "До линейки оставалось совсем немного."
    if "2:1" in cs_rev_choices:
        if cs_rev_choices["2:1"]==0:
            $ cs_rev_choice(2,1,0)
            $ cs_day02_miku_listened = True
            $ cs_rev_award("2:1:cs_friend_mi","cs_friend_mi",1)
            $ cs_day02_miku_listened = True
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Несколько минут у нас есть."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Я тоже хочу послушать."
            $ cs_rev_music(cs_miku_piano_track,0.22)
            $ cs_rev_room('cs_cg_miku_piano_day')
            # cs_page_anchor: 609892be3ee79ce00a11
            cs_narrator "Мику играла увереннее Дарьи — она не искала клавиши."
            cs_narrator "В середине одна и та же музыкальная фраза повторилась несколько раз, и Мику вдруг остановилась."
            stop music fadeout 1.5
            $ cs_rev_room('bg int_musclub_day')
            $ cs_rev_focus("mi")
            with cs_sprite_change
            # cs_page_anchor: 67872c6199e9bf0647dd
            cs_mi "Вот!"
            cs_mi "Вам не кажется, что вступление слишком долгое?"
            cs_mi "Мне каждую часть жалко убирать."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: ab1ff024ad0d8b7b7618
            cs_ls "Мелодия хорошая."
            cs_ls "Но когда фраза повторяется три раза, начинаешь ждать, что дальше будет что-то новое."
            $ cs_rev_focus("da")
            with cs_sprite_change
            # cs_page_anchor: 10ab4f9b5c1d1b994c00
            cs_da "Я бы сократила второе повторение."
            cs_da "Тогда переход прозвучит неожиданнее."
            $ cs_rev_music(cs_miku_piano_track,0.22)
            # cs_page_anchor: 1d8736d115d7d3ed07e2
            cs_narrator "Мику сделала карандашом пометку и сыграла ещё раз."
            cs_narrator "Мелодия будто быстрее нашла своё направление."
            stop music fadeout 1.5
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Так лучше."
            $ cs_rev_focus("mi")
            with cs_sprite_change
            # cs_page_anchor: dda4009421344e88708b
            cs_mi "Спасибо!"
            cs_mi "Я его сегодня третий раз переделываю."
            cs_mi "Когда сама придумала, кажется, что всё понятно."
            cs_mi "А потом кто-нибудь послушает — и нет."
            # cs_page_anchor: 9052b08f60dac93af47d
            cs_narrator "С рисунками у меня то же самое."
            cs_narrator "Часами смотришь на свою работу и перестаёшь видеть ошибки."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "С рисунками такая же история."
            $ cs_rev_focus("mi")
            with cs_sprite_change
            # cs_page_anchor: 12626a51b05abde6e1f3
            cs_mi "Ты рисуешь?"
            cs_mi "Тогда приходи как-нибудь рисовать сюда, у нас ребята делают плакаты для выступлений!"
            $ cs_rev_music(cs_miku_piano_track,0.22)
            # cs_page_anchor: 308223d3fff8726f043e
            cs_narrator "Пока Мику доигрывала, я села на длинную лавку у стены."
            cs_narrator "Лавка оказалась на высоких ножках, и ступни до пола не достали."
            cs_narrator "Советский Союз впервые одержал надо мной архитектурную победу."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Ты до пола не достаёшь?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Благодарю за точную диагностику."
            # cs_page_anchor: 10eba3b07b48be299e0e
            cs_narrator "Дарья села рядом."
            cs_narrator "Я покачивала ногами в такт мелодии, слушала и вдруг поняла, что мне хорошо."
            cs_narrator "Не потому, что мы нашли дорогу домой: автобус по-прежнему был загадкой, а телефон по-прежнему не работал."
            cs_narrator "Просто можно было сидеть, слушать музыку и иногда поглядывать на Дарью."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: cbb9ca1f6a51443b77fd
            cs_ls "Вот так и деградирует человек из две тысячи двадцать шестого."
            cs_ls "Вчера смартфон и графический планшет."
            cs_ls "Сегодня — лавка и бесплатный концерт."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "И что, плохо?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Как ни странно, совсем неплохо."
            stop music fadeout 1.5
            $ cs_rev_focus("mi")
            with cs_sprite_change
            cs_mi "Ой, нам же на линейку!"
            cs_narrator "Я слезла с лавки и поставила обе ноги на пол."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Связь с землёй восстановлена."
            $ cs_rev_finish_choice(2,1)
        else:
            $ cs_rev_choice(2,1,1)
            $ cs_day02_miku_listened = False
            $ cs_day02_miku_listened = False
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 46245b92b24ff09aef36
            cs_ls "Нам, наверное, уже пора."
            cs_ls "Не хочется опоздать на линейку."
            $ cs_rev_focus("mi")
            with cs_sprite_change
            # cs_page_anchor: 3275b1142a3b298ddf25
            cs_mi "Ой, точно!"
            cs_mi "Я совсем про время забыла."
            cs_mi "Приходите ещё — в следующий раз нормально посидим!"
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Спасибо, что показала кружок."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "А тебе, Даш, отдельное спасибо за неожиданную демонстрацию скрытых талантов."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Так уже лучше, чем «выступление»."
            $ cs_rev_finish_choice(2,1)
    else:
        menu:
            "Остаться и послушать репетицию Мику":
                $ cs_rev_choice(2,1,0)
                $ cs_day02_miku_listened = True
                $ cs_rev_award("2:1:cs_friend_mi","cs_friend_mi",1)
                $ cs_day02_miku_listened = True
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Несколько минут у нас есть."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Я тоже хочу послушать."
                $ cs_rev_music(cs_miku_piano_track,0.22)
                $ cs_rev_room('cs_cg_miku_piano_day')
                # cs_page_anchor: 5cf809e0b93899d29bbd
                cs_narrator "Мику играла увереннее Дарьи — она не искала клавиши."
                cs_narrator "В середине одна и та же музыкальная фраза повторилась несколько раз, и Мику вдруг остановилась."
                stop music fadeout 1.5
                $ cs_rev_room('bg int_musclub_day')
                $ cs_rev_focus("mi")
                with cs_sprite_change
                # cs_page_anchor: 2eaa7151bf8255e222d4
                cs_mi "Вот!"
                cs_mi "Вам не кажется, что вступление слишком долгое?"
                cs_mi "Мне каждую часть жалко убирать."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: a30de2aab122f9828fe2
                cs_ls "Мелодия хорошая."
                cs_ls "Но когда фраза повторяется три раза, начинаешь ждать, что дальше будет что-то новое."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: f712f405e65cd1fc5fd6
                cs_da "Я бы сократила второе повторение."
                cs_da "Тогда переход прозвучит неожиданнее."
                $ cs_rev_music(cs_miku_piano_track,0.22)
                # cs_page_anchor: 10fe8d1720208c9b354a
                cs_narrator "Мику сделала карандашом пометку и сыграла ещё раз."
                cs_narrator "Мелодия будто быстрее нашла своё направление."
                stop music fadeout 1.5
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Так лучше."
                $ cs_rev_focus("mi")
                with cs_sprite_change
                # cs_page_anchor: 8f1c991720ed9d221d75
                cs_mi "Спасибо!"
                cs_mi "Я его сегодня третий раз переделываю."
                cs_mi "Когда сама придумала, кажется, что всё понятно."
                cs_mi "А потом кто-нибудь послушает — и нет."
                # cs_page_anchor: 169b6c176f5b7f4b36f6
                cs_narrator "С рисунками у меня то же самое."
                cs_narrator "Часами смотришь на свою работу и перестаёшь видеть ошибки."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "С рисунками такая же история."
                $ cs_rev_focus("mi")
                with cs_sprite_change
                # cs_page_anchor: 99c4194803ac7da56a0b
                cs_mi "Ты рисуешь?"
                cs_mi "Тогда приходи как-нибудь рисовать сюда, у нас ребята делают плакаты для выступлений!"
                $ cs_rev_music(cs_miku_piano_track,0.22)
                # cs_page_anchor: 4f0862a75d6f9ecb1b3b
                cs_narrator "Пока Мику доигрывала, я села на длинную лавку у стены."
                cs_narrator "Лавка оказалась на высоких ножках, и ступни до пола не достали."
                cs_narrator "Советский Союз впервые одержал надо мной архитектурную победу."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Ты до пола не достаёшь?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Благодарю за точную диагностику."
                # cs_page_anchor: fa77cdcddea6e4427187
                cs_narrator "Дарья села рядом."
                cs_narrator "Я покачивала ногами в такт мелодии, слушала и вдруг поняла, что мне хорошо."
                cs_narrator "Не потому, что мы нашли дорогу домой: автобус по-прежнему был загадкой, а телефон по-прежнему не работал."
                cs_narrator "Просто можно было сидеть, слушать музыку и иногда поглядывать на Дарью."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: c4d19944915f8596a4fa
                cs_ls "Вот так и деградирует человек из две тысячи двадцать шестого."
                cs_ls "Вчера смартфон и графический планшет."
                cs_ls "Сегодня — лавка и бесплатный концерт."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "И что, плохо?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Как ни странно, совсем неплохо."
                stop music fadeout 1.5
                $ cs_rev_focus("mi")
                with cs_sprite_change
                cs_mi "Ой, нам же на линейку!"
                cs_narrator "Я слезла с лавки и поставила обе ноги на пол."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Связь с землёй восстановлена."
                $ cs_rev_finish_choice(2,1)
            "Поблагодарить Мику и пойти на линейку":
                $ cs_rev_choice(2,1,1)
                $ cs_day02_miku_listened = False
                $ cs_day02_miku_listened = False
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 2490c4bb9eac5f64130d
                cs_ls "Нам, наверное, уже пора."
                cs_ls "Не хочется опоздать на линейку."
                $ cs_rev_focus("mi")
                with cs_sprite_change
                # cs_page_anchor: 1c3f2fa6135d5bfe8d3f
                cs_mi "Ой, точно!"
                cs_mi "Я совсем про время забыла."
                cs_mi "Приходите ещё — в следующий раз нормально посидим!"
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Спасибо, что показала кружок."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "А тебе, Даш, отдельное спасибо за неожиданную демонстрацию скрытых талантов."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Так уже лучше, чем «выступление»."
                $ cs_rev_finish_choice(2,1)
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Почему ты вчера не сказала, что играешь?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 4e63456b9617ee84aa31
    cs_da "Ты вчера была занята более важными вещами."
    cs_da "Автобус."
    cs_da "Будущее."
    cs_da "Советская электроника."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Это всё было важно."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И собственное признание."
    # cs_page_anchor: eeb4d1062ab177c035e4
    cs_narrator "Я покосилась на неё."
    cs_narrator "Она улыбалась."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Это тоже было важное событие."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я заметила."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "А почему перестала играть?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 7ac95a84ee2072ec3022
    cs_da "Не знаю."
    cs_da "Появились другие дела."
    cs_da "Потом просто не вернулась."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b342969113fdb329f23b
    cs_ls "У меня так было с рисунками."
    cs_ls "Откладываешь на месяц, а находишь через полгода."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Только пианино сложнее убрать в папку."
    $ cs_rev_room('bg ext_square_day')
    # cs_page_anchor: 3b1819155ca40fd44b80
    cs_narrator "Мы подошли к площади."
    cs_narrator "Пионеры строились перед Ольгой Дмитриевной, Семён махал нам рукой."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Что?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 774e9a534b09f257de2c
    cs_ls "Ничего."
    cs_ls "Просто хорошее получилось утро."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Даже с исчезнувшим автобусом?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Хорошее утро и хорошие новости — не всегда одно и то же."
    return

label cs_rev_d2_06:
    $ cs_rev_begin(2,6,['cs_darya', 'cs_semen', 'mt', 'sl'])
    $ save_name = "Чужая смена — День 2: Линейка"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_square_day")
    $ cs_rev_music(cs_day_music_daily,0.16)
    # cs_page_anchor: 488bc4bb73f8d58f00a8
    cs_narrator "Ульяна что-то оживлённо объясняла Алисе, размахивая руками."
    cs_narrator "Алиса слушала с видом человека, который уже пожалел, что не ушёл раньше."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Вы куда пропали?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Участвовали в развитии международных культурных связей."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "А обычными словами?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 5c5d8f1041512be93fee
    cs_da "Были в музыкальном кружке."
    cs_da "Познакомились с Мику."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "А. Понятно."
    $ cs_rev_room('cs_cg_morning_lineup_day')
    $ cs_rev_sfx('sound/sfx/dinner_jingle_speaker.ogg',0.5)
    # cs_page_anchor: d2b1006004d5475f2e6a
    cs_narrator "Ольга Дмитриевна напомнила про порядок у домиков, дежурства и кружки."
    cs_narrator "Потом перешла к вечеру."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 8be4a5a2f5a3db1decb3
    cs_mt "После ужина у нас музыкальный вечер на площади."
    cs_mt "Нужно объявление, чтобы все знали."
    cs_mt "Кто у нас умеет рисовать?"
    $ cs_rev_room('bg ext_square_day')
    # cs_page_anchor: 2f8037fc575e99dd41ac
    cs_narrator "Я помолчала."
    cs_narrator "Потом подняла руку."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Могу попробовать."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 4f34b4a55220dcef7e06
    cs_mt "Отлично."
    cs_mt "Славя поможет с материалами."
    cs_mt "Только, Лена, не увлекайся."
    cs_mt "Главное — чтобы все могли прочитать время и место."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Постараюсь не превращать объявление в дипломную работу."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Значит, теперь ты у нас художник-оформитель?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "А ты назначаешься ответственным за моральную поддержку."
    # cs_page_anchor: 2679fb2fe4a961559985
    cs_narrator "Славя шла навстречу с коробкой в руках и папкой под мышкой."
    cs_narrator "Две светлые косы, аккуратно повязанный галстук и вид человека, который точно знает, куда идёт."
    cs_narrator "Даже коробка не мешала ей выглядеть так, будто она направляется получать грамоту."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: e8b0fc215635bc966b05
    cs_sl "Доброе утро!"
    cs_sl "Ольга Дмитриевна сказала вам про объявление?"
    cs_sl "Я принесла бумагу и карандаши."
    cs_sl "Только сначала нужно отнести это в кладовую."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 70bf0dfcbcde261c1a71
    cs_ls "Славя, тебе никто не говорил, что ты будто сошла с советского плаката?"
    cs_ls "«Образцовый пионер всегда готов»."
    # cs_page_anchor: f9732f23b4ad7945ba1c
    cs_narrator "Славя удивлённо моргнула."
    cs_narrator "Потом рассмеялась."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: d2c79449dee33651aeee
    cs_sl "Ничего подобного."
    cs_sl "Вчера я, например, полчаса искала ключ от кладовой."
    cs_sl "А сама же оставила его у вожатой."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Значит, даже у образцовых пионеров бывают технические неисправности."
    $ cs_rev_room('cs_storage_ext_day')
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Лен, по-моему, ты сама сейчас похожа на автора агитационного плаката."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: 1c557718b6a07b43ea6b
    cs_sl "Вы смешные."
    cs_sl "Ладно, отнесу коробку — и покажу, где можно работать."
    if "2:2" in cs_rev_choices:
        if cs_rev_choices["2:2"]==0:
            $ cs_rev_choice(2,2,0)
            $ cs_helped_sl_day2 = True
            $ cs_rev_award("2:2:cs_friend_sl","cs_friend_sl",1)
            $ cs_sl_day2_awarded = True
            $ cs_helped_sl_day2 = True
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 1051ecb97f54fc4bebc4
            cs_ls "Давай помогу."
            cs_ls "Вдвоём быстрее."
            # cs_page_anchor: 2c05eb6fe62fea373c33
            cs_narrator "Славя передала мне коробку."
            cs_narrator "Внутри что-то немедленно загремело."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Кажется, здесь собрание мелких предметов без утверждённого порядка размещения."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Там всё лежало нормально!"
            # cs_page_anchor: cb0dbeab9273795b5916
            cs_narrator "Дарья взяла папку."
            cs_narrator "Семёну достались катушка верёвки и ещё одна коробка."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Я правильно понимаю, что просто оказался рядом?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Добро пожаловать в трудовой коллектив."
            cs_narrator "По дороге Славя рассказала, что вечером точно будет выступать Мику, а Алиса, кажется, тоже."
            if cs_day02_miku_listened:
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Мы утром немного послушали её репетицию."
            else:
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Она утром показала нам кружок."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Ей нравится, когда кто-нибудь приходит."
            # cs_page_anchor: 63907c61b7925b7b062c
            cs_narrator "В кладовой Славя достала из кармана листок с делами на день."
            cs_narrator "Несколько строк."
            cs_narrator "Потом ещё несколько."
            cs_narrator "И ещё."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Славя, у нас разные определения слова «немного»."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Часть уже сделана!"
            cs_narrator "Она выдала нам карандаши, ластик и несколько листов."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "А ты правда любишь рисовать?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Дома это одно из главных моих занятий."
            $ cs_rev_focus("da")
            with cs_sprite_change
            # cs_page_anchor: b83b56b13b318eb88835
            cs_da "Только дома она рисует на планшете."
            cs_da "А тут даже кнопки отмены нет."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Какой кнопки?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: f9acd3fb903f8eb0d375
            cs_ls "Долгая история."
            cs_ls "Иногда очень хочется стереть неудачную линию одним движением."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Для этого есть ластик."
            cs_narrator "И ведь не поспоришь."
            $ cs_rev_finish_choice(2,2)
        else:
            $ cs_rev_choice(2,2,1)
            $ cs_helped_sl_day2 = False
            $ cs_helped_sl_day2 = False
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Тогда мы пока подготовим место, если ты не против."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            # cs_page_anchor: cc44e537f7cd73472540
            cs_sl "Конечно."
            cs_sl "Вот листы и карандаши."
            cs_sl "Только не пишите пока время крупно — я ещё уточню, когда выступление."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Сначала исходные данные, потом производство."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Именно."
            # cs_page_anchor: 569d936b7b4492253341
            cs_narrator "Славя справится сама."
            cs_narrator "А у нас уже есть первое поручение."
            $ cs_rev_finish_choice(2,2)
    else:
        menu:
            "Предложить Славе помощь с материалами":
                $ cs_rev_choice(2,2,0)
                $ cs_helped_sl_day2 = True
                $ cs_rev_award("2:2:cs_friend_sl","cs_friend_sl",1)
                $ cs_sl_day2_awarded = True
                $ cs_helped_sl_day2 = True
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: f3bdc2d706485ec88067
                cs_ls "Давай помогу."
                cs_ls "Вдвоём быстрее."
                # cs_page_anchor: a062e55cfcf44b87ea3a
                cs_narrator "Славя передала мне коробку."
                cs_narrator "Внутри что-то немедленно загремело."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Кажется, здесь собрание мелких предметов без утверждённого порядка размещения."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "Там всё лежало нормально!"
                # cs_page_anchor: 2cc515a0579ddbad1f07
                cs_narrator "Дарья взяла папку."
                cs_narrator "Семёну достались катушка верёвки и ещё одна коробка."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Я правильно понимаю, что просто оказался рядом?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Добро пожаловать в трудовой коллектив."
                cs_narrator "По дороге Славя рассказала, что вечером точно будет выступать Мику, а Алиса, кажется, тоже."
                if cs_day02_miku_listened:
                    $ cs_rev_focus("da")
                    with cs_sprite_change
                    cs_da "Мы утром немного послушали её репетицию."
                else:
                    $ cs_rev_focus("da")
                    with cs_sprite_change
                    cs_da "Она утром показала нам кружок."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "Ей нравится, когда кто-нибудь приходит."
                # cs_page_anchor: 44cd4372dace24c62fb4
                cs_narrator "В кладовой Славя достала из кармана листок с делами на день."
                cs_narrator "Несколько строк."
                cs_narrator "Потом ещё несколько."
                cs_narrator "И ещё."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Славя, у нас разные определения слова «немного»."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "Часть уже сделана!"
                cs_narrator "Она выдала нам карандаши, ластик и несколько листов."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "А ты правда любишь рисовать?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Дома это одно из главных моих занятий."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: 13716372125b5a4b2c49
                cs_da "Только дома она рисует на планшете."
                cs_da "А тут даже кнопки отмены нет."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "Какой кнопки?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: f4162d49dd5ccaa52943
                cs_ls "Долгая история."
                cs_ls "Иногда очень хочется стереть неудачную линию одним движением."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "Для этого есть ластик."
                cs_narrator "И ведь не поспоришь."
                $ cs_rev_finish_choice(2,2)
            "Поблагодарить Славю и заняться объявлением":
                $ cs_rev_choice(2,2,1)
                $ cs_helped_sl_day2 = False
                $ cs_helped_sl_day2 = False
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Тогда мы пока подготовим место, если ты не против."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                # cs_page_anchor: 66c9cf3cbc367a4f0044
                cs_sl "Конечно."
                cs_sl "Вот листы и карандаши."
                cs_sl "Только не пишите пока время крупно — я ещё уточню, когда выступление."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Сначала исходные данные, потом производство."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                cs_sl "Именно."
                # cs_page_anchor: a96f38ed3aca7f54e3b9
                cs_narrator "Славя справится сама."
                cs_narrator "А у нас уже есть первое поручение."
                $ cs_rev_finish_choice(2,2)
    $ cs_rev_room('bg ext_clubs_day')
    # cs_page_anchor: 8e3815f2c53b898ca601
    cs_narrator "Возле клубов под навесом нашёлся стол."
    cs_narrator "Дарья разложила бумагу и прижала края ладонями."
    cs_narrator "Несколько секунд мы смотрели на чистый лист."
    # cs_page_anchor: 4e61a47d4980ddda0b21
    cs_narrator "Знакомое чувство."
    cs_narrator "В Москве оно возникало перед экраном планшета: чистый холст, никаких ограничений — кроме того, что начинать всегда сложнее, чем продолжать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: aa0ccd027f006c35bbce
    cs_da "Может, сначала зайдём к Шурику с Электроником?"
    cs_da "Пока не начали всерьёз."
    # cs_page_anchor: eedea0568512df57c16c
    cs_narrator "Я коснулась кармана."
    cs_narrator "Телефон был там."
    cs_narrator "Выключенный, но целый."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 97ed3b27859f7e9e0896
    cs_ls "Давайте."
    cs_ls "Художественный проект подождёт несколько минут."
    return

label cs_rev_d2_07:
    $ cs_rev_begin(2,7,['cs_darya', 'cs_semen', 'el', 'sh'])
    $ save_name = "Чужая смена — День 2: Источник питания"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_clubs_male_day")
    $ cs_rev_music("sound/music/smooth_machine.ogg",0.16)
    $ cs_rev_sfx('sound/sfx/open_door_clubs_2.ogg',0.3)
    # cs_page_anchor: af55f6eae9f27630368a
    cs_narrator "Вчера на столе в кружке лежали вещи в относительном порядке."
    cs_narrator "Сегодня его занимали провода, измерительные приборы и самодельная конструкция, которую я не рискнула бы назвать зарядным устройством без заключения специалистов."
    $ cs_rev_focus("el")
    with cs_sprite_change
    # cs_page_anchor: 23ad6118b1f7f543c56a
    cs_el "О, привет!"
    cs_el "А мы как раз тебя вспоминали!"
    $ cs_rev_focus("sh")
    with cs_sprite_change
    # cs_page_anchor: 9c1e7d01f53da62108fd
    cs_sh "Источник питания."
    cs_sh "Напряжение регулируется, под нагрузкой держит стабильно."
    $ cs_rev_focus("el")
    with cs_sprite_change
    # cs_page_anchor: df293f025c76dea03d41
    cs_el "А вот переходник не получился."
    cs_el "Разъём у тебя какой-то… невозможный."
    cs_narrator "Я положила телефон на свободный край стола."
    $ cs_rev_focus("sh")
    with cs_sprite_change
    # cs_page_anchor: a3d2fe837dd89ce7c79f
    cs_sh "Электричество есть."
    cs_sh "Безопасного способа подать его на это устройство — нет."
    cs_sh "Подключим неправильно — испортим то, что внутри."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0f638fc47eccba04f142
    cs_ls "Поэтому никаких опытов на самом телефоне."
    cs_ls "И вскрывать по-прежнему запрещаю."
    $ cs_rev_focus("el")
    with cs_sprite_change
    cs_el "Мы даже не собирались!"
    cs_narrator "Шурик посмотрел на него."
    $ cs_rev_focus("el")
    with cs_sprite_change
    cs_el "Ну… почти."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Может, подходящий провод где-нибудь найдётся?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b81aeecbabe6d37ab258
    cs_ls "Этот разъём появился намного позже вашего оборудования."
    cs_ls "Лет на тридцать."
    cs_narrator "Шурик нахмурился, но спорить не стал."
    # cs_page_anchor: 5ee581a16a9094271329
    cs_narrator "Научно-техническая революция откладывается."
    cs_narrator "И всё же особого разочарования я не чувствовала."
    cs_narrator "Вчера отсутствие зарядки казалось неразрешимой проблемой."
    cs_narrator "Сегодня стало понятно, из чего она состоит."
    cs_narrator "Есть источник."
    cs_narrator "Есть устройство."
    # cs_page_anchor: f707e1415d4f8fe035fa
    cs_narrator "Между ними нет подходящего соединения."
    cs_narrator "Задача неприятная — но вполне определённая."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Лучше ещё один день без телефона, чем окончательно испорченный телефон."
    $ cs_rev_focus("sh")
    with cs_sprite_change
    cs_sh "Вот именно."
    # cs_page_anchor: 364834a6e0d3fbf0ae02
    cs_narrator "Пока Шурик показывал Дарье, как работает регулятор, я обошла стол, чтобы посмотреть на блок сбоку."
    cs_narrator "И задела локтем угол раскрытого шасси — острый край листового металла."
    cs_narrator "Короткое жжение."
    cs_narrator "Я даже не посмотрела на руку."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: f4a920de08fee369c7b7
    cs_sy "Я схожу к Ольге Дмитриевне, уточню время вечера."
    cs_sy "А вы пока рисуйте."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 7e9f39cfabb44555f555
    cs_ls "Только не потеряй папку, товарищ Семён."
    cs_ls "Утрата художественного имущества карается общественным порицанием."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Очень страшно."
    $ cs_rev_room('bg ext_clubs_day')
    $ cs_lena_elbow_injury_day2 = max(1,cs_lena_elbow_injury_day2)
    # cs_page_anchor: 7b57320644e0830686ad
    cs_narrator "Он ушёл к площади."
    cs_narrator "Мы вышли на крыльцо, и тут я почувствовала жжение снова."
    cs_narrator "На локте была царапина — неглубокая, но длинная, с выступившими капельками крови."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: cf55b21741482096ebe3
    cs_da "Лен, ты поцарапалась?"
    cs_da "Покажи."
    cs_narrator "Она повернула мою руку к свету."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 93f0328f7090d4facbe8
    cs_da "Небольшая."
    cs_da "Но лучше обработать."
    cs_da "Об железо же."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Организм предпочёл бы просто забыть о её существовании."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А ты предпочла бы потом объяснять, откуда воспаление?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Аргумент принят."
    # cs_page_anchor: 022a7433f6f503b222a6
    cs_narrator "Медпункт."
    cs_narrator "Белые шкафы, кушетка, рабочий стол."
    cs_narrator "И медсестра, которая умела разговаривать так, что даже Семён иногда терялся."
    # cs_page_anchor: e5694227f3630578e807
    cs_narrator "Виола."
    cs_narrator "Ну здравствуйте."
    return

label cs_rev_d2_08:
    $ cs_rev_begin(2,8,['cs', 'cs_darya'])
    $ save_name = "Чужая смена — День 2: Медпункт"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_aidpost_day")
    cs_narrator "Дорожка к медпункту становилась всё тише."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: ba86564e28ec32b89d87
    cs_da "Ты знаешь дорогу?"
    cs_da "По игре?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 70b4234c3dbc3f879e40
    cs_ls "Отчасти."
    cs_ls "Хотя за два дня уже кое-что запомнила."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Тебя не пугает, насколько многое здесь совпадает?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Пугает."
    cs_narrator "Это прозвучало серьёзнее, чем я хотела."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Просто если останавливаться у каждого знакомого здания, мы до вечера даже столовую не обойдём."
    # cs_page_anchor: 99b78fb7b1127ffd4919
    cs_narrator "Хотя дело не только в зданиях."
    cs_narrator "У людей здесь знакомые лица и имена."
    cs_narrator "Но они постоянно делают что-нибудь неожиданное."
    cs_narrator "Женя оказалась наблюдательнее, чем я думала."
    cs_narrator "Славя спокойно шутит в ответ."
    cs_narrator "А про Дарью я вообще почти ничего не знаю — и каждый разговор открывает в ней что-то новое."
    $ cs_rev_room('bg int_aidpost_day')
    stop music fadeout 1.5
    $ cs_rev_sfx('sound/sfx/medpunkt_door_open.ogg',0.4)
    # cs_page_anchor: b1622ee96f533d3f4e01
    cs_narrator "Может, так и надо относиться ко всему лагерю."
    cs_narrator "Не угадывать, кто как поступит."
    cs_narrator "Просто узнавать людей."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Входите."
    # cs_page_anchor: 59b7b0187ae39bba7db0
    cs_narrator "Внутри пахло антисептиком."
    cs_narrator "За столом сидела женщина в белом халате и что-то записывала в журнал."
    cs_narrator "Я узнала её сразу."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 714a11eeae079a60cef6
    cs_vi "Доброе утро, девочки."
    cs_vi "С чем пожаловали?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2e96b77d909b679a0db2
    cs_ls "Небольшое происшествие."
    cs_ls "Познакомилась в кружке электроники с острым краем шасси."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "И кто победил?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Судя по состоянию моего локтя, шасси."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Ну-ка, садись."
    cs_narrator "Она осмотрела руку, промыла царапину — я поморщилась — и наложила лёгкую повязку."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: e3101514018960d3f402
    cs_vi "Обычная царапина."
    cs_vi "Держи в чистоте."
    cs_vi "Если начнёт краснеть или дёргать — приходи."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я ей сразу сказала, что лучше зайти."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: f53831a4fef2d8d46ff6
    cs_vi "И правильно сказала."
    cs_vi "Вы ведь новенькие?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 30386defbb61c0c50af3
    cs_ls "Лена Соколова."
    cs_ls "А это Даша."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Дарья."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: c10f7c0768efdf4555e0
    cs_vi "Виола."
    cs_vi "Можно просто по имени."
    cs_narrator "Она посмотрела на нас чуть дольше, чем требовало знакомство."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: b07de7b55c236f609b31
    cs_vi "Новенькие в середине смены…"
    cs_vi "У меня в этом году с новенькими какое-то дежавю."
    cs_vi "Не обращайте внимания."
    cs_narrator "Я уже собиралась встать, когда взгляд зацепился за плакат на стене."
    # cs_page_anchor: 7292844bc2715fda44c2
    cs_narrator "Анатомическая иллюстрация."
    cs_narrator "Странная."
    cs_narrator "Маленькое существо с необычной формой головы и непропорциональным телом."
    cs_narrator "И я этот рисунок уже видела."
    cs_narrator "На форумах фанатов оригинальной новеллы его обсуждали годами."
    # cs_page_anchor: 1351c114c0bacfefcf41
    cs_narrator "Алёшенька."
    cs_narrator "Кыштымский карлик."
    cs_narrator "Девяносто шестой год."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Можно спросить, откуда у вас этот плакат?"
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: cc6923b7c462c63dac7a
    cs_vi "Честно?"
    cs_vi "Не знаю."
    cs_vi "Висел здесь ещё до меня."
    cs_vi "Не самое удачное пособие, если хочешь моё мнение."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 8e449f5ea1b4224d57f5
    cs_ls "Есть одно изображение, которое я помню по истории девяностых годов."
    cs_ls "Этот рисунок его очень напоминает."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Каких девяностых?"
    # cs_page_anchor: 10803d37690e7f7f8dc9
    cs_narrator "Не научилась."
    cs_narrator "Опять."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Тысяча девятьсот девяностых."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "До них ещё десять лет."
    # cs_page_anchor: 085d622d14f894abce8a
    cs_narrator "Дарья посмотрела на меня тем самым взглядом."
    cs_narrator "«Лен, только не начинай снова»."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9eb2a3760ef25fe0b746
    cs_ls "Но я могу ошибаться."
    cs_ls "Возможно, просто похожий рисунок."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Ты так говоришь, будто там была."
    $ cs_lena_elbow_bandaged = True
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Будем считать, что я много читаю фантастики."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Я бы не строила большую теорию по одному старому плакату."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Согласна."
    # cs_page_anchor: b93e6109ecbfc82fccd1
    cs_narrator "Плакат существует."
    cs_narrator "Похож на знакомый рисунок."
    cs_narrator "Это всё, что мы действительно знаем."
    cs_narrator "Ещё одна странность — и ещё один вопрос в список."
    cs_narrator "Виола убирала принадлежности и одной рукой придерживала коробку с запечатанными упаковками бинтов, другой пыталась открыть шкаф."
    if "2:3" in cs_rev_choices:
        if cs_rev_choices["2:3"]==0:
            $ cs_rev_choice(2,3,0)
            $ cs_helped_viola_day2 = True
            $ cs_rev_award("2:3:cs_friend_viola","cs_friend_viola",1)
            $ cs_viola_day2_awarded = True
            $ cs_helped_viola_day2 = True
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Виола, давай помогу."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: 8d24fa359de4b306052e
            cs_vi "Если не трудно."
            cs_vi "Только ничего не вскрывай, просто поставь пачки на верхнюю полку."
            $ cs_rev_room('cs_cg_lena_darya_help_viola_day')
            cs_narrator "Дарья придержала дверцу, я поставила упаковки на место."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Медицинское обеспечение лагеря успешно реорганизовано."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: d937051b7fd8840f5803
            cs_vi "Всего-то несколько пачек бинтов."
            cs_vi "Ты всегда так разговариваешь?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "К сожалению для окружающих, довольно часто."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Подтверждаю."
            $ cs_rev_room('bg int_aidpost_day')
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: 76de077a9d35f22ed378
            cs_vi "Ну что ж."
            cs_vi "Заходите, если понадобится помощь."
            cs_vi "Только без новых царапин."
            $ cs_rev_finish_choice(2,3)
        else:
            $ cs_rev_choice(2,3,1)
            $ cs_helped_viola_day2 = False
            $ cs_helped_viola_day2 = False
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 7831850fe856f71f0369
            cs_ls "Спасибо."
            cs_ls "И извини, что отвлекли."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: c74be2c33a18ba8e372b
            cs_vi "Это моя работа."
            cs_vi "Только в следующий раз будь осторожнее."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "До свидания."
            $ cs_rev_finish_choice(2,3)
    else:
        menu:
            "Предложить Виоле помощь с материалами":
                $ cs_rev_choice(2,3,0)
                $ cs_helped_viola_day2 = True
                $ cs_rev_award("2:3:cs_friend_viola","cs_friend_viola",1)
                $ cs_viola_day2_awarded = True
                $ cs_helped_viola_day2 = True
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Виола, давай помогу."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: 60aa03f171305441c623
                cs_vi "Если не трудно."
                cs_vi "Только ничего не вскрывай, просто поставь пачки на верхнюю полку."
                $ cs_rev_room('cs_cg_lena_darya_help_viola_day')
                cs_narrator "Дарья придержала дверцу, я поставила упаковки на место."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Медицинское обеспечение лагеря успешно реорганизовано."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: 936e2cb289b0ae1946b2
                cs_vi "Всего-то несколько пачек бинтов."
                cs_vi "Ты всегда так разговариваешь?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "К сожалению для окружающих, довольно часто."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Подтверждаю."
                $ cs_rev_room('bg int_aidpost_day')
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: 8d5c684b53892198a754
                cs_vi "Ну что ж."
                cs_vi "Заходите, если понадобится помощь."
                cs_vi "Только без новых царапин."
                $ cs_rev_finish_choice(2,3)
            "Поблагодарить Виолу и не задерживаться":
                $ cs_rev_choice(2,3,1)
                $ cs_helped_viola_day2 = False
                $ cs_helped_viola_day2 = False
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: e972f77fc60996b18026
                cs_ls "Спасибо."
                cs_ls "И извини, что отвлекли."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: d6cd968c72879dc90106
                cs_vi "Это моя работа."
                cs_vi "Только в следующий раз будь осторожнее."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "До свидания."
                $ cs_rev_finish_choice(2,3)
    $ cs_rev_room('bg ext_aidpost_day')
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.25)
    cs_narrator "На крыльце солнечный свет показался особенно ярким."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты правда думаешь, что тот рисунок связан с девяностыми?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Мне показалось, что узнала."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 89075ce3eb3fa4d754ef
    cs_da "А разве это не то же самое, что с людьми в лагере?"
    cs_da "Видишь что-то похожее на игру — и сразу думаешь, что знаешь, что это такое."
    cs_narrator "Опять она права."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Запишем как наблюдение, а не как доказательство."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Вот это разумнее."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ты ведь понимаешь, что постепенно становишься руководителем нашей исследовательской группы?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А ты кем будешь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Специалистом по подозрительным плакатам."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Очень узкая специальность."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Зато востребованная именно здесь."
    return

label cs_rev_d2_09:
    $ cs_rev_begin(2,9,['cs_darya', 'cs_semen', 'sl'])
    $ save_name = "Чужая смена — День 2: Без Ctrl+Z"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_clubs_day")
    $ cs_rev_music(cs_day_music_daily,0.16,2.5)
    # cs_page_anchor: 9c7202b834b68a362821
    cs_narrator "Семён уже ждал за столом."
    cs_narrator "Папка лежала перед ним, карандаши — рядом."
    cs_narrator "Художественное имущество пережило отсутствие руководства."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Всё нормально?"
    cs_narrator "Я показала повязку."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 46029f453fa1819c654e
    cs_ls "Медицинская помощь оказана."
    cs_ls "Пациентка допущена к общественно полезным работам."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Узнал время?"
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 85b96f7b19a5f2f7f122
    cs_sy "После ужина."
    cs_sy "Точное время Ольга Дмитриевна просила пока не писать."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "А в медпункте что-нибудь интересное было?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 32fbfc1395ad4873d341
    cs_ls "На стене висит рисунок, похожий на изображение из более поздней истории."
    cs_ls "Но я пока не уверена, что это одно и то же."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мы решили ничего не утверждать без проверки."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "По-моему, правильно."
    # cs_page_anchor: ef78656dc5be9ff1d4ea
    cs_narrator "Первую линию я провела уверенно."
    cs_narrator "Вторую — тоже."
    cs_narrator "А на третьей вспомнила, что у бумаги есть одно крайне неприятное свойство."
    cs_narrator "На ней нельзя нажать Ctrl+Z."
    cs_narrator "Художник двадцать первого века столкнулся с технологическими ограничениями двадцатого."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ластик рядом."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Благодарю, служба технической поддержки."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 25a33bf60d42d48b748f
    cs_da "Лена, нам нужно, чтобы люди прочитали, где и когда."
    cs_da "Это объявление, а не обложка альбома."
    $ cs_rev_room('cs_cg_poster_planning_day')
    # cs_page_anchor: 99977719288f932b8ea1
    cs_narrator "И ведь правда."
    cs_narrator "Дома у меня были бы кисти, шрифты, слои и возможность исправить практически всё."
    cs_narrator "Здесь — бумага, три карандаша, ластик."
    cs_narrator "И два человека, которые не понимали, почему я пятый раз переношу заголовок."
    # cs_page_anchor: 52627dc1dd4c73a90e24
    cs_narrator "Я сделала лёгкую разметку: сверху место под крупный заголовок, по краям ноты, слева гитара — Алиса ведь тоже будет выступать."
    cs_narrator "Внизу место для времени и места."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Председатель художественного совета кто?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 6c2e8a916115d44015c1
    cs_ls "Бумага."
    cs_ls "Она здесь главная пострадавшая сторона."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: b80ab3c63ceb6ab0dc22
    cs_da "Нам ещё нужен заголовок."
    cs_da "«Музыкальный вечер»."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Красивого почерка не обещаю."
    if "2:4" in cs_rev_choices:
        if cs_rev_choices["2:4"]==0:
            $ cs_rev_choice(2,4,0)
            $ cs_worked_with_se_day2 = True
            $ cs_rev_award("2:4:cs_friend_se","cs_friend_se",1)
            $ cs_se_day2_awarded = True
            $ cs_worked_with_se_day2 = True
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Давай вместе."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Ты мне доверяешь заголовок?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Настолько, что собираюсь лично участвовать."
            # cs_page_anchor: 4f6f13b8d18629a7ec31
            cs_narrator "Дарья поставила отметки для верхней и нижней границ букв."
            cs_narrator "На третьей букве Семён остановился."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Кажется, не помещается."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Если продолжишь так же, последнее слово придётся писать на обороте."
            cs_narrator "Мы стёрли разметку и уменьшили расстояние между буквами."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 9e6347924bcf68f54e74
            cs_sy "Слушай, ты правда много рисовала?"
            cs_sy "На планшете?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Угу."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Всегда хотел попробовать."
            # cs_page_anchor: aedfd95493765356f1d1
            cs_narrator "Ещё одна общая тема."
            cs_narrator "И совершенно не связанная с автобусом."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Вернёмся домой — попробуешь."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Думаешь?"
            # cs_page_anchor: c336abc07f95f5f35151
            cs_narrator "Карандаш замер над бумагой."
            cs_narrator "Самая обыкновенная фраза вдруг превратилась в напоминание."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Думаю, надо хотя бы попытаться."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Согласен."
            cs_narrator "На этот раз всё поместилось."
            $ cs_rev_finish_choice(2,4)
        else:
            $ cs_rev_choice(2,4,1)
            $ cs_worked_with_se_day2 = False
            $ cs_worked_with_se_day2 = False
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Ты займись заголовком, а я закончу гитару."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Только сначала наметь, где будут буквы."
            cs_narrator "Буквы у Семёна вышли немного неровными, но читались издалека."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Ну как?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 938de4db7fcb1d6372db
            cs_ls "Отлично."
            cs_ls "Мы же не в типографии."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Значит, справился."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Справились."
            $ cs_rev_finish_choice(2,4)
    else:
        menu:
            "Давай сделаем надпись вместе":
                $ cs_rev_choice(2,4,0)
                $ cs_worked_with_se_day2 = True
                $ cs_rev_award("2:4:cs_friend_se","cs_friend_se",1)
                $ cs_se_day2_awarded = True
                $ cs_worked_with_se_day2 = True
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Давай вместе."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Ты мне доверяешь заголовок?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Настолько, что собираюсь лично участвовать."
                # cs_page_anchor: a8504165eba738746648
                cs_narrator "Дарья поставила отметки для верхней и нижней границ букв."
                cs_narrator "На третьей букве Семён остановился."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Кажется, не помещается."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Если продолжишь так же, последнее слово придётся писать на обороте."
                cs_narrator "Мы стёрли разметку и уменьшили расстояние между буквами."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 6d9a96bb54fb54309427
                cs_sy "Слушай, ты правда много рисовала?"
                cs_sy "На планшете?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Угу."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Всегда хотел попробовать."
                # cs_page_anchor: 24d63fda74f88f9699bb
                cs_narrator "Ещё одна общая тема."
                cs_narrator "И совершенно не связанная с автобусом."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Вернёмся домой — попробуешь."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Думаешь?"
                # cs_page_anchor: 674f8d990c528dad6aa7
                cs_narrator "Карандаш замер над бумагой."
                cs_narrator "Самая обыкновенная фраза вдруг превратилась в напоминание."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Думаю, надо хотя бы попытаться."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Согласен."
                cs_narrator "На этот раз всё поместилось."
                $ cs_rev_finish_choice(2,4)
            "Я закончу рисунок, а ты займись буквами":
                $ cs_rev_choice(2,4,1)
                $ cs_worked_with_se_day2 = False
                $ cs_worked_with_se_day2 = False
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Ты займись заголовком, а я закончу гитару."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Только сначала наметь, где будут буквы."
                cs_narrator "Буквы у Семёна вышли немного неровными, но читались издалека."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Ну как?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: b585320a7207967f056f
                cs_ls "Отлично."
                cs_ls "Мы же не в типографии."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Значит, справился."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Справились."
                $ cs_rev_finish_choice(2,4)
    $ cs_rev_room('bg ext_clubs_day')
    # cs_page_anchor: 512cda31d2ddf578b535
    cs_narrator "Дарья вывела внизу аккуратными буквами: «Сегодня после ужина. На площади»."
    cs_narrator "Я добавила в угол маленькую звёздочку."
    cs_narrator "Посмотрела."
    cs_narrator "Подумала."
    cs_narrator "И отложила карандаш."
    # cs_page_anchor: 6cb79246c42476a4e8d9
    cs_narrator "Хватит."
    cs_narrator "Главное — вовремя остановиться."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: d28f9f45949f68c1208c
    cs_da "Заголовок видно."
    cs_da "Место и время тоже."
    cs_narrator "У доски объявлений Семён закрепил лист кнопками, отступил и посмотрел."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 52a66a1e34780d56e6be
    cs_ls "Левый угол чуть ниже."
    cs_ls "Нет."
    cs_ls "Показалось."
    cs_narrator "Он тяжело вздохнул."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 0c7dbbe980a5c8a21d1d
    cs_da "Не обращай внимания."
    cs_da "У неё профессиональная привычка искать недочёты."
    cs_narrator "Подошла Славя и прочитала объявление."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: 5990318c31699a00c33f
    cs_sl "Очень красиво."
    cs_sl "И всё понятно — это самое главное."
    if cs_helped_sl_day2:
        $ cs_rev_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: 47716708aef68300cac2
        cs_sl "И спасибо ещё раз за коробки."
        cs_sl "Я уже всё разобрала."
    $ cs_rev_room('cs_camp_path_day')
    # cs_page_anchor: 86e56c0faf79b6f03ff1
    cs_narrator "Семён со Славей понесли оставшиеся материалы в клубы."
    cs_narrator "Мы с Дарьей пошли по дорожке."
    # cs_page_anchor: 6175c67d054e0557d7b8
    cs_narrator "Первый официальный заказ в Советском Союзе выполнен."
    cs_narrator "Без оплаты, но на полном пансионе."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 69c764ca4731bea55c0c
    cs_da "Лен."
    cs_da "Тебе Виола понравилась?"
    cs_narrator "О. Интересный поворот."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Как медработник?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Как человек."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: e45545f0d26edc7e34de
    cs_ls "Да."
    cs_ls "Спокойная, внимательная."
    cs_ls "С чувством юмора."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И красивая?"
    # cs_page_anchor: 2e1f6e3732e15acf9087
    cs_narrator "Она смотрела на меня совершенно невинно."
    cs_narrator "Слишком невинно."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 581aa4701d1e44c70634
    cs_ls "Да, красивая."
    cs_ls "Но если это допрос, прошу предоставить адвоката."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Просто ты очень внимательно её рассматривала."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Профессиональная наблюдательность художника."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "В медицинском кабинете?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Особенно там."
    cs_narrator "Потом я перестала шутить."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c55a12a856bdcf13ceea
    cs_ls "Даш, если серьёзно — я ведь уже говорила, кто мне нравится."
    cs_ls "И ничего не изменилось."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я и не думала, что изменилось."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Тогда зачем спрашивала?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Хотела немного тебя подразнить."
    cs_narrator "Я подняла палец."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c2dc73be045f27f97b9f
    cs_ls "Так."
    cs_ls "Это злоупотребление моими собственными методами."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Учитель хороший."
    # cs_page_anchor: 10eb0dc9ce77c52a1448
    cs_narrator "И я рассмеялась."
    cs_narrator "Возразить было нечего."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "А ты не ревновала?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 5b607665ad5acf8e7f6b
    cs_da "К Виоле?"
    cs_da "Ты просто с ней разговаривала."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 7227c5ab614ce9b7ac15
    cs_ls "Я сама иногда немного ревную."
    cs_ls "Понимаю, что это моя проблема, а не твоя."
    cs_narrator "Дарья остановилась."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: b5578157393ea56fb1a7
    cs_da "Лен, мы ещё не решили, что между нами будет."
    cs_da "Мне правда приятно, что ты сказала о своих чувствах."
    cs_da "Но я не хочу, чтобы мы начали следить, кто с кем разговаривает."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 6f9d06e57853fc4c71d7
    cs_ls "И я не хочу."
    cs_ls "Прости."
    cs_ls "У меня совсем нет опыта в таких вещах."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я заметила."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Как жестоко."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 7cad9d1c1b19e8a3abdd
    cs_da "Зато честно."
    cs_da "Мне нравится, что ты говоришь прямо."
    cs_da "Даже если иногда сначала говоришь, а потом думаешь."
    $ cs_rev_music(cs_day_music_home,0.14,3.0)
    # cs_page_anchor: 04dd31a977f0ee43958e
    cs_narrator "Вчера я боялась вслух сказать, что она мне нравится."
    cs_narrator "Сегодня мы смеёмся над моей неопытностью."
    cs_narrator "Пожалуй, это тоже прогресс."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 70279ba23aeabac9ef2c
    cs_ls "Даш."
    cs_ls "Я всё ещё хочу домой."
    cs_ls "И не собираюсь делать вид, будто это просто длинные каникулы."
    cs_ls "Но пока мы здесь — можно иногда позволять себе обычные вещи."
    cs_ls "Рисовать."
    cs_ls "Слушать музыку."
    cs_ls "Разговаривать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мне нравится этот план."
    $ cs_rev_room('cs_cg_lena_darya_hand_in_hand_day')
    # cs_page_anchor: 52c2e7f6f1ffff67f3e1
    cs_narrator "Она чуть повернула ладонь в мою сторону."
    cs_narrator "Не торжественно."
    cs_narrator "Просто навстречу."
    cs_narrator "Я взяла её руку, и несколько шагов мы прошли так."
    return

label cs_rev_d2_10:
    $ cs_rev_begin(2,10,['cs_darya', 'cs_semen'])
    $ save_name = "Чужая смена — День 2: План"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_dining_hall_people_day")
    $ cs_rev_music(cs_day_music_think,0.14,2.5)
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "После обеда куда?"
    # cs_page_anchor: b163ba7951a152ae795b
    cs_narrator "Я хотела сказать: никуда."
    cs_narrator "Но вспомнила пустую стоянку."
    cs_narrator "След, который обрывается посреди асфальта."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "У тебя третье выражение лица."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Какое ещё третье?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: ea30c215c9eb18b5ad82
    cs_da "Первое — когда шутишь."
    cs_da "Второе — когда собираешься пошутить."
    cs_da "Третье — когда придумала что-то сомнительное."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f0bb3ae89561cb9caa5c
    cs_ls "Хочу посмотреть, что за воротами."
    cs_ls "Не уходить в лес."
    cs_ls "Просто пройти по дороге и понять, есть ли там перекрёсток, указатель, дома."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 5e587d7e371cb1f0dc17
    cs_da "Только втроём, как договаривались."
    cs_da "С дороги не сходим."
    cs_da "Берём воду."
    cs_da "И заранее решаем, когда поворачиваем назад."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Тебе определённо нужно руководить экспедицией."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Потому что я вспомнила про воду?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Для нашей группы это выдающийся уровень организации."
    # cs_page_anchor: f0e5d4c34d4fc7a527a1
    cs_narrator "Подсел Семён с подносом."
    cs_narrator "Услышал про ворота и сразу стал серьёзным."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 895b5a772892cb85a181
    cs_sy "Наконец-то."
    cs_sy "Только далеко не надо."
    cs_sy "А если ничего не найдём?"
    # cs_page_anchor: e80a9081a06af044a610
    cs_narrator "Перед глазами снова встали ворота."
    cs_narrator "И зимняя московская остановка."
    cs_narrator "Ещё два дня назад всё было понятно."
    cs_narrator "А теперь я сидела в советской столовой и обсуждала, существует ли вообще дорога из пионерлагеря во внешний мир."
    # cs_page_anchor: 6ecb1bb2b0c5bb6eb30d
    cs_narrator "Можно было ограничиться планом."
    cs_narrator "А можно было сказать, чего я на самом деле боюсь."
    if "2:5" in cs_rev_choices:
        if cs_rev_choices["2:5"]==0:
            $ cs_rev_choice(2,5,0)
            $ cs_trusted_se_road_day2 = True
            $ cs_rev_award("2:5:cs_friend_se","cs_friend_se",1)
            $ cs_se_road_day2_awarded = True
            $ cs_trusted_se_road_day2 = True
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 1dc1709051f5ec819c85
            cs_ls "Если ничего не найдём — вернёмся."
            cs_ls "Меня пугает не это."
            cs_ls "Меня пугает, что за воротами может вообще ничего не оказаться."
            cs_ls "Не пустая дорога, а дорога, по которой сколько ни иди — никуда не придёшь."
            cs_narrator "Семён перестал улыбаться."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 9683726201e13476f833
            cs_ls "Вчера я убеждала себя, что где-то есть город, станция, железная дорога."
            cs_ls "Надо только дойти."
            cs_ls "А сегодня автобус исчез, и я впервые подумала: вдруг у этого места нет нормального выхода?"
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: b5cc64ae70ec0c6d7bbe
            cs_sy "Я тоже об этом думал."
            cs_sy "В первый день всё вспоминал, куда ехал, как уснул."
            cs_sy "Чем больше вспоминал, тем меньше понимал."
            cs_sy "Наверное, поэтому так обрадовался, когда вчера появились вы."
            cs_sy "До этого мне не с кем было нормально поговорить."
            # cs_page_anchor: 5da0f7090aa26bb7df12
            cs_narrator "Он провёл здесь целый день один."
            cs_narrator "Среди людей, которые не понимали, почему он так удивлён."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Тогда хорошо, что мы встретились."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 934838ddf101b0719d63
            cs_sy "Да."
            cs_sy "Хорошо."
            $ cs_rev_focus("da")
            with cs_sprite_change
            # cs_page_anchor: 12ec7cc273cf7888677e
            cs_da "Поэтому поодиночке ничего не делаем."
            cs_da "Что бы там ни было."
            $ cs_rev_finish_choice(2,5)
        else:
            $ cs_rev_choice(2,5,1)
            $ cs_trusted_se_road_day2 = False
            $ cs_trusted_se_road_day2 = False
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 62bff453f7ded5629f10
            cs_ls "Идём втроём, остаёмся на асфальте, отмечаем ориентиры."
            cs_ls "Ничего не найдём за разумное время — возвращаемся."
            $ cs_rev_focus("da")
            with cs_sprite_change
            # cs_page_anchor: a8343057175776bb8729
            cs_da "Пятнадцать минут в одну сторону."
            cs_da "Потом решаем."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "А если дорога начнёт петлять?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: ffe3b86c3a4d98a9d583
            cs_ls "Тогда хотя бы будем знать, что петляет."
            cs_ls "И не полезем через лес напрямик."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Главное — не потеряться, пока ищем выход."
            $ cs_rev_finish_choice(2,5)
    else:
        menu:
            "Сказать Семёну, что меня действительно тревожит":
                $ cs_rev_choice(2,5,0)
                $ cs_trusted_se_road_day2 = True
                $ cs_rev_award("2:5:cs_friend_se","cs_friend_se",1)
                $ cs_se_road_day2_awarded = True
                $ cs_trusted_se_road_day2 = True
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: c81c28dd05258cf103fd
                cs_ls "Если ничего не найдём — вернёмся."
                cs_ls "Меня пугает не это."
                cs_ls "Меня пугает, что за воротами может вообще ничего не оказаться."
                cs_ls "Не пустая дорога, а дорога, по которой сколько ни иди — никуда не придёшь."
                cs_narrator "Семён перестал улыбаться."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 976a1acfae60e5b0bc60
                cs_ls "Вчера я убеждала себя, что где-то есть город, станция, железная дорога."
                cs_ls "Надо только дойти."
                cs_ls "А сегодня автобус исчез, и я впервые подумала: вдруг у этого места нет нормального выхода?"
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 314aabff98b2c488f2e9
                cs_sy "Я тоже об этом думал."
                cs_sy "В первый день всё вспоминал, куда ехал, как уснул."
                cs_sy "Чем больше вспоминал, тем меньше понимал."
                cs_sy "Наверное, поэтому так обрадовался, когда вчера появились вы."
                cs_sy "До этого мне не с кем было нормально поговорить."
                # cs_page_anchor: 23c4077ab9a3d43ea8fe
                cs_narrator "Он провёл здесь целый день один."
                cs_narrator "Среди людей, которые не понимали, почему он так удивлён."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Тогда хорошо, что мы встретились."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 7bc013b7850f40d64564
                cs_sy "Да."
                cs_sy "Хорошо."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: 9d29b0f823aeaf32a390
                cs_da "Поэтому поодиночке ничего не делаем."
                cs_da "Что бы там ни было."
                $ cs_rev_finish_choice(2,5)
            "Ограничиться планом проверки дороги":
                $ cs_rev_choice(2,5,1)
                $ cs_trusted_se_road_day2 = False
                $ cs_trusted_se_road_day2 = False
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 4443c86a99de1011d2ee
                cs_ls "Идём втроём, остаёмся на асфальте, отмечаем ориентиры."
                cs_ls "Ничего не найдём за разумное время — возвращаемся."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: 8419b8acb7d112254c9d
                cs_da "Пятнадцать минут в одну сторону."
                cs_da "Потом решаем."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "А если дорога начнёт петлять?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 8608b5540451af4054e0
                cs_ls "Тогда хотя бы будем знать, что петляет."
                cs_ls "И не полезем через лес напрямик."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Главное — не потеряться, пока ищем выход."
                $ cs_rev_finish_choice(2,5)
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Техническое задание утверждено."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Осталось выполнить."
    return

label cs_rev_d2_11:
    $ cs_rev_begin(2,11,['cs_darya', 'cs_semen'])
    $ save_name = "Чужая смена — День 2: Куст с резинкой"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_camp_entrance_day")
    $ renpy.music.set_volume(0.08, channel="music", delay=2.0)
    # cs_page_anchor: 553cbb5ca9fc1588fec4
    cs_narrator "У ворот Семён уже ждал с флягой."
    cs_narrator "Я проверила карманы: сложенный лист с заметками, карандаш, резинка для волос."
    cs_narrator "И телефон — не знаю зачем."
    cs_narrator "Наверное, привычка."
    # cs_page_anchor: 74e51bd783b9302df261
    cs_narrator "Мы прошли под вывеской «Совёнок»."
    cs_narrator "Я остановилась сразу за воротами и оглянулась."
    cs_narrator "Ворота стояли на месте."
    cs_narrator "Никакой вспышки, никакого звука."
    cs_narrator "Лагерь никуда не делся."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты опять что-то проверяешь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 245f749cf70af6815bcc
    cs_ls "Факт нашего физического существования за воротами."
    cs_ls "Пока положительный."
    $ cs_rev_room('cs_road_powerlines_day')
    # cs_page_anchor: ee356afa38244f511be3
    cs_narrator "Сначала всё было нормально."
    cs_narrator "Трава по обочинам, сосны, птицы, солнечные пятна на асфальте."
    cs_narrator "Так нормально, что даже обидно."
    cs_narrator "Я почти ждала таблички «За пределами сюжетной области проход запрещён»."
    cs_narrator "Минут через десять я остановилась у куста на правой обочине и привязала к ветке резинку — яркую, хорошо заметную среди зелени."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "И что это докажет?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b0f6509a32890bbf533b
    cs_ls "Пока ничего."
    cs_ls "Но если мы почему-нибудь снова увидим этот куст, мы его узнаем."
    cs_narrator "Дарья палочкой начертила в пыли у края асфальта стрелку — в сторону от лагеря."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 02dcfd24865ec0935f5a
    cs_da "Семён, засеки время."
    cs_da "Чтобы потом не спорить."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 6b11fbe39068b421f075
    cs_sy "Засёк."
    cs_sy "Куст с резинкой справа, стрелка от лагеря."
    # cs_page_anchor: 3b82573c072a884f46d0
    cs_narrator "Мы пошли дальше."
    cs_narrator "Сосна, ещё сосна, куст, камень."
    cs_narrator "Пейзажный художник явно сэкономил на разнообразии."
    $ cs_rev_room('cs_road_right_bend_day')
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Почти пятнадцать минут."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Подождите."
    stop music fadeout 2.0
    # cs_page_anchor: 4d58f6f6aab2d8cc5e4e
    cs_narrator "Она смотрела вперёд."
    cs_narrator "На правую обочину."
    cs_narrator "На куст, который выделялся среди остальных маленьким ярким пятном."
    $ cs_road_loop_observations = 1
    # cs_page_anchor: 65d5a45fb899ed704515
    cs_narrator "На ветке висела моя резинка."
    cs_narrator "Та самая — я узнала цвет и узел."
    cs_narrator "А в пыли у края асфальта лежала стрелка."
    cs_narrator "Она по-прежнему указывала вперёд."
    cs_narrator "Туда, куда мы шли."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: fee7a304797a6eaf6025
    cs_sy "Подожди."
    cs_sy "Мы же здесь уже были."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мы ни разу не сворачивали."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Либо мы прошли круг, либо наши наблюдения гораздо менее надёжны, чем хотелось бы."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Надо исключить, что это просто похожий куст."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "С моей резинкой?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 42a38de03a85cc765c48
    cs_da "Ты права."
    cs_da "Но всё равно перепроверим."
    # cs_page_anchor: d1f054d77fb7081c5f6d
    cs_narrator "Сейчас мне очень хотелось объявить об открытии новой геометрии."
    cs_narrator "Возможно, это худший момент для поспешных выводов."
    $ cs_rev_room('cs_road_marked_verge_day')
    # cs_page_anchor: 7fd559630b3a02ae470a
    cs_narrator "Договорились заранее: с асфальта не сходим, Семён следит за временем, Дарья — за обочиной, я — за всем странным."
    cs_narrator "Дарья поставила рядом со своей стрелкой вторую короткую черту."
    # cs_page_anchor: e4d5d9d21ee9e86e7bec
    cs_narrator "Мы снова пошли вперёд."
    cs_narrator "Дорога слегка изгибалась влево."
    cs_narrator "Потом длинный прямой отрезок."
    cs_narrator "Неровность асфальта."
    cs_narrator "Я старалась не смотреть на каждый куст так, будто он собирался переместиться."
    cs_narrator "Получалось плохо."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Лена."
    $ cs_road_loop_observations = 2
    # cs_page_anchor: 94d60d93ec971a11e2a9
    cs_narrator "Яркая резинка."
    cs_narrator "Тот же куст."
    cs_narrator "И у края дороги — отметки."
    # cs_page_anchor: f790c731c08a70e70385
    cs_narrator "Я присела."
    cs_narrator "Стрелка."
    cs_narrator "Вторая черта Дарьи."
    $ cs_rev_room('cs_road_left_bend_day')
    # cs_page_anchor: 38d9c19dc59ee5ff1013
    cs_narrator "И третья."
    cs_narrator "Короткая, чуть наискось."
    cs_narrator "Её не рисовал никто из нас."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: be091bd1598d0cfc3975
    cs_ls "Даш."
    cs_ls "Это ты?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 14f8727aaa50aa927175
    cs_da "Нет."
    cs_da "Я провела одну."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 054dcca3b15929dc4f46
    cs_sy "Может, ветка упала?"
    cs_sy "Или птица."
    # cs_page_anchor: 3cd323b0d9538df9c5a8
    cs_narrator "Может быть."
    cs_narrator "Черта была слишком ровной для ветки."
    cs_narrator "И слишком свежей, чтобы появиться раньше нас."
    $ cs_rev_room('cs_road_marked_verge_day')
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 77cf0eb9c749ff64d633
    cs_sy "Мы опять пришли сюда."
    cs_sy "Значит, дорога идёт кругом?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "По ощущениям мы полного круга не сделали."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А если пойти обратно?"
    $ cs_rev_room('cs_road_powerlines_day')
    $ cs_road_loop_observations = max(2,cs_road_loop_observations)
    # cs_page_anchor: 2910026b44b1fa76766a
    cs_narrator "Мы развернулись."
    cs_narrator "Я следила за дорогой почти болезненно внимательно."
    cs_narrator "Снова деревья."
    cs_narrator "Снова асфальт."
    cs_narrator "Но времени прошло заметно меньше."
    cs_narrator "Небольшой изгиб, впереди посветлело — и между деревьями показалась вывеска «СОВЁНОК»."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Назад — быстрее, чем вперёд."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: a5fb70f62fd10890fa3d
    cs_sy "Минут пять."
    cs_sy "Не больше."
    # cs_page_anchor: 3229e5ed60bc468d220c
    cs_narrator "Получается, уйти можно."
    cs_narrator "На какое-то расстояние."
    cs_narrator "А вот куда ведёт дорога, мы так и не узнали."
    return

label cs_rev_d2_12:
    $ cs_rev_begin(2,12,['cs_darya', 'cs_semen', 'mt'])
    $ save_name = "Чужая смена — День 2: У ворот"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_camp_entrance_day")
    # cs_page_anchor: 3869ce3d2910475e64c9
    cs_narrator "До ворот оставалось метров двадцать."
    cs_narrator "Я обернулась на дорогу — проверить, не появится ли куст и там, позади, — и перестала смотреть под ноги."
    # cs_page_anchor: 7f0f96aa005fe0ce207d
    cs_narrator "Край асфальта был выщерблен."
    cs_narrator "Носок туфли зацепился за выбоину."
    $ cs_rev_sfx('sound/sfx/bodyfall_1.ogg',0.55)
    # cs_page_anchor: 43c112e042b83517fee9
    cs_narrator "Я выставила руку."
    cs_narrator "Ладонь проехалась по асфальту, колено ударилось следом."
    cs_narrator "И утренний локоть — тот самый, с повязкой, — со всего размаху скользнул по шершавому покрытию."
    # cs_page_anchor: 60a903518395c4a4e761
    cs_narrator "Боль пришла не сразу."
    cs_narrator "Сначала было только недоумение."
    $ cs_lena_elbow_injury_day2 = 2
    # cs_page_anchor: 16c0d2bfdde71bd9bf35
    cs_narrator "Так."
    cs_narrator "А это сейчас что было?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ай…"
    # cs_page_anchor: 6b5d1c001e383d83bf49
    cs_narrator "Повязка Виолы сбилась и почернела от пыли."
    cs_narrator "Рядом с утренней царапиной — широкая ссадина, и по коже стекала кровь."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Лена!"
    cs_narrator "Она уже сидела рядом."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Головой ударилась?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: facaf874bf6e72506b68
    cs_ls "Нет."
    cs_ls "Успела выставить руки."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: c424565d3374c81c1de4
    cs_da "Кружится?"
    cs_da "Тошнит?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b5b52281061c54c11bdb
    cs_ls "Даш, всё нормально."
    cs_ls "Просто локоть болит."
    cs_narrator "Я помолчала."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Сильно."
    # cs_page_anchor: c3f72176577ec6f6440f
    cs_narrator "Я потянулась к ссадине другой рукой."
    cs_narrator "Дарья мягко её остановила."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Не трогай грязными пальцами."
    cs_narrator "Она достала чистый платок и помогла прижать его к ссадине, не сдирая грязную повязку."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Пальцами пошевелить можешь?"
    cs_narrator "Могу."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ты сейчас очень серьёзная."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Потому что ты упала и у тебя кровь на руке."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: d1cb08eb029eefdd8f5c
    cs_sy "Давай, вставай."
    cs_sy "Медленно."
    # cs_page_anchor: 09a97a24005369d10015
    cs_narrator "Они подняли меня вдвоём."
    cs_narrator "Колено отозвалось, но стоять я могла."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 4e4007a7166e160a2953
    cs_mt "Лена!"
    cs_mt "Семён!"
    cs_mt "Дарья!"
    # cs_page_anchor: 394cedb94f3763b689ae
    cs_narrator "Ну конечно."
    cs_narrator "Кто ещё мог появиться именно сейчас."
    # cs_page_anchor: 62680d3c2925d790bb5d
    cs_narrator "Ольга Дмитриевна шла по дорожке быстрым шагом."
    cs_narrator "Увидела платок, кровь — и шаг стал ещё быстрее."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Что случилось?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 42370f147340136f81a8
    cs_ls "Споткнулась."
    cs_ls "О собственную невнимательность."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Где вы были?"
    cs_narrator "Выдумывать объяснение не было смысла."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 98e1fea06612bd8a449a
    cs_ls "За воротами."
    cs_ls "Проверяли дорогу."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: c23d572d63d3aa395f08
    cs_mt "Без разрешения."
    cs_mt "Здесь летний лагерь, а не туристическая база."
    cs_mt "Если уходите — хотя бы предупреждайте."
    cs_mt "Я должна знать, где вы."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Мы были вместе и с дороги не сходили."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 7ca37900a7acd88c2a4c
    cs_da "Вы правы."
    cs_da "Нужно было предупредить."
    # cs_page_anchor: fcbe10d95e46d8218377
    cs_narrator "Она права."
    cs_narrator "Если бы случилось что-то ещё более странное, искать нас было бы неизвестно где."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d63491789d73c8eeeb5c
    cs_ls "Извините."
    cs_ls "В следующий раз предупредим."
    cs_ls "Можно спросить?"
    cs_ls "Куда ведёт эта дорога?"
    cs_narrator "Ольга Дмитриевна ответила не сразу."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Из лагеря."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 89d92535c0c504375c05
    cs_ls "В этом мы уже убедились."
    cs_ls "А дальше?"
    cs_ls "Мы дважды вернулись к одной отметке, хотя ни разу не разворачивались."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: f34e01d71abe4acd1b52
    cs_da "Резинка на кусте и стрелка на земле."
    cs_da "Мы шли вперёд, а они снова оказались перед нами."
    # cs_page_anchor: a4c514453ec80d572fa5
    cs_narrator "Взгляд Ольги Дмитриевны изменился на секунду."
    cs_narrator "Удивление?"
    cs_narrator "Раздражение?"
    cs_narrator "Усталость от трёх новеньких, которые второй день ведут себя непонятно?"
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Возможно, вы ошиблись с направлением."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "А вы сами когда-нибудь уходили по ней из лагеря?"
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 0f927bf3c776344bc364
    cs_mt "Лена, сейчас не время для загадок."
    cs_mt "Сейчас время для медпункта."
    cs_mt "Дарья, отведи её к Виоле."
    cs_mt "Семён — со мной, поможешь со скамейками."
    cs_mt "И больше за территорию без предупреждения — ни шагу."
    # cs_page_anchor: 19bfe21d2228dec1b6c9
    cs_narrator "Она увела Семёна к площади."
    cs_narrator "Я посмотрела ей вслед."
    # cs_page_anchor: 02116692251f9cb65484
    cs_narrator "Почему она не назвала ни одного места, куда ведёт дорога?"
    cs_narrator "Не знает?"
    cs_narrator "Не хочет говорить?"
    cs_narrator "Или я опять ищу тайну там, где её нет?"
    return

label cs_rev_d2_13:
    $ cs_rev_begin(2,13,['cs', 'cs_darya'])
    $ save_name = "Чужая смена — День 2: Постоянная посетительница"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_aidpost_day")
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Входите!"
    # cs_page_anchor: e129f921fc0201f90b0a
    cs_narrator "Она посмотрела на Дарью, потом на меня, потом на платок у моего локтя."
    cs_narrator "И медленно отложила ручку."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Лена?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d1925d786ddbfad806e4
    cs_ls "Добрый день."
    cs_ls "У вас есть программа лояльности для постоянных посетителей?"
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Это тот самый локоть, который я сегодня уже обрабатывала?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Он решил продолжить знакомство с окружающей средой."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Садись на кушетку."
    # cs_page_anchor: 6d7e8fae9c7f2d8626cd
    cs_narrator "Она сняла грязную повязку."
    cs_narrator "Я отвела взгляд."
    cs_narrator "Смотреть было совсем неинтересно."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 802ccdf149ad4e9498c9
    cs_vi "Как упала?"
    cs_vi "Головой не ударялась?"
    cs_vi "Сознание не теряла?"
    cs_vi "Не тошнит?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1ff1e2962dadffe13569
    cs_ls "Зацепилась за выбоину у ворот."
    cs_ls "Нет."
    cs_ls "Нет."
    cs_ls "Нет."
    cs_ls "Только локоть и колено."
    cs_narrator "Виола проверила, как двигаются кисть и пальцы."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 8a90544c3b166b7bc616
    cs_vi "Ссадина обширная."
    cs_vi "Грязи туда попало прилично, так что обрабатывать будем как следует."
    cs_vi "Приятного не обещаю."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: c91afefc59d61c23d0ab
    cs_vi "Молодец, что привела."
    cs_vi "И что не стала сама ковыряться."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я просто не хотела сделать хуже."
    if cs_met_mz:
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 52ebeaec9e1b95c719df
        cs_ls "Женя, Славя, теперь Виола."
        cs_ls "У Даши стремительно растёт профессиональная репутация."
    else:
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: e3b9c2469a9e83dfcff0
        cs_ls "Славя, теперь Виола."
        cs_ls "У Даши стремительно растёт профессиональная репутация."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: fdcc68255deb944761a5
    cs_da "Лен."
    cs_da "Сейчас не время."
    $ cs_lena_elbow_bandaged = True
    $ cs_lena_no_sport_day2 = True
    cs_narrator "Кажется, действительно не время."
    cs_narrator "Виола начала промывать ссадину."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ай!"
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: f27a20c86e4963b867f3
    cs_vi "Знаю."
    cs_vi "Потерпи."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: aa231334dabb0730fc6a
    cs_da "Лен."
    cs_da "Держи."
    # cs_page_anchor: 68d71bd9f8ea2b3e58a8
    cs_narrator "Дарья протянула мне руку."
    cs_narrator "Я взялась за неё."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Смотри на меня."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Звучит как начало психологического эксперимента."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты же любишь эксперименты."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Только те, в которых не участвует мой локоть."
    # cs_page_anchor: 4a7154b13b6a86ac30af
    cs_narrator "Постепенно жжение стало терпимым."
    cs_narrator "Я всё ещё держала её за руку."
    cs_narrator "Вчера я бы придумала этому какое-нибудь объяснение."
    cs_narrator "Про психологическую стабилизацию или тактильное обезболивание."
    cs_narrator "А сейчас мне просто было спокойнее."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 5446e65cab60e4ba539e
    cs_vi "Всё."
    cs_vi "Сегодня никаких пробежек, турников и прочих подвигов."
    cs_vi "Повязку не трогай."
    cs_vi "Усилится боль, появится отёк — сразу ко мне."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "То есть спортивная карьера приостановлена?"
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "На сегодня — определённо."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 16b52ad3797e824b1643
    cs_ls "А если серьёзно… спасибо."
    cs_ls "За то, что второй раз со мной возишься."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Для этого я здесь и работаю."
    if "2:6" in cs_rev_choices:
        if cs_rev_choices["2:6"]==0:
            $ cs_rev_choice(2,6,0)
            $ cs_talked_viola_second_day2 = True
            $ cs_rev_award("2:6:cs_friend_viola","cs_friend_viola",1)
            $ cs_viola_second_day2_awarded = True
            $ cs_talked_viola_second_day2 = True
            cs_narrator "На столе у Виолы лежала стопка журналов и заполненных карточек."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "У тебя всегда столько работы?"
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: ccd34a09f00128b4b769
            cs_vi "Когда как."
            cs_vi "Иногда никого."
            cs_vi "Иногда один за другим: ушибы, ссадины, животы."
            cs_vi "Сегодня, например, одна девушка уже успела навестить меня дважды."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Не будем называть имён."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: 7391d4de73d8c09ade2f
            cs_vi "Хорошо, что приходят."
            cs_vi "Хуже, когда терпят до последнего."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 6f46d4b9536289007e3b
            cs_ls "Ты ведь не только травмы лечишь."
            cs_ls "Здесь кто-то всегда скучает по дому или переживает."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: 236cbc719ac8e605e08c
            cs_vi "Бывает."
            cs_vi "Иногда человеку нужна не таблетка, а чтобы его просто выслушали."
            # cs_page_anchor: 0c1d5b1038df7f8d306f
            cs_narrator "Почему-то её слова запомнились."
            cs_narrator "Я всё время ищу в людях что-нибудь необычное."
            cs_narrator "А у Виолы каждый день — десятки обыкновенных человеческих неприятностей."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: b2db97b67805d40d0411
            cs_vi "Ладно, идите."
            cs_vi "И береги руку."
            $ cs_rev_finish_choice(2,6)
        else:
            $ cs_rev_choice(2,6,1)
            $ cs_talked_viola_second_day2 = False
            $ cs_talked_viola_second_day2 = False
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 84ea14e46d93502174b5
            cs_ls "Не будем тебя задерживать."
            cs_ls "Спасибо ещё раз."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            cs_vi "Только с повязкой аккуратнее."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Мы проследим."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Мне только что назначили персонального инспектора по технике безопасности."
            $ cs_rev_finish_choice(2,6)
    else:
        menu:
            "Немного поговорить с Виолой перед уходом":
                $ cs_rev_choice(2,6,0)
                $ cs_talked_viola_second_day2 = True
                $ cs_rev_award("2:6:cs_friend_viola","cs_friend_viola",1)
                $ cs_viola_second_day2_awarded = True
                $ cs_talked_viola_second_day2 = True
                cs_narrator "На столе у Виолы лежала стопка журналов и заполненных карточек."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "У тебя всегда столько работы?"
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: d0c9da57b5492de57079
                cs_vi "Когда как."
                cs_vi "Иногда никого."
                cs_vi "Иногда один за другим: ушибы, ссадины, животы."
                cs_vi "Сегодня, например, одна девушка уже успела навестить меня дважды."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Не будем называть имён."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: d402c1e7d9d76cd2174a
                cs_vi "Хорошо, что приходят."
                cs_vi "Хуже, когда терпят до последнего."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: cf23265fb80a017cbec0
                cs_ls "Ты ведь не только травмы лечишь."
                cs_ls "Здесь кто-то всегда скучает по дому или переживает."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: 3c2a02574b7fddcc9312
                cs_vi "Бывает."
                cs_vi "Иногда человеку нужна не таблетка, а чтобы его просто выслушали."
                # cs_page_anchor: d7e9bfd44fd4be1a7ab6
                cs_narrator "Почему-то её слова запомнились."
                cs_narrator "Я всё время ищу в людях что-нибудь необычное."
                cs_narrator "А у Виолы каждый день — десятки обыкновенных человеческих неприятностей."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: 55dc6f907636f917e01b
                cs_vi "Ладно, идите."
                cs_vi "И береги руку."
                $ cs_rev_finish_choice(2,6)
            "Поблагодарить Виолу и дать ей вернуться к работе":
                $ cs_rev_choice(2,6,1)
                $ cs_talked_viola_second_day2 = False
                $ cs_talked_viola_second_day2 = False
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 682bb7548b9908f34ba9
                cs_ls "Не будем тебя задерживать."
                cs_ls "Спасибо ещё раз."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                cs_vi "Только с повязкой аккуратнее."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Мы проследим."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Мне только что назначили персонального инспектора по технике безопасности."
                $ cs_rev_finish_choice(2,6)
    $ cs_rev_room('bg ext_aidpost_day')
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.25)
    # cs_page_anchor: 10f00a631716502139ae
    cs_narrator "На улице всё было по-прежнему."
    cs_narrator "Солнце."
    cs_narrator "Деревья."
    cs_narrator "Ни одного признака того, что полчаса назад я сидела на асфальте и пыталась понять, насколько сильно повредила руку."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 006f9e79ddf293a9ea03
    cs_ls "Даш."
    cs_ls "Ты сильно испугалась?"
    cs_narrator "Она не ответила сразу."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: b0f39ae756eb64dc6fee
    cs_da "Да."
    cs_da "Сначала я даже не поняла, что случилось."
    cs_da "Услышала удар — а ты уже лежишь."
    cs_da "Потом увидела кровь."
    cs_da "И не знала, насколько сильно ты ударилась."
    cs_narrator "Она посмотрела на меня."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А ты сразу начала шутить."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Привычка."
    cs_narrator "Я остановилась."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1a1947b4b624178bd872
    cs_ls "Прости."
    cs_ls "Когда мне больно или страшно, я начинаю говорить ерунду."
    cs_ls "Так проще не думать о том, что происходит."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: ab1f66c3fcd869832f1b
    cs_da "Я не против твоих шуток."
    cs_da "Мне просто нужно знать, когда тебе действительно плохо."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: bc4e5d2f38a5ce382fef
    cs_ls "Хорошо."
    cs_ls "Договорились."
    $ cs_rev_room('bg ext_aidpost_day')
    # cs_page_anchor: f6385d6ed4ad77e18113
    cs_narrator "В Москве я часами сидела за компьютером, рисовала, отвечала на сообщения людей, которых никогда не видела."
    cs_narrator "И мне всегда было сложно сказать кому-нибудь, что мне страшно."
    cs_narrator "Или больно."
    cs_narrator "Наверное, потому что после таких слов нельзя закрыть вкладку."
    # cs_page_anchor: d9ee02b149dda5e0c3d3
    cs_narrator "А Дарья не исчезала, когда я говорила что-то неловкое."
    cs_narrator "Не требовала стать веселее."
    cs_narrator "Просто оставалась рядом."
    cs_narrator "У развилки она протянула мне руку."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Это распоряжение?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Рекомендация."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Медицинская?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "После сегодняшнего — вполне."
    # cs_page_anchor: fb36808104d97e77d866
    cs_narrator "Я взяла её за руку."
    cs_narrator "Пионеры переносили скамейки к площади."
    cs_narrator "Лагерь жил своей жизнью."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b3bb4e2311701a18c4f1
    cs_ls "Сегодня без новых спортивных достижений."
    cs_ls "И без пространственных аномалий."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ещё лучше."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "А музыкальный вечер разрешается?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Думаю, да."
    return

label cs_rev_d2_14:
    $ cs_rev_begin(2,14,['cs_darya', 'cs_semen', 'cs_zhenya'])
    $ save_name = "Чужая смена — День 2: Угадай кто"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_square_day")
    # cs_page_anchor: 45be68ba348eddfbf1e6
    cs_narrator "Наше объявление висело на доске."
    cs_narrator "«МУЗЫКАЛЬНЫЙ ВЕЧЕР», гитара, ноты, звёздочка в углу."
    cs_narrator "Дома я бы ещё сорок минут двигала заголовок на два пикселя вправо и обратно."
    cs_narrator "Здесь такой возможности не было, и это почему-то совсем не мешало радоваться результату."
    # cs_page_anchor: a8b3834ee11c57a20cd1
    cs_narrator "Семён сидел на лавочке у памятника спиной к нам и вертел в пальцах карандаш."
    cs_narrator "Скамейки он, видимо, уже перетаскал."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: eaaf064e8af70b7bae84
    cs_da "Лена."
    cs_da "Я знаю это выражение лица."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Неужели?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты собираешься сделать что-то совершенно необязательное."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Но потенциально очень весёлое."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Только осторожнее с рукой."
    $ cs_rev_room('cs_cg_lena_semen_guess_who_day')
    cs_narrator "Я подошла сзади, прикрыла ему глаза здоровой ладонью и самым низким голосом, на какой была способна, произнесла:"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Угадай кто."
    # cs_page_anchor: a03eec06c467ac20e671
    cs_narrator "Семён замер."
    cs_narrator "Потом тяжело вздохнул."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Соколова."
    $ cs_rev_room('bg ext_square_day')
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Даже не попытался подумать."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 5a2be7c491554189b789
    cs_sy "А зачем?"
    cs_sy "Ульяна бы уже засмеялась."
    cs_sy "Алиса придумала бы что-нибудь посерьёзнее."
    cs_sy "А Женя сначала спросила бы, почему я сижу без дела."
    cs_narrator "Справедливо."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Рука как?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 444b3a18d2a5eaa74fe5
    cs_ls "Последствия боевого столкновения."
    cs_ls "С асфальтом."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Ты утром бегала, подтягивалась, ходила с нами по петле… а потом просто споткнулась?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Главный противник оказался значительно ниже ожидаемого."
    # cs_page_anchor: fdfbd442f8c7bb070a3d
    cs_narrator "Он рассмеялся."
    cs_narrator "Я села рядом, осторожно устроив руку на коленях."
    cs_narrator "Дарья заняла место с другой стороны."
    cs_narrator "Я развернула лист и записала:"
    cs_narrator "«День второй. Автобус 410 у ворот отсутствует, след обрывается. За воротами: контрольная точка (резинка, стрелка). Двигаясь вперёд, дважды вернулись к ней. Назад — к воротам быстрее (около 5 минут). У отметок третья черта — не наша."
    cs_narrator "«Причина повторного появления точки неизвестна»."
    $ cs_road_notes_written = True
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Может, написать, что дорога возвращает?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: e306f2bb113a0b6ac642
    cs_da "Лучше то, что мы видели."
    cs_da "Вывод потом."
    # cs_page_anchor: 6de821692b43fdda817d
    cs_narrator "Я сложила лист."
    cs_narrator "Мне хотелось предложить ещё десять проверок: измерить расстояние, пройти вечером, взять у Шурика компас."
    cs_narrator "Но сегодня мы и так достаточно рисковали — и всё ещё не понимали, что происходит."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2a6e74e451f737ad730f
    cs_ls "Для начала стоит выяснить, есть ли у лагеря карта окрестностей."
    cs_ls "Куда эта дорога должна вести при нормальных обстоятельствах."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И спросить у кого-нибудь из взрослых, как обычно добираются до лагеря."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Только без рассказов о петлях с самого начала."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Это ты сейчас себе советуешь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Вполне заслуженно."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Мне кажется, Ольга Дмитриевна знает больше, чем говорит."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 51252aa31d84fcff0c27
    cs_ls "Мне тоже."
    cs_ls "Но пока это только впечатление."
    cs_ls "Давай не будем заранее решать, что она что-то скрывает."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 7906a17b974e7b79335f
    cs_sy "Ты серьёзно?"
    cs_sy "Вчера ты придумывала десять теорий после каждой фразы."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 03875392f6d59b9f0b6d
    cs_ls "Сегодня я дважды побывала у Виолы."
    cs_ls "Это сильно способствует переосмыслению приоритетов."
    $ cs_rev_music("sound/music/get_to_know_me_better.ogg",0.12,2.5)
    # cs_page_anchor: 73afee7e5777de220112
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "В Москве он был героем истории, которую я знала почти наизусть."
    cs_narrator "Его решения обсуждали, критиковали, над ними смеялись на форумах."
    cs_narrator "А теперь он сидел рядом, вертел обычный карандаш, уставал после поручений, беспокоился о доме и вполне успешно отвечал на мои шутки."
    cs_narrator "Он не обязан играть роль, которую я для него придумала."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 03245024edeabbe0e655
    cs_sy "Что?"
    cs_sy "Ты так смотришь, будто сейчас что-нибудь скажешь."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 5e339fead8d91b57e00f
    cs_ls "Хотела сказать спасибо."
    cs_ls "За то, что пошёл с нами к воротам."
    cs_ls "И не отмахнулся."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Мне самому нужно понять, что здесь происходит."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0bf15608cb324d90ba2d
    cs_ls "Знаю."
    cs_ls "Всё равно спасибо."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 57837ca49690ab6c9c7a
    cs_sy "Можно теперь и мне?"
    cs_sy "Ты ужасно странная."
    cs_sy "Но с тобой хотя бы не скучно."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я бы сказала примерно то же самое."
    # cs_page_anchor: 8088715d98bf9ba806a8
    cs_narrator "Наверное, так и появляются друзья."
    cs_narrator "Не после особенного признания."
    cs_narrator "Просто однажды замечаешь, что рядом с человеком спокойно."
    # cs_page_anchor: 594ac58c5ac9b2887e7b
    cs_narrator "Главный герой?"
    cs_narrator "Нет."
    cs_narrator "Просто Семён."
    cs_narrator "И этого вполне достаточно."
    # cs_page_anchor: 5982a528376c6d567578
    cs_narrator "Со стороны библиотеки шла Женя."
    cs_narrator "Несколько книг под мышкой, походка человека, который не любит, когда его задерживают без причины."
    # cs_page_anchor: 872089acef681ee282a1
    cs_narrator "Вчера я рассказала ей про игру и про будущее."
    cs_narrator "Она потребовала перестать говорить загадками."
    cs_narrator "И всё-таки не выгнала нас из библиотеки, хотя причин у неё было достаточно."
    if "2:7" in cs_rev_choices:
        if cs_rev_choices["2:7"]==0:
            $ cs_rev_choice(2,7,0)
            $ cs_talked_mz_square_day2 = True
            $ cs_rev_award("2:7:cs_friend_mz","cs_friend_mz",1)
            $ cs_mz_square_day2_awarded = True
            $ cs_talked_mz_square_day2 = True
            cs_narrator "На этот раз без попыток подкрасться и без специальных голосов."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Женя, привет."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: ba774b9aa484c7f34c11
            cs_mz "А, Соколова."
            cs_mz "Что с рукой?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: a7e6bbabf1bc03db9f40
            cs_ls "Неудачно упала."
            cs_ls "Виола уже обработала."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "Тогда осторожнее ходи."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 27df9653e2bdda2e3a73
            cs_ls "Сегодня это самое популярное пожелание в мой адрес."
            cs_ls "Я хотела сказать спасибо."
            cs_ls "За вчерашний разговор."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: 93cdb5b8d3c1ff148871
            cs_mz "За тот, где ты рассказывала, что приехала из будущего?"
            cs_mz "Я ведь тебе так и не поверила."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 129d47034139f36f9308
            cs_ls "Знаю."
            cs_ls "Но ты выслушала."
            cs_ls "И не требовала немедленно доказать каждое слово."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "Потому что доказательств у тебя не было."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: ff03a0bac97f39a0365e
            cs_ls "И сейчас нет."
            cs_ls "Просто я начинаю понимать, что для остальных всё это звучит гораздо страннее, чем для меня."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "Вот это уже похоже на здравую мысль."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 1ff4d8098f75236ff2bc
            cs_ls "Ещё вопрос."
            cs_ls "В библиотеке есть карты окрестностей?"
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: f95d7a1a938afa2a1c39
            cs_mz "Карты?"
            cs_mz "Не помню."
            cs_mz "Можно посмотреть по каталогу."
            cs_mz "Ничего не обещаю."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Этого достаточно."
            # cs_page_anchor: 969dec6ef4e51fb1424b
            cs_narrator "Без скандала."
            cs_narrator "Без спора об устройстве мироздания."
            cs_narrator "Нормальное человеческое общение постепенно переставало быть для меня чем-то непостижимым."
            $ cs_rev_finish_choice(2,7)
        else:
            $ cs_rev_choice(2,7,1)
            $ cs_talked_mz_square_day2 = False
            $ cs_talked_mz_square_day2 = False
            # cs_page_anchor: 9909a3ec33d8a64a447b
            cs_narrator "Женя шла сосредоточенно."
            cs_narrator "Вчерашнего разговора ей, наверное, хватило надолго."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: f91e052d4b7cb5c42c43
            cs_ls "Нет."
            cs_ls "Не будем её задерживать."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "А я думал, ты обязательно подойдёшь."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Учусь неожиданным решениям."
            cs_narrator "Не каждую встречу нужно превращать в событие."
            $ cs_rev_finish_choice(2,7)
    else:
        menu:
            "Подойти к Жене и поблагодарить за вчерашний разговор":
                $ cs_rev_choice(2,7,0)
                $ cs_talked_mz_square_day2 = True
                $ cs_rev_award("2:7:cs_friend_mz","cs_friend_mz",1)
                $ cs_mz_square_day2_awarded = True
                $ cs_talked_mz_square_day2 = True
                cs_narrator "На этот раз без попыток подкрасться и без специальных голосов."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Женя, привет."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: f75e9c03387924270954
                cs_mz "А, Соколова."
                cs_mz "Что с рукой?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 6b2c8eba32c624373bcb
                cs_ls "Неудачно упала."
                cs_ls "Виола уже обработала."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "Тогда осторожнее ходи."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 7c250037ed9b815f6478
                cs_ls "Сегодня это самое популярное пожелание в мой адрес."
                cs_ls "Я хотела сказать спасибо."
                cs_ls "За вчерашний разговор."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: 36d6affff66e83344436
                cs_mz "За тот, где ты рассказывала, что приехала из будущего?"
                cs_mz "Я ведь тебе так и не поверила."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: c12eea32fbe794256845
                cs_ls "Знаю."
                cs_ls "Но ты выслушала."
                cs_ls "И не требовала немедленно доказать каждое слово."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "Потому что доказательств у тебя не было."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 0b2db76d5f2bb77b6c0a
                cs_ls "И сейчас нет."
                cs_ls "Просто я начинаю понимать, что для остальных всё это звучит гораздо страннее, чем для меня."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "Вот это уже похоже на здравую мысль."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 41d8b9fa86ef950ebdc3
                cs_ls "Ещё вопрос."
                cs_ls "В библиотеке есть карты окрестностей?"
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: 15f316b0906e071bb09b
                cs_mz "Карты?"
                cs_mz "Не помню."
                cs_mz "Можно посмотреть по каталогу."
                cs_mz "Ничего не обещаю."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Этого достаточно."
                # cs_page_anchor: 140c0b4770bd29260495
                cs_narrator "Без скандала."
                cs_narrator "Без спора об устройстве мироздания."
                cs_narrator "Нормальное человеческое общение постепенно переставало быть для меня чем-то непостижимым."
                $ cs_rev_finish_choice(2,7)
            "Не отвлекать Женю от её дел":
                $ cs_rev_choice(2,7,1)
                $ cs_talked_mz_square_day2 = False
                $ cs_talked_mz_square_day2 = False
                # cs_page_anchor: 50c62778e46f04424c4f
                cs_narrator "Женя шла сосредоточенно."
                cs_narrator "Вчерашнего разговора ей, наверное, хватило надолго."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 46ca86515d84ed455206
                cs_ls "Нет."
                cs_ls "Не будем её задерживать."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "А я думал, ты обязательно подойдёшь."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Учусь неожиданным решениям."
                cs_narrator "Не каждую встречу нужно превращать в событие."
                $ cs_rev_finish_choice(2,7)
    cs_narrator "Семён ушёл в клубы — Шурик просил что-то передать."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "До вечера, Соколова."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "До вечера, товарищ Семён."
    return

label cs_rev_d2_15:
    $ cs_rev_begin(2,15,['cs_darya', 'cs_zhenya'])
    $ save_name = "Чужая смена — День 2: Просто почитать"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_library_day")
    # cs_page_anchor: 0fad24a94729005c49f7
    cs_narrator "Мы ещё немного прошлись."
    cs_narrator "Я никого не искала, не предложила зайти к Шурику и не придумала новый способ проверить дорогу."
    cs_narrator "Мне надоело быть главным происшествием дня."
    # cs_page_anchor: 71c1e18ec20a4684b98d
    cs_narrator "Впереди показалась библиотека."
    cs_narrator "Я вдруг поняла, что хочу именно туда."
    cs_narrator "Не за картами."
    cs_narrator "Просто туда, где можно сесть и ничего не объяснять."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 27f47dc23e47fe539437
    cs_ls "Даш, кажется, я нашла себе занятие до ужина."
    cs_ls "Хочу почитать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Просто почитать?"
    $ cs_rev_darya_offscreen = True
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 819544979d484da22a52
    cs_ls "Да."
    cs_ls "Представляешь, я иногда так делаю."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 552ecc5150a1a2ff8022
    cs_da "После сегодняшнего я готова ко всему."
    cs_da "Я зайду в домик, попью воды и приду к тебе."
    $ cs_pov_begin()
    with cs_sprite_leave
    stop music fadeout 1.5
    $ cs_rev_sfx('sound/sfx/open_door_1.ogg',0.25)
    # cs_page_anchor: 2f2c50a2c077b22fa5f1
    cs_narrator "В библиотеке было тихо."
    cs_narrator "Пахло бумагой и деревом."
    cs_narrator "Жени не было."
    # cs_page_anchor: 26b2543c573743f18d43
    cs_narrator "Вчера в руках у неё была книга — я запомнила не название, а цвет обложки и рисунок у корешка."
    cs_narrator "На полке нашлись два экземпляра: новый и потёртый, с пожелтевшими страницами."
    cs_narrator "Я взяла второй и села у окна так, чтобы свет падал слева, а больная рука лежала на столе."
    # cs_page_anchor: b8fcefe545cc800c0ffe
    cs_narrator "Первые строки шли тяжело."
    cs_narrator "Я всё ещё думала о дороге, о резинке на кусте, о третьей черте."
    cs_narrator "Потом втянулась."
    cs_narrator "Один абзац, другой, третий."
    cs_narrator "И вместо «Совёнка» передо мной встала совсем другая история."
    # cs_page_anchor: f849dbb1b68534f2e78e
    cs_narrator "Как давно я не читала бумажные книги."
    cs_narrator "В Москве — телефон, вкладки, уведомления, возвращение к тексту через полчаса."
    cs_narrator "Здесь отвлекаться было не на что."
    cs_narrator "И впервые за два дня меня это полностью устраивало."
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.35)
    # cs_page_anchor: 754b0a9d3719b46fb7bf
    cs_narrator "Хлопнула дверь."
    cs_narrator "Шаги."
    cs_narrator "На стол легла стопка бумаг."
    cs_narrator "Я дочитала абзац и только тогда подняла голову."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: cfa17f75e9ed3beb11e2
    cs_mz "Соколова?"
    cs_mz "Ты давно здесь?"
    cs_mz "Зачем пришла?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Почитать."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Просто почитать?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Угу."
    # cs_page_anchor: 10443fab4c6ddf7dbd31
    cs_narrator "Она явно ждала чего угодно: рассказа о будущем, вопросов о лагерных документах, хотя бы попытки завести разговор."
    cs_narrator "А я вернулась к странице."
    if cs_friend_mz <= 0:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 0f80074476fe6fd5f16e
        cs_mz "Только не разговаривай на всю библиотеку."
        cs_mz "И книги с полок бери аккуратно."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Конечно."
        # cs_page_anchor: 261bb98730714c7f132b
        cs_narrator "Человек обозначил правила."
        cs_narrator "Я согласилась."
        cs_narrator "Оказывается, это довольно простая система."
    elif cs_friend_mz == 1:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: d2d6e4a8532601c1304c
        cs_mz "Это ведь та, что я вчера читала?"
        cs_mz "Нашла второй экземпляр?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "На полке стояли два."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 79ae064ad09ae31be139
        cs_mz "Дальше интереснее."
        cs_mz "Только в конец не заглядывай."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Даже не собиралась."
    else:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Ты всё-таки решила её прочитать."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Ты вчера так увлечённо читала, что стало интересно."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: bcfb8ff8afa2670b68d5
        cs_mz "До какого места дошла?"
        cs_mz "Тогда ничего не рассказываю."
        cs_mz "Там дальше есть момент, который лучше прочитать самой."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 60aa527964e83225e57b
        cs_ls "Договорились."
        cs_ls "Без спойлеров."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Без чего?"
        # cs_page_anchor: 383e0e00dede9fba14b9
        cs_narrator "Ах да."
        cs_narrator "Опять."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Без рассказов о том, что будет дальше."
        # cs_page_anchor: aa4ffe0289c376a9633c
        cs_narrator "Через минуту она положила рядом со мной закладку — прямоугольник плотной бумаги."
        cs_narrator "Ещё вчера я бы не подумала, что Женя сама что-нибудь мне предложит."
    cs_narrator "Пришла Дарья, огляделась и остановилась у моего стола."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты действительно читаешь."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "А что должна была делать?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 025023c1e649c2258d79
    cs_da "Не знаю."
    cs_da "Я ожидала хотя бы небольшого расследования."
    $ cs_rev_darya_offscreen = False
    # cs_page_anchor: 9269006917b66a3b2335
    cs_narrator "Она спросила у Жени, какие книги можно брать, выбрала небольшой том и села рядом."
    cs_narrator "Мы читали молча."
    cs_narrator "Иногда она меняла положение на стуле или поправляла волосы."
    cs_narrator "Две девушки, которые ещё позавчера ехали в одном автобусе через зимнюю Москву, сидели в советской библиотеке и читали."
    # cs_page_anchor: ea977f90c5f34b73d1ca
    cs_narrator "Невероятно обыкновенное занятие."
    cs_narrator "Именно его мне и хотелось."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: db50dd05590d9727f0e0
    cs_mz "Лена."
    cs_mz "Ты сидишь здесь уже давно."
    cs_mz "И всё это время читаешь."
    cs_mz "А почему вчера вела себя совсем иначе?"
    # cs_page_anchor: 63dd4ec0bd44b8e3f26c
    cs_narrator "Закономерный вопрос."
    cs_narrator "Вчера я пришла сюда, зная, кто такая Женя, и проверяла, будет ли она вести себя так, как я помню."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ac87ad1d558c41bb2dd9
    cs_ls "Наверное, потому что вчера я очень нервничала."
    cs_ls "Когда происходит слишком много сразу, я начинаю говорить без остановки."
    cs_ls "А когда успокаиваюсь, могу часами сидеть над рисунком или книгой почти молча."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Вот этого я пока не видела."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Теперь видишь."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И мне нравится."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Это всё равно не объясняет половину твоих вчерашних шуток."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Некоторые из них я и сама не объясню."
    # cs_page_anchor: 61b7e8ab279ff534c124
    cs_narrator "Не нужно убеждать её, что сегодняшняя Лена настоящая, а вчерашняя — нет."
    cs_narrator "Обе настоящие."
    cs_narrator "Просто я не всегда одинаковая."
    $ cs_reading_book_borrowed = False
    $ cs_reading_book_location = "library_shelf"
    $ cs_lena_book_returned = True
    # cs_page_anchor: 2d828fb75c4e351b6756
    cs_narrator "Последние страницы оказались не такими, как я ожидала."
    cs_narrator "Автор не устроил грандиозного примирения и не решил всё одной красивой речью."
    cs_narrator "Кто-то так и не сказал самых нужных слов."
    cs_narrator "И всё же финал не казался оборванным."
    cs_narrator "Скорее честным."
    cs_narrator "Я закрыла книгу и отнесла её Жене."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 3c8cb7a7343035914607
    cs_mz "Дочитала?"
    cs_mz "И как?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 4d2a37021875c471c8bd
    cs_ls "Очень хорошая."
    cs_ls "Персонажи не стали другими людьми только потому, что история подошла к концу."
    if cs_friend_mz <= 0:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 77fd22ddee8b44be870b
        cs_mz "Понятно."
        cs_mz "Хорошо, что понравилась."
        cs_narrator "Она поставила отметку о возврате."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 29f76f37f636d5c1a2fc
        cs_mz "В следующий раз осторожнее с книгами."
        cs_mz "И с собой тоже."
    elif cs_friend_mz == 1:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 14d894a91083059ab376
        cs_mz "А мне показалось, автор слишком мягко обошёлся с главным героем."
        cs_mz "Он долго ничего не делал — и всё равно получил шанс."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 4fb899f886d4da3189f0
        cs_ls "Но исправить всё полностью он уже не может."
        cs_ls "Это конец, в котором люди наконец начали отвечать за свои решения."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 18b22f66b7368ed5bd85
        cs_mz "Интересная мысль."
        cs_mz "Если будешь ещё что-нибудь брать — скажи."
        cs_mz "Посоветую."
    else:
        $ cs_mz_reading_invite = True
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "А последнее решение героя?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 877f5d3c40ecd25143ac
        cs_ls "Правильное."
        cs_ls "Но слишком позднее."
        cs_ls "Мне понравилось, что автор не оправдывает его только потому, что он главный герой."
        cs_narrator "Женя негромко рассмеялась."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: d035c546ae74f428cc2a
        cs_mz "Удивительно, Соколова, но в литературе мы иногда можем договориться."
        cs_mz "И вообще… можешь приходить сюда читать."
        cs_mz "Не обязательно каждый раз с вопросами про странные автобусы."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Спасибо, Женя."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Только не разговаривай на всю библиотеку."
    $ cs_reading_book_borrowed = False
    $ cs_lena_book_returned = True
    $ cs_reading_book_location = "library_shelf"
    if cs_talked_mz_square_day2:
        $ cs_mz_map_lead = True
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: d9c5502cf5807594b17f
        cs_mz "И насчёт карт."
        cs_mz "В дальнем углу стоят коробки со старыми каталогами, их давно никто не разбирал."
        cs_mz "Могут быть справочники, планы территории, бумаги прежних смен."
        cs_mz "Я давно собиралась разобрать этот угол."
        cs_mz "Приходи завтра, посмотрим вместе."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Даже это больше, чем у нас есть сейчас."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: ed47052fa1d19179e8a6
        cs_mz "Только без лекций про будущее."
        cs_mz "И ничего не вытаскивай из шкафов сама."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Договорились."
        # cs_page_anchor: 427d28f629437416d3c5
        cs_narrator "Впервые за день кто-то из местных сам предложил помочь."
        cs_narrator "Не потому, что поверил."
        cs_narrator "Потому что мы успели немного узнать друг друга."
        $ cs_mz_map_lead = True
    $ cs_rev_room('bg ext_library_day')
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.25)
    cs_narrator "На крыльце Дарья первой нарушила тишину."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 077b69f2b611e1d30e68
    cs_da "Мне понравилось сидеть с тобой в библиотеке."
    cs_da "Особенно без необходимости всё время о чём-то говорить."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: e84ac0ea11fa8296d540
    cs_ls "Мне тоже."
    cs_ls "Даш… если я иногда молчу, это не значит, что мне с тобой скучно."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 4221911aafd2888d8b01
    cs_da "Я поняла."
    cs_da "И тебе не обязательно постоянно меня развлекать."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Но иногда можно?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Иногда можно."
    return

label cs_rev_d2_16:
    $ cs_rev_begin(2,16,['cs_darya', 'cs_semen', 'cs_zhenya'])
    $ save_name = "Чужая смена — День 2: Котлетки с пюрешкой"
    $ cs_rev_time("sunset")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_camp_path_sunset")
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    cs_narrator "Над лагерем прозвучал горн."
    $ cs_rev_music(cs_day_music_everyday,0.14,2.5)
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 31a875df87806993d0f5
    cs_ls "Ужин."
    cs_ls "Желудок переводит синхронно."
    # cs_page_anchor: 4f0d7eab0bbe95480cae
    cs_narrator "И тут в голове всплыла мелодия."
    cs_narrator "Старая, нелепая, до боли знакомая."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 96baf073c6ccce81f3c9
    cs_ls "Котлетки с макарошками…"
    cs_ls "Нет, с пюрешкой!"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Это что?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Культурное наследие русскоязычного интернета."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я уж подумала, тебе стоит ещё раз показаться Виоле."
    cs_narrator "Старые сайты, видео ужасного качества, шутки, которые невозможно объяснить тому, кто не застал их появления."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 71d1291a71013145db72
    cs_ls "Ой."
    cs_ls "Олдскулы свело."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты же сама из двадцать шестого."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 3bb03b313e1218313eaf
    cs_ls "Именно поэтому и ностальгирую."
    cs_ls "Тогда люди делали всякую ерунду просто потому, что им было весело."
    cs_ls "А потом даже производство глупостей стало профессиональным."
    $ cs_rev_room('bg int_dining_hall_sunset')
    # cs_page_anchor: c3460d4a69eff819bfa2
    cs_narrator "У раздачи я замерла."
    cs_narrator "Картофельное пюре."
    cs_narrator "Котлеты."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 6a94143b85b0c520d586
    cs_ls "Даша."
    cs_ls "Ты видишь?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Котлеты?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "С пюрешкой."
    cs_narrator "Дарья закрыла глаза и рассмеялась."
    # cs_page_anchor: e70dbeb7bab7f51790eb
    cs_narrator "Дома я сфотографировала бы тарелку, отправила знакомым и пошла дальше."
    cs_narrator "А здесь телефон не включить."
    cs_narrator "Может, и к лучшему."
    cs_narrator "Некоторые вещи можно просто запомнить."
    cs_narrator "В дальнем углу, за самым тихим столом у окна, сидела Женя с книгой."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Только не объявляй ей принудительную программу социализации."
    # cs_page_anchor: 5751d88d41a9677bc77e
    cs_narrator "Человек специально сел один."
    cs_narrator "Возможно, это не просьба о спасении."
    cs_narrator "Но спросить можно."
    if cs_friend_mz >= 2:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Ну садитесь, раз уж пришли."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Это сейчас было приглашение?"
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Нет, приказ немедленно покинуть столовую."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Только я сюда села, потому что здесь тихо."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Торжественно обещаю не разрушать атмосферу."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Ты ей веришь?"
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "Минут на пять."
    elif cs_friend_mz == 1:
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: a538a276b6aae0bb1342
        cs_ls "Женя, можно к тебе?"
        cs_ls "Если хочешь посидеть одна — не будем мешать."
        cs_narrator "Женя посмотрела на Дарью, потом на меня."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 8824bb36d49ba1a16bd9
        cs_mz "Ладно."
        cs_mz "Садитесь."
        cs_mz "Только без вчерашнего разговора на полчаса."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Исключительно бытовые темы."
    else:
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Женя, можно к тебе присоединиться?"
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Я хотела спокойно поесть одна."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: a6fd98378e30f04c95a5
        cs_ls "Хорошо."
        cs_ls "Тогда приятного аппетита."
        cs_narrator "Мы сели у другого окна."
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "Я думала, ты будешь настаивать."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: db04d7c53e3a3c7b004e
        cs_ls "Она прямо сказала, чего хочет."
        cs_ls "Странно обижаться на человека за то, что он это знает."
    if cs_friend_mz >= 1:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Что ты так смотришь на тарелку?"
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "Лена по дороге вспомнила старую песенку про котлеты с пюре."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "И ты теперь каждый раз будешь её вспоминать, увидев котлеты?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Надеюсь, что нет."
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "А ты всегда читаешь за едой?"
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Только когда вокруг слишком шумно."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "То есть книга — средство индивидуальной защиты?"
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "От некоторых людей — определённо."
        if cs_mz_map_lead:
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: 65d3fd8d050c05c47b23
            cs_mz "Про каталоги — после завтрака."
            cs_mz "Позже у меня работы много."
    cs_narrator "Между столами прошёл Семён с пустым подносом."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Рука как?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Если не трогать, почти не беспокоит."
    if cs_friend_se >= 2:
        $ cs_rev_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: 276e75752b8c695586cf
        cs_sy "Я после ужина помогаю со скамейками."
        cs_sy "Спрошу у Слави, где вам удобнее сесть — чтобы не пробираться через толпу с рукой."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Только не пересаживай никого специально."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Не собирался."
    else:
        $ cs_rev_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: 9dbe3089e4fddd2671a6
        cs_sy "Ладно, я побежал."
        cs_sy "Обещал помочь с подготовкой."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Смотри под ноги."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Это ты мне говоришь?"
    return

label cs_rev_d2_17:
    $ cs_rev_begin(2,17,['cs', 'cs_darya', 'cs_semen', 'mi', 'mt', 'sl', 'un'])
    $ save_name = "Чужая смена — День 2: Музыкальный вечер"
    $ cs_rev_time("sunset")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_square_sunset")
    $ cs_rev_music("sound/music/feeling_good.ogg",0.16)
    # cs_page_anchor: a2828bb7a210ddbad2f8
    cs_narrator "На площади прибавилось народу."
    cs_narrator "Из-за площадки доносились обрывки звуков гитары."
    if cs_friend_sl >= 1:
        $ cs_sl_good_seats = True
        $ cs_rev_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: 98db0177e7442b9ff43f
        cs_sl "Лена!"
        cs_sl "Даша!"
        cs_sl "Мы оставили вам места у края первого ряда."
        cs_sl "Там удобнее, и не придётся протискиваться с больной рукой."
        if cs_friend_se >= 2:
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Семён тоже про вас спрашивал."
        if cs_helped_sl_day2:
            $ cs_rev_focus("sl")
            with cs_sprite_change
            cs_sl "Вы же утром помогли с коробками."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 90d495e858edbf77534d
        cs_ls "Спасибо, Славя."
        cs_ls "Правда."
    else:
        $ cs_sl_good_seats = False
        $ cs_rev_focus("sl")
        with cs_sprite_change
        cs_sl "Девочки, садитесь скорее, места заканчиваются!"
        # cs_page_anchor: 440af24da1f84b543a85
        cs_narrator "Мы сели сбоку."
        cs_narrator "Оттуда было видно площадку, хотя и дальше от музыкантов."
    # cs_page_anchor: 0eaff10bf1bdc2b29ef7
    cs_narrator "Наш плакат сработал."
    cs_narrator "Люди пришли, места готовы, музыканты настраиваются."
    cs_narrator "Удивительное чувство — сделать что-то маленькое и увидеть результат в настоящей жизни."
    if cs_friend_mi >= 1:
        $ cs_mi_intro_revised = True
        $ cs_rev_focus("mi")
        with cs_sprite_change
        # cs_page_anchor: a8943eb95fc812caffec
        cs_mi "Лена, Даша, вы пришли!"
        cs_mi "Я сократила то вступление, о котором мы утром говорили!"
        cs_mi "Алиса тоже сказала, что так интереснее."
        cs_mi "Только не судите строго, я всё равно волнуюсь!"
        $ cs_mi_intro_revised = True
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "Всё будет хорошо."
    else:
        $ cs_mi_intro_revised = False
        cs_narrator "Мику заметила нас среди зрителей и помахала рукой."
    if cs_friend_viola >= 2:
        $ cs_viola_spare_bandage = True
        $ cs_rev_focus("vi")
        with cs_sprite_change
        # cs_page_anchor: b0681e6f6e083270a40f
        cs_vi "Лена, на минутку."
        cs_vi "Возьми про запас."
        cs_vi "Сегодня ничего менять не нужно — если понадобится, зайдёшь ко мне."
        cs_narrator "Она протянула маленький свёрток с чистой повязкой и к локтю не прикоснулась."
        $ cs_viola_spare_bandage = True
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 9ff6aee68aa364f53029
        cs_ls "Спасибо."
        cs_ls "Я помню: без новых подвигов."
    if cs_met_un and cs_friend_un >= 1:
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 4f41a42c4225ffb58a95
        cs_un "Лена… я попробую зарисовать выступление."
        cs_un "Потом показать тебе?"
        $ cs_un_concert_sketch_seen = True
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 8b4a82316516b13bd9af
        cs_ls "Конечно."
        cs_ls "Мне интересно, что ты заметишь."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 450f099dc71d09ef2140
    cs_mt "Ну что, все готовы?"
    cs_mt "Девочки, вам слово."
    $ cs_rev_room('cs_cg_square_concert_evening')
    $ cs_rev_music(cs_miku_piano_track,0.25,1.0)
    # cs_page_anchor: 2019679db90d5a90c6be
    cs_narrator "Мику взяла первые ноты."
    cs_narrator "Алиса вступила чуть позже, не перекрывая мелодию."
    if cs_mi_intro_revised:
        $ cs_rev_focus("da")
        with cs_sprite_change
        # cs_page_anchor: 336a4697178dca644ccb
        cs_da "Слышишь?"
        cs_da "Она всё-таки сократила начало."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "И мелодия сразу дышит свободнее."
    else:
        # cs_page_anchor: cfa0f1e8d9a19174238c
        cs_narrator "Вступление было коротким и тихим."
        cs_narrator "Оно не требовало внимания — просто постепенно его собирало."
    # cs_page_anchor: 34d734e44e32980c2f92
    cs_narrator "Алиса смотрела на подругу и ловила движение её плеча, чтобы вступить вовремя."
    cs_narrator "Никакой привычной перепалки — только внимательный взгляд и следующая точно взятая нота."
    # cs_page_anchor: 054c0774b6241e6ae406
    cs_narrator "Никуда не торопиться."
    cs_narrator "Ничего не проверять."
    cs_narrator "Просто побыть здесь."
    $ cs_rev_room('cs_cg_square_concert_close')
    cs_narrator "А потом мелодия пошла вверх, и я поняла, какая нота будет следующей."
    # cs_page_anchor: f6d5ccfcc8eb9461684c
    cs_narrator "Не догадалась."
    cs_narrator "Знала."
    cs_narrator "Как знают слово в давно выученной песне."
    cs_narrator "Мику взяла именно её."
    # cs_page_anchor: ba97aef61003fec2c2b4
    cs_narrator "Я эту песню никогда не слышала."
    cs_narrator "Мику сама говорила утром, что придумала её этим летом."
    stop music fadeout 3.0
    # cs_page_anchor: b1cae16378f0cf2c0e6a
    cs_narrator "К последней фразе сопровождение стихло."
    cs_narrator "Алиса сняла руку со струн, оставив ноте время прозвучать."
    cs_narrator "Секунда тишины — и аплодисменты."
    $ cs_rev_sfx('sound/sfx/concert_applause.ogg',0.4)
    cs_narrator "Я хлопала осторожно, почти не двигая локтем."
    if cs_mi_intro_revised:
        $ cs_rev_focus("mi")
        with cs_sprite_change
        # cs_page_anchor: dcdc1ee860c0d838e433
        cs_mi "Спасибо, что утром послушали!"
        cs_mi "Начало теперь как надо!"
    else:
        $ cs_rev_focus("mi")
        with cs_sprite_change
        cs_mi "Как хорошо, что вы пришли!"
    $ cs_rev_room('bg ext_square_sunset')
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Спасибо за музыку."
    cs_narrator "Алиса махнула нам со сцены."
    if cs_friend_se >= 2:
        $ cs_rev_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: f550c43c94856ba90291
        cs_sy "Ну как?"
        cs_sy "Удалось отдохнуть от наших исследований?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 74a913702235065192d6
        cs_ls "Удалось."
        cs_ls "Я даже никого не спросила про автобус."
        $ cs_rev_focus("sy")
        with cs_sprite_change
        # cs_page_anchor: 67d29dc2981305806256
        cs_sy "Запишем как успех."
        cs_sy "Остальное завтра."
    if cs_met_un and cs_friend_un >= 1:
        $ cs_un_concert_sketch_seen = True
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 3e80ae2eed4ea230c295
        cs_un "Вот."
        cs_un "Я обещала."
        # cs_page_anchor: b0a6c4d4796db33f724a
        cs_narrator "Два быстрых силуэта, несколько линий инструментов."
        cs_narrator "Но наклон головы Мику узнавался сразу."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Ты поймала момент, когда они посмотрели друг на друга."
        $ cs_rev_focus("un")
        with cs_sprite_change
        cs_un "Мне тоже он понравился."
    # cs_page_anchor: 4edce1bb1a1623f32ce3
    cs_narrator "Я не помнила, когда последний раз так слушала музыку."
    cs_narrator "Без телефона в руке."
    cs_narrator "Без мысли о том, как потом расскажу об этом подписчикам."
    cs_narrator "Просто слушала."
    return

label cs_rev_d2_18:
    $ cs_rev_begin(2,18,['cs_darya'])
    $ save_name = "Чужая смена — День 2: Своё место"
    $ cs_rev_time("night")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_house_lena_darya_int_night")
    stop music fadeout 1.5
    # cs_page_anchor: be3c079e0cdb5832e6c2
    cs_narrator "Дарья пришла раньше и сидела на кровати с книгой."
    cs_narrator "Я сняла туфли, проверила, не задела ли повязку, и села напротив."
    cs_narrator "После нескольких тихих часов мне снова захотелось разговаривать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: e86ce5f7d7d80e309196
    cs_da "Лена."
    cs_da "Ты опять что-то придумала?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Поздравляю тебя с окончанием вечера образцово спокойной и интеллектуальной Соколовой."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А что вместо неё?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d2b33600e239c4cfcaf9
    cs_ls "Та же Соколова."
    cs_ls "Только у неё снова есть силы разговаривать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мне интересно, что ты скажешь."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: cb03c1095ba561610124
    cs_ls "Знаешь, я сегодня кое-что решила."
    cs_ls "С Женей буду вести себя иначе."
    cs_ls "Раньше я принимала её раздражение за повод пошутить ещё раз."
    cs_ls "А ей не обязательно должно быть весело от каждой моей шутки."
    cs_ls "Если человеку хочется побыть одному, его не нужно спасать от одиночества."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мне нравится эта мысль."
    cs_narrator "Я осторожно легла поперёк кровати."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 78aa98b3ca4e07f92b7b
    cs_ls "Вообще я с разными людьми разная."
    cs_ls "С Женей интересно говорить о книгах."
    cs_ls "Со Славей приятно работать — рядом с ней даже я выгляжу полезным членом общества."
    cs_ls "С Мику — о музыке, хоть я и не понимаю, как она обсуждает пять тем сразу."
    cs_ls "С Семёном у нас бесконечное соревнование по взаимному поддразниванию."
    cs_ls "Но он хороший человек."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "А со мной?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9d0ef93b8f62552c08c5
    cs_ls "С тобой мне хочется быть собой."
    cs_ls "Без объяснений, почему сегодня я разговорчивая, а завтра могу молчать несколько часов."
    # cs_page_anchor: f8ce4f00c6f6106faa9c
    cs_narrator "Дарья долго ничего не говорила."
    cs_narrator "Потом тихо улыбнулась."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Мне тоже с тобой хорошо."
    # cs_page_anchor: fe778de028be7350fafd
    cs_narrator "Одна короткая фраза."
    cs_narrator "А звучит важнее половины моих длинных признаний."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Можно?"
    # cs_page_anchor: aae75df6fb7373221d64
    cs_narrator "Я протянула здоровую руку."
    cs_narrator "Дарья посмотрела на мою ладонь, потом на меня."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Можно."
    # cs_page_anchor: 975b6364be20c65e290b
    cs_narrator "Она взяла меня за руку, и я переплела наши пальцы."
    cs_narrator "Мы просто сидели."
    cs_narrator "Вчера я едва смогла признаться ей."
    cs_narrator "Сегодня мы держимся за руки — и я всё ещё не знаю, что будет дальше."
    cs_narrator "Но сейчас неизвестность не казалась страшной."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Только не говори, что мы подписали какой-нибудь договор."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ты только что уничтожила прекрасную шутку."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: c2418ff3db305a3bd206
    cs_da "Я догадалась."
    cs_da "Можешь придумать новую."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 4eb48fef22c797e46023
    cs_ls "Не сейчас."
    cs_ls "Мне и так хорошо."
    cs_narrator "Она чуть крепче сжала мою ладонь."
    # cs_page_anchor: 49a7e653a24e14efd5f9
    cs_narrator "Галстук я попыталась снять слишком резко, и локоть немедленно напомнил о себе."
    cs_narrator "Дарья развязала узел, стараясь не задеть руку."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Если завтра соберёшься бегать — сначала посмотри, как будет локоть."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 51bdf36c8732e671aa8c
    cs_ls "Виола не зря просила беречь."
    cs_ls "А если рука перестанет болеть — составишь мне компанию на утренней прогулке?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: b53b924e9269075041ac
    cs_da "На прогулке — возможно."
    cs_da "Только не превращай её в забег."
    # cs_page_anchor: b9705f6cb3baacfa0c74
    cs_narrator "Я посмотрела на её кровать."
    cs_narrator "На свободное место у стены."
    cs_narrator "Если не спросить, ответа точно не будет."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 5c2bc1cfa7a6ab3e28c1
    cs_ls "Даш."
    cs_ls "А сегодня мне можно лечь с тобой?"
    # cs_page_anchor: 637ed45426a3f22d7059
    cs_narrator "Она подняла голову."
    cs_narrator "Посмотрела на меня, на мою кровать, снова на меня."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 93f84e14826e0e2b2dfc
    cs_da "Нет, Лен."
    cs_da "Мне пока нужно своё место."
    # cs_page_anchor: e5b972f06731245b39ef
    cs_narrator "Сказала спокойно."
    cs_narrator "Без обиды и без шутки."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f359a207a04073cfeccc
    cs_ls "Понятно."
    cs_ls "Хорошо."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты не обиделась?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 3378ced7719ea866c963
    cs_ls "Нет."
    cs_ls "Ты ведь вчера сказала, что не хочешь торопиться."
    cs_ls "Я помню."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: b27e0a673b3bef65fe1f
    cs_da "Может быть, когда-нибудь."
    cs_da "Это не обещание."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 6e6c1aea75a40fd7956f
    cs_ls "Я понимаю."
    cs_ls "Но формулировка заметно мягче предыдущей."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Спи уже, переговорщица."
    $ cs_rev_room('cs_house_lena_darya_int_sleep_night')
    $ cs_rev_sfx('sound/sfx/click_3.ogg',0.2)
    # cs_page_anchor: 1d74011bdf1e223025c7
    cs_narrator "Дарья погасила свет."
    cs_narrator "Из окна доносились сверчки."
    cs_narrator "Я легла на бок, не прижимая больную руку."
    # cs_page_anchor: bebdf7c498f07201ec9d
    cs_narrator "Ещё утром мне казалось, что каждую свободную минуту я обязана тратить на возвращение домой."
    cs_narrator "Теперь я понимала, что так нельзя."
    cs_narrator "Не потому, что перестала хотеть домой."
    cs_narrator "Просто голова не может бесконечно жить в тревоге."
    cs_narrator "Иногда нужно остановиться."
    # cs_page_anchor: 7827d401bcf2d1b6081f
    cs_narrator "Почитать."
    cs_narrator "Послушать музыку."
    cs_narrator "Помолчать рядом с человеком, который тебе нравится."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 7ad8dc58a19e6cc697a5
    cs_ls "Даш."
    cs_ls "Спасибо за сегодняшний день."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И тебе, Лен."
    # cs_page_anchor: 7cccae0d3b44c0615838
    cs_narrator "Перед сном я ещё раз вспомнила свой лист."
    cs_narrator "Второй день у нас."
    cs_narrator "Третий — у Семёна."
    cs_narrator "Разница в один день."
    cs_narrator "Пока."
    return
