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
    cs_narrator "После спортивной площадки я решила сделать ещё небольшой круг."
    cs_narrator "Лагерь постепенно просыпался."
    cs_narrator "Вдалеке хлопнула дверь."
    cs_narrator "Кто-то вышел на крыльцо."
    cs_narrator "Слышались первые разговоры."
    cs_narrator "Я бежала уже не так быстро."
    cs_narrator "Отчасти из-за усталости."
    cs_narrator "Отчасти потому, что мысли постепенно возвращались к вчерашним событиям."
    cs_narrator "Перед глазами всплыло знакомое изображение."
    cs_narrator "Ворота."
    cs_narrator "Вывеска."
    cs_narrator "Дорога."
    cs_narrator "И автобус номер четыреста десять, который привёз нас сюда."
    cs_th "А ведь мы так и не выяснили, куда он делся."
    cs_narrator "Я замедлила шаг."
    cs_narrator "Вчера всё произошло слишком быстро."
    cs_narrator "Сначала встреча со Славей."
    cs_narrator "Потом разговор с Ольгой Дмитриевной."
    cs_narrator "Переодевание."
    cs_narrator "Знакомство с лагерем."
    cs_narrator "Столовая."
    cs_narrator "И уже к вечеру я почти перестала думать о самом автобусе."
    cs_narrator "Хотя именно он был единственной понятной связью между Москвой и этим местом."
    cs_narrator "Я свернула к воротам."
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
    cs_narrator "Передо мной лежала дорога."
    cs_narrator "Обычная асфальтовая дорога, уходившая между деревьями."
    cs_narrator "По обеим сторонам рос лес."
    cs_narrator "У ворот было тихо."
    cs_narrator "Я огляделась."
    cs_narrator "Потом посмотрела туда, где вчера стоял автобус."
    cs_narrator "Пусто."
    cs_narrator "Я медленно подошла ближе."
    cs_th "Так."
    cs_th "А вот это уже интереснее."
    cs_narrator "Никакого четыреста десятого."
    cs_narrator "Никакого водителя."
    cs_narrator "Никаких пассажиров."
    cs_narrator "Даже намёка на то, что вчера здесь стоял современный городской автобус."
    cs_narrator "Я посмотрела вдоль дороги."
    cs_narrator "Сделала несколько шагов к обочине."
    cs_narrator "Присела."
    cs_narrator "На земле виднелись какие-то следы."
    cs_narrator "От обуви?"
    cs_narrator "От колёс?"
    cs_narrator "После вчерашнего и сегодняшнего движения по лагерю определить было невозможно."
    cs_narrator "Я провела взглядом по асфальту."
    cs_narrator "Никаких очевидных следов, которые могли бы объяснить исчезновение машины."
    cs_th "Ну замечательно."
    cs_th "Транспортное средство, доставившее нас сюда, решило закончить смену раньше пассажиров."
    cs_narrator "Я выпрямилась."
    cs_narrator "Посмотрела наружу."
    cs_narrator "Дорога выглядела совершенно нормально."
    cs_narrator "Не было никакой стены."
    cs_narrator "Никакого тумана."
    cs_narrator "Никакой преграды."
    cs_narrator "Лес."
    cs_narrator "Асфальт."
    cs_narrator "Утренний солнечный свет."
    cs_narrator "И от этого становилось даже не по себе."
    cs_narrator "Ведь вчера всё тоже выглядело нормально."
    cs_narrator "Современный автобус."
    cs_narrator "Обычная остановка."
    cs_narrator "Ничего, что могло бы предупредить о происходящем."
    cs_narrator "А потом мы проснулись здесь."
    cs_narrator "Я сделала шаг ближе к воротам."
    cs_narrator "Остановилась."
    cs_th "А если просто пойти?"
    cs_narrator "Не обязательно далеко."
    cs_narrator "Хотя бы до первого поворота."
    cs_narrator "Посмотреть, куда ведёт дорога."
    cs_narrator "Есть ли там другие здания."
    cs_narrator "Другие люди."
    cs_narrator "Возможно, населённый пункт."
    cs_narrator "Или хоть что-нибудь, что не соответствует знакомой карте игры."
    cs_narrator "Я долго смотрела вперёд."
    cs_narrator "Потом вспомнила вчерашний разговор с Дарьей."
    cs_narrator "Мы обещали не проверять дорогу поодиночке."
    cs_narrator "Она специально напомнила об этом утром."
    cs_narrator "И я пообещала."
    cs_narrator "Я опустила взгляд."
    cs_th "Ну да."
    cs_th "Правила, которые сама согласилась соблюдать."
    cs_th "Как неудобно."
    cs_narrator "Я ещё раз посмотрела на дорогу."
    cs_narrator "И медленно отступила."
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
    cs_narrator "Дело было даже не в том, что за воротами могло оказаться что-нибудь опасное."
    cs_narrator "Я понятия не имела, что именно там находится."
    cs_narrator "И совершенно не хотела выяснять это ценой ещё одного необъяснимого исчезновения."
    cs_th "Вчера мы попали сюда вместе."
    cs_th "Значит, и разбираться будем вместе."
    cs_narrator "Я посмотрела на пустое место возле ворот."
    cs_th "Автобус исчез."
    cs_th "Вот теперь у нас есть ещё один вопрос."
    cs_narrator "Я мысленно добавила его к списку наблюдений."
    cs_narrator "Затем повернулась обратно к лагерю."
    stop music fadeout 3.0
    return
