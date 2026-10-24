# -*- coding: utf-8 -*-
label cs_day03_109a:
    $ save_name = "Чужая смена — День 3: Отдел материального обеспечения"
    cs_narrator "Я посмотрела на Славю."
    cs_ls "Давай мы поможем."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_sl "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Сегодня у меня день общественно полезной деятельности."
    cs_narrator "Дарья усмехнулась."
    cs_da "Она с самого утра об этом объявляет."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Любое серьёзное начинание требует информационного сопровождения."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_sl "Хорошо. Тогда давайте так: Даша будет записывать, а ты — сверять со списком."
    cs_narrator "Я кивнула."
    cs_ls "Прекрасно. Работа по специальности: считать чужие вещи и делать умное лицо."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Последнее у тебя действительно хорошо получается."
    cs_narrator "Я посмотрела на неё."
    cs_th "Так."
    cs_th "Опять."
    cs_th "Скоро придётся вводить лицензирование сарказма."
    label cs_check_day03_109_seated:
    cs_narrator "Мы устроились за столом."
    cs_narrator "Славя принесла несколько небольших коробок."
    cs_narrator "Она сама переставляла их, чтобы мне не приходилось нагружать повреждённую руку."
    cs_narrator "Я проверяла названия и количество."
    cs_narrator "Дарья записывала."
    cs_ls "Ленты красные. Шесть штук."
    cs_da "Есть."
    cs_ls "Синие. Четыре."
    cs_da "Есть."
    cs_narrator "Я заглянула в следующую коробку."
    cs_ls "А вот тут у нас непонятное."
    if renpy.showing("sl"):
        show sl normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя подошла."
    cs_sl "Что такое?"
    cs_narrator "Я показала на несколько металлических креплений."
    cs_ls "Эти штуки в списке как называются?"
    cs_narrator "Она посмотрела."
    cs_sl "Зажимы."
    cs_narrator "Я задумалась."
    cs_ls "Логично. А я уже хотела записать «железные непонятности, пять штук»."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Славя тоже."
    cs_sl "Давай всё-таки правильно."
    cs_narrator "Я кивнула."
    cs_ls "Согласна. Потом кто-нибудь найдёт старую опись и решит, что здесь проводили секретные эксперименты с железными непонятностями."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Не подсказывай идеи."
    cs_narrator "Мы продолжили."
    cs_narrator "Работа заняла около двадцати минут."
    cs_narrator "За это время Славя успела рассказать, что вчера после концерта часть украшений сняли сразу, а часть оставили до утра, потому что уже было поздно."
    cs_sl "А сегодня всё нужно вернуть на места, иначе потом кто-нибудь возьмёт не то."
    cs_narrator "Я кивнула."
    cs_ls "Понимаю. Хаос в системе хранения имущества — первый шаг к гибели цивилизации."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_sl "Ну, не настолько."
    cs_ls "Хорошо. К небольшой хозяйственной катастрофе."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Через некоторое время мы добрались до последнего листа."
    cs_narrator "Я сверила количество креплений."
    cs_narrator "Дарья поставила отметку."
    cs_narrator "Славя просмотрела записи."
    cs_sl "Всё сходится!"
    cs_narrator "Я довольно откинулась на спинку стула."
    cs_ls "Поздравляю. Инвентарь спасён."
    cs_narrator "Она засмеялась."
    cs_sl "Спасибо вам большое. Я бы одна дольше возилась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Не за что."
    cs_narrator "Я кивнула."
    cs_ls "Обращайся. Только в следующий раз желательно не раньше шести утра."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_sl "Ты ведь сама встала раньше всех."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Пауза."
    cs_ls "Славя, почему ты постоянно используешь против меня мои же слова?"
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она довольно улыбнулась."
    cs_sl "Учусь."
    cs_narrator "Я покачала головой."
    cs_th "Ну что ж."
    cs_th "Похоже, уроки действительно усваиваются."
    return
