# -*- coding: utf-8 -*-
label cs_day03_106:
    $ save_name = "Чужая смена — День 3: Социально-бытовые исследования"
    cs_narrator "Я уже собиралась попрощаться, когда в голове всплыл один вопрос."
    cs_th "Нет."
    cs_th "Соколова, даже не начинай."
    cs_th "Ты ведь обещала вести себя прилично."
    cs_narrator "Я посмотрела на домик."
    cs_narrator "Потом на вожатую."
    cs_th "Хотя один вопрос — это ещё не допрос."
    cs_ls "Кстати, Ольга Дмитриевна."
    if renpy.showing("mt"):
        show mt normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она немедленно насторожилась."
    cs_mt "Что?"
    cs_narrator "Я придала лицу наиболее невинное выражение."
    cs_ls "Как там Семён поживает?"
    cs_narrator "Ольга Дмитриевна моргнула."
    cs_mt "Нормально. А что?"
    cs_narrator "Я кивнула."
    cs_ls "Хорошо."
    cs_narrator "Пауза."
    cs_mt "Лена?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Да?"
    cs_mt "Ты что-то задумала?"
    cs_narrator "Я несколько секунд изображала глубокое размышление."
    cs_ls "Просто интересуюсь бытовыми условиями проживания нашего общего знакомого."
    cs_narrator "Дарья медленно повернулась ко мне."
    cs_th "Ой."
    cs_th "Кажется, началось."
    if renpy.showing("mt"):
        show mt angry pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Ольга Дмитриевна прищурилась."
    cs_mt "Какими ещё условиями?"
    cs_narrator "Я подняла палец."
    cs_ls "Ну, знаете. Один домик. Два человека. Ограниченная территория."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Потом на Дарью."
    cs_narrator "Затем медленно выдохнула."
    cs_mt "Соколова."
    cs_narrator "Я выпрямилась."
    cs_ls "Слушаю."
    cs_mt "Семёна поселили со мной, потому что свободных мест почти не осталось. Если ты вдруг забыла."
    cs_narrator "Я кивнула."
    cs_ls "Разумеется."
    cs_narrator "Она продолжила:"
    cs_mt "И у меня совершенно нет времени обсуждать с тобой чужие бытовые привычки."
    cs_narrator "Я выдержала паузу."
    cs_narrator "Потом совершенно серьёзно спросила:"
    cs_ls "Даже вопрос о том, кто первым занимает умывальник?"
    cs_narrator "Дарья не выдержала и рассмеялась."
    cs_narrator "Ольга Дмитриевна посмотрела на меня."
    if renpy.showing("mt"):
        show mt grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом неожиданно тоже усмехнулась."
    cs_mt "Обычно тот, кто раньше встаёт."
    cs_narrator "Я кивнула."
    cs_ls "Наконец-то конкретные сведения."
    cs_narrator "Она вздохнула."
    cs_mt "Лена."
    cs_narrator "Я улыбнулась."
    cs_ls "Всё, всё. Больше не пристаю."
    cs_narrator "Ольга Дмитриевна посмотрела на меня внимательнее."
    cs_mt "И правильно. Лучше бы ты с таким же интересом относилась к лагерным обязанностям."
    cs_narrator "Я кивнула на папку в руках Дарьи."
    cs_ls "Вот поэтому и пришла. Сегодня пытаюсь исправить общественное мнение."
    cs_narrator "Вожатая усмехнулась."
    cs_mt "Тогда начни с того, что донеси бумаги куда следует."
    cs_ls "Есть."
    cs_narrator "Я уже собиралась развернуться."
    cs_narrator "Но Ольга Дмитриевна вдруг окликнула меня."
    cs_mt "И ещё, Лена."
    cs_narrator "Я остановилась."
    cs_ls "Да?"
    if renpy.showing("mt"):
        show mt normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она посмотрела на меня уже без улыбки."
    cs_mt "Надеюсь, сегодня вы не собираетесь снова выходить за ворота?"
    cs_narrator "Я немного помолчала."
    cs_th "А вот это уже серьёзно."
    cs_ls "Нет. Сегодня никаких походов."
    cs_narrator "Она кивнула."
    cs_mt "Хорошо."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Мы вчера, конечно, повели себя не особенно разумно."
    cs_narrator "Дарья тоже кивнула."
    cs_da "Нужно было хотя бы предупредить."
    cs_narrator "Вожатая вздохнула."
    cs_mt "Именно. Даже если вам хочется что-то исследовать, нельзя просто исчезать из лагеря."
    cs_narrator "Я немного опустила взгляд."
    cs_th "И ведь она права."
    cs_th "Какие бы странности ни происходили на дороге, для неё мы трое — пионеры, за которых она отвечает."
    cs_ls "Понимаю. Извините."
    if renpy.showing("mt"):
        show mt surprise pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Ольга Дмитриевна посмотрела на меня с явным удивлением."
    cs_mt "Лена…"
    cs_narrator "Я подняла голову."
    cs_ls "Что?"
    cs_narrator "Она покачала головой."
    cs_narrator "И чуть улыбнулась."
    cs_mt "Ничего. Просто приятно, что ты иногда умеешь быть серьёзной."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Иногда даже сама удивляюсь."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    if renpy.showing("mt"):
        show mt smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Ольга Дмитриевна посмотрела на нас обеих."
    cs_mt "Ладно. Идите уже."
    cs_narrator "Я выпрямилась."
    cs_ls "Разрешите приступать к выполнению поручения?"
    cs_narrator "Она улыбнулась."
    cs_mt "Разрешаю."
    cs_ls "Есть."
    $ cs_actor_exit(["mt"])
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_106_mt_left:
    cs_narrator "Мы попрощались и направились к площади."
    cs_narrator "Я некоторое время молчала."
    cs_narrator "Потом посмотрела на Дарью."
    cs_narrator "Она несла папку."
    cs_da "Ну что?"
    cs_narrator "Я задумалась."
    cs_ls "Полагаю, переговоры прошли успешно."
    cs_da "Тебе сделали замечание."
    cs_ls "Зато не отобрали поручение. Значит, уровень доверия пока положительный."
    cs_narrator "Она улыбнулась."
    cs_da "Очень своеобразная система оценки."
    cs_narrator "Я кивнула."
    cs_ls "Зато объективная."
    cs_narrator "Потом немного помолчала."
    cs_ls "Хотя насчёт дороги она действительно права."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Да."
    cs_narrator "Мы продолжили идти."
    $ cs_reflective_focus()
    with cs_sprite_leave
    cs_th "И, пожалуй, это было важнее всех моих шуток."
    cs_th "Я уже начинала чувствовать себя здесь достаточно свободно, чтобы забывать: для некоторых людей наши выходки — не развлечения."
    cs_th "Им потом приходится за нас отвечать."
    return
