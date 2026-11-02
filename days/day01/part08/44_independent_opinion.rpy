# -*- coding: utf-8 -*-
label cs_day01_44:
    $ save_name = "Чужая смена — День 1: Независимая экспертиза"
    label cs_check_day01_part08_opinion:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_semen"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я села с краю. Дарья осталась рядом."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты ведь не только про телефон поговорить пришла?"
    cs_ls "Почему ты так решил?"
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Слишком довольная."
    cs_ls "Есть один вопрос."
    cs_sy "Ну конечно."
    cs_narrator "Я поправила галстук с серьёзным видом."
    cs_ls "Как считаешь, из меня вышел бы нормальный человек для свидания?"
    pause 0.8
    cs_narrator "Семён повернулся к Дарье. Та старательно прятала улыбку."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что?"
    cs_ls "Вопрос предельно конкретный."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Лена, мы знакомы меньше суток."
    cs_ls "Именно поэтому мне требуется независимая экспертиза."
    cs_narrator "Он закрыл лицо ладонью."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Почему именно я?"
    cs_ls "Ты сидел ближе всех."
    cs_narrator "Дарья рассмеялась. Семён снова посмотрел на меня."
    cs_sy "А тебе самой как кажется?"
    cs_ls "Думаю, у меня имеются определённые недостатки."
    cs_sy "Например?"
    cs_ls "Иногда слишком много говорю."
    cs_da "Иногда?"
    cs_ls "Прошу не вмешиваться в работу независимой комиссии."
    # cs_darya_variety: reaction
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Конечно, товарищ председатель."
    cs_narrator "Семён неожиданно рассмеялся."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вы обе друг друга стоите."
    cs_ls "Вот видишь. Уже есть положительная оценка совместимости."
    show cs_semen awkward_alt pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я вообще не это имел в виду!"
    # cs_darya_variety: reaction
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я тоже не уверена, что это можно считать оценкой."
    cs_ls "Протест отклонён."
    cs_narrator "Семён покачал головой."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Нет, ну вы действительно забавные."
    cs_ls "Спасибо. На этом экспертное заключение принимается."
    cs_narrator "Он посмотрел на нас ещё раз."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Только вы сначала сами разберитесь, что у вас происходит."
    cs_ls "Этим и занимаемся."
    cs_narrator "Мы с Дарьей встретились взглядами."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она улыбнулась, и продолжать шутку расхотелось."
    return
