# -*- coding: utf-8 -*-
label cs_day05_20:
    $ cs_d5_scene = 20
    $ save_name = "Чужая смена — День 5: До рассвета"
    $ cs_bus_scene_enter(20)
    stop music fadeout 1.0
    stop ambience fadeout 0.5
    $ cs_d5_quiet = True
    $ cs_d5_clock = "23:57"
    stop ambience fadeout 0.5
    stop music fadeout 1.0
    show screen cs_d5_clock_face
    cs_narrator "Я проснулась окончательно."
    cs_narrator "Первое, что заметила, — тишину."
    cs_narrator "В комнате ещё шуршали бумаги."
    cs_narrator "Семён немного передвинул стул."
    cs_narrator "Кто-то поставил кружку на стол."
    cs_narrator "Но снаружи не было слышно ничего."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Ни насекомых."
    cs_narrator "Ни ветра."
    cs_narrator "Даже привычного шелеста листвы."
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она тоже заметила."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Ты слышишь?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Именно в этом и проблема."
    cs_narrator "Ольга Дмитриевна встала возле окна."
    cs_narrator "Осторожно отодвинула край занавески."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Все остаются внутри."
    cs_narrator "Никто не возразил."
    cs_narrator "Виола посмотрела на часы."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Ещё несколько минут."
    cs_narrator "Я достала из кармана листок с записями."
    cs_narrator "Бумага немного помялась."
    cs_narrator "На ней всё ещё можно было прочитать моё имя."
    cs_narrator "Дату."
    cs_narrator "Короткое описание утреннего автобуса."
    cs_narrator "Я провела пальцем по строчке."
    cs_narrator "Потом убрала лист обратно."
    if cs_da_shared_bed_day3 and cs_da_love_confession_day3:
        cs_narrator "Я осторожно нашла ладонь Даши под столом."
        cs_narrator "Она сразу сжала мои пальцы."
        cs_narrator "Не сказала ничего."
        cs_narrator "Я тоже промолчала."
    elif cs_friend_da >= 4:
        cs_narrator "Даша положила руку мне на плечо."
        cs_narrator "Я повернулась."
        cs_narrator "Она кивнула."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Я рядом."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Знаю."
    else:
        cs_narrator "Мы с Дашей проверили, что у каждой осталась своя копия записей."
        cs_narrator "Она положила листок на колени."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Всё на месте."
        cs_narrator "Я кивнула."
    if cs_d5_slavya_present:
        cs_narrator "Славя убрала термос подальше от края стола."
        cs_narrator "Затем пересела ближе к двери, но не подходила к ней."
        $ cs_d5_focus("sl")
        with cs_sprite_change
        cs_sl "Если что-нибудь понадобится, скажите."
    if cs_d5_alisa_present:
        cs_narrator "Алиса вошла с веранды."
        $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.3)
        cs_narrator "Закрыла за собой дверь."
        cs_narrator "Фонарик она держала в руке."
        $ cs_d5_focus("dv")
        with cs_sprite_change
        # cs_page_anchor: 451fc421b0a752f5a694
        cs_dv "Снаружи никого."
        cs_dv "И тихо как-то."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Мы заметили."
    if cs_d5_miku_present:
        cs_narrator "Мику подвинула будильник так, чтобы его было видно Виоле."
        $ cs_d5_focus("mi")
        with cs_sprite_change
        cs_mi "Он ещё идёт."
        $ cs_d5_focus("vi")
        with cs_sprite_change
        # cs_page_anchor: 697957b27779a4afc9f2
        cs_vi "Хорошо."
        cs_vi "Сравним со стенными."
    if not cs_d5_slavya_present:
        cs_narrator "Даша убрала термос подальше от края стола."
    if not cs_d5_alisa_present:
        cs_narrator "Ольга Дмитриевна проверила фонарик и положила его рядом."
    if not cs_d5_miku_present:
        cs_narrator "Виола придвинула будильник, чтобы видеть оба циферблата."
    cs_narrator "Я посмотрела на два циферблата."
    cs_narrator "Стенные часы начали отставать."
    cs_narrator "Сначала совсем немного."
    cs_narrator "Потом секундная стрелка остановилась."
    cs_narrator "Подёрнулась."
    cs_narrator "Сделала ещё одно движение."
    cs_narrator "И снова замерла."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вы это видите?"
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Да."
    cs_narrator "Женя поднялась со стула."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "А будильник?"
    cs_narrator "Маленькая стрелка продолжала двигаться."
    cs_narrator "Ещё несколько секунд."
    cs_narrator "Потом остановилась и она."
    cs_narrator "Оба циферблата показывали одно и то же время."
    $ cs_d5_clock = "23:59"
    $ cs_d5_clock_stopped = True
    cs_narrator "23:59."
    cs_narrator "Я посмотрела на часы."
    cs_narrator "Потом на Семёна."
    cs_narrator "Он сидел неподвижно."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Вот и приехали."
    cs_narrator "Никто не ответил."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Шестой день Семёна заканчивался."
    cs_narrator "Если стрелки снова пойдут, начнётся седьмой."
    cs_narrator "Остался один."
    $ cs_bus_cue("cabin_bus")
    cs_narrator "Издалека донёсся звук двигателя."
    cs_narrator "Очень знакомый."
    cs_narrator "Я узнала его сразу."
    cs_narrator "Хотелось закрыть уши."
    cs_narrator "Но это ничего бы не изменило."
    cs_narrator "Звук становился громче."
    $ cs_bus_cue("cabin_bus_stop")
    cs_narrator "Потом оборвался."
    cs_narrator "Будто машина остановилась совсем рядом."
    $ cs_bus_cue("knock_warning")
    $ cs_d5_knocks(7)
    cs_narrator "В дверь постучали."
    cs_narrator "Семь раз."
    $ cs_d5_room("bg int_house_of_mt_night2")
    cs_narrator "На последнем ударе погас свет."
    cs_narrator "Я вздрогнула."
    cs_narrator "В комнате кто-то задел стул."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: eeec6535d81eb04d1ba7
    cs_mt "Все остаются на местах."
    cs_mt "Сейчас включим фонарь."
    cs_narrator "Раздался щелчок."
    cs_narrator "Слабый луч осветил пол."
    cs_narrator "Затем стол."
    cs_narrator "Я увидела Дашу рядом."
    cs_narrator "Семёна напротив."
    cs_narrator "Женю возле шкафа."
    cs_narrator "Тихонову у кровати."
    cs_narrator "Ольгу Дмитриевну с фонариком."
    cs_narrator "Остальные тоже были здесь."
    cs_narrator "Все на месте."
    cs_narrator "Пока."
    cs_narrator "За дверью раздался голос."
    cs_narrator "Мой голос."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Семён."
    cs_narrator "Я почувствовала, как Даша напряглась."
    cs_narrator "Семён поднял голову."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Время выбирать."
    cs_narrator "В комнате стало ещё тише."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Что выбирать?"
    cs_narrator "Ответ прозвучал почти сразу."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    # cs_page_anchor: b41363ddaa8e6f255fe9
    cs_d5_voice "Один остаётся."
    cs_d5_voice "Один возвращается."
    cs_narrator "Я посмотрела на дверь."
    cs_narrator "Говорившая повторяла мой голос до последней интонации."
    cs_narrator "Не просто похожий."
    cs_narrator "Практически такой же."
    cs_narrator "И всё равно это была не я."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Куда возвращается?"
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Домой."
    cs_narrator "Семён медленно выпрямился."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А что будет с остальными?"
    cs_narrator "Ответа пришлось подождать."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Смена закончится."
    cs_narrator "Я нахмурилась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Очень содержательно."
    cs_narrator "Несколько человек повернулись ко мне."
    cs_narrator "Я продолжила."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 384eaa69cea621126828
    cs_ls "Может, всё-таки объяснишь нормально?"
    cs_ls "У нас тут не конкурс на самое загадочное объявление."
    cs_narrator "За дверью тихо засмеялись."
    cs_narrator "От этого смеха мне стало неприятно."
    cs_narrator "Я знала, как смеюсь сама."
    cs_narrator "И сейчас слышала почти то же самое."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Назови имена."
    cs_narrator "Семён посмотрел на Ольгу Дмитриевну."
    cs_narrator "Та не двигалась."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Пока ничего не называй."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Я и не собирался."
    cs_narrator "Из-под двери послышался шорох."
    cs_narrator "На полу появился белый конверт."
    cs_narrator "Он медленно скользнул вперёд и остановился возле ножки стула."
    cs_narrator "Я уставилась на него."
    cs_narrator "Утром такой же лежал в автобусе."
    cs_narrator "Теперь он был здесь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Опять конверт."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Не трогайте."
    cs_narrator "Виола осторожно присела."
    cs_narrator "Посмотрела на бумагу."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Здесь написано имя."
    cs_narrator "Ольга Дмитриевна направила фонарик ниже."
    cs_narrator "На конверте было выведено:"
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("Семёну", "Надпись на конверте")
    cs_narrator "«Семёну»."
    cs_narrator "Мы подождали."
    cs_narrator "Ничего не происходило."
    hide screen cs_d5_insert
    cs_narrator "Виола взяла конверт за край и положила на стол."
    cs_narrator "Затем осторожно открыла."
    cs_narrator "Внутри лежала плотная карточка."
    cs_narrator "Я наклонилась ближе."
    cs_narrator "Бумага выглядела старой."
    cs_narrator "Потёртые углы, слегка пожелтевшая поверхность."
    cs_narrator "Самая обыкновенная карточка."
    cs_narrator "Если бы она лежала среди наших записей с начала вечера, я бы, наверное, вообще не обратила на неё внимания."
    cs_narrator "Виола повернула карточку к фонарику."
    cs_narrator "Прочитала."
    cs_narrator "Затем положила перед Семёном."
    cs_narrator "На лицевой стороне было написано:"
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("ОСТАТЬСЯ — ОДИН.\nВЕРНУТЬСЯ — ОДИН.\nВЫБИРАЕТ ПЕРВЫЙ.", "Карточка: лицевая сторона")
    cs_narrator "ОСТАТЬСЯ — ОДИН."
    cs_narrator "ВЕРНУТЬСЯ — ОДИН."
    cs_narrator "ВЫБИРАЕТ ПЕРВЫЙ."
    cs_narrator "Семён долго смотрел на слова."
    cs_narrator "Затем перевернул карточку."
    cs_narrator "На обороте, другим почерком, было выведено:"
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("ТЫ УЖЕ ВЫБИРАЛ", "Карточка: оборот")
    cs_narrator "«ТЫ УЖЕ ВЫБИРАЛ»."
    hide screen cs_d5_insert
    cs_narrator "Он провёл пальцем по краю бумаги."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Первый…"
    cs_narrator "Я посмотрела на него."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Я приехал раньше вас."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Возможно, речь об этом."
    cs_narrator "Она немного помолчала."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Но мы не знаем наверняка."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "И вообще неизвестно, кто это написал."
    cs_narrator "Я кивнула."
    cs_narrator "Хорошее замечание."
    cs_narrator "Мы с самого утра пытались понять, что говорит голос."
    cs_narrator "Но почти не задумывались о том, зачем он говорит именно это."
    if cs_friend_se >= 4:
        cs_narrator "Семён повернулся ко мне."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Лена."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Да?"
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "А если я действительно уже кого-то оставил?"
        cs_narrator "Я посмотрела на карточку."
        cs_narrator "Потом на него."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Семён, мы даже не знаем, кто её написал."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Но там сказано…"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 6ff8fbd2ba9e9bfe707d
        cs_ls "Там много чего сказано."
        cs_ls "Пока ни одно слово не объяснили нормально."
        cs_narrator "Он опустил глаза."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: e4d5ade6aadcfe018563
        cs_ls "Давай сначала выясним, что от тебя хотят."
        cs_ls "А потом будешь решать, за что себя ругать."
        cs_narrator "Семён выдохнул."
        cs_narrator "Немного расслабил плечи."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Ладно."
        cs_narrator "Он положил карточку ближе к середине стола."
    else:
        cs_narrator "Семён повернулся к Ольге Дмитриевне."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Вы же говорили, что всё может повторяться."
        cs_narrator "Она кивнула."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Я мог уже быть здесь?"
        cs_narrator "Ольга Дмитриевна посмотрела на карточку."
        $ cs_d5_focus("mt")
        with cs_sprite_change
        cs_mt "Не знаю, Семён."
        cs_narrator "Она немного помолчала."
        $ cs_d5_focus("mt")
        with cs_sprite_change
        cs_mt "Но эта бумага не доказывает, что ты кому-то навредил."
        cs_narrator "Он опустил взгляд."
        $ cs_d5_focus("sy")
        with cs_sprite_change
        cs_sy "Понимаю."
        cs_narrator "Я не стала вмешиваться."
        cs_narrator "Вожатая сказала именно то, что ему сейчас было нужно услышать."
    cs_narrator "Тихонова неожиданно поднялась."
    cs_narrator "Мы посмотрели на неё."
    cs_narrator "Она стояла возле стула, держа альбом в руках."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Я вспомнила."
    cs_narrator "Я осторожно повернулась к ней."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Что именно?"
    cs_narrator "Тихонова посмотрела на Семёна."
    $ cs_d5_focus("un")
    with cs_sprite_change
    # cs_page_anchor: f4036aa61fdce28ff07e
    cs_un "У ворот."
    cs_un "Мне снилось, что мы стоим возле автобуса."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Семён нахмурился."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Мы?"
    cs_narrator "Она кивнула."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Ты и я."
    cs_narrator "Он перестал двигаться."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Ты говорил мне: «Прости. Я думал, что спасаю тебя»."
    cs_narrator "В комнате стало тихо."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Он выглядел совершенно растерянным."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Я?"
    $ cs_d5_focus("un")
    with cs_sprite_change
    # cs_page_anchor: 30ee1925168e34ce43f4
    cs_un "Во сне."
    cs_un "Я не знаю, было ли это на самом деле."
    cs_narrator "Она села."
    cs_narrator "Прижала альбом к коленям."
    if cs_d5_lena_private_memory:
        cs_narrator "Тихонова посмотрела на меня."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Помнишь, я рассказывала про руку с краской?"
        cs_narrator "Я кивнула."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Помню."
        $ cs_d5_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 6504af383882b892229c
        cs_un "После этого во сне был автобус."
        cs_un "Только я не уверена, что это один и тот же сон."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Тогда так и запишем."
        cs_narrator "Я взяла карандаш."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Не будем соединять их, пока ты сама не вспомнишь."
        cs_narrator "Она кивнула."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Спасибо."
    else:
        cs_narrator "Тихонова посмотрела на Женю."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Я не знаю, почему мне это снилось."
        cs_narrator "Женя подвинула ей чистый лист."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        # cs_page_anchor: 2cd8f8e2917ae7f40271
        cs_mz "Тогда просто запиши слова."
        cs_mz "Остальное потом."
        cs_narrator "Тихонова кивнула."
    cs_narrator "Ольга Дмитриевна вернулась к карточке."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    # cs_page_anchor: 4877cbc90ece4a7c5b0a
    cs_mt "Здесь написано про двоих."
    cs_mt "Но про остальных ничего не сказано."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "И непонятно, что означает «остаться»."
    cs_narrator "Я посмотрела на дверь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Поэтому имён пока никто называть не будет."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Семён повернулся ко мне."
    cs_narrator "Я заметила его взгляд и поспешила уточнить."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 2886b074b8453daa61a6
    cs_ls "Я про себя."
    cs_ls "За тебя не решаю."
    cs_narrator "Он снова посмотрел на карточку."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Я тоже пока не буду ничего выбирать."
    cs_narrator "Он немного помолчал."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Сначала пусть объяснят, что произойдёт."
    cs_narrator "Я кивнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Согласна."
    cs_narrator "Женя пододвинула ему лист."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 55287b57c6cbc0407580
    cs_mz "Запиши вопросы."
    cs_mz "Так проще будет не забыть."
    cs_narrator "Семён взял карандаш."
    cs_narrator "Первым написал одно слово."
    cs_narrator "«Куда?»"
    cs_narrator "Потом остановился."
    cs_narrator "Из-за двери ответили."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Тогда выберет лагерь."
    cs_narrator "Я подняла голову."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "По каким правилам?"
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "По прежним."
    cs_narrator "Я посмотрела на остальных."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 88daa14ac131ad323439
    cs_ls "Которых никто не знает."
    cs_ls "Очень удобно."
    cs_narrator "Голос за дверью изменился."
    cs_narrator "Теперь он больше не был похож на мой."
    cs_narrator "Но я узнала интонацию."
    cs_narrator "Именно такой голос мы слышали возле старого корпуса."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Ты проснулась раньше."
    cs_narrator "Женя замерла с карандашом в руке."
    cs_narrator "Потом открыла тетрадь."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Подождите."
    cs_narrator "Она нашла одну из старых записей."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "У меня во сне было: «Она пришла раньше»."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Затем на дверь."
    $ cs_d5_focus("voice")
    with cs_sprite_change
    cs_d5_voice "Теперь выбрать может и вторая."
    cs_narrator "Я нахмурилась."
    cs_narrator "Вторая?"
    cs_narrator "Что именно это должно означать?"
    cs_narrator "Я перевела взгляд на Лену Тихонову."
    cs_narrator "Она смотрела на меня."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Какая из нас?"
    cs_narrator "Ответа не последовало."
    if cs_d5_lena_respected:
        cs_narrator "Тихонова придвинула ко мне свой лист."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Только не решай сразу, что это я."
        cs_narrator "Я посмотрела на неё."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Не решу."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Правда?"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: d7246cf8aef082a18694
        cs_ls "Правда."
        cs_ls "Мы вообще ещё не поняли, о ком речь."
        cs_narrator "Она кивнула."
        cs_narrator "Я записала вопрос рядом с её словами."
    else:
        cs_narrator "Тихонова придвинулась ближе к Жене."
        $ cs_d5_focus("un")
        with cs_sprite_change
        # cs_page_anchor: ae1254133b6b91db666c
        cs_un "Я не знаю."
        cs_un "Я правда не знаю."
        $ cs_d5_focus("mz")
        with cs_sprite_change
        cs_mz "Никто тебя сейчас не обвиняет."
        cs_narrator "Я осталась на своём месте."
        cs_narrator "После утреннего разговора мне было понятно, почему Тихонова не хочет обращаться ко мне."
        cs_narrator "И сейчас исправить это одной красивой фразой всё равно бы не получилось."
    cs_narrator "За дверью что-то тихо зашуршало."
    cs_narrator "Я повернула голову."
    cs_narrator "Ольга Дмитриевна подняла фонарик."
    cs_narrator "На внутренней стороне двери начали проступать белые буквы."
    cs_narrator "Сначала одна строка."
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("ПЕРВЫЙ ИЛИ ВТОРАЯ.", "Надпись на двери")
    cs_narrator "ПЕРВЫЙ ИЛИ ВТОРАЯ."
    cs_narrator "Затем ниже появилась ещё одна."
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("ПЕРВЫЙ ИЛИ ВТОРАЯ.\nДО РАССВЕТА.", "Надпись на двери")
    cs_narrator "ДО РАССВЕТА."
    cs_narrator "Я смотрела на надпись."
    cs_narrator "Никто не произносил ни слова."
    hide screen cs_d5_insert
    cs_narrator "Потом Женя резко наклонилась к столу."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Карточка."
    cs_narrator "Я посмотрела туда же."
    cs_narrator "Карточки не было."
    cs_narrator "Только что она лежала перед Семёном."
    cs_narrator "Теперь остался пустой участок стола."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Она исчезла?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Да."
    cs_narrator "Женя быстро взяла свою тетрадь."
    cs_narrator "Открыла на нужной странице."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Запись осталась."
    cs_narrator "Я посмотрела на строчки."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Там были переписаны все слова."
    cs_narrator "Остаться."
    cs_narrator "Вернуться."
    cs_narrator "Выбирает первый."
    cs_narrator "Ты уже выбирал."
    cs_narrator "Я медленно выдохнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 4b2c7d5a89b3ead07b07
    cs_ls "Хорошо."
    cs_ls "Хоть что-то осталось."
    cs_narrator "Ольга Дмитриевна снова посмотрела на часы."
    cs_narrator "Оба циферблата показывали то же время."
    cs_narrator "23:59."
    cs_narrator "Я не знала, сколько мы уже сидели."
    cs_narrator "Может быть, несколько минут."
    cs_narrator "Может быть, гораздо дольше."
    cs_narrator "Снаружи по-прежнему было тихо."
    cs_narrator "Надпись на двери не исчезала."
    cs_narrator "Даша взяла плед и накрыла наши колени."
    cs_narrator "Семён переставил стул ближе к столу."
    cs_narrator "Тихонова открыла альбом на чистой странице."
    cs_narrator "Женя убрала чашки, освобождая место для записей."
    cs_narrator "Я посмотрела на всех."
    cs_narrator "Никто не выглядел спокойным."
    cs_narrator "Но никто и не собирался уходить."
    cs_narrator "Я подвинула Семёну карандаш."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d78cec74540dd8063a9f
    cs_ls "Запиши всё, что ещё помнишь."
    cs_ls "Даже если кажется ерундой."
    cs_narrator "Он взял карандаш."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Хорошо."
    cs_narrator "Я достала собственный лист."
    cs_narrator "Положила рядом."
    cs_narrator "За дверью не было слышно ни шагов, ни дыхания."
    cs_narrator "Я всё ещё не понимала, кто с нами разговаривает."
    cs_narrator "Не знала, почему голос выбирает именно Семёна."
    cs_narrator "Не знала, кого называют второй."
    cs_narrator "И совершенно не собиралась считать эти вопросы решёнными только потому, что кто-то написал ответ на двери."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Я посмотрела на часы."
    cs_narrator "Стрелки не двигались."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Значит, до рассвета."
    cs_narrator "Даша повернулась ко мне."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Думаешь, у нас действительно столько времени?"
    cs_narrator "Я посмотрела на надпись."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Не знаю."
    cs_narrator "Помолчала."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: e15e7a8e3d60dda622c5
    cs_ls "Но сидеть и ждать объяснений я уже устала."
    cs_ls "Давайте хотя бы запишем, что нам известно."
    cs_narrator "Женя открыла новую страницу."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Начинай."
    cs_narrator "Я взяла карандаш."
    cs_narrator "Первой написала фразу из своего сна."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_narrator "«Не садись второй раз»."
    cs_narrator "Ниже — другую."
    cs_narrator "«Остался один»."
    cs_narrator "Потом посмотрела на остальных."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Кто что помнит ещё?"
    cs_narrator "Семён придвинул свой лист."
    cs_narrator "Тихонова начала рисовать расположение людей у ворот."
    cs_narrator "Даша помогла Жене разложить записи."
    cs_narrator "Ольга Дмитриевна проверила дверь."
    cs_narrator "Виола осталась возле окна."
    cs_narrator "Мы не знали, что произойдёт дальше."
    cs_narrator "Но пока все были здесь."
    cs_narrator "И пока у нас оставались вопросы, я не собиралась принимать чужие ответы за окончательную правду."
    cs_narrator "За дверью ждали выбора."
    cs_narrator "А мы продолжали писать."
    hide screen cs_d5_insert
    hide screen cs_d5_clock_face
    hide screen cs_d5_notes
    $ cs_bus_cue("mystery_end")
    $ cs_director_scene("black")
    scene black
    with Dissolve(1.0)
    stop ambience fadeout 0.5
    stop music fadeout 1.0
    return
