# -*- coding: utf-8 -*-
label cs_day02_03:
    $ save_name = "Чужая смена — День 2: «Совёнок» без пионеров"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day at cs_early_morning
    # cs_presence_keep: hide cs_darya
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    play music "sound/music/feeling_good.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_s03:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Снаружи было прекрасно."
    cs_narrator "И совершенно непривычно."
    cs_narrator "Вчера «Совёнок» встретил нас шумом, разговорами и бесконечными попытками окружающих выяснить, откуда мы взялись."
    cs_narrator "Сегодня всё было иначе."
    cs_narrator "Пустые дорожки."
    cs_narrator "Роса на траве."
    cs_narrator "Солнце, которое только начинало прогревать воздух."
    cs_narrator "Ни Алисы."
    cs_narrator "Ни Ульяны."
    cs_narrator "Ни Слави, появляющейся с очередным поручением."
    cs_narrator "Ни Ольги Дмитриевны, пытающейся организовать весь лагерь одновременно."
    cs_narrator "Даже Семён, похоже, ещё спал."
    cs_th "Вот это уже интересно."
    cs_th "«Совёнок» без населения."
    cs_th "Редкая возможность спокойно осмотреть декорации."
    cs_narrator "Я остановилась на крыльце."
    cs_narrator "Сделала несколько глубоких вдохов."
    cs_narrator "Воздух был прохладным."
    cs_narrator "Пахло травой, влажной землёй и соснами."
    cs_narrator "Никаких автомобильных выхлопов."
    cs_narrator "Никакого городского гула."
    cs_narrator "Никакого соседского ремонта в семь утра."
    cs_th "Москва, конечно, прекрасный город."
    cs_th "Но в вопросах утренней тишины у неё серьёзная конкуренция."
    cs_narrator "Я сошла с крыльца."
    cs_narrator "Размяла плечи."
    cs_narrator "Несколько раз повернула корпус."
    cs_narrator "Разогрела колени и голеностоп."
    cs_narrator "Потом сделала пару лёгких приседаний и наклонов."
    cs_narrator "Тело постепенно просыпалось."
    cs_th "Ну что, Соколова."
    cs_th "Проверим качество местной дорожной инфраструктуры."
    cs_narrator "Я начала с лёгкого бега."
    cs_narrator "Не торопясь."
    cs_narrator "Первые минуты просто привыкала к поверхности."
    cs_narrator "Дорожки здесь были не особенно ровными. Где-то попадались корни деревьев, где-то мелкие камешки, а после ночной прохлады отдельные участки оставались влажными."
    cs_narrator "Поэтому на скорость я пока не работала."
    cs_narrator "Бежала спокойно."
    cs_narrator "Следила за дыханием."
    cs_narrator "За шагом."
    cs_narrator "За тем, как постепенно разогреваются мышцы."
    cs_narrator "И неожиданно поняла, насколько мне этого не хватало."
    cs_narrator "Вчера весь день приходилось думать."
    cs_narrator "Куда мы попали?"
    cs_narrator "Почему именно сюда?"
    cs_narrator "Что делать с телефоном?"
    cs_narrator "Как объяснять происходящее Семёну?"
    cs_narrator "Стоит ли доверять Ольге Дмитриевне?"
    cs_narrator "А ещё — как разговаривать с людьми, которых раньше знала только по визуальной новелле."
    cs_narrator "Слишком много вопросов."
    cs_narrator "Слишком мало ответов."
    cs_narrator "А здесь всё было просто."
    cs_narrator "Вдох."
    cs_narrator "Выдох."
    cs_narrator "Следующий шаг."
    cs_narrator "Поворот."
    cs_narrator "Ещё несколько метров."
    cs_narrator "Никаких временных аномалий в голове."
    cs_narrator "Только дорога под ногами."
    cs_th "Вот за что я люблю бег."
    cs_th "Хотя бы полчаса можно не пытаться понять устройство мироздания."
    return
