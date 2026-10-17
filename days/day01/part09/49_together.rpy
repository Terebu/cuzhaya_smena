# -*- coding: utf-8 -*-
label cs_day01_49:
    $ save_name = "Чужая смена — День 1: Дальше вместе"
    $ cs_director_scene("bg ext_houses_sunset")
    scene bg ext_houses_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.5)
    label cs_check_day01_part09_merge:
    $ renpy.music.set_volume(0.24,delay=1.0,channel="music")
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.35,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы продолжили путь между домиками."
    cs_narrator "Солнце уже клонилось к горизонту."
    cs_narrator "Длинные тени ложились на дорожку."
    cs_narrator "Где-то в стороне слышались голоса пионеров."
    cs_narrator "Я некоторое время шла молча."
    cs_narrator "Потом посмотрела на Дарью."
    cs_ls "Всё-таки странная здесь жизнь."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты о чём?"
    cs_narrator "Я кивнула в сторону лагеря."
    cs_ls "О том, как быстро обычные вещи перестают казаться обычными."
    cs_narrator "Дарья вопросительно посмотрела на меня."
    cs_ls "Ещё недавно для меня это были изображения на экране."
    cs_narrator "Я показала на домики."
    cs_ls "Вот фон. Вот дорожка. Вот место, где по сценарию должен появиться очередной персонаж."
    cs_narrator "Я помолчала."
    cs_ls "А теперь я могу просто свернуть не туда, и никакой сценарий не скажет, что делать дальше."
    cs_da "Может, это и хорошо?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Почему?"
    # cs_darya_variety: reaction
    show cs_darya explaining pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Потому что тогда у нас хотя бы есть возможность самим решать, что делать."
    cs_narrator "Я задумалась."
    cs_th "А ведь действительно."
    cs_narrator "В знакомой мне истории всё зависело от заранее подготовленных вариантов."
    cs_narrator "Здесь же я не могла даже уверенно сказать, какие события повторятся."
    cs_narrator "И повторятся ли вообще."
    cs_ls "То есть предлагаешь импровизировать?"
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А у нас есть другой выбор?"
    cs_narrator "Я улыбнулась."
    cs_ls "Похоже, нет."
    cs_narrator "Мы прошли мимо ещё одного домика."
    cs_narrator "По дорожке навстречу пробежали двое пионеров."
    cs_narrator "Где-то в окне негромко играло радио."
    cs_narrator "Вечер постепенно становился прохладнее."
    cs_narrator "Я поправила рубашку."
    cs_ls "Знаешь, ещё сегодня утром я бы не поверила, что мне придётся искать общий язык с целым советским пионерлагерем."
    cs_da "А теперь?"
    cs_ls "Теперь у меня есть домик, форма, знакомый Семён и заявка на ремонт телефона."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Насыщенный день."
    cs_ls "И это мы ещё до ужина не добрались."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "На мгновение захотелось снова сказать что-нибудь о нашем разговоре после кружка."
    cs_narrator "Но передумала."
    cs_narrator "Не потому, что мне было нечего сказать."
    cs_narrator "Просто не хотелось превращать каждую минуту рядом с ней в попытку выяснить, что она ко мне чувствует."
    cs_narrator "Она уже сказала достаточно."
    cs_narrator "И я услышала."
    cs_narrator "Пожалуй, иногда этого действительно хватает."
    return
