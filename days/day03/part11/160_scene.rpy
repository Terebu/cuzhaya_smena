# -*- coding: utf-8 -*-
label cs_day03_160:
    $ save_name = "Чужая смена — День 3: За ужином тоже происходят события"
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    cs_narrator "Ужин подходил к концу. Даша поставила пустой стакан на поднос. Женя аккуратно взяла свою книгу. Я ещё немного посидела."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Надо же."
    cs_narrator "Женя посмотрела на меня."
    $ cs_pov_end()
    with cs_sprite_change
    cs_mz "Ты чего задумалась?"
    cs_narrator "Я улыбнулась."
    cs_ls "Подсчитываю количество людей, с которыми сегодня успела поговорить."
    cs_narrator "Она приподняла бровь."
    cs_mz "И много?"
    cs_ls "Уже сбилась со счёта."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась. Пока я доедала, Даша успела рассказать Жене, как я обозвала идиотом героя романа. Конца истории я не слышала."
    cs_mz "Тебе бы сначала с героями спорить научиться молча."
    cs_narrator "Я замерла. Повернулась к Даше. Она немедленно рассмеялась."
    cs_ls "Женщина."
    cs_da "Что?"
    cs_ls "Ты рассказала Жене про идиота?"
    cs_narrator "Даша попыталась сохранить серьёзное лицо. Не получилось."
    cs_da "Возможно."
    cs_narrator "Я медленно покачала головой."
    cs_ls "Прекрасно. Теперь компрометирующие сведения о моей читательской деятельности распространяются между учреждениями."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "А ты думала, никто не узнает?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Больше всего меня беспокоит скорость передачи информации."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Даша рассмеялась. Я тоже улыбнулась."
    cs_th "И ведь самое интересное — Женя уже сама с удовольствием участвует в подобных разговорах. Пожалуй, за эту неделю я узнаю о ней больше, чем могла бы представить в первый день."
    if cs_friend_mi >= 2 and cs_mi_followup_invitation_day3:
        $ cs_frame_focus(["cs_zhenya", "cs_darya", "mi"])
        with cs_sprite_change
        cs_narrator "Неподалёку появилась Мику. Она заметила наш стол. Улыбнулась."
        cs_mi "Лена! Даша! Вы ещё здесь?"
        cs_narrator "Я повернулась."
        cs_ls "Привет. Да, заканчиваем ужин."
        cs_narrator "Мику подошла чуть ближе."
        cs_mi "Я как раз хотела сказать, что почти закончила то вступление, которое мы сегодня обсуждали! Только после ужина уже поздновато снова начинать репетицию, поэтому, если хотите, завтра можно будет послушать. Я думаю, вам понравится, хотя, конечно, ещё можно кое-что изменить…"
        $ cs_actor_exit(["cs_zhenya"])
        with cs_sprite_leave
        $ cs_frame_focus(["cs_darya", "mi", "dv"])
        with cs_sprite_change
        cs_narrator "Алиса, проходившая неподалёку, усмехнулась."
        cs_dv "Мику, только не начинай переделывать его по новой."
        if renpy.showing("mi"):
            show mi laugh pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Мику рассмеялась."
        cs_mi "Не буду! Ну, наверное."
        cs_ls "Тогда завтра обязательно послушаем."
        cs_narrator "Мику обрадовалась."
        cs_mi "Отлично!"
        $ cs_mi_followup_target_day = 4
    if cs_friend_dv >= 2 and cs_dv_followup_invitation_day3:
        $ cs_actor_exit(["mi", "cs_zhenya"])
        with cs_sprite_leave
        $ cs_frame_focus(["cs_darya", "dv"])
        with cs_sprite_change
        cs_narrator "Алиса посмотрела на меня."
        cs_dv "Соколова."
        cs_narrator "Я повернулась."
        cs_ls "Да?"
        cs_narrator "Она кивнула в сторону клуба."
        cs_dv "Завтра загляни, если будет время. Хочу одну штуку показать."
        cs_narrator "Я приподняла бровь."
        cs_ls "Это сейчас было приглашение?"
        if renpy.showing("dv"):
            show dv grin pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Алиса усмехнулась."
        cs_dv "Можешь считать как хочешь. Только не опаздывай, если придёшь."
        cs_ls "Договорились."
        cs_narrator "Она кивнула."
        cs_dv "Вот и хорошо."
        cs_narrator "Даша посмотрела на меня."
        cs_da "У тебя действительно скоро будет расписание."
        cs_narrator "Я вздохнула."
        cs_ls "Да. Похоже, меня всё-таки втянули в художественную самодеятельность."
        $ cs_dv_followup_target_day = 4
    $ cs_actor_exit(["mi", "dv"])
    with cs_sprite_leave
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    cs_narrator "Женя посмотрела на нас, потом на часы."
    cs_mz "Ладно. Допью чай — и в библиотеку."
    if cs_mz_evening_help_day3:
        cs_ls "Тогда я только за книгой сбегаю — и к тебе."
        cs_narrator "Женя посмотрела на меня."
        cs_mz "Только не забывай, что обещала помогать с книгами, а не устраивать собрание художественного совета."
        cs_ls "Конечно. Исключительно библиотечная деятельность."
        cs_narrator "Даша усмехнулась."
        cs_da "Посмотрим, надолго ли тебя хватит."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Дарья, не подрывай доверие работодателя к сотруднику до начала первой смены."
        cs_narrator "Женя рассмеялась."
        cs_mz "Соколова, ты уже начинаешь."
        cs_narrator "Я подняла здоровую руку."
        cs_ls "Всё. Молчу."
    else:
        cs_narrator "Я улыбнулась."
        cs_ls "Приятного вечера, Женя."
        cs_narrator "Она кивнула."
        cs_mz "Спасибо."
        cs_narrator "Даша тоже пожелала ей хорошего вечера."
        $ cs_frame_focus(["cs_zhenya", "cs_darya"])
        with cs_sprite_change
        cs_narrator "Женя придвинула к себе чашку и раскрыла книгу. Я посмотрела на них обеих."
        cs_th "Хороший получился вечер. И, пожалуй, лучше не пытаться немедленно сделать его ещё лучше."
    $ cs_day03_dinner_finished = True
    return
