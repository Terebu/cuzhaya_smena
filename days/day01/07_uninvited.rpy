# -*- coding: utf-8 -*-
# Source: source/day01_part02.md.
label cs_day01_07:
    $ save_name = u"Чужая смена — День 1: Неожиданное знакомство"
    hide screen cs_day01_pending
    window show dissolve
    $ renpy.music.set_volume(0.35, delay=1.5, channel="ambience")
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_part02_gate:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Славя несколько секунд смотрела на меня с тем выражением, которое обычно появляется у человека, когда незнакомка совершенно неожиданно называет его по имени."
    cs_narrator "А ведь она даже представиться не успела."
    cs_narrator "Я слегка подняла руку."
    cs_ls "Привет. Тебя ведь Славя зовут?"
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она моргнула."
    cs_sl "Да… Славя."
    cs_ls "Отлично. Пока действительность придерживается технической документации."
    cs_sl "Простите?"
    cs_ls "Ничего. Мысли вслух."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Очень убедительно."
    cs_narrator "Я незаметно ткнула её локтем."
    cs_narrator "Славя перевела взгляд с меня на Дарью, затем обратно."
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Вы только приехали?"
    cs_ls "Ага. Буквально только что."
    cs_narrator "Я обернулась и указала на автобус."
    cs_ls "На четыреста десятом."
    cs_narrator "Славя тоже посмотрела на него."
    cs_narrator "На мгновение мне показалось, что она удивилась сильнее, чем следовало."
    # cs_camp_emotion: text reaction
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "На автобусе?"
    cs_ls "Угу. Причём поездка получилась весьма познавательной."
    cs_narrator "Я подняла куртку со свитером, затем выставила вперёд тяжёлый зимний ботинок. На фоне зелёной травы он смотрелся нелепо."
    cs_ls "Выехали мы зимой. Приехали летом. Очень удобно, если планируешь отпуск без предварительного согласования."
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя посмотрела на наши вещи, потом на автобус."
    cs_sl "Но сейчас же июль."
    cs_ls "Вот именно. А минут двадцать назад у меня за окном лежал снег."
    cs_narrator "Она озадаченно нахмурилась, пытаясь найти разумное объяснение."
    cs_sl "Может, вы приехали издалека?"
    cs_ls "Настолько издалека, что там другой сезон?"
    pause 0.6
    # cs_camp_emotion: text reaction
    show sl shy pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Ну… нет."
    cs_ls "Вот и я пока не могу подобрать подходящий регион."
    cs_narrator "Дарья поправила сумку на плече."
    # cs_darya_variety: reaction
    show cs_dasha_winter explaining normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы обе уснули в автобусе."
    cs_narrator "Славя повернулась к ней."
    # cs_camp_emotion: text reaction
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Обе?"
    cs_da "Да."
    cs_sl "И проснулись уже здесь?"
    cs_da "Именно."
    cs_narrator "Я подняла указательный палец."
    cs_ls "И ещё один любопытный момент. Водитель отсутствует."
    $ renpy.music.set_volume(0.15, delay=2.0, channel="music")
    cs_narrator "Мы со Славей обернулись. Четыреста десятый стоял у дороги: открытые двери, пустой салон."
    cs_narrator "Словно всегда был частью местного пейзажа."
    # cs_camp_emotion: text reaction
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Может быть, водитель просто отошёл?"
    cs_ls "Возможно."
    cs_narrator "Я пожала плечами."
    cs_ls "Правда, он мог уйти ещё зимой. Тогда поисковая операция несколько осложняется."
    cs_ls "Да, понимаю. Сейчас я выгляжу как человек, которому желательно сначала измерить температуру."
    # cs_darya_variety: reaction
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И проверить голову."
    cs_ls "Спасибо за поддержку."
    cs_da "Всегда пожалуйста."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя тихо рассмеялась. Смех был живой. На экране так не бывает."
    cs_ls "В общем, если всё здесь хотя бы примерно соответствует моим предположениям, нам нужно к Ольге Дмитриевне."
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "К Ольге Дмитриевне?"
    cs_narrator "И тут я поняла: второй раз подряд назвала человека, которого вроде бы не должна знать."
    cs_ls "Да."
    cs_sl "Вы её знаете?"
    cs_ls "Нет."
    cs_sl "Но знаете имя?"
    cs_ls "Получается, что так."
    cs_sl "Откуда?"
    cs_narrator "Я открыла рот, закрыла и посмотрела на Дарью. Та спокойно наблюдала."
    cs_th "Предательница."
    cs_ls "Очень длинная история."
    cs_sl "Насколько длинная?"
    cs_ls "Если без подробностей — часов на двадцать чтения."
    cs_narrator "Славя явно не поняла. И её можно было понять."
    cs_ls "Пока предлагаю считать это необъяснённым обстоятельством."
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Желание помочь всё-таки победило любопытство."
    # cs_camp_emotion: text reaction
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Хорошо. Тогда давайте я отведу вас к вожатой!"
    $ renpy.music.set_volume(0.35, delay=2.0, channel="music")
    cs_ls "Вот. Именно такое предложение я и надеялась услышать."
    cs_narrator "Славя развернулась к воротам."
    cs_sl "Только вам, наверное, лучше снять тёплую одежду. Сегодня очень жарко."
    cs_narrator "Я посмотрела на куртку со свитером, потом на свои ботинки."
    cs_ls "С ботинками будет сложнее."
    cs_da "Можешь ходить босиком."
    cs_ls "И познакомиться с местным медпунктом после первого же осколка стекла? Благодарю, пока воздержусь."
    cs_narrator "Я остановилась."
    cs_th "Медпункт. Виола."
    cs_narrator "Я усмехнулась, вспомнив ещё один знакомый образ."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Ничего. Вспомнила местную систему здравоохранения."
    cs_narrator "Я кивнула в сторону Слави."
    cs_ls "Идём."
    return
