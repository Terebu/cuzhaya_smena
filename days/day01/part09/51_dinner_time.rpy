# -*- coding: utf-8 -*-
label cs_day01_51:
    $ save_name = "Чужая смена — День 1: Время ужинать"
    $ cs_director_scene("bg ext_houses_sunset")
    scene bg ext_houses_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.5)
    stop music fadeout 2.5
    $ renpy.music.set_volume(0.35,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "В этот момент над лагерем раздался сигнал горна."
    play sound "sound/sfx/dinner_jingle_speaker.ogg"
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела в сторону столовой."
    cs_narrator "Затем на Дарью."
    cs_ls "А вот и звуковое сопровождение следующего пункта программы."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ужин?"
    cs_ls "Судя по всему."
    cs_narrator "Она посмотрела на дорожку."
    cs_da "Пойдём?"
    cs_narrator "Я кивнула."
    cs_ls "Пойдём."
    cs_narrator "Мы направились к столовой."
    # cs_director_begin: REFLECTIVE_SHOT: Evening camp before looking back at Darya
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_368a2a6837:
    # cs_director_end
    cs_narrator "Вокруг постепенно оживал лагерь."
    cs_narrator "Открывались двери домиков."
    cs_narrator "На дорожках появлялись пионеры."
    cs_narrator "Кто-то торопился, кто-то спокойно шёл, разговаривая с друзьями."
    cs_narrator "Обычный летний вечер."
    cs_narrator "В обычном пионерском лагере."
    cs_narrator "Только для меня он уже давно перестал быть обычным."
    # cs_director_begin: Return to direct interaction: Evening camp before looking back at Darya
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_ac2ec6714a:
    # cs_director_end
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она шла рядом, слегка улыбаясь чему-то своему."
    cs_th "Может, я и не знаю, как мы отсюда выберемся."
    cs_th "Может, знакомый сюжет уже изменился настолько, что полагаться на него бесполезно."
    cs_th "Но хотя бы сегодня я не одна."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Даш."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Если на ужин снова будет компот, предлагаю официально признать его стратегическим ресурсом лагеря."
    cs_narrator "Она рассмеялась."
    cs_da "Только не начинай."
    cs_ls "Поздно. Проект постановления уже готов."
    cs_narrator "Мы свернули к столовой."
    $ renpy.music.set_volume(0.24,delay=1.0,channel="music")
    play music cs_day_music_everyday fadeout 2.0 fadein 2.5
    return
