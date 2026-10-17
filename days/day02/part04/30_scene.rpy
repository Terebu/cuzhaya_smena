# -*- coding: utf-8 -*-
label cs_day02_30:
    $ save_name = "Чужая смена — День 2: Алёшенька"
    $ cs_part03_live = False
    $ cs_part04_live = True
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
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    if renpy.music.get_playing() != "sound/music/just_think.ogg":
        play music "sound/music/just_think.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.14, channel="music", delay=1.0)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/medstation_inside_day.ogg":
        play ambience "sound/ambiences/medstation_inside_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.08, channel="ambience", delay=1.0)
    label cs_check_part04_s30:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    # cs_director_begin: REFLECTIVE_SHOT: Anatomical poster and remembered dates
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_c2a563ebcd:
    # cs_director_end
    cs_narrator "Я медленно повернула голову."
    # cs_presence_keep: hide cs_darya
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
    $ cs_part04_cast = []
    label cs_check_part04_poster_observation:
    cs_narrator "На стене висел анатомический плакат."
    cs_narrator "Странный."
    cs_narrator "Очень странный."
    cs_narrator "На нём было изображено маленькое существо с необычной формой головы и непропорциональным телом."
    cs_narrator "Не совсем привычная анатомическая иллюстрация."
    cs_narrator "Но дело было даже не в этом."
    cs_narrator "Я уже видела этот рисунок."
    cs_th "Подожди."
    cs_th "Только не говори, что он действительно здесь."
    cs_narrator "Я поднялась со стула."
    cs_narrator "Подошла ближе."
    cs_narrator "Присмотрелась."
    cs_narrator "Чем дольше я рассматривала изображение, тем отчётливее вспоминала обсуждения этого плаката среди поклонников оригинальной новеллы."
    cs_th "Алёшенька."
    cs_th "Кыштымский карлик."
    cs_th "Девяносто шестой год."
    cs_narrator "Я медленно выдохнула."
    # cs_director_begin: Return to direct interaction: Anatomical poster and remembered dates
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_5752982251:
    # cs_director_end
    cs_ls "Вот это уже интересно."
    cs_narrator "Дарья подошла ближе."
    cs_da "Что там?"
    cs_narrator "Я указала на плакат."
    cs_ls "Узнаёшь?"
    cs_narrator "Она несколько секунд рассматривала изображение."
    cs_da "Не особенно. А должна?"
    cs_narrator "Я покачала головой."
    cs_ls "Не обязательно."
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
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part04_viola_restored:
    cs_narrator "Виола заметила наш интерес."
    cs_vi "Что-то не так?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Затем снова на плакат."
    cs_ls "Можно спросить, откуда он у вас?"
    cs_narrator "Виола подошла ближе."
    cs_vi "Этот?"
    cs_ls "Да."
    cs_narrator "Она немного задумалась."
    cs_vi "Честно говоря, точно не знаю. Он здесь висел ещё до того, как я начала работать."
    cs_ls "А что на нём изображено?"
    cs_narrator "Виола посмотрела на рисунок."
    cs_vi "Странная анатомическая иллюстрация. Не самое удачное пособие, если спрашиваешь моё мнение."
    # cs_director_begin: REFLECTIVE_SHOT: Easter egg versus real object
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_b13f77739b:
    # cs_director_end
    cs_narrator "Я снова уставилась на изображение."
    cs_th "Вот ведь."
    cs_narrator "В обычной игре такой плакат можно было принять за шутку художников."
    cs_narrator "За пасхалку."
    cs_narrator "За случайную деталь фона."
    cs_narrator "Мельком посмотреть."
    cs_narrator "Улыбнуться."
    cs_narrator "И забыть."
    cs_narrator "Но сейчас я стояла в настоящем помещении."
    cs_narrator "Перед настоящей стеной."
    cs_narrator "И смотрела на изображение, которое, по моим воспоминаниям, напоминало историю из будущего относительно здешнего времени."
    # cs_director_begin: Return to direct interaction: Easter egg versus real object
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_0a71aca9ab:
    # cs_director_end
    cs_narrator "Я повернулась к Даше."
    cs_ls "Помнишь, мы говорили о том, что здесь не всё обязательно соответствует обычному прошлому?"
    cs_narrator "Она кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да."
    cs_ls "Кажется, появился ещё один повод так думать."
    cs_narrator "Виола посмотрела на меня."
    cs_vi "Почему?"
    cs_narrator "Я некоторое время молчала."
    cs_th "Ну вот."
    cs_th "Опять этот момент."
    cs_th "Сказать правду?"
    cs_th "Начать объяснять человеку историю, которая ещё не произошла?"
    cs_th "Или наконец научиться сначала оценивать собственные слова?"
    cs_narrator "Я посмотрела на Виолу."
    cs_ls "Есть одно изображение, которое я помню по истории девяностых годов. Этот рисунок его очень напоминает."
    cs_narrator "Виола нахмурилась."
    cs_vi "Каких девяностых?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Тысяча девятьсот девяностых."
    cs_narrator "Несколько секунд она молчала."
    cs_narrator "Затем осторожно произнесла:"
    cs_vi "До них ещё десять лет."
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "В её взгляде читалось знакомое предупреждение."
    cs_th "Лен, только не начинай снова."
    cs_narrator "Я едва заметно выдохнула."
    cs_ls "Но я могу ошибаться. Возможно, это просто похожий рисунок."
    cs_narrator "Виола приподняла бровь."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Вот это уже разумнее."
    cs_narrator "Я усмехнулась."
    cs_ls "Иногда получается."
    cs_narrator "Она посмотрела на плакат ещё раз."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "А почему ты вообще знаешь что-то о девяностых годах?"
    cs_narrator "Я немного помолчала."
    cs_ls "Потому что у нас с Дашей довольно необычная история приезда."
    cs_vi "Ольга Дмитриевна уже намекала, что с вами не всё просто."
    cs_narrator "Я кивнула."
    cs_ls "Тогда, думаю, не буду окончательно портить впечатление подробностями."
    cs_narrator "Виола тихо рассмеялась."
    show cs custom warm_smile medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Смотри сама."
    cs_narrator "Она скрестила руки."
    show cs custom serious medical normal at cs_viola_normal_left zorder 10
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_vi "Только я бы не стала строить большую теорию по одному старому плакату."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И впервые за разговор улыбнулась совершенно искренне."
    cs_ls "Согласна."
    cs_narrator "Дарья повернулась ко мне."
    cs_narrator "Кажется, она ожидала продолжения спора."
    cs_narrator "Но его не последовало."
    # cs_director_begin: REFLECTIVE_SHOT: Evidence and uncertainty about returning home
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_ffc2b3a354:
    # cs_director_end
    cs_narrator "Я ещё раз взглянула на изображение."
    cs_th "Плакат существует."
    cs_th "Похож на знакомый рисунок."
    cs_th "Но это пока всё, что мы действительно знаем."
    cs_narrator "Никаких доказательств временных петель."
    cs_narrator "Никакой уверенности, что перед нами изображён именно Алёшенька."
    cs_narrator "Только ещё одна странность."
    cs_narrator "И ещё один вопрос."
    cs_narrator "Я мысленно добавила его к списку наблюдений."
    cs_th "Домой вернусь — надо будет перечитать всё, что помню об этой истории."
    cs_narrator "Потом остановила себя."
    cs_th "Если вернусь."
    cs_narrator "Неприятная мысль."
    cs_narrator "Но вполне честная."
    # cs_director_begin: Return to direct interaction: Evidence and uncertainty about returning home
    $ cs_frame_focus(["cs", "cs_darya"])
    with cs_sprite_change
    label cs_director_check_fcda4f0e22:
    # cs_director_end
    cs_narrator "Я повернулась к Даше."
    cs_narrator "Она всё ещё стояла рядом."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты в порядке?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Просто задумалась."
    cs_narrator "Она чуть улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Кажется, это становится твоим главным занятием в лагере."
    cs_ls "После пробежек и посещения столовой."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part04_cast = ["cs", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "И я почувствовала, как напряжение немного отпускает."
    return
