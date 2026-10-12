# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_26:
    $ save_name = "Чужая смена — День 1: Дорога к новому дому"
    scene bg ext_dining_hall_near_day
    show sl smile pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    with Dissolve(1.3)
    $ renpy.music.set_volume(0.45,delay=1.0,channel="music")
    play music cs_day_music_daily fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_camp_center:
        play ambience cs_day_camp_center fadeout 1.5 fadein 2.0
    cs_narrator "Снаружи нас снова встретило летнее солнце."
    cs_narrator "После прохладной столовой жара казалась особенно заметной."
    cs_narrator "Я машинально поправила галстук."
    cs_narrator "Всё-таки удивительная вещь."
    cs_narrator "Ещё утром я сидела в собственной комнате, собираясь за продуктами."
    cs_narrator "Теперь шла по советскому пионерлагерю в форме, которую мне выдали совершенно бесплатно."
    cs_th "Интересная программа лояльности."
    cs_narrator "Славя шагала впереди."
    cs_sl "Ваш домик недалеко. Там сейчас никто не живёт, так что можете располагаться вдвоём."
    cs_ls "Замечательно. А коммунальные платежи здесь предусмотрены?"
    cs_narrator "Славя удивлённо посмотрела на меня."
    show sl surprise pioneer at cs_actor_left
    cs_sl "Какие платежи?"
    cs_ls "Никакие. Уточняю условия проживания."
    cs_narrator "Дарья бросила на меня взгляд."
    show cs_darya serious pioneer normal at cs_darya_normal_right
    cs_da "Лен."
    cs_ls "Что?"
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    cs_da "Может, хотя бы пять минут без вопросов, которые никто не понимает?"
    cs_narrator "Я задумалась."
    cs_ls "Сложное требование. Но попробую."
    cs_narrator "Славя улыбнулась."
    scene cs_camp_path_day
    show sl smile pioneer at cs_actor_left
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    with Dissolve(1.4)
    cs_narrator "Мы свернули на дорожку между домиками."
    cs_narrator "Над головами шелестели деревья."
    cs_narrator "Где-то стрекотали насекомые."
    cs_narrator "Издалека слышались голоса пионеров."
    cs_narrator "Я смотрела по сторонам и снова ловила себя на странном ощущении узнавания."
    cs_narrator "Вон тот поворот."
    cs_narrator "Знакомая ограда."
    cs_narrator "Фасад клуба, мелькнувший между деревьями."
    cs_narrator "Всё выглядело так, будто кто-то взял нарисованные фоны и осторожно соединил их в единое пространство."
    cs_narrator "Только теперь оно существовало независимо от моего взгляда."
    cs_narrator "Я могла свернуть не туда."
    cs_narrator "Зайти за домик."
    cs_narrator "Увидеть то, чего не было ни на одном изображении из игры."
    cs_narrator "И это одновременно притягивало и настораживало."
    cs_narrator "Дарья заметила, что я замедлила шаг."
    cs_da "Опять что-то узнала?"
    cs_ls "Скорее пытаюсь сопоставить географию с памятью."
    cs_da "Получается?"
    cs_ls "Пока да. Но это как пользоваться картой города, нарисованной человеком, который видел только пять перекрёстков."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_da "Звучит не слишком надёжно."
    cs_ls "Поэтому и проверяем."
    cs_narrator "Славя оглянулась."
    show sl smile pioneer at cs_actor_left
    cs_sl "Вы раньше бывали в похожем лагере?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "В похожем"
    show sl surprise pioneer at cs_actor_left
    cs_sl "А где?"
    cs_narrator "Пауза."
    cs_ls "Дома."
    cs_narrator "Ответ был достаточно расплывчатым, чтобы не вызвать новых вопросов."
    cs_narrator "По крайней мере, я на это надеялась."
    cs_narrator "Славя удовлетворённо кивнула и продолжила путь."
    cs_narrator "Дарья тихо произнесла:"
    cs_da "Неплохо выкрутилась."
    cs_ls "Спасибо. Запишем в протокол."
    return
