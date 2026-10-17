# -*- coding: utf-8 -*-
label cs_day02_55:
    $ save_name = "Чужая смена — День 2: Угадай кто"
    $ cs_part07_live = False
    $ cs_part08_live = True
    # cs_presence_keep: hide cs_darya
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
    # cs_presence_keep: hide cs
    $ cs_part08_cast = []
    label cs_check_part08_s55:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я подошла к Семёну со спины."
    cs_narrator "Осторожно."
    cs_narrator "Не особенно быстро."
    cs_narrator "После сегодняшнего знакомства с корнем дерева любые резкие движения казались подозрительным предложением со стороны мироздания."
    cs_narrator "Семён меня не замечал."
    cs_narrator "Он действительно рассматривал карандаш."
    cs_narrator "Крутил его между пальцами, потом останавливался, разглядывал стёртый кончик и снова начинал вращать."
    cs_th "Интересно."
    cs_th "О чём человек думает после знакомства с пространственной петлёй?"
    cs_th "Возможно, о фундаментальной природе мироздания."
    cs_th "Возможно, о том, что скоро ужин."
    cs_th "А возможно, просто о карандаше."
    cs_narrator "Я приблизилась ещё на шаг."
    cs_narrator "Потом наклонилась."
    $ cs_director_scene("cs_cg_lena_semen_guess_who_day")
    scene cs_cg_lena_semen_guess_who_day
    # cs_presence_keep: hide cs_darya
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
    # cs_presence_keep: hide cs
    $ cs_part08_cast = []
    with Dissolve(0.8)
    $ cs_part08_cg = True
    label cs_check_part08_guess_cg:
    cs_narrator "Осторожно прикрыла ему глаза ладонью здоровой руки."
    cs_narrator "И самым низким голосом, на который была способна, произнесла:"
    cs_ls "Угадай кто."
    cs_narrator "Семён замер."
    cs_narrator "Совершенно."
    cs_narrator "На несколько секунд."
    cs_narrator "Затем тяжело вздохнул."
    cs_sy "Соколова."
    cs_narrator "Я убрала руку."
    cs_ls "Ну вот."
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_winter
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    $ cs_part08_cg = False
    label cs_check_part08_turned:
    cs_narrator "Он повернулся."
    cs_narrator "Посмотрел на меня."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что «ну вот»?"
    cs_ls "Даже не попытался подумать."
    cs_sy "А зачем?"
    cs_narrator "Я развела руками."
    cs_narrator "Точнее, одной рукой."
    cs_narrator "Вторая после медпункта требовала максимально бережного отношения."
    cs_ls "Ради атмосферы. Ради интриги. Ради элементарного уважения к творческому замыслу."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он усмехнулся."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты действительно думаешь, что здесь есть ещё кто-нибудь, кто подкрадётся ко мне и начнёт разговаривать таким голосом?"
    cs_narrator "Я задумалась."
    cs_ls "Ульяна?"
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Она бы уже засмеялась."
    cs_ls "Алиса?"
    cs_sy "Она бы придумала что-нибудь посерьёзнее."
    cs_ls "Женя?"
    cs_narrator "Он посмотрел на меня."
    cs_narrator "Затем на ближайшую дорожку."
    cs_sy "Женя, наверное, сначала спросила бы, почему я сижу без дела."
    cs_narrator "Я рассмеялась."
    cs_ls "А ведь верно."
    cs_sy "Так что вариантов у меня было немного."
    cs_narrator "Я сложила руки на груди."
    cs_narrator "Тут же вспомнила о локте."
    cs_narrator "Поморщилась."
    cs_narrator "Опустила повреждённую руку."
    cs_narrator "Семён заметил."
    show cs_semen serious pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Кстати, а что у тебя с рукой?"
    cs_narrator "Я подняла её."
    cs_narrator "Продемонстрировала повязку."
    cs_ls "Последствия боевого столкновения."
    cs_narrator "Он нахмурился."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "С кем?"
    cs_ls "С корнем дерева."
    cs_narrator "Пауза."
    cs_narrator "Семён посмотрел на руку."
    cs_narrator "Потом на меня."
    cs_sy "Ты споткнулась?"
    cs_narrator "Я вздохнула."
    cs_ls "Как же быстро распространяется эта враждебная формулировка."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он начал смеяться."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Подожди. Ты утром бегала, подтягивалась, потом ходила с нами по лесной дороге…"
    cs_ls "И что?"
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А после всего этого просто споткнулась о корень?"
    cs_narrator "Я кивнула."
    cs_ls "Именно. Главный противник оказался значительно ниже ожидаемого."
    cs_narrator "Он рассмеялся ещё сильнее."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Совершенно серьёзно."
    cs_ls "Товарищ Семён, раненым положено сочувствие."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Прости."
    cs_narrator "Он попытался перестать смеяться."
    cs_narrator "Не получилось."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Просто представил."
    cs_narrator "Я покачала головой."
    cs_ls "Ужасно. Два дня знакомства, а уважение уже потеряно."
    # cs_presence_keep: hide cs_dasha_winter
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part08_darya_returns:
    cs_narrator "В этот момент подошла Дарья."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "По-моему, ты сама слишком подробно всё описываешь."
    cs_narrator "Я повернулась к ней."
    cs_ls "Я рассчитывала на поддержку."
    cs_da "Я тебя поддерживала всю дорогу до медпункта."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "И что Виола сказала?"
    cs_narrator "Дарья ответила первой."
    cs_da "Что сегодня лучше обойтись без тренировок и не трогать повязку."
    cs_narrator "Я кивнула."
    cs_ls "Спортивная деятельность временно приостановлена решением медицинской комиссии."
    cs_narrator "Семён усмехнулся."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ну хоть сегодня посидишь спокойно."
    cs_narrator "Я посмотрела на лавочку."
    cs_narrator "Потом на него."
    cs_ls "Собственно, этим и собираюсь заняться."
    cs_narrator "Села рядом."
    cs_narrator "Осторожно устроила повреждённую руку так, чтобы не задевать повязку."
    # cs_presence_keep: hide cs_dasha_winter
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part08_seated:
    cs_narrator "Дарья заняла свободное место."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "А потом Семён вдруг произнёс:"
    cs_sy "Слушай, а ведь ты утром сама предлагала мне соревнование на турниках."
    cs_narrator "Я медленно повернулась."
    cs_ls "И?"
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Получается, я победил без участия?"
    cs_narrator "Я прищурилась."
    cs_ls "Не спеши радоваться. Соревнование перенесено по медицинским показаниям."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он рассмеялся."
    cs_sy "Буду ждать."
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она улыбалась."
    cs_th "Прекрасно."
    cs_th "Кажется, теперь уже двое освоили искусство отвечать мне моими же шутками."
    cs_th "Скоро придётся организовывать курсы повышения квалификации."
    return
