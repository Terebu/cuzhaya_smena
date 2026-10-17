# -*- coding: utf-8 -*-
label cs_day02_44:
    $ save_name = "Чужая смена — День 2: Повторный опыт"
    $ cs_part05_live = False
    $ cs_part06_live = True
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
    show cs_semen neutral pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/waltz_of_doubts.ogg":
        play music "sound/music/waltz_of_doubts.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.12, channel="music", delay=1.0)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/forest_day.ogg":
        play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.1, channel="ambience", delay=1.0)
    label cs_check_part06_s44:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы решили провести ещё одну проверку."
    cs_narrator "На этот раз договорились заранее."
    cs_narrator "Никто не сходит с асфальта."
    cs_narrator "Не делает ненужных поворотов."
    cs_narrator "Не отвлекается надолго на лес."
    cs_narrator "Семён следит за временем."
    cs_narrator "Дарья запоминает заметные особенности дороги."
    cs_narrator "Я отмечаю всё, что кажется необычным."
    cs_narrator "Прежде чем отправиться, я ещё раз посмотрела на куст."
    cs_narrator "Поправила резинку так, чтобы её было хорошо видно."
    cs_narrator "Дарья сделала рядом со старой стрелкой вторую короткую отметку."
    show cs_darya surprised pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Теперь хотя бы будем уверены, что это действительно наше место."
    show cs_semen thinking pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Идём?"
    cs_narrator "Я кивнула."
    cs_ls "Идём."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_powerlines_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap2_a")
    label cs_check_part06_lap2_a:
    cs_narrator "Мы снова пошли вперёд."
    cs_narrator "Прошло несколько минут."
    cs_narrator "Потом ещё несколько."
    cs_narrator "Я старалась не смотреть на каждый куст так, будто он собирался внезапно переместиться."
    cs_narrator "Получалось плохо."
    cs_th "Ну же."
    cs_th "Обычная дорога."
    cs_th "Обычный лес."
    cs_th "Ничего сверхъестественного."
    cs_narrator "Но теперь даже птицы казались подозрительно громкими."
    cs_narrator "Семён время от времени сообщал, сколько прошло времени."
    cs_narrator "Дарья внимательно следила за обочиной."
    cs_narrator "Я смотрела то вперёд, то на землю под ногами."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_left_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap2_b")
    label cs_check_part06_lap2_b:
    cs_narrator "На одном участке дорога слегка изгибалась влево."
    cs_narrator "Мы прошли его."
    cs_narrator "Потом длинный прямой отрезок."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_right_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap2_c")
    label cs_check_part06_lap2_c:
    cs_narrator "Небольшая неровность асфальта."
    cs_narrator "Ещё несколько деревьев."
    cs_narrator "И…"
    show cs_darya shrug pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена."
    cs_narrator "Я подняла голову."
    cs_narrator "Она не смотрела на меня."
    cs_narrator "Смотрела вперёд."
    cs_narrator "Я перевела взгляд туда же."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_marked_verge_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("lap2_return")
    label cs_check_part06_lap2_return:
    $ cs_road_loop_observations = 2
    pause 1.0
    cs_narrator "Яркая резинка."
    cs_narrator "Тот же куст."
    cs_narrator "У края дороги — две отметки."
    cs_narrator "Я остановилась."
    cs_narrator "Семён медленно выдохнул."
    show cs_semen serious pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Мы опять пришли сюда."
    cs_narrator "Я несколько секунд молчала."
    cs_narrator "Потом подошла к обочине."
    cs_narrator "Присела."
    cs_narrator "Проверила вторую отметку."
    cs_narrator "Она была на месте."
    cs_ls "Да."
    cs_da "И мы ни разу не разворачивались."
    cs_sy "Ни разу."
    cs_narrator "Я выпрямилась."
    cs_narrator "Посмотрела на дорогу."
    cs_narrator "С виду она ничем не отличалась от самой обычной лесной трассы."
    cs_narrator "Но теперь у нас было два последовательных наблюдения."
    cs_narrator "Мы шли в одном направлении."
    cs_narrator "Без намеренного возвращения."
    cs_narrator "И дважды оказывались у одной и той же контрольной точки."
    cs_th "Вот теперь стало по-настоящему неуютно."
    cs_narrator "Семён потёр затылок."
    show cs_semen thinking pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Значит, дорога идёт кругом?"
    cs_narrator "Я задумалась."
    cs_ls "Возможно. Только по ощущениям мы не сделали полного круга."
    show cs_darya thinking pioneer far at cs_darya_far_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Может быть, здесь какая-то особенность местности. Или мы неправильно оцениваем направление."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Может."
    cs_narrator "Пауза."
    cs_ls "Но в обычной местности я всё-таки ожидала бы увидеть хоть один поворот, после которого можно понять, что возвращаешься назад."
    cs_narrator "Семён посмотрел в сторону лагеря."
    cs_sy "А если мы попробуем пойти обратно?"
    cs_narrator "Мы переглянулись."
    cs_narrator "Я кивнула."
    cs_ls "Думаю, на сегодня хватит движения вперёд."
    cs_narrator "Дарья согласилась."
    cs_narrator "Мы развернулись."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_right_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("back_c")
    label cs_check_part06_back_c:
    cs_narrator "И пошли в противоположную сторону."
    cs_narrator "Я следила за дорогой почти болезненно внимательно."
    cs_narrator "Снова деревья."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_left_bend_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("back_b")
    label cs_check_part06_back_b:
    cs_narrator "Снова асфальт."
    cs_narrator "Снова одинаковая трава по обочинам."
    cs_narrator "Но теперь прошло заметно меньше времени."
    hide cs_road_powerlines_day
    hide cs_road_right_bend_day
    hide cs_road_marked_verge_day
    hide cs_road_left_bend_day
    show cs_road_powerlines_day behind cs_darya, cs_semen
    with Dissolve(0.8)
    $ cs_road_visual_trace.append("back_a")
    label cs_check_part06_back_a:
    cs_narrator "Дорога сделала небольшой изгиб."
    cs_narrator "Впереди посветлело."
    $ cs_director_scene("bg ext_no_bus")
    scene bg ext_no_bus
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
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_part06_gate_return:
    cs_narrator "И между деревьями показалась знакомая вывеска."
    cs_narrator "«СОВЁНОК»."
    cs_narrator "Я остановилась."
    cs_ls "Вот теперь действительно интересно."
    cs_narrator "Семён посмотрел на часы."
    cs_sy "Назад мы шли намного меньше."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да."
    cs_narrator "Я взглянула на ворота."
    cs_narrator "Они были совершенно обычными."
    cs_narrator "Такими же, какими я видела их утром."
    cs_narrator "Но теперь смотреть на них было гораздо неприятнее."
    cs_th "Получается, уйти можно."
    cs_th "По крайней мере, на какое-то расстояние."
    cs_th "А вот куда именно ведёт дорога, мы так и не выяснили."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Потом на Дарью."
    cs_ls "У нас есть наблюдение, которое пока не укладывается в обычную схему."
    cs_sy "Это ты ещё мягко сказала."
    cs_narrator "Я невесело усмехнулась."
    cs_ls "Если начну формулировать жёстче, боюсь, нам всем станет ещё хуже."
    cs_narrator "Дарья посмотрела на вывеску."
    cs_da "Я бы сначала вернулась в лагерь. А уже там записала всё, пока мы не забыли детали."
    cs_narrator "Я кивнула."
    cs_ls "Согласна."
    cs_narrator "Мы направились к воротам."
    cs_th "На этот раз я даже не пыталась шутить."
    return
