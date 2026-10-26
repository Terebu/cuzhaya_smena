# -*- coding: utf-8 -*-
label cs_day03_183:
    $ save_name = "Чужая смена — День 3: Второй вопрос"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    cs_narrator "Я немного помолчала."
    cs_narrator "Потом посмотрела Даше в глаза."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Слушай…"
    cs_narrator "Она улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Да?"
    cs_narrator "Я осторожно поправила край одеяла."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Помнишь, вчера я спрашивала, можно ли нам спать вместе?"
    cs_narrator "Даша кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Помню."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "И ты сказала, что пока не хочешь."
    cs_narrator "Она снова кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Да."
    cs_narrator "Я посмотрела на неё."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Я не считаю, что за сегодняшний день ты должна была передумать."
    cs_narrator "Даша чуть улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Просто хочу спросить ещё раз."
    cs_narrator "Пауза."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Можно сегодня лечь рядом с тобой?"
    cs_narrator "Она перестала улыбаться, но не потому, что рассердилась."
    cs_narrator "Скорее задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты серьёзно?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ага."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "А почему тебе хочется?"
    cs_narrator "Я немного подумала."
    cs_th "Хороший вопрос."
    cs_th "И, к моему собственному удивлению, у меня есть нормальный ответ."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Потому что мне спокойно рядом с тобой."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_narrator "Я продолжила:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Сегодня был хороший день. Мы столько всего успели. И сейчас мне просто хочется немного побыть рядом."
    cs_narrator "Немного помолчала."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Не ради шутки. Не для того, чтобы потом кого-нибудь удивить."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Просто хочется заснуть рядом."
    cs_narrator "Даша опустила взгляд на свою кровать."
    cs_narrator "Потом снова посмотрела на меня."
    if cs_da_friend_before_night >= 2:
        cs_narrator "Она немного помолчала."
        cs_narrator "Затем улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Хорошо."
        cs_narrator "Я замерла."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Что хорошо?"
        cs_narrator "Она усмехнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Сегодня можешь лечь рядом со мной."
        cs_narrator "Я несколько секунд смотрела на неё."
        cs_th "Так."
        cs_th "Спокойно."
        if not cs_reflective_shot:
            $ cs_pov_begin()
            with cs_sprite_leave
        cs_th "Соколова."
        cs_th "Внутри сейчас начнётся торжественная церемония с салютом."
        cs_th "Нужно срочно отменить приглашение оркестра."
        cs_narrator "Я медленно улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Спасибо."
        cs_narrator "Дарья чуть приподняла бровь."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "И всё?"
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Я держусь."
        cs_narrator "Она рассмеялась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Вижу."
        cs_narrator "Я задумалась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Хотя должна признать, что внутренний комитет уже подготовил праздничную резолюцию."
        cs_narrator "Она покачала головой."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Лена…"
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Всё. Никаких резолюций."
        cs_narrator "Даша посмотрела на две кровати."
        cs_narrator "Потом на меня."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Только у меня кровать довольно узкая."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Это я заметила."
        cs_narrator "Она посмотрела на мою повязку."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "И локоть твой жалко."
        cs_narrator "Я улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "С ним будем аккуратно."
        cs_narrator "Даша немного подумала."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Тогда договорились. Но если станет неудобно, ты перейдёшь на свою кровать. Хорошо?"
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Конечно."
        cs_narrator "Она улыбнулась."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "И без ночных представлений."
        cs_narrator "Я приложила здоровую руку к груди."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Даю слово."
        cs_narrator "Даша прищурилась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Насколько оно надёжно?"
        cs_narrator "Я задумалась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Приблизительно настолько же, насколько советская мебель рассчитана на двух взрослых девушек."
        cs_narrator "Она рассмеялась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Значит, будем осторожны."
        cs_narrator "Я улыбнулась."
        cs_th "Вот и всё."
        cs_th "Никакого великого договора."
        if not cs_reflective_shot:
            $ cs_pov_begin()
            with cs_sprite_leave
        cs_th "Просто она согласилась."
        cs_th "А я не собираюсь превращать это согласие в обязательство на каждый следующий вечер."
        $ cs_da_shared_bed_day3 = True
        if not cs_da_shared_bed_awarded_day3:
            $ cs_friend_da += 1
            $ cs_da_shared_bed_awarded_day3 = True
    else:
        cs_narrator "Дарья немного помолчала."
        cs_narrator "Потом мягко покачала головой."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Лен, давай сегодня всё-таки отдельно."
        cs_narrator "Я посмотрела на неё."
        cs_narrator "Она добавила:"
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Мне с тобой хорошо. Правда. Просто я пока не готова так спать."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Хорошо."
        cs_narrator "Она внимательно посмотрела на меня."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Не обиделась?"
        cs_narrator "Я покачала головой."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Нет."
        cs_narrator "Немного улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Ты же не обязана соглашаться только потому, что я спросила."
        cs_narrator "Дарья выдохнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Спасибо."
        cs_narrator "Я посмотрела на две кровати."
        cs_narrator "Потом на неё."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Значит, продолжаем существовать в рамках двух независимых спальных государств."
        cs_narrator "Она рассмеялась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Именно."
        cs_narrator "Я кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Тогда устанавливаем добрососедские отношения."
        cs_narrator "Даша улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Они уже установлены."
        cs_th "Ну вот."
        cs_th "Ничего страшного."
        if not cs_reflective_shot:
            $ cs_pov_begin()
            with cs_sprite_leave
        cs_th "Даже наоборот."
        cs_th "Спросила."
        cs_th "Получила ответ."
        cs_th "И теперь мы обе знаем, что можем нормально об этом разговаривать."
    return
