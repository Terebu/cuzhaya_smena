# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_05:
    $ save_name = u"Чужая смена — День 1: То, что осталось дома"
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    play music cs_day_music_home fadeout 2.0 fadein 4.0
    $ renpy.music.set_volume(0.15, delay=2.0, channel="ambience")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    # cs_director_begin: REFLECTIVE_SHOT: Moscow and the life left behind
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_d3d42e530a:
    # cs_director_end
    cs_narrator "Одно дело — рассуждать о новелле, в которую попала. И совсем другое — вспомнить, что где-то осталась моя жизнь."
    cs_narrator "Квартира, работа, графический планшет. Картины, которые я так и не закончила."
    cs_narrator "Привычный мир, в котором утром была зима, а автобусы обычно довозили людей хотя бы приблизительно до нужной остановки."
    pause 1.0
    cs_narrator "Всё вокруг выглядело настоящим, и от этого становилось тревожнее."
    cs_th "Ладно. Допустим, ты здесь. Что дальше?"
    # cs_director_begin: Return to direct interaction: Moscow and the life left behind
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_4b1ab5b0ff:
    # cs_director_end
    cs_narrator "Я поправила одежду на плече."
    cs_ls "Предположим, правила хотя бы частично совпадают с игрой."
    cs_narrator "Дарья повернулась ко мне."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда что должно произойти дальше?"
    # cs_director_begin: REFLECTIVE_SHOT: Remembering the beginning of the novel
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_81ca1cb78b:
    # cs_director_end
    cs_narrator "Я вспомнила начало новеллы: автобус, ворота, первую встречу."
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.65, delay=2.0, channel="ambience")
    cs_narrator "За оградой послышались шаги. К нам кто-то приближался."
    return
