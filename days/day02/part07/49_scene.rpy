# -*- coding: utf-8 -*-
label cs_day02_49:
    $ save_name = "Чужая смена — День 2: Второй визит"
    $ cs_part06_live = False
    $ cs_part07_live = True
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    # cs_presence_keep: hide cs_dasha_winter
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
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)
    stop music fadeout 0.5
    label cs_check_part07_s49:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "До медпункта мы добрались без новых происшествий. Я старалась держать повреждённую руку так, чтобы не задевать ею одежду. Любое движение, натягивавшее кожу возле локтя, вызывало неприятное жжение."
    cs_narrator "Дарья несколько раз спрашивала, не нужно ли остановиться. Я каждый раз отрицательно качала головой. Не потому, что пыталась изображать героиню. Просто хотелось поскорее добраться до Виолы."
    cs_th "Какая удивительная перемена приоритетов. Ещё утром я рассматривала медпункт как очередную знакомую локацию. Теперь меня интересовали исключительно перевязочные материалы."
    cs_narrator "Мы поднялись на крыльцо."
    play sound "sound/sfx/knock_door7_polite.ogg"
    cs_narrator "Дарья постучала."
    cs_vi "Входите!"
    $ cs_director_scene("bg int_aidpost_day")
    scene bg int_aidpost_day
    # cs_presence_keep: hide cs_dasha_winter
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
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/medstation_inside_day.ogg":
        play ambience "sound/ambiences/medstation_inside_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.1, channel="ambience", delay=1.0)
    label cs_check_part07_clinic:
    cs_narrator "Она открыла дверь. Виола сидела за столом. Услышав нас, подняла голову. Посмотрела на Дарью."
    cs_narrator "Потом на меня, затем на платок возле моего локтя. И медленно отложила ручку."
    show cs custom surprised medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Лена?"
    cs_narrator "Я виновато улыбнулась."
    cs_ls "Добрый день. У вас есть программа лояльности для постоянных посетителей?"
    cs_narrator "Виола встала."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Что на этот раз?"
    cs_narrator "Я осторожно показала руку."
    cs_ls "Неудачное знакомство с корнем дерева."
    cs_narrator "Она подошла ближе. Посмотрела на повреждение."
    cs_vi "Это тот самый локоть, который я сегодня уже обрабатывала?"
    cs_ls "К сожалению, он решил продолжить знакомство с окружающей средой."
    show cs custom eyes_closed medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Виола вздохнула."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Садись на кушетку. Посмотрим, что ты натворила."
    cs_narrator "Дарья помогла мне устроиться. Виола подготовила всё необходимое. Осторожно убрала испачканный платок. Затем принялась снимать повреждённую повязку."
    cs_narrator "Я отвела взгляд."
    cs_th "Вот теперь даже неинтересно смотреть. Совсем."
    cs_vi "Рассказывай. Как упала?"
    cs_ls "Зацепилась туфлей за корень. Выставила руку, а локтем проехалась по дорожке."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Головой не ударялась?"
    cs_ls "Нет."
    cs_vi "Сознание не теряла? Не тошнило? Голова не кружится?"
    cs_ls "Нет. Только локоть и колено."
    cs_narrator "Виола кивнула. Проверила движения кисти и пальцев, осторожно осмотрела руку и попросила меня сказать, если какое-то движение вызывает резкую боль. Я выполнила её просьбу."
    cs_vi "Похоже, основная неприятность — обширная ссадина. Но грязи туда попало достаточно, так что обработать нужно как следует."
    cs_ls "Звучит не особенно вдохновляюще."
    show cs custom thoughtful medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Ничего приятного не обещаю. Зато потом будет лучше."
    cs_narrator "Я вздохнула."
    cs_ls "Прекрасное описание медицинских услуг."
    cs_narrator "Дарья стояла рядом. Виола посмотрела на неё."
    cs_vi "Молодец, что привела. И что не стала сама ковыряться в ране."
    cs_da "Я просто не хотела сделать хуже."
    cs_vi "Правильно."
    cs_narrator "Я посмотрела на них обеих."
    if cs_met_mz:
        cs_ls "Удивительно. Женя, Славя, теперь Виола. У Даши стремительно растёт профессиональная репутация."
    else:
        cs_ls "Удивительно. Славя, теперь Виола. У Даши стремительно растёт профессиональная репутация."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Лен, сейчас не время."
    cs_narrator "Я замолчала."
    cs_th "Да."
    cs_th "Кажется, действительно не время."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_treatment:
    cs_narrator "Виола начала осторожно промывать ссадину. Я невольно напряглась."
    cs_ls "Ай!"
    cs_vi "Знаю. Сейчас немного потерпи."
    cs_narrator "Я сжала пальцы здоровой руки. Попыталась сосредоточиться на шкафу напротив. На белой стене. На краю окна."
    cs_narrator "На чём угодно, кроме локтя. Но боль всё равно возвращала к себе внимание."
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я повернулась."
    cs_ls "М?"
    cs_narrator "Она протянула мне руку."
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Держи."
    cs_narrator "Я посмотрела на её ладонь, затем на неё. И осторожно взялась."
    cs_ls "Спасибо."
    # cs_presence_keep: hide cs_dasha_winter
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
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_seated:
    cs_narrator "Дарья села рядом, не мешая Виоле работать."
    cs_da "Смотри на меня."
    cs_narrator "Я выдохнула."
    cs_ls "Звучит как начало психологического эксперимента."
    cs_da "А мне казалось, ты любишь эксперименты."
    cs_narrator "Я невольно улыбнулась."
    cs_ls "Только те, в которых не участвует мой локоть."
    cs_narrator "Она тихо рассмеялась. Виола продолжила обработку. Постепенно неприятное жжение стало терпимее. Я всё ещё сжимала руку Дарьи."
    cs_narrator "Не особенно сильно. Просто держала. И это почему-то действительно помогало не отвлекаться на каждое движение Виолы."
    cs_th "Вчера я бы непременно придумала этому какое-нибудь идиотское объяснение. Что-нибудь о психологической стабилизации человеческого организма. Или о повышении эффективности обезболивания при тактильном контакте. А сейчас…"
    cs_th "Сейчас мне просто было спокойнее."
    return
