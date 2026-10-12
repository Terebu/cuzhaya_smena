# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_28:
    $ save_name = "Чужая смена — День 1: Без свидетелей"
    label cs_check_day01_part06_private:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="music")
    play music cs_day_music_think fadeout 2.0 fadein 3.0
    cs_narrator "Я подошла к окну."
    cs_narrator "Снаружи колыхались ветви деревьев."
    cs_narrator "По дорожке прошли две девочки в пионерской форме."
    cs_narrator "Они о чём-то разговаривали и смеялись."
    cs_narrator "Всё выглядело настолько обыденно, что на мгновение захотелось просто принять происходящее."
    cs_narrator "Летний лагерь."
    cs_narrator "Комната на двоих."
    cs_narrator "Знакомая девушка рядом."
    cs_narrator "Никаких срочных дел."
    cs_narrator "Никаких уведомлений."
    cs_narrator "Никаких рабочих сообщений."
    cs_th "Отпуск мечты."
    cs_th "Если не считать того, что домой вернуться пока невозможно."
    cs_narrator "Дарья присела на кровать."
    show cs_darya worried pioneer normal at cs_darya_normal_center
    cs_da "Лен."
    cs_narrator "Я повернулась."
    cs_ls "М?"
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_center
    cs_da "Ты ведь что-то ещё не рассказала Семёну."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Немного помолчала."
    cs_ls "Да."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Почему?"
    cs_narrator "Я отошла от окна и села напротив."
    cs_ls "Потому что он пока едва справляется с тем, что здесь оказался."
    cs_da "А мы?"
    cs_ls "Мы тоже."
    # cs_darya_variety: reaction
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_center
    cs_narrator "Дарья сложила руки на коленях."
    cs_da "Тогда почему ты выглядишь так, будто знаешь, что делать?"
    cs_narrator "Я задумалась."
    cs_narrator "Хороший вопрос."
    cs_ls "Наверное, потому, что знаю, чего делать пока не стоит."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Например?"
    cs_ls "Рассказывать всем подряд, что мы из будущего. Пытаться проверить каждое событие из игры. И уж тем более принимать какие-либо серьёзные решения на основании чужих концовок."
    cs_narrator "Дарья кивнула."
    cs_da "А что насчёт возвращения?"
    cs_narrator "Я опустила взгляд."
    cs_ls "Пока не знаю."
    # cs_darya_variety: reaction
    show cs_darya surprised pioneer normal at cs_darya_normal_center
    cs_da "Совсем?"
    cs_ls "Знаю некоторые варианты из оригинальной истории. Но ни один из них нельзя считать инструкцией."
    cs_narrator "Она немного помолчала."
    cs_da "Ты боишься?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Можно было ответить привычной шуткой."
    cs_narrator "Сказать, что ситуация находится под контролем специально созданной комиссии."
    cs_narrator "Или что партия ещё не утвердила план эвакуации."
    cs_narrator "Но почему-то не захотелось."
    label cs_check_day01_part06_fear:
    cs_ls "Да, Даш."
    cs_narrator "Она подняла глаза."
    show cs_darya worried pioneer normal at cs_darya_normal_center
    cs_da "Я тоже."
    cs_narrator "Мы несколько секунд молчали."
    cs_narrator "За окном пели птицы."
    cs_narrator "Я провела ладонью по волосам."
    cs_ls "Только паника нам не поможет."
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_center
    cs_da "Согласна."
    cs_ls "Поэтому предлагаю действовать последовательно. Сначала выясняем дату. Потом исследуем лагерь. Проверяем, что совпадает с известной мне историей, а что нет."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "И ищем способ вернуться?"
    cs_ls "Обязательно."
    cs_narrator "Дарья кивнула."
    cs_narrator "Затем спросила:"
    cs_da "А если придётся остаться здесь надолго?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Тогда будем решать эту проблему, когда она действительно возникнет."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    cs_narrator "Она слабо улыбнулась."
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_center
    cs_da "Звучит разумно."
    cs_ls "Я иногда умею."
    return
