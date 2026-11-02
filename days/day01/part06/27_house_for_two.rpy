# -*- coding: utf-8 -*-
# Source: source/day01_part06.md; authored speaker transcript in source/day01_part06_dialogue.json.
label cs_day01_27:
    $ save_name = "Чужая смена — День 1: Домик"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    show sl smile pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(1.3)
    label cs_check_day01_part06_house_ext:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_camp_center:
        play ambience cs_day_camp_center fadeout 1.5 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["sl", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Славя остановилась перед небольшим домиком."
    cs_sl "Вот и пришли!"
    cs_narrator "Небольшое крыльцо, два окна, деревянные стены. Обычный домик — а нам предстоит здесь ночевать."
    cs_th "Новая квартира. Условия предоставления — временная аномалия. Срок проживания неизвестен."
    cs_da "Симпатично."
    cs_ls "Есть такое."
    cs_narrator "Славя поднялась на крыльцо и открыла дверь."
    cs_sl "Проходите."
    $ renpy.music.set_volume(0.45,channel="sound")
    play sound cs_day_sfx_door
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
    show sl normal pioneer at cs_actor_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(1.4)
    label cs_check_day01_part06_house_int:
    $ renpy.music.set_volume(0.3,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != cs_day_cabin:
        play ambience cs_day_cabin fadeout 1.5 fadein 2.0
    stop music fadeout 2.0
    cs_narrator "Внутри было уютно: две кровати, стол, шкаф, тумбочки. Сквозь занавески падали солнечные прямоугольники."
    cs_narrator "Ни компьютера, ни холодильника. Даже розетки возле кровати для телефона не видно."
    cs_th "Радикальный минимализм."
    cs_narrator "Славя показала на шкаф."
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Здесь можно хранить вещи. Постельное бельё уже должно быть приготовлено."
    cs_sl "На нижней полке лежат футболки и спортивные шорты для физкультуры. Если захотите позаниматься, берите."
    cs_narrator "Дарья потрогала покрывало."
    cs_da "Выглядит неплохо."
    cs_narrator "Я посмотрела на вторую кровать."
    cs_ls "Проверим соответствие заявленным характеристикам."
    cs_narrator "Я села на край. Скрипнули пружины."
    $ renpy.music.set_volume(0.45,channel="sound")
    play sound cs_day_sfx_bed
    cs_narrator "Я чуть покачалась."
    cs_ls "Конструкция функционирует."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Славя не удержалась от смеха."
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sl "Вы забавные."
    cs_ls "Спасибо. Хотя пока не уверена, что это официальная характеристика."
    cs_narrator "Славя объяснила, где умывальники и какие здесь правила. Я слушала: полагаться на память об игре было бы глупо."
    cs_sl "Если что-нибудь понадобится, обращайтесь ко мне или к Ольге Дмитриевне."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо. Спасибо тебе."
    cs_ls "Правда, спасибо. Ты нам очень помогла."
    cs_narrator "Славя улыбнулась ещё шире."
    cs_sl "Не за что!"
    cs_narrator "Она направилась к двери."
    cs_sl "Тогда я побегу. У меня ещё дела!"
    cs_da "Увидимся."
    cs_ls "Пока, Славя."
    cs_narrator "Дверь закрылась."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["sl"])
    with cs_sprite_leave
    label cs_director_check_1633c67ed0:
    # cs_director_end
    # cs_presence_keep: hide sl
    # cs_composition: regroup
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Мы остались вдвоём."
    pause 1.0
    cs_narrator "Мы помолчали, потом переглянулись."
    cs_ls "Ну что."
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Кажется, у нас теперь есть недвижимость."
    show cs_darya amused pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Временная."
    cs_ls "Уточнение принято."
    return
