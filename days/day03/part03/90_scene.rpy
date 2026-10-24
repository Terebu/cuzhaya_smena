# -*- coding: utf-8 -*-
label cs_day03_90:
    $ save_name = "Чужая смена — День 3: Знакомые очки"
    $ cs_director_scene("bg ext_dining_hall_away_day")
    scene bg ext_dining_hall_away_day
    show cs_darya shy_smile pioneer normal at Transform(xpos=0.75, xanchor=0.5, ypos=1.60, yanchor=1.0)
    $ cs_presence_stage()
    with Dissolve(0.8)
    # cs_authored_pov_0: Lena looks for Zhenya among the crowd
    $ cs_frame_focus([])
    with cs_sprite_change
    cs_narrator "У столовой уже собирался народ."
    cs_narrator "Возле входа Мику что-то оживлённо рассказывала Славе."
    cs_narrator "Та слушала, время от времени улыбаясь и кивая."
    cs_narrator "Чуть дальше Алиса спорила с Ульяной."
    cs_narrator "Причём, судя по выражениям лиц, предмет спора был чрезвычайно важным."
    cs_narrator "Возможно, речь шла о распределении обязанностей."
    cs_narrator "Возможно, о том, кто вчера громче хлопал на концерте."
    cs_narrator "А возможно, об очередной совершенно незначительной вещи, которая в исполнении этих двоих уже успела превратиться в принципиальный вопрос."
    cs_th "Обычное утро в «Совёнке»."
    cs_th "Ничего необычного."
    cs_narrator "Семён, которого мы незадолго до этого встретили на дорожке, уже стоял возле крыльца и разговаривал с кем-то из пионеров."
    cs_narrator "Я только кивнула ему издалека."
    cs_narrator "Он кивнул в ответ."
    cs_th "Вот."
    cs_th "Второй акт вежливого общения."
    cs_th "День определённо войдёт в историю."
    cs_narrator "Но искала я глазами совсем другого человека."
    cs_narrator "И вскоре нашла."
    cs_narrator "Женя стояла немного в стороне от входа."
    cs_narrator "В одной руке держала книгу, другой поправляла очки."
    cs_narrator "Выглядела вполне довольной тем, что вокруг неё пока никто не пытался начинать особенно длинный разговор."
    cs_narrator "Я направилась к ней."
    # cs_authored_pov_1: The three meet and converse together
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Дарья пошла рядом."
    cs_narrator "Женя заметила нас примерно за пару метров."
    cs_narrator "Подняла взгляд."
    with None
    show cs_zhenya normal pioneer normal at cs_day03_p3_actor_enter(0.25)
    $ renpy.pause(0.30, hard=True)
    show cs_zhenya normal pioneer normal at Transform(xpos=0.25, xanchor=0.5, ypos=1.60, yanchor=1.0, zoom=1.0, alpha=1.0)
    $ cs_presence_stage()
    with None
    label cs_check_day03_90_zhenya:
    cs_ls "Доброе утро, Женя."
    cs_narrator "Она посмотрела на меня."
    cs_mz "Доброе."
    cs_narrator "Я улыбнулась."
    cs_ls "Как спалось?"
    if renpy.showing("cs_zhenya"):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя на секунду удивилась."
    cs_narrator "Потом пожала плечами."
    cs_mz "Нормально. А тебе?"
    cs_ls "Хорошо. Правда, проснулась раньше горна."
    cs_narrator "Она заметила мою повязку."
    cs_mz "Опять бегала?"
    cs_narrator "Я слегка усмехнулась."
    cs_ls "Попробовала. Но локоть быстро напомнил, что вчерашнее происшествие ещё не забыто."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya arms_crossed pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя нахмурилась."
    cs_mz "Тогда зачем?"
    cs_ls "Захотелось проверить, смогу ли. Выяснила, что пока лучше просто ходить."
    cs_narrator "Она кивнула."
    cs_mz "Разумно."
    cs_narrator "Я улыбнулась."
    cs_ls "Стараюсь."
    cs_narrator "Женя посмотрела на меня ещё раз."
    cs_narrator "Потом на Дарью."
    cs_mz "Она сегодня какая-то спокойная."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "У неё с утра культурная реформа."
    cs_narrator "Я медленно повернула голову."
    cs_th "Предательница."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya thinking pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя приподняла бровь."
    cs_mz "Какая ещё реформа?"
    cs_narrator "Я поправила галстук."
    cs_ls "Решила немного сократить количество необязательных разговоров."
    cs_narrator "Женя посмотрела на меня."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Потом едва заметно улыбнулась."
    cs_mz "Неплохое начинание."
    cs_ls "Спасибо."
    cs_narrator "Пауза."
    cs_narrator "Никакой дополнительной реплики."
    cs_narrator "Я просто осталась стоять рядом."
    cs_narrator "Женя посмотрела на книгу."
    cs_narrator "Затем на дверь столовой."
    cs_narrator "И, кажется, постепенно перестала ожидать продолжения."
    if cs_friend_mz >= 2:
        cs_narrator "Женя сама повернулась ко мне."
        cs_mz "Кстати, я вспомнила ещё одну книгу, которая тебе может понравиться."
        cs_narrator "Я заинтересованно посмотрела на неё."
        cs_ls "Правда?"
        cs_narrator "Она кивнула."
        cs_mz "Да. Только сначала хотела узнать, что ты обычно предпочитаешь читать."
        cs_narrator "Я немного подумала."
        cs_ls "Истории, где персонажи интереснее самого конфликта. Но вообще зависит от настроения."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shy pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя улыбнулась."
        cs_mz "Тогда, кажется, знаю, что предложить."
        cs_narrator "Я кивнула."
        cs_ls "Буду рада посмотреть."
    elif cs_friend_mz == 1 and cs_lena_book_returned:
        cs_narrator "Женя посмотрела на книгу в своей руке."
        cs_mz "Ты вчера довольно быстро дочитала."
        cs_narrator "Я кивнула."
        cs_ls "Да. Последние главы оказались интереснее, чем я ожидала."
        cs_narrator "Она улыбнулась."
        cs_mz "Бывает. Иногда первые главы просто нужно пережить."
        cs_narrator "Я тихо рассмеялась."
        cs_ls "Хорошее описание некоторых книг."
    else:
        cs_narrator "Женя ненадолго вернулась к своей книге."
        cs_narrator "Я посмотрела на крыльцо."
        cs_th "Кажется, сейчас начнут пускать внутрь."
        cs_narrator "Разговор естественно закончился."
        cs_narrator "И мне не хотелось начинать новый только ради того, чтобы нарушить тишину."
    cs_narrator "Двери столовой открылись."
    cs_narrator "Пионеры начали заходить."
    cs_narrator "Женя убрала книгу под мышку."
    cs_mz "Ну что, идём?"
    cs_narrator "Я кивнула."
    cs_ls "Пойдём."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_narrator "И мы направились внутрь."
    return
