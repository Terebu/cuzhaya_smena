# -*- coding: utf-8 -*-
label cs_day02_56:
    $ save_name = "Чужая смена — День 2: Разговор на лавочке"
    $ cs_part07_live = False
    $ cs_part08_live = True
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/lets_be_friends.ogg":
        play music "sound/music/lets_be_friends.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.16, channel="music", delay=1.0)
    label cs_check_part08_s56:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Некоторое время мы просто сидели."
    cs_narrator "Семён снова взял карандаш."
    cs_narrator "Дарья смотрела на площадь, где несколько пионеров переставляли скамейки перед вечерним выступлением."
    cs_narrator "А я пыталась устроиться удобнее."
    cs_narrator "Что оказалось не особенно трудно."
    cs_narrator "Хотя совершенно неожиданно выяснилось, что даже обычное сидение на лавочке требует некоторого участия локтевых суставов."
    cs_th "Вот ведь."
    cs_th "Пока ничего не болит, вообще не замечаешь, сколько раз за день опираешься на руку."
    cs_narrator "Я осторожно положила её на колени."
    # cs_director_begin: REFLECTIVE_SHOT: Square panorama and three displaced people
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_b4cefde74c:
    # cs_director_end
    cs_narrator "И посмотрела вперёд."
    cs_narrator "Площадь была удивительно спокойной."
    cs_narrator "По дорожке проходили пионеры."
    cs_narrator "Где-то разговаривали девочки."
    cs_narrator "Издали доносился смех."
    cs_narrator "Если не знать, что сегодня произошло за воротами, можно было решить, что всё здесь совершенно нормально."
    cs_narrator "Трое знакомых сидят на лавочке."
    cs_narrator "Обсуждают занятия."
    cs_narrator "Ждут ужина."
    cs_narrator "Вечером пойдут слушать музыку."
    cs_th "И ни один из нас не должен находиться здесь."
    # cs_director_begin: Return to direct interaction: Square panorama and three displaced people
    $ cs_frame_focus(["cs_darya", "cs_semen"])
    with cs_sprite_change
    label cs_director_check_57427f3ded:
    # cs_director_end
    cs_narrator "Семён первым нарушил молчание."
    cs_sy "Я всё думаю о дороге."
    cs_narrator "Я посмотрела на него."
    cs_ls "Я тоже."
    cs_sy "Особенно о том, как мы второй раз вернулись к кусту."
    cs_narrator "Дарья кивнула."
    cs_da "Мне до сих пор трудно представить, как это произошло. Мы ведь специально следили за направлением."
    cs_sy "Вот именно. Я даже время засекал."
    cs_narrator "Я ненадолго задумалась."
    cs_ls "Самое неприятное, что мы пока не понимаем, какая именно часть наших наблюдений неправильная."
    cs_narrator "Он повернулся ко мне."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты думаешь, мы ошиблись?"
    cs_ls "Я думаю, что кто-нибудь обязательно предложит такое объяснение. Поэтому в следующий раз придётся проверять всё ещё аккуратнее."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Только не сегодня."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Сегодня исследовательская деятельность официально приостановлена."
    cs_sy "Как и спортивная?"
    cs_ls "Да. Мой сегодняшний рабочий график состоит преимущественно из вынужденного отдыха."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он усмехнулся."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Наконец-то."
    cs_narrator "Мы немного помолчали."
    cs_narrator "Потом Семён спросил:"
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "А завтра что будем делать?"
    cs_narrator "Я задумалась."
    cs_th "Хороший вопрос."
    cs_narrator "Мне уже хотелось составить целый список."
    cs_narrator "Взять у Шурика что-нибудь для измерений."
    cs_narrator "Попробовать набросать маршрут."
    cs_narrator "Отметить расстояния."
    cs_narrator "Сравнить направление дороги с положением солнца."
    cs_narrator "Возможно, поискать старую карту окрестностей."
    cs_narrator "Но потом вспомнила Ольгу Дмитриевну."
    cs_narrator "И её реакцию возле ворот."
    cs_ls "Для начала стоит выяснить, есть ли у лагеря карта окрестностей."
    cs_sy "Думаешь, поможет?"
    cs_ls "Не знаю. Но хотя бы станет понятно, куда эта дорога должна вести при нормальных обстоятельствах."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья задумалась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "И ещё можно попробовать спросить у кого-нибудь из взрослых, как обычно добираются до лагеря."
    cs_narrator "Я кивнула."
    cs_ls "Только без рассказов о пространственных петлях с самого начала."
    cs_narrator "Семён улыбнулся."
    cs_sy "Это ты сейчас сама себе совет даёшь?"
    cs_narrator "Я посмотрела на него."
    cs_ls "Между прочим, вполне заслуженно."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Он рассмеялся."
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Тогда хорошая идея."
    cs_narrator "Некоторое время мы обсуждали, где вообще могла находиться такая карта."
    cs_narrator "Семён предположил, что какие-нибудь схемы есть у Ольги Дмитриевны."
    cs_narrator "Дарья предложила проверить библиотеку."
    cs_narrator "Я вспомнила Женю."
    cs_th "О."
    cs_th "Возможно, это действительно неплохое направление."
    cs_narrator "Но пока не хотелось превращать случайный отдых в очередной поход по лагерю с расспросами."
    cs_narrator "К тому же в нашем распоряжении оставался весь завтрашний день."
    cs_narrator "По крайней мере, я очень надеялась, что это действительно так."
    show cs_semen serious pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Знаешь, я ещё кое-чего не понимаю."
    cs_narrator "Я повернулась."
    cs_ls "Чего?"
    cs_sy "Почему Ольга Дмитриевна так разозлилась?"
    cs_narrator "Дарья немного помолчала."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Потому что мы вышли за территорию без предупреждения."
    cs_sy "Это понятно. Но когда мы начали рассказывать про дорогу, она как-то странно отреагировала."
    cs_narrator "Я кивнула."
    cs_ls "Мне тоже показалось."
    cs_narrator "Затем добавила:"
    cs_ls "Только давай не будем заранее решать, что она что-то скрывает."
    cs_narrator "Семён посмотрел на меня."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ты серьёзно?"
    cs_narrator "Я приподняла бровь."
    cs_ls "А что?"
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Вчера ты была готова придумать десять теорий после каждой необычной фразы."
    cs_narrator "Я задумалась."
    cs_narrator "Потом усмехнулась."
    cs_ls "Вчера я ещё не прошла полный курс повышения квалификации."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А сегодня?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Сегодня я дважды побывала у Виолы. Это сильно способствует переосмыслению жизненных приоритетов."
    cs_narrator "Все трое рассмеялись."
    cs_narrator "Потом я стала серьёзнее."
    cs_ls "Если говорить без шуток, мне действительно кажется, что Ольга Дмитриевна знает больше, чем говорит. Но пока это только впечатление."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Значит, проверим."
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part08_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Завтра?"
    cs_ls "Не обязательно прямо завтра. Главное, чтобы это было разумно."
    cs_narrator "Он кивнул."
    if cs_friend_se >= 2:
        show cs_semen relaxed pioneer normal at cs_semen_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    else:
        show cs_semen neutral pioneer normal at cs_semen_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
    label cs_check_part08_trust:
    cs_narrator "И почему-то после этого мне стало немного легче."
    cs_narrator "Мы по-прежнему не понимали, что происходит."
    cs_narrator "Зато теперь не пытались решить всё немедленно."
    cs_th "Маленькая победа здравого смысла."
    cs_th "Причём на этот раз даже без чьего-либо падения."
    return
