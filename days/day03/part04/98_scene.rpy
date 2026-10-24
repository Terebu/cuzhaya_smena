# -*- coding: utf-8 -*-
label cs_day03_98:
    $ save_name = "Чужая смена — День 3: Условно здоровая гражданка"
    $ cs_director_scene("bg int_aidpost_day")
    scene bg int_aidpost_day
    show cs custom warm_smile medical normal at cs_viola_normal_left
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    stop music fadeout 2.0
    play ambience "sound/ambiences/medstation_inside_day.ogg" fadein 1.5
    label cs_check_day03_98:
    cs_narrator "В медпункте пахло лекарствами."
    cs_narrator "На столе лежали какие-то записи."
    cs_narrator "Возле шкафа стояла небольшая коробка с перевязочными материалами."
    cs_narrator "Виола сидела за столом."
    cs_narrator "Услышав шаги, она подняла голову."
    cs_narrator "Увидела меня."
    cs_narrator "Потом Дарью."
    cs_narrator "Затем опустила взгляд на повязку."
    cs_narrator "И улыбнулась."
    cs_vi "Доброе утро, пионерки."
    cs_narrator "Я кивнула."
    cs_ls "Доброе."
    cs_vi "Смотрю, решила не заставлять меня искать тебя по всему лагерю."
    cs_narrator "Я приложила здоровую ладонь к груди."
    cs_ls "Более того, явилась совершенно добровольно."
    cs_narrator "Она приподняла бровь."
    cs_vi "Вот как?"
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Правда. Сама предложила зайти после завтрака."
    cs_narrator "Виола посмотрела на меня внимательнее."
    cs_vi "Похвально. Тогда садись, посмотрим, как поживает твой локоть."
    cs_narrator "Я послушно устроилась на кушетке."
    cs_ls "Докладываю: локоть по-прежнему находится при мне."
    if renpy.showing("cs"):
        show cs custom amused medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола усмехнулась."
    cs_vi "Очень хорошо. Желательно, чтобы так и продолжалось."
    cs_th "Прекрасно."
    cs_th "Кажется, сегодня все решили соревноваться со мной в остроумии."
    cs_narrator "Она подошла ближе."
    cs_narrator "Осторожно осмотрела повязку."
    cs_vi "Ночью сильно болело?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Иногда немного тянуло, когда сгибала руку."
    cs_vi "А сегодня?"
    cs_narrator "Я помолчала."
    cs_narrator "Дарья посмотрела на меня."
    cs_th "Так."
    cs_th "Начинается медицинский допрос."
    cs_th "Врать бессмысленно."
    cs_ls "Утром попробовала пробежаться."
    cs_narrator "Виола перестала поправлять бинт."
    cs_narrator "Медленно подняла взгляд."
    cs_vi "Лена."
    cs_narrator "Я вздохнула."
    cs_ls "Знаю."
    cs_vi "Что именно знаешь?"
    cs_ls "Что вчера вы просили не нагружать руку."
    cs_narrator "Она кивнула."
    cs_vi "И как это соотносится с пробежкой?"
    cs_narrator "Я задумалась."
    cs_ls "Ну, технически я бегала ногами."
    if renpy.showing("cs_darya"):
        show cs_darya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья закрыла глаза."
    cs_narrator "Я добавила:"
    cs_ls "Рука присутствовала исключительно в качестве свидетеля."
    cs_narrator "Наступила короткая пауза."
    cs_narrator "Виола посмотрела на меня."
    cs_narrator "Потом неожиданно улыбнулась."
    cs_vi "Свидетеля, которого тоже подвергли нагрузке."
    cs_narrator "Я опустила взгляд."
    cs_ls "Согласна. Процессуальное нарушение."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Виола осторожно начала снимать повязку."
    cs_vi "А если серьёзно?"
    cs_narrator "Я подняла голову."
    cs_ls "Почувствовала боль почти сразу. Поэтому перестала и дальше просто ходила."
    cs_narrator "Она кивнула."
    cs_vi "Хорошо, что не стала продолжать. Сегодня пока обойдись без бега и упражнений, которые нагружают руку."
    cs_narrator "Я вздохнула."
    cs_ls "То есть турник окончательно отправлен в отпуск."
    cs_vi "Пока да."
    cs_ls "А можно подать апелляцию?"
    cs_narrator "Она посмотрела на меня."
    cs_vi "Можно."
    cs_narrator "Я удивлённо подняла бровь."
    cs_ls "Серьёзно?"
    cs_vi "Конечно. Рассмотрю, когда локоть заживёт."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я несколько секунд смотрела на медсестру."
    cs_narrator "Потом медленно кивнула."
    cs_ls "Блестяще. Юридически безупречный отказ."
    if renpy.showing("cs"):
        show cs custom warm_smile medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола улыбнулась."
    cs_vi "Спасибо."
    return
