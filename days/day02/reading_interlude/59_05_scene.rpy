# -*- coding: utf-8 -*-
label cs_day02_reading_05:
    $ save_name = "Чужая смена — Тишина на троих: Вторая читательница"
    $ cs_part08_live = False
    $ cs_reading_live = True
    # cs_presence_keep: hide cs_darya
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
    $ cs_reading_cast = []
    label cs_check_reading_05:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я прочитала ещё несколько страниц."
    cs_narrator "Потом остановилась на довольно длинном абзаце."
    cs_narrator "Перечитала его."
    cs_narrator "И неожиданно поняла, что уже некоторое время ни о чём другом не думаю."
    cs_narrator "Не о доме."
    cs_narrator "Не о загадочной дороге."
    cs_narrator "Не об автобусе."
    cs_narrator "Даже не о том, что после вчерашнего признания отношения с Дарьей оставались неопределёнными."
    cs_th "Надо же."
    cs_th "Оказывается, мой мозг способен заниматься чем-то одним."
    cs_th "Без попытки одновременно решить все проблемы мироздания."
    cs_narrator "Я перевернула страницу."
    cs_narrator "И в этот момент снова открылась дверь."
    cs_narrator "Послышались шаги."
    cs_narrator "Знакомые."
    cs_narrator "Я подняла голову."
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
    label cs_check_reading_darya_returned:
    cs_narrator "На пороге стояла Дарья."
    cs_narrator "Она огляделась."
    cs_narrator "Увидела Женю за рабочим столом."
    cs_narrator "Затем меня."
    cs_narrator "И остановилась."
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
    cs_da "Лена?"
    cs_narrator "Я подняла взгляд."
    cs_ls "Я здесь."
    cs_narrator "Даша подошла ближе."
    cs_narrator "Посмотрела на книгу передо мной."
    cs_narrator "Потом на меня."
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
    cs_da "Ты действительно читаешь."
    cs_narrator "Я немного удивилась."
    cs_ls "А что должна была делать?"
    cs_narrator "Она улыбнулась."
    cs_da "Не знаю. После сегодняшнего дня я ожидала хотя бы небольшого расследования."
    cs_narrator "Я покачала головой."
    cs_ls "Сегодня уже хватит."
    cs_narrator "Она села на соседний стул."
    cs_narrator "Заметила, как я устроила повреждённую руку."
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
    cs_da "Локоть не болит?"
    cs_ls "Если не двигать лишний раз, почти нет."
    cs_narrator "Она кивнула."
    cs_narrator "Потом посмотрела на книгу."
    cs_da "Интересная?"
    cs_ls "Пока да."
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
    cs_da "Тогда не буду мешать."
    cs_narrator "Я немного подвинулась, освобождая ей место у края стола."
    cs_ls "Можешь тоже что-нибудь взять."
    cs_narrator "Она посмотрела на стеллажи."
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
    cs_da "А здесь можно просто выбрать книгу?"
    cs_narrator "Я кивнула в сторону Жени."
    cs_ls "Лучше спросить."
    # cs_presence_keep: hide cs_darya
    $ cs_reading_cast = []
    # cs_director_begin: Reader viewpoint while Darya goes to the distant desk
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_1c69659476:
    # cs_director_end
    cs_narrator "Даша подошла к библиотекарше."
    cs_narrator "Я слышала их негромкий разговор."
    cs_narrator "Женя объяснила, с каких полок можно брать книги для чтения в зале и что нужно сделать, если захочется унести книгу с собой."
    cs_narrator "Дарья поблагодарила её."
    cs_narrator "Затем выбрала небольшой том."
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
    cs_narrator "Вернулась ко мне."
    cs_narrator "Устроилась рядом."
    cs_narrator "И открыла первую страницу."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она — на меня."
    cs_da "Что?"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Ничего."
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
    cs_da "Подозрительно."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Вот видишь, уже переняла мои привычки."
    cs_narrator "Она улыбнулась."
    cs_narrator "И вернулась к чтению."
    cs_th "Вот так."
    cs_th "Две девушки, которые ещё недавно ехали в одном автобусе сквозь зимнюю Москву."
    cs_th "Теперь сидят рядом в советской библиотеке."
    cs_th "И читают книги."
    cs_th "Без попытки немедленно понять, почему оказались здесь."
    cs_narrator "Невероятно обыкновенное занятие."
    cs_narrator "Но сейчас именно этого мне и хотелось."
    return
