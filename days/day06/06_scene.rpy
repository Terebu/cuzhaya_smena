# -*- coding: utf-8 -*-
label cs_day06_06:
    $ save_name = "Чужая смена — День 6: До ужина"
    $ cs_rev_time("sunset")
    $ cs_d6_room("bg ext_house_of_mt_sunset",['cs_darya', 'mt'])
    cs_narrator "Ольга ждала на крыльце."
    cs_narrator "Увидела нас, посмотрела на часы и только потом спросила:"
    $ cs_d6_focus("mt")
    cs_mt "Ну?"
    cs_narrator "Я протянула конверт."
    $ cs_d6_focus("ls")
    cs_ls "Вернулись вовремя."
    cs_ls "Все конечности при нас."
    cs_ls "Протокол выдающейся экспедиции."
    cs_narrator "Она быстро просмотрела листы, задержалась на датах."
    $ cs_d6_focus("mt")
    cs_mt "Копию оставите мне."
    $ cs_d6_focus("ls")
    cs_ls "Сейчас сделаем."
    cs_narrator "Пока я переписывала, Даша рассказала про коробку."
    cs_narrator "Очень подробно, с выразительными взглядами в мою сторону."
    $ cs_d6_focus("ls")
    cs_ls "Это происшествие не влияет на качество исследования."
    $ cs_d6_focus("da")
    cs_da "На качество тумбочки повлияло."
    cs_narrator "Ольга впервые за день рассмеялась."
    $ cs_d6_olga_copy = True
    $ cs_d6_room("bg int_aidpost_day",['cs_darya', 'cs'])
    cs_narrator "Виоле мы вернули аптечку."
    cs_narrator "Она спросила про локоть, заставила меня несколько раз согнуть руку и велела не устраивать вечером спортивные подвиги."
    $ cs_d6_firstaid_location = "viola"
    $ cs_d6_focus("ls")
    cs_ls "Тогда шахматы?"
    $ cs_d6_focus("vi")
    cs_vi "Желательно без травм."
    $ cs_d6_focus("ls")
    cs_ls "Очень много условий для отдыха."
    cs_narrator "Виола поставила аптечку на место."
    $ cs_d6_focus("vi")
    cs_vi "Вы обе поесть не забудьте."
    cs_vi "Ольга сегодня греет ужин сама, поварихи уже уехали."
    if cs_friend_viola >= 4 and cs_d4_viola_full_trust:
        cs_narrator "Я показала Виоле копии с датами."
        cs_narrator "Она прочла подписи и попросила оставить лист рядом с Ольгиной копией."
        $ cs_d6_focus("vi")
        cs_vi "О причинах пока не гадаю."
        cs_vi "Но это стоит сохранить."
        $ cs_d6_viola_documents_shared = True
    $ cs_d6_think()
    cs_narrator "Вот теперь в лагере действительно оставались только четверо."
    cs_narrator "Даже на кухне больше не было привычного движения."
    $ cs_d6_room("bg ext_aidpost_day",['cs_darya'])
    cs_narrator "Я поблагодарила и вышла вслед за Дашей."
    $ cs_d6_room("cs_camp_path_sunset",['cs_darya'])
    cs_narrator "До ужина мы дошли до воды."
    $ cs_d6_room("cs_d6_pier_sunset",['cs_darya'])
    cs_narrator "На пристани я сняла обувь, села на доски и опустила ноги вниз."
    cs_narrator "Даша устроилась рядом."
    cs_narrator "Она тоже устала: молча отодвинула рюкзак и долго растирала плечо под лямкой."
    cs_narrator "Я нашла у берега плоский камень."
    cs_narrator "Бросила — он один раз подпрыгнул и утонул."
    $ cs_d6_focus("da")
    cs_da "Уверенное начало."
    $ cs_rev_sfx("sound/sfx/water_splash.ogg",0.25)
    $ cs_d6_focus("ls")
    cs_ls "Я проверяла глубину."
    cs_narrator "Она показала, как держать камень, и сама сделала два отскока."
    cs_narrator "На третьем броске у меня получилось столько же."
    $ cs_d6_cg("cs_cg_day06_pier_evening")
    cs_narrator "Я довольно посмотрела на неё."
    $ cs_d6_focus("ls")
    cs_ls "Видишь?"
    cs_ls "Обучаюсь."
    $ cs_d6_focus("da")
    cs_da "У тебя даже свидетель есть."
    cs_narrator "Больше мы камни не искали."
    cs_narrator "Сидели, слушали воду и смотрели, как солнце уходит за деревья."
    $ cs_d6_focus("ls")
    cs_ls "Что первым делом сделаешь дома?"
    cs_narrator "Даша подумала."
    $ cs_d6_focus("da")
    cs_da "Позвоню своим."
    cs_da "Они, наверное, с ума сходят."
    cs_narrator "Я кивнула."
    cs_narrator "У меня от этого простого ответа неприятно сжалось внутри."
    $ cs_d6_focus("ls")
    cs_ls "Я тоже."
    cs_ls "Потом в душ."
    cs_ls "Потом заряжать телефон и проверять дату."
    $ cs_d6_focus("da")
    cs_da "В таком порядке?"
    $ cs_d6_focus("ls")
    cs_ls "Телефон можно поставить раньше."
    cs_ls "Я гибкая."
    cs_narrator "Даша усмехнулась, но почти сразу снова стала серьёзной."
    $ cs_d6_focus("da")
    cs_da "Лишь бы наш год."
    $ cs_d6_focus("ls")
    cs_ls "Две тысячи двадцать шестой."
    $ cs_d6_focus("ls")
    cs_ls "Пока ещё мой любимый из доступных."
    $ cs_d6_focus("da")
    cs_da "Ещё недавно жаловалась."
    $ cs_d6_focus("ls")
    cs_ls "Я не знала, с чем сравнивать."
    cs_narrator "Она опустила пятку в воду и тут же отдёрнула."
    $ cs_d6_focus("da")
    cs_da "Холодная."
    $ cs_d6_focus("ls")
    cs_ls "Вот."
    cs_ls "Ещё один повод вернуться к горячему душу."
    $ cs_d6_room("cs_d6_pier_sunset",['cs_darya'])
    cs_narrator "Мы посидели немного и пошли обратно."
    cs_narrator "Я надела обувь, стряхнув с подошвы песок."
    $ cs_d6_room("bg ext_house_of_mt_sunset",['cs_darya', 'mt', 'cs'])
    $ cs_rev_sfx("sound/sfx/paper_bag.ogg",0.23)
    cs_narrator "У домика Ольги уже стояли чашки."
    cs_narrator "Виола принесла колоду карт."
    $ cs_d6_focus("vi")
    cs_vi "На полчаса."
    $ cs_d6_focus("vi")
    cs_vi "Потом ужин."
    cs_narrator "Я села за стол."
    $ cs_d6_focus("ls")
    cs_ls "Наконец-то мероприятие, к которому у меня нет вопросов."
    $ cs_d6_cg("cs_cg_day06_cards_four")
    cs_narrator "Вопросы появились после первой раздачи."
    cs_narrator "Виола выигрывала слишком уверенно."
    cs_narrator "Даша пару раз просила напомнить правила, я один раз торжественно побила карту не той мастью."
    $ cs_d6_focus("mt")
    cs_mt "Это нельзя."
    $ cs_d6_focus("ls")
    cs_ls "А если очень убедительно?"
    $ cs_d6_focus("mt")
    cs_mt "Всё равно нельзя."
    $ cs_d6_focus("ls")
    cs_ls "Как у вас тут всё устроено…"
    cs_narrator "Я забрала карты обратно."
    cs_narrator "Даша смеялась, не пытаясь скрыть."
    cs_narrator "Когда я снова проиграла, попросила реванш."
    cs_narrator "Виола согласилась — и закончила вторую партию быстрее первой."
    $ cs_d6_focus("ls")
    cs_ls "Научите так же."
    $ cs_d6_focus("vi")
    cs_vi "Сначала научись смотреть, что уже вышло."
    $ cs_d6_room("bg ext_house_of_mt_sunset",['cs_darya', 'mt', 'cs'])
    cs_narrator "Я собрала карты в ровную стопку."
    $ cs_d6_focus("ls")
    cs_ls "Сегодня все хотят, чтобы я что-нибудь запоминала."
    cs_narrator "На этот раз шутка никого не смутила."
    cs_narrator "Ольга поднялась поставить ужин греться, а мы помогли убрать со стола."
    return
