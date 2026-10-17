# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_17:
    $ save_name = u"Чужая смена — День 1: Мир за пределами экрана"
    $ cs_director_scene("bg ext_house_of_mt_day")
    scene bg ext_house_of_mt_day
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_home fadeout 1.5 fadein 3.0
    $ renpy.music.set_volume(0.45, delay=1.0, channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_camp_center:
        play ambience cs_day_camp_center fadeout 1.0 fadein 2.0
    label cs_check_day01_part04_outside:
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "На улице оказалось ещё жарче."
    cs_narrator "Но теперь хотя бы не возникало ощущения, что я медленно превращаюсь в варёного человека."
    cs_narrator "Я шла по лагерной дорожке в пионерской форме и время от времени поглядывала на себя."
    cs_narrator "Красный галстук."
    cs_narrator "Юбка."
    cs_narrator "Белая рубашка."
    cs_narrator "Лёгкие туфли."
    cs_narrator "Всё это по-прежнему напоминало невероятно качественный косплей."
    cs_narrator "С одним существенным отличием."
    cs_narrator "Здесь никто не косплеил."
    cs_narrator "Для окружающих это была совершенно обычная одежда."
    cs_narrator "Обычный лагерь."
    cs_narrator "Обычное лето."
    cs_narrator "И, вероятно, совершенно обычный Советский Союз."
    # cs_director_begin: REFLECTIVE_SHOT: Camp without modern devices
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_8e5548a32d:
    # cs_director_end
    cs_narrator "Я посмотрела на проходящих мимо ребят."
    cs_narrator "Они разговаривали."
    cs_narrator "Смеялись."
    cs_narrator "Кто-то нёс мяч."
    cs_narrator "Двое мальчишек спорили из-за какой-то ерунды."
    cs_narrator "Никаких смартфонов."
    cs_narrator "Никаких беспроводных наушников."
    cs_narrator "Никакой привычной современной одежды."
    cs_th "Потрясающе."
    cs_th "Технический прогресс официально взял отпуск."
    # cs_director_begin: Return to direct interaction: Camp without modern devices
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_cbaf0ce5ec:
    # cs_director_end
    cs_ls "М-да."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что теперь?"
    cs_ls "Осознаю масштаб технологического отката."
    # cs_darya_stage: present in story
    show cs_darya serious pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы здесь меньше часа."
    cs_ls "А у меня телефон разрядился ещё до прибытия. Для человека из двадцать первого века это уже существенное осложнение жизни."
    cs_da "Ты же не очень любишь общаться."
    cs_ls "Именно поэтому интернет мне особенно нужен."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Идеальная система: можно общаться с людьми, физически с ними не встречаясь."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья усмехнулась."
    show bg ext_houses_day with Dissolve(1.5)
    # cs_director_begin: REFLECTIVE_SHOT: World extending beyond painted backgrounds
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_a2b3df439b:
    # cs_director_end
    cs_narrator "Мы прошли мимо нескольких домиков."
    cs_narrator "Я практически автоматически узнавала каждый поворот."
    cs_narrator "И это продолжало беспокоить."
    cs_narrator "Когда играешь в визуальную новеллу, фон существует только в пределах экрана."
    cs_narrator "Здесь всё было иначе."
    cs_narrator "Можно было повернуть голову."
    cs_narrator "Заглянуть за домик."
    cs_narrator "Посмотреть в окно."
    cs_narrator "Прикоснуться к дереву."
    cs_narrator "Мир не заканчивался там, где художник не нарисовал следующую локацию."
    hide bg
    show cs_camp_path_day zorder -10 with Dissolve(1.5)
    cs_narrator "Я на мгновение замедлила шаг."
    cs_th "Вот этого игра не показывала."
    cs_th "А здесь оно есть."
    cs_narrator "От такой простой мысли становилось одновременно интересно и не по себе."
    # cs_director_begin: Return to direct interaction: World extending beyond painted backgrounds
    $ cs_frame_focus(["mt", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_96adca2052:
    # cs_director_end
    cs_narrator "Я приблизилась к Дарье."
    cs_ls "Знаешь, это очень неприятное ощущение."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Какое?"
    cs_ls "Когда знаешь место, в котором никогда не была."
    cs_narrator "Она посмотрела вперёд."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне это чувство знакомо."
    cs_narrator "Я повернулась к ней."
    cs_narrator "И тут же вспомнила, с кем именно разговариваю."
    cs_ls "А. Ну да."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья слегка усмехнулась."
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Именно."
    cs_narrator "Несколько секунд мы шли молча."
    cs_ls "У тебя хотя бы есть опыт существования внутри довольно запутанной истории."
    # cs_darya_stage: present in story
    show cs_darya worried pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Не уверена, что это преимущество."
    cs_ls "Сейчас выясним."
    cs_narrator "Я бросила взгляд на Ольгу Дмитриевну, которая шла немного впереди."
    cs_narrator "Она выглядела совершенно спокойно."
    cs_th "Две странные девушки. Неизвестный автобус. Непонятные объяснения."
    cs_th "И всё равно главное — успеть на обед."
    cs_narrator "В некотором смысле я даже восхищалась её способностью сохранять рабочее настроение."
    return
