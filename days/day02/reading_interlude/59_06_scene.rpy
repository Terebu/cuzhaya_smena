# -*- coding: utf-8 -*-
label cs_day02_reading_06:
    $ save_name = "Чужая смена — Тишина на троих: Другая Лена"
    $ cs_part08_live = False
    $ cs_reading_live = True
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_reading_entry_pov: both continue reading independently.
    $ cs_frame_focus([])
    $ cs_reading_cast = []
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_06:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Прошло ещё немного времени. Я дочитала главу. Перевернула страницу. Потом ещё одну."
    cs_narrator "Дарья тоже читала. Иногда она слегка меняла положение на стуле, иногда поправляла волосы, но в остальном почти не двигалась."
    # cs_director_begin: Both read independently; Lena recalls Moscow
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_493862e91a:
    # cs_director_end
    cs_narrator "Мне было спокойно. И даже немного странно от того, насколько быстро это спокойствие вернулось. В Москве подобные вечера случались довольно часто. Я могла рисовать несколько часов."
    cs_narrator "Могла слушать музыку в наушниках. Могла открыть книгу и настолько увлечься, что забывала проверить сообщения. И при этом совершенно не чувствовала необходимости с кем-нибудь разговаривать. Да, у меня была довольно заметная страница в социальной сети."
    cs_narrator "Много подписчиков. Знакомые. Постоянные уведомления. Но всё это не делало меня человеком, которому непременно нужна компания каждую минуту."
    cs_th "Забавная вещь. Чем больше людей видят тебя на экране, тем меньше они могут знать о том, как ты проводишь самый обыкновенный вечер."
    cs_narrator "Я дочитала предложение."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_three:
    # cs_director_begin: Return to the table conversation
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    label cs_director_check_1915709574:
    # cs_director_end
    cs_narrator "И услышала голос Жени."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Лена."
    cs_narrator "Я подняла голову. Она стояла возле стола."
    cs_ls "Да?"
    cs_narrator "Женя посмотрела на книгу, затем на Дарью. Потом снова на меня."
    cs_mz "Ты давно уже здесь сидишь."
    cs_narrator "Я посмотрела на часы."
    cs_th "А ведь действительно."
    cs_ls "Похоже на то."
    cs_narrator "Она слегка нахмурилась."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И всё это время читаешь?"
    cs_ls "Да."
    cs_narrator "Женя помолчала. Потом произнесла то, чего я совершенно не ожидала."
    cs_mz "А почему вчера ты вела себя совсем иначе?"
    cs_narrator "Я задумалась."
    cs_th "Вот он. Вполне закономерный вопрос."
    cs_narrator "Вчера я пришла в библиотеку, зная, кто такая Женя. Почти сразу начала задавать вопросы. Шутила. Разговаривала слишком много."
    cs_narrator "Словно пыталась проверить, действительно ли этот человек будет вести себя так, как я помнила. А сейчас… Сейчас мне просто хотелось читать. Я положила закладку между страницами."
    cs_narrator "Закрыла книгу. И посмотрела на Женю."
    cs_ls "Наверное, потому что вчера я очень нервничала."
    cs_narrator "Она приподняла бровь."
    cs_mz "Ты?"
    cs_ls "Угу."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Не было похоже."
    cs_narrator "Я немного улыбнулась."
    cs_ls "Знаю."
    cs_narrator "Потом опустила взгляд на книгу."
    cs_ls "Когда происходит слишком много всего сразу, я иногда начинаю говорить без остановки."
    cs_narrator "Женя внимательно слушала."
    cs_ls "Шучу. Задаю вопросы. Комментирую буквально каждую мелочь."
    cs_narrator "Пауза."
    cs_ls "А когда успокаиваюсь, могу несколько часов сидеть над рисунком или книгой почти молча."
    cs_narrator "Дарья повернулась ко мне."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вот этого я, кстати, тоже пока не видела."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Теперь видишь."
    cs_narrator "Она улыбнулась."
    cs_da "И мне нравится."
    cs_narrator "Я слегка смутилась. Не потому, что её слова прозвучали как признание. Скорее потому, что Дарья сказала это без всякой попытки меня поддеть. Просто заметила что-то новое."
    cs_narrator "И ей это понравилось. Я улыбнулась в ответ."
    cs_ls "Хорошо."
    cs_narrator "Женя перевела взгляд с неё на меня."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "То есть ты не всегда такая разговорчивая?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет."
    cs_mz "А вчера?"
    cs_narrator "Я помолчала."
    cs_ls "Вчера я оказалась в незнакомом месте, не понимала, как вернуться домой, и встретила людей, которых почему-то узнавала."
    cs_narrator "Женя нахмурилась. Я продолжила уже спокойнее:"
    cs_ls "Для меня это было слишком много сразу."
    cs_narrator "Некоторое время она молчала. Затем кивнула."
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_reading_cast = ["cs_zhenya", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Понятно."
    cs_narrator "Немного подумала."
    cs_mz "Хотя это всё равно не объясняет половину твоих вчерашних шуток."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Некоторые из них я и сама объяснить не смогу."
    cs_narrator "Дарья улыбнулась. Женя покачала головой. Но больше не выглядела раздражённой. И я неожиданно поняла одну простую вещь."
    cs_th "Мне совершенно не нужно убеждать её, что сегодняшняя Лена настоящая, а вчерашняя — нет. Обе настоящие. Просто я не всегда одинаковая."
    return
