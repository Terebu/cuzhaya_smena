# -*- coding: utf-8 -*-
label cs_day02_48:
    $ save_name = "Чужая смена — День 2: Встреча с землёй"
    $ cs_part06_live = False
    $ cs_part07_live = True
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
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_s48:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я не заметила корень."
    cs_narrator "Он почти полностью скрывался под травой и выступал на дорожку всего на несколько сантиметров."
    cs_narrator "Достаточно, чтобы носок туфли зацепился за него."
    cs_narrator "Недостаточно, чтобы я успела что-нибудь исправить."
    stop music fadeout 0.5
    play sound "sound/sfx/bodyfall_1.ogg"
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
    # cs_global_transition
    with cs_sprite_change
    $ cs_lena_elbow_injury_day2 = 2
    $ cs_lena_bandage_damaged = True
    label cs_check_part07_fall:
    cs_narrator "В следующую секунду земля внезапно оказалась значительно ближе, чем предполагалось."
    cs_th "Ой."
    cs_narrator "Я попыталась выставить руку."
    cs_narrator "Плечо дёрнулось."
    cs_narrator "Ладонь коснулась дорожки."
    cs_narrator "Колено ударилось следом."
    cs_narrator "И уже повреждённый утром локоть скользнул по шероховатой поверхности."
    cs_narrator "Боль пришла не сразу."
    cs_narrator "Сначала было только неприятное ощущение удара."
    cs_narrator "И полное недоумение."
    cs_th "Так."
    cs_th "А это сейчас что было?"
    cs_narrator "Я лежала почти на боку, чувствуя под ладонью мелкие камешки."
    cs_narrator "Несколько секунд просто смотрела на них."
    cs_narrator "Потом медленно села."
    cs_ls "Ай…"
    cs_th "Вот теперь дошло."
    cs_narrator "Локоть жгло так, словно кто-то решил приложить к нему раскалённый утюг."
    cs_narrator "Я повернула руку."
    cs_narrator "Посмотрела."
    cs_narrator "И замерла."
    cs_narrator "Повязка, которую Виола наложила утром, сбилась и испачкалась."
    cs_narrator "Рядом с прежней царапиной появилась широкая ссадина."
    cs_narrator "По коже стекала кровь."
    cs_narrator "Не особенно быстро, но достаточно заметно, чтобы настроение окончательно испортилось."
    cs_ls "Ну прекрасно."
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена!"
    cs_narrator "Она уже возвращалась ко мне."
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
    show cs_darya serious pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_injury_focus:
    cs_narrator "Присела рядом."
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты как? Сильно ударилась?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на собственный локоть."
    cs_ls "Кажется, земная поверхность одержала убедительную победу."
    cs_da "Лен, серьёзно."
    cs_narrator "Я выдохнула."
    cs_ls "Локоть содрала. И колено немного болит."
    cs_narrator "Даша осторожно посмотрела на руку."
    cs_narrator "Её лицо изменилось."
    cs_narrator "Улыбка исчезла."
    cs_da "Кровь идёт."
    cs_ls "Да, заметила."
    cs_narrator "Я потянулась другой рукой к ссадине."
    cs_narrator "Дарья мягко остановила меня."
    cs_da "Подожди. Не трогай грязными пальцами."
    cs_narrator "Я посмотрела на собственную ладонь."
    cs_narrator "На ней была пыль."
    cs_th "Справедливо."
    cs_ls "Ладно."
    cs_da "Головой не ударилась?"
    cs_ls "Нет. Успела выставить руки."
    cs_da "Не кружится?"
    cs_ls "Нет."
    cs_narrator "Она внимательно посмотрела на меня."
    cs_da "Тошноты нет?"
    cs_ls "Даш, со мной всё нормально. Просто локоть болит."
    cs_narrator "Я немного помолчала."
    cs_ls "Сильно."
    cs_narrator "Она кивнула."
    cs_da "Тогда давай сначала разберёмся с кровью, а потом пойдём к Виоле."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "На этот раз без шуток."
    cs_ls "Хорошо."
    cs_narrator "Даша достала чистый платок."
    cs_narrator "Помогла мне аккуратно прижать его к повреждённому участку, не пытаясь самостоятельно отдирать грязную повязку."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Я старалась ровно дышать."
    cs_narrator "И не смотреть на руку каждые три секунды."
    cs_narrator "Получалось не особенно хорошо."
    cs_da "Только не дёргай её."
    cs_ls "Постараюсь."
    cs_narrator "Она подняла взгляд."
    cs_da "Можешь пошевелить пальцами?"
    cs_narrator "Я осторожно сжала и разжала ладонь."
    cs_ls "Могу."
    cs_da "Хорошо."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Ты сейчас очень серьёзная."
    cs_narrator "Она не улыбнулась."
    cs_da "Потому что ты упала и у тебя кровь на руке."
    cs_narrator "Я немного помолчала."
    cs_th "Вот ведь."
    cs_th "Ещё минуту назад мы смеялись над невозможной дорогой."
    cs_th "А теперь Даша сидит передо мной и пытается понять, насколько сильно я пострадала."
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
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part07_standing:
    cs_narrator "Я осторожно поднялась с её помощью."
    cs_narrator "Перенесла вес на ноги."
    cs_narrator "Колено неприятно отозвалось, но стоять я могла."
    cs_da "Идти сможешь?"
    cs_ls "Да."
    cs_da "Тогда без спешки."
    cs_narrator "Я кивнула."
    cs_ls "Без спешки."
    cs_narrator "Она придержала меня за здоровую руку."
    cs_narrator "Мы медленно направились к медпункту."
    cs_th "И всё-таки есть в этой ситуации какая-то ирония."
    cs_th "Утром мне уже объясняли, что с ранами нужно обращаться осторожнее."
    cs_th "Не прошло и суток."
    cs_th "Даже половины дня."
    cs_th "Соколова, ты выдающийся специалист по повторным обращениям."
    return
