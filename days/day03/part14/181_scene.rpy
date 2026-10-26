# -*- coding: utf-8 -*-
label cs_day03_181:
    $ save_name = "Чужая смена — День 3: Две кровати и один вопрос"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    cs_narrator "Дарья взяла вещи для сна."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Давай сначала умоемся. А потом переоденемся и ляжем."
    cs_narrator "Я поднялась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "С удовольствием. А то после целого дня в этой форме начинаю понимать, почему человечество изобрело домашнюю одежду."
    cs_narrator "Она улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я взяла полотенце и ненадолго вышла."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_narrator "Когда я вернулась, Даша положила полотенце на спинку стула. Одежду для сна мы пока оставили рядом с подушками."
    cs_narrator "Я отложила своё полотенце и поправила рукав над повязкой."
    cs_narrator "Потом осторожно села на свою кровать."
    cs_narrator "Комната выглядела привычно."
    cs_narrator "Две кровати."
    cs_narrator "Стол."
    cs_narrator "Шкаф."
    cs_narrator "Окно."
    cs_narrator "Ничего особенного."
    cs_narrator "Но на кроватях мой взгляд почему-то задержался."
    cs_th "Вчера я уже задавала ей один вопрос."
    cs_th "Предлагала спать вместе."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "И она отказалась."
    cs_th "Спокойно."
    cs_th "Без объяснений, которые была обязана мне давать."
    cs_th "Я тогда согласилась."
    cs_th "И правильно сделала."
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она поправляла подушку."
    cs_narrator "Вчерашний разговор неожиданно снова всплыл в памяти."
    cs_th "Сегодня многое изменилось."
    if cs_da_day3_fear_of_getting_used_to_camp:
        cs_th "Я уже смогла сказать ей, почему боюсь привыкнуть к лагерю. И она выслушала."
    elif cs_da_day3_music_talk:
        cs_th "После разговора о музыке мне стало легче говорить с ней без заготовленных шуток."
    cs_th "Мы провели вместе ещё один день."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Разговаривали."
    cs_th "Смеялись."
    cs_th "Иногда просто молчали."
    cs_th "Но означает ли это, что теперь можно снова спросить?"
    cs_narrator "Я задумалась."
    cs_th "Можно."
    cs_th "Только не вести себя так, будто вчерашнее «нет» превратилось в сегодняшнее «да» само по себе."
    cs_narrator "Дарья заметила мой взгляд."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Лен?"
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "М?"
    cs_narrator "Она улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты чего так серьёзно смотришь на кровать?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Провожу исследование спальных мест."
    cs_narrator "Она приподняла бровь."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Очень интересная тема."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Особенно учитывая размеры местной мебели. Подозреваю, проектировщик рассчитывал исключительно на дисциплинированных пионеров, которые спят смирно и не претендуют на чужое одеяло."
    cs_narrator "Даша рассмеялась."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты что-то задумала?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "На этот раз не стала сразу отвечать шуткой."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Вообще-то да."
    cs_narrator "Она перестала поправлять подушку."
    cs_narrator "Села на край своей кровати."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Слушаю."
    cs_narrator "Я почувствовала, как становится немного неловко."
    cs_th "Вот ведь."
    cs_th "Обвинить Семёна в вымышленном семейном предательстве при Славе — без проблем."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "А задать Даше один нормальный вопрос — сразу начинаются сложности."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И решила не превращать разговор в очередное представление."
    return
