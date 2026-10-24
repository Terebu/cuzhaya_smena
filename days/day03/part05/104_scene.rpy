# -*- coding: utf-8 -*-
label cs_day03_104:
    $ save_name = "Чужая смена — День 3: Новая профессия Соколовой"
    # revised_medpoint_bridge: the decision was already made in part 4.
    label cs_check_day03_104:
    if cs_day03_medpoint_revision_done and not cs_day03_part05_legacy_entry:
        cs_narrator "По дороге к домику вожатой я ещё раз посмотрела на повязку."
        cs_ls "Помочь можно и без подвигов. Начнём с чего-нибудь, для чего не нужны обе руки."
        cs_da "Вот с этого и начни разговор."
    else:
        if cs_day03_part05_legacy_entry:
            $ cs_director_scene("cs_camp_path_day")
            scene cs_camp_path_day
            show cs_darya neutral pioneer normal at cs_darya_normal_right
            $ cs_presence_stage()
            with Dissolve(0.8)
        else:
            $ cs_director_scene("bg ext_aidpost_day")
            scene bg ext_aidpost_day
            show cs_darya neutral pioneer normal at cs_darya_normal_right
            $ cs_presence_stage()
            with Dissolve(0.8)
        if renpy.music.get_playing() != "sound/music/my_daily_life.ogg":
            play music "sound/music/my_daily_life.ogg" fadein 2.0
        play ambience "sound/ambiences/camp_center_day.ogg" fadein 1.0
        if cs_day03_part05_legacy_entry:
            cs_narrator "Мы ещё не успели далеко уйти от развилки, когда мне в голову пришла очередная мысль."
        else:
            cs_narrator "От медпункта мы успели отойти всего на несколько шагов, когда мне в голову пришла очередная мысль."
        cs_narrator "Причём на этот раз даже полезная."
        cs_narrator "Я остановилась."
        cs_narrator "Дарья тоже."
        cs_narrator "Она посмотрела на меня."
        cs_da "Что-то забыла?"
        cs_narrator "Я задумчиво поправила галстук."
        cs_narrator "Посмотрела в сторону площади."
        cs_narrator "Потом снова на неё."
        cs_ls "Нет. Просто решила, что сегодняшняя культурная программа ещё недостаточно насыщенна."
        if renpy.showing("cs_darya"):
            show cs_darya thinking pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья приподняла бровь."
        cs_da "Мы только что были у Виолы."
        cs_ls "Именно. А теперь предлагаю посетить ещё одного чрезвычайно влиятельного человека."
        if renpy.showing("cs_darya"):
            show cs_darya thinking pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Она посмотрела на меня с подозрением."
        cs_da "Кого?"
        cs_narrator "Я выпрямилась."
        cs_ls "Ольгу Дмитриевну."
        cs_narrator "Дарья некоторое время молчала."
        cs_narrator "Потом осторожно спросила:"
        cs_da "Зачем?"
        cs_narrator "Я приложила здоровую руку к груди."
        cs_ls "Предложить помощь."
        cs_narrator "Она остановилась окончательно."
        cs_narrator "Посмотрела на меня."
        cs_narrator "Затем медленно улыбнулась."
        cs_da "Добровольно?"
        cs_ls "Между прочим, да."
        cs_da "Без предварительного распоряжения?"
        cs_ls "Даша, я начинаю чувствовать некоторое недоверие к моим трудовым качествам."
        cs_narrator "Она рассмеялась."
        cs_da "Просто неожиданно."
        cs_narrator "Я кивнула."
        cs_ls "Справедливо. Моя репутация человека, который самостоятельно находит себе занятия, пока ещё формируется."
        cs_narrator "Немного подумала."
        cs_ls "Хотя вчера я добровольно помогала с плакатом."
        cs_da "И добровольно полезла исследовать дорогу."
        cs_narrator "Я посмотрела на неё."
        cs_th "Так."
        cs_th "Аргумент неприятный."
        cs_th "И, что хуже всего, совершенно обоснованный."
        cs_ls "Вот именно поэтому сегодня предлагаю заняться общественно полезной деятельностью на официально утверждённой территории лагеря."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Уже лучше."
    cs_narrator "Я сделала шаг вперёд."
    cs_narrator "Потом остановилась."
    cs_ls "Хотя есть ещё один вопрос, который давно требует исследования."
    cs_narrator "Она вздохнула."
    cs_da "Какой?"
    cs_narrator "Я понизила голос."
    cs_ls "Мне всё ещё интересно, как Ольга Дмитриевна терпит Семёна под одной крышей."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Несколько секунд молчала."
    cs_da "Лена."
    cs_narrator "Я невинно моргнула."
    cs_ls "Что?"
    cs_da "Ты опять собираешься расспрашивать её о личной жизни?"
    cs_narrator "Я задумалась."
    cs_ls "Нет. Мне скорее интересна организация совместного быта."
    cs_da "Конечно."
    cs_ls "Представь: два человека, один домик, ограниченное количество личного пространства. Чисто исследовательский вопрос."
    cs_narrator "Она покачала головой."
    cs_da "А ты ещё утром рассказывала мне о правилах проживания."
    cs_narrator "Я посмотрела на неё."
    cs_th "А вот это уже удар ниже пояса."
    cs_ls "Значит, если Ольга Дмитриевна попросит не обсуждать её личные дела, я не буду."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Правда."
    cs_narrator "Она посмотрела на меня ещё секунду."
    cs_da "Тогда пойдём."
    cs_narrator "Я довольно улыбнулась."
    cs_th "Вот и хорошо."
    cs_th "Дипломатическая миссия одобрена."
    cs_th "Теперь главное — не сорвать переговоры в первые тридцать секунд."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya neutral pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы свернули к домикам."
    return
