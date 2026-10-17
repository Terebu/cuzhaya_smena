# -*- coding: utf-8 -*-
label cs_day02_07:
    $ save_name = "Чужая смена — День 2: Возвращение"
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
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
    play ambience "sound/ambiences/int_cabin_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.22, channel="ambience", delay=1.0)
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.22, channel="music", delay=1.0)
    label cs_check_new_d2_s07:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Когда я вернулась, солнце уже заметно поднялось."
    cs_narrator "Я остановилась на крыльце."
    cs_narrator "Перевела дыхание."
    cs_narrator "Вытерла лоб предплечьем."
    cs_narrator "Ноги приятно устали."
    cs_narrator "Руки после турника тоже напоминали о себе."
    cs_th "Неплохо."
    cs_th "Первый спортивный день в «Совёнке» официально открыт."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day
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
    cs_narrator "Я осторожно вошла в домик."
    # cs_director_begin: Return indoors: Darya participates despite lying down
    $ cs_frame_focus(["cs_darya"])
    show cs_darya neutral pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_95df4f349e:
    # cs_director_end
    cs_narrator "Дарья всё ещё лежала, но уже не спала."
    cs_narrator "Она повернула голову, когда я закрыла дверь."
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
    cs_da "Вернулась?"
    cs_ls "Как видишь. Экспедиция завершена успешно."
    cs_narrator "Она приподнялась на локте."
    cs_narrator "Осмотрела меня."
    cs_da "Ты вся вспотела."
    cs_narrator "Я посмотрела на свою футболку."
    cs_ls "Есть такое."
    cs_da "Давно бегала?"
    cs_ls "Успела сделать круг по лагерю, немного позаниматься и встретить двух знакомых."
    cs_narrator "Дарья села."
    cs_da "Каких?"
    cs_narrator "Я начала загибать пальцы."
    cs_ls "Ольгу Дмитриевну. Семёна."
    cs_da "И что они сказали?"
    cs_ls "Ольга Дмитриевна похвалила меня за физкультуру, а Семён попытался понять, зачем человеку добровольно просыпаться раньше всех."
    # cs_director_begin: Warm reaction during the uninterrupted morning conversation
    $ cs_frame_focus(["cs_darya"])
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_d495fc5820:
    # cs_director_end
    cs_narrator "Дарья тихо рассмеялась."
    cs_da "Вполне разумный вопрос."
    cs_ls "Заговор против жаворонков."
    cs_narrator "Я подошла к своей кровати."
    cs_narrator "Но прежде чем сесть, посмотрела на мокрую футболку."
    cs_th "Нет."
    cs_th "Сначала хотя бы полотенце."
    cs_narrator "Взяла его со спинки стула и вытерла шею."
    cs_narrator "Дарья наблюдала за мной."
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
    cs_da "А больше ничего не случилось?"
    cs_narrator "Я замолчала."
    cs_narrator "Потом посмотрела на неё."
    cs_ls "Случилось."
    # cs_director_begin: Bus disappearance is a serious subject
    $ cs_frame_focus(["cs_darya"])
    show cs_darya worried pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_aedf775c9a:
    # cs_director_end
    cs_narrator "Её улыбка исчезла."
    cs_da "Что?"
    cs_narrator "Я присела на край собственной кровати."
    cs_ls "Автобус исчез."
    cs_narrator "Дарья несколько секунд смотрела на меня."
    cs_da "В каком смысле?"
    cs_ls "В самом обычном. Его больше нет возле ворот."
    cs_narrator "Она медленно выпрямилась."
    cs_da "Ты ходила туда?"
    cs_ls "Да. Во время пробежки."
    cs_da "За территорию выходила?"
    cs_ls "Нет."
    cs_narrator "Я посмотрела ей в глаза."
    cs_ls "Обещала ведь."
    cs_narrator "Дарья ненадолго опустила взгляд."
    cs_narrator "Потом кивнула."
    cs_da "Спасибо."
    cs_narrator "Я немного помолчала."
    cs_ls "Не за что."
    cs_narrator "Она задумалась."
    cs_da "А может, он просто уехал?"
    cs_narrator "Я пожала плечами."
    cs_ls "Может."
    cs_da "Но куда?"
    cs_ls "Вот это и хочется выяснить."
    cs_narrator "Я взяла телефон с тумбочки."
    cs_narrator "Экран по-прежнему оставался чёрным."
    cs_narrator "Повернула его в руке."
    cs_ls "Семён предложил сходить к воротам вместе после завтрака."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "И ты согласилась?"
    cs_ls "Сказала, что сначала поговорю с тобой."
    cs_narrator "Она ненадолго задумалась."
    cs_da "Я не против посмотреть. Но давай не будем сразу уходить далеко по дороге."
    cs_narrator "Я кивнула."
    cs_ls "Согласна."
    cs_da "И ещё…"
    cs_ls "Что?"
    cs_narrator "Она посмотрела на мой телефон."
    cs_da "Ты ведь хотела сегодня снова пойти к Шурику и Электронику."
    cs_narrator "Я усмехнулась."
    cs_ls "Точно."
    cs_da "Тогда сначала завтрак. Потом клубы. А с дорогой решим, когда будем знать, сколько у нас времени."
    cs_narrator "Я задумчиво кивнула."
    # cs_director_begin: Morning plans agreed
    $ cs_frame_focus(["cs_darya"])
    show cs_darya neutral pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_27f52f7702:
    # cs_director_end
    cs_ls "Хороший план."
    cs_narrator "Она улыбнулась."
    cs_da "Ты вчера обещала мне обычный завтрак."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И не удержалась от улыбки."
    cs_ls "Помню."
    cs_da "Желательно без внезапных расследований за столом."
    cs_ls "Постараюсь."
    cs_narrator "Дарья приподняла бровь."
    cs_da "Опять «постараюсь»?"
    cs_ls "Даш, я с утра уже обнаружила исчезнувший автобус. Совсем без расследований сегодня, кажется, не получится."
    cs_narrator "Она рассмеялась."
    cs_narrator "Потом встала с кровати."
    cs_da "Ладно. Тогда хотя бы сначала умойся."
    # cs_director_begin: Mirror focus after the conversation
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_7b10da8ab9:
    # cs_director_end
    cs_narrator "Я посмотрела на своё отражение в небольшом зеркале."
    cs_narrator "Растрёпанные волосы."
    cs_narrator "Разгорячённое лицо."
    cs_narrator "Спортивная футболка."
    cs_th "Да."
    cs_th "Пожалуй, выглядит убедительно."
    return
