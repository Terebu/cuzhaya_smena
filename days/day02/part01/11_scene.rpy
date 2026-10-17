# -*- coding: utf-8 -*-
label cs_day02_11:
    $ save_name = "Чужая смена — День 2: Трудовые будни товарища Семёна"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_breakfast_s11:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Семён взял ложку."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Потом на его тарелку."
    cs_narrator "Потом снова на него."
    cs_narrator "Он это заметил."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что?"
    cs_ls "Ничего."
    cs_sy "Тогда почему смотришь?"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Думаю, как тебе удалось пережить вчерашний день."
    cs_narrator "Он нахмурился."
    cs_sy "В каком смысле?"
    cs_ls "Ольга Дмитриевна. Поручения. Коробки. Трудовая дисциплина."
    cs_narrator "Он отложил ложку."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А-а. Это."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Она действительно заставила тебя весь вечер работать?"
    cs_sy "Не весь. Просто когда я закончил одно дело, нашлось другое."
    cs_narrator "Я сочувственно покачала головой."
    cs_ls "Классическая система управления персоналом."
    cs_sy "Очень смешно."
    cs_ls "Представляю. Ты приехал неизвестно куда, пытаешься разобраться с происходящим, а тебе выдают коробку и предлагают заняться переноской материальных ценностей."
    cs_sy "Примерно так всё и было."
    cs_narrator "Дарья улыбнулась."
    cs_da "Может, она просто хотела, чтобы ты не сидел без дела?"
    cs_sy "Похоже на то."
    cs_narrator "Я задумчиво кивнула."
    cs_ls "Гениальная методика психологической адаптации. Не понимаешь, где оказался? Неси коробку."
    cs_narrator "Семён невольно усмехнулся."
    cs_sy "Знаешь, как ни странно, немного помогло."
    cs_narrator "Я подняла бровь."
    cs_ls "Правда?"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen serious pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ну да. Пока таскал вещи, хотя бы не думал постоянно об автобусе."
    cs_narrator "Я замолчала."
    cs_th "А ведь он прав."
    cs_narrator "У меня для этого была пробежка."
    cs_narrator "У него — поручения."
    cs_narrator "Разные методы, но результат примерно одинаковый."
    cs_narrator "Когда занимаешься чем-то понятным, мысли перестают бесконечно ходить по одному кругу."
    cs_narrator "Дарья начала завтракать."
    cs_narrator "Я последовала её примеру."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Семён посмотрел на меня."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Кстати, ты сегодня действительно ходила на турники?"
    cs_ls "Угу."
    cs_sy "И сколько подтянулась?"
    cs_narrator "Я назвала результат утреннего подхода."
    cs_narrator "Он одобрительно кивнул."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen smile pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Неплохо."
    cs_ls "Спасибо. Официальная аттестация пройдена?"
    cs_sy "Почти."
    cs_ls "Что значит «почти»?"
    cs_sy "Завтра проверим."
    cs_narrator "Я посмотрела на него."
    cs_ls "О. Добровольно записываешься на физкультурные мероприятия?"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я такого не говорил."
    cs_ls "Поздно. Предложение зарегистрировано."
    cs_narrator "Дарья тихо рассмеялась."
    cs_sy "Не надо ничего регистрировать."
    cs_ls "Тогда утренний норматив остаётся исключительно рекомендательным."
    cs_narrator "Он покачал головой."
    cs_sy "С тобой невозможно нормально разговаривать."
    cs_narrator "Я улыбнулась."
    cs_ls "А ты вчера ещё удивлялся."
    cs_narrator "Но затем всё-таки взялась за ложку."
    cs_th "Ладно."
    cs_th "Человеку тоже необходимо поесть."
    cs_th "Не будем подвергать товарища Семёна дополнительным испытаниям."
    return
