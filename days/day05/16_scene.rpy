# -*- coding: utf-8 -*-
label cs_day05_16:
    $ cs_d5_scene = 16
    $ save_name = "Чужая смена — День 5: К вечеру"
    $ cs_bus_scene_enter(16)
    $ cs_d5_room("bg int_library_day")
    cs_narrator "Виола выслушала нас спокойно."
    cs_narrator "Она не перебивала."
    cs_narrator "Только иногда задавала уточняющие вопросы."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Кто первым услышал голос?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Я. Но остальные тоже слышали."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Слова были одинаковыми для всех?"
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 95cc7e767d5b3f8938b6
    cs_mz "Да."
    cs_mz "Семь стуков, потом имя Семёна и слово «сегодня»."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "А дверь?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 41228ac58e65d7b3ac07
    cs_da "Ручка опустилась."
    cs_da "Но внутрь никто не вошёл."
    cs_narrator "Виола записала несколько строк."
    cs_narrator "Я наблюдала за ней и впервые за долгое время радовалась, что разговор ведёт кто-то другой."
    cs_narrator "Моё желание самостоятельно расследовать всё на свете заметно уменьшилось."
    cs_narrator "Возможно, это называлось взрослением."
    cs_narrator "Или усталостью."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    # cs_page_anchor: db1e3539b863a8d0d250
    cs_vi "Хорошо."
    cs_vi "Пока больше ничего не проверяйте."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "С удовольствием."
    cs_narrator "Она посмотрела на меня."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Даже не споришь?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я сегодня удивительно послушная."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Надо запомнить дату."
    cs_narrator "Я вздохнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вы все сговорились."
    cs_narrator "Вожатая положила на стол папку."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 37e41bcd7a3ca657c700
    cs_mt "Вечером собираемся возле моего домика."
    cs_mt "Там будем все вместе."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Дежурить?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 16a4ddd77e01e19073cd
    cs_mt "Сначала просто посидим."
    cs_mt "Обсудим, что знаем."
    cs_mt "И посмотрим, повторится ли что-нибудь."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Во сколько?"
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "В девять."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: e6b276fd0dd1cce196e0
    cs_da "Хорошо."
    cs_da "Мы придём."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 3cc7216e48dd859cdf2f
    cs_mt "Славю, Алису и Мику я предупрежу сама."
    cs_mt "Кто захочет — придёт."
    cs_mt "И будем следить за временем: принесите часы, у кого есть."
    cs_narrator "Я посмотрела на листы."
    cs_narrator "За сегодняшний день их стало заметно больше."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 20430613fe030dd4cd91
    cs_ls "Надо каждому сделать копию."
    cs_ls "Не хочется, чтобы всё хранилось в одной папке."
    cs_narrator "Женя кивнула."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 10389552d4d47b5aeaa2
    cs_mz "Давайте."
    cs_mz "Я дам бумагу."
    cs_narrator "Мы принялись переписывать записи."
    cs_narrator "Я осторожно вывела своё имя."
    cs_narrator "Потом дату."
    cs_narrator "Затем кратко записала, что произошло у ворот."
    cs_narrator "Автобус."
    cs_narrator "Голос."
    cs_narrator "Отражение."
    cs_narrator "Конверт."
    cs_narrator "После этого — стуки у библиотеки."
    cs_narrator "Я перечитала написанное."
    cs_narrator "Выглядело как сюжет дешёвого фильма ужасов."
    cs_narrator "Но я сама всё это видела."
    cs_narrator "И остальные тоже."
    cs_narrator "Семён сидел напротив и пытался вспомнить, когда именно впервые услышал двигатель."
    cs_narrator "Даша помогала раскладывать листы."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Женя следила, чтобы мы не перепутали оригиналы и копии."
    cs_narrator "Тихонова зарисовывала отметки на косяке."
    cs_narrator "Работали мы медленно."
    cs_narrator "Но впервые за день никто не пытался командовать всеми сразу."
    cs_narrator "Это было приятно."
    cs_narrator "Я посмотрела на свои записи."
    cs_narrator "Всё утро я шутила, задавала вопросы и пыталась делать вид, что понимаю, куда нам двигаться дальше."
    cs_narrator "Но теперь, когда передо мной лежали листы с собственными словами, хотелось признать одну простую вещь."
    cs_narrator "Мне было страшно."
    cs_narrator "И я совершенно не знала, что делать."
    menu:
        "Сказать Даше и Семёну, что мне тоже страшно":
            $ cs_d5_choose(5, 0)
            cs_narrator "Я положила карандаш."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Слушайте."
            cs_narrator "Даша подняла глаза."
            $ cs_d5_focus("da")
            with cs_sprite_change
            cs_da "Что?"
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Я, кажется, должна кое-что сказать."
            cs_narrator "Семён отложил листок."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Только не про новый план."
            cs_narrator "Я усмехнулась."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 7dfc3d1f85be028253a8
            cs_ls "Как раз наоборот."
            cs_ls "Никакого плана у меня нет."
            cs_narrator "Он посмотрел внимательнее."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 62f87bd901b43e89b23b
            cs_ls "Я весь день шучу, потому что боюсь."
            cs_ls "Мне кажется, если всё время острить, будет не так страшно."
            cs_narrator "Даша молчала."
            cs_narrator "Я продолжила."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "А на самом деле я понятия не имею, что нас ждёт вечером."
            cs_narrator "Семён немного помолчал."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Вообще-то это заметно."
            cs_narrator "Я посмотрела на него."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Мог бы хотя бы изобразить удивление."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: 9df91dd24f6c0bf653f2
            cs_sy "Извини."
            cs_sy "Я берегу актёрское мастерство."
            cs_narrator "Я рассмеялась."
            cs_narrator "Даша села рядом."
            $ cs_d5_focus("da")
            with cs_sprite_change
            cs_da "Тебе необязательно всё время держать лицо."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Знаю."
            $ cs_d5_focus("da")
            with cs_sprite_change
            cs_da "Тогда иногда вспоминай об этом."
            cs_narrator "Я кивнула."
            cs_narrator "Семён взял свой лист."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            # cs_page_anchor: fa545f581a45e17a7f69
            cs_sy "Я тоже боюсь."
            cs_sy "Особенно после того автобуса."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Понимаю."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Но мне спокойнее, когда мы хотя бы можем нормально поговорить."
            cs_narrator "Я посмотрела на него."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 0b73de51806f0173c677
            cs_ls "Тогда договорились."
            cs_ls "Без лишнего геройства."
            $ cs_d5_focus("da")
            with cs_sprite_change
            cs_da "Вот это уже похоже на хороший план."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Первый за сегодня?"
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Не будем считать."
        "Не обсуждать чувства, а заняться подготовкой":
            $ cs_d5_choose(5, 1)
            cs_narrator "Я решила не обсуждать сейчас собственные переживания."
            cs_narrator "Если начну, могу окончательно потерять способность сосредоточиться."
            cs_narrator "Вместо этого взяла чистый лист."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Давайте лучше проверим, что нам понадобится вечером."
            $ cs_d5_focus("da")
            with cs_sprite_change
            cs_da "Например?"
            $ cs_d5_focus("ls")
            with cs_sprite_change
            # cs_page_anchor: 5364ef6576e01a8c07b3
            cs_ls "Фонарики."
            cs_ls "Часы."
            cs_ls "Бумага."
            cs_ls "Вода."
            $ cs_d5_focus("sy")
            with cs_sprite_change
            cs_sy "Фонарик у Алисы можно взять."
            $ cs_d5_focus("mz")
            with cs_sprite_change
            cs_mz "Бумагу я принесу."
            $ cs_d5_focus("da")
            with cs_sprite_change
            cs_da "Тогда я помогу с остальным."
            cs_narrator "Она посмотрела на меня."
            $ cs_d5_focus("da")
            with cs_sprite_change
            # cs_page_anchor: f8244e25aa886d9d6872
            cs_da "Только себе тоже копию оставь."
            cs_da "А то раздашь все и останешься без записей."
            cs_narrator "Я посмотрела на лист."
            $ cs_d5_focus("ls")
            with cs_sprite_change
            cs_ls "Хорошо."
            cs_narrator "Даша положила передо мной одну из записей."
            cs_narrator "Я сложила её и убрала в карман."
    cs_narrator "Когда с записями было закончено, Ольга Дмитриевна разрешила нам немного отдохнуть."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 9057c243f3b43b8aea65
    cs_mt "До девяти ещё есть время."
    cs_mt "Займитесь обычными делами."
    cs_mt "Только не ходите по одному туда, где никого нет."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "И обязательно поешьте."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1b67981b4e5d19447023
    cs_ls "Удивительно."
    cs_ls "Сегодня мне уже второй раз официально назначают еду."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "В твоём случае это неплохое лечение."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Я прослежу."
    cs_narrator "Я посмотрела на неё."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Предательство."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Забота."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Очень удобно называть это именно так."
    $ cs_actor_exit(["mt", "cs"])
    $ cs_d5_cast = []
    cs_narrator "Ольга Дмитриевна и Виола ушли по своим делам."
    cs_narrator "Мы остались в библиотеке."
    cs_narrator "Женя достала с нижней полки стопку старых формуляров."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Раз вы всё равно здесь, можете помочь."
    cs_narrator "Я посмотрела на карточки."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 5a2a603a15f9f5b49e28
    cs_ls "Конечно."
    cs_ls "Даже после загадочного автобуса библиотечная работа не заканчивается."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Книги сами себя не приведут в порядок."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Жестокая реальность."
    cs_narrator "Мы взялись за дело."
    cs_narrator "Семён сортировал карточки."
    cs_narrator "Даша помогала подклеивать обложки."
    cs_narrator "Я получила несколько повреждённых книг и строгую инструкцию не трогать тяжёлые стопки."
    cs_narrator "Тихонова закончила рисунок фотографии, затем села рядом со мной."
    cs_narrator "На столе лежала чистая бумага."
    cs_narrator "Я не удержалась и начала рисовать стоявшую на подоконнике кружку."
    cs_narrator "Сначала получилась кривая ручка."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Потом я исправила контур."
    cs_narrator "Даша заглянула через плечо."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Настоящая кружка не такая ровная."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я занимаюсь художественным улучшением действительности."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Кружка в курсе?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Сообщу, когда станет знаменитой."
    cs_narrator "Тихонова улыбнулась."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Здесь тень немного не с той стороны."
    cs_narrator "Я посмотрела на рисунок."
    cs_narrator "Она была права."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 96a024da67a008a12b6a
    cs_ls "Спасибо."
    cs_ls "Теперь даже у кружки есть художественный консультант."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Извини."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: e0636620cf1c4b085d07
    cs_ls "За что?"
    cs_ls "Я же сама хотела научиться принимать замечания."
    cs_narrator "Она чуть расслабилась."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Тогда здесь лучше затемнить."
    cs_narrator "Я протянула ей карандаш."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Покажи."
    cs_narrator "Она осторожно провела несколько линий."
    cs_narrator "Кружка действительно стала выглядеть лучше."
    cs_narrator "Я посмотрела на неё с уважением."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ad613a0f06711a4d8e6f
    cs_ls "Всё."
    cs_ls "Забираю тебя в художественный отдел."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Какой отдел?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 91650d30ab477a3b1c4d
    cs_ls "Пока не существует."
    cs_ls "Но перспективы хорошие."
    cs_narrator "Мы обе рассмеялись."
    if cs_friend_un >= 4:
        cs_narrator "Тихонова немного помолчала."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Может, завтра вместе что-нибудь нарисуем?"
        cs_narrator "Я повернулась к ней."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "С удовольствием."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Если будет время."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 6d8ac7d674b751e554bd
        cs_ls "Найдём."
        cs_ls "Ради искусства можно ненадолго отказаться от расследований."
        cs_narrator "Она улыбнулась."
        $ cs_d5_un_day6_sketch_offer = True
    else:
        cs_narrator "Тихонова вернулась к своему альбому."
        cs_narrator "Я не стала отвлекать её."
        cs_narrator "Кажется, нам обеим было приятно просто сидеть рядом и рисовать."
        $ cs_d5_un_day6_sketch_offer = False
    cs_narrator "Время прошло незаметно."
    cs_narrator "Мы закончили с книгами, убрали клей, собрали карточки и вымыли руки."
    cs_narrator "Женя пересчитала ножницы."
    cs_narrator "Одни нашлись под моим рисунком."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Соколова."
    cs_narrator "Я подняла глаза."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Да?"
    cs_narrator "Она показала ножницы."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Я просто хотела проверить твою внимательность."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 5acbaa260a06283bbb7c
    cs_mz "Проверила."
    cs_mz "Теперь убери."
    cs_narrator "Я рассмеялась и вернула их на место."
    $ cs_rev_sfx('sound/sfx/dinner_horn_processed.ogg',0.6)
    cs_narrator "К ужину мы отправились вместе."
    cs_narrator "На этот раз я действительно хотела просто поесть."
    cs_narrator "Без загадок."
    cs_narrator "Без стуков."
    cs_narrator "И желательно без новых объявлений о том, что кто-то должен сделать выбор."
    return
