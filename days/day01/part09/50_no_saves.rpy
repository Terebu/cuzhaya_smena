# -*- coding: utf-8 -*-
label cs_day01_50:
    $ save_name = "Чужая смена — День 1: Никаких сохранений"
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.5)
    $ renpy.music.set_volume(0.14,delay=2.0,channel="music")
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы вышли на более широкую дорожку."
    # cs_director_begin: Panorama and independent reflection
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_b323b7e93a:
    # cs_director_end
    # cs_inward_beat_0: attention turns inward
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_narrator "Отсюда открывался вид на деревья и несколько домиков, освещённых вечерним солнцем."
    cs_narrator "Позади остались клубы, площадь и столовая. Знакомые по игре места, знакомые лица."
    cs_narrator "Теперь от прогулки по ним болели ноги."
    label cs_check_day01_part09_introspection:
    cs_th "И никаких сохранений. Ни перемотать неудачный разговор, ни выбрать другую реплику."
    cs_th "А что случится, если серьёзно ошибиться?"
    cs_narrator "Я медленно вдохнула."
    # cs_director_begin: Resume the uninterrupted conversation
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_961dd14276:
    # cs_director_end
    # Return to the same conversation, with the same cast and placement.
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Дарья заметила моё выражение лица."
    label cs_check_day01_part09_returns:
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты опять задумалась?"
    cs_ls "Немного."
    cs_da "О чём?"
    cs_ls "О том, что здесь нельзя сохраняться."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_da "Как в игре?"
    cs_ls "Угу."
    cs_da "Но в обычной жизни тоже нельзя."
    cs_narrator "Я помолчала и кивнула."
    cs_ls "Верно."
    cs_narrator "Она посмотрела на меня внимательнее."
    cs_da "Лен, ты ведь не обязана всё время знать, как правильно поступить."
    cs_ls "Это прозвучало подозрительно разумно."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Я старалась."
    cs_ls "Спасибо."
    cs_narrator "Она кивнула."
    cs_narrator "Мы снова пошли."
    # cs_director_begin: REFLECTIVE_SHOT: Difference between game choices and real consequences
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_031e208f3c:
    # cs_director_end
    cs_narrator "А я вдруг подумала, что, возможно, именно в этом и заключается самая большая разница между игрой и происходящим."
    cs_narrator "В игре я выбирала ответы ради результата. Здесь придётся говорить с людьми, не зная продолжения, и принимать последствия."
    return
