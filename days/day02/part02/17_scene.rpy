# -*- coding: utf-8 -*-
label cs_day02_17:
    $ save_name = "Чужая смена — День 2: Комната, в которой живёт музыка"
    $ cs_director_scene("bg ext_musclub_day")
    scene bg ext_musclub_day
    $ cs_part02_cg = False
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    play sound "sound/sfx/open_door_2.ogg"
    $ cs_director_scene("bg int_musclub_day")
    scene bg int_musclub_day
    $ cs_part02_cg = False
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi normal pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/music_club_day.ogg":
        play ambience "sound/ambiences/music_club_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.12, channel="ambience", delay=1.0)
    stop music fadeout 2.0
    label cs_check_part02_s17:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mi", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Внутри было светло."
    cs_narrator "Через окна падали широкие полосы солнечного света, ложившиеся на деревянный пол и инструменты."
    cs_narrator "Я остановилась у входа."
    cs_narrator "Осмотрелась."
    cs_narrator "Пианино."
    cs_narrator "Гитары."
    cs_narrator "Нотные подставки."
    cs_narrator "Несколько стульев."
    cs_narrator "Шкаф с папками и разными мелочами."
    cs_narrator "Всё выглядело знакомо."
    cs_narrator "Но теперь я могла заметить то, чего не было видно на игровом фоне."
    cs_narrator "Потёртости на краях инструментов."
    cs_narrator "Следы карандаша на нотных листах."
    cs_narrator "Один неровно поставленный стул."
    cs_narrator "И едва уловимый запах дерева и старого лака."
    cs_th "И снова то же чувство."
    cs_th "Вчера всё это было частью игры."
    cs_th "А сегодня я стою посреди комнаты, в которой кто-то действительно занимается музыкой."
    cs_narrator "Мику положила папку на стол."
    cs_narrator "Та немедленно раскрылась."
    cs_narrator "Несколько листов сползли к краю."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    $ cs_part02_cast = ["mi", "cs_darya"]
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part02_miku_17:
    cs_mi "Ой!"
    cs_narrator "Она успела поймать один."
    cs_narrator "Второй подхватила Дарья."
    cs_narrator "Я подняла третий с пола."
    cs_da "Похоже, папке действительно нужен ремонт."
    cs_mi "Я же говорила!"
    cs_narrator "Мы рассмеялись."
    cs_narrator "Мику забрала бумаги и аккуратно сложила их."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi shy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Спасибо. А то я потом опять буду искать нужную страницу по всему кружку."
    cs_narrator "Я посмотрела на пианино у стены."
    cs_narrator "Подошла ближе."
    cs_narrator "Провела взглядом по клавишам."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Ты тоже играешь?"
    cs_ls "Почти нет."
    cs_mi "Почти?"
    cs_ls "Могу найти несколько нот и сделать вид, что понимаю происходящее."
    cs_narrator "Дарья негромко усмехнулась."
    cs_da "Она скромничает. На нервах играет очень уверенно."
    cs_narrator "Я медленно повернулась к ней."
    cs_ls "Даша."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Это было неожиданно жестоко."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты сама начала."
    cs_narrator "Мику засмеялась."
    cs_narrator "Я улыбнулась."
    cs_th "Надо же."
    cs_th "Она начинает подхватывать мои шутки."
    cs_narrator "И делает это всё увереннее."
    cs_narrator "Впрочем, теперь я уже не собиралась отвечать какой-нибудь новой колкостью."
    cs_narrator "Мне действительно было интересно услышать, как она играет."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_ls "А ты помнишь что-нибудь из того, чему училась?"
    cs_narrator "Дарья посмотрела на пианино."
    cs_da "Может быть."
    cs_mi "Хочешь попробовать?"
    cs_narrator "Она отодвинула стул."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi surprise pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Сейчас?"
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mi "Конечно! Только если сама хочешь."
    cs_narrator "Даша задумалась."
    cs_narrator "Потом посмотрела на меня."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Не смейся, если я перепутаю ноты."
    cs_narrator "Я подняла обе руки."
    cs_ls "Даже не собиралась."
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    show cs_darya surprised pioneer normal at cs_darya_normal_right
    $ cs_part02_cast = ["mi", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Совсем?"
    cs_ls "Торжественно обещаю."
    cs_narrator "Она улыбнулась."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    $ cs_part02_cast = []
    show mi happy pioneer at cs_actor_left zorder 10
    $ cs_part02_cast = ["mi"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Подошла к инструменту и села."
    cs_narrator "Я осталась чуть в стороне."
    cs_th "Интересно."
    cs_th "Кажется, сейчас узнаю о ней что-то новое."
    return
