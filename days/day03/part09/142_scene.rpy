# -*- coding: utf-8 -*-
label cs_day03_142:
    $ save_name = "Чужая смена — День 3: Когда шутка уже закончилась"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    $ renpy.music.set_volume(0.12,delay=1.0,channel="music")
    cs_narrator "Мы отошли от лавочки. Несколько секунд Дарья молчала. Потом посмотрела на меня."
    cs_da "Слушай, Лен."
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    cs_da "А ты ведь действительно к нему привязалась."
    cs_ls "К Семёну?"
    cs_narrator "Она кивнула. Я посмотрела назад. Лавочку уже почти не было видно за деревьями."
    cs_ls "Наверное."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Раньше ты говорила, что он тебя просто забавляет."
    cs_narrator "Я помолчала."
    cs_ls "Забавляет. Но это ведь не всё."
    cs_narrator "Она посмотрела на меня. Я продолжила:"
    cs_ls "Он иногда ведёт себя довольно нелепо. Иногда отвечает так, что хочется схватиться за голову."
    cs_narrator "Немного улыбнулась."
    cs_ls "Но вообще он нормальный парень."
    cs_narrator "Дарья кивнула."
    cs_da "Мне тоже так кажется."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Просто у нас странное знакомство."
    cs_narrator "Она усмехнулась."
    cs_da "У вас?"
    cs_narrator "Я подняла бровь."
    cs_ls "Хорошо. У всех троих."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась. Мы продолжили идти."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Интересная вещь. В первые дни мне казалось, что я уже знаю Семёна. Каким он должен быть. Как станет реагировать."
    cs_th "Что скажет. Но вживую человек оказался куда менее предсказуемым. Иногда язвительным. Иногда совершенно растерянным."
    cs_th "А иногда способным сказать что-нибудь настолько обычное и искреннее, что вся моя заранее подготовленная ирония становилась неуместной."
    $ cs_pov_end()
    with cs_sprite_change
    cs_da "А что насчёт его прозвища?"
    cs_narrator "Я повернулась."
    cs_ls "Какого?"
    cs_narrator "Она улыбнулась."
    cs_da "«Сёмочка»."
    cs_narrator "Я вздохнула."
    cs_ls "Великолепное прозвище. Не оценённое современниками."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_da "Ты ведь не перестанешь так его называть?"
    cs_ls "Если ему действительно не нравится, перестану."
    cs_narrator "Она посмотрела на меня."
    cs_da "А шутки?"
    cs_ls "Шутки останутся. Просто появятся новые."
    if renpy.showing("cs_darya"):
        show cs_darya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья покачала головой."
    cs_da "Бедный Семён."
    cs_ls "Да. Ему явно не повезло оказаться в одном лагере со мной."
    cs_narrator "Пауза."
    cs_ls "Хотя, судя по сегодняшнему разговору, он начинает получать от этого определённое удовольствие."
    cs_narrator "Она улыбнулась."
    cs_da "Иногда мне тоже так кажется."
    cs_narrator "Мы улыбнулись друг другу. Вот и хорошо. Кажется, у нас начинает получаться настоящая дружба."
    return
