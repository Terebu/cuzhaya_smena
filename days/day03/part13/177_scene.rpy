# -*- coding: utf-8 -*-
label cs_day03_177:
    $ save_name = "Чужая смена — День 3: Не обязательно переключаться"
    $ cs_director_scene("cs_camp_path_night")
    scene cs_camp_path_night
    $ cs_frame_focus(["cs_darya"])
    with Dissolve(0.7)
    play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0
    $ renpy.music.set_volume(0.08,channel="music",delay=1.0)
    cs_narrator "Мы шли медленно. Никуда не торопились. Лагерь уже почти затих. Свет фонарей ложился на дорожку небольшими пятнами."
    cs_narrator "По обе стороны темнели деревья. Я смотрела вперёд. Иногда под ноги. Иногда на Дашу."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_th "Красиво. Совсем не так, как днём. Днём здесь постоянно кто-то куда-нибудь спешит. Ольга Дмитриевна раздаёт поручения."
    cs_th "Славя их выполняет. Ульяна старается сделать вид, что никаких поручений не существует. А ночью всё наконец успокаивается."
    cs_narrator "Даша посмотрела на меня."
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
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она некоторое время молчала. Потом спросила:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Сильно зацепила?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Скорее заставила задуматься."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "О чём?"
    cs_narrator "Я посмотрела на дорожку."
    cs_th "О том, что человек может изменить свою жизнь и однажды перестать узнавать самого себя. О том, что иногда мы слишком поздно понимаем, чего на самом деле хотели. И о том, что я всё ещё не знаю, сколько времени нам придётся провести здесь."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "О всяком."
    cs_narrator "Даша посмотрела на меня внимательнее. Но расспрашивать не стала. Мы прошли ещё несколько метров. Потом она тихо сказала:"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ты пошутила про писателей, а теперь снова задумалась."
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
    cs_th "Вот. Это мне и нравится. Никаких вопросов о том, почему я вдруг стала серьёзной. Никаких попыток немедленно меня развеселить."
    cs_th "Просто можно идти рядом."
    cs_narrator "Я чуть сильнее прижалась плечом к её руке."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Спасибо."
    cs_narrator "Даша удивлённо посмотрела."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "За что?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "За то, что не требуешь от меня концертной программы каждый вечер."
    cs_narrator "Она рассмеялась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Лен, по-моему, ты сама её чаще всего устраиваешь."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Очень неприятно, когда против тебя используют факты."
    cs_narrator "Даша улыбнулась."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Но больше ничего не сказала. Мы продолжили идти."
    return
