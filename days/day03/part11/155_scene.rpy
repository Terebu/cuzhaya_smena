# -*- coding: utf-8 -*-
label cs_day03_155:
    $ save_name = "Чужая смена — День 3: Три секунды доверия"
    if cs_day03_dinner_greeting_done:
        return
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    cs_narrator "Женя заметила нас, когда мы подошли на несколько шагов."
    cs_narrator "Она подняла взгляд."
    cs_narrator "Посмотрела сначала на меня."
    cs_narrator "Потом на Дашу."
    cs_mz "Привет."
    cs_narrator "Я улыбнулась."
    cs_ls "Привет."
    cs_da "Добрый вечер."
    cs_narrator "Женя кивнула."
    cs_mz "Добрый."
    cs_narrator "Я остановилась рядом."
    cs_narrator "На мгновение задумалась."
    cs_th "Вообще-то мне хочется её обнять."
    cs_th "Просто по-дружески."
    cs_th "Но с Женей подобные вещи лучше не делать неожиданно."
    cs_th "Личные границы важнее любого моего внезапного порыва. И с Семёном это правило тоже стоило помнить."
    if cs_mz_dinner_friend_on_arrival >= 3 and cs_mz_open_library_invitation_day3:
        cs_narrator "Я немного наклонила голову."
        cs_ls "Женя."
        cs_narrator "Она посмотрела на меня."
        cs_mz "Что?"
        cs_narrator "Я улыбнулась."
        cs_ls "Можно тебя обнять?"
        cs_narrator "Она замерла."
        cs_narrator "Моргнула."
        cs_narrator "Потом посмотрела на Дарью."
        cs_narrator "Та совершенно спокойно стояла рядом."
        cs_narrator "Женя снова повернулась ко мне."
        cs_mz "Ты сейчас серьёзно?"
        cs_narrator "Я кивнула."
        cs_ls "Да."
        cs_narrator "Она немного помолчала."
        cs_mz "С чего вдруг?"
        cs_narrator "Я пожала здоровым плечом."
        cs_ls "Просто захотелось."
        cs_narrator "Женя посмотрела на меня внимательнее."
        cs_ls "Если не хочешь, ничего страшного."
        cs_narrator "Она опустила взгляд."
        cs_narrator "Потом снова подняла."
        cs_narrator "И неожиданно чуть улыбнулась."
        cs_mz "Ладно."
        cs_narrator "Я удивлённо подняла бровь."
        cs_ls "Правда?"
        cs_narrator "Она вздохнула."
        cs_mz "Только недолго."
        cs_narrator "Я улыбнулась."
        cs_ls "Договорились."
        cs_narrator "Я осторожно приобняла её здоровой рукой за плечи."
        cs_narrator "Всего на несколько секунд."
        cs_narrator "Женя сначала немного напряглась."
        cs_narrator "Но отстраняться не стала."
        cs_narrator "Потом тихо сказала:"
        cs_mz "Всё. Хватит."
        label cs_check_day03_155_hug:
        $ cs_mz_hug_allowed_day3 = True
        cs_narrator "Я сразу отпустила."
        cs_ls "Хорошо."
        cs_narrator "Она поправила очки."
        cs_narrator "Посмотрела на меня."
        cs_mz "Ты всегда такая неожиданная?"
        cs_narrator "Я задумалась."
        cs_ls "Только в специально отведённые часы."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Тогда предупреди, когда они закончатся."
        cs_narrator "Я улыбнулась."
        cs_ls "Постараюсь."
        cs_narrator "Она немного помолчала."
        cs_narrator "Потом добавила:"
        cs_mz "И в следующий раз тоже сначала спрашивай."
        cs_narrator "Я кивнула."
        cs_ls "Обязательно."
        cs_narrator "Дарья наблюдала за нами с лёгкой улыбкой."
        cs_narrator "Но ничего не комментировала."
        if not cs_reflective_shot:
            $ cs_pov_begin()
            with cs_sprite_leave
        cs_th "Спасибо тебе, Даша."
        cs_th "Потому что внутри у меня сейчас действительно проходит маленький парад."
        cs_th "С оркестром."
        cs_th "Флагами."
        cs_th "И торжественным докладом об установлении дипломатических отношений с библиотекой."
    elif cs_mz_dinner_friend_on_arrival >= 1:
        $ cs_pov_end()
        with cs_sprite_change
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Чего такая довольная?"
        cs_narrator "Я улыбнулась."
        cs_ls "Хороший день."
        cs_narrator "Она приподняла бровь."
        cs_mz "Даже после твоих приключений?"
        cs_narrator "Я кивнула."
        cs_ls "Особенно после того, как сегодня решила больше не устраивать приключений."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Разумное решение."
        cs_narrator "Я немного помолчала."
        cs_ls "Кстати, спасибо за книгу."
        cs_narrator "Она кивнула."
        cs_mz "Пожалуйста."
        cs_narrator "Я улыбнулась."
        cs_th "Пока этого вполне достаточно."
    else:
        cs_narrator "Я остановилась рядом."
        cs_ls "Как вечер?"
        cs_narrator "Женя пожала плечами."
        cs_mz "Нормально. Только народу многовато."
        cs_narrator "Я посмотрела на толпу возле входа."
        cs_ls "Согласна."
        cs_narrator "Она кивнула."
        cs_mz "Тогда подождём немного."
        cs_narrator "Я улыбнулась."
        cs_ls "Давай."
        cs_th "Пожалуй, не стоит навязывать человеку дружеские жесты, к которым он ещё не привык."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Женя посмотрела на меня."
    cs_narrator "Потом на Дарью."
    cs_mz "Ну что, идём ужинать?"
    cs_narrator "Я кивнула."
    cs_ls "Ради этого и пришли."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "А я думала, Лена пришла проверить, не научился ли Семён прятаться."
    cs_narrator "Я повернулась к ней."
    cs_ls "Дарья, прошу не разглашать детали моих культурно-просветительских мероприятий."
    cs_narrator "Женя тихо фыркнула."
    cs_narrator "И мы направились к очереди."
    $ cs_day03_dinner_greeting_done = True
    return
