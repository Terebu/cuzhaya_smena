# -*- coding: utf-8 -*-
label cs_day03_177:
    $ save_name = "Чужая смена — День 3: Не обязательно переключаться"
    $ cs_director_scene("cs_camp_path_night")
    scene cs_camp_path_night
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0
    $ renpy.music.set_volume(0.08,channel="music",delay=1.0)
    cs_narrator "Мы шли медленно."
    cs_narrator "Никуда не торопились."
    cs_narrator "Лагерь уже почти затих."
    cs_narrator "Свет фонарей ложился на дорожку небольшими пятнами."
    cs_narrator "По обе стороны темнели деревья."
    cs_narrator "Я смотрела вперёд."
    cs_narrator "Иногда под ноги."
    cs_narrator "Иногда на Дашу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Красиво."
    cs_th "Совсем не так, как днём."
    cs_th "Днём здесь постоянно кто-то куда-нибудь спешит."
    cs_th "Ольга Дмитриевна раздаёт поручения."
    cs_th "Славя их выполняет."
    cs_th "Ульяна старается сделать вид, что никаких поручений не существует."
    cs_th "А ночью всё наконец успокаивается."
    cs_narrator "Дарья посмотрела на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты какая-то задумчивая."
    cs_narrator "Я повернулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Немного."
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Всё ещё о книге думаешь?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она некоторое время молчала."
    cs_narrator "Потом спросила:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Сильно зацепила?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Скорее заставила задуматься."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "О чём?"
    cs_narrator "Я посмотрела на дорожку."
    cs_th "О том, что человек может изменить свою жизнь и однажды перестать узнавать самого себя."
    cs_th "О том, что иногда мы слишком поздно понимаем, чего на самом деле хотели."
    cs_th "И о том, что я всё ещё не знаю, сколько времени нам придётся провести здесь."
    cs_narrator "Я немного улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "О всяком."
    cs_narrator "Дарья посмотрела на меня внимательнее."
    cs_narrator "Но расспрашивать не стала."
    cs_narrator "Мы прошли ещё несколько метров."
    cs_narrator "Потом она тихо сказала:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты пошутила про писателей, а теперь снова задумалась."
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Не хочется."
    cs_narrator "Она кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Тогда и не надо."
    cs_narrator "Я посмотрела на неё."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Вот."
    cs_th "Это мне и нравится."
    cs_th "Никаких вопросов о том, почему я вдруг стала серьёзной."
    cs_th "Никаких попыток немедленно меня развеселить."
    cs_th "Просто можно идти рядом."
    cs_narrator "Я чуть сильнее прижалась плечом к её руке."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Спасибо."
    cs_narrator "Дарья удивлённо посмотрела."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "За что?"
    cs_narrator "Я слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "За то, что не требуешь от меня концертной программы каждый вечер."
    cs_narrator "Она рассмеялась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Лен, по-моему, ты сама её чаще всего устраиваешь."
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Очень неприятно, когда против тебя используют факты."
    cs_narrator "Дарья улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Но больше ничего не сказала."
    cs_narrator "Мы продолжили идти."
    return
