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
    cs_narrator "Ни пластиковых окон, ни зарядных устройств, ни роутера, который я машинально поискала взглядом."
    cs_narrator "Деревянная мебель. Кровати. Тумбочки. Книги и журналы. Старенький радиоприёмник."
    cs_narrator "В музее каждый предмет поставили бы ради достоверности. Здесь этими вещами пользовались, не подозревая, что однажды они станут ретро."
    cs_th "Практически музей. Только экспонаты пока не знают, что они экспонаты."
    cs_narrator "Мой взгляд остановился на знакомом плакате. Фантомас."
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
    cs_narrator "Дарья посмотрела на плакат, потом на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Этого человека не существовало. Подозрительный тип. Я бы за ним присматривала."
    cs_mt "Это актёр."
    cs_ls "Именно так подозрительные люди обычно и объясняют своё появление."
    cs_narrator "Славя, стоявшая у двери, прикрыла рот рукой."
    cs_ls "Не смейся. Если ночью он начнёт разгуливать по лагерю, я предупреждала."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Пять минут назад ты рассказывала о множественных реальностях."
    cs_ls "Одно другому не мешает."
    stop music fadeout 2.0
    cs_narrator "Я положила куртку и свитер на ближайший стул. Вожатая посмотрела на стопку одежды, затем на мои ботинки."
    cs_mt "Вы действительно приехали в этом?"
    cs_ls "Угу."
    cs_narrator "За окном солнце заливало зелень."
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
    cs_narrator "Точно. Для меня — история, для неё — обычная жизнь."
    cs_narrator "Я посмотрела на отрывной календарь: крупное число и месяц, а года нигде не было."
    cs_narrator "Журналы, мебель, одежда Слави — всё указывало на Советский Союз."
    cs_narrator "Не исторический парк, а страну, которой для меня давно не существовало."
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
    cs_narrator "Дарья молчала. Славя тоже притихла."
    cs_narrator "Я пока решила не отвечать: фраза «мы приехали из 2026 года» вряд ли помогла бы установить доверие."
    cs_ls "Думаю, к этому вопросу лучше вернуться чуть позже."
    # cs_camp_emotion: text reaction
    show mt sad pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Лена…"
    cs_ls "Серьёзно. Мне бы для начала перестать выглядеть как человек, который заблудился по дороге на зимнюю рыбалку."
    cs_narrator "Я приподняла ногу. Тяжёлый ботинок в июльскую жару был убедительнее любых объяснений."
    cs_ls "Нам бы какую-нибудь летнюю одежду."
    return
