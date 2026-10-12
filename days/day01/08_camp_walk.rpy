# -*- coding: utf-8 -*-
# Source: source/day01_part02.md.
label cs_day01_08:
    $ save_name = u"Чужая смена — День 1: Территория лагеря"
    hide sl
    # cs_composition: regroup
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    scene cs_camp_path_day with Dissolve(1.5)
    window show dissolve
    $ renpy.music.set_volume(0.55, delay=1.0, channel="music")
    play music cs_day_music_daily fadeout 2.0 fadein 3.0
    $ renpy.music.set_volume(0.55, delay=1.5, channel="ambience")
    play ambience cs_day_camp_center fadeout 1.0 fadein 2.0
    label cs_check_day01_walk:
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_narrator "Мы прошли через ворота."
    cs_narrator "И вот здесь ощущение нереальности стало ещё сильнее."
    cs_narrator "До этого я могла смотреть на лагерь как на декорацию."
    cs_narrator "Как на очень качественную реконструкцию."
    cs_narrator "Или, в конце концов, как на необычайно убедительный сон."
    cs_narrator "Но теперь всё вокруг было слишком живым."
    cs_narrator "Солнечный свет пробивался сквозь листья."
    cs_narrator "Где-то пахло нагретой древесиной."
    cs_narrator "Издалека доносились голоса."
    cs_narrator "Кто-то смеялся."
    cs_narrator "В одном из зданий хлопнула дверь."
    cs_narrator "На дорожке лежали мелкие камешки."
    cs_narrator "Не текстура."
    cs_narrator "Не нарисованный фон."
    cs_narrator "Настоящие камни."
    cs_narrator "Я намеренно замедлила шаг и провела подошвой по асфальту."
    cs_narrator "Шероховатый."
    cs_narrator "Совершенно обычный."
    cs_narrator "Дарья заметила моё движение."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "Проверяешь?"
    cs_ls "Угу."
    cs_da "И как?"
    cs_ls "Пока мир успешно проходит тест на существование."
    # cs_darya_variety: reaction
    show cs_dasha_winter smile normal at cs_darya_normal_center
    cs_narrator "Она чуть улыбнулась."
    show sl normal pioneer at cs_actor_left
    # cs_composition: regroup
    show cs_dasha_winter smile normal at cs_darya_normal_right
    cs_narrator "Славя обернулась."
    cs_sl "Вы что-то сказали?"
    cs_ls "Нет, всё хорошо."
    cs_narrator "Я ускорила шаг."
    cs_narrator "Мы пошли дальше."
    cs_narrator "Я смотрела по сторонам, испытывая странную смесь любопытства и очень нехорошего предчувствия."
    cs_narrator "Потому что знала эти места."
    cs_narrator "Вот эта дорожка."
    cs_narrator "Эти деревья."
    cs_narrator "Там должна быть площадь."
    cs_narrator "Дальше — столовая."
    cs_narrator "Клубы."
    cs_narrator "Домики."
    cs_narrator "Медпункт."
    cs_narrator "Библиотека."
    cs_narrator "Я знала карту лагеря."
    cs_narrator "Но знание карты совершенно не помогало принять тот факт, что сейчас я по ней иду."
    cs_narrator "Я приблизилась к Дарье."
    cs_ls "Знаешь, это очень странное чувство."
    # cs_darya_variety: reaction
    show cs_dasha_winter thinking normal at cs_darya_normal_right
    cs_da "Какое?"
    cs_ls "Когда знаешь место, в котором никогда не была."
    cs_narrator "Она посмотрела вперёд."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    cs_da "Мне это чувство знакомо."
    cs_narrator "Я повернулась к ней."
    cs_narrator "И тут же вспомнила, с кем разговариваю."
    cs_ls "А. Ну да."
    # cs_darya_variety: reaction
    show cs_dasha_winter smile normal at cs_darya_normal_right
    cs_narrator "Дарья слегка усмехнулась."
    cs_da "Именно."
    hide sl with dissolve
    # cs_composition: regroup
    show cs_dasha_winter smile normal at cs_darya_normal_center
    cs_narrator "Некоторое время мы шли молча."
    cs_ls "У тебя хотя бы имеется опыт существования внутри весьма запутанной истории."
    # cs_darya_stage: present in story
    show cs_dasha_winter worried normal at cs_darya_normal_center
    cs_da "Не уверена, что это преимущество."
    cs_ls "Сейчас проверим."
    cs_narrator "Я бросила взгляд на Славю."
    cs_narrator "Она шагала впереди, совершенно спокойно ведя нас через лагерь."
    cs_narrator "Для неё всё происходящее, вероятно, выглядело обычным летним днём."
    cs_narrator "Две странно одетые девушки."
    cs_narrator "Непонятный автобус."
    cs_narrator "Несколько нелепых объяснений."
    cs_th "Ничего особенного."
    cs_th "Рядовая смена в пионерском лагере."
    cs_narrator "Я едва заметно покачала головой."
    return
