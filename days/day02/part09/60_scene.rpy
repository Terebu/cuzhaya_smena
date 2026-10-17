# -*- coding: utf-8 -*-
label cs_day02_60:
    $ save_name = "Чужая смена — День 2: Культурное наследие"
    $ cs_part08_live = False
    $ cs_part09_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    play sound "sound/sfx/dinner_horn_processed.ogg"
    label cs_check_part09_s60:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы успели пройти всего несколько десятков метров, когда над лагерем раздался горн."
    cs_narrator "Я невольно вздрогнула."
    cs_narrator "Не сильно."
    cs_narrator "Но достаточно, чтобы на секунду остановиться."
    cs_ls "О!"
    cs_narrator "Дарья повернулась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я посмотрела в сторону столовой."
    cs_narrator "Потом на солнце."
    cs_ls "Кажется, ужин."
    cs_da "Ты уже научилась различать сигналы?"
    cs_narrator "Я задумалась."
    cs_ls "Этот особенно легко. Желудок переводит синхронно."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на дорожку."
    cs_narrator "И вдруг в голове всплыла мелодия."
    cs_narrator "Старая."
    cs_narrator "Нелепая."
    cs_narrator "До боли знакомая."
    cs_narrator "Такая, которую не слышала уже несколько лет, но почему-то могла вспомнить практически мгновенно."
    cs_th "О нет."
    cs_th "Только не это."
    cs_narrator "Я начала тихо напевать."
    cs_narrator "Сначала едва слышно."
    cs_narrator "Потом немного увереннее."
    cs_ls "Котлетки с макарешками…"
    cs_narrator "Остановилась."
    cs_narrator "Подняла палец."
    cs_ls "Нет, с пюрешкой!"
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Несколько секунд молчала."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена."
    cs_narrator "Я повернулась."
    cs_ls "М?"
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты сейчас серьёзно?"
    cs_narrator "Я широко улыбнулась."
    cs_ls "Абсолютно."
    cs_narrator "Она засмеялась."
    cs_da "Это же какая-то старая интернетная песенка?"
    cs_ls "Именно!"
    cs_narrator "Я торжественно кивнула."
    cs_ls "Культурное наследие русскоязычного интернета."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А я уж подумала, что тебе после падения всё-таки стоит ещё раз показаться Виоле."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Попрошу не оскорблять народное творчество."
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Я продолжила напевать мелодию, уже без слов."
    cs_narrator "Осторожно покачала головой в такт."
    cs_narrator "И неожиданно вспомнила совершенно другое время."
    cs_narrator "Старые сайты."
    cs_narrator "Видео с отвратительным качеством изображения."
    cs_narrator "Шутки, смысл которых невозможно было объяснить человеку, не заставшему их появления."
    cs_narrator "Записи, которые пересылали друзьям просто потому, что кто-то однажды решил сделать нечто максимально бессмысленное."
    cs_th "Господи."
    cs_th "Сколько же всего было."
    cs_narrator "Я остановилась."
    cs_narrator "Приложила здоровую ладонь к щеке."
    cs_ls "Ой."
    cs_narrator "Дарья моментально насторожилась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что? Болит?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Просто олдскулы свело."
    cs_narrator "Она несколько секунд смотрела на меня."
    cs_narrator "Потом медленно улыбнулась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты неисправима."
    cs_ls "Представляешь, меня морально отбросило лет на пятнадцать назад."
    cs_narrator "Дарья задумалась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "В начало десятых?"
    cs_narrator "Я кивнула."
    cs_ls "Угу."
    cs_narrator "Она усмехнулась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты ведь сама из двадцать шестого года."
    cs_ls "Именно поэтому и ностальгирую."
    cs_narrator "Я посмотрела сквозь деревья на лагерь."
    cs_narrator "Здесь всё выглядело так, будто время остановилось ещё раньше."
    cs_narrator "Ни интернета."
    cs_narrator "Ни смартфонов."
    cs_narrator "Ни привычных мне сервисов."
    cs_narrator "Даже музыку нельзя было просто включить в наушниках по дороге."
    cs_narrator "И всё равно в голове неожиданно всплывали воспоминания не о последних годах, а о том старом интернете, который я застала ещё подростком."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А что тебе в нём так нравилось?"
    cs_narrator "Я задумалась."
    cs_ls "Наверное, ощущение, что люди делали всякую ерунду просто потому, что им было весело."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Сейчас тоже делают."
    cs_ls "Конечно. Просто тогда всё казалось каким-то менее серьёзным."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Видео могли снять на что угодно. Монтаж был ужасный. Звук иногда такой, что хотелось пожаловаться на нарушение Женевской конвенции."
    cs_narrator "Дарья засмеялась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Но ты всё равно смотрела?"
    cs_ls "Разумеется."
    cs_narrator "Я немного помолчала."
    cs_ls "А потом даже производство глупостей стало профессиональным."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part09_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Технический прогресс."
    cs_ls "Не все его последствия одинаково полезны человечеству."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я посмотрела на неё."
    cs_th "Надо же."
    cs_th "Мы сейчас идём по советскому лагерю и обсуждаем интернет начала десятых."
    cs_th "Неизвестно, сколько нам ещё здесь находиться."
    cs_th "А я внезапно скучаю по старым мемам."
    cs_narrator "Мозг — удивительная штука."
    cs_da "Пойдём уже. А то твоя культурная программа закончится без ужина."
    cs_narrator "Я посмотрела в сторону столовой."
    cs_ls "Справедливо."
    cs_narrator "Мы направились к зданию."
    cs_narrator "На этот раз обычным шагом."
    cs_narrator "Без подпрыгиваний."
    cs_narrator "Без попыток ускориться."
    cs_narrator "И с совершенно искренним намерением больше сегодня не встречаться с корнями деревьев."
    return
