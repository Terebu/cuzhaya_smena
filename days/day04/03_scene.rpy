# -*- coding: utf-8 -*-
label cs_day04_03:
    $ save_name = "Чужая смена — День 4: Металлическая дверь"
    $ cs_director_scene("cs_d4_old_door")
    scene cs_d4_old_door
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    stop music fadeout 1.5
    cs_narrator "Внизу лестницы оказалась массивная металлическая дверь."
    cs_narrator "Она была приоткрыта."
    cs_narrator "Из узкой щели пробивался холодный свет, а где-то за стеной монотонно гудело оборудование."
    cs_narrator "Я остановилась на последней ступени."
    cs_narrator "Настоящее электричество."
    cs_narrator "В здании, которое выглядит брошенным уже много лет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Интересно, кто здесь платит за свет."
    cs_narrator "Разумеется, никто не ответил."
    cs_narrator "Я осторожно потянула дверь."
    cs_narrator "Скрип прокатился по лестнице. С таким же успехом можно было объявить о себе в громкоговоритель."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тише ты. Я здесь вообще-то инкогнито."
    cs_narrator "Дверь продолжала скрипеть."
    cs_narrator "Видимо, понятие конфиденциальности советской промышленности было совершенно неизвестно."
    $ cs_director_scene("bg int_catacombs_entrance")
    scene bg int_catacombs_entrance
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "За дверью начинался короткий бетонный коридор."
    cs_narrator "Вдоль стен тянулись трубы, под потолком мерцала лампа. Пол был гораздо чище, чем наверху."
    cs_narrator "Я провела пальцем по ближайшей трубе."
    cs_narrator "Пыль."
    cs_narrator "По соседней."
    cs_narrator "Почти ничего."
    cs_narrator "Я нахмурилась."
    cs_narrator "Кто-то здесь бывает."
    cs_narrator "Причём достаточно часто."
    cs_narrator "За поворотом щёлкнуло и коротко загудело, будто включился мотор."
    cs_narrator "Я остановилась."
    cs_narrator "Работающее оборудование."
    cs_narrator "Чистые поверхности."
    cs_narrator "И неизвестный человек, который почему-то не хочет показываться."
    cs_narrator "Прекрасно. Список причин немедленно уйти продолжал пополняться."
    cs_narrator "Но любопытство оказалось сильнее."
    cs_narrator "Я заглянула в ближайшую комнату."
    $ cs_director_scene("cs_d4_old_bunker")
    scene cs_d4_old_bunker
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Помещение напоминало небольшую мастерскую."
    cs_narrator "Шкафы были забиты проводами, деталями и инструментами. На столе лежал разобранный радиоприёмник."
    cs_narrator "Я приблизилась."
    cs_narrator "Пыль покрывала почти всю поверхность стола, кроме одного аккуратного прямоугольника."
    cs_narrator "Здесь недавно что-то стояло."
    cs_narrator "И кто-то это забрал."
    cs_narrator "Один из шкафов оказался незапертым."
    cs_narrator "Внутри находились папки."
    cs_narrator "Десятки старых папок с пожелтевшими корешками."
    cs_narrator "Я вытащила ближайшую."
    cs_narrator "На обложке ещё можно было разобрать надпись:"
    cs_narrator "«Совёнок. Смена…»"
    cs_narrator "Дата почти полностью стёрлась."
    cs_narrator "Внутри лежали списки."
    cs_narrator "Имена. Фамилии. Возраст. Отряды."
    cs_narrator "Самые обычные лагерные документы."
    cs_narrator "Я перелистнула несколько страниц."
    cs_narrator "Ничего особенно интересного."
    cs_narrator "Следующая папка."
    cs_narrator "Ещё одна."
    cs_narrator "И вдруг взгляд остановился на цифрах."
    cs_narrator "1971."
    $ cs_director_scene("cs_d4_old_archive")
    scene cs_d4_old_archive
    $ cs_frame_focus([])
    with dissolve
    cs_narrator "Я медленно раскрыла папку."
    show cs_d4_document roster1971 at cs_d4_document_center zorder 40
    with dissolve
    cs_narrator "Сначала увидела таблицу с фамилиями."
    cs_narrator "Потом знакомые имена."
    cs_narrator "Лена."
    cs_narrator "Женя."
    cs_narrator "Славя."
    cs_narrator "Семён."
    cs_narrator "Ниже — Алиса, Ульяна, Мику."
    cs_narrator "Я перечитала список."
    cs_narrator "Потом ещё раз."
    cs_narrator "Буквы никуда не исчезли."
    cs_narrator "Нет."
    cs_narrator "Так не бывает."
    cs_narrator "Я быстро перевернула страницу."
    hide cs_d4_document
    with dissolve
    show cs_d4_document photo1971 at cs_d4_document_center zorder 40
    with dissolve
    cs_narrator "Там находилась фотография."
    cs_narrator "Пионерский отряд."
    cs_narrator "Знакомые лица."
    cs_narrator "Я достала снимок, найденный наверху, и положила рядом."
    cs_narrator "Оба изображали примерно одну и ту же группу людей."
    cs_narrator "Но фотографии не были одинаковыми."
    cs_narrator "На одном снимке девушки стояли в другом порядке. Причёски немного отличались. Кто-то улыбался, кто-то смотрел в сторону."
    cs_narrator "Как две версии одной картины."
    cs_narrator "Один сюжет, но разные наброски."
    cs_narrator "Я почувствовала неприятное напряжение в пальцах."
    cs_narrator "Взяла следующую папку."
    hide cs_d4_document
    with dissolve
    show cs_d4_document photo1963 at cs_d4_document_center zorder 40
    with dissolve
    cs_narrator "1963."
    cs_narrator "Несколько секунд просто смотрела на цифры."
    cs_narrator "Потом открыла."
    cs_narrator "Снова списки."
    cs_narrator "Снова фотографии."
    cs_narrator "И снова некоторые лица, которые я видела буквально вчера."
    cs_narrator "Я опустилась на край стула."
    cs_narrator "Так."
    cs_narrator "Совпадения бывают."
    cs_narrator "Родственники тоже бывают."
    cs_narrator "Бывает, что человеку очень хочется найти знакомые черты на старой фотографии."
    cs_narrator "Но одинаковая родинка у девушки в очках?"
    cs_narrator "Одинаковый разрез глаз?"
    cs_narrator "Те же имена?"
    cs_narrator "Я закрыла глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ну что ж. У исторической науки только что появилась серьёзная проблема."
    cs_narrator "И тут в голове возникло слово."
    cs_narrator "Циклы."
    cs_narrator "Я открыла глаза."
    cs_narrator "Нет."
    cs_narrator "Пока это гипотеза."
    cs_narrator "Не ответ."
    cs_narrator "В игре время тоже вытворяло странное. Но здешние события я уже не узнавала. Да и Семён упорно жил своей жизнью, как бы я ни пыталась превратить её в комедию."
    cs_narrator "Я осторожно вынула из папки 1971 года одну фотографию и лист со списком."
    hide cs_d4_document
    with dissolve
    cs_narrator "Остальные документы вернула на место."
    cs_narrator "Находки поместила между листами картона рядом с первым снимком."
    $ cs_d4_photo1971_location = cs_d4_roster_location = "lena"
    cs_narrator "Покажу Даше."
    cs_narrator "Потом Семёну."
    cs_narrator "И, возможно, Ольге Дмитриевне."
    cs_narrator "Дальше будем думать."
    $ cs_director_scene("cs_d4_old_bunker")
    scene cs_d4_old_bunker
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Из коридора донеслись быстрые шаги."
    cs_narrator "Я резко подняла голову."
    cs_narrator "В дверном проёме мелькнула девушка в пионерской форме."
    cs_narrator "Два хвостика."
    cs_narrator "Тёмные волосы, которые в тусклом свете показались фиолетовыми."
    cs_narrator "Лицо я разглядеть не успела."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Стой!"
    cs_narrator "Девушка исчезла."
    cs_narrator "Я бросилась к выходу."
    $ cs_director_scene("bg int_catacombs_entrance")
    scene bg int_catacombs_entrance
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "В коридоре никого не было."
    cs_narrator "Только в дальнем конце медленно закрывалась металлическая дверь."
    cs_narrator "Я приблизилась."
    $ cs_director_scene("cs_d4_old_stairs")
    scene cs_d4_old_stairs
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "За ней начиналась ещё одна лестница."
    cs_narrator "Вниз."
    cs_narrator "Ещё глубже."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Разумеется. Здесь, видимо, каждый следующий ответ хранят этажом ниже."
    cs_narrator "Я осторожно заглянула в тёмный проём."
    cs_narrator "И услышала голос."
    cs_d4_unknown_girl "Лена."
    cs_narrator "Я застыла."
    cs_narrator "Женский."
    cs_narrator "Тихий."
    cs_narrator "Совершенно спокойный."
    cs_narrator "Не крик. Не шёпот."
    cs_narrator "Кто-то просто произнёс моё имя."
    stop music fadeout 1.5
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Кто там?"
    cs_narrator "Ответа не последовало."
    cs_narrator "Я всматривалась в темноту, пытаясь разглядеть хотя бы силуэт."
    cs_narrator "Ничего."
    cs_narrator "Только ступени, уходящие вниз, и слабое свечение где-то далеко за поворотом."
    cs_narrator "Я осторожно сделала шаг."
    cs_d4_unknown_girl "Не ходи дальше."
    cs_narrator "Сердце неприятно сжалось."
    cs_narrator "Голос звучал совсем близко."
    cs_narrator "Но рядом никого не было."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты кто?"
    cs_narrator "Тишина."
    cs_narrator "Потом:"
    cs_d4_unknown_girl "Ты не должна была проснуться здесь."
    cs_narrator "Я почувствовала, как по спине пробежал холод."
    cs_narrator "Слова прозвучали спокойно, почти буднично."
    cs_narrator "И именно поэтому испугали гораздо сильнее, чем любой крик."
    cs_narrator "Не должна была проснуться."
    cs_narrator "Значит, кто-то знает, как я сюда попала."
    cs_narrator "И знает меня."
    cs_narrator "Я крепче сжала деревянную ножку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Откуда ты знаешь моё имя?"
    cs_d4_unknown_girl "Уходи."
    cs_narrator "Голос не повысился."
    cs_narrator "В нём не было злости."
    cs_narrator "Скорее усталость."
    cs_narrator "Или предупреждение."
    cs_narrator "Я сделала ещё один шаг."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сначала скажи, что происходит."
    cs_narrator "Ответа не последовало."
    cs_narrator "В темноте что-то тихо щёлкнуло."
    $ cs_director_scene("black")
    scene black
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "И свет погас."
    stop music fadeout 1.5
    cs_narrator "Я отшатнулась в темноте, потеряла равновесие и ударилась плечом о стену."
    cs_narrator "Деревяшка едва не выскользнула из руки."
    cs_narrator "Я замерла."
    cs_narrator "Вокруг было настолько темно, что я с трудом различала собственные пальцы."
    cs_narrator "Где-то впереди продолжала капать вода."
    cs_narrator "Кап."
    cs_narrator "Кап."
    cs_narrator "Кап."
    cs_narrator "Я пыталась понять, слышу ли ещё чьё-нибудь дыхание."
    cs_narrator "Ничего."
    cs_narrator "Только собственное сердце, стучавшее так сильно, что казалось, его слышно по всему убежищу."
    cs_narrator "Всё."
    cs_narrator "Хватит."
    cs_narrator "Я медленно нащупала перила и начала отступать."
    cs_narrator "Не побежала."
    cs_narrator "Потому что понятия не имела, сколько ступеней осталось за спиной и насколько прочным был бетон под ногами."
    $ cs_director_scene("cs_d4_old_bunker")
    scene cs_d4_old_bunker
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Добравшись до освещённого коридора, я почти ввалилась в техническую комнату."
    cs_narrator "Там свет пока горел."
    cs_narrator "Я прислонилась к шкафу и несколько секунд пыталась восстановить дыхание."
    cs_narrator "Руки дрожали. Я стиснула пальцы, злясь на себя."
    cs_narrator "Какого чёрта я вообще сюда полезла?"
    cs_narrator "Одна."
    cs_narrator "Без фонаря."
    cs_narrator "Без возможности позвать на помощь."
    cs_narrator "И всё ради фотографий, которые никто не мешал сначала показать остальным."
    cs_narrator "Я проверила папку: фотографии и список были на месте."
    cs_narrator "Домой."
    cs_narrator "Больше никаких подвигов."
    cs_narrator "Никаких незнакомых лестниц."
    cs_narrator "И никаких попыток проверить, насколько удачно я умею сражаться с мистикой при помощи мебели."
    cs_narrator "Я направилась к выходу."
    $ cs_director_scene("cs_d4_old_stairs")
    scene cs_d4_old_stairs
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "И почти добралась до лестницы наверх, когда услышала шаги."
    cs_narrator "Быстрые."
    cs_narrator "Человеческие."
    cs_narrator "Кто-то спускался."
    cs_narrator "Я прижалась к стене, подняв деревянную ножку."
    cs_narrator "Из полумрака показался силуэт."
    cs_da "Лена?!"
    cs_narrator "Я узнала голос раньше, чем увидела лицо."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Даша?"
    show cs_darya worried sport normal at cs_darya_normal_center
    $ cs_d4_scene_cast = ["cs_darya"]
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Она остановилась на ступеньке."
    cs_narrator "Волосы кое-как собраны, кроссовки в грязи. Даша явно одевалась и бежала сюда впопыхах."
    cs_narrator "Даша посмотрела на меня."
    cs_narrator "Потом на деревяшку в руке."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Опусти это."
    cs_narrator "Я медленно опустила ножку стула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Доброе утро."
    cs_narrator "Она не улыбнулась. Молча рассматривала меня."
    cs_narrator "На грязные кроссовки."
    cs_narrator "На пыльную футболку."
    cs_narrator "На бумаги, прижатые к груди."
    cs_narrator "Потом снова в глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты ушла одна."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "В старый лагерь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И спустилась сюда."
    cs_narrator "Я сглотнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "…Да."
    cs_narrator "Даша закрыла глаза."
    cs_narrator "Я приготовилась выслушать всё, что заслужила."
    cs_narrator "Но вместо этого она резко шагнула ко мне."
    $ cs_director_scene("cs_cg_lena_darya_bunker_reunion")
    scene cs_cg_lena_darya_bunker_reunion
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "И обняла."
    cs_narrator "Я растерялась."
    cs_narrator "Настолько, что не сразу смогла ответить."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Даш…"
    cs_narrator "Она не произнесла ни слова."
    cs_narrator "Только крепче прижалась ко мне."
    cs_narrator "Я осторожно обняла её здоровой рукой."
    cs_narrator "И только тогда я поняла: Даша испугалась, что я не вернусь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Прости."
    cs_narrator "Даша ещё несколько секунд не отпускала."
    $ cs_director_scene("cs_d4_old_stairs")
    scene cs_d4_old_stairs
    show cs_darya worried sport normal at cs_darya_normal_center
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Потом отстранилась, но осталась совсем рядом."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Я проснулась, а тебя нет."
    cs_narrator "Она говорила негромко."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Сначала подумала, что ты просто вышла побегать. Потом начала искать."
    if cs_d4_left_note == True:
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Записку нашла почти сразу."
        cs_narrator "Я опустила взгляд."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Но ты написала про старую дорогу. А потом я спросила Славю, куда она ведёт."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "И она рассказала про корпус?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Да. Ещё сказала, что туда никто не ходит и лучше позвать Ольгу Дмитриевну."
        cs_narrator "Даша посмотрела на меня."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Я решила сначала проверить дорогу. Если бы не нашла тебя, вернулась бы за помощью."
        cs_narrator "Я медленно кивнула."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Понимаю."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "И, Лена… «Не волнуйся» в записке — не очень хорошая идея, когда ты уходишь в заброшенное здание."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Согласна. Формулировка не выдерживает критики."
    else:
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Ты даже записку не оставила."
        cs_narrator "Я отвела взгляд."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Я не знала, куда ты ушла. Сначала проверила спортивную площадку, потом спросила Славю. Она рассказала про старую дорогу."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "И ты решила меня искать?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "А что мне оставалось?"
        cs_narrator "Она произнесла это без злости."
        cs_narrator "От чего стало только хуже."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_da "Я не знала, что с тобой. Даже не знала, в какую сторону идти."
        cs_narrator "Мне нечего было ответить. Даже шутки закончились."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Да. Это было очень глупо."
    cs_narrator "Даша глубоко вдохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "На тропе остались следы. Я пошла по ним, потом услышала шум из корпуса."
    cs_narrator "Она посмотрела на деревянную ножку в моей руке."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Нашла лестницу. Спустилась. А здесь ты. С палкой."
    cs_narrator "Я посмотрела на своё импровизированное оружие."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "С ножкой стула. Это важное уточнение."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Лена."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Всё. Молчу."
    cs_narrator "Она ещё несколько секунд смотрела на меня."
    cs_narrator "Я медленно выдохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я правда не должна была идти одна."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Не должна была."
    cs_narrator "На этот раз я не спорила."
    cs_narrator "На лестничной площадке стало тихо."
    cs_narrator "Где-то за стеной продолжало гудеть оборудование."
    cs_narrator "Я вспомнила голос."
    cs_narrator "Темноту."
    cs_narrator "Фразу про то, что мне не следовало просыпаться здесь."
    cs_narrator "И снова почувствовала холод."
    cs_narrator "Даша заметила, что я смотрю в сторону лестницы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что там?"
    cs_narrator "Я достала фотографии."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Кое-что нашла."
    cs_narrator "Она осторожно взяла верхний снимок."
    cs_narrator "Несколько секунд рассматривала."
    cs_narrator "Потом нахмурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Это же…"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Славя. Женя. Возможно, Тихонова."
    cs_narrator "Даша подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Папка за 1971 год."
    cs_narrator "Она снова посмотрела на снимок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Но сейчас восьмидесятый."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Я показала список."
    cs_narrator "Даша быстро пробежала глазами по именам."
    cs_narrator "Её лицо постепенно менялось."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Семён?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ага."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И остальные?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Причём есть ещё папка за шестьдесят третий. Там похожая история."
    cs_narrator "Даша медленно опустила бумаги."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Этого не может быть."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Очень хочется согласиться."
    cs_narrator "Она внимательно посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Это всё?"
    cs_narrator "Я покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нет."
    cs_narrator "Несколько секунд пыталась подобрать слова."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я видела здесь девушку. В пионерской форме. С двумя хвостиками."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Лену?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не знаю. Лица не видела."
    cs_narrator "Я посмотрела на тёмную лестницу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А потом кто-то говорил со мной оттуда."
    cs_narrator "Дарья повернула голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что сказал?"
    cs_narrator "Я почувствовала, как внутри снова всё сжалось."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что я не должна была здесь проснуться."
    cs_narrator "Даша ничего не ответила."
    cs_narrator "Только посмотрела вниз."
    cs_narrator "Потом взяла меня за руку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Мы уходим."
    cs_narrator "Я сразу кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она удивлённо посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Без споров?"
    cs_narrator "Я слабо улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "За последние двадцать минут мой талант к возражениям серьёзно пострадал."
    cs_narrator "Даша почти улыбнулась."
    cs_narrator "Но глаза оставались напряжёнными."
    cs_narrator "Мы начали подниматься."
    cs_narrator "Ступени гулко отзывались под ногами. Я держалась рядом с Дашей и смотрела, куда ставлю ногу."
    cs_narrator "На середине подъёма снизу донёсся короткий смех."
    cs_narrator "Женский."
    cs_narrator "Едва слышный."
    cs_narrator "Мы остановились одновременно."
    cs_d4_unknown_girl "До встречи, Лена."
    cs_narrator "Пальцы Даши сжались на моей руке."
    cs_narrator "Она медленно повернула голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты слышала?"
    cs_narrator "Я посмотрела на неё."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Мы стояли неподвижно."
    cs_narrator "Снизу больше ничего не доносилось."
    cs_narrator "Никаких шагов."
    cs_narrator "Никакого смеха."
    cs_narrator "Только вода продолжала размеренно капать где-то в темноте."
    cs_narrator "Даша потянула меня наверх."
    cs_narrator "Я не сопротивлялась."
    cs_narrator "И впервые за всё утро мне совершенно искренне не хотелось узнавать, кто остался внизу."
    $ cs_d4_found_1971_records = True
    $ cs_d4_unknown_girl_seen = True
    $ cs_d4_heard_unknown_voice = True
    return
