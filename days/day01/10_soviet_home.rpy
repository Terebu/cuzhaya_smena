# -*- coding: utf-8 -*-
# Source: source/day01_part03.md.
label cs_day01_10:
    $ save_name = u"Чужая смена — День 1: Советский быт"
    hide screen cs_day01_pending
    hide screen cs_phone
    $ day_time()
    $ persistent.sprite_time = "day"
    $ cs_director_scene("bg int_house_of_mt_day")
    scene bg int_house_of_mt_day
    with Dissolve(1.5)
    play ambience cs_day_cabin fadeout 1.0 fadein 2.0
    window show dissolve
    $ renpy.music.set_volume(0.45, delay=1.0, channel="ambience")
    if renpy.music.get_playing(channel="music") != cs_day_music_think:
        $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
        play music cs_day_music_think fadeout 1.5 fadein 2.0
    show mt normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_part03_inside:
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mt", "sl", "cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы с Дарьей вошли в домик."
    # cs_director_begin: REFLECTIVE_SHOT: Counsellor cabin and historic objects
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_2c552e9788:
    # cs_director_end
    cs_narrator "И вот здесь ощущение путешествия во времени стало особенно отчётливым."
    cs_narrator "Никаких пластиковых окон."
    cs_narrator "Никаких зарядных устройств."
    cs_narrator "Никакого роутера, который я почти машинально поискала взглядом."
    cs_narrator "Деревянная мебель. Кровати. Тумбочки. Книги и журналы. Старенький радиоприёмник."
    cs_narrator "Всё выглядело не как музей Советского Союза, где каждый предмет тщательно расставлен ради исторической достоверности."
    cs_narrator "Здесь этими вещами просто пользовались."
    cs_narrator "И никто, вероятно, даже не задумывался, что однажды всё это станут называть ретро."
    cs_narrator "Я медленно осмотрелась."
    cs_th "Неплохо."
    cs_th "Практически музей."
    cs_th "Только экспонаты пока не знают, что они экспонаты."
    cs_narrator "И тут мой взгляд остановился на плакате."
    cs_narrator "Фантомас."
    cs_narrator "Я несколько секунд смотрела на знакомое лицо."
    # cs_director_begin: Return to direct interaction: Counsellor cabin and historic objects
    $ cs_frame_focus(["mt", "sl", "cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_a45e77b705:
    # cs_director_end
    cs_narrator "Потом совершенно серьёзно указала на него пальцем."
    cs_ls "Этого человека в реальности не было. Самозванец."
    show mt surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Ольга Дмитриевна замерла."
    cs_narrator "Дарья посмотрела на плакат."
    cs_narrator "Потом на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я повторила, уже спокойнее и понятнее."
    cs_ls "Этого человека не существовало. Подозрительный тип. Я бы за ним присматривала."
    cs_mt "Это актёр."
    cs_ls "Именно так подозрительные люди обычно и объясняют своё появление."
    cs_narrator "Славя, стоявшая у двери, прикрыла рот рукой."
    cs_narrator "Я заметила."
    cs_ls "Не смейся. Если ночью он начнёт разгуливать по лагерю, я предупреждала."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Пять минут назад ты рассказывала о множественных реальностях."
    cs_ls "Одно другому не мешает."
    stop music fadeout 2.0
    cs_narrator "Я сняла с плеча зимнюю куртку и аккуратно положила её на ближайший стул."
    cs_narrator "Следом туда отправился свитер."
    cs_narrator "Ольга Дмитриевна посмотрела на образовавшуюся стопку одежды."
    cs_narrator "Потом на мои ботинки."
    cs_mt "Вы действительно приехали в этом?"
    cs_ls "Угу."
    cs_narrator "Я посмотрела в окно."
    cs_narrator "Снаружи солнце заливало зелень."
    cs_ls "Там была зима. Настоящая. Снег, холод, серое небо. Всё как положено."
    cs_narrator "Я указала на окно."
    cs_ls "А здесь, судя по всему, ударники труда досрочно выполнили план по производству лета."
    cs_narrator "Ольга Дмитриевна нахмурилась."
    cs_mt "Какой ещё план?"
    cs_ls "Неважно. Неудачная попытка объяснить погоду."
    cs_narrator "Я замолчала."
    # cs_director_begin: REFLECTIVE_SHOT: History versus present reality
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_53a69c5550:
    # cs_director_end
    cs_narrator "Точно."
    cs_narrator "Для меня всё это было историей."
    cs_narrator "Для неё — обычной жизнью."
    cs_narrator "Я посмотрела на отрывной календарь: крупное число и месяц, а года нигде не было."
    cs_narrator "Затем на журналы."
    cs_narrator "На оформление комнаты."
    cs_narrator "На одежду Слави."
    cs_narrator "Если происходящее соответствовало оригинальной игре, мы действительно могли находиться в Советском Союзе."
    cs_narrator "Не на реконструкции."
    cs_narrator "Не на тематическом фестивале."
    cs_narrator "Не в историческом парке."
    cs_narrator "А в стране, которая для меня давно перестала существовать."
    cs_th "Хотя сначала неплохо бы установить дату."
    # cs_director_begin: Return to direct interaction: History versus present reality
    $ cs_frame_focus(["mt", "sl", "cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_96e1923c75:
    # cs_director_end
    cs_narrator "Я повернулась к вожатой."
    cs_ls "Ольга Дмитриевна, а какой сейчас год?"
    show mt surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она посмотрела на меня с ещё большим подозрением."
    cs_mt "Ты серьёзно?"
    cs_ls "К сожалению."
    cs_mt "Ты не знаешь, какой сейчас год?"
    cs_ls "Я знаю, какой был до автобуса."
    cs_narrator "Вот теперь она окончательно перестала улыбаться."
    cs_mt "И какой же?"
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Она молчала."
    cs_narrator "Славя тоже притихла."
    cs_narrator "Я решила пока не отвечать."
    cs_narrator "Не потому, что боялась немедленного визита представителей органов."
    cs_narrator "Хотя перспектива объяснять человеку из прошлого, почему в моём кармане лежит смартфон из двадцать первого века, выглядела весьма сомнительной."
    cs_narrator "Просто фраза «мы приехали из 2026 года» сейчас явно не способствовала бы установлению взаимного доверия."
    cs_ls "Думаю, к этому вопросу лучше вернуться чуть позже."
    # cs_camp_emotion: text reaction
    show mt sad pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Лена…"
    cs_ls "Серьёзно. Мне бы для начала перестать выглядеть как человек, который заблудился по дороге на зимнюю рыбалку."
    cs_narrator "Я слегка приподняла ногу."
    cs_narrator "Тяжёлый ботинок в июльскую жару смотрелся как памятник неправильному планированию."
    cs_ls "Нам бы какую-нибудь летнюю одежду."
    return
