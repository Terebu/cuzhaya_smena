# -*- coding: utf-8 -*-
label cs_day01_45:
    $ save_name = "Чужая смена — День 1: Пока"
    stop music fadeout 2.0
    $ renpy.music.set_volume(0.35,delay=1.5,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_evening.ogg":
        play ambience "sound/ambiences/camp_center_evening.ogg" fadeout 2.0 fadein 2.0
    cs_narrator "Некоторое время мы просто сидели втроём."
    cs_narrator "Семён смотрел на площадь."
    cs_narrator "Дарья — на деревья, за которыми медленно опускалось солнце."
    cs_narrator "А я пыталась понять, как умудрилась за один день пережить столько всего."
    cs_narrator "Утром — зимняя Москва."
    cs_narrator "Днём — автобус, неизвестный лагерь, знакомые лица и советская пионерская форма."
    cs_narrator "После обеда — знакомство с Семёном, собственный домик и попытка вернуть к жизни смартфон."
    cs_narrator "И вот теперь ещё этот разговор."
    cs_th "Молодец, Соколова."
    cs_th "Планировала купить продукты."
    cs_th "Вместо этого решила разобраться с собственной личной жизнью."
    cs_narrator "Семён поднялся."
    show cs_semen relaxed pioneer normal at cs_semen_normal_left
    cs_sy "Ладно, я пойду. Ольга Дмитриевна ещё просила кое-что сделать."
    cs_ls "Трудовая дисциплина прежде всего."
    cs_narrator "Он покачал головой."
    show cs_semen thinking_alt pioneer normal at cs_semen_normal_left
    cs_sy "Ты когда-нибудь перестанешь так разговаривать?"
    cs_ls "Никаких гарантий."
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    cs_narrator "Дарья улыбнулась."
    cs_narrator "Семён махнул рукой."
    show cs_semen smile pioneer normal at cs_semen_normal_left
    cs_sy "Увидимся."
    cs_ls "Увидимся."
    hide cs_semen with Dissolve(0.6)
    # cs_composition: regroup
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    label cs_check_day01_part08_semen_leaves:
    cs_narrator "Он пошёл в сторону домиков."
    cs_narrator "Мы с Дарьей тоже поднялись со скамейки."
    $ renpy.music.set_volume(0.28,delay=1.0,channel="music")
    play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 3.0
    cs_narrator "Я посмотрела на неё."
    cs_ls "Не слишком тебя смутила?"
    # cs_darya_variety: reaction
    show cs_darya shy_bend pioneer normal at cs_darya_normal_center
    cs_da "Немного."
    cs_ls "Извини."
    cs_narrator "Она покачала головой."
    cs_da "Всё нормально. Просто я не ожидала от тебя такого разговора. Тем более сегодня."
    cs_ls "Я сама не ожидала."
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    cs_narrator "Дарья тихо усмехнулась."
    cs_narrator "Мы направились к дорожке."
    cs_narrator "Через несколько шагов я осторожно коснулась её плеча."
    cs_narrator "Она повернулась ко мне."
    cs_ls "Можно?"
    cs_narrator "Дарья взглянула на мою руку."
    cs_narrator "Затем на меня."
    # cs_darya_variety: reaction
    show cs_darya reaching pioneer normal at cs_darya_normal_center
    cs_da "Сейчас можно."
    label cs_check_day01_part08_hug:
    cs_narrator "Я мягко приобняла её за плечи."
    cs_narrator "Совсем ненадолго."
    cs_narrator "Она не отстранилась."
    cs_narrator "Мы прошли так несколько шагов."
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    cs_narrator "Потом Дарья посмотрела на меня с лёгкой улыбкой."
    cs_da "Только не делай из этого событие государственного масштаба."
    cs_narrator "Я немедленно приняла серьёзный вид."
    cs_ls "Постановление ЦК о совместной прогулке уже подготовлено."
    # cs_darya_variety: reaction
    show cs_darya amused pioneer normal at cs_darya_normal_center
    cs_narrator "Она рассмеялась."
    cs_da "Лена!"
    cs_ls "Хорошо. Отзываю постановление."
    cs_narrator "Я убрала руку."
    cs_narrator "Мы снова шли рядом."
    cs_narrator "Через некоторое время Дарья негромко произнесла:"
    # cs_darya_variety: reaction
    show cs_darya arms_crossed pioneer normal at cs_darya_normal_center
    cs_da "И не думай, что я уже на всё согласилась."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даже не собиралась."
    cs_da "Правда?"
    cs_ls "Даш, мне достаточно того, что мы можем об этом спокойно разговаривать."
    cs_narrator "Она кивнула."
    # cs_darya_variety: reaction
    show cs_darya reaching pioneer normal at cs_darya_normal_center
    cs_da "Тогда хорошо."
    cs_narrator "Я тоже кивнула."
    cs_narrator "И на этот раз не стала ничего добавлять."
    cs_narrator "Впереди тянулась дорожка между деревьями."
    cs_narrator "Издалека доносились голоса пионеров."
    cs_narrator "Лагерь постепенно готовился к вечеру."
    cs_narrator "Солнце золотило крыши домиков."
    cs_narrator "А я шла рядом с девушкой, которую ещё утром совершенно не знала."
    cs_narrator "И которая за несколько часов успела стать для меня неожиданно важной."
    cs_narrator "Я не знала, что она ответит завтра."
    cs_narrator "Не знала, что произойдёт с нами через неделю."
    cs_narrator "И даже не была уверена, существует ли в этом лагере само понятие «через неделю» в привычном смысле."
    cs_narrator "Но сейчас всё это могло немного подождать."
    cs_narrator "Дарья вдруг посмотрела на меня."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_center
    cs_da "Лен?"
    cs_ls "М?"
    cs_da "Спасибо, что сказала."
    cs_narrator "Я повернулась к ней."
    cs_ls "Не за что."
    # cs_darya_variety: reaction
    show cs_darya shy_smile pioneer normal at cs_darya_normal_center
    cs_narrator "Она улыбнулась."
    cs_narrator "И мы продолжили идти."
    # cs_focus: camera
    hide cs_darya with Dissolve(0.25)
    cs_th "Кажется, впервые за весь день мне не хотелось ничего проверять, объяснять или выяснять."
    cs_th "Просто идти рядом."
    cs_th "Неплохое завершение дня."
    cs_th "Хотя до отбоя ещё далеко."
    scene cs_camp_path_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_center
    with Dissolve(1.5)
    label cs_check_day01_part08_walk:
    return
