# -*- coding: utf-8 -*-
label cs_day02_01:
    $ save_name = "Чужая смена — День 2: Когда лагерь ещё спит"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_early_morning
    # cs_presence_keep: hide cs_darya
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    stop music fadeout 1.0
    label cs_check_new_d2_s01:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Проснулась я раньше лагеря. За окном было тихо, горн ещё молчал. Ни московской улицы, ни гудения компьютера. Только доски над головой и бесполезный разряженный телефон."
    cs_narrator "На соседней кровати спала Дарья. Красные пряди упали на лицо, одеяло она подтянула к плечам."
    cs_th "Как ей удаётся так спокойно спать после всего, что случилось вчера?"
    cs_narrator "Я ещё немного посмотрела на неё и отвернулась."
    cs_th "Соколова, перестань разглядывать человека. Он спит."
    cs_narrator "И всё же я улыбнулась. Вчера она разрешила себя приобнять. Сказала, что не хочет торопиться, — и я согласилась. Я попробовала снова уснуть. Без толку: организм уже выспался и требовал встать."
    cs_narrator "Я всегда была жаворонком. Могла бы полежать ещё, но через десять минут начала бы искать себе занятие. Посмотрела на спящую Дарью."
    cs_th "Нет. Сегодня попробуем без жертв."
    cs_narrator "Я осторожно села, опустила ноги на прохладный пол. Дарья не проснулась."
    return
