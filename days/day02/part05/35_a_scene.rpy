# -*- coding: utf-8 -*-
label cs_day02_35a:
    $ save_name = "Чужая смена — День 2: Совместное производство"
    $ cs_part04_live = False
    $ cs_part05_live = True
    if not renpy.showing("cs_cg_poster_planning_day"):
        $ cs_director_scene("cs_cg_poster_planning_day")
        scene cs_cg_poster_planning_day
    $ cs_part05_cg = True
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
    $ cs_part05_cast = []
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    if renpy.music.get_playing() is None:
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    label cs_check_part05_s35a:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я положила карандаш."
    cs_narrator "Повернулась к Семёну."
    cs_ls "Давай вместе сделаем."
    cs_narrator "Он приподнял бровь."
    cs_sy "Ты мне доверяешь заголовок?"
    cs_ls "Настолько, что собираюсь лично участвовать в процессе."
    cs_sy "Очень утешает."
    cs_narrator "Я рассмеялась."
    cs_narrator "Мы придвинули лист ближе к середине стола."
    cs_narrator "Дарья поставила отметки для верхней и нижней границ букв."
    cs_narrator "Семён осторожно начал писать."
    cs_narrator "Первую букву он сделал довольно ровно."
    cs_narrator "Вторая получилась чуть шире."
    cs_narrator "На третьей он остановился."
    cs_sy "Так. Кажется, не помещается."
    cs_narrator "Я посмотрела на надпись."
    cs_narrator "Затем на свободное место."
    cs_ls "Если продолжишь так же, последнее слово придётся писать на обратной стороне."
    cs_narrator "Семён вздохнул."
    cs_sy "Спасибо за поддержку."
    cs_narrator "Я улыбнулась."
    cs_ls "Подожди, сейчас исправим."
    cs_narrator "Мы осторожно стёрли разметку."
    cs_narrator "Я предложила немного уменьшить расстояние между буквами."
    cs_narrator "Он согласился."
    cs_narrator "Через несколько минут заголовок стал выглядеть значительно лучше."
    cs_sy "Слушай, а ты правда много рисовала до приезда?"
    cs_narrator "Я кивнула."
    cs_ls "Довольно много. В основном на компьютере."
    cs_sy "На графическом планшете?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Угу."
    cs_sy "Всегда хотел попробовать."
    cs_narrator "Я удивилась."
    cs_ls "Правда?"
    cs_sy "Ну да. Просто как-то не доходили руки."
    cs_narrator "Я ненадолго задумалась."
    cs_th "Забавно."
    cs_narrator "Оказывается, у нас появилось ещё одно общее занятие для разговора."
    cs_narrator "Причём совершенно не связанное с автобусом."
    cs_ls "Если вернёмся домой, сможешь попробовать."
    cs_narrator "Семён посмотрел на меня."
    cs_narrator "Несколько секунд молчал."
    cs_sy "Думаешь?"
    cs_narrator "Я остановилась."
    cs_narrator "Карандаш замер над бумагой."
    cs_th "Вот так."
    cs_th "Самая обыкновенная фраза внезапно превратилась в напоминание."
    cs_narrator "Ни у кого из нас не было уверенности, что мы вернёмся."
    cs_narrator "Но и отказываться от этой надежды пока было рано."
    cs_narrator "Я посмотрела на Семёна."
    cs_ls "Думаю, надо хотя бы попытаться."
    cs_narrator "Он кивнул."
    cs_sy "Согласен."
    cs_narrator "Дарья, до этого молча разбиравшая карандаши, посмотрела на нас."
    cs_da "Тогда сначала закончим объявление. А уже потом будем обсуждать планы на возвращение."
    cs_narrator "Я улыбнулась."
    cs_ls "Правильный подход."
    cs_narrator "Семён снова взял карандаш."
    cs_sy "Ну что, продолжаем?"
    cs_ls "Продолжаем."
    cs_narrator "Мы дописали заголовок."
    cs_narrator "На этот раз всё поместилось."
    cs_narrator "И даже получилось довольно аккуратно."
    cs_narrator "Я посмотрела на Семёна."
    cs_ls "Поздравляю. Художественная комиссия одобряет результат."
    cs_narrator "Он усмехнулся."
    cs_sy "Наконец-то."
    return
