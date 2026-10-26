# -*- coding: utf-8 -*-
label cs_day03_151:
    $ save_name = "Чужая смена — День 3: Последствия хороших знакомств"
    $ cs_director_scene("cs_house_lena_darya_int_sunset")
    scene cs_house_lena_darya_int_sunset
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    play music cs_day_music_home fadein 2.0
    $ renpy.music.set_volume(0.08,delay=1.0,channel="music")
    cs_narrator "Я снова взяла книгу."
    cs_narrator "Но теперь уже не торопилась продолжать чтение."
    cs_narrator "Просто держала её на коленях."
    cs_narrator "Дарья закончила что-то записывать."
    cs_narrator "Посмотрела на меня."
    cs_da "Лен, а тебе сегодня вообще понравилось?"
    cs_narrator "Я подняла голову."
    cs_ls "Что именно?"
    cs_da "День."
    cs_narrator "Я немного удивилась."
    cs_narrator "Потом задумалась."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Хороший вопрос."
    cs_narrator "Вроде бы ничего выдающегося."
    cs_narrator "Обычные лагерные дела."
    cs_narrator "Немного музыки."
    cs_narrator "Несколько разговоров."
    cs_narrator "Рисование."
    cs_narrator "Книги."
    cs_narrator "И постоянные напоминания о том, что моя рука пока не предназначена для героических подвигов."
    cs_narrator "Я улыбнулась."
    $ cs_pov_end()
    with cs_sprite_change
    cs_ls "Да. Очень."
    cs_narrator "Дарья кивнула."
    cs_da "Мне тоже."
    if cs_un_private_drawing_shown_day3:
        cs_narrator "Я посмотрела на блокнот."
        cs_ls "Сегодня Тихонова показала мне личный рисунок. Для неё это, кажется, было непросто."
        cs_narrator "Дарья заинтересовалась."
        cs_da "Правда?"
        cs_narrator "Я кивнула."
        cs_ls "Да."
        cs_narrator "Она улыбнулась."
        cs_da "И какой?"
        cs_narrator "Я немного помолчала."
        cs_narrator "Потом мягко покачала головой."
        cs_ls "Думаю, лучше она сама расскажет, если захочет."
        cs_narrator "Дарья на секунду задумалась."
        cs_narrator "Затем кивнула."
        cs_da "Понимаю."
        cs_narrator "Я улыбнулась."
        cs_narrator "Всё-таки доверие — не повод немедленно пересказывать чужие личные вещи."
    elif cs_un_sketch_completed_day3:
        cs_narrator "Я посмотрела на блокнот."
        cs_ls "Мы сегодня с Тихоновой неплохо порисовали."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "И надолго увлеклись?"
        cs_narrator "Я кивнула."
        cs_ls "Как обычно бывает, когда два художника находят удобное место и забывают о существовании часов."
    else:
        cs_narrator "Я посмотрела на свой блокнот."
        cs_ls "Успела немного порисовать."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Покажешь потом?"
        cs_narrator "Я кивнула."
        cs_ls "Когда доведу до состояния, которое не вызывает желания немедленно спрятать лист."
        cs_narrator "Она тихо рассмеялась."
    cs_narrator "Дарья немного помолчала."
    cs_da "А ещё ты сегодня долго была в библиотеке."
    cs_narrator "Я кивнула."
    cs_ls "Да."
    if cs_mz_open_library_invitation_day3:
        cs_narrator "Я улыбнулась."
        cs_ls "И Женя сама сказала, что я могу приходить даже просто посидеть."
        cs_narrator "Дарья посмотрела на меня."
        cs_da "Значит, она действительно к тебе привыкла."
        cs_narrator "Я немного задумалась."
        cs_ls "Похоже на то."
        cs_narrator "Пауза."
        cs_ls "Хотя официально это пока не подтверждено печатью библиотечного учреждения."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
    else:
        cs_ls "Хорошую книгу взяла. Думаю, завтра снова зайду к Жене."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Тебе там нравится."
        cs_narrator "Я кивнула."
        cs_ls "Очень."
    cs_narrator "Некоторое время мы сидели молча."
    cs_narrator "Потом я посмотрела на Дашу."
    cs_ls "Знаешь, что самое странное?"
    cs_narrator "Она повернулась."
    cs_da "Что?"
    cs_narrator "Я немного подумала."
    cs_ls "Я уже начинаю ждать следующего дня."
    cs_narrator "Она улыбнулась."
    cs_da "Потому что интересно, что будет?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_narrator "Немного помолчала."
    cs_ls "Хотя ещё недавно мне казалось, что я только и буду думать о возвращении домой."
    cs_narrator "Дарья посмотрела в окно."
    cs_da "Я всё равно хочу вернуться."
    cs_narrator "Я кивнула."
    cs_ls "Я тоже."
    cs_narrator "Посмотрела на неё."
    cs_ls "Просто это не мешает мне иногда получать удовольствие от того, что происходит здесь."
    cs_narrator "Она улыбнулась."
    cs_da "Понимаю."
    cs_narrator "Я чуть вздохнула."
    cs_ls "А ещё, кажется, у меня появляется слишком много знакомых."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Тебя это беспокоит?"
    cs_narrator "Я задумалась."
    cs_ls "Немного. Пока справляюсь."
    cs_narrator "Она улыбнулась."
    cs_da "Ты же любишь всё планировать."
    cs_narrator "Я кивнула."
    cs_ls "Но не в таком масштабе. У меня уже есть литературный консультант, музыкальные знакомства и коллега по художественному цеху."
    if cs_se_day3_personal_talk and cs_se_friend_before_square_day3 >= 1:
        cs_narrator "Я немного помолчала."
        cs_ls "А ещё Семён сегодня рассказал кое-что о том, как сам привыкает к лагерю."
        cs_narrator "Дарья кивнула."
        cs_da "Да. Я заметила, что он был откровеннее обычного."
        cs_narrator "Я задумалась."
        cs_ls "Пожалуй, мы наконец начинаем разговаривать не только ради шуток."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "И тебе всё это нравится?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Подумала."
    cs_narrator "И кивнула."
    cs_ls "Да."
    cs_narrator "Потом добавила:"
    cs_ls "Но сейчас, пожалуй, мне больше всего нравится сидеть здесь."
    cs_narrator "Дарья слегка улыбнулась."
    cs_da "Со мной?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Разумеется."
    cs_narrator "Она улыбнулась чуть шире."
    cs_narrator "Я задумалась."
    cs_ls "Хотя Гончаров тоже вносит определённый вклад."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Я уж думала, ты о нём забыла."
    cs_narrator "Я покачала головой."
    cs_ls "Никогда. Наш литературный союз ещё слишком молод."
    cs_narrator "Она закрыла лицо ладонью."
    cs_da "Господи, Лена."
    cs_narrator "Я довольно улыбнулась."
    cs_th "Ну вот."
    cs_narrator "Теперь всё окончательно вернулось на круги своя."
    return
