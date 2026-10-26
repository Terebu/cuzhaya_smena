# -*- coding: utf-8 -*-
label cs_day03_167:
    $ save_name = "Чужая смена — День 3: Комиссия продолжает работу"
    $ cs_director_scene("bg ext_square_sunset")
    scene bg ext_square_sunset
    $ cs_frame_focus(["cs_semen", "sl"])
    with Dissolve(0.7)
    cs_narrator "На обратном пути я снова увидела Семёна и Славю."
    cs_narrator "Они всё ещё были возле дорожки."
    cs_narrator "Правда, теперь Славя уже складывала бумаги."
    cs_narrator "Семён что-то говорил."
    cs_narrator "Она кивала."
    cs_th "Ну надо же."
    cs_th "Совещание затянулось."
    cs_narrator "Я заранее подняла здоровую руку."
    cs_ls "Ничего не говорю!"
    cs_narrator "Семён повернулся."
    cs_narrator "Посмотрел на меня."
    cs_sy "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Правда."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя улыбнулась."
    cs_sl "Нашла книгу?"
    cs_narrator "Я показала том."
    cs_ls "Докладываю: объект обнаружен и возвращён в распоряжение читателя."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_narrator "Семён посмотрел на книгу."
    cs_narrator "Потом на меня."
    cs_sy "Ты ведь за ней и ходила?"
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_sy "Тогда почему у меня такое чувство, что ты ещё что-нибудь собираешься сказать?"
    cs_narrator "Я задумалась."
    cs_th "Проклятье."
    cs_th "Он действительно начинает слишком хорошо меня понимать."
    if cs_friend_se >= 2 and cs_se_day3_personal_talk:
        cs_narrator "Я улыбнулась."
        cs_ls "Вообще-то хотела узнать, закончилось ли ваше тайное совещание."
        cs_narrator "Семён посмотрел на Славю."
        cs_narrator "Потом на меня."
        cs_sy "Почти. Комиссия постановила: Семён невиновен."
        cs_narrator "Я остановилась."
        cs_narrator "Медленно подняла бровь."
        cs_ls "Вот как?"
        cs_narrator "Он кивнул."
        cs_sy "Да. И обжалованию решение не подлежит."
        if renpy.showing("sl"):
            show sl laugh pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Славя рассмеялась."
        cs_narrator "Я задумалась."
        cs_narrator "Потом торжественно кивнула."
        cs_ls "Хорошо. Следствие принимает решение суда."
        cs_narrator "Семён удивлённо посмотрел на меня."
        cs_sy "Даже так?"
        cs_narrator "Я улыбнулась."
        cs_ls "Да. При условии, что материалы дела будут переданы в архив."
        cs_narrator "Славя покачала головой."
        cs_sl "Лена, ты невероятная."
        cs_narrator "Я посмотрела на неё."
        cs_ls "Не спорю. Иногда это даже мешает жить."
        if renpy.showing("cs_semen"):
            show cs_semen smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Семён рассмеялся."
    else:
        cs_narrator "Я улыбнулась."
        cs_ls "Хотела пожелать вам спокойного вечера."
        cs_narrator "Семён некоторое время смотрел на меня."
        cs_narrator "Потом кивнул."
        cs_sy "Спасибо. И тебе."
        if renpy.showing("sl"):
            show sl smile pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Славя улыбнулась."
        cs_sl "До завтра!"
        cs_narrator "Я кивнула."
        cs_ls "До завтра."
    cs_narrator "Я уже сделала несколько шагов."
    cs_narrator "Потом вдруг остановилась."
    cs_th "Нет."
    cs_th "Не потому, что хочу начать всё сначала."
    cs_th "Просто кое-что действительно забыла."
    cs_narrator "Я обернулась."
    cs_ls "Семён."
    cs_narrator "Он посмотрел на меня."
    cs_sy "Что?"
    cs_ls "Хорошего вечера."
    cs_narrator "Он на секунду замолчал."
    cs_narrator "Потом усмехнулся."
    cs_sy "И тебе, Соколова."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя улыбнулась."
    cs_narrator "Я кивнула."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "И продолжила путь."
    cs_th "Вот."
    cs_th "Получилось."
    cs_th "Можно было бы, конечно, снова устроить трагедию о предательстве."
    cs_th "Но одна хорошая шутка лучше пяти одинаковых."
    cs_th "А Семён, между прочим, умеет ответить так, что продолжать представление уже незачем."
    cs_th "Хорошо, что я вовремя остановилась и дала ему сказать своё."
    cs_narrator "Я улыбнулась."
    cs_th "Хотя вожатой я бы это объяснять не стала."
    return
