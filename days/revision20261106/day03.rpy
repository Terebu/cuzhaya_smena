# -*- coding: utf-8 -*-
label cs_rev_d3_01:
    $ cs_rev_begin(3,1,['sl'])
    $ save_name = "Чужая смена — День 3: Раньше горна"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_house_lena_darya_int_day")
    stop music fadeout 1.5
    cs_narrator "Проснулась я раньше горна."
    # cs_page_anchor: 4bfb5595d2aec5ee2e8d
    cs_narrator "Сначала даже не поняла почему."
    cs_narrator "Потом пошевелила рукой, и локоть немедленно напомнил о вчерашнем падении на дороге."
    # cs_page_anchor: bd323e5249e4fd8791de
    cs_narrator "Ах да."
    cs_narrator "Пространственная петля и асфальт у ворот."
    cs_narrator "Отличное сочетание."
    # cs_page_anchor: fff263439903ea0cb818
    cs_narrator "Я села и посмотрела на повязку."
    cs_narrator "Виола наложила её аккуратно, но под бинтом всё ещё ныло."
    cs_narrator "Даша спала на своей кровати, натянув одеяло до подбородка."
    # cs_page_anchor: 35442d664312d5dc85b9
    cs_narrator "Вчера вечером я спросила, можно ли лечь рядом."
    cs_narrator "Она отказала — спокойно, без обиды."
    cs_narrator "Сказала, что ей пока нужно своё место."
    # cs_page_anchor: 597207932ad77a0955a6
    cs_narrator "Я это помнила."
    cs_narrator "И не собиралась делать вид, что не помню."
    cs_narrator "Я тихо оделась, придерживая больную руку, и нашла на столе карандаш."
    cs_narrator "«Ушла прогуляться по лагерю. Никаких дорог за воротами. Честно. Лена»."
    cs_narrator "Подумала и подчеркнула «честно»."
    cs_narrator "После вчерашнего Даша имела полное право мне не верить."
    $ cs_rev_room('bg ext_square_day')
    # cs_page_anchor: c5ac04ef318d64afee1f
    cs_narrator "Лагерь ещё спал."
    cs_narrator "Туман лежал над дорожками, на скамейках блестела роса."
    $ cs_rev_room('bg ext_playground_day')
    cs_narrator "На спортивной площадке я по привычке попробовала перейти на бег."
    # cs_page_anchor: 7e757a23d5af5db3a935
    cs_narrator "Три шага."
    cs_narrator "Локоть дёрнуло так, что я остановилась."
    # cs_page_anchor: edfe2db0806d9dab45ad
    cs_narrator "Ладно."
    cs_narrator "Сегодня у нас оздоровительная прогулка."
    $ cs_rev_sfx('<from 0.0 to 0.7>sound/sfx/bus_idle.ogg',0.12)
    cs_narrator "Где-то далеко, за лесом, со стороны ворот, послышался звук мотора."
    # cs_page_anchor: 0aaea1536b43aa0f346a
    cs_narrator "Низкий, ровный."
    cs_narrator "Как у автобуса."
    cs_narrator "Я замерла и прислушалась."
    cs_narrator "Звук прокатился по верхушкам деревьев и стих."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: c55e404855efbe7c280a
    cs_sl "Лена?"
    cs_sl "Ты сегодня рано."
    # cs_page_anchor: c03c58bec47ac79f433c
    cs_narrator "Славя шла от столовой с папкой под мышкой."
    cs_narrator "Даже в такую рань она выглядела так, будто уже успела выполнить половину дневного плана."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 20880ad1d6010d00b36c
    cs_ls "Доброе утро."
    cs_ls "Ты тоже слышала мотор?"
    $ cs_rev_focus("sl")
    with cs_sprite_change
    cs_sl "Какой мотор?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d30a56d1c925089c5b15
    cs_ls "Со стороны ворот."
    cs_ls "Как будто автобус."
    cs_narrator "Славя посмотрела в сторону леса."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: 8ba7cd11eeaa45711cdf
    cs_sl "Автобус до конца смены не приходит."
    cs_sl "Может, грузовик с продуктами?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "В пять утра?"
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: 7d21ac5b5b0d155b0051
    cs_sl "Бывает."
    cs_sl "Наверное."
    # cs_page_anchor: e971fd006320c60e2757
    cs_narrator "Она сказала это слишком быстро."
    cs_narrator "Будто не хотела об этом думать."
    # cs_page_anchor: 9c11023749fa61bda578
    cs_narrator "Я тоже решила не думать."
    cs_narrator "По крайней мере, пока."
    if cs_friend_sl >= 1:
        cs_narrator "Славя открыла папку."
        $ cs_rev_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: 92a1fdd909f847af2c8d
        cs_sl "Кстати, смотри."
        cs_sl "Я сохранила."
        # cs_page_anchor: 4592731a13c9b6f17350
        cs_narrator "Внутри лежал наш вчерашний плакат о музыкальном вечере."
        cs_narrator "Тот самый, над которым мы втроём сидели ещё до моего падения."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Его же собирались снять вместе с остальным."
        $ cs_rev_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: 91478713c8367f184a80
        cs_sl "Сняли."
        cs_sl "Но выбрасывать было жалко."
        cs_sl "Он хороший."
        cs_sl "Заберёшь потом, ладно?"
        cs_sl "Сейчас у меня руки заняты."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 4e77ed9b8d6c567c32a6
        cs_ls "Спасибо, Славя."
        cs_ls "Правда."
        # cs_page_anchor: 48a261355cfebd3e8014
        cs_narrator "Странное чувство."
        cs_narrator "В Москве мои рисунки видели тысячи людей."
        cs_narrator "А тут одна девушка не стала выбрасывать плакат — и это почему-то было приятнее."
        $ cs_sl_poster_saved_day3 = True
    else:
        $ cs_rev_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: 560d8c744d46f77653fc
        cs_sl "Плакаты после концерта я уже сняла."
        cs_sl "Ваш тоже."
        cs_sl "Аккуратно, не волнуйся."
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    cs_narrator "Над лагерем прозвучал горн."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: b981b214332011cf3fb1
    cs_sl "Всё, побежала."
    cs_sl "И руку береги!"
    cs_narrator "Я помахала ей здоровой рукой и пошла обратно к домику."
    return

