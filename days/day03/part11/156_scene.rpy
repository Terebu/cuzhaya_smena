# -*- coding: utf-8 -*-
label cs_day03_156:
    $ save_name = "Чужая смена — День 3: Книга, которая всё ещё не закончилась"
    $ cs_director_scene("bg int_dining_hall_sunset")
    scene bg int_dining_hall_sunset
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with Dissolve(0.7)
    play ambience "sound/ambiences/dining_hall_full.ogg" fadeout 1.5 fadein 1.5
    cs_narrator "Очередь двигалась довольно быстро."
    cs_narrator "Я взяла поднос."
    cs_narrator "Женя — следующий."
    cs_narrator "Дарья встала рядом."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом Женя неожиданно повернулась ко мне."
    cs_mz "Ну что?"
    cs_narrator "Я подняла бровь."
    cs_ls "Что?"
    cs_narrator "Она посмотрела на меня поверх очков."
    cs_mz "Книгу дочитала?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Прочитала ещё несколько глав, но до конца пока далеко."
    cs_narrator "Женя кивнула."
    cs_mz "И как?"
    cs_narrator "Я немного задумалась."
    cs_ls "Ты была права."
    cs_narrator "Она приподняла бровь."
    cs_mz "В чём именно?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "В том, что история постепенно становится интереснее."
    cs_narrator "Немного помолчала."
    cs_ls "Мне нравится, как меняются отношения между героями. Причём не потому, что автор внезапно решил сделать кого-нибудь злодеем."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя улыбнулась."
    cs_mz "А почему?"
    cs_narrator "Я пожала плечами."
    cs_ls "Потому что они сами меняются. Иногда незаметно для себя."
    cs_narrator "Она кивнула."
    cs_mz "Именно."
    cs_narrator "Я задумалась."
    cs_ls "Хотя некоторых всё равно хочется взять за плечи и хорошенько встряхнуть."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Вот поэтому я и говорила тебе дочитать."
    if cs_mz_friend_on_arrival_day3 >= 1:
        cs_ls "Уже начинаю подозревать, что ты специально выбрала произведение, чтобы проверить мою способность спокойно воспринимать чужие ошибки."
    else:
        cs_ls "Начинаю подозревать, что эта книга проверяет мою способность спокойно воспринимать чужие ошибки."
    cs_narrator "Она посмотрела на меня."
    cs_mz "И как успехи?"
    cs_narrator "Я вздохнула."
    cs_ls "Пока неудовлетворительно."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Женя тоже слегка улыбнулась."
    if cs_mz_day3_honest_book_talk:
        cs_narrator "Женя немного помолчала."
        cs_narrator "Потом добавила:"
        cs_mz "Кстати, я ещё подумала о том, что ты говорила в библиотеке."
        cs_narrator "Я заинтересовалась."
        cs_ls "О чём?"
        cs_mz "Про решения, после которых человек уже не может вернуться к прежней жизни."
        cs_narrator "Я кивнула."
        cs_mz "Мне кажется, ты немного торопишься с выводами."
        cs_narrator "Я приподняла бровь."
        cs_ls "Почему?"
        cs_narrator "Она слегка улыбнулась."
        cs_mz "Потому что ты ещё не дочитала."
        cs_narrator "Я замолчала."
        cs_narrator "Потом медленно кивнула."
        cs_ls "Очень удобная позиция человека, который уже знает конец."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Зато без спойлеров."
        cs_ls "Ладно. Пока принимаю."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Вы даже за ужином обсуждаете книги?"
        cs_narrator "Я посмотрела на неё."
        cs_ls "А что? Между прочим, это очень культурная форма досуга."
        cs_narrator "Женя кивнула."
        cs_mz "По крайней мере, лучше некоторых твоих шуток."
        cs_narrator "Я замерла."
        cs_narrator "Потом повернулась к ней."
        cs_ls "Женя, это сейчас была попытка задеть моё самолюбие?"
        cs_narrator "Она совершенно спокойно ответила:"
        cs_mz "Получилось?"
        cs_narrator "Я задумалась."
        cs_ls "К сожалению, да."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
        cs_narrator "Женя тоже улыбнулась."
        cs_th "Прекрасно."
        cs_th "Теперь меня подкалывает даже библиотекарь."
        cs_th "Причём делает это весьма профессионально."
    else:
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Дочитай, потом обсудим."
        cs_narrator "Я кивнула."
        cs_ls "Договорились."
    cs_narrator "Очередь продвинулась."
    cs_narrator "Мы получили ужин."
    cs_narrator "Я осторожно устроила поднос так, чтобы не задевать локоть."
    cs_narrator "Женя посмотрела на мою повязку."
    cs_mz "Рука не мешает?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Уже почти привыкла."
    cs_mz "Только не забывай, что это не значит, будто она полностью зажила."
    cs_narrator "Я вздохнула."
    cs_ls "Женя, мне уже не первый раз за сегодня об этом напоминают."
    cs_narrator "Она кивнула."
    cs_mz "Значит, нас четверо разумных."
    cs_narrator "Дарья прыснула со смеху."
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Потом медленно улыбнулась."
    cs_ls "Убедительно. Спор проигран."
    cs_narrator "Мы направились к свободным столам."
    return
