# -*- coding: utf-8 -*-
label cs_day01_48_a:
    $ save_name = "Чужая смена — День 1: Знакомство"
    show un normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ renpy.music.set_volume(0.24,delay=1.0,channel="music")
    play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 2.5
    cs_narrator "Я сделала небольшой шаг назад, чтобы не загораживать дорогу."
    cs_ls "Слушай, раз уж мы так удачно едва не столкнулись, давай хотя бы познакомимся."
    cs_narrator "Девушка осторожно подняла взгляд."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Давай…"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Лена. Лена Соколова."
    # cs_darya_variety: reaction
    show cs_darya surprise_hand pioneer normal at cs_darya_normal_right
    cs_narrator "Она удивлённо моргнула."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Лена?"
    cs_ls "Угу."
    cs_narrator "Пауза."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Меня тоже Лена зовут."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Затем на Дарью."
    cs_narrator "Медленно кивнула."
    cs_ls "Великолепно. Теперь главное — не потеряться при перекличке."
    show un shy pioneer at cs_actor_left zorder 10
    cs_narrator "Тёзка смущённо улыбнулась."
    $ cs_un_name_known = True
    # cs_speaker: present
    show un shy pioneer at cs_actor_left zorder 10
    cs_un "Да…"
    cs_narrator "Я протянула руку."
    cs_narrator "Она нерешительно посмотрела на неё, затем осторожно пожала."
    cs_ls "Очень приятно."
    show un normal pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Мне тоже."
    cs_narrator "Дарья подошла чуть ближе."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_da "А я Даша."
    show un smile pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show un smile pioneer at cs_actor_left zorder 10
    cs_un "Приятно познакомиться."
    cs_da "Взаимно."
    cs_narrator "На несколько секунд повисла тишина."
    cs_narrator "Я снова обратила внимание на наше внешнее сходство."
    cs_narrator "Фиолетовые волосы."
    cs_narrator "Зелёные глаза."
    cs_narrator "Даже рост не слишком различался."
    cs_narrator "При этом характеры, кажется, были совершенно противоположными."
    cs_narrator "Я указала на свои волосы."
    cs_ls "Забавно получилось."
    cs_narrator "Тёзка вопросительно посмотрела на меня."
    cs_ls "У нас даже волосы почти одного цвета."
    cs_narrator "Она посмотрела на мою причёску."
    cs_narrator "Потом на свою прядь."
    cs_narrator "И едва заметно улыбнулась."
    # cs_speaker: present
    show un smile pioneer at cs_actor_left zorder 10
    cs_un "Правда, похожи."
    cs_da "Особенно глаза."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо, что причёски разные. Иначе нас пришлось бы подписывать."
    cs_narrator "Лена тихо рассмеялась."
    cs_narrator "Я почувствовала, что напряжение немного спало."
    cs_th "Вот."
    cs_th "Уже лучше."
    cs_th "Не обязательно устраивать дипломатический приём. Иногда достаточно обычного знакомства."
    cs_ls "Ты куда шла?"
    show un normal pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "В библиотеку."
    cs_narrator "Я кивнула."
    cs_ls "Любишь читать?"
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Да."
    cs_narrator "Она немного помолчала."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "А ты?"
    cs_ls "Читаю. Хотя чаще рисую."
    cs_narrator "Кажется, последнее её заинтересовало."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Рисуешь?"
    cs_ls "Угу. В основном цифровые рисунки, но карандаши и бумагу тоже никто не отменял."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    cs_narrator "Она задумчиво кивнула."
    # cs_speaker: present
    show un normal pioneer at cs_actor_left zorder 10
    cs_un "Я тоже иногда рисую."
    cs_narrator "Я улыбнулась уже искренне."
    cs_ls "Правда? Тогда у нас, кажется, появилось больше общего, чем одинаковый цвет волос."
    show un smile pioneer at cs_actor_left zorder 10
    cs_narrator "Лена немного смутилась."
    show un shy pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show un shy pioneer at cs_actor_left zorder 10
    cs_un "Наверное."
    cs_ls "Как-нибудь покажешь свои рисунки?"
    cs_narrator "Она ненадолго задумалась."
    # cs_speaker: present
    show un shy pioneer at cs_actor_left zorder 10
    cs_un "Может быть…"
    cs_ls "Только если сама захочешь."
    show un smile pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show un smile pioneer at cs_actor_left zorder 10
    cs_un "Хорошо."
    cs_narrator "Я кивнула."
    cs_narrator "Всё-таки удивительная вещь."
    cs_narrator "Ещё пару часов назад я знала её исключительно как персонажа визуальной новеллы."
    cs_narrator "Знала некоторые события её истории."
    cs_narrator "И считала, что понимаю её характер."
    cs_narrator "А сейчас мы просто разговаривали о рисовании."
    cs_narrator "И, кажется, это было гораздо важнее всех моих знаний о возможных концовках."
    pause 0.6
    cs_narrator "Откуда-то со стороны дорожки раздался знакомый голос."
    cs_sy "Лена!"
    cs_narrator "Я обернулась."
    cs_narrator "Тёзка тоже."
    show un smile pioneer far at cs_actor_left zorder 10
    show cs_darya shrug pioneer far at cs_darya_far_right
    show cs_semen awkward pioneer far at cs_semen_far_right
    # cs_composition: regroup
    show un smile pioneer far at cs_actor_far_left zorder 10
    # cs_composition: regroup
    show cs_darya shrug pioneer far at cs_darya_far_center
    with None
    label cs_check_day01_part09_trio:
    cs_narrator "Семён остановился."
    cs_narrator "Посмотрел сначала на неё."
    cs_narrator "Потом на меня."
    cs_narrator "Затем снова на неё."
    show cs_semen surprised pioneer far at cs_semen_far_right
    cs_sy "Э-э…"
    cs_narrator "Я не удержалась от улыбки."
    cs_ls "Да, Семён?"
    show un normal pioneer far at cs_actor_far_left zorder 10
    # cs_speaker: present
    show un normal pioneer far at cs_actor_far_left zorder 10
    cs_un "Ты меня звал?"
    cs_narrator "Он несколько секунд переводил взгляд между нами."
    cs_sy "Подождите. Вас обеих зовут Лена?"
    cs_narrator "Я приняла совершенно серьёзное выражение лица."
    cs_ls "Верно. Прошу при обращении указывать фамилию во избежание административной путаницы."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer far at cs_darya_far_center
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Семён покачал головой."
    show cs_semen awkward_alt pioneer far at cs_semen_far_right
    cs_sy "Отлично. Теперь вас две."
    cs_ls "Попрошу не говорить так, будто это стихийное бедствие."
    cs_sy "Я пока ничего не говорил!"
    cs_ls "Но выражение лица весьма красноречивое."
    cs_narrator "Тёзка не выдержала и тихо засмеялась."
    cs_narrator "Семён посмотрел на неё."
    cs_narrator "Потом на меня."
    cs_narrator "И тоже усмехнулся."
    show cs_semen smile pioneer far at cs_semen_far_right
    cs_sy "Ладно. Разберётесь сами, кто из вас какая."
    cs_ls "Работа по идентификации населения уже начата."
    cs_narrator "Он махнул рукой."
    cs_sy "Увидимся."
    cs_ls "Пока."
    # cs_speaker: present
    show un normal pioneer far at cs_actor_far_left zorder 10
    cs_un "Пока…"
    hide cs_semen
    # cs_composition: regroup
    show cs_darya amused pioneer far at cs_darya_far_right
    show un smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    with None
    cs_narrator "Он продолжил путь по своим делам."
    cs_narrator "Я посмотрела на тёзку."
    cs_narrator "Она всё ещё улыбалась."
    cs_narrator "Но уже совсем немного."
    cs_ls "Ладно, не будем тебя задерживать."
    # cs_speaker: present
    show un smile pioneer at cs_actor_left zorder 10
    cs_un "Да, мне ещё нужно книгу вернуть."
    cs_ls "Тогда увидимся."
    cs_narrator "Она кивнула."
    label cs_check_day01_un_farewell:
    show un smile pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show un smile pioneer at cs_actor_left zorder 10
    cs_un "Увидимся, Лена."
    cs_narrator "Я улыбнулась."
    cs_ls "Удачи, Лена."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_right
    cs_narrator "Она снова тихо рассмеялась и направилась к библиотеке."
    hide un with Dissolve(0.7)
    # cs_composition: regroup
    show cs_darya amused pioneer normal at cs_darya_normal_center
    stop music fadeout 2.5
    return
