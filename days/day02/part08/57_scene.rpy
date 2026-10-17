# -*- coding: utf-8 -*-
label cs_day02_57:
    $ save_name = "Чужая смена — День 2: Непрошеные определения"
    $ cs_part07_live = False
    $ cs_part08_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part08_s57:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Разговор постепенно вернулся к обычным лагерным делам."
    cs_narrator "Семён рассказал, что после нашего возвращения от ворот ему пришлось помочь перенести несколько скамеек."
    cs_sy "Славя сказала, что к вечеру всё должно быть готово."
    cs_ls "А ты уже работаешь в отделе материально-технического обеспечения."
    cs_sy "Меня просто попросили помочь."
    cs_ls "Вот так всегда и начинается карьера."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он усмехнулся."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А твоя закончилась на объявлении?"
    cs_ls "Временно. Художнику предоставлен оплачиваемый отпуск по состоянию здоровья."
    cs_da "Без оплаты."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Не разрушай мечту."
    cs_narrator "Она рассмеялась."
    cs_narrator "Семён отложил карандаш."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А вообще объявление хорошее получилось. Я сначала думал, что мы просто напишем пару слов на листе."
    cs_ls "Это ты недооценил мощь графического дизайна."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Я просто не ожидал, что мы будем обсуждать размер каждой буквы."
    cs_narrator "Я кивнула."
    cs_ls "Зато теперь знаешь, что творческие люди способны усложнить даже самое простое задание."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А потом обвинить бумагу."
    cs_ls "Бумага не предоставила возможности отмены."
    cs_narrator "Семён рассмеялся."
    cs_narrator "Некоторое время мы снова сидели молча."
    cs_narrator "Я посмотрела на Семёна."
    cs_narrator "И неожиданно подумала, насколько странно изменилось моё отношение к нему за эти два дня."
    cs_narrator "В Москве он был героем истории, которую я знала практически наизусть."
    cs_narrator "Человеком, чьи поступки можно было обсуждать, оценивать, критиковать."
    cs_narrator "Иногда смеяться над его решениями."
    cs_narrator "Иногда спорить с другими поклонниками игры о том, почему он поступил именно так."
    cs_narrator "А теперь Семён сидел рядом."
    cs_narrator "Держал в руках обычный карандаш."
    cs_narrator "Уставал после поручений."
    cs_narrator "Беспокоился о возвращении домой."
    cs_narrator "И вполне успешно отвечал на мои шутки."
    cs_th "Кажется, я наконец перестаю видеть перед собой заранее написанный сюжет."
    cs_narrator "Я вспомнила, как раньше называла его главным героем."
    cs_narrator "Сейчас это словосочетание показалось не особенно удачным."
    cs_th "Он ведь не обязан играть роль, которую я для него придумала."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Что?"
    cs_narrator "Я моргнула."
    cs_ls "А?"
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты на меня смотришь так, будто сейчас опять что-нибудь скажешь."
    cs_narrator "Я улыбнулась."
    cs_ls "Вообще-то хотела сказать спасибо."
    show cs_semen surprised pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он удивился."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "За что?"
    cs_narrator "Я немного подумала."
    cs_ls "За то, что сегодня пошёл с нами к воротам. И не стал отмахиваться от наших предположений."
    cs_narrator "Он пожал плечами."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Мне самому нужно понять, что здесь происходит."
    cs_ls "Знаю. Но всё равно спасибо."
    cs_narrator "Он посмотрел на меня."
    cs_narrator "Потом слегка улыбнулся."
    cs_sy "Не за что."
    cs_narrator "Дарья наблюдала за нашим разговором."
    cs_narrator "И тоже улыбалась."
    cs_narrator "Несколько секунд было тихо."
    cs_narrator "Потом Семён неожиданно спросил:"
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А можно теперь и мне кое-что сказать?"
    cs_narrator "Я насторожилась."
    cs_ls "Зависит от степени разрушительности."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты ужасно странная."
    cs_narrator "Я задумалась."
    cs_ls "Заключение принято."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Но с тобой хотя бы не скучно."
    cs_narrator "Я посмотрела на него."
    cs_narrator "Потом на Дарью."
    cs_narrator "Она едва заметно пожала плечами."
    cs_da "Я бы сказала примерно то же самое."
    cs_narrator "Я медленно положила здоровую руку на грудь."
    cs_ls "Надо же. Два положительных отзыва за один день."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Только не записывай."
    cs_ls "Поздно. Уже сохранено во внутреннем архиве."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он рассмеялся."
    cs_narrator "И я рассмеялась вместе с ним."
    cs_th "Да."
    cs_th "Наверное, именно так и появляются друзья."
    cs_th "Не после особенного признания."
    cs_th "Не после какого-нибудь обязательного события."
    cs_th "Просто однажды замечаешь, что рядом с человеком тебе стало спокойно."
    cs_narrator "Я посмотрела на площадь."
    cs_narrator "Потом снова на Семёна."
    cs_th "Главный герой?"
    cs_th "Нет."
    cs_th "Просто Семён."
    cs_th "И этого вполне достаточно."
    return
