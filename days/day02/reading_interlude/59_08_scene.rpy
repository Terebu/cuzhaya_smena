# -*- coding: utf-8 -*-
label cs_day02_reading_08:
    $ save_name = "Чужая смена — Тишина на троих: Соколова записывается в библиотеку"
    $ cs_part08_live = False
    $ cs_reading_live = True
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_08:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда я в следующий раз подняла голову, за окнами заметно изменился свет."
    cs_narrator "Солнце клонилось ниже."
    cs_narrator "Пылинки в воздухе теперь казались почти золотыми."
    cs_narrator "Я посмотрела на страницу."
    cs_narrator "Затем на часы."
    cs_th "Надо же."
    cs_th "Время действительно прошло незаметно."
    cs_narrator "Дарья тоже закрыла книгу."
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Кажется, скоро ужин."
    cs_narrator "Я кивнула."
    cs_ls "Похоже на то."
    cs_narrator "Она посмотрела на мою книгу."
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Дочитала?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Но осталось совсем немного."
    cs_narrator "Потом посмотрела в сторону Жени."
    cs_th "Надо будет спросить, можно ли взять с собой."
    cs_narrator "Я аккуратно вложила закладку между страницами."
    cs_narrator "Поднялась."
    cs_narrator "Взяла книгу здоровой рукой."
    cs_narrator "Дарья тоже встала, вернула свой том на место, предварительно уточнив у Жени нужную полку."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_checkout:
    cs_narrator "Я подошла к столу библиотекарши."
    cs_ls "Женя, можно мне эту книгу взять до завтра?"
    cs_narrator "Она посмотрела на обложку."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Дочитать хочешь?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_narrator "Она достала журнал выдачи."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда запишем."
    cs_narrator "Я подошла ближе."
    cs_narrator "Она открыла нужную страницу."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Фамилия, имя. И какой у тебя домик?"
    cs_narrator "Я назвала данные."
    cs_narrator "Женя внесла их в журнал."
    $ cs_reading_book_borrowed = True
    $ cs_reading_book_location = "lena_hand"
    label cs_check_reading_borrowed:
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только постарайся не испачкать книгу."
    cs_narrator "Я кивнула."
    cs_ls "Конечно."
    cs_narrator "Она посмотрела на мой локоть."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И не урони её по дороге."
    cs_narrator "Я немного помолчала."
    cs_narrator "Затем усмехнулась."
    cs_ls "Очень своевременное уточнение."
    cs_narrator "Дарья тихо рассмеялась."
    if cs_friend_mz == 0:
        cs_narrator "Женя закрыла журнал."
        cs_mz "Всё. Вернёшь, когда дочитаешь."
        cs_ls "Хорошо. Спасибо."
        cs_mz "Не за что."
        cs_narrator "Она вернулась к бумагам."
        cs_narrator "Я поправила книгу в руке."
        cs_th "Обычная выдача."
        cs_th "Обычные правила."
        cs_th "И нормальное отношение, даже несмотря на наше вчерашнее знакомство."
        cs_th "Пожалуй, вполне неплохо."
    elif cs_friend_mz == 1:
        cs_narrator "Женя закрыла журнал."
        cs_mz "Когда дочитаешь, скажешь, что думаешь о концовке."
        cs_narrator "Я улыбнулась."
        cs_ls "Договорились."
        cs_mz "Только не рассказывай её всем остальным."
        cs_ls "Никаких преждевременных разглашений."
        cs_narrator "Она покачала головой."
        cs_narrator "Но улыбнулась."
    else:
        cs_narrator "Женя посмотрела на книгу."
        cs_narrator "Затем на меня."
        cs_mz "Можешь вернуть завтра. Если захочешь, обсудим, когда дочитаешь."
        cs_narrator "Я улыбнулась."
        cs_ls "С удовольствием."
        cs_narrator "Она кивнула."
        cs_mz "Только не вздумай специально читать всю ночь ради этого."
        cs_narrator "Я рассмеялась."
        cs_ls "Обещать не буду."
        cs_narrator "Женя посмотрела на Дарью."
        cs_mz "Проследи хотя бы ты, чтобы она не сидела до утра."
        cs_narrator "Дарья улыбнулась."
        # cs_presence_keep: hide cs_semen
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
        # cs_presence_keep: hide cs_dasha_winter
        # cs_presence_keep: hide cs_dasha_pioneer
        show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
        show cs_darya shrug pioneer normal at cs_darya_normal_right
        $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_da "Попробую."
        cs_narrator "Я посмотрела на них обеих."
        cs_ls "Какие прекрасные перспективы. Уже двое контролируют мой режим дня."
        cs_narrator "Женя усмехнулась."
        cs_mz "Кто-то же должен."
    cs_narrator "Я взяла книгу."
    cs_narrator "Посмотрела на Женю."
    cs_narrator "И неожиданно для себя произнесла:"
    cs_ls "Спасибо."
    cs_narrator "Она подняла взгляд."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "За книгу?"
    cs_narrator "Я немного подумала."
    cs_ls "И за неё тоже."
    cs_narrator "Потом оглядела библиотеку."
    cs_ls "Просто здесь хорошо."
    cs_narrator "Женя проследила за моим взглядом."
    cs_narrator "Посмотрела на шкафы."
    cs_narrator "На столы."
    cs_narrator "На свет, падавший из окон."
    cs_narrator "И чуть заметно улыбнулась."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Да. Здесь тихо."
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "Затем Дарья подошла к двери."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен, пойдём? А то скоро все в столовую побегут."
    cs_narrator "Я кивнула."
    cs_ls "Иду."
    cs_narrator "Повернулась к Жене."
    cs_ls "До завтра."
    if cs_friend_mz >= 1:
        cs_mz "До завтра."
    else:
        cs_mz "До встречи."
    cs_narrator "Мы направились к выходу."
    return
