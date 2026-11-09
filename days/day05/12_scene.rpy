# -*- coding: utf-8 -*-
label cs_day05_12:
    $ cs_d5_scene = 12
    $ save_name = "Чужая смена — День 5: Чужая дата"
    $ cs_bus_scene_enter(12)
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Сегодня утром возле ворот появился автобус."
    cs_narrator "Славя посмотрела на него."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Автобус?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: ee56d97ebccafb59ed10
    cs_sy "Да."
    cs_sy "Тот самый, четыреста десятый."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "И что в нём необычного?"
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Он ехал без водителя."
    cs_narrator "Славя нахмурилась."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Может, вы просто не разглядели?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Мы смотрели прямо на лобовое стекло."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b5b990425202428e5b8d
    cs_ls "Я бы с удовольствием ошиблась."
    cs_ls "Но водительское место было пустым."
    cs_narrator "Славя некоторое время молчала."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "А Ольга Дмитриевна знает?"
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 976e1a4f35ec706c28c5
    cs_mz "Мы уже рассказали."
    cs_mz "Она сама ходила смотреть остановку."
    cs_narrator "Славя перевела взгляд на меня."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "И что теперь?"
    cs_narrator "Я достала копию списка из старого корпуса."
    cs_narrator "Положила перед ней."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вот ещё одна вещь, которую мы нашли."
    cs_narrator "Она взяла лист."
    cs_narrator "Пробежала глазами по именам."
    cs_narrator "Затем остановилась на дате."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Семьдесят первый год?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Да."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Откуда это?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 97833a3cc72a459cc02c
    cs_ls "Из старого корпуса."
    cs_ls "Оригинал сейчас у Ольги Дмитриевны."
    cs_narrator "Славя снова посмотрела на список."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Здесь знакомые фамилии."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Именно поэтому мы и пытаемся разобраться."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "А вдруг это просто совпадение?"
    cs_narrator "Я кивнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 402342ef6dcfab49af08
    cs_ls "Может быть."
    cs_ls "Мы пока не исключаем."
    cs_narrator "Она посмотрела на меня с лёгким удивлением."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Ты сейчас серьёзно?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Славя, я умею не делать выводов за пять секунд."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Иногда."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Не мешай мне выглядеть убедительно."
    cs_narrator "Славя улыбнулась, но снова стала серьёзной."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Чем я могу помочь?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b933b1c0dcdfeaea30d2
    cs_ls "Посмотри фотографии вместе с нами."
    cs_ls "Если узнаешь кого-то, скажешь."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: bed3e6f22038ee7c63a3
    cs_mz "Только фотографии — после обеда, в библиотеке."
    cs_mz "Не здесь."
    $ cs_d5_focus("sl")
    with cs_sprite_change
    cs_sl "Хорошо."
    if cs_friend_sl >= 4:
        $ cs_d5_focus("sl")
        with cs_sprite_change
        cs_sl "Я останусь с вами."
        cs_narrator "Я подняла глаза."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "У тебя же дела."
        $ cs_d5_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: e231073cd4f488e97ff4
        cs_sl "Закончу дежурство и приду."
        cs_sl "Мне тоже хочется понять, что происходит."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 2e29901325166ec2ebb0
        cs_ls "Вот за что тебя ценю."
        cs_ls "Даже к загадочному автобусу подходишь по расписанию."
        $ cs_d5_focus("sl")
        with cs_sprite_change
        cs_sl "А ты могла бы попробовать хоть иногда приходить вовремя."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Мы сейчас не обо мне."
        cs_narrator "Славя рассмеялась."
        $ cs_d5_slavya_volunteer = True
    else:
        $ cs_d5_focus("sl")
        with cs_sprite_change
        # cs_page_anchor: a3c4f1098abd7dd7b787
        cs_sl "Я принесу папку, как просила вожатая."
        cs_sl "Потом мне нужно будет вернуться к своим делам."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: f3341b18a904ce7f83e1
        cs_ls "Конечно."
        cs_ls "Спасибо, что поможешь."
        $ cs_d5_focus("sl")
        with cs_sprite_change
        cs_sl "Если понадобится что-нибудь ещё, скажите Ольге Дмитриевне."
        $ cs_d5_slavya_volunteer = False
    cs_narrator "Славя продолжила обедать."
    cs_narrator "Я тоже взялась за ложку."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Суп почти остыл."
    cs_narrator "После утренней пробежки и всех разговоров он всё равно казался замечательным."
    cs_narrator "Даша заметила, что я снова смотрю в сторону двери."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Лен, ешь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ем."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Ты уже минуту ложку не поднимаешь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Осмысляю вкус."
    cs_narrator "Она пододвинула ко мне стакан компота."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Тогда осмысли ещё и это."
    cs_narrator "Я улыбнулась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Спасибо."
    cs_narrator "Мы наконец закончили обед."
    $ cs_d5_room("bg ext_dining_hall_near_day")
    cs_narrator "На выходе нас догнала Алиса."
    cs_narrator "В руках у неё был свёрнутый провод."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Даша, ты сегодня к пианино зайдёшь?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 44afdac334a7d4bc2c99
    cs_da "Не знаю."
    cs_da "А что?"
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Мику хотела кое-что показать."
    cs_narrator "Она посмотрела на нас."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    # cs_page_anchor: 7123bea8281a23a6f533
    cs_dv "А вы чего такие мрачные?"
    cs_dv "Весь обед шептались, как заговорщики."
    cs_narrator "Я переглянулась с Семёном."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Алиса, у тебя есть немного времени?"
    $ cs_d5_focus("dv")
    with cs_sprite_change
    cs_dv "Смотря для чего."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: b036aed4b4662a05648b
    cs_ls "Нужно кое-что рассказать."
    cs_ls "Только лучше не здесь."
    cs_narrator "Алиса посмотрела на провод."
    $ cs_d5_focus("dv")
    with cs_sprite_change
    # cs_page_anchor: a0c59b2ed84ee0dc782c
    cs_dv "Тогда пошли в клуб."
    cs_dv "Всё равно туда иду."
    $ cs_d5_room("cs_camp_path_day")
    cs_narrator "И мы свернули на дорожку к музыкальному кружку."
    return
