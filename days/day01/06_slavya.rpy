# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_06:
    $ save_name = u"Чужая смена — День 1: Девушка с двумя косами"
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    play music cs_day_music_mystery fadeout 2.0 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Дарья заметила, как изменилось моё выражение лица."
    cs_da "Ты знаешь, кто это?"
    cs_narrator "За воротами показался силуэт: светлые волосы, белая рубашка, пионерская форма."
    cs_narrator "Я на секунду прикрыла глаза."
    cs_ls "Если сейчас появится блондинка с двумя косами и предложит нам помощь, я официально признаю этот день самым странным в своей жизни."
    show sl normal pioneer at cs_actor_left
    # cs_composition: regroup
    show cs_dasha_winter thinking normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Из-за ворот вышла девушка и остановилась, увидев нас."
    show sl surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Удивлённо моргнула, затем приветливо улыбнулась."
    stop music fadeout 1.5
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_day01_slavya:
    cs_sl "Ой! Привет! Вы, наверное, только приехали?"
    pause 1.5
    cs_narrator "Я молча смотрела на её лицо, рубашку, красный галстук, две аккуратные косы. Имя возникло раньше, чем я успела его произнести."
    $ cs_slavya_known = True
    cs_narrator "{b}Славя.{/b}"
    cs_narrator "Настоящая. Не спрайт с пятью эмоциями, а живая девушка: дышит, двигается и ждёт ответа."
    cs_narrator "Её голос я помнила по игре. Но здесь, среди летнего леса, он звучал совсем иначе."
    pause 1.0
    cs_narrator "До меня наконец дошло: я больше не смотрела на «Совёнок» через экран. Я стояла перед его воротами."
    $ renpy.music.set_volume(0.25, delay=1.0, channel="music")
    play music cs_day_music_friends fadeout 2.0 fadein 3.0
    cs_narrator "Я медленно повернулась к Дарье."
    cs_ls "Ну всё."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Поздравляю. Совпадение официально перестало быть совпадением."
    cs_ls "Осталось только выяснить, предусмотрен ли здесь обратный билет."
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    pause 1.0
    return
