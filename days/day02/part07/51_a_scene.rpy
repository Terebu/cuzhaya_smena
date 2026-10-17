# -*- coding: utf-8 -*-
label cs_day02_51a:
    $ save_name = "Чужая смена — День 2: Не только пациенты"
    $ cs_part06_live = False
    $ cs_part07_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_check_part07_s51a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я уже собиралась встать, но заметила на столе Виолы большую стопку журналов."
    cs_narrator "Рядом лежало несколько заполненных карточек."
    cs_ls "Слушай, Виола, можно вопрос?"
    cs_narrator "Она подняла глаза."
    show cs custom amused medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Если не собираешься снова спрашивать, можно ли тебе бегать, то можно."
    cs_narrator "Я рассмеялась."
    cs_ls "Нет. Пока оставим спорт."
    cs_narrator "Потом кивнула на бумаги."
    cs_ls "У тебя всегда столько работы?"
    cs_narrator "Виола посмотрела на журналы."
    show cs custom explaining medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Зависит от дня. Иногда почти никого нет. А иногда один за другим приходят с ушибами, ссадинами, жалобами на живот."
    cs_narrator "Она улыбнулась."
    show cs custom amused medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Сегодня, например, одна девушка уже успела навестить меня дважды."
    cs_narrator "Я виновато опустила голову."
    cs_ls "Не будем называть имён."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "И хорошо, что приходят. Хуже, когда пытаются терпеть до последнего."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Ты ведь, наверное, не только травмы лечишь. Здесь постоянно кто-нибудь скучает по дому, ссорится или переживает из-за чего-нибудь."
    cs_narrator "Виола немного задумалась."
    cs_vi "Бывает и такое."
    cs_narrator "Она поправила ручку на столе."
    cs_vi "Иногда человеку действительно нужна не таблетка, а чтобы его просто выслушали."
    cs_narrator "Я замолчала."
    cs_narrator "Почему-то её слова запомнились."
    cs_th "Интересно."
    cs_th "Я всё время пытаюсь искать в людях что-нибудь необычное."
    cs_th "А у Виолы, возможно, каждый день проходит через десятки совершенно обычных человеческих неприятностей."
    cs_ls "Наверное, это сложнее, чем кажется со стороны."
    cs_narrator "Она слегка улыбнулась."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Иногда. Но я свою работу люблю."
    cs_narrator "Я кивнула."
    cs_ls "Тогда надеюсь, в следующий раз у нас получится встретиться без необходимости менять мне повязку."
    cs_narrator "Виола усмехнулась."
    cs_vi "Вот это было бы замечательно."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Поддерживаю."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Решение принято единогласно."
    cs_narrator "Виола рассмеялась."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Ладно, идите уже. И береги руку."
    return
