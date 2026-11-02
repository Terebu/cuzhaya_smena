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
    cs_narrator "Вернувшись, я остановилась на крыльце и вытерла лоб. После пробежки и турника хотелось умыться."
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
    cs_narrator "Дарья всё ещё лежала, но уже не спала. Она повернула голову, когда я закрыла дверь."
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
    cs_narrator "Она приподнялась на локте. Осмотрела меня."
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
    cs_narrator "Я подошла к своей кровати. Но прежде чем сесть, посмотрела на мокрую футболку."
    cs_th "Нет."
    cs_th "Сначала хотя бы полотенце."
    cs_narrator "Взяла его со спинки стула и вытерла шею. Дарья наблюдала за мной."
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
    cs_narrator "Я рассказала про ворота и пустую дорогу."
    # cs_director_begin: Bus disappearance is a serious subject
    $ cs_frame_focus(["cs_darya"])
    show cs_darya worried pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    label cs_director_check_aedf775c9a:
    # cs_director_end
    cs_da "За территорию выходила?"
    cs_ls "Нет. Обещала ведь."
    cs_narrator "Дарья ненадолго опустила взгляд. Потом кивнула."
    cs_da "Спасибо."
    cs_narrator "Я взяла телефон с тумбочки."
    cs_ls "Семён предложил сходить к воротам вместе после завтрака."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "И ты согласилась?"
    cs_ls "Сказала, что сначала поговорю с тобой."
    cs_narrator "Она ненадолго задумалась."
    cs_da "Я не против посмотреть. Но давай не будем сразу уходить далеко по дороге."
    cs_ls "Согласна."
    cs_da "И ещё…"
    cs_ls "Что?"
    cs_narrator "Она посмотрела на мой телефон."
    cs_da "Ты ведь хотела сегодня снова пойти к Шурику и Электронику."
    cs_narrator "Я усмехнулась."
    cs_ls "Точно."
    cs_da "Тогда сначала завтрак. Потом клубы. А с дорогой решим, когда будем знать, сколько у нас времени."
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
    cs_narrator "Я посмотрела на неё. И не удержалась от улыбки."
    cs_ls "Помню."
    cs_da "Желательно без внезапных расследований за столом."
    cs_ls "Постараюсь."
    cs_narrator "Дарья приподняла бровь."
    cs_da "Опять «постараюсь»?"
    cs_ls "Даш, я с утра уже обнаружила исчезнувший автобус. Совсем без расследований сегодня, кажется, не получится."
    cs_narrator "Дарья встала с кровати."
    cs_da "Ладно. Тогда хотя бы сначала умойся."
    # cs_director_begin: Mirror focus after the conversation
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_7b10da8ab9:
    # cs_director_end
    cs_narrator "Я посмотрела на отражение: растрёпанные волосы и красное после пробежки лицо."
    return
