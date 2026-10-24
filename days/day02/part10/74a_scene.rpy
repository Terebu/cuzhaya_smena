# -*- coding: utf-8 -*-
label cs_day02_74a:
    $ save_name = "Чужая смена — День 2: Переговоры перед сном"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    $ cs_frame_focus(["cs_darya"])
    label cs_check_day03_night_insert:
    cs_narrator "Я уже собиралась устроиться поудобнее и окончательно завершить этот удивительно длинный день, когда заметила кое-что чрезвычайно важное."
    cs_narrator "Свободное место на Дашиной кровати."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Потом на саму Дашу."
    cs_narrator "Она поправляла подушку и, кажется, совершенно не подозревала, что прямо сейчас ей предстоит участвовать в очередном обсуждении условий нашего совместного проживания."
    cs_th "Ну что ж."
    cs_th "Если не спросить, ответа точно не получишь."
    cs_ls "Даш."
    cs_da "М?"
    cs_narrator "Я постаралась придать лицу максимально невинное выражение."
    cs_ls "А сегодня мне разрешается спать с тобой?"
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она подняла голову."
    cs_narrator "Посмотрела на меня."
    cs_narrator "Потом на мою собственную кровать."
    cs_narrator "Затем снова на меня."
    cs_da "Лена."
    cs_narrator "Я выпрямилась."
    cs_ls "Да?"
    cs_da "У тебя есть кровать."
    cs_ls "Существование кровати не является ответом на поставленный вопрос."
    cs_narrator "Она приподняла бровь."
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    cs_da "Тогда нет."
    cs_narrator "Я замерла."
    cs_narrator "Медленно кивнула."
    cs_ls "Понятно."
    cs_narrator "Вздохнула."
    cs_ls "Вопрос о расширении жилплощади отклонён."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Ты ведь заранее знала, что я отвечу."
    cs_ls "Подозревала. Но научный подход требует экспериментального подтверждения."
    cs_narrator "Она покачала головой."
    cs_da "Тогда эксперимент закончен."
    cs_ls "Принято."
    cs_narrator "Я улеглась на свою кровать."
    cs_narrator "Накрылась одеялом."
    cs_narrator "Некоторое время молчала."
    cs_narrator "Потом повернула голову."
    cs_ls "А на будущее заявки принимаются?"
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "И неожиданно улыбнулась."
    cs_da "Может быть, когда-нибудь."
    cs_narrator "Я медленно приподнялась."
    cs_ls "О."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    cs_da "Лена, это не обещание."
    cs_ls "Я понимаю."
    cs_narrator "Пауза."
    cs_ls "Но формулировка заметно мягче предыдущей."
    cs_narrator "Она рассмеялась."
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with cs_sprite_change
    cs_da "Спи уже, переговорщица."
    cs_narrator "Я довольно улыбнулась."
    cs_ls "Спокойной ночи."
    cs_da "Спокойной."
    $ cs_reflective_focus()
    with cs_sprite_leave
    cs_narrator "Я повернулась на бок, стараясь не задевать повреждённый локоть."
    cs_narrator "В комнате постепенно стало тихо."
    cs_th "Нет так нет."
    cs_th "Никуда торопиться не нужно."
    cs_th "В конце концов, сегодня нам и без того было хорошо вместе."
    cs_narrator "А собственная кровать, надо признать, тоже обладала некоторыми неоспоримыми преимуществами."
    cs_narrator "Особенно когда хотелось растянуться по диагонали и никому не мешать."
    cs_narrator "Я закрыла глаза."
    cs_narrator "И вскоре уснула."
    return
