# -*- coding: utf-8 -*-
label cs_day02_12:
    $ save_name = "Чужая смена — День 2: Две Лены за одним столом"
    if not (cs_met_un and cs_friend_un >= 1):
        return
    $ cs_un_name_known = True
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_breakfast_s12:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["un", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "До этого тёзка в основном слушала наш разговор."
    cs_narrator "Теперь она посмотрела на меня и осторожно улыбнулась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_breakfast_un:
    cs_un "Доброе утро, Лена."
    cs_narrator "Я повернулась."
    cs_ls "И тебе доброе."
    cs_narrator "Несколько секунд мы смотрели друг на друга."
    cs_narrator "Я снова поймала себя на мысли, насколько странным оказалось наше знакомство."
    cs_narrator "Похожие волосы."
    cs_narrator "Одинаковый цвет глаз."
    cs_narrator "Одно имя."
    cs_narrator "И совершенно разные привычки."
    cs_narrator "Вчера она с трудом решилась показать мне свой рисунок."
    cs_narrator "А я тем временем успела рассказать половине лагеря совершенно невероятную историю, признаться Даше в симпатии и попытаться организовать разработку зарядки для телефона."
    cs_th "Есть ощущение, что нас воспитывали по разным учебным программам."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["un", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Ты сегодня рано встала?"
    cs_ls "Очень. Даже успела немного побегать."
    cs_narrator "Она удивилась."
    cs_un "До подъёма?"
    cs_ls "Угу."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "А я обычно в это время ещё сплю."
    cs_da "Я тоже."
    cs_narrator "Я посмотрела на них обеих."
    cs_ls "Прекрасно. Чувствую, нахожусь в меньшинстве."
    cs_narrator "Тёзка тихо рассмеялась."
    cs_narrator "Семён, который до этого спокойно завтракал, поднял голову."
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
    cs_sy "Лена, передай хлеб, пожалуйста."
    cs_narrator "Мы обе одновременно повернулись к нему."
    cs_ls "Мне?"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["un", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Мне?"
    cs_narrator "Он замер."
    cs_narrator "Посмотрел на одну."
    cs_narrator "Потом на другую."
    cs_narrator "Дарья опустила взгляд, скрывая улыбку."
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
    cs_sy "Э-э…"
    cs_narrator "Я медленно положила ложку."
    cs_ls "Товарищ Семён, у нас возникла административная проблема."
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
    cs_sy "Какая ещё?"
    cs_ls "Недостаточная точность идентификации адресата."
    cs_narrator "Тёзка прикрыла рот ладонью."
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
    cs_sy "Я просто хлеб попросил!"
    cs_ls "А получил внеочередное заседание комиссии по персональным данным."
    cs_narrator "Дарья не выдержала и засмеялась."
    cs_narrator "Лена Тихонова тоже."
    cs_narrator "Семён устало посмотрел на нас."
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
    cs_sy "Можно тебя Соколовой называть?"
    cs_narrator "Я задумалась."
    cs_ls "Можно."
    cs_narrator "Потом посмотрела на тёзку."
    cs_ls "А тебя?"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["un", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un shy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Наверное, Тихоновой…"
    cs_ls "Прекрасно. Проблема решена."
    cs_narrator "Я передала Семёну хлеб."
    cs_narrator "Он взял его."
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
    show cs_semen smile pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Спасибо, Соколова."
    cs_ls "Всегда пожалуйста, товарищ Семён."
    cs_narrator "Тёзка снова улыбнулась."
    cs_narrator "И мне вдруг стало приятно, что она теперь не пытается спрятать каждую улыбку."
    cs_narrator "Конечно, я знала её совсем недолго."
    cs_narrator "Но вчера мы хотя бы успели поговорить о рисовании."
    cs_narrator "Не о сюжетных ветках."
    cs_narrator "Не о возможных событиях."
    cs_narrator "О карандашах, бумаге и том, как нарисовать ветку, чтобы она не закрывала половину домика."
    cs_th "Хорошая тема."
    cs_th "Пожалуй, стоит к ней возвращаться чаще."
    cs_narrator "Я посмотрела на тёзку."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Кстати, твой вчерашний рисунок мне действительно понравился."
    cs_narrator "Она удивлённо подняла взгляд."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["un", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Правда?"
    cs_ls "Правда. Особенно перспектива."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Я ещё хотела кое-что исправить."
    cs_ls "А что именно?"
    cs_narrator "Она немного оживилась."
    cs_un "Мне кажется, крыша получилась слишком низкой. И ветка почти полностью закрывает окно."
    cs_narrator "Я задумалась."
    cs_ls "Тогда попробуй сначала сделать маленький набросок отдельно. Посмотри, как будет выглядеть композиция."
    cs_narrator "Она кивнула."
    cs_un "Хорошая идея."
    cs_narrator "Семён наблюдал за нашим разговором."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вы обе рисуете?"
    cs_ls "Угу."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    $ cs_breakfast_cast = ["un", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un shy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Немного."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Она скромничает."
    cs_narrator "Тёзка смутилась."
    cs_un "Да нет…"
    cs_ls "Ладно, не буду устраивать художественную экспертизу за завтраком."
    cs_narrator "Дарья улыбнулась."
    cs_da "А я уже думала, что сейчас начнётся."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Между прочим, я умею останавливаться."
    cs_da "Иногда."
    cs_narrator "Мы рассмеялись."
    cs_narrator "Лена Тихонова посмотрела на часы в столовой."
    cs_narrator "Затем на почти пустую тарелку."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Мне скоро надо идти."
    cs_ls "Куда?"
    cs_un "Хотела зайти в библиотеку, а потом на линейку."
    cs_narrator "Я кивнула."
    cs_ls "Тогда не задерживаем."
    cs_narrator "Она взяла поднос."
    cs_narrator "Перед уходом ненадолго остановилась."
    cs_un "Лена…"
    cs_narrator "Я подняла взгляд."
    cs_ls "М?"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Может, потом действительно порисуем?"
    cs_narrator "Я улыбнулась."
    cs_ls "Конечно. Когда будет свободное время."
    cs_narrator "Она кивнула."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_breakfast_cast = []
    show un smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["un", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_un "Хорошо."
    cs_da "Увидимся."
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_breakfast_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Пока."
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
    with Dissolve(0.7)
    $ cs_breakfast_un_here = False
    cs_narrator "Тёзка попрощалась и направилась к выходу."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["un"])
    with cs_sprite_leave
    label cs_director_check_aa1b67bd6c:
    # cs_director_end
    cs_narrator "Я проводила её взглядом."
    cs_th "Забавно."
    cs_th "Ещё вчера она казалась мне знакомым персонажем."
    cs_th "А сегодня сама предложила провести время вместе."
    cs_narrator "И от этого наше знакомство становилось куда интереснее."
    return
