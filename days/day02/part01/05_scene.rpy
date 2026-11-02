# -*- coding: utf-8 -*-
label cs_day02_05:
    $ save_name = "Чужая смена — День 2: Четыреста десятый"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day at cs_early_morning
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
    stop music fadeout 2.0
    label cs_check_new_d2_s05:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После спортплощадки я решила сделать ещё круг. Лагерь уже просыпался: хлопали двери, слышались первые голоса. Автобус оставался единственной понятной связью с Москвой. Стоило хотя бы проверить, здесь ли он ещё. Я свернула к воротам."
    $ cs_director_scene("bg ext_camp_entrance_day")
    scene bg ext_camp_entrance_day at cs_early_morning
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
    play music "sound/music/into_the_unknown.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_gate:
    cs_narrator "И остановилась."
    $ cs_director_scene("bg ext_no_bus")
    scene bg ext_no_bus at cs_early_morning
    with Dissolve(0.8)
    cs_narrator "Между деревьями уходила обычная асфальтовая дорога. А место, где вчера стоял «Икарус», пустовало. Я подошла к обочине и присела. Следы обуви, какие-то полосы на земле — ничего, что помогло бы понять, куда уехал автобус."
    cs_th "Ну замечательно. Транспортное средство, доставившее нас сюда, решило закончить смену раньше пассажиров."
    cs_narrator "Я выпрямилась. За воротами не было ни стены, ни тумана. Только лес, асфальт и утреннее солнце. От этого было не по себе. Вчерашняя остановка в Москве тоже выглядела обычно. А потом мы проснулись здесь. Я сделала шаг ближе к воротам."
    cs_narrator "Остановилась."
    cs_th "А если просто пойти?"
    cs_narrator "Хотя бы до первого поворота. Вдруг там есть ещё здания или люди? Я посмотрела вдоль дороги. Но вспомнила наш уговор с Дарьей: поодиночке ничего не проверять."
    cs_th "Ну да. Правила, которые сама согласилась соблюдать. Как неудобно."
    cs_narrator "Я ещё раз посмотрела на дорогу. И медленно отступила."
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
    cs_ls "Нет. Сегодня без самостоятельных экспедиций."
    cs_narrator "Я не знала, что за воротами. И выяснять это ценой ещё одного исчезновения не хотелось."
    cs_th "Вчера мы попали сюда вместе. Значит, и разбираться будем вместе."
    cs_narrator "Я ещё раз посмотрела на пустую стоянку и повернулась к лагерю."
    stop music fadeout 3.0
    return
