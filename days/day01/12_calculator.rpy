# -*- coding: utf-8 -*-
# Source: source/day01_part03.md.
label cs_day01_12:
    $ save_name = u"Чужая смена — День 1: Японский калькулятор"
    $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 1.5 fadein 2.0
    $ renpy.music.set_volume(0.45, delay=1.0, channel="ambience")
    # cs_presence_keep: hide sl
    # cs_composition: regroup
    show mt normal pioneer at cs_actor_left
    # cs_composition: regroup
    show cs_dasha_winter arms_crossed far at cs_darya_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    show screen cs_phone(mode="off", phone_x=820, phone_width=260)
    # cs_darya_stage: present in story
    show cs_dasha_winter arms_crossed normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["mt", "cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я медленно достала телефон."
    label cs_check_day01_part03_phone_off:
    cs_narrator "Экран всё ещё оставался чёрным."
    cs_narrator "Нажала кнопку питания."
    cs_narrator "Ничего."
    cs_narrator "Посмотрела на аппарат."
    cs_narrator "Потом на советский радиоприёмник."
    cs_narrator "И снова на смартфон."
    cs_ls "А вот это отдельная проблема."
    cs_narrator "Ольга Дмитриевна заметила устройство."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Что это у тебя?"
    hide screen cs_phone
    cs_narrator "Я моментально убрала телефон."
    cs_ls "Ничего особенного."
    cs_mt "Я видела."
    label cs_check_day01_part03_calculator:
    cs_ls "Калькулятор."
    cs_da "Ты ужасно врёшь."
    cs_ls "Спасибо за экспертное заключение."
    cs_narrator "Ольга Дмитриевна подошла ближе."
    cs_mt "Какой ещё калькулятор?"
    cs_ls "Японский."
    cs_mt "А где у него кнопки?"
    cs_ls "Передовые технологии. Минимализм."
    # cs_darya_variety: reaction
    show cs_dasha_winter shrug normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты могла просто его не доставать."
    cs_ls "Согласна. К сожалению, решение принято, отмене не подлежит."
    cs_narrator "Я убрала смартфон поглубже в карман."
    cs_ls "Предлагаю считать его очень скучным калькулятором."
    # cs_camp_emotion: text reaction
    show mt sad pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Лена…"
    cs_ls "Поверьте, подробное объяснение сейчас только добавит вопросов."
    cs_narrator "Она внимательно посмотрела на меня."
    cs_mt "Ты очень странная девушка."
    cs_ls "Мне это уже говорили."
    cs_mt "И ты знаешь моё имя."
    cs_ls "Да."
    cs_mt "И имя Слави."
    cs_ls "Да."
    cs_mt "Хотя утверждаешь, что никогда здесь не была."
    stop music fadeout 2.0
    cs_narrator "Я замолчала."
    cs_narrator "Вот здесь разговор окончательно перестал быть забавным."
    cs_ls "Не была."
    # cs_darya_variety: reaction
    show cs_dasha_winter arms_crossed normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она скрестила руки."
    cs_mt "Тогда откуда всё знаешь?"
    cs_narrator "Я посмотрела ей прямо в глаза."
    cs_narrator "Можно было соврать."
    cs_narrator "Сказать, что кто-то рассказывал об этом лагере."
    cs_narrator "Что слышала о нём от знакомых."
    cs_narrator "Что здесь бывали мои родители."
    cs_narrator "Любая версия прозвучала бы значительно правдоподобнее."
    cs_narrator "Но проблема заключалась в другом."
    cs_narrator "Если это действительно тот самый «Совёнок», слишком много выдумок в самом начале могли однажды сыграть против меня."
    cs_narrator "Поэтому я решила сказать правду."
    cs_narrator "Очень маленькую её часть."
    $ renpy.music.set_volume(0.3, delay=1.0, channel="music")
    play music cs_day_music_doubt fadeout 1.5 fadein 3.0
    cs_ls "Я знаю это место."
    # cs_camp_emotion: text reaction
    show mt surprise pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mt "Откуда?"
    cs_ls "Не отсюда."
    cs_mt "Это как понимать?"
    cs_narrator "Я чуть наклонила голову."
    cs_ls "Вот этого я пока сама не могу объяснить."
    pause 1.0
    cs_narrator "Тишина."
    cs_narrator "Ольга Дмитриевна явно собиралась задать ещё один вопрос."
    cs_narrator "Но тут открылась дверь."
    $ renpy.music.set_volume(0.65, channel="sound")
    play sound cs_day_sfx_door
    # cs_composition: regroup
    show mt normal pioneer far at cs_actor_far_left
    # cs_composition: regroup
    show sl smile pioneer far at cs_actor_far_right
    # cs_composition: regroup
    # cs_darya_stage: present in story
    show cs_dasha_winter arms_crossed far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Нашла!"
    stop music fadeout 1.5
    return
