# -*- coding: utf-8 -*-
label cs_day01_44:
    $ save_name = "Чужая смена — День 1: Независимая экспертиза"
    label cs_check_day01_part08_opinion:
    cs_narrator "Я села на свободный край скамейки."
    cs_narrator "Дарья осталась рядом."
    cs_narrator "Семён посмотрел на меня."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    cs_sy "Ты ведь не только про телефон поговорить пришла?"
    cs_ls "Почему ты так решил?"
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    cs_sy "Слишком довольная."
    cs_narrator "Я невольно улыбнулась."
    cs_ls "Есть один вопрос."
    cs_sy "Ну конечно."
    cs_narrator "Я поправила галстук."
    cs_narrator "Сделала совершенно серьёзное лицо."
    cs_ls "Как считаешь, из меня вышел бы нормальный человек для свидания?"
    pause 0.8
    cs_narrator "Семён несколько секунд молчал."
    cs_narrator "Потом медленно повернулся к Дарье."
    cs_narrator "Та отвела взгляд, стараясь не рассмеяться."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    cs_sy "Что?"
    cs_ls "Вопрос предельно конкретный."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    cs_sy "Лена, мы знакомы меньше суток."
    cs_ls "Именно поэтому мне требуется независимая экспертиза."
    cs_narrator "Он закрыл лицо ладонью."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    cs_sy "Почему именно я?"
    cs_ls "Ты сидел ближе всех."
    cs_narrator "Дарья не выдержала и рассмеялась."
    cs_narrator "Семён посмотрел на неё."
    cs_narrator "Потом снова на меня."
    cs_sy "А тебе самой как кажется?"
    cs_narrator "Я задумалась."
    cs_ls "Думаю, у меня имеются определённые недостатки."
    cs_sy "Например?"
    cs_ls "Иногда слишком много говорю."
    cs_da "Иногда?"
    cs_narrator "Я повернулась к ней."
    cs_ls "Прошу не вмешиваться в работу независимой комиссии."
    # cs_darya_variety: reaction
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_right
    cs_da "Конечно, товарищ председатель."
    cs_narrator "Семён неожиданно рассмеялся."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    cs_sy "Вы обе друг друга стоите."
    cs_narrator "Я медленно повернулась к Дарье."
    cs_narrator "Потом обратно к Семёну."
    cs_ls "Вот видишь. Уже есть положительная оценка совместимости."
    show cs_semen awkward_alt pioneer normal at cs_semen_normal_left
    cs_sy "Я вообще не это имел в виду!"
    # cs_darya_variety: reaction
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    cs_da "Я тоже не уверена, что это можно считать оценкой."
    cs_ls "Протест отклонён."
    cs_narrator "Семён покачал головой."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    cs_sy "Нет, ну вы действительно забавные."
    cs_narrator "Я усмехнулась."
    cs_ls "Спасибо. На этом экспертное заключение принимается."
    cs_narrator "Он посмотрел на нас ещё раз."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    cs_sy "Только вы сначала сами разберитесь, что у вас происходит."
    cs_narrator "Я коротко кивнула."
    cs_ls "Этим и занимаемся."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "На секунду наши взгляды встретились."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    cs_narrator "Она слегка улыбнулась."
    cs_narrator "И почему-то мне совершенно не захотелось продолжать шутку."
    return
