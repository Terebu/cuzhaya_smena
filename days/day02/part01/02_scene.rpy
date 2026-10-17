# -*- coding: utf-8 -*-
label cs_day02_02:
    $ save_name = "Чужая смена — День 2: Добровольная физкультура"
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_early_morning
    # cs_presence_keep: hide cs_darya
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
    with Dissolve(0.8)
    play ambience "sound/ambiences/forest_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_s02:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я подошла к шкафу."
    cs_narrator "Пионерская форма висела на своём месте."
    cs_narrator "Белая рубашка."
    cs_narrator "Юбка."
    cs_narrator "Галстук, который вчера вечером я аккуратно положила так, чтобы утром не пришлось устраивать поисковую экспедицию."
    cs_narrator "Для пробежки всё это подходило не особенно хорошо."
    cs_narrator "Я присела возле нижней полки."
    cs_narrator "Там лежали простые спортивные шорты и футболка из лагерного комплекта для физкультуры."
    cs_th "Вот теперь другое дело."
    cs_narrator "Вчера я ещё не предполагала, насколько быстро они пригодятся."
    cs_narrator "Переоделась."
    cs_narrator "Проверила, удобно ли сидят кеды."
    cs_narrator "Собрала фиолетовые волосы так, чтобы они не лезли в глаза."
    cs_narrator "Посмотрела в небольшое зеркало."
    cs_th "Обычная девушка."
    cs_th "Обычная спортивная одежда."
    cs_th "Совершенно необычное место жительства."
    cs_narrator "Я невольно усмехнулась."
    cs_narrator "До попадания в лагерь тренировки были одной из немногих привычек, которые мне не приходилось специально поддерживать."
    cs_narrator "Бег."
    cs_narrator "Растяжка."
    cs_narrator "Упражнения с собственным весом."
    cs_narrator "Не ради каких-нибудь спортивных рекордов."
    cs_narrator "Просто мне нравилось чувствовать, что собственное тело выполняет поставленную задачу без необходимости договариваться с ним полчаса."
    cs_narrator "В отличие от собственного характера."
    cs_narrator "С ним переговоры периодически заходили в тупик."
    cs_narrator "Я осторожно подошла к двери."
    cs_narrator "Но перед выходом остановилась."
    cs_th "Наверное, стоит предупредить."
    # cs_director_begin: Face-to-face before the run; lying down does not hide Darya
    $ cs_frame_focus(["cs_darya"])
    show cs_darya neutral pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_33c14ca943:
    # cs_director_end
    cs_narrator "Вернулась к кровати Дарьи."
    cs_narrator "Наклонилась, стараясь не говорить громко."
    # cs_presence_keep: hide cs_darya
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
    cs_ls "Даш, я ненадолго выйду. Хочу пробежаться."
    cs_narrator "Она не ответила."
    cs_narrator "Я подождала пару секунд."
    cs_ls "Если проснёшься раньше меня, не пугайся. Я где-нибудь на территории."
    cs_narrator "Никакой реакции."
    cs_th "Ладно."
    cs_th "Видимо, информация принята непосредственно во сне."
    cs_narrator "Я поправила сползший край её одеяла."
    cs_narrator "Уже собиралась уходить, когда услышала сонный голос:"
    # cs_presence_keep: hide cs_darya
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
    cs_da "Лен…"
    cs_narrator "Я замерла."
    cs_ls "М?"
    cs_narrator "Она даже не открыла глаз."
    cs_da "Ты всегда так рано встаёшь?"
    cs_narrator "Я улыбнулась."
    cs_ls "Обычно да."
    cs_da "Добровольно?"
    cs_ls "Представь себе."
    cs_narrator "Дарья тихо выдохнула."
    cs_da "Удивительная женщина."
    cs_ls "Спасибо. Могу оформить благодарность письменно."
    # cs_director_begin: Sleepy smile during continuous dialogue
    $ cs_frame_focus(["cs_darya"])
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_a0b7342a26:
    # cs_director_end
    cs_narrator "Она слегка улыбнулась, не открывая глаз."
    # cs_director_begin: Serious warning in the waking dialogue
    $ cs_frame_focus(["cs_darya"])
    show cs_darya worried pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_b79045dfe5:
    # cs_director_end
    cs_da "Только не уходи за территорию лагеря одна."
    cs_narrator "Я перестала улыбаться."
    cs_narrator "Совсем ненадолго."
    cs_ls "Не буду."
    cs_da "Обещаешь?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Обещаю. Обычная пробежка по дорожкам."
    cs_narrator "Дарья кивнула."
    cs_da "Тогда хорошей пробежки."
    cs_ls "Спасибо. Спи."
    cs_narrator "Я снова направилась к двери."
    cs_narrator "Уже взялась за ручку, когда она добавила:"
    cs_da "И не пытайся заодно разобраться со всеми загадками лагеря."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Никаких гарантий по загадкам. Но за ворота не пойду."
    cs_da "Лена…"
    cs_ls "Всё, ухожу."
    cs_narrator "Она негромко усмехнулась."
    cs_narrator "Я закрыла дверь настолько осторожно, насколько позволяли старые петли."
    # cs_director_begin: Lena leaves the cabin; Darya stays inside
    $ cs_actor_exit(["cs_darya"])
    with cs_sprite_leave
    label cs_director_check_d7c88fa410:
    # cs_director_end
    play sound "sound/sfx/close_door_1.ogg"
    stop music fadeout 2.0
    return
