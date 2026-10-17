# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_29:
    $ save_name = "Чужая смена — День 1: План исследования"
    label cs_check_day01_part06_notes:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я достала телефон."
    cs_narrator "Чёрный экран."
    cs_narrator "Никакой реакции."
    cs_narrator "Снова убрала его в карман."
    cs_ls "Надо будет найти способ зарядить."
    cs_narrator "Дарья удивлённо посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Здесь?"
    cs_ls "Теоретически электричество существует."
    cs_da "Но зарядка у тебя с собой?"
    cs_narrator "Я замолчала."
    cs_narrator "Затем медленно посмотрела на неё."
    cs_ls "Хорошее замечание."
    # cs_darya_variety: reaction
    show cs_darya forearm_hold pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты оставила её дома?"
    cs_ls "Вместе с пауэрбанком."
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Прекрасная подготовка к путешествию во времени."
    cs_narrator "Я кивнула."
    cs_ls "Молодец, Лена. Надёжная, как швейцарские часы."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Которые забыли завести?"
    cs_ls "Примерно."
    cs_narrator "Я подошла к столу."
    cs_narrator "На нём лежали карандаш и несколько листов бумаги."
    cs_narrator "Посмотрела на них."
    cs_narrator "Потом на Дарью."
    cs_ls "Хотя кое-что мы всё-таки можем сделать."
    cs_da "Что?"
    cs_narrator "Я взяла карандаш."
    cs_narrator "Села за стол."
    cs_narrator "На верхней части листа написала:"
    cs_narrator "{b}«Совёнок. День первый».{/b}"
    cs_narrator "Ниже провела черту."
    cs_ls "Будем вести записи."
    cs_narrator "Дарья подошла ближе."
    cs_da "Дневник?"
    cs_ls "Скорее журнал наблюдений."
    cs_narrator "Я начала перечислять вслух, одновременно записывая."
    cs_ls "Первое. Автобус номер четыреста десять. Засыпание зимой, пробуждение летом."
    cs_narrator "Новая строка."
    cs_ls "Второе. Здесь находится Семён, который прибыл раньше нас."
    cs_narrator "Третья."
    cs_ls "Третье. Лагерь соответствует знакомым мне локациям и персонажам, но есть отличия."
    cs_narrator "Дарья посмотрела на лист."
    cs_da "Какие отличия мы уже подтвердили?"
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Я подняла карандаш."
    cs_ls "Мы сами. Во-первых, в оригинальной истории нас здесь вообще не было."
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Логично."
    cs_ls "Во-вторых, Ольга Дмитриевна назвала меня по имени ещё до того, как мы представились."
    cs_narrator "Дарья стала серьёзнее."
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да. Это было странно."
    cs_ls "И, в-третьих…"
    cs_narrator "Я замолчала."
    cs_narrator "Посмотрела на окно."
    cs_ls "Пока хватит."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему?"
    cs_ls "Не хочу записывать неподтверждённые предположения как факты."
    cs_narrator "Дарья одобрительно кивнула."
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Правильно."
    cs_narrator "Я отложила карандаш."
    cs_ls "Теперь у нас есть настоящий план."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И какой?"
    cs_ls "Не потерять этот листок."
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Очень амбициозно."
    cs_ls "С малого начинаются великие достижения."
    stop music fadeout 2.5
    return
