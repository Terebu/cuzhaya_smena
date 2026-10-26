# -*- coding: utf-8 -*-
label cs_day03_152:
    $ save_name = "Чужая смена — День 3: Конкуренцию выиграла столовая"
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я снова открыла роман."
    cs_narrator "На этот раз совершенно спокойно."
    cs_narrator "Устроилась поудобнее."
    cs_narrator "Дарья вернулась к своим записям."
    cs_narrator "Некоторое время мы почти не разговаривали."
    cs_narrator "Я читала."
    cs_narrator "Она занималась своим."
    cs_narrator "Иногда кто-то проходил мимо домика."
    cs_narrator "Иногда в окно заглядывал ветер."
    cs_narrator "Всё было настолько обыкновенно, что мне даже не хотелось искать в происходящем какой-то скрытый смысл."
    cs_narrator "Наверное, так и выглядит нормальный отдых."
    cs_narrator "Без расписания."
    cs_narrator "Без необходимости куда-нибудь бежать."
    cs_narrator "И без Семёна, которого можно было бы довести до нервного тика."
    cs_narrator "Я едва заметно улыбнулась."
    cs_narrator "Перевернула страницу."
    if not cs_day03_dinner_horn_played:
        $ cs_day03_dinner_horn_played = True
        label cs_check_day03_152_horn:
        play sound "sound/sfx/dinner_horn_processed.ogg"
    $ renpy.music.set_volume(0.04,delay=0.7,channel="music")
    cs_narrator "И тут за окном раздался горн."
    cs_narrator "Я услышала его."
    cs_narrator "Конечно, услышала."
    cs_narrator "Но решила сначала закончить абзац."
    cs_th "Так."
    cs_narrator "Ещё пара предложений."
    cs_narrator "И всё."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Дарья подняла голову."
    cs_da "Лен."
    cs_narrator "Я продолжила читать."
    cs_ls "М?"
    cs_da "Ужин."
    cs_narrator "Я кивнула."
    cs_ls "Ага."
    cs_narrator "Дочитала предложение."
    cs_narrator "Перевернула страницу."
    cs_narrator "Вот теперь можно…"
    cs_narrator "Нет."
    cs_narrator "На следующей странице происходило что-то интересное."
    cs_narrator "Ладно."
    cs_narrator "Ещё немного."
    cs_da "Лена."
    cs_narrator "Я подняла глаза."
    cs_ls "Что?"
    cs_narrator "Она улыбнулась."
    cs_da "Ты сейчас собираешься сказать «ещё пять минут»?"
    cs_narrator "Я задумалась."
    cs_ls "Вообще-то да."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Я так и знала."
    cs_narrator "Я посмотрела на книгу."
    cs_narrator "Потом на неё."
    cs_ls "Даш, пойми. Здесь чрезвычайно важный момент."
    cs_narrator "Она приподняла бровь."
    cs_da "Настолько важный, что ты готова пропустить ужин?"
    cs_narrator "Я посмотрела на страницу."
    cs_narrator "Немного подумала."
    cs_narrator "Потом на Дарью."
    cs_th "Чёрт."
    cs_narrator "Вопрос поставлен исключительно грамотно."
    cs_ls "Так."
    cs_narrator "Она улыбнулась."
    cs_da "Что?"
    cs_narrator "Я закрыла книгу."
    cs_narrator "Аккуратно вставила закладку."
    cs_narrator "И положила роман на кровать."
    cs_ls "Победила еда."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Даже не я?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даша, не заставляй меня устраивать рейтинг важнейших составляющих человеческого существования."
    cs_narrator "Она усмехнулась."
    cs_da "А какое там у меня место?"
    cs_narrator "Я задумалась."
    cs_narrator "Потом совершенно серьёзно ответила:"
    cs_ls "Сведения засекречены."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я осторожно поднялась."
    cs_narrator "Поправила юбку."
    cs_narrator "Разгладила рубашку."
    cs_narrator "Затем поправила галстук."
    cs_th "Так."
    cs_narrator "Гражданка Соколова временно возвращается из литературной действительности в советскую."
    cs_narrator "Дарья встала следом."
    cs_da "Ну что, идём?"
    cs_narrator "Я кивнула."
    cs_ls "Сейчас."
    cs_narrator "Подошла к столу."
    $ cs_day03_reading_book_location = "house_table"
    cs_narrator "Положила книгу рядом с блокнотом."
    cs_narrator "Аккуратно, подальше от края."
    cs_ls "Всё. После ужина продолжу."
    cs_narrator "Дарья театрально вздохнула."
    cs_da "Понятно."
    cs_narrator "Я повернулась."
    cs_ls "Что?"
    cs_narrator "Она посмотрела на книгу."
    cs_narrator "Потом на меня."
    cs_da "Сегодня я окончательно проиграла литературе."
    cs_narrator "Я задумалась."
    cs_narrator "Подошла к ней ближе."
    cs_ls "Ну не совсем."
    cs_narrator "Она приподняла бровь."
    cs_da "Правда?"
    cs_narrator "Я чуть улыбнулась."
    $ cs_da_cheek_kiss_day3 = True
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом быстро поцеловала её в щёку."
    cs_narrator "Совершенно просто."
    cs_narrator "Без торжественного объявления."
    cs_narrator "И отступила на полшага."
    cs_narrator "Дарья замерла."
    cs_narrator "Посмотрела на меня."
    cs_da "Лен…"
    cs_narrator "Я подняла бровь."
    cs_ls "Что?"
    cs_narrator "Она коснулась щеки."
    cs_narrator "Потом улыбнулась."
    cs_da "Это сейчас что было?"
    cs_narrator "Я задумалась."
    cs_ls "Компенсация за моральный ущерб, причинённый русской классикой."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Но через секунду посмотрела на меня чуть внимательнее."
    cs_da "А если без шуток?"
    cs_narrator "Я немного помолчала."
    cs_narrator "Потом улыбнулась уже спокойнее."
    cs_ls "Просто захотелось."
    cs_narrator "Дарья несколько секунд смотрела на меня."
    cs_narrator "Затем улыбнулась."
    cs_da "Мне понравилось."
    cs_narrator "Я почувствовала, как немного теплеют щёки."
    cs_th "Так."
    cs_narrator "Вот теперь действительно пора на ужин."
    cs_narrator "Пока я окончательно не разучилась произносить нормальные слова."
    cs_narrator "Я выпрямилась."
    cs_ls "Прекрасно. Значит, дипломатический инцидент исчерпан."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Ты неисправима."
    cs_narrator "Я кивнула."
    cs_ls "Есть немного."
    cs_narrator "Потом протянула ей здоровую руку."
    cs_ls "Пойдём?"
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_narrator "Взяла меня за руку."
    cs_da "Пойдём."
    cs_th "Ну вот."
    cs_narrator "И никакого специального названия для того, что между нами происходит, пока не требуется."
    cs_narrator "Просто приятно быть рядом."
    return
