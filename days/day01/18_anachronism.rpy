# -*- coding: utf-8 -*-
# Source: source/day01_part04.md.
label cs_day01_18:
    $ save_name = u"Чужая смена — День 1: Анахронизм"
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    with Dissolve(1.5)
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 1.5 fadein 2.0
    label cs_check_day01_part04_aidpost:
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я узнала медпункт и толкнула Дарью локтем."
    cs_ls "Кстати."
    # cs_darya_stage: present in story
    show cs_darya surprised pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    label cs_check_darya_hold_pause:
    cs_narrator "Я наклонилась ближе, чтобы идущая впереди вожатая нас не услышала."
    cs_ls "Здесь работает очень привлекательная медсестра."
    cs_narrator "Дарья медленно повернула ко мне голову."
    cs_da "Кто?"
    cs_ls "Виола."
    # cs_darya_stage: present in story
    show cs_darya serious pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты её ещё даже не видела."
    cs_ls "Лично — нет."
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Вот именно."
    cs_ls "Предлагаю пока не придираться к способу получения информации."
    cs_narrator "Дарья посмотрела на медпункт."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И это одно из твоих важных знаний о лагере?"
    cs_ls "Исключительно важное."
    cs_da "Среди временных аномалий, возможных повторений событий и неизвестного механизма, который привёз нас сюда, ты решила сообщить мне, что местная медсестра красивая?"
    cs_ls "Необходимо сохранять разнообразие исследовательских направлений."
    cs_narrator "Она покачала головой. Через пару шагов я снова наклонилась к её уху."
    cs_ls "Но вот что действительно интересно."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Наконец-то."
    cs_ls "Насколько я помню, в медпункте должен быть плакат с Алёшенькой."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это кто?"
    cs_ls "Кыштымский карлик. Российская городская легенда о маленьком существе, которое некоторые считали гуманоидом."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо."
    cs_ls "Только история стала известна в 1996 году."
    cs_narrator "Я показала на дорожку под ногами."
    cs_ls "А мы, судя по всему, находимся где-то в восьмидесятых."
    cs_narrator "Мы обе замедлили шаг."
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_doubt fadeout 1.5 fadein 3.0
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_darya_reasoning:
    cs_da "То есть ты предполагаешь, что в лагере, который выглядит как советский лагерь восьмидесятых…"
    cs_ls "Угу."
    label cs_check_day01_part04_hypothesis:
    cs_da "…может находиться изображение события из будущего?"
    cs_ls "Именно."
    # cs_darya_stage: present in story
    show cs_darya serious pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Но ты его пока не видела здесь."
    cs_ls "Верно. Пока это только воспоминание об игре."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тогда возможно, что разработчики просто допустили ошибку."
    cs_ls "Разумеется."
    # cs_darya_stage: present in story
    show cs_darya worried pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И почему тебя это беспокоит?"
    cs_narrator "Я посмотрела на здание медпункта."
    cs_ls "Потому что если плакат действительно висит там, это уже не просто ошибка на нарисованном фоне."
    cs_narrator "Я продолжила тише:"
    cs_ls "На компьютере можно сказать, что художник вставил мем, сценарист пошутил или никто не проверил дату."
    cs_narrator "Я кивнула на настоящее здание."
    cs_ls "Но здесь мы имеем дело с физическим предметом."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Или эпоха здесь вообще ненастоящая."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "Вот за что я тебя ценю. Ты всегда умеешь вовремя ухудшить прогноз."
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_darya_smile:
    cs_ls "Ладно. Запишем плакат в список того, что нужно проверить."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "У тебя появляются здравые мысли."
    cs_ls "Не привыкай."
    cs_narrator "Мы снова двинулись вперёд."
    stop music fadeout 2.5
    cs_th "Автобус, странное знание вожатой, возможные анахронизмы. И Семён уже здесь."
    cs_narrator "Список вопросов рос быстрее, чем число ответов."
    cs_ls "Оставим хотя бы несколько экзистенциальных кризисов на вечер."
    return
