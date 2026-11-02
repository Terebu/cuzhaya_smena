# -*- coding: utf-8 -*-
# Source: source/day01_part02.md.
label cs_day01_09:
    $ save_name = u"Чужая смена — День 1: Домик вожатой"
    # cs_presence_keep: hide sl
    $ cs_director_scene("bg ext_house_of_mt_day")
    scene bg ext_house_of_mt_day
    with Dissolve(1.5)
    window show dissolve
    stop music fadeout 2.0
    show sl normal pioneer at cs_actor_left
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Славя остановилась возле одного из домиков."
    cs_narrator "Я сразу узнала крыльцо, окна, дверь. И опять стало неуютно."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Сейчас, кажется, будет ещё интереснее."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему?"
    cs_ls "Познакомимся с человеком, который, скорее всего, решит, что мы две потерявшиеся пионерки."
    cs_narrator "Славя поднялась по ступенькам."
    cs_sl "Ольга Дмитриевна?"
    cs_narrator "Изнутри раздался женский голос."
    cs_mt "Да?"
    $ renpy.music.set_volume(0.35, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 2.0 fadein 2.0
    cs_narrator "По спине прошёл холодок, несмотря на жару."
    cs_narrator "Славя приоткрыла дверь."
    cs_sl "Тут две девушки приехали."
    cs_mt "Какие ещё девушки?"
    cs_narrator "Я тихо обратилась к Дарье."
    cs_ls "Вот сейчас начинается импровизация."
    # cs_darya_variety: reaction
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты же говорила, что знаешь сюжет почти наизусть."
    cs_ls "Знаю."
    cs_narrator "Я посмотрела на дверь."
    cs_ls "Только в сюжете приехал один Семён."
    cs_narrator "Потом указала сначала на себя, затем на неё."
    cs_ls "А нас две. Небольшое отклонение от технического задания."
    pause 0.5
    $ cs_olga_seen = True
    cs_narrator "Из домика вышла женщина."
    # cs_composition: regroup
    show sl normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show mt normal pioneer far at cs_actor_far_right
    # cs_composition: regroup
    show cs_dasha_winter shrug far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_trio:
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Белая рубашка, красный галстук, тёмная юбка. Ольгу Дмитриевну я узнала сразу."
    cs_narrator "Она остановилась на крыльце, оглядела Славю, Дарью и наконец меня."
    cs_narrator "Особенно долго её взгляд задержался на зимней куртке у меня в руках."
    # cs_camp_emotion: text reaction
    show mt smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Добрый день."
    cs_narrator "Я слегка подняла ладонь."
    cs_ls "Здравствуйте."
    cs_narrator "Я решила начать с самого простого."
    cs_ls "У нас небольшая логистическая проблема."
    show mt surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Какая именно?"
    cs_narrator "Я указала через плечо в сторону ворот."
    cs_ls "Мы сели в автобус зимой."
    cs_narrator "Затем посмотрела на яркое солнце."
    cs_ls "А приехали сюда. Летом."
    pause 0.6
    cs_narrator "Ольга Дмитриевна молчала."
    cs_narrator "Я подняла куртку."
    cs_ls "Доказательство номер один."
    cs_narrator "Показала свитер."
    cs_ls "Номер два."
    cs_narrator "Затем слегка выставила вперёд ботинок."
    cs_ls "И памятник моему выдающемуся умению подбирать гардероб по погоде."
    show sl smile pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Позади меня Славя тихо хихикнула."
    cs_narrator "Ольга Дмитриевна посмотрела на неё."
    show sl normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя моментально приняла серьёзный вид."
    cs_ls "И ещё наш автобус до сих пор стоит возле ворот."
    cs_mt "Ваш автобус?"
    cs_ls "Четыреста десятый."
    stop music fadeout 1.5
    pause 1.0
    cs_narrator "На этот раз Ольга Дмитриевна медленно перевела взгляд на меня. Славя удивлялась, а вожатая будто что-то вспомнила."
    cs_narrator "Что-то, связанное с номером автобуса."
    $ renpy.music.set_volume(0.35, delay=1.0, channel="music")
    play music cs_day_music_mystery fadeout 2.0 fadein 3.0
    cs_ls "Странно."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Не сводя глаз с Ольги Дмитриевны, я ответила:"
    cs_ls "Кажется, четыреста десятый ей знаком."
    cs_narrator "После короткого молчания вожатая заговорила."
    label cs_check_day01_name:
    cs_mt "Лена, давайте для начала зайдём внутрь."
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.2, delay=1.5, channel="ambience")
    pause 1.5
    cs_narrator "Я замерла и подняла взгляд."
    cs_ls "Простите."
    cs_narrator "Теперь остановилась уже она."
    cs_mt "Что?"
    cs_ls "Как вы меня сейчас назвали?"
    show mt surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она нахмурилась."
    # cs_camp_emotion: text reaction
    show mt angry pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Лена."
    pause 1.5
    cs_narrator "Мы обе молчали. Славя посмотрела на вожатую, Дарья — на меня."
    cs_narrator "Я сделала один шаг к крыльцу."
    cs_ls "Славя вам моё имя сказала?"
    show sl surprise pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя сразу покачала головой."
    cs_sl "Нет."
    cs_ls "Точно?"
    # cs_camp_emotion: text reaction
    show sl normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Точно. Я даже не знала, как тебя зовут."
    cs_narrator "Я снова посмотрела на вожатую. Несколько секунд мы стояли друг напротив друга."
    $ renpy.music.set_volume(0.22, delay=1.0, channel="music")
    play music cs_day_music_unknown fadeout 2.0 fadein 3.0
    label cs_check_day01_tension:
    cs_ls "Вот теперь интересно."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что именно?"
    cs_narrator "Сарказм перестал помогать."
    cs_ls "Кажется, мы добрались до событий, которых в оригинальной истории не было."
    pause 1.0
    cs_narrator "Вожатая смотрела на меня, будто собиралась что-то сказать, но медлила."
    return
