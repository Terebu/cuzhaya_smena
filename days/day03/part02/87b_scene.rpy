# -*- coding: utf-8 -*-
label cs_day03_87b:
    $ save_name = "Чужая смена — День 3: Вежливость как экстремальный спорт"
    label cs_check_day03_87b:
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "Потом на дорожку к столовой."
    cs_ls "Ладно, не будем тебя задерживать. Всё-таки скоро завтрак."
    show cs_semen awkward pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Он приподнял бровь."
    cs_sy "И всё?"
    cs_narrator "Я кивнула."
    cs_ls "И всё."
    cs_narrator "Семён посмотрел на Дарью."
    cs_sy "Она точно нормально себя чувствует?"
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Пока да."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Прекрасно. Пытаюсь проявить элементарную вежливость, а люди уже обсуждают моё состояние здоровья."
    show cs_semen smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Семён рассмеялся."
    cs_sy "Просто непривычно."
    cs_narrator "Я посмотрела на него."
    cs_ls "Привыкай. Сегодня у нас пилотный запуск культурного общения."
    cs_narrator "Он усмехнулся."
    cs_sy "Посмотрим, сколько продержится."
    cs_narrator "Я выдержала паузу."
    cs_narrator "Потом кивнула."
    cs_ls "Разумный скептицизм."
    cs_narrator "Дарья тихо рассмеялась."
    cs_sy "Ладно, увидимся за завтраком."
    cs_ls "Увидимся."
    cs_da "До встречи."
    cs_narrator "Семён махнул рукой."
    cs_th "Вот так."
    cs_th "Никаких происшествий."
    cs_th "Даже немного подозрительно."
    return
