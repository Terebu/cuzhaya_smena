# -*- coding: utf-8 -*-
label cs_day02_46:
    $ save_name = "Чужая смена — День 2: Записать, пока не забыли"
    $ cs_part05_live = False
    $ cs_part06_live = True
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
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
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/just_think.ogg":
        play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part06_s46:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы возвращались к площади уже без прежнего энтузиазма."
    cs_narrator "Семён время от времени поглядывал назад."
    cs_narrator "Дарья шла рядом со мной."
    # cs_director_begin: REFLECTIVE_SHOT: Writing the actual observations
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_c9c5bc3879:
    # cs_director_end
    # cs_inward_beat_2: attention turns inward
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_narrator "Я достала сложенный листок."
    cs_narrator "Развернула."
    cs_narrator "И начала записывать."
    cs_narrator "«День второй. Проверка дороги»."
    cs_th "Выход за ворота состоялся."
    cs_th "Автобус № 410 отсутствует."
    cs_th "Создана контрольная точка: яркая резинка на кусте, стрелка на земле."
    cs_th "При движении вперёд контрольная точка встретилась повторно."
    cs_th "Повторная проверка дала тот же результат."
    cs_th "При движении назад ворота появились заметно быстрее."
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела на написанное."
    cs_th "Так."
    cs_th "Теперь самое сложное."
    # cs_director_begin: Return to direct interaction: Writing the actual observations
    $ cs_frame_focus(["cs_darya", "cs_semen"])
    with cs_sprite_change
    label cs_director_check_df8261df49:
    # cs_director_end
    cs_narrator "Сделать вывод, который не будет выглядеть как фантазия человека, слишком много игравшего в визуальные новеллы."
    # Return to the same conversation, with the same cast and placement.
    $ cs_pov_end()
    with cs_sprite_change
    cs_ls "Что записать в качестве заключения?"
    cs_narrator "Семён задумался."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что дорога возвращает нас обратно?"
    cs_narrator "Дарья немного покачала головой."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лучше написать, что мы дважды вернулись к одной точке, двигаясь вперёд. Это мы действительно наблюдали."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И кивнула."
    cs_ls "Согласна."
    cs_narrator "Добавила строчку."
    cs_narrator "«Причина повторного появления контрольной точки неизвестна»."
    $ cs_road_notes_written = True
    cs_narrator "Затем сложила лист."
    cs_narrator "Семён посмотрел на меня."
    cs_sy "И что теперь будем делать?"
    cs_narrator "Я задумалась."
    cs_narrator "Вот здесь хотелось немедленно предложить ещё десять проверок."
    cs_narrator "Измерить расстояние."
    cs_narrator "Попробовать пройти дорогу вечером."
    cs_narrator "Привязать несколько меток."
    cs_narrator "Взять с собой часы, компас, бумагу и целую комиссию из кружка электроники."
    cs_narrator "Но чем больше я об этом думала, тем очевиднее становилась одна вещь."
    cs_narrator "Сегодня мы уже достаточно рисковали."
    cs_narrator "И пока не имели даже понятной модели происходящего."
    cs_ls "Пока ничего. Сохраним записи. Потом спокойно обсудим, как проверить результат ещё раз — и стоит ли вообще это делать."
    cs_narrator "Семён кивнул."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Хорошо."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А сейчас?"
    cs_narrator "Я взглянула на площадь."
    cs_narrator "Там кто-то передвигал скамейки."
    cs_narrator "Несколько пионеров обсуждали вечернее выступление."
    cs_narrator "Наше объявление уже висело на доске."
    cs_narrator "Обычная лагерная жизнь продолжалась."
    cs_th "Как будто совершенно ничего не произошло."
    cs_narrator "Я вздохнула."
    cs_ls "А сейчас возвращаемся к программе культурного отдыха."
    cs_narrator "Семён невольно улыбнулся."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "После всего этого?"
    cs_narrator "Я посмотрела на него."
    cs_ls "А что нам остаётся? Ещё полдня ходить кругами по дороге?"
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Думаю, с этим на сегодня хватит."
    cs_narrator "Я кивнула."
    cs_ls "Единогласно."
    cs_narrator "Семён посмотрел на часы."
    cs_sy "Мне нужно отнести кое-что в клубы. Увидимся позже?"
    cs_da "Конечно."
    cs_ls "До вечера."
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
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part06_semen_left:
    cs_narrator "Он попрощался и пошёл своей дорогой."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    label cs_director_check_785ee06518:
    # cs_director_end
    cs_narrator "Я осталась рядом с Дарьей."
    cs_narrator "Она смотрела на меня."
    cs_narrator "И почему-то улыбалась."
    cs_ls "Что?"
    cs_da "Ничего. Просто ты сегодня намного осторожнее, чем вчера."
    cs_narrator "Я задумалась."
    cs_ls "Вчера у меня был ускоренный курс обучения на собственных ошибках."
    cs_narrator "Она рассмеялась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Помогло?"
    cs_ls "Частично. Полную версию программы обещают установить позднее."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_narrator "А потом ненадолго замолчала."
    if renpy.music.get_playing() != "sound/music/a_promise_from_distant_days.ogg":
        play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тебе страшно?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Вспомнила дорогу."
    cs_narrator "Яркую резинку."
    cs_narrator "Семёна, который несколько секунд просто стоял и смотрел на знакомый куст."
    cs_narrator "И вывеску «Совёнок», внезапно появившуюся между деревьями."
    cs_ls "Да."
    cs_narrator "Дарья кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне тоже."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Немного помолчала."
    cs_ls "Но сегодня хотя бы стало понятно, что мы не зря задаём вопросы."
    cs_da "И что торопиться с ответами не стоит."
    cs_narrator "Я улыбнулась."
    cs_ls "Именно."
    cs_narrator "Мы продолжили идти."
    cs_narrator "Некоторое время молчали."
    cs_narrator "Потом я не удержалась."
    cs_ls "Хотя у нашей ситуации всё-таки есть одно преимущество."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Какое?"
    cs_narrator "Я пожала плечами."
    cs_ls "Пока мы здесь, у меня есть немного больше времени тебя узнавать."
    cs_narrator "Она замедлила шаг."
    cs_narrator "Посмотрела на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты можешь делать это и без пространственных загадок."
    cs_narrator "Я задумалась."
    cs_narrator "Потом улыбнулась."
    cs_ls "Справедливо."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И желательно без предварительного научного заключения."
    cs_ls "Тогда моя исследовательская карьера находится под угрозой."
    cs_da "Переживёшь."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И вдруг поняла, что она снова меня переиграла."
    cs_th "Ну замечательно."
    cs_th "Дорога не выпускает."
    cs_th "Даша научилась отвечать моими же шутками."
    cs_th "Второй день становится всё интереснее."
    cs_narrator "Но на этот раз я ничего не сказала вслух."
    cs_narrator "Просто пошла рядом."
    cs_narrator "Впереди виднелась площадь."
    cs_narrator "И люди, которые собирались провести совершенно обычный музыкальный вечер."
    cs_th "Пусть."
    cs_th "На сегодня загадок достаточно."
    stop music fadeout 3.0
    $ cs_day02_part06_complete = True
    label cs_check_part06_ready:
    pause 0.5
    return
