# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_25:
    $ save_name = "Чужая смена — День 1: После обеда"
    hide mt with dissolve
    hide sl
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    show cs_darya tie_touch pioneer far at cs_darya_far_left
    label cs_check_day01_part06_lunch:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_dining_full:
        play ambience cs_day_dining_full fadeout 1.5 fadein 2.0
    cs_narrator "Я допила компот и поставила стакан на стол."
    cs_narrator "Семён всё ещё задумчиво смотрел куда-то мимо меня."
    cs_narrator "Понимала его."
    cs_narrator "Ещё вчера он, по собственным словам, считал себя единственным человеком, который каким-то невозможным образом оказался здесь."
    cs_narrator "А сегодня к нему присоединились две девушки из будущего. Причём одна имела неприятную привычку знать то, чего знать не должна."
    cs_th "Прекрасное пополнение."
    cs_th "Партия одобряет."
    show cs_semen smile pioneer far at cs_semen_far_right
    cs_sy "Слушай."
    cs_narrator "Я подняла глаза."
    cs_ls "М?"
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    cs_sy "А ты правда знаешь, что здесь может произойти?"
    cs_narrator "Я немного подумала."
    cs_ls "Знаю, что происходило в знакомой мне истории."
    cs_sy "Но это ведь не одно и то же?"
    cs_ls "Именно."
    cs_narrator "Семён кивнул, хотя легче ему от ответа явно не стало."
    cs_narrator "Дарья отодвинула пустую тарелку."
    show cs_darya shrug pioneer far at cs_darya_far_left
    cs_da "Тогда нам лучше сначала разобраться с тем, что известно наверняка."
    cs_ls "Разумное предложение."
    cs_da "Для начала нам нужен домик, где можно оставить вещи и спокойно поговорить."
    show cs_semen smile pioneer far at cs_semen_far_right
    cs_sy "А ещё неплохо бы выяснить дату."
    cs_narrator "Я повернулась к нему."
    cs_ls "Вот. Уже два полезных предложения. Рабочая группа демонстрирует положительную динамику."
    cs_narrator "Семён усмехнулся."
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    cs_sy "Ты всегда так разговариваешь?"
    cs_ls "Не всегда. Иногда я сплю."
    show cs_darya amused pioneer far at cs_darya_far_left
    cs_narrator "Дарья тихо рассмеялась."
    stop music fadeout 2.0
    show sl smile pioneer far at cs_actor_left
    # cs_composition: regroup
    show sl smile pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show cs_darya amused pioneer far at cs_darya_far_center
    cs_sl "Вот вы где!"
    cs_narrator "Мы обернулись."
    cs_narrator "Возле стола стояла Славя."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer far at cs_darya_far_center
    cs_narrator "Она улыбнулась."
    cs_sl "Ольга Дмитриевна попросила показать вам домик. Вы уже закончили?"
    cs_narrator "Я посмотрела на пустой стакан."
    cs_ls "Кажется, да."
    cs_sl "Тогда пойдёмте!"
    cs_narrator "Семён поднялся вместе с нами."
    show cs_semen smile pioneer far at cs_semen_far_right
    cs_sy "Я тоже могу проводить."
    cs_narrator "Славя покачала головой."
    show sl normal pioneer far at cs_actor_far_left
    cs_sl "Тебя Ольга Дмитриевна просила помочь после обеда. Помнишь?"
    cs_narrator "Он слегка поморщился."
    show cs_semen awkward_alt pioneer far at cs_semen_far_right
    cs_sy "Точно."
    cs_narrator "Я посмотрела на него."
    cs_ls "Трудовая дисциплина, товарищ Семён. Ничего личного."
    cs_sy "Начинается…"
    cs_ls "Партия внимательно следит за выполнением плана."
    cs_narrator "Он махнул рукой."
    show cs_semen smile pioneer far at cs_semen_far_right
    cs_sy "Увидимся потом."
    cs_ls "Увидимся."
    cs_narrator "Я слегка помедлила."
    cs_ls "И, Семён…"
    cs_narrator "Он обернулся."
    show cs_semen thinking_alt pioneer far at cs_semen_far_right
    cs_sy "Что?"
    cs_ls "Пока никому не рассказывай наш разговор. Особенно ту часть, которая касается истории лагеря."
    cs_narrator "Улыбка с его лица исчезла."
    cs_sy "Думаешь, не стоит?"
    cs_ls "Пока мы сами ничего не понимаем, лучше не проверять, насколько местные готовы к подобным откровениям."
    cs_narrator "Семён несколько секунд смотрел на меня."
    cs_narrator "Затем кивнул."
    show cs_semen serious pioneer far at cs_semen_far_right
    cs_sy "Ладно."
    cs_narrator "Мы вышли из-за стола."
    cs_th "Первый контакт установлен."
    cs_th "Уровень взаимного доверия — предварительный."
    cs_th "Результаты наблюдений удовлетворительные."
    return
