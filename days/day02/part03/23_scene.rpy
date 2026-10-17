# -*- coding: utf-8 -*-
label cs_day02_23:
    $ save_name = "Чужая смена — День 2: Человек с плаката"
    $ cs_part03_live = True
    $ cs_part02_live = False
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part03_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_part03_s23:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Славя шла нам навстречу."
    cs_narrator "В руках она держала небольшую коробку, а под мышкой — папку с листами бумаги."
    cs_narrator "Две светлые косы покачивались при каждом шаге."
    cs_narrator "На лице — привычная доброжелательная улыбка."
    cs_narrator "Причём даже коробка, похоже, не мешала ей выглядеть так, будто она прекрасно знает, куда идёт и что собирается делать."
    cs_th "Вот это дисциплина."
    cs_th "Я бы на её месте уже успела потерять карандаши, забыть папку и начать искать виноватых."
    cs_narrator "Славя заметила нас."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Доброе утро!"
    cs_ls "Привет."
    cs_da "Доброе утро."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Привет."
    cs_narrator "Славя поправила папку."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    $ cs_part03_cast = ["sl", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Ольга Дмитриевна уже сказала вам про объявление?"
    cs_ls "Сказала. Мы как раз обсуждали организацию творческого производства."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Тогда хорошо. Я вам бумагу и карандаши принесла. Только сначала нужно убрать часть материалов в кладовую."
    cs_narrator "Я посмотрела на коробку."
    cs_narrator "Потом на Славю."
    cs_narrator "На её причёску."
    cs_narrator "На аккуратно завязанный галстук."
    cs_narrator "На то, как спокойно она одновременно удерживала коробку и папку."
    cs_narrator "И в голове сама собой появилась совершенно нелепая ассоциация."
    cs_ls "Славя."
    cs_narrator "Она посмотрела на меня."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Да?"
    cs_ls "Тебе никто не говорил, что ты будто сошла с советского плаката?"
    cs_narrator "Славя удивлённо моргнула."
    cs_sl "С какого?"
    cs_narrator "Я задумалась."
    cs_ls "Ну… «Поможем товарищам выполнить план». Или «Образцовый пионер всегда готов»."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Уже улыбалась."
    cs_sl "Почему?"
    cs_narrator "Я развела руками."
    cs_ls "Ты всё успеваешь. Всех знаешь. Всем помогаешь. И даже с этой коробкой выглядишь так, будто идёшь получать грамоту."
    cs_narrator "Славя тихо рассмеялась."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Ничего подобного. Я иногда тоже всё забываю."
    cs_ls "Не верю."
    cs_sl "Правда!"
    cs_narrator "Она улыбнулась."
    cs_sl "Вчера, например, искала ключ от кладовой. Оказалось, сама же оставила его у вожатой."
    cs_narrator "Я торжественно кивнула."
    cs_ls "Значит, даже у образцовых пионеров бывают технические неисправности."
    cs_narrator "Дарья засмеялась."
    cs_da "Лен, по-моему, ты сейчас сама напоминаешь автора агитационного плаката."
    cs_ls "Не исключено. Моя задача — подготовить население к выполнению плана."
    cs_narrator "Славя улыбнулась."
    cs_sl "Тогда начните с объявления. Его сегодня действительно нужно закончить."
    cs_narrator "Я посмотрела на коробку."
    cs_ls "Поняла. Задачи вполне реальные."
    cs_narrator "Несколько секунд мы стояли молча."
    cs_narrator "Затем Семён спросил:"
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А что там вообще?"
    cs_narrator "Славя приоткрыла крышку."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Карандаши, кнопки, несколько катушек ниток и разные мелочи для объявлений."
    cs_narrator "Я заглянула внутрь."
    cs_ls "Значит, техническое оснащение художественного отдела уже прибыло."
    cs_da "Осталось только организовать сам художественный отдел."
    cs_ls "Справедливое замечание."
    cs_narrator "Славя посмотрела на нас с улыбкой."
    cs_sl "Вы смешные."
    cs_narrator "Я повернулась к Дарье."
    cs_ls "Слышала? Официальная оценка деятельности коллектива."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part03_cast = []
    show sl smile pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part03_cast = ["sl", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Положительная?"
    cs_ls "Пока да."
    cs_narrator "Славя засмеялась."
    cs_narrator "Но затем посмотрела на коробку."
    cs_sl "Ладно, мне надо отнести это в кладовую, а потом показать вам, где можно работать."
    cs_narrator "Я посмотрела на неё."
    cs_th "Вот теперь можно просто пройти дальше."
    cs_th "Или предложить помощь."
    cs_th "Кажется, иногда первое решение оказывается важнее самой длинной речи."
    return
