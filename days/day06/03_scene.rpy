# -*- coding: utf-8 -*-
label cs_day06_03:
    $ save_name = "Чужая смена — День 6: Автобус"
    $ cs_d6_room("bg int_dining_hall_people_day",['cs_darya', 'cs_semen', 'mt', 'cs_zhenya', 'un', 'sl', 'dv', 'mi'])
    play sound "sound/sfx/dinner_horn_processed.ogg"
    cs_narrator "На обед мы пришли вместе."
    cs_narrator "За разговорами о багаже еду разобрали быстро; потом каждый отправился за своей сумкой."
    $ cs_d6_room("bg ext_no_bus",['cs_darya', 'cs_semen', 'mt', 'cs_zhenya', 'un', 'sl', 'dv', 'mi'])
    stop music fadeout 1.5
    cs_narrator "После обеда сумки потянулись к воротам."
    if cs_d6_help == "mi":
        cs_narrator "Мику спокойно ждала с дорожной папкой."
        cs_narrator "Алиса громко возмущалась, что её гитару считают отдельным местом багажа."
    else:
        cs_narrator "Мику ещё раз вернулась в клуб."
        cs_narrator "Алиса громко возмущалась, что её гитару считают отдельным местом багажа."
    cs_narrator "Женя стояла возле Слави."
    cs_narrator "Тихонова пристроила альбом поверх своей сумки и смотрела на дорогу."
    $ cs_bus_engine("distant")
    cs_narrator "Я услышала двигатель раньше, чем увидела автобус."
    cs_narrator "Даша оказалась рядом и задела меня плечом."
    $ cs_d6_focus("da")
    cs_da "Дыши."
    $ cs_d6_focus("ls")
    cs_ls "Я дышу."
    cs_ls "Просто с недоверием."
    $ cs_bus_cue("stop")
    $ cs_d6_room("bg ext_bus",['cs_darya', 'cs_semen', 'mt', 'cs_zhenya', 'un', 'sl', 'dv', 'mi'])
    $ cs_bus_cue("open")
    cs_narrator "Автобус выехал из-за деревьев, поднял пыль и остановился перед воротами."
    cs_narrator "Дверь открылась."
    cs_narrator "Из кабины выглянул водитель."
    $ cs_d6_focus("driver")
    cs_d6_driver "Ольга Дмитриевна, вы готовы?"
    $ cs_d6_focus("mt")
    cs_mt "Сейчас, Пётр."
    cs_mt "Сначала документы посмотрю."
    $ cs_d6_focus("driver")
    cs_d6_driver "Опять что-то в списках?"
    $ cs_d6_focus("mt")
    cs_mt "Проверка перед рейсом."
    cs_narrator "Он пожал плечами и достал бумаги."
    cs_narrator "Я удержалась от вопросов про количество рук и происхождение человечества."
    cs_narrator "У Ольги были вполне нормальные вопросы: откуда едет, куда повезёт детей, где остановится."
    if cs_d6_help == "sl":
        cs_narrator "Славя сверила списки."
        cs_narrator "Даша вместе с ней прошла по салону."
    else:
        cs_narrator "Славя сверила списки и вернулась к багажу."
        cs_narrator "Даша вместе с Ольгой проверила салон."
    if cs_d6_help == "dv":
        $ cs_d6_focus("dv")
        cs_dv "Пойдём, с другой стороны посмотрим."
    $ cs_d6_think()
    cs_narrator "Семён обошёл автобус снаружи и сам заглянул внутрь."
    $ cs_d6_room("bg int_bus",['cs_darya', 'cs_semen', 'mt', 'cs_zhenya', 'un', 'sl', 'dv', 'mi'])
    cs_narrator "Я поднялась на первую ступеньку и заглянула в салон."
    cs_narrator "Внутри пахло нагретыми сиденьями и пылью."
    cs_narrator "На переднем стекле лежала тряпка."
    cs_narrator "Возле водительского места дребезжала неплотно закрытая крышка."
    $ cs_d6_think()
    cs_th "Вчерашний автобус я боялась вспоминать."
    cs_th "Этот пока был занят тем, что возил людей и раздражал водителя мелкими поломками."
    cs_narrator "Пётр заметил мой взгляд."
    $ cs_d6_focus("driver")
    cs_d6_driver "Первый раз автобус видишь?"
    $ cs_d6_focus("ls")
    cs_ls "Такой нормальный."
    $ cs_d6_think()
    $ cs_d6_room("bg ext_bus",['cs_darya', 'cs_semen', 'mt', 'cs_zhenya', 'un', 'sl', 'dv', 'mi'])
    cs_narrator "Он решил, что я шучу, и вернулся к бумагам."
    cs_narrator "Посадка началась с обычной суматохи."
    cs_narrator "Кто-то забыл сумку, кто-то занял чужое место."
    cs_narrator "Ольга пересчитывала пионеров, Славя помогала с багажом."
    if cs_d6_help == "sl":
        cs_narrator "Я забрала у неё стопку оставшихся полотенец."
        $ cs_d6_focus("ls")
        cs_ls "Иди уже."
        cs_ls "Ты сегодня за всех собраться не успеешь."
        $ cs_d6_focus("sl")
        cs_sl "Я только проверю…"
        $ cs_d6_focus("ls")
        cs_ls "Проверила."
        cs_ls "Даже автобус внутри."
        cs_narrator "Она посмотрела на полотенца в моих руках и сдалась."
        cs_narrator "Перед тем как подняться в салон, Славя обняла Дашу, потом меня."
        $ cs_d6_focus("sl")
        cs_sl "Спасибо за утро."
        $ cs_d6_focus("ls")
        cs_ls "Пожалуйста."
        cs_ls "Если завтра найдёшь пропавшую наволочку у себя в сумке, это заговор."
        $ cs_d6_towels_carried = True
    else:
        cs_narrator "Славя поставила последнюю сумку у багажного отделения и наконец выпрямилась."
        $ cs_d6_focus("sl")
        cs_sl "Всё, теперь можно ехать."
        $ cs_d6_focus("ls")
        cs_ls "Попробуй хотя бы в дороге посидеть."
        $ cs_d6_focus("sl")
        cs_sl "Если никто больше ничего не забудет."
    if cs_d6_before("sl") >= 4:
        $ cs_d6_focus("sl")
        cs_sl "Возьми."
        cs_sl "У меня второй есть."
        cs_narrator "Славя протянула запасной значок."
        $ cs_d6_focus("ls")
        cs_ls "Теперь точно не выгонят за нарушение формы."
        $ cs_d6_focus("sl")
        cs_sl "За форму — нет."
        cs_narrator "Я приколола значок к карману."
        $ cs_d6_focus("ls")
        cs_ls "Остальные основания ты благоразумно оставила."
        $ cs_d6_sl_badge_received = True
    cs_narrator "Она рассмеялась."
    with None
    $ cs_actor_exit(["sl"])
    $ cs_d6_cast = [t for t in cs_d6_cast if t != "sl"]
    with cs_sprite_leave
    cs_narrator "Алиса прощалась быстрее."
    $ cs_d6_focus("dv")
    cs_dv "Не лезьте никуда."
    $ cs_d6_focus("ls")
    cs_ls "Это напутствие или приказ?"
    $ cs_d6_focus("dv")
    cs_dv "Как лучше дойдёт."
    cs_narrator "Я протянула руку."
    cs_narrator "Она пожала её, чуть сильнее, чем требовалось."
    $ cs_d6_focus("ls")
    cs_ls "Ладно."
    cs_ls "Хорошей дороги, Двачевская."
    $ cs_d6_focus("dv")
    cs_dv "И вам тут не сдохнуть от скуки, Соколова."
    if cs_d6_help == "dv" and cs_friend_dv >= 4:
        cs_narrator "Алиса положила мне в ладонь медиатор."
        $ cs_d6_focus("dv")
        cs_dv "Потом вернёшь."
        $ cs_d6_focus("ls")
        cs_ls "Ты сейчас выдаёшь мне повод приставать к тебе после лагеря?"
        $ cs_d6_focus("dv")
        cs_dv "Ты и без повода справляешься."
        $ cs_d6_focus("ls")
        cs_ls "Спасибо."
        $ cs_d6_dv_pick_received = True
    cs_narrator "На этом мы сочли обмен любезностями завершённым."
    with None
    $ cs_actor_exit(["dv"])
    $ cs_d6_cast = [t for t in cs_d6_cast if t != "dv"]
    with cs_sprite_leave
    cs_narrator "Мику остановилась перед нами и вдруг растеряла все приготовленные слова."
    $ cs_d6_focus("mi")
    cs_mi "Я хотела сказать…"
    cs_mi "Если вы завтра…"
    $ cs_d6_focus("da")
    cs_da "Мы будем осторожны."
    $ cs_d6_focus("mi")
    cs_mi "Правда?"
    $ cs_d6_focus("da")
    cs_da "Я прослежу."
    cs_narrator "Я посмотрела на неё."
    $ cs_d6_focus("ls")
    cs_ls "У тебя теперь работа на полную ставку."
    cs_narrator "Мику всё-таки улыбнулась и обняла нас обеих."
    if cs_d6_help == "mi" and cs_friend_mi >= 4:
        if cs_d5_miku_intro_heard or cs_day02_miku_listened:
            $ cs_d6_focus("mi")
            cs_mi "Я отдельно начало записала."
            cs_mi "Не пытайся сразу всю песню вспомнить."
            $ cs_d6_focus("ls")
            cs_ls "Я ноты читаю примерно как старые ведомости."
            cs_narrator "Она напела первые звуки и показала строку пальцем."
            $ cs_d6_focus("mi")
            cs_mi "Тогда запомни хотя бы так."
            cs_narrator "Я повторила."
            cs_narrator "Со второго раза стало похоже."
            $ cs_d6_mi_known_motif = True
        else:
            $ cs_d6_focus("mi")
            cs_mi "Это короткий напев на прощание."
            cs_mi "Новый — такого мы ещё не играли."
            cs_narrator "Она напела и положила в конверт несколько записанных тактов."
        $ cs_d6_mi_music_received = True
    cs_narrator "Потом Мику побежала в салон, прижимая к себе сумку."
    with None
    $ cs_actor_exit(["mi"])
    $ cs_d6_cast = [t for t in cs_d6_cast if t != "mi"]
    with cs_sprite_leave
    cs_narrator "Женя задержалась у ступенек."
    $ cs_d6_focus("mz")
    cs_mz "Записи не смешивай."
    if cs_d6_mz_address_received:
        $ cs_d6_focus("ls")
        cs_ls "Адрес отдельно."
        cs_ls "Наблюдения отдельно."
        cs_ls "Фантазии оставила в голове."
    else:
        $ cs_d6_focus("ls")
        cs_ls "Наблюдения отдельно."
        cs_ls "Фантазии оставила в голове."
    $ cs_d6_focus("mz")
    cs_mz "Там им и место."
    if cs_friend_mz >= 4 and cs_d6_mz_listened:
        cs_narrator "Я коротко спросила, можно ли её обнять."
        cs_narrator "Женя вздохнула, но кивнула."
        $ cs_d6_focus("mz")
        cs_mz "И не заходи ночью в старый корпус."
        $ cs_d6_focus("ls")
        cs_ls "Даже в объятиях инструкции выдаёшь."
        $ cs_d6_focus("mz")
        cs_mz "Иначе не слушаешь."
    else:
        cs_narrator "Женя кивнула на прощание и поднялась в автобус."
    with None
    $ cs_actor_exit(["cs_zhenya"])
    $ cs_d6_cast = [t for t in cs_d6_cast if t != "cs_zhenya"]
    with cs_sprite_leave
    cs_narrator "Тихонова подошла последней из девушек."
    cs_narrator "Протянула мне утренний набросок Даши."
    if cs_d6_sketch_done and cs_friend_un >= 4:
        $ cs_d6_focus("un")
        cs_un "Тебе."
        cs_un "Я у себя оставила твою руку."
        $ cs_d6_focus("ls")
        cs_ls "Звучит тревожно."
        cs_narrator "Она посмотрела на собственный рисунок и тихо засмеялась."
        $ cs_d6_focus("un")
        cs_un "Ты поняла."
        $ cs_d6_focus("ls")
        cs_ls "Поняла."
        cs_ls "Спасибо."
        cs_narrator "Я убрала лист между двумя чистыми страницами, чтобы не помять."
        $ cs_d6_un_sketch_received = True
    else:
        cs_narrator "Тихонова коротко пожала мне руку."
        cs_narrator "Альбом остался у неё."
        $ cs_d6_focus("un")
        cs_un "Хорошей дороги завтра."
        $ cs_d6_focus("ls")
        cs_ls "И тебе сегодня."
    with None
    $ cs_actor_exit(["un"])
    $ cs_d6_cast = [t for t in cs_d6_cast if t != "un"]
    with cs_sprite_leave
    if cs_d6_before("se") >= 1:
        cs_narrator "Семён ждал, пока остальные устроятся."
        cs_narrator "Когда он подошёл к двери, я окликнула его."
        cs_narrator "Без крика на весь лагерь."
        cs_narrator "Он и так стоял в двух шагах."
        $ cs_d6_focus("ls")
        cs_ls "Можно?"
        cs_narrator "Я раскрыла руки."
        cs_narrator "Семён сам шагнул навстречу."
        $ cs_d6_cg("cs_cg_day06_semen_farewell_day")
        $ cs_d6_focus("sy")
        cs_sy "Ты меня уже утром проверила."
        $ cs_d6_focus("ls")
        cs_ls "Это контроль перед отправкой."
        cs_narrator "Обняла крепко, но быстро отпустила."
        cs_narrator "Ему ещё предстояло зайти в автобус, и превращать это в испытание я не хотела."
        $ cs_d6_focus("ls")
        cs_ls "Доедешь."
        $ cs_d6_focus("sy")
        cs_sy "Постараюсь."
        $ cs_d6_focus("ls")
        cs_ls "Принимается."
        cs_narrator "Он удивлённо посмотрел на меня."
        $ cs_d6_focus("sy")
        cs_sy "Без обещания на всю жизнь?"
        $ cs_d6_focus("ls")
        cs_ls "Я сегодня уже почти взрослый человек."
        cs_ls "Пользуйся, пока не прошло."
        $ cs_d6_room("bg ext_bus",['cs_darya', 'cs_semen', 'mt', 'cs_zhenya', 'un', 'sl', 'dv', 'mi'])
        if cs_d6_se_address_offered:
            cs_narrator "Семён улыбнулся и передал мне сложенный листок с адресом."
            $ cs_d6_focus("sy")
            cs_sy "Вот."
            cs_sy "Чтобы не начала опять требовать."
            $ cs_d6_focus("ls")
            cs_ls "Заботливый."
            $ cs_d6_se_address_received = True
        if cs_d6_se_agency and cs_friend_se >= 4:
            cs_narrator "Перед посадкой Семён оставил нам ещё один лист."
            cs_narrator "На нём были его последние воспоминания о ночи: карточка, слова голоса и вопрос о выборе."
            $ cs_d6_focus("sy")
            cs_sy "Сравните со своим рассказом."
            cs_sy "Тут только то, что я сам помню."
            $ cs_d6_focus("ls")
            cs_ls "Спасибо."
            $ cs_d6_se_account_received = True
        cs_narrator "Даша пожала ему руку."
        cs_narrator "Они о чём-то тихо договорились — я расслышала только «если получится»."
        cs_narrator "Потом Семён поднялся по ступенькам и обернулся."
        $ cs_d6_focus("sy")
        cs_sy "До встречи, Лена."
        $ cs_d6_focus("ls")
        cs_ls "До встречи, Сёмочка."
        $ cs_d6_focus("sy")
        cs_sy "Я так и знал."
        cs_narrator "Он ушёл в салон, а я осталась внизу с его адресом в руке."
    else:
        cs_narrator "Семён подошёл к автобусу."
        cs_narrator "Даша пожала ему руку; я пожелала хорошей дороги."
        if cs_d6_se_address_offered:
            cs_narrator "Семён протянул заново записанный адрес."
            $ cs_d6_focus("sy")
            cs_sy "Вчерашний лист пропал."
            cs_sy "Этот положи отдельно."
            $ cs_d6_focus("ls")
            cs_ls "Спасибо."
            $ cs_d6_se_address_received = True
        $ cs_d6_focus("sy")
        cs_sy "До встречи."
        $ cs_d6_focus("ls")
        cs_ls "До встречи, Семён."
        cs_narrator "Он поднялся в салон."
    $ cs_actor_exit(["cs_semen"])
    $ cs_d6_cast = [t for t in cs_d6_cast if t != "cs_semen"]
    with cs_sprite_leave
    if cs_d6_se_address_received:
        cs_narrator "Я осталась у ступенек с его адресом в руке."
    if cs_da_shared_bed_day3 and cs_da_love_confession_day3:
        cs_narrator "Когда Семён сел, Даша взяла меня за руку."
        $ cs_d6_focus("da")
        cs_da "Отпустила?"
        $ cs_d6_focus("ls")
        cs_ls "Физически — да."
        cs_ls "Мысленно ещё держу за воротник."
        $ cs_d6_focus("da")
        cs_da "Отпускай постепенно."
        cs_narrator "Я переплела наши пальцы и кивнула."
    $ cs_d6_think()
    cs_narrator "Пётр закрыл двери."
    cs_narrator "Мику замахала нам из окна, Алиса что-то крикнула, но двигатель заглушил слова."
    $ cs_d6_cg("cs_cg_day06_semen_bus_wave")
    cs_narrator "Семён сел у окна."
    cs_narrator "Я подняла руку; он ответил тем же."
    $ cs_bus_cue("close")
    $ cs_bus_engine("depart")
    cs_narrator "Автобус выехал за ворота и покатил по дороге."
    cs_narrator "Мы смотрели, пока он не скрылся за поворотом."
    stop music fadeout 1.5
    cs_narrator "Ещё немного был слышен мотор."
    cs_narrator "Потом стих и он."
    $ cs_bus_cue("gone")
    $ cs_d6_bus_departed = True
    $ cs_d6_room("bg ext_no_bus",['cs_darya', 'mt', 'cs'])
    stop sound fadeout 0.6
    stop music fadeout 2.0
    cs_narrator "Ольга сложила список."
    $ cs_d6_focus("mt")
    cs_mt "Всё."
    cs_mt "Уехали."
    $ cs_d6_think()
    cs_narrator "Я не ответила сразу."
    cs_narrator "Пока мы провожали автобус, лагерь успел опустеть."
    cs_narrator "У ворот остался след колёс и маленькая ленточка от чьей-то сумки."
    cs_narrator "Даша подняла её и положила на столбик."
    $ cs_d6_focus("da")
    cs_da "Пойдём?"
    cs_narrator "Я кивнула."
    if cs_d6_towels_carried:
        cs_narrator "Ольга попросила нас занести полотенца на склад и потом зайти к ней."
        cs_narrator "Виола пошла закрывать медпункт после осмотра уезжавших."
    else:
        cs_narrator "Ольга попросила зайти к ней за поручением."
        cs_narrator "Виола пошла закрывать медпункт после осмотра уезжавших."
    cs_narrator "На площади я привычно свернула к скамейке, где обычно сидели наши."
    cs_narrator "И только тогда заметила, что не к кому сворачивать."
    $ cs_d6_focus("da")
    cs_da "Будет тихо."
    $ cs_d6_focus("ls")
    cs_ls "Ужасно."
    cs_ls "Теперь все мои гениальные замечания достанутся тебе одной."
    if cs_d6_towels_carried:
        cs_narrator "Она забрала у меня половину полотенец."
        $ cs_d6_focus("da")
        cs_da "Выдержу."
        cs_da "Только сначала на склад."
    else:
        $ cs_d6_focus("da")
        cs_da "Выдержу."
        cs_da "Пойдём к Ольге."
    cs_narrator "Семён прожил здесь на день больше нас."
    cs_narrator "Его седьмой день закончился отъездом — насколько мы могли судить с обочины."
    $ cs_d6_think()
    cs_th "Я ещё раз посмотрела на пустую дорогу и пошла за Дашей."
    $ cs_d6_room("cs_camp_path_day",['cs_darya'])
    cs_narrator "Наш шестой продолжался."
    return
