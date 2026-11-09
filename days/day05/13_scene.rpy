# -*- coding: utf-8 -*-
label cs_day05_13:
    $ cs_d5_scene = 13
    $ save_name = "Чужая смена — День 5: Музыкальный клуб"
    $ cs_bus_scene_enter(13)
    $ cs_d5_room("bg ext_musclub_day")
    with Dissolve(0.7)
    $ cs_d5_room("bg ext_musclub_day")
    cs_narrator "У музыкального клуба Алиса остановилась."
    cs_narrator "Провод в её руках окончательно запутался."
    cs_narrator "Она посмотрела на него с таким выражением, словно собиралась выбросить в ближайшие кусты."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Да что ж такое!"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Давай помогу."
    cs_narrator "Он взял один конец."
    cs_narrator "Алиса осторожно потянула другой."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Приятно видеть проблему, которую действительно можно решить."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Причём без старых архивов."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f4b028b11dfe09215cd6
    cs_ls "И без автобусов."
    cs_ls "Почти праздник."
    cs_narrator "Алиса посмотрела на нас."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Вы меня всё больше пугаете."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Сейчас испугаешься по-настоящему."
    # cs_page_anchor: 6ef3679305ad9418e576
    cs_narrator "Пока Семён держал провод, я коротко рассказала про утро."
    cs_narrator "Без подробностей: автобус у ворот, пустое место водителя, голос из салона."
    cs_narrator "Алиса перестала тянуть свой конец."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Без водителя?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Мы все видели."
    cs_narrator "Алиса помолчала."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    # cs_page_anchor: 6878af590a4ef06f254e
    cs_dv "Мику утром тоже какая-то странная была."
    cs_dv "Всё про сон рассказывала."
    cs_dv "Я не слушала."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Теперь послушаешь?"
    $ cs_d5_focus("dv")
    with cs_sprite_change
    # cs_page_anchor: ac4da972dd431764bcb4
    cs_dv "Ладно."
    cs_dv "Только при ней не делайте такие лица."
    cs_narrator "Наконец провод удалось распутать."
    $ cs_d5_room("bg int_musclub_day")
    cs_narrator "Мы вошли."
    cs_narrator "Мику сидела за пианино и что-то записывала в нотную тетрадь."
    cs_narrator "Увидев нас, она оживилась."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 0398227ed24783ef6042
    cs_mi "О, вы пришли!"
    cs_mi "Даша, посмотри, пожалуйста!"
    cs_mi "Тут переход между двумя частями, и он у меня всё время разваливается, хотя я вроде всё записала."
    cs_narrator "Даша подошла к инструменту."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Покажи, где именно сбиваешься."
    cs_narrator "Мику открыла тетрадь."
    cs_narrator "Провела пальцем по строчке."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: fbee521f18bb1ae49047
    cs_mi "Вот здесь."
    cs_mi "Сначала всё нормально, а потом я ускоряюсь."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Давай попробуем медленнее."
    cs_narrator "Она села рядом."
    play music cs_miku_piano_track fadein 0.5
    cs_narrator "Мику сыграла несколько тактов."
    cs_narrator "Даша послушала."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: c0b1d3e2ac1ffd1e80a1
    cs_da "Здесь не нужно торопиться."
    cs_da "Попробуй чуть задержаться перед переходом."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 7cb51c5597ca8e3328f6
    cs_mi "А, поняла!"
    cs_mi "Сейчас!"
    cs_narrator "Она повторила."
    cs_narrator "На этот раз получилось ровнее."
    stop music fadeout 0.5
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 036175750850850bf68e
    cs_mi "Вот!"
    cs_mi "Спасибо!"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Пожалуйста."
    if cs_mi_followup_invitation_day3:
        cs_narrator "Мику вдруг всплеснула руками."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        # cs_page_anchor: c455e80e12628288288b
        cs_mi "Ой!"
        cs_mi "Вступление!"
        cs_mi "Вы же вчера обещали послушать оба варианта!"
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: 1e194bc2269ee3a6c481
        cs_dv "Четыре такта, Мику."
        cs_dv "Речь идёт о четырёх тактах."
        play music cs_miku_piano_track fadein 0.5
        cs_narrator "Мику сыграла сначала длинный вариант, потом короткий."
        # cs_page_anchor: abeca38729a9ab119c1d
        cs_narrator "Разница была."
        cs_narrator "Небольшая, но была."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 37d3948bb34ca098672d
        cs_ls "Второй."
        cs_ls "Пауза там всё равно слышна, просто короче."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Алиса, ты слышала?!"
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: ca4a9773e25751738fd2
        cs_dv "Слышала."
        cs_dv "Она за меня."
        stop music fadeout 0.5
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Она сказала, что пауза слышна!"
        cs_narrator "Даша прикрыла рот ладонью, чтобы не рассмеяться."
        $ cs_mi_followup_invitation_day3 = False
        $ cs_d5_miku_intro_heard = True
    cs_narrator "Я устроилась на свободном стуле."
    cs_narrator "Семён остался возле двери."
    cs_narrator "Алиса убрала провод и прислонила гитару к стене."
    cs_narrator "Некоторое время я просто слушала музыку."
    cs_narrator "У Даши действительно хорошо получалось объяснять."
    # cs_page_anchor: 62ec89d1ade2fdf857ab
    cs_narrator "Она не старалась показать, насколько лучше играет сама."
    cs_narrator "Просто находила место, где Мику ошибалась, и спокойно помогала."
    cs_narrator "Я улыбнулась."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Чего довольная?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 68a1d1505892c087c6fc
    cs_ls "Ничего."
    cs_ls "Просто приятно смотреть на людей, которые занимаются нормальным делом."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Ты можешь тоже попробовать."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 6a7f30b3274b7ef3d722
    cs_ls "Нет, спасибо."
    cs_ls "Музыкальное искусство пока переживёт без моего участия."
    cs_narrator "Алиса усмехнулась."
    cs_narrator "Даша поднялась из-за пианино."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Мику, можно кое-что спросить?"
    $ cs_d5_focus("mi")
    with cs_sprite_change
    cs_mi "Конечно."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 8f23f61531e1e3d425cc
    cs_da "Нам сегодня снились странные вещи."
    cs_da "Алиса говорит, тебе тоже что-то приснилось."
    cs_narrator "Мику посмотрела на неё внимательнее."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: a6501b00934e061b0863
    cs_mi "Приснился."
    cs_mi "Только я не уверена, что он связан с вашим."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c6e21710e161121ec5a5
    cs_ls "Расскажи."
    cs_ls "Мы пока просто собираем рассказы."
    cs_narrator "Алиса присела на край стула."
    if cs_friend_dv >= 4:
        $ cs_d5_focus("dv")
        with cs_sprite_change
        cs_dv "Мне тоже кое-что снилось."
        cs_narrator "Я повернулась к ней."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Что именно?"
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: 15cc4d6dc04dbbc34238
        cs_dv "Клуб."
        cs_dv "Я сидела с гитарой, а струн на ней не было."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Совсем?"
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: ae26afa61496c668d707
        cs_dv "Да."
        cs_dv "И у пианино кто-то стоял."
        cs_dv "Не помню кто."
        cs_narrator "Она посмотрела в сторону инструмента."
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: b785ff4d20f4ce4323b3
        cs_dv "Потом музыка оборвалась."
        cs_dv "А мне сказали: «Смена закончилась»."
        cs_narrator "Я немного помолчала."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Спасибо, что рассказала."
        $ cs_d5_focus("dv")
        with cs_sprite_change
        cs_dv "Только не надо теперь объявлять меня пророком."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 19283da165c61edf6692
        cs_ls "Даже не собиралась."
        cs_ls "У нас и так слишком много вакансий."
        cs_narrator "Она хмыкнула."
        $ cs_d5_alisa_dream_full = True
    else:
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: bfb75ad05fc2daa61d89
        cs_dv "Мне тоже снился клуб."
        cs_dv "Но я не понимаю, при чём тут ваш автобус."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Возможно, ни при чём."
        $ cs_d5_focus("dv")
        with cs_sprite_change
        cs_dv "Вот и я так думаю."
        cs_narrator "Она скрестила руки."
        cs_narrator "Подробности рассказывать явно не собиралась."
        cs_narrator "Я не стала настаивать."
        $ cs_d5_alisa_dream_full = False
    cs_narrator "Мику осторожно закрыла нотную тетрадь."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    cs_mi "А мне снилась музыка."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Какая?"
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 4901efe3a65bf2906002
    cs_mi "Я утром попробовала её записать."
    cs_mi "Вот только конец всё время забываю."
    cs_narrator "Она открыла тетрадь снова."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 5ff11141aee65cc165dd
    cs_mi "Сначала я играю."
    cs_mi "Потом кто-то стучит."
    cs_mi "Семь раз."
    cs_narrator "Семён выпрямился."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Семь?"
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: d473fbad4ea590206b46
    cs_mi "Да."
    cs_mi "Я считала."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "А дальше?"
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 2e7fd03e256ce5ac2995
    cs_mi "Открываю дверь клуба."
    cs_mi "И там не крыльцо."
    cs_narrator "Я посмотрела на неё."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "А что?"
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 0b5c5480a0a6aaba9006
    cs_mi "Дорога."
    cs_mi "Как возле ворот."
    cs_narrator "Мы замолчали."
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она тоже слушала очень внимательно."
    if cs_friend_mi >= 4:
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Я могу сыграть начало, если хотите."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Если тебе не трудно."
        cs_narrator "Мику села за пианино."
        cs_narrator "Несколько секунд собиралась с мыслями."
        play music cs_miku_piano_track fadein 0.5
        cs_narrator "Затем сыграла короткую мелодию."
        cs_narrator "Она начиналась спокойно."
        cs_narrator "Потом становилась чуть тревожнее."
        stop music fadeout 0.5
        cs_narrator "На последнем звуке Мику остановилась."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Вот здесь дальше ничего не помню."
        $ cs_d5_focus("da")
        with cs_sprite_change
        # cs_page_anchor: 6a3fd1b0c671dfa15aea
        cs_da "Не пытайся сейчас вспомнить силой."
        cs_da "Ты уже показала достаточно."
        cs_narrator "Мику кивнула."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Я могу вечером прийти и рассказать Ольге Дмитриевне сама."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 9d3b9543cb438ee76bfe
        cs_ls "Хорошо."
        cs_ls "Я скажу ей."
        cs_ls "Она передаст, где и когда."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Тогда я приду."
        $ cs_d5_miku_volunteer = True
    else:
        $ cs_d5_focus("mi")
        with cs_sprite_change
        # cs_page_anchor: 397af68dbd4da7cea963
        cs_mi "Я не очень хочу сейчас играть эту мелодию."
        cs_mi "Можно просто записать?"
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Конечно."
        cs_narrator "Мику взяла карандаш."
        cs_narrator "Несколько минут писала на обороте нотного листа."
        cs_narrator "Затем отдала его Семёну."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Передайте Ольге Дмитриевне, пожалуйста."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Передадим."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "А я пока с Алисой останусь."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 4fbe5797b45143a2d505
        cs_ls "Хорошо."
        cs_ls "Спасибо, что рассказала."
        $ cs_d5_miku_volunteer = False
    stop music fadeout 0.5
    cs_narrator "Даша посмотрела на клавиши."
    cs_narrator "Но играть не стала."
    cs_narrator "Я заметила это."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ты как?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 84d821a7d7dc93312eaa
    cs_da "Нормально."
    cs_da "Просто не хочется сейчас играть самой."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "И не надо."
    cs_narrator "Она посмотрела на меня."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Правда?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 068131d385916fd68458
    cs_ls "Конечно."
    cs_ls "Мы сюда не на концерт пришли."
    cs_narrator "Даша чуть улыбнулась."
    cs_narrator "Алиса сложила провод возле стены."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "В общем, если вам нужен фонарик на вечер, у нас есть один."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Пригодится."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Главное, чтобы у фонарика не оказалось собственного мнения."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Соколова, ты иногда такую ерунду говоришь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Зато бесплатно."
    cs_narrator "Мику тихо рассмеялась."
    cs_narrator "Перед уходом мы помогли ей собрать нотные листы."
    cs_narrator "Даша ещё раз объяснила сложный переход."
    cs_narrator "Мику попробовала повторить его без пианино, просто отбивая ритм пальцами по столу."
    cs_narrator "И неожиданно получилось."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 1ccae4ed047be3f4acf1
    cs_mi "Вот!"
    cs_mi "Теперь запомню!"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Запиши, пока не забыла."
    $ cs_d5_focus("mi")
    with cs_sprite_change
    cs_mi "Точно!"
    cs_narrator "Я посмотрела на неё."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Кажется, у нас сегодня хотя бы одна загадка решена."
    cs_narrator "Мику улыбнулась."
    $ cs_d5_room("cs_camp_path_day")
    cs_narrator "Мы попрощались и вышли из клуба."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Нужно было возвращаться к остальным."
    cs_narrator "Но я поймала себя на том, что немного отдохнула."
    cs_narrator "Даже несмотря на разговоры о снах."
    cs_narrator "Наверное, дело было в музыке."
    cs_narrator "И в том, что кто-то здесь всё ещё мог радоваться удачно сыгранным двум тактам."
    return
