# -*- coding: utf-8 -*-
label cs_day03_126:
    $ save_name = "Чужая смена — День 3: Ждать тоже можно по-разному"
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    cs_narrator "Я закончила есть первой."
    cs_narrator "Отодвинула тарелку."
    cs_narrator "Посмотрела на Женю."
    cs_narrator "Потом на Дашу."
    cs_narrator "Они ещё обедали."
    cs_narrator "Я не стала вставать."
    cs_narrator "Просто устроилась поудобнее и посмотрела в окно."
    cs_narrator "Через некоторое время Дарья подняла взгляд."
    cs_da "Теперь ждёшь?"
    cs_narrator "Я повернулась."
    cs_ls "Да."
    cs_narrator "Она приподняла бровь."
    cs_da "А раньше почему не стала?"
    cs_narrator "Я задумалась."
    cs_ls "Потому что тогда ты ещё не пришла. А сейчас мы уже сидим вместе."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Логично."
    cs_narrator "Женя посмотрела на меня."
    cs_mz "А если я буду есть ещё полчаса?"
    cs_narrator "Я пожала плечами."
    cs_ls "Посижу."
    cs_mz "Зачем?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Не спешу."
    cs_narrator "Она немного помолчала."
    cs_narrator "Потом кивнула."
    cs_mz "Хорошо."
    cs_narrator "И вернулась к еде."
    cs_narrator "Я снова повернулась к окну."
    cs_narrator "Солнечный свет."
    cs_narrator "Тёплая дорожка."
    cs_narrator "Пионеры, спешащие по своим делам."
    cs_narrator "Откуда-то донёсся голос Ульяны."
    cs_narrator "Почти сразу — недовольный ответ Алисы."
    cs_narrator "Я невольно улыбнулась."
    cs_th "Да."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Где-то там кипит обычная лагерная жизнь."
    cs_th "Кто-то спорит."
    cs_th "Кто-то куда-то бежит."
    cs_th "Кто-то наверняка снова решил не выполнять поручение Ольги Дмитриевны."
    cs_th "А мы просто сидим."
    cs_th "И мне это нравится."
    if cs_friend_mz >= 2:
        $ cs_pov_end()
        with cs_sprite_change
        cs_narrator "Женя допила чай."
        cs_narrator "И неожиданно произнесла:"
        cs_mz "Знаешь, Соколова, я сначала думала, что ты будешь всё время болтать."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Я тоже иногда так думаю."
        cs_narrator "Она усмехнулась."
        cs_mz "Но, кажется, с тобой можно нормально посидеть."
        cs_narrator "Я улыбнулась."
        cs_ls "Сочту за комплимент."
        cs_mz "Как хочешь."
        cs_narrator "Пауза."
        cs_narrator "Она слегка улыбнулась."
        cs_mz "Это и был комплимент."
        cs_narrator "Я удивлённо посмотрела на неё."
        cs_th "О."
        cs_th "Вот это уже неожиданно."
        cs_ls "Тогда спасибо."
    else:
        $ cs_pov_end()
        with cs_sprite_change
        cs_narrator "Женя закончила чай."
        cs_narrator "Посмотрела в окно."
        cs_mz "Вроде народу стало меньше."
        cs_narrator "Я кивнула."
        cs_ls "Ага. Кажется, обеденная операция подходит к концу."
        cs_narrator "Она усмехнулась."
        cs_mz "У тебя любое событие — операция."
        cs_narrator "Я улыбнулась."
        cs_ls "Профессиональная привычка делать из обыденности что-нибудь торжественное."
    cs_narrator "Женя взяла книгу."
    cs_narrator "Осторожно поднялась."
    cs_mz "Ладно, мне пора."
    cs_narrator "Я посмотрела на неё."
    cs_ls "В библиотеку?"
    cs_narrator "Она кивнула."
    cs_mz "Да."
    cs_ls "Я немного пройдусь и зайду позже."
    cs_narrator "Женя посмотрела на мою повязку."
    cs_mz "Только без новых приключений."
    cs_narrator "Я улыбнулась."
    cs_ls "Сегодня уже хватит."
    cs_narrator "Она немного помолчала."
    if cs_friend_mz >= 2:
        cs_mz "Книгу я тебе отложила. Приходи, когда освободишься."
        cs_ls "Спасибо."
        cs_mz "Пожалуйста."
    else:
        cs_mz "Придёшь — посмотрим, что у нас есть."
        cs_ls "Хорошо."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она поправила очки."
    cs_narrator "Посмотрела на Дарью."
    cs_mz "До встречи."
    cs_da "Пока."
    cs_ls "До встречи."
    $ cs_actor_exit(["cs_zhenya"])
    with cs_sprite_leave
    label cs_check_day03_126_zhenya_left:
    cs_narrator "Женя направилась к выходу."
    cs_narrator "Я проводила её взглядом."
    cs_th "Хороший получился обед."
    cs_th "Причём без необходимости изображать совершенно другого человека."
    return
