# -*- coding: utf-8 -*-
label cs_day01_58:
    $ save_name = "Чужая смена — День 1: На каком экране?"
    $ renpy.music.set_volume(0.23,delay=1.0,channel="music")
    play music "sound/music/into_the_unknown.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/library_day.ogg":
        play ambience "sound/ambiences/library_day.ogg" fadeout 1.5 fadein 1.5
    cs_narrator "Я осторожно положила ладони на спинку ближайшего стула."
    cs_ls "Представь, что существует история."
    cs_narrator "Женя ничего не ответила."
    cs_narrator "Я продолжила:"
    cs_ls "Не книга. Компьютерная игра, в которой человек читает текст, разговаривает с другими героями и иногда принимает решения."
    show mz normal glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Компьютерная?"
    cs_ls "Да."
    cs_narrator "Она прищурилась."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И при чём здесь библиотека?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "В той истории был пионерский лагерь «Совёнок»."
    cs_narrator "Пауза."
    cs_ls "С воротами, площадью, столовой, клубами. И этой библиотекой."
    cs_narrator "Женя медленно выпрямилась."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Допустим."
    cs_ls "Там была Ольга Дмитриевна. Славя. Алиса. Ульяна."
    cs_narrator "Она перестала двигаться."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Ты это к чему?"
    cs_narrator "Я посмотрела ей в глаза."
    cs_ls "Там была и девушка по имени Женя."
    cs_narrator "Женя несколько секунд смотрела на меня."
    cs_narrator "Затем перевела взгляд на Дарью."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Это что, розыгрыш?"
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_da "Нет."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Тогда откуда вы знаете всех этих людей?"
    cs_narrator "Я медленно выдохнула."
    cs_ls "Я не утверждаю, что понимаю, как это возможно. Но в моём времени действительно существует игра с очень похожим лагерем."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "В твоём времени?"
    cs_narrator "Я кивнула."
    cs_ls "Я родилась значительно позже того года, который сейчас указан в ваших газетах."
    cs_narrator "Женя нахмурилась сильнее."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Подожди."
    cs_narrator "Она сняла очки."
    cs_narrator "Аккуратно положила их на стол."
    cs_narrator "Посмотрела на меня уже совершенно серьёзно."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Ты хочешь сказать, что приехала сюда из будущего?"
    cs_ls "Да."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И что я, по-твоему, существую в какой-то компьютерной игре?"
    cs_narrator "Вот теперь я замолчала."
    cs_narrator "Потому что услышала собственное объяснение с её стороны."
    cs_narrator "И оно действительно звучало ужасно."
    cs_narrator "Я медленно покачала головой."
    cs_ls "Нет. Я не хочу сказать, что ты ненастоящая."
    cs_narrator "Женя посмотрела на меня внимательнее."
    cs_ls "Я говорю только о том, что видела очень похожую историю. И в ней был человек, которого я знала под твоим именем."
    cs_narrator "Небольшая пауза."
    cs_ls "А с тобой я познакомилась только сегодня."
    cs_narrator "Женя молчала."
    cs_narrator "Дарья тоже."
    cs_narrator "За окном тихо шелестели деревья."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И ты действительно во всё это веришь?"
    cs_narrator "Я задумалась."
    cs_ls "Я верю в то, что видела своими глазами."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "А доказательства есть?"
    cs_narrator "Я машинально коснулась кармана с телефоном."
    cs_narrator "Потом убрала руку."
    cs_ls "Возможно. Но сейчас моё главное доказательство даже не включается."
    cs_narrator "Женя посмотрела на мой карман."
    cs_narrator "Затем снова на меня."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Очень удобно."
    cs_narrator "Я кивнула."
    cs_ls "Согласна. На твоём месте я бы тоже не поверила."
    cs_narrator "Это, кажется, удивило её больше всего."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Тогда зачем рассказываешь?"
    cs_narrator "Я медленно выдохнула."
    cs_ls "Потому что ты спросила. А придумывать ещё одну нелепую историю мне уже надоело."
    cs_narrator "Женя несколько секунд молчала."
    cs_narrator "Затем снова надела очки."
    cs_narrator "Посмотрела на дверь."
    cs_narrator "На часы."
    cs_narrator "И наконец произнесла:"
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Ладно."
    cs_narrator "Я подняла бровь."
    cs_ls "Ладно?"
    show mz angry glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz angry glasses pioneer at cs_actor_left zorder 10
    cs_mz "Я пока не верю ни одному слову."
    cs_narrator "Пауза."
    show mz normal glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Но если вы действительно хотите что-то выяснить, то хотя бы перестаньте разговаривать загадками."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Немного подумала."
    cs_narrator "И кивнула."
    cs_ls "Справедливое требование."
    cs_narrator "Женя указала на стул."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Тогда с самого начала."
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_right
    cs_narrator "Та едва заметно улыбнулась."
    cs_th "Ну вот."
    cs_th "Похоже, знакомство всё-таки состоялось."
    cs_th "И теперь придётся объяснять, как обычная поездка за продуктами закончилась в советской библиотеке."
    cs_narrator "Я осторожно придвинула стул."
    cs_ls "Хорошо."
    cs_narrator "Небольшая пауза."
    cs_ls "Только история действительно длинная."
    cs_narrator "Женя посмотрела на часы."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Тогда говори коротко. Библиотеку я всё равно скоро закрываю."
    cs_narrator "Я едва заметно улыбнулась."
    cs_ls "Есть, товарищ хранитель книжного фонда."
    cs_narrator "Женя закатила глаза."
    show mz angry glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz angry glasses pioneer at cs_actor_left zorder 10
    cs_mz "Лена…"
    cs_ls "Всё. Начинаю."
    return
