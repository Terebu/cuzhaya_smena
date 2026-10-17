# -*- coding: utf-8 -*-
# Source: source/day01_part05.md.
label cs_day01_21:
    $ save_name = "Чужая смена — День 1: Не самый простой вопрос"
    window show dissolve
    label cs_check_day01_part05_start:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_semen", "mt"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Семён не ответил сразу."
    cs_narrator "Его взгляд скользнул за моё плечо, будто там всё ещё мог стоять автобус."
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты его видела?"
    cs_ls "Да. Мы с Дарьей на нём приехали."
    cs_narrator "Он посмотрел на неё."
    cs_narrator "Дарья кивнула."
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Сегодня утром. Хотя сели в него совсем в другом месте."
    cs_narrator "Семён медленно выдохнул."
    cs_sy "В каком?"
    cs_narrator "Я заметила, как Ольга Дмитриевна обернулась на оклик из другого конца столовой."
    show mt normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Семён, покажи девочкам, где взять обед. Я сейчас подойду."
    # cs_presence_keep: hide mt
    # cs_composition: regroup
    show cs_darya shrug pioneer far at cs_darya_far_left
    show cs_semen tie_touch pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она направилась к столу у окна."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["mt"])
    with cs_sprite_leave
    label cs_director_check_2b08382bad:
    # cs_director_end
    cs_narrator "Семён проводил её взглядом и заговорил тише."
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вы тоже ничего не понимаете?"
    cs_ls "Понимаю достаточно, чтобы задавать вопросы. Недостаточно, чтобы на них отвечать."
    cs_narrator "Он чуть нахмурился."
    show cs_darya explaining pioneer far at cs_darya_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы из Москвы. Я ехала по своим делам, Лена собиралась за продуктами. Встретились уже в автобусе."
    cs_sy "Зимой?"
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да."
    cs_narrator "Вокруг продолжали звенеть ложки."
    cs_narrator "Кто-то позади нас попросил передать хлеб."
    cs_narrator "Обычный обед. Почти нелепая обстановка для такого разговора."
    cs_sy "А какой у вас был год?"
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya shy_bend pioneer far at cs_darya_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она не отвела взгляда."
    stop music fadeout 1.5
    label cs_check_day01_part05_2026:
    cs_ls "Две тысячи двадцать шестой."
    cs_narrator "Семён замер."
    cs_narrator "На этот раз он смотрел не на мои волосы и не на пионерскую форму."
    cs_narrator "Прямо в лицо."
    cs_sy "Вы серьёзно?"
    cs_da "Да. Обе."
    show cs_semen awkward_alt pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "У меня дома был другой год."
    cs_narrator "Я медленно кивнула."
    cs_ls "Значит, не обязательно одинаковая дата отправления. Это уже полезно."
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Полезно?"
    cs_ls "Лучше знать, чем предполагать."
    cs_narrator "Он несколько секунд молчал."
    cs_narrator "Потом словно вспомнил про поручение вожатой."
    show cs_semen tie_touch pioneer far at cs_semen_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Давайте сначала возьмём еду. А то здесь неудобно стоять."
    cs_narrator "На удивление, спорить не хотелось."
    cs_narrator "Мы взяли подносы и прошли вдоль раздачи."
    cs_narrator "Я старалась не разглядывать каждого человека, который попадался навстречу."
    cs_narrator "Получалось плохо."
    cs_narrator "Семён выбрал стол чуть в стороне от шумной компании."
    cs_narrator "Дарья села рядом со мной."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_right
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    with None
    cs_narrator "Он — напротив."
    cs_th "Три человека с одним и тем же вопросом."
    cs_th "Для начала уже неплохо."
    return
