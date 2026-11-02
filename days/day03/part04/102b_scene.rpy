# -*- coding: utf-8 -*-
label cs_day03_102b:
    $ save_name = "Чужая смена — День 3: Не обязательно вмешиваться"
    cs_narrator "Я посмотрела на Алису, потом на её палец."
    cs_th "Вообще-то она уже пришла к Виоле. Пожалуй, медицинскую консультацию без медицинского образования проводить не требуется."
    cs_ls "Тогда не будем тебя задерживать. Надеюсь, всё быстро пройдёт."
    cs_narrator "Алиса посмотрела на меня. Немного удивлённо."
    cs_dv "Ага. Спасибо."
    cs_narrator "Я улыбнулась."
    cs_ls "И удачи."
    cs_narrator "Она усмехнулась."
    cs_dv "Тебе тоже. Только перестань испытывать прочность деревьев."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась. Я вздохнула."
    cs_ls "Даже не представляешь, насколько популярна эта рекомендация."
    if renpy.showing("dv"):
        show dv smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса улыбнулась."
    cs_dv "Верю."
    $ cs_actor_exit(["dv"])
    with cs_sprite_leave
    label cs_check_day03_102_alice_left_b:
    cs_narrator "Она вернулась в медпункт."
    cs_th "Всё. Нормально поговорили. Никто никого не обидел. Это уже можно считать положительным результатом."
    return
