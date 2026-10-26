# -*- coding: utf-8 -*-
label cs_day03_180:
    $ save_name = "Чужая смена — День 3: Домик, который стал своим"
    $ cs_director_scene("cs_house_lena_darya_int_night")
    scene cs_house_lena_darya_int_night
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    $ night_time()
    $ persistent.sprite_time = "night"
    stop music fadeout 2.0
    cs_narrator "Я закрыла за нами дверь и на секунду задержалась у порога."
    cs_narrator "За спиной остались библиотека и освещённые фонарями дорожки. Передо мной была наша комната."
    cs_narrator "Наша."
    cs_th "Забавно."
    cs_th "Всего три дня назад я и представить не могла, что буду жить в «Совёнке»."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "А сейчас уже мысленно называю этот домик своим."
    cs_th "Ещё немного — и начну возмущаться, если кто-нибудь неправильно поставит обувь у двери."
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она стояла рядом и ждала, пока я уберу руку с дверной ручки."
    cs_narrator "Последние шаги до двери мы прошли молча."
    cs_narrator "И это меня вполне устраивало."
    cs_narrator "После хорошей книги иногда хочется просто подумать."
    cs_narrator "Особенно если книга закончилась так, что вместо облегчения оставила целую коллекцию вопросов."
    cs_th "Вот ведь, Гончаров."
    cs_th "Нельзя было просто написать счастливый конец?"
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Нет, обязательно нужно заставить читателя задуматься о собственной жизни."
    cs_narrator "Я тихо усмехнулась."
    cs_narrator "Дарья повернулась ко мне."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Что?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ничего. Вспомнила книгу."
    cs_narrator "Она улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты теперь весь вечер о ней думать будешь?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Возможно. Но обещаю не пересказывать тебе роман целиком перед сном."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Спасибо."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Хотя могу подготовить краткий доклад."
    cs_narrator "Она рассмеялась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Не надо."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Очень жаль. А я уже придумала название: «Проблемы нравственного взросления на примере гражданина Адуева»."
    cs_narrator "Даша покачала головой."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Тебя нельзя оставлять одну с книгами."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    if cs_mz_open_library_invitation_day3:
        cs_ls "Женя, похоже, придерживается противоположного мнения."
    else:
        cs_ls "Женя, по крайней мере, не запретила мне приходить снова."
    cs_narrator "На столе лежали мой блокнот и карандаши. Рядом — аккуратно сложенные вещи."
    if cs_sl_poster_collected_day3:
        cs_narrator "На столе всё ещё находилась папка с концертным плакатом."
        cs_narrator "Я мельком посмотрела на неё."
        cs_th "Надо же."
        cs_th "Небольшая коллекция сувениров из невозможного путешествия."
    cs_narrator "Дарья поправила ослабленный галстук."
    cs_narrator "Потом отодвинула стул, чтобы можно было пройти к кровати."
    cs_narrator "Затем посмотрела на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ну что, спать?"
    cs_narrator "Я потянулась было вслед за собственным галстуком, но осторожно остановила движение повреждённой руки."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Думаю, да."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Даже без ещё одной главы?"
    cs_narrator "Я вздохнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Гончаров сегодня официально исчерпал свои полномочия."
    cs_narrator "Дарья рассмеялась."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "И надолго?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "До завтрашнего посещения библиотеки. Там, возможно, появится новый литературный подозреваемый."
    cs_narrator "Она улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Я подошла к своей кровати."
    cs_narrator "Села."
    cs_narrator "Огляделась."
    cs_th "Какой всё-таки странный день."
    cs_th "Столько разговоров."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Столько маленьких решений."
    if cs_lena_elbow_bandaged:
        cs_th "И ни одного нового происшествия, после которого пришлось бы бежать к Виоле."
    else:
        cs_th "И ни одного нового происшествия."
    cs_th "Можно считать это личным рекордом."
    return
