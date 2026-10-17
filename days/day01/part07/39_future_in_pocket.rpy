# -*- coding: utf-8 -*-
label cs_day01_39:
    $ save_name = "Чужая смена — День 1: Будущее в кармане"
    $ renpy.music.set_volume(0.30,delay=1.0,channel="music")
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/clubs_inside_day.ogg":
        play ambience "sound/ambiences/clubs_inside_day.ogg" fadeout 1.5 fadein 2.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "sh", "el"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Электроник всё ещё смотрел на мой карман, словно телефон мог внезапно включиться и продемонстрировать всю историю вычислительной техники."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Слушай, Лена."
    cs_ls "М?"
    cs_el "А ты сказала, что миллиарды людей общаются через компьютеры."
    cs_ls "Ну да."
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "И что они там делают?"
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Например, выкладывают фотографии и видео. Другие люди их смотрят, обсуждают, подписываются на авторов."
    cs_narrator "Электроник задумался."
    cs_el "Подписываются?"
    cs_ls "Условно говоря, начинают следить за публикациями человека."
    cs_el "Как за газетой?"
    cs_ls "Примерно. Только газету может выпускать почти любой желающий."
    cs_narrator "Он посмотрел на меня внимательнее."
    cs_el "И ты тоже?"
    cs_narrator "Я кивнула."
    cs_ls "У меня было почти двести пятьдесят тысяч подписчиков."
    cs_narrator "Шурик поднял голову."
    show sh surprise pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "Сколько?"
    cs_ls "Почти четверть миллиона."
    show sh normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "И они знают тебя?"
    cs_narrator "Я задумалась."
    cs_ls "Некоторые. Большинство просто смотрят, что я публикую."
    cs_narrator "Электроник нахмурился."
    cs_el "А зачем им твои фотографии?"
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya smile pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Та уже начинала улыбаться."
    cs_ls "Вот. Ещё один прекрасный вопрос."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Я серьёзно!"
    cs_ls "И я."
    cs_narrator "Я присела на край свободного стула."
    cs_ls "Людям интересно смотреть, что делают другие. Кто-то рисует, кто-то снимает видео, кто-то рассказывает о своей работе или увлечениях."
    cs_narrator "Шурик задумчиво кивнул."
    cs_sh "Значит, можно показывать свои разработки?"
    cs_ls "Разумеется."
    cs_sh "И обсуждать их с людьми из других городов?"
    cs_ls "Даже из других стран."
    cs_narrator "Шурик посмотрел на Электроника."
    cs_narrator "В глазах обоих появился совершенно одинаковый интерес."
    cs_th "Ну вот."
    cs_th "Нашли практическое применение."
    cs_narrator "Электроник вдруг спросил:"
    show el surprise pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "А можно будет увидеть всё это на твоём телефоне?"
    cs_ls "Если он заработает, кое-что из сохранённого покажу. Но интернет здесь сам по себе не появится."
    cs_el "Почему?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Потому что для него нужна целая инфраструктура. Мобильные сети, оборудование, связь с другими устройствами…"
    cs_narrator "Он вздохнул."
    show el smile pioneer far at cs_actor_far_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_el "Понятно."
    cs_narrator "Я кивнула."
    cs_ls "Пять вольт мы, возможно, найдём. А вот глобальную сеть придётся строить несколько дольше."
    show cs_darya amused pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    show sh smile pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Шурик впервые за разговор тоже улыбнулся."
    cs_narrator "Я поднялась."
    cs_ls "Ладно, товарищи инженеры. Спасибо за консультацию."
    cs_narrator "Электроник махнул рукой."
    cs_el "Заходите ещё!"
    cs_ls "Завтра обязательно."
    cs_narrator "Шурик добавил:"
    show sh normal pioneer far at cs_actor_far_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sh "И телефон не забудь."
    cs_narrator "Я коснулась кармана."
    cs_ls "Теперь это будет довольно сложно."
    cs_narrator "Мы с Дарьей направились к двери."
    cs_narrator "Но уже на пороге она тихо спросила:"
    show cs_darya thinking pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен, а тебе не кажется, что мы слишком много им рассказали?"
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела на Шурика и Электроника."
    cs_narrator "Они уже склонились над столом, оживлённо обсуждая, каким образом можно подготовить подходящий источник питания."
    cs_th "Да."
    cs_th "Кажется."
    cs_ls "Есть такое."
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты ведь сама говорила, что не стоит рассказывать всем подряд."
    cs_ls "Говорила."
    show cs_darya thinking pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И?"
    cs_narrator "Я немного помолчала."
    cs_ls "Похоже, научно-технический прогресс временно подавил у меня инстинкт самосохранения."
    cs_narrator "Дарья покачала головой."
    show cs_darya shrug pioneer far at cs_darya_far_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Главное, чтобы потом не пришлось объясняться с Ольгой Дмитриевной."
    cs_narrator "Я посмотрела в сторону выхода."
    cs_ls "Тогда будем надеяться, что местные инженеры умеют хранить профессиональные секреты."
    cs_narrator "Дарья открыла дверь."
    cs_narrator "Снаружи нас снова встретил летний воздух."
    play sound "sound/sfx/open_door_clubs.ogg"
    $ cs_director_scene("bg ext_clubs_day")
    scene bg ext_clubs_day
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    with Dissolve(1.0)
    $ renpy.music.set_volume(0.25,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.5 fadein 2.0
    label cs_check_day01_part07_exit:
    cs_narrator "Я вышла на крыльцо."
    cs_narrator "За спиной остался кружок электроники."
    cs_narrator "Впереди — весь остальной «Совёнок»."
    cs_narrator "Я коснулась кармана, в котором лежал телефон."
    cs_narrator "Пока он оставался бесполезным куском стекла, металла и кремния."
    cs_narrator "Но теперь хотя бы появилась возможность это изменить."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Ну что?"
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Первый научно-технический проект нашей смены официально запущен."
    cs_narrator "Она улыбнулась."
    cs_da "И какие результаты?"
    cs_narrator "Я задумалась."
    cs_ls "Никаких."
    cs_narrator "Небольшая пауза."
    cs_ls "Но энтузиазм исполнителей исключительно высокий."
    # cs_director_begin: Independent recap after the electronics errand
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_103eb8e099:
    # cs_director_end
    cs_th "Молодец, Лена."
    cs_th "Приехала за продуктами."
    cs_th "Получила пионерский галстук, домик и собственную программу развития советской электроники."
    cs_th "План на день можно считать перевыполненным."
    return
