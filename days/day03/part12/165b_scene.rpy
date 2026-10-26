# -*- coding: utf-8 -*-
label cs_day03_165b:
    $ save_name = "Чужая смена — День 3: Вовремя уйти — тоже навык"
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_frame_focus(["cs_semen", "sl"])
    with cs_sprite_change
    cs_narrator "Я посмотрела на листок в руках Слави."
    cs_narrator "Потом на Семёна."
    cs_th "Нет."
    cs_th "Сегодня я уже достаточно участвовала в общественной жизни."
    cs_th "Пусть хотя бы одно поручение лагерная администрация выполнит без моего экспертного заключения."
    cs_narrator "Я улыбнулась."
    cs_ls "Я как раз за книгой, а потом в библиотеку."
    $ cs_sl_evening_destination_told_day3 = True
    cs_ls "Ладно, не буду мешать. Вам ещё нужно разобраться с бумагами."
    cs_narrator "Славя кивнула."
    cs_sl "Спасибо. Мы уже почти закончили."
    cs_narrator "Семён посмотрел на меня с подозрением."
    cs_sy "И никаких последних замечаний?"
    cs_narrator "Я задумалась."
    cs_narrator "Посмотрела на него."
    cs_ls "Есть одно."
    cs_narrator "Он закрыл глаза."
    cs_sy "Ну конечно."
    cs_narrator "Я улыбнулась."
    cs_ls "Желаю успешного завершения совещания."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_narrator "Семён открыл глаза."
    cs_narrator "Посмотрел на меня."
    cs_narrator "Потом усмехнулся."
    cs_sy "Спасибо, товарищ Соколова."
    cs_narrator "Я кивнула."
    cs_ls "Всегда пожалуйста."
    cs_narrator "Развернулась."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "И направилась к домику."
    cs_th "Вот."
    cs_th "Прекрасно."
    cs_th "Сумела пройти мимо двух знакомых людей и не задержаться у них на полчаса."
    cs_th "Пожалуй, моя способность к самоконтролю действительно развивается."
    $ cs_sl_evening_scene_done_day3 = True
    return