label cs_rev_d3_02:
    $ cs_rev_begin(3,2,['cs_darya', 'cs_semen'])
    $ save_name = "Чужая смена — День 3: Двадцать секунд самоконтроля"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_house_lena_darya_int_day")
    $ cs_rev_darya_offscreen = True
    $ cs_rev_sfx('sound/sfx/open_door_1.ogg',0.35)
    cs_narrator "Я открыла дверь."
    cs_narrator "Даша стояла посреди комнаты и как раз натягивала рубашку."
    cs_narrator "Я развернулась к двери быстрее, чем успела подумать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Лена!"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 8bbce2386e2e57296a28
    cs_ls "Я ничего не видела."
    cs_ls "Я смотрю на дверь."
    cs_ls "Дверь очень интересная."
    cs_ls "Деревянная."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Стучаться не пробовала?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Это мой собственный домик."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Наш домик."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ec40a0466e7e2685f979
    cs_ls "Наш."
    cs_ls "Согласна."
    cs_ls "Признаю ошибку."
    # cs_page_anchor: 528b2e86c84703193796
    cs_narrator "За спиной шуршала ткань."
    cs_narrator "Двадцать секунд я изучала дверные петли так внимательно, будто собиралась их рисовать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 7bf395078a3bd8a1366a
    cs_da "Всё."
    cs_da "Можешь поворачиваться."
    $ cs_rev_darya_offscreen = False
    # cs_page_anchor: ab6157372f1575da38a0
    cs_narrator "Даша уже застёгивала верхнюю пуговицу."
    cs_narrator "Щёки у неё были чуть розовее обычного."
    cs_narrator "У меня, подозреваю, тоже."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 5c5e1c061fb02cf0c22d
    cs_da "Записку я нашла."
    cs_da "«Честно» подчёркнуто."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Это был важный юридический момент."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Как рука?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 91fd2684a4545baa8480
    cs_ls "Бегать отказывается."
    cs_ls "Ходить согласна."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Хоть кто-то из вас благоразумный."
    cs_narrator "Она посмотрела на меня внимательнее."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 86c85c419bb8e920f00e
    cs_da "И, Лен."
    cs_da "Давай договоримся."
    cs_da "Стучать."
    cs_da "Обеим."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 227d957aef2750c4ec8b
    cs_ls "Договорились."
    cs_ls "И… тебе идёт форма."
    cs_ls "Это просто наблюдение художника."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Художника, который двадцать секунд смотрел на дверь."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c88984ce0445a854d641
    cs_ls "Двадцать секунд самоконтроля."
    cs_ls "Почти рекорд."
    cs_narrator "Даша рассмеялась, и неловкость прошла."
    $ cs_rev_room('cs_camp_path_day')
    $ cs_rev_music(cs_day_music_daily,0.16,2.5)
    # cs_page_anchor: 60978771aca3eaba0020
    cs_narrator "По дороге к столовой мы встретили Семёна."
    cs_narrator "Он шёл медленно, с таким видом, будто его разбудили на полчаса раньше, чем было бы гуманно."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Доброе."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 66b01ef84d9da5260e77
    cs_ls "Доброе утро."
    cs_ls "Выглядишь, как будто всю ночь чинил бетономешалку."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Спал плохо."
    # cs_page_anchor: ab9263e121a3ecdefdbb
    cs_narrator "Он сказал это без раздражения."
    cs_narrator "Просто устало."
    if "3:1" in cs_rev_choices:
        if cs_rev_choices["3:1"]==0:
            $ cs_rev_choice(3,1,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Что-то случилось?"
            # cs_page_anchor: 1383be1592e9b836f3f3
            cs_narrator "Семён посмотрел на нас."
            cs_narrator "Потом в сторону ворот."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 7cd29cf5d9575645bb9a
            cs_sy "После вчерашней дороги."
            cs_sy "Закрываю глаза — и снова иду по ней."
            cs_sy "Иду, иду, а впереди опять лагерь."
            cs_narrator "Даша поёжилась."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Мне тоже было не по себе."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: fd18308d0e3a018be934
            cs_ls "И мне."
            cs_ls "Если честно, я сегодня тоже проснулась раньше, чем хотела."
            cs_narrator "Семён удивлённо поднял брови."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: d90390d299c1227d388e
            cs_sy "Ты?"
            cs_sy "Я думал, ты из всего делаешь анекдот."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 8480411869fd29a3d94e
            cs_ls "Из всего, что можно."
            cs_ls "Петля в анекдот пока не складывается."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 35fe23cc58deed6fba3d
            cs_sy "Ладно."
            cs_sy "Если опять начнётся — скажу."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 14073b003785850a6e3b
            cs_ls "И я скажу."
            cs_ls "Договорились?"
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Договорились."
            $ cs_rev_award("3:1:cs_friend_se","cs_friend_se",1)
            $ cs_rev_finish_choice(3,1)
        else:
            $ cs_rev_choice(3,1,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 6c54adb0ee4b567d36dd
            cs_ls "Тогда тебе срочно нужен чай."
            cs_ls "Не будем задерживать."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Вот это разумно."
            cs_narrator "Он кивнул и пошёл к столовой."
            $ cs_rev_finish_choice(3,1)
    else:
        menu:
            "Спросить Семёна, как у него дела":
                $ cs_rev_choice(3,1,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Что-то случилось?"
                # cs_page_anchor: 5dd9917462d6c4b466b6
                cs_narrator "Семён посмотрел на нас."
                cs_narrator "Потом в сторону ворот."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 408a25ea9d5081acda61
                cs_sy "После вчерашней дороги."
                cs_sy "Закрываю глаза — и снова иду по ней."
                cs_sy "Иду, иду, а впереди опять лагерь."
                cs_narrator "Даша поёжилась."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Мне тоже было не по себе."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: aed1c0c9a08f33740cc5
                cs_ls "И мне."
                cs_ls "Если честно, я сегодня тоже проснулась раньше, чем хотела."
                cs_narrator "Семён удивлённо поднял брови."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 1e278159fc8d9e2f2629
                cs_sy "Ты?"
                cs_sy "Я думал, ты из всего делаешь анекдот."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 5222a6431bcd4ee54df0
                cs_ls "Из всего, что можно."
                cs_ls "Петля в анекдот пока не складывается."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: d66e88ec2ff2c4915191
                cs_sy "Ладно."
                cs_sy "Если опять начнётся — скажу."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: f928310ffa8671e9ebb9
                cs_ls "И я скажу."
                cs_ls "Договорились?"
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Договорились."
                $ cs_rev_award("3:1:cs_friend_se","cs_friend_se",1)
                $ cs_rev_finish_choice(3,1)
            "Не задерживать его перед завтраком":
                $ cs_rev_choice(3,1,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: e83fe8c6c1d94e00fa7c
                cs_ls "Тогда тебе срочно нужен чай."
                cs_ls "Не будем задерживать."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Вот это разумно."
                cs_narrator "Он кивнул и пошёл к столовой."
                $ cs_rev_finish_choice(3,1)
    # cs_page_anchor: 26aec46009b71309f937
    cs_narrator "Семён ушёл вперёд."
    cs_narrator "Я посмотрела ему вслед."
    # cs_page_anchor: 1fe7290f155c7f292485
    cs_narrator "Плохо спал."
    cs_narrator "После дороги."
    # cs_page_anchor: eb84a83d233c550fcccc
    cs_narrator "Я вспомнила утренний мотор за лесом и решила пока ничего не говорить."
    cs_narrator "Без доказательств это звучало бы как очередная моя шутка."
    cs_narrator "Только несмешная."
    return

label cs_rev_d3_03:
    $ cs_rev_begin(3,3,['cs_darya', 'cs_zhenya'])
    $ save_name = "Чужая смена — День 3: Место у окна"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_dining_hall_people_day")
    # cs_page_anchor: c32248b5e13120ef3611
    cs_narrator "Женя сидела у окна с книгой и чашкой чая."
    cs_narrator "В столовой, где все кричали, толкались и спорили из-за хлеба, вокруг неё каким-то образом сохранялась тишина."
    if cs_friend_mz <= 0:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Доброе утро."
        # cs_page_anchor: 4c33e73fcbde9ec66236
        cs_narrator "Она кивнула и снова уткнулась в книгу."
        cs_narrator "Мы сели за соседний стол."
    elif cs_friend_mz == 1:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: fb577647bb2759a1b6fc
        cs_mz "Доброе утро."
        cs_mz "Можете сесть, если не будете шуметь."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Мы будем образцом тишины."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Посмотрим."
    else:
        cs_narrator "Женя подняла глаза и сама отодвинула свободный стул."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: cf7080727e4159a64615
        cs_mz "Садитесь."
        cs_mz "Как рука?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: cbdcd1722b47f14e3e15
        cs_ls "Держится."
        cs_ls "Спасибо, что спросила."
    # cs_page_anchor: 6aac48edab50ce0a53a7
    cs_narrator "Мы ели кашу."
    cs_narrator "Женя читала."
    cs_narrator "Даша рассказывала, как ночью к ней в окно стучалась ветка, а она полчаса не могла понять, что это."
    if cs_mz_map_lead:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: bf3c2704c1258a4151be
        cs_mz "Про каталоги я не забыла."
        cs_mz "После медпункта заходите в библиотеку."
        cs_mz "Только ничего не обещаю."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Каталоги — уже больше, чем у нас есть."
    if "3:2" in cs_rev_choices:
        if cs_rev_choices["3:2"]==0:
            $ cs_rev_choice(3,2,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 41969c23192271978308
            cs_ls "Жень, а что бы ты посоветовала почитать?"
            cs_ls "Не для учёбы."
            cs_ls "Для себя."
            cs_narrator "Женя посмотрела на меня поверх очков."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "Ты серьёзно спрашиваешь?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 689f10140b835991c040
            cs_ls "Абсолютно."
            cs_ls "Мне нужна книга, в которой никто не попадает в пионерлагерь из другого года."
            cs_narrator "Женя едва заметно улыбнулась."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: b283cec2f6e8ec84a3e3
            cs_mz "Тогда Гончаров."
            cs_mz "«Обыкновенная история»."
            cs_mz "Про молодого человека, который приезжает в столицу с большими ожиданиями."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "И что с ним случается?"
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: ac94b45613b7fa4e4250
            cs_mz "Жизнь."
            cs_mz "Подберу после обеда."
            $ cs_rev_award("3:2:cs_friend_mz","cs_friend_mz",1)
            $ cs_mz_book_requested_day3 = True
            $ cs_rev_finish_choice(3,2)
        else:
            $ cs_rev_choice(3,2,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: c1011f4ad126510402b4
            cs_ls "Не будем мешать."
            cs_ls "Хорошего утра, Жень."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "И вам."
            $ cs_rev_finish_choice(3,2)
    else:
        menu:
            "Спросить Женю, какую книгу она посоветовала бы":
                $ cs_rev_choice(3,2,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: b67452b24b313b0012a0
                cs_ls "Жень, а что бы ты посоветовала почитать?"
                cs_ls "Не для учёбы."
                cs_ls "Для себя."
                cs_narrator "Женя посмотрела на меня поверх очков."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "Ты серьёзно спрашиваешь?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: b0795b7382dcbd79d91b
                cs_ls "Абсолютно."
                cs_ls "Мне нужна книга, в которой никто не попадает в пионерлагерь из другого года."
                cs_narrator "Женя едва заметно улыбнулась."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: 073520542248d9ef3bd6
                cs_mz "Тогда Гончаров."
                cs_mz "«Обыкновенная история»."
                cs_mz "Про молодого человека, который приезжает в столицу с большими ожиданиями."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "И что с ним случается?"
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: 71a20a4d667355d32b30
                cs_mz "Жизнь."
                cs_mz "Подберу после обеда."
                $ cs_rev_award("3:2:cs_friend_mz","cs_friend_mz",1)
                $ cs_mz_book_requested_day3 = True
                $ cs_rev_finish_choice(3,2)
            "Не задерживать Женю перед её делами":
                $ cs_rev_choice(3,2,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 8868d6ca7caede62b8ae
                cs_ls "Не будем мешать."
                cs_ls "Хорошего утра, Жень."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "И вам."
                $ cs_rev_finish_choice(3,2)
    cs_narrator "Женя закрыла книгу и встала."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Мне пора открывать библиотеку."
    cs_narrator "Уже у двери она остановилась и обернулась."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 2af0300e7195b9c605c5
    cs_mz "Соколова."
    cs_mz "Вы вчера правда ходили по дороге к воротам?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Правда."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 137de0e6e80383353ad0
    cs_mz "В библиотеке есть старые каталоги."
    cs_mz "Говорят, остальной архив лагеря так и остался в старом корпусе."
    cs_mz "Я бы туда не ходила."
    cs_narrator "И ушла, не дожидаясь ответа."
    cs_narrator "Я посмотрела на Дашу."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Даже не думай."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Я ничего не говорила."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты думала очень громко."
    return

label cs_rev_d3_04:
    $ cs_rev_begin(3,4,['cs', 'cs_darya'])
    $ save_name = "Чужая смена — День 3: Медпункт"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_aidpost_day")
    $ cs_rev_music(cs_day_music_friends,0.14,2.5)
    cs_narrator "Виола встретила нас так, будто ожидала увидеть меня ещё раньше."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 5984c76cbf98e7a13257
    cs_vi "Соколова."
    cs_vi "Садись."
    cs_vi "Даша, ты тоже можешь сесть, раз уж охраняешь пациента."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Охраняю."
    cs_narrator "Виола размотала повязку и внимательно осмотрела ссадину."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 72d0df5b04b88741b0e4
    cs_vi "Заживает."
    cs_vi "Медленно, но заживает."
    cs_vi "Турник?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ни в коем случае."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Бег?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 8236026404b15340422a
    cs_ls "Попробовала."
    cs_ls "Три шага."
    cs_ls "Больше не буду."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Хотя бы честно."
    # cs_page_anchor: d847c2337ac7c0a6292d
    cs_narrator "Она обработала ссадину и начала накладывать свежий бинт."
    cs_narrator "Потом на секунду остановилась."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    cs_vi "Странно."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Что?"
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: 6a0acfc800d58a1573b8
    cs_vi "Мне показалось, что я уже перевязывала тебе этот локоть."
    cs_vi "Давно."
    cs_vi "Ещё до смены."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Я здесь третий день."
    $ cs_rev_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: a927ad2156db8be55695
    cs_vi "Знаю."
    cs_vi "Путаю, наверное."
    cs_vi "Устала."
    # cs_page_anchor: 37c3c6968d6dca864edd
    cs_narrator "Она закончила повязку."
    cs_narrator "Но ещё несколько секунд смотрела на мою руку так, словно пыталась вспомнить что-то очень важное."
    # cs_page_anchor: 0085d4d71e47cbb58716
    cs_narrator "На столе стояли коробки с бинтами и пузырьками."
    cs_narrator "Виола вздохнула над ними, как над личным врагом."
    $ cs_rev_viola_before = cs_friend_viola
    if "3:3" in cs_rev_choices:
        if cs_rev_choices["3:3"]==0:
            $ cs_rev_choice(3,3,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 60b8b0d85a060e409041
            cs_ls "Можем помочь посчитать."
            cs_ls "Одной рукой я тоже умею считать."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: f8deee319941ec720da8
            cs_vi "Только запечатанные упаковки."
            cs_vi "Ничего не открывать."
            cs_vi "Тяжёлое не поднимать."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Тяжёлое — я."
            $ cs_rev_room('cs_cg_lena_darya_medical_inventory_day')
            # cs_page_anchor: fa04cc99fff4b0a0e172
            cs_narrator "Мы пересчитали бинты, вату и пузырьки с зелёнкой."
            cs_narrator "Даша диктовала, я записывала."
            cs_narrator "Виола проверяла."
            $ cs_rev_room('bg int_aidpost_day')
            $ cs_rev_focus("vi")
            with cs_sprite_change
            # cs_page_anchor: c974dc08546abc2e2fc8
            cs_vi "Быстро."
            cs_vi "Спасибо."
            cs_vi "Заходите, если что — не только когда что-нибудь сломаете."
            $ cs_rev_award("3:3:cs_friend_viola","cs_friend_viola",1)
            $ cs_rev_finish_choice(3,3)
        else:
            $ cs_rev_choice(3,3,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: cc1896d2fa1357849b08
            cs_ls "Спасибо, Виола."
            cs_ls "Не будем мешать."
            $ cs_rev_focus("vi")
            with cs_sprite_change
            cs_vi "Береги руку."
            $ cs_rev_finish_choice(3,3)
    else:
        menu:
            "Предложить помочь пересчитать запасы":
                $ cs_rev_choice(3,3,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 6c8f116128ce84c353ac
                cs_ls "Можем помочь посчитать."
                cs_ls "Одной рукой я тоже умею считать."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: a3d3049c712934c6faf8
                cs_vi "Только запечатанные упаковки."
                cs_vi "Ничего не открывать."
                cs_vi "Тяжёлое не поднимать."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Тяжёлое — я."
                $ cs_rev_room('cs_cg_lena_darya_medical_inventory_day')
                # cs_page_anchor: f48003ee2d5fccfd66b4
                cs_narrator "Мы пересчитали бинты, вату и пузырьки с зелёнкой."
                cs_narrator "Даша диктовала, я записывала."
                cs_narrator "Виола проверяла."
                $ cs_rev_room('bg int_aidpost_day')
                $ cs_rev_focus("vi")
                with cs_sprite_change
                # cs_page_anchor: b00dfe5ee38ddfb6d7d0
                cs_vi "Быстро."
                cs_vi "Спасибо."
                cs_vi "Заходите, если что — не только когда что-нибудь сломаете."
                $ cs_rev_award("3:3:cs_friend_viola","cs_friend_viola",1)
                $ cs_rev_finish_choice(3,3)
            "Поблагодарить и не задерживать Виолу":
                $ cs_rev_choice(3,3,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: d24d8003109b25ff8798
                cs_ls "Спасибо, Виола."
                cs_ls "Не будем мешать."
                $ cs_rev_focus("vi")
                with cs_sprite_change
                cs_vi "Береги руку."
                $ cs_rev_finish_choice(3,3)
    if cs_rev_viola_before >= 2:
        cs_narrator "Виола достала из шкафа небольшой свёрток."
        $ cs_rev_focus("vi")
        with cs_sprite_change
        # cs_page_anchor: 7da836dac42fc3027daf
        cs_vi "Возьми."
        cs_vi "Запасной бинт и пластырь."
        cs_vi "Если повязка намокнет — меняй, а не терпи."
        $ cs_viola_spare_dressing_day3 = True
    $ cs_rev_room('bg ext_aidpost_day')
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.25)
    cs_narrator "Мы вышли из медпункта на солнце."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Она странно на тебя смотрела."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 03bd66fe377cf949c5a5
    cs_ls "На мой локоть."
    cs_ls "Видимо, он у меня очень запоминающийся."
    cs_narrator "Но шутка опять не получилась."
    return

label cs_rev_d3_05:
    $ cs_rev_begin(3,5,['cs_darya', 'cs_semen', 'mt', 'sl'])
    $ save_name = "Чужая смена — День 3: Поручение вожатой"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_house_of_mt_day")
    $ cs_rev_music(cs_day_music_daily,0.18,2.5)
    cs_narrator "У домика вожатой Ольга Дмитриевна разбирала бумаги прямо на крыльце."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2004c7ca87e0a76116f3
    cs_ls "Доброе утро."
    cs_ls "Можем чем-нибудь помочь?"
    cs_narrator "Вожатая посмотрела на меня так, будто я предложила ей прыгнуть с парашютом."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: a00d0f221432731d35bd
    cs_mt "Соколова добровольно предлагает помощь."
    cs_mt "Что с тобой?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ea3abf63bfaf832a11e0
    cs_ls "Локоть."
    cs_ls "Он делает меня ответственнее."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Как он?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Виола говорит, заживает."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 7a56d58e7b99a13d3492
    cs_mt "Хорошо."
    cs_mt "Тогда отнесите эту папку в администрацию."
    cs_mt "Даша, неси ты."
    cs_mt "А потом, если будет время, помогите Славе на складе."
    cs_narrator "Даша взяла папку."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 3493d3e2e508b32350cb
    cs_mt "И, Лена."
    cs_mt "Про вчерашнюю дорогу."
    cs_mt "За ворота без меня — ни шагу."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Даже не собиралась."
    $ cs_rev_focus("mt")
    with cs_sprite_change
    cs_mt "Именно это меня и беспокоит."
    # cs_page_anchor: a9b720e889f63ae2ad8a
    cs_narrator "Из домика вышел Семён с полотенцем на плече."
    cs_narrator "Увидел нас и замедлил шаг."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: f2b5ab657d503e36f1fd
    cs_ls "О. А вот и ваш самый образцовый жилец."
    cs_ls "Ольга Дмитриевна, он вам не мешает по утрам?"
    cs_ls "Не поёт в умывальнике?"
    $ cs_rev_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: b7b144b7e006075c1f78
    cs_mt "Лена."
    cs_mt "Хватит."
    cs_narrator "Сказано было спокойно, но так, что продолжать не захотелось."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 49c481ecaae3a31b32c6
    cs_ls "Поняла."
    cs_ls "Молчу."
    $ cs_rev_room('cs_int_administration_day')
    # cs_page_anchor: d872bae465dc6a686fc0
    cs_narrator "В администрации пахло бумагой и пылью."
    cs_narrator "Пожилая женщина за столом приняла папку, не поднимая головы."
    cs_narrator "Пока она расписывалась, я рассматривала стену."
    # cs_page_anchor: 12df16462161228cd43f
    cs_narrator "Расписание кружков."
    cs_narrator "График дежурств."
    cs_narrator "И пожелтевший машинописный лист, приколотый, кажется, ещё до моего рождения."
    cs_narrator "«Рейс № 410. Заезд — день первый. Отъезд — день седьмой»."
    cs_narrator "А ниже, выцветшим карандашом, кто-то дописал:"
    cs_narrator "«Повторный — ?»"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Извините, а что значит «повторный»?"
    cs_narrator "Женщина подняла голову и посмотрела на лист так, будто видела его впервые."
    $ cs_rev_focus("rev_admin")
    with cs_sprite_change
    # cs_page_anchor: 531f8fee07f403687fd8
    cs_rev_admin "Не знаю."
    cs_rev_admin "Он тут всегда висел."
    $ cs_rev_room('cs_camp_path_day')
    # cs_page_anchor: 11dd08f4ddf9d65770ee
    cs_narrator "Даша дёрнула меня за рукав."
    cs_narrator "Мы вышли."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты опять думаешь громко."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0110874637f9b3ddbdd0
    cs_ls "Седьмой день."
    cs_ls "Отъезд."
    cs_ls "У Семёна смена началась на день раньше нашей."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "И?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: effadabe094290632ed6
    cs_ls "Пока ничего."
    cs_ls "Просто запомнила."
    $ cs_rev_room('cs_storage_int_day')
    $ cs_rev_sfx('sound/sfx/open_door_squeak_2.ogg',0.3)
    cs_narrator "Славя стояла среди коробок со списком в руках и выглядела так, будто инвентарь лагеря лично объявил ей войну."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    cs_sl "Только не говорите, что Ольга Дмитриевна прислала вас мне в помощь."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9a6efa089cb57c912eca
    cs_ls "Прислала."
    cs_ls "Но мы согласились добровольно."
    if "3:4" in cs_rev_choices:
        if cs_rev_choices["3:4"]==0:
            $ cs_rev_choice(3,4,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 8a17431c5420e06030b7
            cs_ls "Я считаю, Даша носит."
            cs_ls "Идеальное разделение труда."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Почему-то всегда носит Даша."
            cs_narrator "Мы пересчитали мячи, скакалки, флажки и одну загадочную коробку, в которой лежали только сломанные свистки."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            # cs_page_anchor: c3a11e172fb98457b1fb
            cs_sl "Вы мне полдня сэкономили."
            cs_sl "Спасибо."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 8296ae12b17b69b3153e
            cs_ls "Обращайся."
            cs_ls "Только без тяжёлого и без свистков."
            $ cs_rev_award("3:4:cs_friend_sl","cs_friend_sl",1)
            $ cs_rev_finish_choice(3,4)
        else:
            $ cs_rev_choice(3,4,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Славя, я с одной рукой тут больше помешаю."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            # cs_page_anchor: e3913467d925376ace8d
            cs_sl "Ничего."
            cs_sl "Спасибо, что честно."
            cs_sl "Даша, можешь подержать список?"
            # cs_page_anchor: ecd9fa8e0c4fc92117e6
            cs_narrator "Даша помогла минут десять."
            cs_narrator "Я честно держала дверь."
            $ cs_rev_finish_choice(3,4)
    else:
        menu:
            "Помочь Славе закончить учёт инвентаря":
                $ cs_rev_choice(3,4,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: aecf995d186f170f23ad
                cs_ls "Я считаю, Даша носит."
                cs_ls "Идеальное разделение труда."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Почему-то всегда носит Даша."
                cs_narrator "Мы пересчитали мячи, скакалки, флажки и одну загадочную коробку, в которой лежали только сломанные свистки."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                # cs_page_anchor: 27fd85c51a13ab17649a
                cs_sl "Вы мне полдня сэкономили."
                cs_sl "Спасибо."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 80dbc7764b15631ea7e8
                cs_ls "Обращайся."
                cs_ls "Только без тяжёлого и без свистков."
                $ cs_rev_award("3:4:cs_friend_sl","cs_friend_sl",1)
                $ cs_rev_finish_choice(3,4)
            "Честно сказать, что с рукой много не наработаешь":
                $ cs_rev_choice(3,4,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Славя, я с одной рукой тут больше помешаю."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                # cs_page_anchor: 1f6b42bf2a6fe9559830
                cs_sl "Ничего."
                cs_sl "Спасибо, что честно."
                cs_sl "Даша, можешь подержать список?"
                # cs_page_anchor: 61b67b89a02e28398673
                cs_narrator "Даша помогла минут десять."
                cs_narrator "Я честно держала дверь."
                $ cs_rev_finish_choice(3,4)
    if cs_sl_poster_saved_day3:
        cs_narrator "Славя достала из папки наш плакат."
        $ cs_rev_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: 274fe6a87f65e704fd6b
        cs_sl "Держи."
        cs_sl "Пока не помялся."
        cs_narrator "Я свернула его в трубочку и сунула под мышку."
        $ cs_sl_poster_collected_day3 = True
    $ cs_rev_room('cs_storage_ext_day')
    # cs_page_anchor: 0ca7bb0060b121021cb6
    cs_narrator "Когда мы вышли со склада, у дорожки нас догнал Семён."
    cs_narrator "Уже без полотенца."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 49dbb79395c8f7967b90
    cs_sy "Лена."
    cs_sy "Можно тебя на минуту?"
    cs_narrator "Даша деликатно отошла к клумбе."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 75108d2f60904b1f13a1
    cs_sy "Про Ольгу Дмитриевну."
    cs_sy "Не надо больше."
    cs_sy "Мне и так неловко, что я у неё живу."
    # cs_page_anchor: 52733f2fafc28f97ed43
    cs_narrator "Шутка уже вертелась на языке."
    cs_narrator "Я её проглотила."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d3e2723474194b9a8eb1
    cs_ls "Хорошо."
    cs_ls "Больше не буду."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Правда?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: efa33340290472d56889
    cs_ls "Правда."
    cs_ls "Я могу быть саркастичной."
    cs_ls "Но не хочу быть неприятной."
    # cs_page_anchor: 52deaa999ce2b75803c4
    cs_narrator "Он кивнул."
    cs_narrator "Кажется, с облегчением."
    return

label cs_rev_d3_06:
    $ cs_rev_begin(3,6,['cs_darya', 'dv', 'mi'])
    $ save_name = "Чужая смена — День 3: Музыкальный клуб"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_musclub_day")
    if cs_mz_map_lead:
        $ cs_rev_room('bg ext_musclub_day')
    $ cs_rev_music(cs_miku_piano_track,0.22,1.0)
    # cs_page_anchor: 51b9960b8371d260e1dd
    cs_narrator "Из клуба доносилась музыка."
    cs_narrator "Мику играла что-то медленное, потом сбивалась, начинала заново и снова сбивалась на одном и том же месте."
    $ cs_rev_room('bg int_musclub_day')
    cs_narrator "Алиса сидела на подоконнике с гитарой и, судя по выражению лица, считала до десяти."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 37bb0aaae160982d5e1a
    cs_mi "Ой, вы пришли!"
    cs_mi "Лена, Даша!"
    cs_mi "Послушайте, у меня одна мелодия не выходит из головы, я её не сочиняла, честное слово, она просто есть, а вот здесь я никак не могу вспомнить, что дальше…"
    # cs_page_anchor: cd7384bce995b564a9be
    cs_narrator "Она сыграла короткую фразу."
    cs_narrator "Спокойную, немного грустную."
    $ cs_rev_music(cs_miku_piano_track,0.22)
    cs_narrator "Мелодия обрывалась на полуслове."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: 766c666f9d0a91240479
    cs_mi "Как будто я её уже играла."
    cs_mi "На прошлой смене."
    cs_mi "Только я на прошлой смене не была."
    $ cs_rev_focus("dv")
    with cs_sprite_change
    # cs_page_anchor: 3dd1bb9a38d7cef72d71
    cs_dv "Мику, ты её играешь с утра."
    cs_dv "Двадцать раз."
    $ cs_rev_focus("mi")
    with cs_sprite_change
    cs_mi "Двадцать три!"
    cs_narrator "Даша подошла к пианино и посмотрела на клавиши."
    stop music fadeout 1.5
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Можно я попробую тот переход?"
    $ cs_rev_focus("mi")
    with cs_sprite_change
    # cs_page_anchor: f86fa3430c61555c6e68
    cs_mi "Конечно!"
    cs_mi "Ты же вчера так хорошо играла!"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: da51e73eb8ae8eee653b
    cs_da "Вчера я половину забыла."
    cs_da "Но этот переход попробую."
    # cs_page_anchor: a7bd0d735e60d8a7aef6
    cs_narrator "Она сыграла фразу Мику, чуть замедлив её в конце."
    cs_narrator "Звучало естественнее."
    cs_narrator "Мику смотрела на Дашу так, будто только что встретила живую легенду."
    if "3:5" in cs_rev_choices:
        if cs_rev_choices["3:5"]==0:
            $ cs_rev_choice(3,5,0)
            cs_narrator "Я села рядом с пианино и слушала, как Мику с Дашей разбирают мелодию."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 5b16b65a264a790c7d7c
            cs_ls "Мне кажется, конец не нужно придумывать."
            cs_ls "Он придёт сам."
            cs_ls "Как в рисунке: иногда линия сама знает, куда ей идти."
            $ cs_rev_focus("mi")
            with cs_sprite_change
            # cs_page_anchor: 5a8cdab96bbaf2aed4ed
            cs_mi "Ой."
            cs_mi "Как красиво ты сказала."
            cs_mi "Я так и запишу."
            cs_mi "То есть не запишу, а запомню."
            cs_mi "Приходите завтра, я вам сыграю, что получится!"
            cs_mi "И вступление тоже, Алиса хочет его сократить, а я — нет!"
            $ cs_rev_focus("dv")
            with cs_sprite_change
            cs_dv "На четыре такта, Мику."
            $ cs_rev_award("3:5:cs_friend_mi","cs_friend_mi",1)
            $ cs_mi_followup_invitation_day3 = True
            $ cs_rev_finish_choice(3,5)
        else:
            $ cs_rev_choice(3,5,1)
            cs_narrator "Я подсела к Алисе на подоконник."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Играешь что-нибудь своё?"
            $ cs_rev_focus("dv")
            with cs_sprite_change
            cs_dv "А тебе какое дело?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 81c8e97dcd8a510072bb
            cs_ls "Профессиональное любопытство."
            cs_ls "Я рисую, ты играешь."
            cs_ls "Почти коллеги."
            # cs_page_anchor: 48f165dc99a4e5812d51
            cs_narrator "Алиса фыркнула."
            cs_narrator "Потом всё-таки взяла пару аккордов."
            $ cs_rev_focus("dv")
            with cs_sprite_change
            # cs_page_anchor: 5714e11a375369441f15
            cs_dv "Вот."
            cs_dv "Своё."
            cs_dv "Пока без слов."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 8519aa2b35f876d0603f
            cs_ls "Хорошо звучит."
            cs_ls "Без слов даже лучше — каждый услышит своё."
            cs_narrator "Алиса посмотрела на меня с подозрением, но было видно, что ей приятно."
            $ cs_rev_focus("dv")
            with cs_sprite_change
            # cs_page_anchor: e81be46729b43f9e942b
            cs_dv "Заходи как-нибудь."
            cs_dv "Покажу, как это дальше звучит."
            cs_dv "Если не будешь умничать."
            $ cs_rev_award("3:5:cs_friend_dv","cs_friend_dv",1)
            $ cs_dv_music_talk_day3 = True
            $ cs_dv_followup_invitation_day3 = True
            $ cs_rev_finish_choice(3,5)
    else:
        menu:
            "Послушать мелодию Мику до конца и помочь с аранжировкой":
                $ cs_rev_choice(3,5,0)
                cs_narrator "Я села рядом с пианино и слушала, как Мику с Дашей разбирают мелодию."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: e725bfdf1dfdb27209f4
                cs_ls "Мне кажется, конец не нужно придумывать."
                cs_ls "Он придёт сам."
                cs_ls "Как в рисунке: иногда линия сама знает, куда ей идти."
                $ cs_rev_focus("mi")
                with cs_sprite_change
                # cs_page_anchor: 5bcdea5dcf688847d1ec
                cs_mi "Ой."
                cs_mi "Как красиво ты сказала."
                cs_mi "Я так и запишу."
                cs_mi "То есть не запишу, а запомню."
                cs_mi "Приходите завтра, я вам сыграю, что получится!"
                cs_mi "И вступление тоже, Алиса хочет его сократить, а я — нет!"
                $ cs_rev_focus("dv")
                with cs_sprite_change
                cs_dv "На четыре такта, Мику."
                $ cs_rev_award("3:5:cs_friend_mi","cs_friend_mi",1)
                $ cs_mi_followup_invitation_day3 = True
                $ cs_rev_finish_choice(3,5)
            "Подсесть к Алисе и поговорить о гитаре":
                $ cs_rev_choice(3,5,1)
                cs_narrator "Я подсела к Алисе на подоконник."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Играешь что-нибудь своё?"
                $ cs_rev_focus("dv")
                with cs_sprite_change
                cs_dv "А тебе какое дело?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 9ef608d3a6659cb7fd52
                cs_ls "Профессиональное любопытство."
                cs_ls "Я рисую, ты играешь."
                cs_ls "Почти коллеги."
                # cs_page_anchor: fb01295da91efcfcbf61
                cs_narrator "Алиса фыркнула."
                cs_narrator "Потом всё-таки взяла пару аккордов."
                $ cs_rev_focus("dv")
                with cs_sprite_change
                # cs_page_anchor: 31016deae721444caf8f
                cs_dv "Вот."
                cs_dv "Своё."
                cs_dv "Пока без слов."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 97b9e4410f0f9c6c9646
                cs_ls "Хорошо звучит."
                cs_ls "Без слов даже лучше — каждый услышит своё."
                cs_narrator "Алиса посмотрела на меня с подозрением, но было видно, что ей приятно."
                $ cs_rev_focus("dv")
                with cs_sprite_change
                # cs_page_anchor: 3751afb4320c941c7ccf
                cs_dv "Заходи как-нибудь."
                cs_dv "Покажу, как это дальше звучит."
                cs_dv "Если не будешь умничать."
                $ cs_rev_award("3:5:cs_friend_dv","cs_friend_dv",1)
                $ cs_dv_music_talk_day3 = True
                $ cs_dv_followup_invitation_day3 = True
                $ cs_rev_finish_choice(3,5)
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    cs_narrator "Горн к обеду прозвучал как раз тогда, когда Мику в третий раз пыталась объяснить Алисе, почему четыре такта — это очень много."
    return

label cs_rev_d3_07:
    $ cs_rev_begin(3,7,['cs_darya', 'cs_zhenya', 'un'])
    $ save_name = "Чужая смена — День 3: Общество тихих людей"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_dining_hall_people_day")
    $ cs_rev_music(cs_day_music_everyday,0.14,2.5)
    cs_narrator "В очереди Даша рассказывала, что у них дома в 2026 году обед выглядел как «Мивина» над ноутбуком."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9d0425a67e92449966e3
    cs_ls "У меня тоже."
    cs_ls "Только над планшетом."
    cs_ls "Рисую, а лапша остывает."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Скучаешь?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 22c57282975ccee06a00
    cs_ls "По лапше?"
    cs_ls "Нет."
    cs_ls "По тому, что можно было не думать, который сейчас год."
    # cs_page_anchor: b40b472687d552571ce2
    cs_narrator "Даша кивнула."
    cs_narrator "Она поняла."
    cs_narrator "Не про лапшу."
    # cs_page_anchor: 9e7c244c05b5f810e979
    cs_narrator "У окна сидела Женя."
    cs_narrator "А за соседним столом, одна, — Лена Тихонова."
    cs_narrator "Перед ней лежал альбом, и она рисовала, почти не притрагиваясь к супу."
    # cs_page_anchor: 46562ab8b9bcbb23ce19
    cs_narrator "Мы сели к Жене."
    cs_narrator "Я то и дело поглядывала на тёзку."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 12a9c46e840b2d5b5669
    cs_mz "Хочешь пригласить — пригласи."
    cs_mz "Я не против."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ты читаешь мысли?"
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Ты на неё смотришь уже третью ложку."
    if "3:6" in cs_rev_choices:
        if cs_rev_choices["3:6"]==0:
            $ cs_rev_choice(3,6,0)
            cs_narrator "Я подошла к соседнему столу."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 9b9abd6387ac2ea2a8ba
            cs_ls "Лен."
            cs_ls "Пересядешь к нам?"
            cs_ls "Обещаю не заглядывать в альбом без спроса."
            # cs_page_anchor: 71208e65b31ac322b94c
            cs_narrator "Тихонова вздрогнула и прижала альбом к себе."
            cs_narrator "Потом посмотрела на Женю, на Дашу."
            $ cs_rev_focus("un")
            with cs_sprite_change
            cs_un "Можно… если я не помешаю."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: a8df06cf6b6dacffe949
            cs_mz "Не помешаешь."
            cs_mz "Тут все тихие."
            cs_mz "Кроме Соколовой."
            # cs_page_anchor: 1261b545600e83e1e2b0
            cs_narrator "Тихонова пересела."
            cs_narrator "Некоторое время мы просто ели."
            cs_narrator "Потом она сама открыла альбом и положила его между нами."
            # cs_page_anchor: e8655e64a8b2f95bf521
            cs_narrator "На листе был старый корпус."
            cs_narrator "Облупившиеся стены, крыльцо, тёмные окна."
            cs_narrator "Нарисовано тонко и очень точно."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Ты там была?"
            $ cs_rev_focus("un")
            with cs_sprite_change
            # cs_page_anchor: ad73bd5a22005ed362a1
            cs_un "Один раз."
            cs_un "Дошла до лестницы и ушла."
            cs_un "Там… неуютно."
            cs_narrator "Я посмотрела на рисунок внимательнее."
            # cs_page_anchor: 311885a663bb9802f432
            cs_narrator "В одном из тёмных окон второго этажа угадывался силуэт."
            cs_narrator "Девушка."
            cs_narrator "Два хвостика."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "А это кто?"
            cs_narrator "Тихонова наклонилась к рисунку и нахмурилась."
            $ cs_rev_focus("un")
            with cs_sprite_change
            # cs_page_anchor: b8c36ca9142e066be371
            cs_un "Не знаю."
            cs_un "Я её не рисовала."
            cs_un "То есть… рисовала, наверное."
            cs_un "Не помню."
            cs_narrator "Она быстро закрыла альбом."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: b9f88d7b1e61c999d11e
            cs_ls "Красиво нарисовано."
            cs_ls "Правда."
            cs_ls "Хочешь вечером порисовать вместе?"
            cs_ls "Я тоже давно не брала карандаш."
            $ cs_rev_focus("un")
            with cs_sprite_change
            cs_un "Хочу."
            $ cs_rev_award("3:6:cs_friend_un","cs_friend_un",1)
            $ cs_un_day3_lunch_together = True
            $ cs_un_sketch_invite_day3 = True
            $ cs_rev_finish_choice(3,6)
        else:
            $ cs_rev_choice(3,6,1)
            # cs_page_anchor: bb3d4d76be0f4734d0b3
            cs_narrator "Я решила не мешать."
            cs_narrator "Человек рисует — это святое."
            # cs_page_anchor: 11622e3f0981d79fa28a
            cs_narrator "Когда мы уходили, Тихонова подняла голову и чуть кивнула мне."
            cs_narrator "Я кивнула в ответ."
            $ cs_rev_finish_choice(3,6)
    else:
        menu:
            "Позвать Тихонову за наш стол":
                $ cs_rev_choice(3,6,0)
                cs_narrator "Я подошла к соседнему столу."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 465f8cfa0869ba027894
                cs_ls "Лен."
                cs_ls "Пересядешь к нам?"
                cs_ls "Обещаю не заглядывать в альбом без спроса."
                # cs_page_anchor: 695f263ec16afc08b297
                cs_narrator "Тихонова вздрогнула и прижала альбом к себе."
                cs_narrator "Потом посмотрела на Женю, на Дашу."
                $ cs_rev_focus("un")
                with cs_sprite_change
                cs_un "Можно… если я не помешаю."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: f8970ab2b607bb021289
                cs_mz "Не помешаешь."
                cs_mz "Тут все тихие."
                cs_mz "Кроме Соколовой."
                # cs_page_anchor: cdaab1645ed54f764732
                cs_narrator "Тихонова пересела."
                cs_narrator "Некоторое время мы просто ели."
                cs_narrator "Потом она сама открыла альбом и положила его между нами."
                # cs_page_anchor: 63a3ed9ea97cdf5b6a09
                cs_narrator "На листе был старый корпус."
                cs_narrator "Облупившиеся стены, крыльцо, тёмные окна."
                cs_narrator "Нарисовано тонко и очень точно."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Ты там была?"
                $ cs_rev_focus("un")
                with cs_sprite_change
                # cs_page_anchor: 80bb1cbd516304cd7b60
                cs_un "Один раз."
                cs_un "Дошла до лестницы и ушла."
                cs_un "Там… неуютно."
                cs_narrator "Я посмотрела на рисунок внимательнее."
                # cs_page_anchor: 17d6267a889175b478ac
                cs_narrator "В одном из тёмных окон второго этажа угадывался силуэт."
                cs_narrator "Девушка."
                cs_narrator "Два хвостика."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "А это кто?"
                cs_narrator "Тихонова наклонилась к рисунку и нахмурилась."
                $ cs_rev_focus("un")
                with cs_sprite_change
                # cs_page_anchor: e2d84d7a2698ef6ea4eb
                cs_un "Не знаю."
                cs_un "Я её не рисовала."
                cs_un "То есть… рисовала, наверное."
                cs_un "Не помню."
                cs_narrator "Она быстро закрыла альбом."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: ef8153865867767f9b09
                cs_ls "Красиво нарисовано."
                cs_ls "Правда."
                cs_ls "Хочешь вечером порисовать вместе?"
                cs_ls "Я тоже давно не брала карандаш."
                $ cs_rev_focus("un")
                with cs_sprite_change
                cs_un "Хочу."
                $ cs_rev_award("3:6:cs_friend_un","cs_friend_un",1)
                $ cs_un_day3_lunch_together = True
                $ cs_un_sketch_invite_day3 = True
                $ cs_rev_finish_choice(3,6)
            "Не мешать ей рисовать":
                $ cs_rev_choice(3,6,1)
                # cs_page_anchor: f6ff47a625c02c25c811
                cs_narrator "Я решила не мешать."
                cs_narrator "Человек рисует — это святое."
                # cs_page_anchor: f5d205f91a5025d211d1
                cs_narrator "Когда мы уходили, Тихонова подняла голову и чуть кивнула мне."
                cs_narrator "Я кивнула в ответ."
                $ cs_rev_finish_choice(3,6)
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 988ff8e3a901c31b766d
    cs_mz "После обеда я в библиотеке."
    cs_mz "Если надумаешь читать — приходи."
    if cs_mz_book_requested_day3:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Гончаров тебя ждёт."
    cs_narrator "Даша собиралась к Мику — та требовала продолжения с переходом."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Встретимся вечером?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 61b021afcadb91a1f08d
    cs_ls "У библиотеки."
    cs_ls "Или там, где будет Гончаров."
    return

label cs_rev_d3_08:
    $ cs_rev_begin(3,8,['cs_zhenya'])
    $ save_name = "Чужая смена — День 3: Читательский билет"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_library_day")
    $ cs_rev_music("sound/music/get_to_know_me_better.ogg",0.12,2.5)
    $ cs_rev_sfx('sound/sfx/open_door_1.ogg',0.25)
    # cs_page_anchor: beb6e3907eacc8cb854e
    cs_narrator "В библиотеке было прохладно и тихо."
    cs_narrator "Женя что-то записывала в журнал."
    cs_narrator "На входе она сохранила себе текущее значение дружбы."
    $ cs_rev_snapshot("cs_mz_friend_on_arrival_day3","cs_friend_mz")
    $ cs_rev_snapshot("cs_mz_friend_on_arrival_day3","cs_friend_mz")
    if cs_mz_map_lead:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 33b9c82cb36065d822a6
        cs_mz "Каталоги."
        cs_mz "Как обещала."
        # cs_page_anchor: d4567b53fd5439b12ce9
        cs_narrator "Она поставила на стол две коробки с карточками."
        cs_narrator "Мы перебирали их минут двадцать."
        cs_narrator "Списки изданий, учётные номера, ничего похожего на карту."
        cs_narrator "Потом мне попалась карточка, написанная от руки."
        cs_narrator "«Архив лагеря „Совёнок“. Списки смен и фотоматериалы, 1963–1971. Место хранения: старый корпус, подвальное помещение»."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: d4c33626937ba95b6f26
        cs_ls "Жень."
        cs_ls "Смотри."
        cs_narrator "Женя прочитала и нахмурилась."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 16005fa37da3eb8df6ce
        cs_mz "Я про это и говорила."
        cs_mz "Туда никто не ходит."
        cs_mz "Старый корпус закрыт."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Закрыт — это на замок?"
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Закрыт — это «туда никто не ходит», Соколова."
        # cs_page_anchor: 79b59588551e72ca9bd7
        cs_narrator "Я вернула карточку на место."
        cs_narrator "Но запомнила каждую цифру."
        $ cs_mz_catalog_checked_day3 = True
    if cs_mz_friend_on_arrival_day3 <= 0:
        # cs_page_anchor: cb8266498ab4aed0e327
        cs_narrator "Женя молча показала на полку с классикой."
        cs_narrator "Я сама выбрала «Обыкновенную историю» Гончарова — понравилось название."
        cs_narrator "Женя записала выдачу."
    elif cs_mz_friend_on_arrival_day3 == 1:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 8129323212561aa80367
        cs_mz "Возьми Гончарова."
        cs_mz "«Обыкновенную историю»."
        cs_mz "Думаю, тебе подойдёт."
    else:
        cs_narrator "Женя уже держала в руках книгу."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 96d2c850d61b70540b41
        cs_mz "Гончаров."
        cs_mz "Я её отложила."
        cs_mz "Садись за тот стол у окна — там свет лучше и никто не ходит."
        $ cs_mz_quiet_reading_place_day3 = True
    $ cs_mz_book_borrowed_day3 = True
    cs_narrator "Я села и открыла книгу."
    $ cs_pov_begin()
    with cs_sprite_leave
    $ cs_day03_reading_book_id = "goncharov_ordinary_story"
    $ cs_day03_reading_book_location = "lena_hand"
    # cs_page_anchor: de2bab9def2591c5fd6f
    cs_narrator "Молодой человек из провинции едет в Петербург, полный надежд."
    cs_narrator "Дядя встречает его и методично объясняет, что жизнь устроена совсем иначе."
    cs_narrator "Через двадцать страниц я поймала себя на том, что не думаю ни о петле, ни об автобусе, ни о листке «Повторный — ?»."
    cs_narrator "Просто читаю."
    cs_narrator "Час прошёл незаметно."
    if "3:7" in cs_rev_choices:
        if cs_rev_choices["3:7"]==0:
            $ cs_rev_choice(3,7,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: dc4af6b8532a4fd30c28
            cs_ls "Жень."
            cs_ls "Этот Адуев."
            cs_ls "Он ведь не глупый."
            cs_ls "Он просто думает, что мир устроен так, как ему рассказали."
            cs_narrator "Женя оторвалась от журнала."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "А ты думаешь иначе?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: d43818b8cb780453d4b4
            cs_ls "Я думаю, мне это знакомо."
            cs_ls "Я тоже приехала сюда, думая, что знаю, как всё будет."
            cs_ls "А тут каждый человек живёт по-своему."
            cs_narrator "Женя некоторое время смотрела на меня."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: 5aca9c330b8b175ce79d
            cs_mz "Интересное прочтение."
            cs_mz "Обычно все спорят, кто прав — дядя или племянник."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: e31cb51f53c27dbedaf0
            cs_ls "Оба."
            cs_ls "И оба нет."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: 5f20276c8ebf41a8864f
            cs_mz "Можешь приходить сюда просто так."
            cs_mz "Не обязательно за книгой."
            $ cs_rev_award("3:7:cs_friend_mz","cs_friend_mz",1)
            $ cs_mz_day3_honest_book_talk = True
            $ cs_mz_open_library_invitation_day3 = True
            $ cs_rev_finish_choice(3,7)
        else:
            $ cs_rev_choice(3,7,1)
            # cs_page_anchor: a69949701b4f3507f46f
            cs_narrator "Я молча читала дальше."
            cs_narrator "Женя работала."
            cs_narrator "Тишина была общей — и это было приятно."
            $ cs_rev_finish_choice(3,7)
    else:
        menu:
            "Честно сказать Жене, что думаешь о главном герое":
                $ cs_rev_choice(3,7,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 21a515bd7381abe73d94
                cs_ls "Жень."
                cs_ls "Этот Адуев."
                cs_ls "Он ведь не глупый."
                cs_ls "Он просто думает, что мир устроен так, как ему рассказали."
                cs_narrator "Женя оторвалась от журнала."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "А ты думаешь иначе?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: f0255f63cf45494bfdbd
                cs_ls "Я думаю, мне это знакомо."
                cs_ls "Я тоже приехала сюда, думая, что знаю, как всё будет."
                cs_ls "А тут каждый человек живёт по-своему."
                cs_narrator "Женя некоторое время смотрела на меня."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: 36ddc47346b23ab9c28b
                cs_mz "Интересное прочтение."
                cs_mz "Обычно все спорят, кто прав — дядя или племянник."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 736f9c40f7686abe4f00
                cs_ls "Оба."
                cs_ls "И оба нет."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: 3611c95ab38962e9f789
                cs_mz "Можешь приходить сюда просто так."
                cs_mz "Не обязательно за книгой."
                $ cs_rev_award("3:7:cs_friend_mz","cs_friend_mz",1)
                $ cs_mz_day3_honest_book_talk = True
                $ cs_mz_open_library_invitation_day3 = True
                $ cs_rev_finish_choice(3,7)
            "Не мешать Жене работать":
                $ cs_rev_choice(3,7,1)
                # cs_page_anchor: 5f67b512f7c23aab8be9
                cs_narrator "Я молча читала дальше."
                cs_narrator "Женя работала."
                cs_narrator "Тишина была общей — и это было приятно."
                $ cs_rev_finish_choice(3,7)
    cs_narrator "Ближе к вечеру я закрыла книгу на закладке."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 9252c4edcad343a0234a
    cs_mz "Дочитаешь — вернёшь."
    cs_mz "Не порти страницы."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 0a36fcee32b2258609e0
    cs_ls "Ни за что."
    cs_ls "Я с книгами обращаюсь лучше, чем с собственным локтем."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Невысокая планка, Соколова."
    return

label cs_rev_d3_09:
    $ cs_rev_begin(3,9,['cs_darya', 'cs_semen'])
    $ save_name = "Чужая смена — День 3: Площадь"
    $ cs_rev_time("day")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_square_day")
    $ cs_rev_snapshot("cs_se_friend_before_square_day3","cs_friend_se")
    # cs_page_anchor: f1fc7aadf9ed000f123f
    cs_narrator "У библиотеки меня ждала Даша."
    cs_narrator "На пальцах у неё были следы карандаша: Мику заставила её записывать ноты."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 48bd013e14c5aef25061
    cs_da "Мику хочет, чтобы я завтра снова пришла."
    cs_da "И послезавтра."
    cs_da "И, кажется, всегда."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 8a5cc6172032fea31d4b
    cs_ls "Поздравляю."
    cs_ls "Ты официально член музыкального клуба."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Я не записывалась."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Мику записала тебя за тебя."
    # cs_page_anchor: 588eb0eeaa2b281da91e
    cs_narrator "На площади на скамейке сидел Семён."
    cs_narrator "Смотрел в сторону ворот."
    cs_narrator "Не читал, не ел, ни с кем не разговаривал."
    cs_narrator "Просто смотрел."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ты сегодня совсем без дела?"
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: bb96479d553e03a6045e
    cs_sy "Ищу его."
    cs_sy "Пока не нашёл."
    if "3:8" in cs_rev_choices:
        if cs_rev_choices["3:8"]==0:
            $ cs_rev_choice(3,8,0)
            # cs_page_anchor: 9d055b1cf1afcb833ae9
            cs_narrator "Я села рядом."
            cs_narrator "Даша — с другой стороны."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Опять дорога?"
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 22d5990a6f359c263f73
            cs_sy "Не только."
            cs_sy "Знаешь, что странно?"
            cs_sy "Я сбился со счёта."
            cs_sy "Сколько я тут?"
            cs_sy "Четыре дня?"
            cs_sy "Пять?"
            cs_sy "Утром проснулся и не мог вспомнить."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Ты приехал на день раньше нас."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: bf28a01681446b01b122
            cs_sy "Вот и я так думаю."
            cs_sy "Но ощущение, будто дольше."
            cs_sy "Намного."
            cs_narrator "Он потёр лицо."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 465d5e1c4f6bffa08154
            cs_sy "Ладно."
            cs_sy "Ерунда."
            cs_sy "Не обращай внимания."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: f71db139a627cb03e03d
            cs_ls "Это не ерунда."
            cs_ls "Если что-то кажется странным — говори."
            cs_ls "Я лучше послушаю странное, чем потом узнаю его последней."
            # cs_page_anchor: 90d1dae77fb8e7ab271c
            cs_narrator "Семён посмотрел на меня."
            cs_narrator "Без привычного раздражения."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Ты сегодня какая-то нормальная."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Не привыкай."
            $ cs_rev_award("3:8:cs_friend_se","cs_friend_se",1)
            $ cs_se_day3_personal_talk = True
            if cs_se_friend_before_square_day3 >= 2:
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 62824240b6785d37f264
                cs_sy "Знаешь, мне иногда кажется, что я уже сидел на этой скамейке."
                cs_sy "И ты сидела рядом."
                cs_sy "Только тебя тогда звали не Соколова."
                cs_narrator "Он сам смутился от этих слов."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 5d16348829120df80072
                cs_sy "Всё."
                cs_sy "Точно ерунда."
                # cs_page_anchor: ebdea0c69b9fa7a9e0a8
                cs_narrator "Я не ответила."
                cs_narrator "Только почувствовала, как по спине прошёл холодок."
            $ cs_rev_finish_choice(3,8)
        else:
            $ cs_rev_choice(3,8,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: e119c0acb5a94b7e03f4
            cs_ls "Тогда отдыхай."
            cs_ls "Иногда искать дело тоже дело."
            $ cs_rev_focus("sy")
            with cs_sprite_change
            cs_sy "Глубоко."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 7c3adf3a81dc4fede793
            cs_ls "Я сегодня читаю Гончарова."
            cs_ls "Набираюсь мудрости."
            $ cs_rev_finish_choice(3,8)
    else:
        menu:
            "Сесть рядом и поговорить с Семёном по-настоящему":
                $ cs_rev_choice(3,8,0)
                # cs_page_anchor: 5677e8c14676406edbf7
                cs_narrator "Я села рядом."
                cs_narrator "Даша — с другой стороны."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Опять дорога?"
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 6cefec090e43094453f1
                cs_sy "Не только."
                cs_sy "Знаешь, что странно?"
                cs_sy "Я сбился со счёта."
                cs_sy "Сколько я тут?"
                cs_sy "Четыре дня?"
                cs_sy "Пять?"
                cs_sy "Утром проснулся и не мог вспомнить."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Ты приехал на день раньше нас."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: 7f0c8e8192a724c3f5c8
                cs_sy "Вот и я так думаю."
                cs_sy "Но ощущение, будто дольше."
                cs_sy "Намного."
                cs_narrator "Он потёр лицо."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                # cs_page_anchor: ee3a5659fe2f5df77e59
                cs_sy "Ладно."
                cs_sy "Ерунда."
                cs_sy "Не обращай внимания."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 6164d5da9c8075678dcc
                cs_ls "Это не ерунда."
                cs_ls "Если что-то кажется странным — говори."
                cs_ls "Я лучше послушаю странное, чем потом узнаю его последней."
                # cs_page_anchor: 0ecb1e1708fe39d1290b
                cs_narrator "Семён посмотрел на меня."
                cs_narrator "Без привычного раздражения."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Ты сегодня какая-то нормальная."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Не привыкай."
                $ cs_rev_award("3:8:cs_friend_se","cs_friend_se",1)
                $ cs_se_day3_personal_talk = True
                if cs_se_friend_before_square_day3 >= 2:
                    $ cs_rev_focus("sy")
                    with cs_sprite_change
                    # cs_page_anchor: 49d7262c1b9abc4f3c60
                    cs_sy "Знаешь, мне иногда кажется, что я уже сидел на этой скамейке."
                    cs_sy "И ты сидела рядом."
                    cs_sy "Только тебя тогда звали не Соколова."
                    cs_narrator "Он сам смутился от этих слов."
                    $ cs_rev_focus("sy")
                    with cs_sprite_change
                    # cs_page_anchor: 9ade83992694e1762628
                    cs_sy "Всё."
                    cs_sy "Точно ерунда."
                    # cs_page_anchor: 283afa3c2579dd399af2
                    cs_narrator "Я не ответила."
                    cs_narrator "Только почувствовала, как по спине прошёл холодок."
                $ cs_rev_finish_choice(3,8)
            "Дать Семёну отдохнуть":
                $ cs_rev_choice(3,8,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 48ff98540ef31af8671a
                cs_ls "Тогда отдыхай."
                cs_ls "Иногда искать дело тоже дело."
                $ cs_rev_focus("sy")
                with cs_sprite_change
                cs_sy "Глубоко."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: ee566a780ebcd1cb5116
                cs_ls "Я сегодня читаю Гончарова."
                cs_ls "Набираюсь мудрости."
                $ cs_rev_finish_choice(3,8)
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 697ec4d4a71c51829030
    cs_sy "Вы рисовать собираетесь?"
    cs_sy "Видел утром Тихонову с альбомом."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Собираемся."
    $ cs_rev_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 2297df7c819f092c6fe1
    cs_sy "За музыкальным клубом есть хорошее место."
    cs_sy "Видно весь лагерь, и никто не ходит."
    $ cs_se_sketch_spot_day3 = True
    return

label cs_rev_d3_10:
    $ cs_rev_begin(3,10,['cs_darya', 'un'])
    $ save_name = "Чужая смена — День 3: Две Лены и один карандаш"
    $ cs_rev_time("sunset")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg ext_musclub_day")
    if cs_un_sketch_invite_day3:
        # cs_page_anchor: a531d76af3a4ddcda3a0
        cs_narrator "Тихонова уже сидела на месте, которое посоветовал Семён."
        cs_narrator "Альбом на коленях, карандаш за ухом."
        $ cs_rev_focus("un")
        with cs_sprite_change
        cs_un "Ты пришла."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Обещала же."
        # cs_page_anchor: e9456433559f3d3099cf
        cs_narrator "Мы рисовали молча."
        cs_narrator "Отсюда действительно был виден весь лагерь: площадь, столовая, крыши домиков."
        cs_narrator "И дорога к воротам, которая уходила за деревья."
        # cs_page_anchor: e898d7bb515d645d55e3
        cs_narrator "Я рисовала крыши."
        cs_narrator "Тихонова — что-то своё, прикрывая лист ладонью."
        cs_narrator "Минут через сорок она вдруг протянула мне альбом."
        $ cs_rev_focus("un")
        with cs_sprite_change
        cs_un "Это я никому не показывала."
        # cs_page_anchor: 773dbb3eb6ae56757f9e
        cs_narrator "На листе была автобусная остановка у ворот."
        cs_narrator "Пустая."
        cs_narrator "Табличка с номером маршрута."
        cs_narrator "410."
        # cs_page_anchor: 4d9e189ff3c1101e40dc
        cs_narrator "И в стекле стоявшего автобуса — неясное отражение."
        cs_narrator "Девушка."
        cs_narrator "Лица не разобрать."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Ты часто это рисуешь?"
        $ cs_rev_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 1ce4d7e547f2aa924e63
        cs_un "Часто."
        cs_un "Не знаю почему."
        cs_un "Просто рука сама."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Спасибо, что показала."
        cs_narrator "Тихонова убрала альбом и впервые за день улыбнулась по-настоящему."
        $ cs_un_private_drawing_shown_day3 = True
        $ cs_un_sketch_completed_day3 = True
    else:
        # cs_page_anchor: 2190f3eb3857faa377bf
        cs_narrator "Я пришла на место за клубом одна."
        cs_narrator "Отсюда был виден весь лагерь и дорога к воротам."
        # cs_page_anchor: 6c3eda97541d7c2f029b
        cs_narrator "Я нарисовала крыши, столовую и маленький прямоугольник остановки у ворот."
        cs_narrator "Почему-то он получился темнее всего остального."
    $ cs_rev_room('cs_house_lena_darya_int_sunset')
    $ cs_rev_music(cs_day_music_home,0.12,3.0)
    # cs_page_anchor: 1cc2dc50137bc4c94309
    cs_narrator "В домике Даша сидела у окна и что-то писала в тетради."
    cs_narrator "Ноты для Мику, судя по всему."
    cs_narrator "Я повесила плакат над кроватью, если забрала его у Слави, и легла с Гончаровым."
    # cs_page_anchor: d9dbc7587bc6a3b64118
    cs_narrator "Некоторое время мы не разговаривали."
    cs_narrator "Это было удивительно спокойно."
    cs_narrator "Я читала, Даша писала."
    cs_narrator "Ветер шевелил занавеску."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 8f91cdca943bff1a727d
    cs_da "Лен."
    cs_da "Тебе здесь удобно?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "В домике?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Вообще."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2c5fb453352635d59960
    cs_ls "Уже да."
    cs_ls "Знаешь, на какую половицу нельзя наступать ночью — значит, почти дома."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: d8f6dda65ca5dc1e7cec
    cs_da "Мне тоже."
    cs_da "И это немного пугает."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Почему?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 6d900657648b04abbdf2
    cs_da "Потому что я не хочу привыкнуть."
    cs_da "Вдруг привыкну — и перестану искать, как вернуться."
    cs_narrator "Я отложила книгу."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 36d3d13197dc89ed6eb8
    cs_ls "Не перестанем."
    cs_ls "Мы обе слишком упрямые."
    cs_narrator "Даша улыбнулась."
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    # cs_page_anchor: f3ea4a3fdd3def6b555b
    cs_narrator "Над лагерем прозвучал горн к ужину."
    cs_narrator "Я дочитала абзац."
    cs_narrator "Потом ещё один."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 3721ed29c8fd0423ef30
    cs_da "Лен."
    cs_da "Ужин."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Ещё полстраницы."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 01f0cd3a47817a0087e7
    cs_da "Гончаров никуда не убежит."
    cs_da "А котлеты — убегут."
    cs_narrator "Я закрыла книгу, встала и неожиданно для самой себя быстро поцеловала Дашу в щёку."
    # cs_page_anchor: 1046ebf7d441e123ca12
    cs_narrator "Совершенно просто."
    cs_narrator "Без объявлений."
    cs_narrator "Даша замерла."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Лен…"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2997f811170574bcfff1
    cs_ls "Это за котлеты."
    cs_ls "Спасибо, что напомнила."
    $ cs_da_cheek_kiss_day3 = True
    # cs_page_anchor: f46ac293f234b1f3338c
    cs_narrator "Она покраснела."
    cs_narrator "Но улыбнулась."
    return

label cs_rev_d3_11:
    $ cs_rev_begin(3,11,['cs_darya', 'cs_semen', 'cs_zhenya', 'sl'])
    $ save_name = "Чужая смена — День 3: Ужин и совещание на площади"
    $ cs_rev_time("sunset")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("bg int_dining_hall_sunset")
    $ cs_rev_snapshot("cs_mz_dinner_friend_on_arrival","cs_friend_mz")
    $ cs_rev_music(cs_day_music_everyday,0.14,2.5)
    cs_narrator "У столовой стояла Женя."
    if cs_mz_dinner_friend_on_arrival >= 3 and cs_mz_open_library_invitation_day3:
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 4c00e7ae202a3c2f2581
        cs_ls "Можно тебя обнять?"
        cs_ls "Три секунды."
        cs_ls "Без оркестра."
        # cs_page_anchor: 8821eff1e2f04d690051
        cs_narrator "Женя посмотрела на меня так, будто я предложила ей прочитать стихи на линейке."
        cs_narrator "Потом вздохнула."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Три секунды."
        # cs_page_anchor: 90636bef14719c585d56
        cs_narrator "Я обняла её."
        cs_narrator "Ровно три секунды."
        cs_narrator "Женя стояла прямо, но не отстранялась."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 87e8b45cd04a0a982b16
        cs_mz "Всё."
        cs_mz "Хватит."
        $ cs_mz_hug_allowed_day3 = True
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Как Гончаров?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 683d24767f10746b3fad
    cs_ls "Дядя Адуев невыносим."
    cs_ls "Но, кажется, прав."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Дочитаешь — обсудим."
    if "3:9" in cs_rev_choices:
        if cs_rev_choices["3:9"]==0:
            $ cs_rev_choice(3,9,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 97cc7721756dc5606a5a
            cs_ls "Тебе вечером помочь с книгами?"
            cs_ls "Даша тоже свободна."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Я свободна?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            cs_ls "Ты свободна."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            # cs_page_anchor: 63c1d165dd3cb7276add
            cs_mz "Если не будете шуметь."
            cs_mz "После ужина."
            $ cs_rev_award("3:9:cs_friend_mz","cs_friend_mz",1)
            $ cs_mz_evening_help_day3 = True
            $ cs_rev_finish_choice(3,9)
        else:
            $ cs_rev_choice(3,9,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: f1b09161f91c16f7220a
            cs_ls "Хорошего вечера, Жень."
            cs_ls "Я ещё зайду — дочитать."
            $ cs_rev_focus("mz")
            with cs_sprite_change
            cs_mz "До закрытия."
            $ cs_rev_finish_choice(3,9)
    else:
        menu:
            "Предложить Жене помочь с возвращёнными книгами":
                $ cs_rev_choice(3,9,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 5258934c50ec1d0e9930
                cs_ls "Тебе вечером помочь с книгами?"
                cs_ls "Даша тоже свободна."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Я свободна?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Ты свободна."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                # cs_page_anchor: fad58b47eb0a5185d1aa
                cs_mz "Если не будете шуметь."
                cs_mz "После ужина."
                $ cs_rev_award("3:9:cs_friend_mz","cs_friend_mz",1)
                $ cs_mz_evening_help_day3 = True
                $ cs_rev_finish_choice(3,9)
            "Не вмешиваться и пожелать хорошего вечера":
                $ cs_rev_choice(3,9,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 880bb9c4441415c7e6b6
                cs_ls "Хорошего вечера, Жень."
                cs_ls "Я ещё зайду — дочитать."
                $ cs_rev_focus("mz")
                with cs_sprite_change
                cs_mz "До закрытия."
                $ cs_rev_finish_choice(3,9)
    # cs_page_anchor: 1a2ddf64131995fc422f
    cs_narrator "После ужина Женя ушла в библиотеку."
    cs_narrator "Мне нужно было забрать из домика Гончарова."
    $ cs_rev_room('bg ext_square_sunset')
    cs_narrator "На площади Семён и Славя склонились над листом с завтрашними поручениями."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Совещание?"
    $ cs_rev_focus("sy")
    with cs_sprite_change
    cs_sy "Совещание."
    if cs_friend_se >= 2 and cs_se_day3_personal_talk:
        $ cs_rev_focus("sy")
        with cs_sprite_change
        cs_sy "Комиссия постановила: Соколова сегодня ведёт себя подозрительно прилично."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 432a1561bb58d71f5948
        cs_ls "Протестую."
        cs_ls "У меня алиби — Гончаров."
    cs_narrator "Славя показала мне лист."
    $ cs_rev_focus("sl")
    with cs_sprite_change
    # cs_page_anchor: f7d29402b74538fe5f97
    cs_sl "Мне завтра ещё расписание кружков переписать."
    cs_sl "А я в нём уже сама путаюсь."
    # cs_page_anchor: 1289294ada015e4a35ae
    cs_narrator "Раньше я бы непременно пошутила про Семёна-секретаря."
    cs_narrator "Сейчас промолчала."
    cs_narrator "Я обещала."
    $ cs_rev_snapshot("cs_sl_friend_before_evening_choice","cs_friend_sl")
    if "3:10" in cs_rev_choices:
        if cs_rev_choices["3:10"]==0:
            $ cs_rev_choice(3,10,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 88bf70f8302a8a01ebed
            cs_ls "Давай посмотрим."
            cs_ls "Я хорошо вижу, где таблица врёт."
            cs_narrator "Мы за пять минут нашли два кружка, назначенных на одно время."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            # cs_page_anchor: 8ab395a5d1a451fb2e72
            cs_sl "Ой."
            cs_sl "Спасибо!"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 25cf5208ad684e9bad3d
            cs_ls "А объявление с расписанием давай я завтра оформлю."
            cs_ls "Буквы у меня ровные."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            # cs_page_anchor: f41da5f239af481543ad
            cs_sl "Правда?"
            cs_sl "Тогда завтра."
            $ cs_rev_award("3:10:cs_friend_sl","cs_friend_sl",1)
            $ cs_sl_evening_schedule_help_day3 = True
            $ cs_sl_day4_notice_offer = True
            $ cs_rev_finish_choice(3,10)
        else:
            $ cs_rev_choice(3,10,1)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 4a9d5924a7b21907b740
            cs_ls "Удачи вам."
            cs_ls "Меня ждёт Гончаров."
            $ cs_rev_focus("sl")
            with cs_sprite_change
            # cs_page_anchor: a23e3a2f6d850174cc38
            cs_sl "Иди."
            cs_sl "Ты сегодня и так помогла."
            $ cs_rev_finish_choice(3,10)
    else:
        menu:
            "Предложить сверить завтрашние поручения и помочь с объявлением":
                $ cs_rev_choice(3,10,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 399c4f8a8129dba066e0
                cs_ls "Давай посмотрим."
                cs_ls "Я хорошо вижу, где таблица врёт."
                cs_narrator "Мы за пять минут нашли два кружка, назначенных на одно время."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                # cs_page_anchor: 5d0b0c25d99c13a0bd40
                cs_sl "Ой."
                cs_sl "Спасибо!"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 5904e28aaed382605127
                cs_ls "А объявление с расписанием давай я завтра оформлю."
                cs_ls "Буквы у меня ровные."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                # cs_page_anchor: af5a8d54c78ecb1caab8
                cs_sl "Правда?"
                cs_sl "Тогда завтра."
                $ cs_rev_award("3:10:cs_friend_sl","cs_friend_sl",1)
                $ cs_sl_evening_schedule_help_day3 = True
                $ cs_sl_day4_notice_offer = True
                $ cs_rev_finish_choice(3,10)
            "Пожелать удачи и идти за книгой":
                $ cs_rev_choice(3,10,1)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 1b739daf39075733d076
                cs_ls "Удачи вам."
                cs_ls "Меня ждёт Гончаров."
                $ cs_rev_focus("sl")
                with cs_sprite_change
                # cs_page_anchor: 1d200e1474381f551c15
                cs_sl "Иди."
                cs_sl "Ты сегодня и так помогла."
                $ cs_rev_finish_choice(3,10)
    cs_narrator "Я сходила в домик за книгой и вернулась через площадь."
    stop music fadeout 1.5
    cs_narrator "Часы на столбе показывали без одной минуты двенадцать."
    # cs_page_anchor: 13f42435f752e1e70457
    cs_narrator "Я остановилась."
    cs_narrator "Солнце ещё не село."
    cs_narrator "Какая полночь?"
    # cs_page_anchor: 3981fae4415ab1eac121
    cs_narrator "Моргнула."
    cs_narrator "Стрелки стояли на восьми вечера."
    cs_narrator "Наверное, я просто не так посмотрела."
    return

label cs_rev_d3_12:
    $ cs_rev_begin(3,12,['cs_darya', 'cs_zhenya'])
    $ save_name = "Чужая смена — День 3: Последняя страница"
    $ cs_rev_time("sunset")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_library_interior_evening")
    if cs_mz_evening_help_day3:
        # cs_page_anchor: 9d0b6897207b17c1f04b
        cs_narrator "Даша уже была в библиотеке."
        cs_narrator "Женя выдала нам стопку возвращённых книг и строгую инструкцию: по номерам, а не по цвету обложки."
        cs_narrator "Мы расставили всё за пятнадцать минут."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: e5ebba10acc52220ff28
        cs_mz "Неплохо."
        cs_mz "Даже ничего не перепутали."
        $ cs_rev_focus("da")
        with cs_sprite_change
        # cs_page_anchor: 24fb4a5f5d9496b379c6
        cs_da "Это я."
        cs_da "Лена путала."
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Предательство."
        $ cs_mz_evening_help_completed_day3 = True
    $ cs_rev_time('night')
    $ cs_rev_room('cs_library_interior_night')
    $ cs_pov_begin()
    with cs_sprite_leave
    # cs_page_anchor: bfbba37033c47711cad5
    cs_narrator "Я села за стол и открыла Гончарова."
    cs_narrator "Оставалось немного."
    if cs_friend_mz >= 3:
        cs_narrator "Женя сама принесла мне лампу поближе."
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 166e23d7ef35fcfdd149
        cs_mz "Дочитывай."
        cs_mz "Мне интересно, что скажешь о финале."
    else:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        cs_mz "Через двадцать минут закрываю."
    cs_narrator "Последняя страница."
    # cs_page_anchor: 0d3ca38917f581984652
    cs_narrator "Племянник, который приехал с мечтами, стал похож на своего дядю."
    cs_narrator "Деловой, спокойный, разумный."
    cs_narrator "И почему-то от этого было грустно."
    cs_narrator "Я закрыла книгу."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 5ffe094731f53d0d38ad
    cs_ls "Он вырос."
    cs_ls "И потерял что-то по дороге."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "Или нашёл."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 80c129082f155d712c25
    cs_ls "Или нашёл."
    cs_ls "Обыкновенная история."
    if cs_mz_day3_honest_book_talk:
        $ cs_rev_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 9a770360a7603d40e88e
        cs_mz "Ты днём сказала, что он думал, будто знает, как устроен мир."
        cs_mz "А в конце?"
        $ cs_rev_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 6bf4f784817617b5b1b7
        cs_ls "В конце он перестал удивляться."
        cs_ls "Вот этого я больше всего боюсь."
        # cs_page_anchor: 270f7d68da9259bf1e80
        cs_narrator "Женя ничего не ответила."
        cs_narrator "Но посмотрела на меня внимательнее, чем обычно."
        $ cs_mz_day3_final_discussion = True
    # cs_page_anchor: 045cdefe541000542bf6
    cs_narrator "Я вернула книгу."
    cs_narrator "Женя записала возврат."
    $ cs_mz_book_finished_day3 = True
    $ cs_rev_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: a39e65ee6297084c5507
    cs_mz "Завтра подберу тебе что-нибудь следующее."
    cs_mz "Если придёшь."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Приду."
    $ cs_rev_focus("mz")
    with cs_sprite_change
    cs_mz "До завтра, Лена."
    # cs_page_anchor: 1f58da13d1b144d249cd
    cs_narrator "Она впервые назвала меня по имени."
    cs_narrator "Я сделала вид, что не заметила."
    return

label cs_rev_d3_13:
    $ cs_rev_begin(3,13,['cs_darya'])
    $ save_name = "Чужая смена — День 3: Девушка, которая ждала"
    $ cs_rev_time("night")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_library_exterior_night")
    $ cs_rev_music(cs_day_music_think,0.12,2.5)
    cs_narrator "Когда я вышла из библиотеки, на крыльце сидела Даша."
    if cs_mz_evening_help_day3:
        $ cs_rev_focus("da")
        with cs_sprite_change
        # cs_page_anchor: a2d844b683b3e22f0987
        cs_da "Я вышла подышать, пока ты дочитывала."
        cs_da "Решила подождать."
    else:
        $ cs_rev_focus("da")
        with cs_sprite_change
        # cs_page_anchor: db3b7943e82c73ddb69e
        cs_da "Я подумала, что ты будешь читать до последнего."
        cs_da "И решила подождать."
    $ cs_da_waiting_outside_library_day3 = True
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Долго ждала?"
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 916cb394ea3721b3933f
    cs_da "Не очень."
    cs_da "Тут хорошо сидеть."
    cs_da "Тихо."
    $ cs_rev_room('bg ext_square_night')
    $ cs_rev_sfx('sound/sfx/owl_far.ogg',0.18)
    # cs_page_anchor: f45df585d41dcac36cdc
    cs_narrator "Мы пошли к домику через площадь."
    cs_narrator "Фонари горели через один."
    cs_narrator "Где-то в домиках ещё смеялись."
    cs_narrator "У столба с часами я невольно подняла голову."
    # cs_page_anchor: 6d187c193211fc5f42e9
    cs_narrator "Половина одиннадцатого."
    cs_narrator "Нормальные стрелки."
    cs_narrator "Нормальное время."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Что?"
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1ea387482466933f60fb
    cs_ls "Ничего."
    cs_ls "Вечером мне показалось, что эти часы стоят на без одной минуты двенадцать."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Тебе сегодня многое кажется."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 502a8398ea172b65aeff
    cs_ls "Мотор утром."
    cs_ls "Листок в администрации."
    cs_ls "Часы."
    cs_ls "И Виола, которая будто бы уже перевязывала мне этот локоть."
    cs_narrator "Даша остановилась."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Ты мне это всё не рассказывала."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 011d9fab0f1bc0a86fc5
    cs_ls "Рассказываю."
    cs_ls "Сейчас."
    $ cs_rev_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 4a51894a457d595c75d1
    cs_da "Лен."
    cs_da "Это всё вместе — уже не «кажется»."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: c512877da6f6fc23837d
    cs_ls "Знаю."
    cs_ls "Поэтому и рассказываю тебе, а не держу в голове."
    if "3:11" in cs_rev_choices:
        if cs_rev_choices["3:11"]==0:
            $ cs_rev_choice(3,11,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 6975233c284b7c237690
            cs_ls "Знаешь, чего я боюсь больше петли?"
            cs_ls "Что однажды проснусь — и мне не захочется домой."
            cs_narrator "Даша посмотрела на меня."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Мне днём то же самое пришло в голову."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 836c5627be04bedbceb0
            cs_ls "Тогда давай так."
            cs_ls "Если кто-то из нас начнёт слишком привыкать — другая напомнит."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Про Москву?"
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: e862f088016dbc390208
            cs_ls "Про «Мивину» над планшетом."
            cs_ls "Самое страшное, что я могу вспомнить."
            # cs_page_anchor: 788c5ba176866e6777d5
            cs_narrator "Даша рассмеялась."
            cs_narrator "И взяла меня под руку."
            $ cs_rev_award("3:11:cs_friend_da","cs_friend_da",1)
            $ cs_da_day3_fear_of_getting_used_to_camp = True
            $ cs_rev_finish_choice(3,11)
        else:
            $ cs_rev_choice(3,11,1)
            # cs_page_anchor: cc0835959091a2ca5a0e
            cs_narrator "Я ничего не стала говорить."
            cs_narrator "Мы шли рядом, и этого было достаточно."
            # cs_page_anchor: b800f44b174aec89040c
            cs_narrator "Даша чуть задела моё плечо своим."
            cs_narrator "Случайно или нет — я не стала уточнять."
            $ cs_da_day3_shared_silence = True
            $ cs_rev_finish_choice(3,11)
    else:
        menu:
            "Сказать Даше, что страшно не только застрять, но и привыкнуть":
                $ cs_rev_choice(3,11,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 66a846e01d682cdf7cad
                cs_ls "Знаешь, чего я боюсь больше петли?"
                cs_ls "Что однажды проснусь — и мне не захочется домой."
                cs_narrator "Даша посмотрела на меня."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Мне днём то же самое пришло в голову."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 95f6f99e5d1c945240c8
                cs_ls "Тогда давай так."
                cs_ls "Если кто-то из нас начнёт слишком привыкать — другая напомнит."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Про Москву?"
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: e3141c4e4e2b00250389
                cs_ls "Про «Мивину» над планшетом."
                cs_ls "Самое страшное, что я могу вспомнить."
                # cs_page_anchor: 589cfaec0bcc422e3866
                cs_narrator "Даша рассмеялась."
                cs_narrator "И взяла меня под руку."
                $ cs_rev_award("3:11:cs_friend_da","cs_friend_da",1)
                $ cs_da_day3_fear_of_getting_used_to_camp = True
                $ cs_rev_finish_choice(3,11)
            "Просто помолчать вместе":
                $ cs_rev_choice(3,11,1)
                # cs_page_anchor: aece85d3517bbc31dafe
                cs_narrator "Я ничего не стала говорить."
                cs_narrator "Мы шли рядом, и этого было достаточно."
                # cs_page_anchor: f3fe2029744723fcbeba
                cs_narrator "Даша чуть задела моё плечо своим."
                cs_narrator "Случайно или нет — я не стала уточнять."
                $ cs_da_day3_shared_silence = True
                $ cs_rev_finish_choice(3,11)
    cs_narrator "Домик был совсем рядом."
    return

label cs_rev_d3_14:
    $ cs_rev_begin(3,14,['cs_darya'])
    $ save_name = "Чужая смена — День 3: Ближе, чем вчера"
    $ cs_rev_time("night")
    $ cs_rev_costume("pioneer")
    $ cs_rev_room("cs_house_lena_darya_int_night")
    $ cs_rev_snapshot("cs_da_friend_before_night","cs_friend_da")
    $ cs_rev_knocks(2,0.45)
    # cs_page_anchor: b3b4c0a4d1a9706f5a46
    cs_narrator "В домике мы переоделись по очереди."
    cs_narrator "На этот раз я постучала."
    cs_narrator "Дважды."
    $ cs_rev_focus("da")
    with cs_sprite_change
    cs_da "Прогресс."
    $ cs_rev_focus("ls")
    with cs_sprite_change
    cs_ls "Я обучаемая."
    cs_narrator "Мы сели каждая на свою кровать."
    # cs_page_anchor: 91de2e1f62acf1ca8b2e
    cs_narrator "Вчера я спросила."
    cs_narrator "Вчера Даша сказала «нет»."
    cs_narrator "Это не было обещанием «завтра да»."
    cs_narrator "И я это помнила."
    if "3:12" in cs_rev_choices:
        if cs_rev_choices["3:12"]==0:
            $ cs_rev_choice(3,12,0)
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: f5a5c74dba64d83556cd
            cs_ls "Даш."
            cs_ls "Я помню, что вчера ты сказала."
            cs_ls "Поэтому спрашиваю ещё раз, а не считаю, что ответ поменялся."
            cs_ls "Можно сегодня рядом?"
            cs_ls "Если нет — правда ничего страшного."
            $ cs_da_bed_request_day3 = True
            if cs_da_friend_before_night >= 1:
                # cs_page_anchor: e7a5bad85758fbf094b5
                cs_narrator "Даша помолчала."
                cs_narrator "Потом подвинулась к стене."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: 9342f76dbdb5bc7732c5
                cs_da "Можно."
                cs_da "Только одеяло пополам."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                cs_ls "Справедливое распределение ресурсов."
                $ cs_rev_music("sound/music/a_promise_from_distant_days.ogg",0.12)
                $ cs_day03_sketchbook_location = "cabin_table"
                # cs_page_anchor: 15fbc570c904d4ea1080
                cs_narrator "Я осторожно легла, оставив больной руке место."
                cs_narrator "Даша придвинулась сзади так, чтобы не задеть повязку."
                $ cs_da_shared_bed_day3 = True
                $ cs_rev_award("3:12:cs_friend_da","cs_friend_da",1)
            else:
                # cs_page_anchor: c55988bb2f6ec90709d4
                cs_narrator "Даша посмотрела на меня."
                cs_narrator "Мягко."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: 90c9be02cde60c034461
                cs_da "Лен."
                cs_da "Пока нет."
                cs_da "Не потому, что ты что-то не так сделала."
                cs_da "Мне просто нужно ещё немного своего места."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 95b90182d60c7556e321
                cs_ls "Поняла."
                cs_ls "Спасибо, что сказала прямо."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Спасибо, что спросила прямо."
                $ cs_da_shared_bed_day3 = False
            $ cs_rev_finish_choice(3,12)
        else:
            $ cs_rev_choice(3,12,1)
            cs_narrator "Я ничего не стала спрашивать."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Ты сегодня тихая."
            $ cs_rev_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: a102c7d1a3d453458180
            cs_ls "Даю тебе пространство."
            cs_ls "Вчера ты его просила."
            cs_narrator "Даша улыбнулась."
            $ cs_rev_focus("da")
            with cs_sprite_change
            cs_da "Это очень мило, Лен."
            $ cs_da_respected_space_day3 = True
            $ cs_da_shared_bed_day3 = False
            $ cs_rev_finish_choice(3,12)
    else:
        menu:
            "Сказать Даше, что сегодня хочется спать рядом":
                $ cs_rev_choice(3,12,0)
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 446dcb936559e0a80162
                cs_ls "Даш."
                cs_ls "Я помню, что вчера ты сказала."
                cs_ls "Поэтому спрашиваю ещё раз, а не считаю, что ответ поменялся."
                cs_ls "Можно сегодня рядом?"
                cs_ls "Если нет — правда ничего страшного."
                $ cs_da_bed_request_day3 = True
                if cs_da_friend_before_night >= 1:
                    # cs_page_anchor: 2260f0db5a5dbbaba788
                    cs_narrator "Даша помолчала."
                    cs_narrator "Потом подвинулась к стене."
                    $ cs_rev_focus("da")
                    with cs_sprite_change
                    # cs_page_anchor: b6856579f47b05fccda5
                    cs_da "Можно."
                    cs_da "Только одеяло пополам."
                    $ cs_rev_focus("ls")
                    with cs_sprite_change
                    cs_ls "Справедливое распределение ресурсов."
                    $ cs_rev_music("sound/music/a_promise_from_distant_days.ogg",0.12)
                    $ cs_day03_sketchbook_location = "cabin_table"
                    # cs_page_anchor: fab29c4fa303b3f5c9bf
                    cs_narrator "Я осторожно легла, оставив больной руке место."
                    cs_narrator "Даша придвинулась сзади так, чтобы не задеть повязку."
                    $ cs_da_shared_bed_day3 = True
                    $ cs_rev_award("3:12:cs_friend_da","cs_friend_da",1)
                else:
                    # cs_page_anchor: 7915105805f5befc03dd
                    cs_narrator "Даша посмотрела на меня."
                    cs_narrator "Мягко."
                    $ cs_rev_focus("da")
                    with cs_sprite_change
                    # cs_page_anchor: 6e88720ec59b344645ea
                    cs_da "Лен."
                    cs_da "Пока нет."
                    cs_da "Не потому, что ты что-то не так сделала."
                    cs_da "Мне просто нужно ещё немного своего места."
                    $ cs_rev_focus("ls")
                    with cs_sprite_change
                    # cs_page_anchor: 2385d8cca74c2f77efad
                    cs_ls "Поняла."
                    cs_ls "Спасибо, что сказала прямо."
                    $ cs_rev_focus("da")
                    with cs_sprite_change
                    cs_da "Спасибо, что спросила прямо."
                    $ cs_da_shared_bed_day3 = False
                $ cs_rev_finish_choice(3,12)
            "Не торопить события":
                $ cs_rev_choice(3,12,1)
                cs_narrator "Я ничего не стала спрашивать."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Ты сегодня тихая."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: 590cb3af254620e5dfb3
                cs_ls "Даю тебе пространство."
                cs_ls "Вчера ты его просила."
                cs_narrator "Даша улыбнулась."
                $ cs_rev_focus("da")
                with cs_sprite_change
                cs_da "Это очень мило, Лен."
                $ cs_da_respected_space_day3 = True
                $ cs_da_shared_bed_day3 = False
                $ cs_rev_finish_choice(3,12)
    if cs_da_shared_bed_day3:
        # cs_page_anchor: 397ca14e7aa8d03d35ce
        cs_narrator "Мы лежали рядом в темноте."
        cs_narrator "Даша нашла мою здоровую руку и чуть сжала."
        $ cs_rev_focus("da")
        with cs_sprite_change
        # cs_page_anchor: 2d53a227ed836b3c33b8
        cs_da "Мне сегодня понравилось."
        cs_da "День."
        cs_da "И сейчас тоже хорошо."
        if "3:13" in cs_rev_choices:
            if cs_rev_choices["3:13"]==0:
                $ cs_rev_choice(3,13,0)
                cs_narrator "Я повернулась к ней."
                # cs_page_anchor: 6b500e0c0f05881f6716
                cs_narrator "В Москве я спокойно говорила с тысячами людей."
                cs_narrator "А сейчас голос почему-то стал тише."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: e2a165b2ac2ad58bf73a
                cs_ls "Даш."
                cs_ls "Я тебя люблю."
                # cs_page_anchor: 38d9a7f8eb567fd77dc2
                cs_narrator "Даша долго молчала."
                cs_narrator "Я успела пожалеть обо всём на свете."
                cs_narrator "Потом она уткнулась лбом мне в плечо."
                $ cs_rev_focus("da")
                with cs_sprite_change
                # cs_page_anchor: fa8f3a711c61717c301e
                cs_da "Я знаю."
                cs_da "Я тоже…"
                cs_da "Мне просто страшно говорить это здесь."
                cs_da "Как будто, если скажу, лагерь услышит."
                $ cs_rev_focus("ls")
                with cs_sprite_change
                # cs_page_anchor: dab93429ed28f6d4e61f
                cs_ls "Пусть слышит."
                cs_ls "Ему полезно."
                cs_narrator "Даша тихо рассмеялась в подушку."
                $ cs_da_love_confession_day3 = True
                $ cs_rev_finish_choice(3,13)
            else:
                $ cs_rev_choice(3,13,1)
                # cs_page_anchor: 85ac238859973641882e
                cs_narrator "Слова были совсем рядом."
                cs_narrator "Но я решила, что им не нужно торопиться."
                cs_narrator "Иногда достаточно просто лежать рядом и знать."
                $ cs_da_unspoken_feelings_day3 = True
                $ cs_rev_finish_choice(3,13)
        else:
            menu:
                "Сказать Даше три слова":
                    $ cs_rev_choice(3,13,0)
                    cs_narrator "Я повернулась к ней."
                    # cs_page_anchor: 56d99ea0df001bcdec3e
                    cs_narrator "В Москве я спокойно говорила с тысячами людей."
                    cs_narrator "А сейчас голос почему-то стал тише."
                    $ cs_rev_focus("ls")
                    with cs_sprite_change
                    # cs_page_anchor: e51ad356d86188cfcbe1
                    cs_ls "Даш."
                    cs_ls "Я тебя люблю."
                    # cs_page_anchor: 53259077a316b573a419
                    cs_narrator "Даша долго молчала."
                    cs_narrator "Я успела пожалеть обо всём на свете."
                    cs_narrator "Потом она уткнулась лбом мне в плечо."
                    $ cs_rev_focus("da")
                    with cs_sprite_change
                    # cs_page_anchor: 9792803b1155614d6fc9
                    cs_da "Я знаю."
                    cs_da "Я тоже…"
                    cs_da "Мне просто страшно говорить это здесь."
                    cs_da "Как будто, если скажу, лагерь услышит."
                    $ cs_rev_focus("ls")
                    with cs_sprite_change
                    # cs_page_anchor: 2baa0ae29bd295a5f154
                    cs_ls "Пусть слышит."
                    cs_ls "Ему полезно."
                    cs_narrator "Даша тихо рассмеялась в подушку."
                    $ cs_da_love_confession_day3 = True
                    $ cs_rev_finish_choice(3,13)
                "Оставить слова на потом":
                    $ cs_rev_choice(3,13,1)
                    # cs_page_anchor: 2c2bb7bcf637c7d3fd5a
                    cs_narrator "Слова были совсем рядом."
                    cs_narrator "Но я решила, что им не нужно торопиться."
                    cs_narrator "Иногда достаточно просто лежать рядом и знать."
                    $ cs_da_unspoken_feelings_day3 = True
                    $ cs_rev_finish_choice(3,13)
        $ cs_rev_focus("ls")
        with cs_sprite_change
        cs_ls "Но если ночью одеяло окажется на моей стороне — это непреднамеренное изменение границ."
        $ cs_rev_focus("da")
        with cs_sprite_change
        cs_da "Всё, спи уже."
    else:
        cs_narrator "Даша спала на своей кровати, в нескольких шагах от меня."
        cs_narrator "И даже на этом расстоянии я знала, что мы не чужие друг другу."
    if cs_da_shared_bed_day3:
        $ cs_rev_room("cs_cg_lena_darya_shared_sleep_night")
        $ cs_da_shared_sleep_cg_seen_day3 = True
    else:
        $ cs_rev_room("cs_house_lena_darya_int_sleep_night")
    $ cs_pov_begin()
    with cs_sprite_leave
    stop music fadeout 2.0
    cs_narrator "Я закрыла глаза."
    # cs_page_anchor: fbe07d8a5cd2285d5012
    cs_narrator "Третий день."
    cs_narrator "Прочитанная книга, которую хочется обсуждать."
    cs_narrator "Рисунок, который хочется закончить."
    cs_narrator "Люди, которых хочется увидеть завтра."
    # cs_page_anchor: e2014c167c283b482c89
    cs_narrator "И всё ещё хочется домой."
    cs_narrator "В Москву."
    cs_narrator "К собственной жизни."
    cs_narrator "Но, кажется, за эти дни здесь появилась маленькая её часть."
    cs_narrator "Мысли путались."
    # cs_page_anchor: 6950ed0f86fd21089312
    cs_narrator "На самом краю сна мне привиделась остановка у ворот."
    cs_narrator "Солнечный свет."
    cs_narrator "Табличка с номером маршрута."
    cs_narrator "И в окне автобуса — моё собственное лицо."
    # cs_page_anchor: b9a8a1a419091e4b7a8f
    cs_narrator "Оно смотрело на меня и что-то говорило."
    cs_narrator "Беззвучно."
    cs_narrator "Я хотела разобрать слова, но сон уже утянул меня глубже."
    cs_narrator "К утру я этого не вспомню."
    # cs_page_anchor: 3304ae43f9f2168bf824
    cs_narrator "Вспомню позже."
    cs_narrator "Когда будет уже совсем не до сна."
    return
