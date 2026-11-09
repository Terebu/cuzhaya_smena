# -*- coding: utf-8 -*-
label cs_day05_04:
    $ cs_d5_scene = 4
    $ save_name = "Чужая смена — День 5: Бумаги вожатой"
    $ cs_bus_scene_enter(4)
    $ cs_d5_room("bg ext_house_of_mt_day")
    with Dissolve(0.7)
    $ cs_rev_sfx('sound/sfx/open_door_1.ogg',0.4)
    cs_narrator "Дверь открыла сама Ольга Дмитриевна."
    cs_narrator "Увидев нашу компанию, она вздохнула."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Только не говорите, что опять что-то случилось."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 39b99ca77f643fb60d1e
    cs_ls "Доброе утро."
    cs_ls "Пока ничего не сломали."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Меня настораживает слово «пока»."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0875fcf377f565e7894c
    cs_ls "Тогда начнём с хороших новостей."
    cs_ls "Мы все живы и даже позавтракали."
    cs_narrator "Она посмотрела на Семёна."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Что произошло?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 80c25445fa8887da132f
    cs_sy "Нам нужно поговорить."
    cs_sy "Про сны."
    cs_narrator "Вожатая отступила от двери."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 50e11b3fbedd264c057b
    cs_mt "Заходите."
    cs_mt "Только у меня немного времени."
    $ cs_d5_room("bg int_house_of_mt_day")
    cs_narrator "Мы вошли."
    cs_narrator "На столе лежали бумаги, возле них стояла кружка с чаем."
    # cs_page_anchor: f3c2c7f259dbad23796f
    cs_narrator "Семён сел на край своей кровати."
    cs_narrator "Женя устроилась на стуле, достала тетрадь и приготовила карандаш."
    cs_narrator "Даша осталась возле окна."
    cs_narrator "Я села напротив Ольги Дмитриевны."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Рассказывайте."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ce38966ae35330b32c86
    cs_ls "Вчера вы говорили, что иногда вспоминаете вещи, которых вроде бы не было."
    cs_ls "Сегодня ничего нового не появилось?"
    cs_narrator "Ольга Дмитриевна отложила ручку."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 84acd2bbf118d91b5b84
    cs_mt "Кое-что вспомнила."
    cs_mt "Но не уверена, что это вообще воспоминание."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 3b452fee52f8eb7bf381
    cs_mz "Расскажите как есть."
    cs_mz "Мы пока ничего объяснять не будем."
    cs_narrator "Вожатая посмотрела на неё с благодарностью."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: bcdcf9a6aa9fc3b20af4
    cs_mt "Мне снился автобус."
    cs_mt "Будто он дважды приезжал к лагерю за одну смену."
    cs_narrator "Я почувствовала, как напряглись плечи."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Дважды?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 5f01ce2fa76ffc503456
    cs_mt "Сначала забирал отряд."
    cs_mt "А потом возвращался."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "За кем?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Из него выходила девушка."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Вы помните, как она выглядела?"
    cs_narrator "Ольга Дмитриевна покачала головой."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 8cab517823dba0d088f4
    cs_mt "Лицо не помню."
    cs_mt "Только волосы."
    cs_mt "Фиолетовые."
    cs_narrator "Семён повернулся ко мне."
    cs_narrator "Я подняла брови."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c9048524fbd61cffa697
    cs_ls "Если что, у меня сегодня на утро алиби."
    cs_ls "Я бегала."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Лена, я серьёзно."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 70c1b47d9e92c9fbdd27
    cs_ls "Я тоже."
    cs_ls "Просто мне не нравится, что подозреваемых выбирают по цвету волос."
    cs_narrator "Даша положила ладонь на спинку моего стула."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Давайте дальше."
    cs_narrator "Семён рассказал свой сон."
    cs_narrator "Я добавила подробности собственного."
    cs_narrator "Ольга Дмитриевна слушала, не перебивая."
    cs_narrator "Когда прозвучала фраза «Остался один», она перестала перебирать бумаги."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Вы узнали эти слова?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 46c8ebcca0a750deb672
    cs_mt "Да."
    cs_mt "Мне тоже такое снилось."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "И что было дальше?"
    cs_narrator "Вожатая задумалась."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 0239a3df78ff9517ab0d
    cs_mt "Пустой лагерь."
    cs_mt "Я стою здесь и жду автобус."
    cs_mt "Потом открываются двери."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вы садитесь?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 2386e4232d404dd219a4
    cs_mt "Не помню."
    cs_mt "Следующее, что вижу, — утро."
    cs_mt "Все снова на месте."
    cs_narrator "Я переглянулась с Дашей."
    cs_narrator "В голове уже выстраивалось несколько предположений."
    cs_narrator "Но Женя предупредила ещё за завтраком: не надо торопиться."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 4c4c850fcf1913b16b5f
    cs_ls "Хорошо."
    cs_ls "А про старые смены что-нибудь вспомнилось?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 83c15d183393427654d3
    cs_mt "Только то, что я вам рассказывала."
    cs_mt "Иногда мне кажется, что я уже встречала кого-то из пионеров раньше."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Конкретные даты?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Нет."
    cs_narrator "Женя достала из сумки папку — ту самую, которую вчера заперла в ящике картотеки."
    cs_narrator "Фотография семьдесят первого года и список."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Тогда посмотрите ещё раз на это."
    $ cs_d5_documents_location = "olga"
    cs_narrator "Ольга Дмитриевна взяла фотографии."
    cs_narrator "Она долго рассматривала лица."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Знакомые."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Кто именно?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: e80c34fe1de28b7ae5ad
    cs_mt "Вот в том и дело."
    cs_mt "Узнать могу, а вспомнить откуда — нет."
    cs_narrator "Она положила снимок обратно."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 2d03a4b24eb361727fba
    cs_mz "Может, пусть все оригиналы лежат в одном месте?"
    cs_mz "Тот снимок, что Лена вам вчера оставила, ведь уже здесь."
    cs_narrator "Вожатая кивнула."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 74c9e66bddf5feb02be0
    cs_mt "Да."
    cs_mt "Я уберу их вместе."
    cs_mt "А вы сделайте копии записей."
    cs_narrator "Женя тут же переписала список к себе в тетрадь — аккуратно, фамилия под фамилией."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 39864d21139610b0f829
    cs_ls "Хорошо."
    cs_ls "Хотя я бы предпочла иметь дело с обычными лагерными отчётами."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Поверь, я тоже."
    if cs_d4_od_trust_approach:
        cs_narrator "Она открыла ящик стола и достала ещё один лист."
        $ cs_d5_focus("mt")
        with cs_sprite_change
        # cs_page_anchor: 8a29e18eb5cd1799604c
        cs_mt "Вчера нашла старую ведомость."
        cs_mt "Здесь есть запись «Повторный рейс»."
        cs_narrator "Я наклонилась ближе."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Дата есть?"
        $ cs_d5_focus("mt")
        with cs_sprite_change
        # cs_page_anchor: 954a3325349d180fd0ff
        cs_mt "Нет."
        cs_mt "И подписи нет."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        cs_mz "Можно переписать?"
        $ cs_d5_focus("mt")
        with cs_sprite_change
        # cs_page_anchor: 14e6a908d622f955a465
        cs_mt "Переписывайте."
        cs_mt "Саму ведомость пока оставлю у себя."
        cs_narrator "Я достала блокнот."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: b9b13eb0d2a81e9c4a87
        cs_ls "Наконец-то документация."
        cs_ls "А то автобус есть, загадки есть, а нормальной инструкции никто не выдал."
        $ cs_d5_repeat_trip_record = True
    else:
        $ cs_d5_focus("mt")
        with cs_sprite_change
        # cs_page_anchor: e7fe4dbb1b382da993f8
        cs_mt "Я ещё раз проверю архивные папки."
        cs_mt "Возможно, там осталось что-нибудь полезное."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Только, пожалуйста, не ходите в старый корпус одна."
        cs_narrator "Она посмотрела на меня."
        $ cs_d5_focus("mt")
        with cs_sprite_change
        cs_mt "Это ты сейчас меня предупреждаешь?"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Учусь на собственных ошибках."
        $ cs_d5_repeat_trip_record = False
    cs_narrator "Мы закончили разговор."
    cs_narrator "Ольга Дмитриевна сложила документы в папку."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: b6326f9900ef4169fefb
    cs_mt "Если хотите, можете осмотреть остановку."
    cs_mt "Только держитесь возле ворот и сразу возвращайтесь, если появится что-нибудь необычное."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Хорошо."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Далеко не пойдём."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Особенно ты, Соколова."
    cs_narrator "Я посмотрела на неё."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Удивительно, как быстро у меня появилась репутация."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Ты старательно работала."
    cs_narrator "Спорить было трудно."
    $ cs_d5_room("bg ext_house_of_mt_day")
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.35)
    cs_narrator "Мы попрощались и вышли наружу."
    cs_narrator "Семён закрыл за нами дверь."
    cs_narrator "Я посмотрела в сторону ворот."
    cs_narrator "Утро начиналось слишком спокойно."
    cs_narrator "Теперь хотелось проверить, не закончилась ли эта спокойная часть окончательно."
    return
