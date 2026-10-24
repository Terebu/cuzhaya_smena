# -*- coding: utf-8 -*-
label cs_day03_105:
    $ save_name = "Чужая смена — День 3: Приём у начальства"
    $ cs_director_scene("bg ext_house_of_mt_day")
    scene bg ext_house_of_mt_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    show mt normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_105:
    cs_narrator "Ольга Дмитриевна обнаружилась на крыльце своего домика."
    cs_narrator "Она стояла возле небольшого столика и перебирала бумаги."
    cs_narrator "Часть листов была сложена в аккуратную стопку."
    cs_narrator "Другие лежали отдельно, прижатые какой-то тетрадью."
    cs_narrator "Судя по выражению её лица, советская административная система прямо сейчас испытывала временные трудности."
    cs_th "Знакомая картина."
    cs_th "Меняются десятилетия, технологии и государственные устройства, но бумажная работа остаётся вечной."
    cs_narrator "Я подошла ближе."
    cs_ls "Доброе утро, Ольга Дмитриевна."
    cs_narrator "Она подняла голову."
    cs_narrator "Увидела меня."
    cs_narrator "Потом Дарью."
    cs_narrator "Потом мою свежую повязку."
    cs_narrator "И медленно вздохнула."
    if renpy.showing("mt"):
        show mt normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mt "Доброе. Что на этот раз?"
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела на неё."
    cs_ls "А почему сразу «на этот раз»?"
    if renpy.showing("mt"):
        show mt surprise pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она приподняла бровь."
    cs_mt "Лена, за два дня ты успела заблудиться за воротами, дважды поранить руку и задать мне столько вопросов, сколько остальные пионеры не задают за всю смену."
    cs_narrator "Я задумалась."
    cs_ls "Зато теперь вы точно запомнили моё имя."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Ольга Дмитриевна покачала головой."
    cs_narrator "Но тоже едва заметно улыбнулась."
    cs_mt "Это уж точно."
    cs_narrator "Я выпрямилась."
    cs_ls "Вообще-то мы пришли по хорошему делу."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_mt "Какому?"
    cs_ls "Хотели узнать, не нужна ли вам помощь."
    cs_narrator "Наступила пауза."
    cs_narrator "Ольга Дмитриевна посмотрела на Дарью."
    cs_mt "Это её идея?"
    cs_narrator "Дарья покачала головой."
    cs_da "Нет. Лена сама предложила."
    cs_narrator "Вожатая перевела взгляд на меня."
    if renpy.showing("mt"):
        show mt surprise pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mt "Сама?"
    cs_narrator "Я приложила здоровую ладонь к груди."
    cs_ls "Кажется, сегодня мне никто не верит."
    cs_mt "Просто удивляюсь."
    cs_ls "Удивляться можно. Но желательно с положительной оценкой моей инициативы."
    cs_narrator "Она усмехнулась."
    cs_mt "А руку ты уже показывала Виоле?"
    cs_narrator "Я кивнула."
    cs_ls "Только что от неё. Повязку сменили, спортивные подвиги временно отменены."
    if renpy.showing("mt"):
        show mt smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Ольга Дмитриевна заметно расслабилась."
    cs_mt "Вот и правильно."
    cs_ls "Слово «правильно» сегодня преследует меня с раннего утра."
    cs_mt "Значит, есть повод задуматься."
    cs_narrator "Я вздохнула."
    cs_ls "К сожалению, это уже не первое обоснованное замечание за сегодня."
    cs_narrator "Она улыбнулась."
    cs_narrator "Потом посмотрела на бумаги."
    cs_mt "Помощь, говоришь?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Только желательно без переноски тяжёлых предметов. Моя левая рука сегодня работает исключительно в консультативном режиме."
    cs_narrator "Дарья усмехнулась."
    cs_narrator "Ольга Дмитриевна взглянула на повязку."
    cs_mt "С этим согласна. Тяжёлого ничего не дам."
    cs_narrator "Она взяла со стола тонкую папку."
    cs_narrator "Проверила содержимое."
    cs_mt "Нужно передать эти документы в администрацию. Там их ждут."
    cs_narrator "Я посмотрела на папку."
    cs_ls "Это всё?"
    cs_mt "Пока да."
    cs_ls "Даже немного обидно. Я мысленно готовилась к пятилетнему плану развития лагерного хозяйства."
    cs_narrator "Она рассмеялась."
    cs_mt "Начнём с малого."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Я могу отнести папку."
    $ cs_day03_documents_location = "darya"
    label cs_check_day03_105_documents:
    cs_narrator "Ольга Дмитриевна протянула её Дарье."
    cs_mt "Спасибо. А потом, если останется время, загляните к Славе. Она разбирает вчерашний инвентарь."
    cs_narrator "Я кивнула."
    cs_ls "Понятно."
    cs_narrator "Немного подумала."
    cs_ls "То есть сначала документооборот, потом хозяйственный учёт."
    cs_narrator "Ольга Дмитриевна улыбнулась."
    cs_mt "Именно."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Поздравляю. Нас официально приняли на государственную службу."
    cs_narrator "Она тихо рассмеялась."
    cs_da "Главное, чтобы без переработок."
    if renpy.showing("mt"):
        show mt grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mt "Если будете меньше разговаривать, управитесь быстрее."
    cs_narrator "Я повернулась к вожатой."
    cs_th "Ого."
    cs_th "Похоже, сарказм здесь начинает передаваться воздушно-капельным путём."
    cs_ls "Ольга Дмитриевна, это сейчас было почти обидно."
    cs_narrator "Она совершенно спокойно ответила:"
    cs_mt "А я ещё даже не начала."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я несколько секунд смотрела на вожатую."
    cs_narrator "Затем медленно кивнула."
    cs_ls "Хорошо. Признаю: педагогический состав лагеря обладает определённым преимуществом."
    cs_narrator "Ольга Дмитриевна улыбнулась."
    return
