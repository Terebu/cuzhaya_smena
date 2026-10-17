# -*- coding: utf-8 -*-
label cs_day02_28:
    $ save_name = "Чужая смена — День 2: Ещё одно знакомое место"
    $ cs_part03_live = False
    $ cs_part04_live = True
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_part04_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
        play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.2, channel="music", delay=1.0)
    label cs_check_part04_s28:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Дорожка постепенно становилась тише."
    cs_narrator "Чем дальше мы отходили от площади, тем меньше слышалось голосов."
    cs_narrator "По обе стороны росли деревья."
    cs_narrator "Между стволами виднелись кусты, залитые солнечным светом."
    cs_narrator "Я шла немного впереди."
    cs_narrator "Дарья держалась рядом."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты знаешь дорогу?"
    cs_narrator "Я кивнула."
    cs_ls "Примерно."
    cs_da "По игре?"
    cs_ls "Отчасти. Хотя за эти два дня уже успела немного запомнить, где что находится."
    cs_narrator "Она посмотрела на меня."
    cs_da "Тебя всё ещё не пугает, насколько многое здесь совпадает?"
    cs_narrator "Я помолчала."
    cs_ls "Пугает."
    cs_narrator "Это прозвучало серьёзнее, чем я собиралась."
    cs_narrator "Дарья немного замедлила шаг."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Просто если каждый раз останавливаться и удивляться знакомому зданию, мы до вечера даже столовую не обойдём."
    cs_narrator "Она слегка улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Тоже верно."
    # cs_director_begin: REFLECTIVE_SHOT: Game characters versus people; restore at Darya
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_b04206e46a:
    # cs_director_end
    cs_narrator "Я посмотрела вперёд."
    cs_th "Хотя на самом деле дело не только в зданиях."
    cs_narrator "Окружающие люди имели знакомые лица."
    cs_narrator "Знакомые имена."
    cs_narrator "Иногда даже говорили вещи, которые вполне могли бы оказаться в оригинальной новелле."
    cs_narrator "Но при этом постоянно делали что-нибудь неожиданное."
    cs_narrator "Женя оказалась наблюдательнее, чем я предполагала."
    cs_narrator "Славя спокойно шутила в ответ."
    cs_narrator "Мику с искренним интересом расспрашивала нас о музыке."
    cs_narrator "А Дарья…"
    # cs_director_begin: Return to direct interaction: Game characters versus people; restore at Darya
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_68ee94beab:
    # cs_director_end
    cs_narrator "Я посмотрела на неё."
    cs_th "А про Дашу я вообще почти ничего не знала."
    cs_narrator "Вчера она была незнакомкой из автобуса."
    cs_narrator "Сегодня — человеком, с которым я уже делила домик, планы и довольно необычные обстоятельства."
    cs_narrator "И всё равно каждый новый разговор открывал в ней что-то, чего я раньше не замечала."
    cs_th "Может, именно так и надо относиться ко всему лагерю."
    cs_th "Не пытаться угадать чужое поведение."
    cs_th "А просто узнавать людей."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен?"
    cs_narrator "Я повернулась."
    cs_ls "Да?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты опять задумалась."
    cs_ls "Есть немного."
    cs_narrator "Она кивнула вперёд."
    cs_da "Кажется, пришли."
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    $ cs_part04_cg = False
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "За деревьями показалось небольшое здание."
    cs_narrator "На фасаде располагалась знакомая вывеска."
    cs_narrator "Медпункт."
    cs_narrator "Я остановилась."
    cs_narrator "Несколько секунд рассматривала его."
    cs_th "Вот он."
    cs_th "Ещё одно место, которое раньше существовало для меня только на экране."
    cs_narrator "Дарья посмотрела на дверь."
    cs_da "Надеюсь, здесь кто-нибудь есть."
    cs_narrator "Я поправила галстук."
    cs_ls "Сейчас узнаем."
    cs_narrator "Мы поднялись на крыльцо."
    play sound "sound/sfx/knock_door7_polite.ogg"
    cs_narrator "Я постучала."
    cs_narrator "Изнутри послышался женский голос:"
    cs_vi "Входите."
    play sound "sound/sfx/open_door_2.ogg"
    cs_narrator "Я открыла дверь."
    return
