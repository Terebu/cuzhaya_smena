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
    cs_narrator "Мы приблизились к медпункту."
    cs_narrator "Я мгновенно узнала здание."
    cs_narrator "И слегка толкнула Дарью локтем."
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
    cs_narrator "Она покачала головой."
    cs_narrator "Я сделала ещё пару шагов."
    cs_narrator "Потом снова наклонилась к её уху."
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
    cs_narrator "Я задумалась."
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
    cs_narrator "Дарья замедлила шаг."
    cs_narrator "Я тоже."
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
    cs_narrator "Она немного помолчала."
    # cs_darya_stage: present in story
    show cs_darya serious pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Но ты его пока не видела здесь."
    cs_narrator "Я кивнула."
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
    cs_narrator "Дарья замолчала."
    cs_narrator "Я продолжила, значительно тише:"
    cs_ls "На компьютере можно сказать, что художник вставил мем, сценарист пошутил или никто не проверил дату."
    cs_narrator "Я кивнула на настоящее здание."
    cs_ls "Но здесь мы имеем дело с физическим предметом."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Если он действительно существует."
    cs_ls "Вот это и нужно проверить."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А если существует?"
    cs_narrator "Я пожала плечами."
    cs_ls "Тогда у нас появится ещё один признак того, что этот лагерь не совсем соответствует заявленной эпохе."
    # cs_darya_stage: present in story
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Или что эпоха здесь вообще ненастоящая."
    cs_ls "Тоже вариант."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Или что само место устроено совершенно иначе, чем ты предполагаешь."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Вот за что я тебя ценю как собеседника. Ты всегда умеешь своевременно ухудшить прогноз."
    cs_da "Я просто рассматриваю возможности."
    cs_ls "Мы обе из Москвы 2026 года, а сейчас идём по советскому лагерю в пионерской форме. Поводов для вопросов уже достаточно."
    cs_narrator "Дарья посмотрела на себя."
    cs_narrator "Потом на меня."
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_darya_smile:
    cs_da "Справедливо."
    cs_narrator "Я тихо усмехнулась."
    cs_ls "Поэтому пока запишем плакат в список того, что нужно проверить."
    # cs_darya_stage: present in story
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А если окажется, что плаката нет?"
    cs_ls "Тогда вычеркнем. Я вполне допускаю, что моя память тоже не идеальна."
    # cs_darya_stage: present in story
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "У тебя появляются здравые мысли."
    cs_ls "Не привыкай."
    cs_narrator "Мы снова двинулись вперёд."
    stop music fadeout 2.5
    cs_th "Итак."
    cs_th "Первое: автобус."
    cs_th "Второе: странное знание Ольги Дмитриевны."
    cs_th "Третье: возможные анахронизмы."
    cs_th "Четвёртое: Семён действительно здесь."
    cs_narrator "Список вопросов рос значительно быстрее, чем количество ответов."
    cs_narrator "Я вздохнула."
    cs_ls "Оставим хотя бы несколько экзистенциальных кризисов на вечер."
    return
