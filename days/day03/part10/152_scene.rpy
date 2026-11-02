# -*- coding: utf-8 -*-
label cs_day03_152:
    $ save_name = "Чужая смена — День 3: Конкуренцию выиграла столовая"
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я снова открыла роман. На этот раз спокойно. Устроилась поудобнее. Дарья вернулась к своим записям."
    cs_narrator "Некоторое время мы почти не разговаривали. Я читала. Она занималась своим. Иногда кто-то проходил мимо домика."
    cs_narrator "Иногда в окно заглядывал ветер. Всё было настолько обыкновенно, что мне даже не хотелось искать в происходящем какой-то скрытый смысл. Наверное, так и выглядит нормальный отдых. Без расписания."
    cs_narrator "Без необходимости куда-нибудь бежать. И без Семёна, которого можно было бы довести до нервного тика. Я едва заметно улыбнулась. Перевернула страницу."
    if not cs_day03_dinner_horn_played:
        $ cs_day03_dinner_horn_played = True
        label cs_check_day03_152_horn:
        play sound "sound/sfx/dinner_horn_processed.ogg"
    $ renpy.music.set_volume(0.04,delay=0.7,channel="music")
    cs_narrator "И тут за окном раздался горн. Я услышала его. Конечно, услышала. Но решила сначала закончить абзац."
    cs_th "Так."
    cs_narrator "Ещё пара предложений. И всё."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Дарья подняла голову."
    cs_da "Лен."
    cs_narrator "Я продолжила читать."
    cs_ls "М?"
    cs_da "Ужин."
    cs_ls "Ага."
    cs_narrator "Дочитала предложение. Перевернула страницу. Вот теперь можно…"
    cs_narrator "Нет."
    cs_narrator "На следующей странице происходило что-то интересное. Ладно. Ещё немного."
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
    cs_narrator "Я посмотрела на книгу, потом на неё."
    cs_ls "Даш, пойми. Здесь чрезвычайно важный момент."
    cs_narrator "Она приподняла бровь."
    cs_da "Настолько важный, что ты готова пропустить ужин?"
    cs_narrator "Я посмотрела на страницу. Немного подумала, потом на Дарью."
    cs_th "Чёрт."
    cs_narrator "Вопрос поставлен исключительно грамотно."
    cs_ls "Так."
    cs_narrator "Она улыбнулась."
    cs_da "Что?"
    cs_narrator "Я закрыла книгу. Аккуратно вставила закладку. И положила роман на кровать."
    cs_ls "Победила еда."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_da "Даже не я?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даша, не заставляй меня устраивать рейтинг важнейших составляющих человеческого существования."
    cs_narrator "Она усмехнулась."
    cs_da "А какое там у меня место?"
    cs_narrator "Я задумалась. Потом серьёзно ответила:"
    cs_ls "Сведения засекречены."
    cs_narrator "Она рассмеялась. Я осторожно поднялась. Поправила юбку. Разгладила рубашку."
    cs_narrator "Затем поправила галстук."
    cs_th "Так."
    cs_narrator "Гражданка Соколова временно возвращается из литературной действительности в советскую. Дарья встала следом."
    cs_da "Ну что, идём?"
    cs_ls "Сейчас."
    cs_narrator "Подошла к столу."
    $ cs_day03_reading_book_location = "house_table"
    cs_narrator "Положила книгу рядом с блокнотом. Аккуратно, подальше от края."
    cs_ls "Всё. После ужина продолжу."
    cs_narrator "Дарья театрально вздохнула."
    cs_da "Понятно."
    cs_narrator "Я повернулась."
    cs_ls "Что?"
    cs_narrator "Она посмотрела на книгу, потом на меня."
    cs_da "Сегодня я окончательно проиграла литературе."
    cs_narrator "Я задумалась. Подошла к ней ближе."
    cs_ls "Ну не совсем."
    cs_narrator "Она приподняла бровь."
    cs_da "Правда?"
    cs_narrator "Я чуть улыбнулась."
    $ cs_da_cheek_kiss_day3 = True
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом быстро поцеловала её в щёку. Совершенно просто. Без торжественного объявления. И отступила на полшага."
    cs_narrator "Даша замерла. Посмотрела на меня."
    cs_da "Лен…"
    cs_narrator "Я подняла бровь."
    cs_ls "Что?"
    cs_narrator "Она коснулась щеки. Потом улыбнулась."
    cs_da "Это сейчас что было?"
    cs_narrator "Я задумалась."
    cs_ls "Компенсация за моральный ущерб, причинённый русской классикой."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Но через секунду посмотрела на меня чуть внимательнее."
    cs_da "А если без шуток?"
    cs_narrator "Я помолчала. Потом улыбнулась уже спокойнее."
    cs_ls "Просто захотелось."
    cs_narrator "Даша несколько секунд смотрела на меня. Затем улыбнулась."
    cs_da "Мне понравилось."
    cs_narrator "Я почувствовала, как немного теплеют щёки."
    cs_th "Так."
    cs_narrator "Вот теперь действительно пора на ужин. Пока я окончательно не разучилась произносить нормальные слова. Я выпрямилась."
    cs_ls "Прекрасно. Значит, дипломатический инцидент исчерпан."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша рассмеялась."
    cs_da "Ты неисправима."
    cs_ls "Есть немного."
    cs_narrator "Потом протянула ей здоровую руку."
    cs_ls "Пойдём?"
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша улыбнулась. Взяла меня за руку."
    cs_da "Пойдём."
    cs_narrator "Просто приятно быть рядом."
    return
