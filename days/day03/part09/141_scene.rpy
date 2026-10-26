# -*- coding: utf-8 -*-
label cs_day03_141:
    $ save_name = "Чужая смена — День 3: Полезная информация без секретов"
    cs_narrator "Я посмотрела на книгу."
    cs_narrator "Потом в сторону клубов."
    cs_ls "Кстати, раз уж мы заговорили о рисовании…"
    cs_narrator "Семён повернулся."
    cs_sy "Что?"
    if cs_un_sketch_time_agreed_day3:
        cs_ls "Я сегодня с Тихоновой обсуждала её рисунки. Возможно, ближе к вечеру вместе что-нибудь нарисуем."
    else:
        cs_ls "Утром видели Тихонову с альбомом. Я вот тоже хочу сегодня порисовать."
    cs_narrator "Он кивнул."
    cs_sy "А, с Леной?"
    cs_narrator "Я улыбнулась."
    cs_ls "Да. С другой Леной. У нас здесь теперь собственная проблема однофамильцев, только ещё на этапе имён."
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Очень удобно, когда кто-то кричит «Лена!», а оборачиваетесь обе."
    cs_narrator "Я кивнула."
    cs_ls "Зато можно организовать коллективную ответственность за любые происшествия."
    if renpy.showing("cs_semen"):
        show cs_semen relaxed pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Семён рассмеялся."
    cs_sy "Даже не пытайся."
    cs_narrator "Я улыбнулась."
    if cs_se_friend_before_square_day3 >= 2 and cs_un_sketch_time_agreed_day3:
        if renpy.showing("cs_semen"):
            show cs_semen thinking pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Семён задумался."
        cs_narrator "Потом кивнул куда-то в сторону клубов."
        cs_sy "Слушай, если будете рисовать лагерь, там за музыкальным клубом есть неплохое место."
        cs_narrator "Я заинтересовалась."
        cs_ls "Какое?"
        cs_sy "Небольшая скамейка у деревьев. Оттуда хорошо видно дорожку и часть площади. И солнце после обеда не так сильно мешает."
        cs_narrator "Я посмотрела в указанную сторону."
        cs_ls "Правда?"
        cs_narrator "Он кивнул."
        cs_sy "Я там утром проходил. Почти никого не было."
        cs_narrator "Я задумалась."
        cs_narrator "Хм."
        cs_narrator "Тень."
        cs_narrator "Нормальный вид."
        cs_narrator "И отсутствие толпы."
        cs_narrator "Звучит вполне подходяще."
        cs_ls "Спасибо. Надо будет посмотреть."
        cs_narrator "Семён улыбнулся."
        cs_sy "Только не говори потом, что это я организовал вам художественное мероприятие."
        cs_narrator "Я кивнула."
        cs_ls "Хорошо. В официальных документах укажем анонимного консультанта."
        cs_narrator "Он рассмеялся."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "А по-моему, хорошая идея."
        cs_narrator "Я кивнула."
        cs_ls "Тогда проверим, когда встретимся с Тихоновой."
        $ cs_se_sketch_spot_day3 = True
    else:
        cs_narrator "Семён посмотрел в сторону дорожки."
        cs_sy "Тогда удачи. Главное, чтобы вам никто не мешал."
        cs_narrator "Я улыбнулась."
        cs_ls "Спасибо. Художникам иногда требуется тишина не меньше, чем библиотекарям."
        cs_narrator "Он усмехнулся."
        cs_sy "Надеюсь, ты сама себе мешать не будешь."
        cs_narrator "Я приподняла бровь."
        cs_ls "Семён, мне начинает казаться, что моя репутация творческого человека находится под угрозой."
        cs_narrator "Он рассмеялся."
    cs_narrator "Я поднялась с лавочки."
    cs_narrator "Осторожно взяла книгу."
    cs_narrator "Дарья тоже встала."
    cs_narrator "Семён посмотрел на нас."
    cs_sy "Ну что, пойдёте?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Ещё надо заглянуть в домик."
    cs_narrator "Он улыбнулся."
    cs_sy "Тогда увидимся."
    cs_narrator "Я посмотрела на него."
    cs_ls "До встречи, товарищ Семён."
    cs_narrator "Он приподнял бровь."
    cs_sy "Уже без «Сёмочки»?"
    cs_narrator "Я остановилась."
    cs_narrator "Медленно повернулась к нему."
    cs_narrator "О."
    cs_narrator "А это интересно."
    cs_ls "Ты же просил."
    cs_narrator "Он на секунду замолчал."
    cs_narrator "Потом усмехнулся."
    cs_sy "И правильно."
    cs_narrator "Я улыбнулась."
    cs_ls "Вот и договорились."
    if renpy.showing("cs_darya"):
        show cs_darya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья покачала головой."
    cs_narrator "Но тоже улыбалась."
    cs_narrator "Мы попрощались."
    $ cs_actor_exit(["cs_semen"])
    with cs_sprite_leave
    cs_narrator "И направились к домикам."
    cs_narrator "Ну вот."
    cs_narrator "Семён жив."
    cs_narrator "Я жива."
    cs_narrator "И мы сумели провести вполне нормальный разговор."
    cs_narrator "Кажется, подобное действительно заслуживает упоминания в лагерной летописи."
    return
