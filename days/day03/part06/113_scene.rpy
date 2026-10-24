# -*- coding: utf-8 -*-
label cs_day03_113:
    $ save_name = "Чужая смена — День 3: Дела, которые сами себя не сделают"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadein 2.0
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
    label cs_check_day03_113:
    cs_narrator "После расставания с Семёном мы наконец остались вдвоём."
    cs_narrator "Я посмотрела на дорожку."
    cs_narrator "Потом на часы."
    cs_narrator "Потом снова на дорожку."
    cs_th "Так."
    cs_th "На сегодняшний день общественно полезная деятельность выполнена."
    cs_th "Документы доставлены."
    cs_th "Локоть проверен."
    if cs_helped_sl_day3:
        cs_th "Славя не осталась один на один с бесконечными списками."
    else:
        cs_th "К Славе заглянули и честно сказали, что у нас ещё есть свои дела."
    cs_th "Даже с Семёном удалось поговорить без международного скандала."
    cs_th "Если продолжу в таком темпе, Ольга Дмитриевна начнёт использовать меня в качестве образцового пионера."
    cs_narrator "Я невольно улыбнулась."
    cs_da "Чего улыбаешься?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Представляю, как Ольга Дмитриевна вручает мне грамоту за примерное поведение."
    cs_narrator "Дарья остановилась."
    cs_narrator "Посмотрела на меня."
    cs_narrator "Затем улыбнулась."
    cs_da "Думаешь, доживём до такого?"
    cs_narrator "Я задумалась."
    cs_ls "Зависит от того, сколько ещё раз мне удастся не упасть."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я осторожно поправила рукав возле повязки."
    cs_da "Кстати, рука как?"
    cs_ls "Лучше. Виола сказала, что всё заживает нормально."
    cs_da "Тогда, пожалуйста, не проверяй это сегодня на практике."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даш, у меня появляется ощущение, что ты собираешься повторять это каждый час."
    cs_narrator "Она улыбнулась."
    cs_da "Если понадобится."
    cs_narrator "Я вздохнула."
    cs_ls "Какая предусмотрительность. Даже будильник не нужен."
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Мы остановились возле развилки."
    if cs_mz_map_lead and not cs_mz_catalog_checked_day3:
        cs_narrator "Я вспомнила вчерашний разговор с Женей."
        cs_th "Точно."
        cs_th "Каталоги."
        cs_narrator "Она ведь не просто предложила мне очередную книгу. Мы договорились посмотреть, не сохранилось ли в библиотеке что-нибудь о самом лагере."
        cs_narrator "Я повернулась к Дарье."
        cs_ls "Сначала к Жене?"
        cs_narrator "Она кивнула."
        cs_da "Мы же обещали."
        cs_ls "Вот именно. А то ещё окажется, что единственный ответственный человек в нашей компании — библиотекарь."
        if renpy.showing("cs_darya"):
            show cs_darya thinking pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья приподняла бровь."
        cs_da "Единственный?"
        cs_narrator "Я посмотрела на неё."
        cs_ls "Ну хорошо. Один из двух."
        cs_da "Уже лучше."
        cs_narrator "Я улыбнулась."
        cs_narrator "Мы свернули к библиотеке."
    else:
        cs_narrator "Дарья посмотрела в сторону музыкального клуба."
        cs_da "Тогда, может, к Мику?"
        cs_narrator "Я повернулась к ней."
        cs_ls "С удовольствием."
        cs_narrator "Она слегка удивилась."
        cs_da "И никаких замечаний про пианино?"
        cs_narrator "Я задумалась."
        cs_ls "Могу подготовить официальную просьбу о проведении частного концерта."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
        cs_da "Не надо."
        cs_ls "Тогда просто пойдём."
        cs_narrator "Она улыбнулась."
        cs_narrator "Мы направились к музыкальному клубу."
    return
