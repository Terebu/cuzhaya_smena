# -*- coding: utf-8 -*-
label cs_day02_37:
    $ save_name = "Чужая смена — День 2: Работа принята"
    $ cs_part04_live = False
    $ cs_part05_live = True
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_part05_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show sl normal pioneer far at cs_actor_far_left zorder 10
    show cs_semen neutral pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/lets_be_friends.ogg":
        play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.18, channel="music", delay=1.0)
    label cs_check_part05_s37:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Возле площади было оживлённо. Несколько пионеров переносили скамейки. Кто-то занимался уборкой. У доски объявлений остановились две девочки, обсуждавшие расписание кружков."
    cs_narrator "Мы подошли ближе. Семён аккуратно приложил наш лист к свободному месту. Славя передала ему кнопки. Он закрепил верхние углы."
    cs_narrator "Затем нижние. Отступил на шаг. Посмотрел."
    cs_sy "Кажется, ровно."
    cs_narrator "Я прищурилась."
    cs_ls "Левый угол чуть ниже."
    cs_narrator "Он повернулся ко мне."
    show cs_semen thinking pioneer far at cs_semen_far_center
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Серьёзно?"
    cs_narrator "Я посмотрела ещё раз."
    cs_ls "Нет. Теперь кажется, что нормально."
    cs_narrator "Он тяжело вздохнул."
    show cs_darya amused pioneer far at cs_darya_far_right
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Не обращай внимания. У неё профессиональная привычка искать недочёты."
    cs_ls "Именно. Если художник не найдёт недостаток в собственной работе, его найдут зрители."
    cs_narrator "Славя отступила рядом со мной. Посмотрела на объявление."
    show sl smile pioneer far at cs_actor_far_left zorder 10
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "По-моему, очень хорошо."
    cs_narrator "Я улыбнулась."
    $ cs_day02_poster_posted = True
    cs_ls "Тогда всё. Готово."
    cs_narrator "Семён убрал оставшиеся кнопки."
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
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part05_viola_arrived:
    # cs_director_begin: Viola and Darya conversation; others remain offscreen
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_6b17943bf8:
    # cs_director_end
    cs_narrator "В этот момент мимо площади проходила Виола. Она заметила нас. Остановилась."
    cs_vi "Уже работаете?"
    cs_narrator "Я обернулась."
    cs_ls "Пытаемся поддерживать культурную жизнь лагеря."
    cs_narrator "Виола посмотрела на объявление."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part05_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Неплохо."
    cs_narrator "Затем перевела взгляд на меня."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part05_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "А руку-то как? Не разболелась?"
    cs_narrator "Я посмотрела на обработанный локоть."
    cs_ls "Пока всё в порядке."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part05_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Тогда хорошо. Только сегодня постарайся обходиться без новых столкновений с мебелью."
    cs_ls "Ничего не обещаю. Местная архитектура настроена ко мне довольно враждебно."
    cs_narrator "Виола усмехнулась."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part05_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Если что, знаешь, где меня искать."
    cs_da "Спасибо, Виола. Надеюсь, больше не понадобится."
    cs_vi "Я тоже надеюсь."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show sl smile pioneer far at cs_actor_far_left zorder 10
    show cs_semen thinking pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part05_viola_left:
    # cs_director_begin: Farewell frame before the actual departure
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_2cc41ac75c:
    # cs_director_end
    cs_narrator "Она попрощалась и продолжила путь."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs"])
    with cs_sprite_leave
    label cs_director_check_58d8c2533e:
    # cs_director_end
    cs_narrator "Я проводила её взглядом."
    cs_th "Удивительно спокойный человек. Ещё сегодня утром она выслушивала мои подозрения насчёт странного плаката. А теперь обсуждает царапину так, будто ничего необычного не произошло."
    cs_narrator "Хотя, возможно, именно так и должен вести себя хороший медицинский работник. Дарья посмотрела на меня. Потом в сторону удалявшейся Виолы. И чуть заметно улыбнулась."
    cs_th "Так. Мне почему-то не нравится это выражение лица."
    # cs_director_begin: Return to the group after Viola leaves
    $ cs_frame_focus(["sl", "cs_semen", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_2ec2b9e143:
    # cs_director_end
    cs_narrator "Семён тем временем собрал оставшиеся материалы."
    cs_sy "Ладно, я отнесу это обратно. Вы пока свободны?"
    cs_narrator "Славя кивнула."
    show sl normal pioneer far at cs_actor_far_left zorder 10
    $ cs_part05_cast = ["sl", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Я помогу. Всё равно мне туда по дороге."
    cs_ls "Тогда спасибо."
    cs_sy "Увидимся."
    cs_da "До встречи."
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part05_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part05_companions_left:
    cs_narrator "Семён и Славя направились в сторону клубов."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_semen", "sl"])
    with cs_sprite_leave
    label cs_director_check_c2919cc19c:
    # cs_director_end
    cs_narrator "Я посмотрела на готовое объявление, затем на Дарью."
    cs_ls "Ну что. Первый официальный заказ в Советском Союзе выполнен."
    cs_narrator "Она усмехнулась."
    cs_da "И даже без оплаты."
    cs_ls "Попрошу не обесценивать. У нас полный пансион."
    cs_da "Очень убедительная система расчётов."
    cs_narrator "Я улыбнулась. И мы направились по дорожке."
    return
