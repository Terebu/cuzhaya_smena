# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_05:
    $ save_name = u"Чужая смена — День 1: То, что осталось дома"
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    play music cs_day_music_home fadeout 2.0 fadein 4.0
    $ renpy.music.set_volume(0.15, delay=2.0, channel="ambience")
    cs_narrator "Потому что одно дело — рассуждать о визуальной новелле, в которую каким-то невероятным образом попала."
    cs_narrator "И совсем другое — вспомнить, что где-то осталась моя жизнь."
    cs_narrator "Квартира."
    cs_narrator "Знакомые вещи."
    cs_narrator "Работа."
    cs_narrator "Люди."
    cs_narrator "Интернет."
    cs_narrator "Моя комната."
    cs_narrator "Графический планшет."
    cs_narrator "Картины, которые я так и не закончила."
    cs_narrator "Привычный мир, в котором утром была зима, а автобусы обычно довозили людей хотя бы приблизительно до нужной остановки."
    pause 1.0
    cs_narrator "Я посмотрела на ворота."
    cs_narrator "Всё вокруг выглядело совершенно настоящим."
    cs_narrator "И от этого становилось только тревожнее."
    cs_th "Ладно."
    cs_th "Допустим, ты действительно здесь."
    cs_th "Что дальше?"
    cs_narrator "Я поправила одежду на плече."
    cs_ls "Предположим, правила хотя бы частично совпадают с игрой."
    cs_narrator "Дарья повернулась ко мне."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "Тогда что должно произойти дальше?"
    cs_narrator "Я задумалась."
    cs_narrator "Хороший вопрос."
    cs_narrator "Очень хороший."
    cs_narrator "Я вспомнила начало новеллы."
    cs_narrator "Автобус."
    cs_narrator "Ворота."
    cs_narrator "Первую встречу."
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.65, delay=2.0, channel="ambience")
    cs_narrator "И почти одновременно с этой мыслью за оградой послышались шаги."
    cs_narrator "Я замерла."
    cs_narrator "К нам кто-то приближался."
    return
