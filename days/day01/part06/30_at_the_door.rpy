# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_30:
    $ save_name = "Чужая смена — День 1: За дверью"
    label cs_check_day01_part06_visitors:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_cabin:
        play ambience cs_day_cabin fadeout 1.5 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я аккуратно сложила лист пополам и положила на тумбочку."
    cs_narrator "Дарья тем временем подошла к окну."
    show cs_darya serious pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_ls "Что?"
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Кажется, к нам кто-то идёт."
    cs_narrator "Из-за деревьев показались две фигуры: рыжеволосая и та, что ниже ростом. Я подошла к окну."
    cs_th "Алиса. Ульяна."
    cs_narrator "Ну разумеется."
    cs_ls "Даш."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "М?"
    cs_ls "У нас гости."
    cs_da "Знакомые?"
    cs_ls "Более чем."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Это хорошо?"
    cs_narrator "За окном Алиса что-то сказала Ульяне."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Та рассмеялась. Обе направились к нашему домику."
    cs_ls "Скажем так. Сейчас получим возможность оценить качество местной системы знакомства с новосёлами."
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты опять начинаешь?"
    cs_ls "Я ещё даже ничего не сказала."
    cs_narrator "На крыльце послышались шаги, затем стук."
    $ renpy.music.set_volume(0.45,channel="sound")
    play sound cs_day_sfx_knock
    label cs_check_day01_part06_knock:
    cs_narrator "Мы с Дарьей переглянулись."
    cs_dv "Эй, новенькие! Вы там живые?"
    cs_narrator "Я медленно выдохнула."
    cs_th "Спокойное заселение официально завершено."
    cs_narrator "Я подошла к двери и взялась за ручку."
    cs_ls "Живые. Предварительная проверка это подтверждает."
    cs_narrator "Из-за двери донёсся второй, более звонкий голос:"
    cs_us "Алиса, я же говорила, они странные!"
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Та уже с трудом сдерживала улыбку."
    cs_ls "Ну всё. Международная репутация окончательно сформирована."
    $ renpy.music.set_volume(0.45,delay=1.0,channel="music")
    play music cs_day_music_play fadeout 2.0 fadein 2.0
    pause 0.7
    play sound cs_day_sfx_door
    label cs_check_day01_part06_open_door:
    cs_narrator "Я открыла дверь."
    return
