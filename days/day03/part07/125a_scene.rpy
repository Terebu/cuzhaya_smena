# -*- coding: utf-8 -*-
label cs_day03_125a:
    $ save_name = "Чужая смена — День 3: Художницы обсуждают недостатки человечества"
    cs_narrator "Я слегка подняла руку."
    cs_ls "Лен!"
    $ cs_frame_focus(["cs_zhenya", "cs_darya", "un"])
    with cs_sprite_change
    if renpy.showing("un"):
        show un shy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Тихонова повернулась."
    cs_un "Да?"
    cs_narrator "Я улыбнулась."
    cs_ls "Если хочешь, у нас есть свободное место."
    cs_narrator "Она посмотрела на стол."
    cs_narrator "Потом на Женю."
    cs_narrator "На Дарью."
    cs_narrator "Снова на меня."
    cs_un "Можно?"
    cs_narrator "Я кивнула."
    cs_ls "Конечно."
    if renpy.showing("un"):
        show un shy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она осторожно подошла."
    cs_un "Спасибо."
    cs_narrator "Устроилась рядом."
    cs_narrator "Мы немного помолчали."
    cs_narrator "Потом я посмотрела на неё."
    cs_ls "Как рисунок?"
    if renpy.showing("un"):
        show un smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Тихонова чуть улыбнулась."
    cs_un "Лучше."
    if cs_un_day3_art_talk:
        cs_ls "Получилось изменить передний план?"
    else:
        cs_ls "Удалось продолжить?"
    cs_narrator "Она кивнула."
    if cs_un_day3_art_talk:
        cs_un "Да. Как ты советовала."
    else:
        cs_un "Да. Я немного переделала рисунок."
    cs_narrator "Я улыбнулась."
    cs_ls "И тебе самой нравится?"
    cs_un "Да."
    cs_narrator "Я кивнула."
    cs_ls "Тогда отлично."
    cs_narrator "Женя посмотрела на нас."
    cs_mz "Вы про вчерашний концерт?"
    cs_narrator "Тихонова кивнула."
    cs_un "Я его рисовала."
    cs_narrator "Женя посмотрела на меня."
    if cs_un_day3_art_talk:
        cs_mz "И ты, конечно, уже успела дать художественную консультацию."
    else:
        cs_mz "Вы уже успели обсудить рисунок?"
    cs_narrator "Я приложила здоровую ладонь к груди."
    if cs_un_day3_art_talk:
        cs_ls "Между прочим, исключительно по запросу."
    else:
        cs_ls "Утром только посмотрели. Не стали отвлекать."
    if renpy.showing("un"):
        show un smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Тихонова тихо улыбнулась."
    if cs_un_day3_art_talk:
        cs_un "Правда. Я сама попросила."
    else:
        cs_un "Я тогда ещё не закончила. Сейчас уже можно показать."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Тогда ладно."
    cs_narrator "Дарья посмотрела на Тихонову."
    cs_da "А что ты хочешь рисовать дальше?"
    cs_narrator "Та немного задумалась."
    cs_un "Не знаю. Может быть, что-нибудь в лагере."
    cs_ls "Советую выбрать место подальше от корней."
    cs_narrator "Все посмотрели на меня."
    cs_narrator "Я вздохнула."
    cs_ls "Простите. Профессиональная травма."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Тихонова тоже тихо улыбнулась."
    if cs_un_sketch_invite_day3:
        cs_narrator "Тихонова посмотрела на меня внимательнее."
        cs_un "А насчёт того, чтобы порисовать вместе…"
        cs_narrator "Я улыбнулась."
        cs_ls "Да?"
        cs_narrator "Она немного помолчала."
        cs_un "Я подумала, что можно было бы выбрать какое-нибудь место в лагере. И попробовать нарисовать его по-разному."
        cs_narrator "Я заинтересовалась."
        cs_ls "Мне нравится."
        cs_un "Правда?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Даже интересно, насколько разными получатся наши рисунки."
        cs_narrator "Она улыбнулась."
        cs_un "Тогда, может быть, после обеда?"
        cs_narrator "Я немного подумала."
        cs_ls "Я уже обещала Жене зайти в библиотеку. Но можем договориться на более позднее время."
        cs_narrator "Женя спокойно кивнула."
        cs_mz "Я тебя там не на весь день запираю."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Какое облегчение. А я уже начала опасаться пожизненного литературного заключения."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_narrator "Тихонова тихо рассмеялась."
        cs_un "Тогда можем встретиться ближе к вечеру. Если будешь свободна."
        cs_narrator "Я кивнула."
        cs_ls "Давай. Только место выберем там, где есть тень."
        cs_narrator "Она улыбнулась."
        cs_un "Хорошо."
        $ cs_un_sketch_time_agreed_day3 = True
        $ cs_un_sketch_plan_discussed_day3 = True
    elif cs_friend_un >= 2:
        cs_narrator "Тихонова посмотрела на меня."
        cs_un "А ты сегодня ещё будешь рисовать?"
        cs_narrator "Я задумалась."
        cs_ls "Не планировала. Но карандаш в руки взять хотелось бы."
        cs_narrator "Она слегка улыбнулась."
        cs_un "Может, как-нибудь порисуем вместе?"
        cs_narrator "Я заинтересовалась."
        cs_ls "С удовольствием."
        cs_narrator "Она кивнула."
        cs_un "Тогда позже договоримся."
        $ cs_un_sketch_invite_day3 = True
    else:
        cs_narrator "Тихонова спокойно закончила обед."
        cs_narrator "Иногда она поглядывала на меня."
        cs_narrator "Похоже, ей уже было проще находиться рядом."
        cs_narrator "Но разговоров о новых рисунках она больше не начинала."
        cs_narrator "Я тоже не торопила."
        cs_th "Хорошие знакомства не обязаны развиваться с такой скоростью, будто завтра экзамен по дружбе."
    cs_narrator "Тихонова допила чай."
    cs_narrator "Осторожно встала."
    cs_un "Спасибо за компанию."
    cs_narrator "Я улыбнулась."
    cs_ls "Не за что."
    cs_narrator "Женя кивнула."
    cs_narrator "Дарья тоже попрощалась."
    cs_narrator "Тихонова отнесла поднос."
    $ cs_actor_exit(["un"])
    with cs_sprite_leave
    cs_narrator "И направилась к выходу."
    return
