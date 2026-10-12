# -*- coding: utf-8 -*-
label cs_day01_31:
    $ save_name = "Чужая смена — День 1: Незваные гости"
    show dv normal pioneer far at cs_actor_left
    # cs_composition: regroup
    show cs_darya smile pioneer normal at cs_darya_normal_right
    show us grin pioneer far at cs_actor_right
    # cs_composition: regroup
    show dv normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show us grin pioneer far at cs_actor_far_right
    # cs_composition: regroup
    show cs_darya smile pioneer far at cs_darya_far_center
    show cs_darya shrug pioneer far at cs_darya_far_center
    label cs_check_day01_part07_guests:
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/int_cabin_day.ogg":
        play ambience "sound/ambiences/int_cabin_day.ogg" fadeout 1.5 fadein 2.0
    cs_narrator "На пороге стояли две девушки."
    cs_narrator "Точнее, девушка и девочка."
    show dv smile pioneer far at cs_actor_far_left
    show us smile pioneer far at cs_actor_far_right
    cs_narrator "Рыжеволосая Алиса смотрела на меня с нескрываемым любопытством. Ульяна выглядывала из-за её плеча и улыбалась так, будто заранее придумала какую-нибудь пакость."
    show dv surprise pioneer far at cs_actor_far_left
    cs_dv "Привет. Вы новенькие?"
    cs_narrator "Я окинула обеих взглядом."
    cs_ls "Судя по тому, что вы уже пришли знакомиться, информация распространяется быстро."
    show dv smile pioneer far at cs_actor_far_left
    cs_narrator "Алиса усмехнулась."
    cs_dv "А ты забавная."
    cs_ls "Иногда. По праздникам."
    cs_narrator "Ульяна заглянула внутрь."
    show us grin pioneer far at cs_actor_far_right
    cs_us "А вас правда двое?"
    cs_narrator "Дарья подошла ко мне."
    show cs_darya shrug pioneer far at cs_darya_far_center
    cs_da "Правда."
    cs_narrator "Ульяна посмотрела на её волосы, затем на мои."
    cs_us "Ого! У вас волосы крашеные?"
    cs_narrator "Я опустила взгляд на фиолетовую прядь."
    cs_ls "Есть такое."
    cs_us "А у тебя?"
    cs_da "Тоже."
    show us smile pioneer far at cs_actor_far_right
    cs_us "Круто!"
    cs_narrator "Алиса сложила руки на груди."
    cs_dv "Я Алиса. Это Ульянка."
    cs_us "Эй!"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Лена. А это Даша."
    cs_da "Дарья."
    show us grin pioneer far at cs_actor_far_right
    cs_us "Вы откуда приехали?"
    cs_narrator "Я на секунду задумалась."
    cs_ls "Из Москвы."
    show dv surprise pioneer far at cs_actor_far_left
    cs_dv "Правда? И как там?"
    cs_th "Хороший вопрос."
    cs_th "Смотря о какой Москве спрашивать."
    cs_ls "Шумно. Очень много людей, машин и рекламы."
    cs_dv "Рекламы?"
    cs_ls "Неважно. Большой город, одним словом."
    cs_narrator "Дарья бросила на меня короткий взгляд."
    cs_narrator "Поняла."
    cs_narrator "Не стоит превращать первое знакомство в лекцию о разнице эпох."
    cs_narrator "Алиса осмотрела комнату."
    show dv smile pioneer far at cs_actor_far_left
    cs_dv "Ну, ладно. Просто хотели посмотреть, кто тут поселился."
    cs_ls "Инспекция жилого фонда?"
    show dv surprise pioneer far at cs_actor_far_left
    cs_dv "Чего?"
    cs_ls "Ничего. Проверка пройдена?"
    cs_narrator "Алиса фыркнула."
    show dv smile pioneer far at cs_actor_far_left
    cs_dv "Пока не знаю."
    cs_narrator "Ульяна неожиданно потянула её за рукав."
    show us smile pioneer far at cs_actor_far_right
    cs_us "Алис, пойдём уже! Ты обещала!"
    cs_dv "Да иду я!"
    cs_narrator "Алиса повернулась к нам."
    cs_dv "Ладно, ещё увидимся."
    cs_ls "Не сомневаюсь."
    cs_narrator "Ульяна помахала рукой."
    cs_us "Пока!"
    # cs_darya_variety: reaction
    show cs_darya wave pioneer far at cs_darya_far_center
    cs_da "Пока."
    hide dv
    # cs_composition: regroup
    show cs_darya wave pioneer far at cs_darya_far_left
    hide us
    # cs_composition: regroup
    show cs_darya wave pioneer far at cs_darya_far_center
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    with None
    play sound "sound/sfx/close_door_1.ogg"
    cs_narrator "Я закрыла дверь."
    cs_narrator "Несколько секунд мы с Дарьей молчали."
    cs_narrator "Затем она произнесла:"
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    cs_da "Вроде нормальные девчонки."
    cs_ls "Вполне."
    cs_narrator "Я посмотрела на дверь."
    cs_ls "Хотя младшая, кажется, способна обеспечить лагерю годовой план происшествий."
    cs_narrator "Дарья усмехнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Ты ведь их уже знаешь?"
    cs_ls "По игре — да. Но теперь придётся знакомиться заново."
    cs_narrator "Я подошла к кровати."
    cs_ls "И желательно без преждевременных выводов."
    stop music fadeout 2.0
    return
