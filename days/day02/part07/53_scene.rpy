# -*- coding: utf-8 -*-
label cs_day02_53:
    $ save_name = "Чужая смена — День 2: Необязательное геройство"
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
    # cs_presence_keep: hide cs
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_s53:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы уже подходили к развилке возле площади, когда Даша неожиданно протянула мне руку."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на её ладонь."
    cs_ls "Что?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ничего. Просто иди рядом."
    cs_narrator "Я медленно улыбнулась."
    cs_ls "Это распоряжение?"
    cs_da "Рекомендация."
    cs_ls "Медицинская?"
    cs_da "После сегодняшнего — вполне."
    cs_narrator "Я рассмеялась."
    cs_narrator "Взяла её за руку."
    cs_narrator "И мы продолжили путь."
    cs_narrator "Не особенно быстро."
    cs_narrator "Пионеры проходили мимо по своим делам."
    cs_narrator "Где-то возле площади готовили скамейки для музыкального вечера."
    cs_narrator "Издалека доносились голоса."
    cs_narrator "Лагерь по-прежнему жил своей жизнью."
    cs_narrator "Я подняла перевязанный локоть."
    cs_narrator "Посмотрела на него с некоторым неодобрением."
    cs_ls "Всё-таки надо признать, что сегодняшняя исследовательская экспедиция закончилась не идеально."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Ты обнаружила странность дороги, а потом упала."
    cs_ls "Очень сжатый, но технически точный отчёт."
    cs_narrator "Она улыбнулась."
    cs_da "Зато теперь ты хотя бы будешь смотреть под ноги."
    cs_narrator "Я задумалась."
    cs_ls "Это слишком смелое предположение."
    cs_narrator "Дарья остановилась."
    cs_narrator "Медленно повернула ко мне голову."
    cs_da "Лена."
    cs_narrator "Я тут же подняла здоровую руку."
    cs_ls "Всё. Смотрю."
    cs_narrator "Она покачала головой."
    cs_narrator "Но улыбаться не перестала."
    cs_narrator "Некоторое время мы шли молча."
    cs_narrator "Потом я тихо сказала:"
    cs_ls "Спасибо, что помогла мне."
    cs_narrator "Дарья слегка сжала мою ладонь."
    cs_da "Конечно."
    cs_narrator "Я посмотрела на неё."
    cs_ls "И что не бросила меня лежать на дороге."
    cs_narrator "Она рассмеялась."
    cs_da "Удивительно, что ты вообще предположила такой вариант."
    cs_ls "Я обязана учитывать все возможные исходы."
    cs_da "Тогда учти ещё один."
    cs_narrator "Я повернулась."
    cs_ls "Какой?"
    cs_narrator "Она улыбнулась."
    cs_da "В следующий раз я просто заставлю тебя идти медленнее."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на наши руки."
    cs_narrator "И вдруг поняла, что мне совершенно не хочется никуда спешить."
    cs_th "Странно."
    cs_th "Ещё утром я успела пробежать половину лагеря, прежде чем остальные проснулись."
    cs_th "А теперь не возражаю против самой медленной прогулки за весь день."
    cs_narrator "Возможно, дело было в больном локте."
    cs_narrator "А возможно, не только в нём."
    cs_narrator "Впереди показалась площадь."
    cs_narrator "Мы направились к ней."
    cs_ls "Ладно. Сегодня без новых спортивных достижений."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо."
    cs_ls "И без проверок пространственных аномалий."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ещё лучше."
    cs_narrator "Я ненадолго задумалась."
    cs_ls "А музыкальный вечер хотя бы разрешается?"
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Думаю, да."
    cs_ls "Отлично."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Тогда предлагаю заняться тем, что не требует ни бега, ни медицинского вмешательства."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Например?"
    cs_ls "Найти скамейку и спокойно послушать музыку."
    cs_narrator "Она рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вот теперь мне нравится твой план."
    cs_narrator "Я улыбнулась."
    cs_th "На сегодня приключений действительно хватит."
    cs_th "Дорога оказалась страннее, чем ожидалось."
    cs_th "Локоть — значительно менее прочным."
    cs_th "А Даша…"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Она заметила мой взгляд и слегка улыбнулась."
    cs_th "А Даша продолжала удивлять меня совершенно обычными вещами."
    cs_th "Пожалуй, ради этого не обязательно снова падать."
    stop music fadeout 3.0
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.18, channel="ambience", delay=1.0)
    $ cs_day02_part07_complete = True
    label cs_check_part07_ready:
    pause 0.5
    return
