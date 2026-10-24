# -*- coding: utf-8 -*-
label cs_day03_101:
    $ save_name = "Чужая смена — День 3: Ещё один посетитель"
    if cs_viola_friend_before_day3 >= 2 and not cs_viola_day3_bonus_seen:
        if not cs_viola_spare_bandage:
            cs_narrator "Виола открыла ящик."
            cs_narrator "Достала небольшой запечатанный пакет с перевязочными материалами."
            cs_vi "Лена, возьми на всякий случай. Если повязка испачкается или отклеится, пригодится. Но если рана начнёт беспокоить, снова приходи ко мне."
            cs_narrator "Я удивилась."
            cs_ls "Спасибо."
            cs_narrator "Она улыбнулась."
            cs_vi "Только не воспринимай это как приглашение к новым травмам."
            cs_narrator "Я задумчиво кивнула."
            cs_ls "Очень предусмотрительное уточнение."
            if renpy.showing("cs_darya"):
                show cs_darya amused pioneer normal
                $ cs_presence_stage()
                with cs_sprite_change
            cs_narrator "Дарья рассмеялась."
            cs_narrator "Я взяла небольшой пакет здоровой рукой."
            $ cs_viola_spare_bandage = True
            label cs_check_day03_102_spare_given:
            cs_narrator "Я убрала запечатанный пакет в сумку, чтобы не потерять его по дороге."
        else:
            cs_vi "Запасная повязка ещё у тебя? Пусть остаётся в сумке. Если рука будет беспокоить, приходи."
            cs_ls "Да, она со мной. Спасибо."
        $ cs_viola_day3_bonus_seen = True
    else:
        cs_narrator "Виола ещё раз посмотрела на мою повязку."
        cs_vi "И не забывай, что я сказала."
        cs_narrator "Я улыбнулась."
        cs_ls "Без спорта, без падений и без попыток доказать, что организм умнее медицинских рекомендаций."
        cs_narrator "Она кивнула."
        cs_vi "Прекрасно."
    cs_narrator "Мы уже собирались прощаться."
    cs_narrator "Я поправила галстук."
    cs_narrator "Дарья подошла к двери."
    cs_narrator "И в этот момент раздался стук."
    cs_dv "Можно?"
    cs_narrator "Виола подняла голову."
    cs_vi "Входи."
    cs_narrator "Дверь приоткрылась."
    show dv normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_check_day03_101_alice:
    cs_narrator "На пороге появилась Алиса Двачевская."
    cs_narrator "Я удивлённо посмотрела на неё."
    cs_th "О."
    cs_th "Какие люди."
    cs_th "Кажется, сегодня медпункт решил собрать половину музыкального состава вчерашнего концерта."
    cs_narrator "Алиса заметила нас."
    cs_narrator "Остановилась."
    cs_dv "О. Вы здесь?"
    cs_narrator "Я улыбнулась."
    cs_ls "Как видишь."
    cs_narrator "Она посмотрела на мою повязку."
    cs_dv "Опять?"
    cs_narrator "Я вздохнула."
    cs_ls "Удивительно. Стоит вернуться на перевязку, и люди уже начинают считать тебя постоянным клиентом."
    if renpy.showing("dv"):
        show dv grin pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Алиса усмехнулась."
    cs_dv "А разве нет?"
    cs_narrator "Я задумалась."
    cs_ls "К сожалению, статистика против меня."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Алиса тоже улыбнулась."
    cs_narrator "Потом немного поправила руку."
    cs_narrator "Я заметила, что один из её пальцев обёрнут чистым платком."
    cs_narrator "Не туго."
    cs_narrator "Скорее так, чтобы ничего не задевать."
    cs_narrator "Виола тоже обратила на это внимание."
    cs_vi "Алиса, что случилось?"
    cs_narrator "Та поморщилась."
    cs_dv "Да ерунда. Со струной неудачно вышло."
    cs_narrator "Виола поднялась."
    cs_vi "Покажи."
    cs_narrator "Алиса посмотрела на нас."
    cs_narrator "Потом на медсестру."
    cs_dv "Может, сначала они выйдут?"
    cs_narrator "Я мгновенно кивнула."
    cs_ls "Конечно."
    cs_narrator "Виола посмотрела на неё."
    cs_vi "Хорошо. Девочки, вы уже закончили?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Спасибо за всё."
    cs_narrator "Я повернулась к Алисе."
    cs_narrator "Она всё ещё стояла возле двери."
    cs_ls "Надеюсь, ничего серьёзного."
    cs_narrator "Алиса пожала плечами."
    cs_dv "Ерунда, говорю же."
    cs_narrator "Я кивнула."
    cs_ls "Тогда не задерживаем."
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    show dv normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with Dissolve(0.8)
    play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.5
    label cs_check_day03_102_outside:
    cs_narrator "Мы вышли."
    cs_narrator "На улице я остановилась."
    cs_narrator "Дарья встала рядом."
    cs_narrator "Алиса тоже вышла на крыльцо, осторожно придерживая руку."
    cs_th "Так."
    cs_th "Судя по виду, ничего особенно страшного."
    cs_th "Но ей явно не нравится, когда на неё смотрят как на пострадавшую."
    cs_th "Знакомое ощущение."
    cs_th "Я сама последние два дня не слишком радовалась вниманию к собственному локтю."
    cs_narrator "Алиса заметила мой взгляд."
    cs_dv "Чего?"
    cs_narrator "Я улыбнулась."
    cs_ls "Ничего."
    if renpy.showing("dv"):
        show dv normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она прищурилась."
    cs_dv "Ага. У тебя на лице обычно не «ничего»."
    cs_narrator "Дарья тихо усмехнулась."
    cs_narrator "Я посмотрела на Алису."
    cs_th "Ну что ж."
    cs_th "Можно ответить привычной колкостью."
    cs_th "А можно поговорить нормально."
    cs_th "В конце концов, кажется, у нас есть кое-что общее."
    return
