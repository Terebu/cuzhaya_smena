# -*- coding: utf-8 -*-
label cs_day04_02:
    $ save_name = "Чужая смена — День 4: Фотографии из прошлого"
    $ cs_director_scene("cs_d4_old_photo_room")
    scene cs_d4_old_photo_room
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Я сделала несколько шагов в сторону коридора, но остановилась."
    cs_narrator "Нет."
    cs_narrator "Сначала фотография."
    cs_narrator "Раз уж я сюда пришла, нужно хотя бы попытаться понять, что именно нашла."
    cs_narrator "Я вернулась к щиту."
    cs_narrator "Под снимком висела металлическая табличка. Ржавчина почти съела надпись."
    cs_narrator "Я осторожно протёрла её краем футболки."
    cs_narrator "Без особого успеха."
    cs_narrator "Удалось разобрать только несколько обломков цифр."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Потрясающе. Историческое свидетельство есть, а паспорт исторического свидетельства утерян."
    cs_narrator "Я снова посмотрела на фотографии."
    cs_narrator "Славя. Женя. Девушка, похожая на Лену Тихонову."
    cs_narrator "Похожие."
    cs_narrator "Именно так."
    cs_narrator "Не одинаковые."
    cs_narrator "Чёрно-белый снимок вообще не позволял определить цвет волос. Да и лица были слишком маленькими."
    cs_narrator "Как художница, я знала этот фокус: пара линий — и мозг сам достроит знакомое лицо. Здесь доверять ему не хотелось."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Либо я дура…"
    cs_narrator "Я перевела взгляд на табличку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "…либо лагерь опять развлекается со временем."
    cs_narrator "Оба варианта меня совершенно не устраивали."
    cs_narrator "Я сняла снимок с крепления. На подоконнике нашлась картонная папка с плотными листами."
    cs_narrator "Фотографию удалось поместить между ними, не сгибая."
    $ cs_d4_undated_photo_location = "lena"
    cs_narrator "Верну, когда разберёмся."
    cs_narrator "Хотя сначала желательно отсюда выбраться."
    cs_narrator "В коридоре снова что-то скрипнуло."
    cs_narrator "Я замерла, прислушиваясь."
    cs_narrator "Шагов больше не было."
    cs_narrator "Только ветер."
    cs_narrator "Я оглядела комнату в поисках чего-нибудь полезного."
    cs_narrator "Фонарика, разумеется, не нашлось."
    cs_narrator "Телефон остался у Шурика и Электроника. Впрочем, с пустым аккумулятором из него всё равно плохой фонарик."
    cs_narrator "На полу возле перевёрнутого стула лежала отломанная деревянная ножка."
    cs_narrator "Я подняла её здоровой рукой."
    cs_narrator "Покрутила, проверила вес."
    cs_narrator "Примерно полметра дерева."
    cs_narrator "Ни фонарь, ни средство связи, ни особенно убедительное оружие."
    cs_narrator "Но уже что-то."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Всегда знала, что мебель — величайшее достижение цивилизации."
    $ cs_director_scene("cs_d4_old_corridor")
    scene cs_d4_old_corridor
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Я осторожно вышла в коридор."
    cs_narrator "Свет за окнами постепенно усиливался, но дальняя часть здания по-прежнему оставалась тёмной."
    cs_narrator "Под ногами хрустело стекло."
    cs_narrator "Стараясь не задеть повреждённым локтем стены, я приблизилась к повороту и остановилась."
    cs_narrator "Так, Соколова. Включаем мозг."
    cs_narrator "Если там человек, сначала разговариваем."
    cs_narrator "Если человек собирается напасть, вспоминаем школьную физкультуру и быстро бежим."
    cs_narrator "А если там мистика…"
    cs_narrator "Я посмотрела на ножку стула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Попробую отлупить мистику мебелью."
    cs_narrator "Звучало настолько глупо, что я невольно усмехнулась."
    cs_narrator "Ненадолго стало легче."
    cs_narrator "Я осторожно выглянула из-за угла."
    cs_narrator "Никого."
    cs_narrator "Коридор тянулся ещё несколько метров, после чего обрывался лестницей, уходящей вниз."
    cs_narrator "Я уставилась на ступени."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Конечно."
    cs_narrator "Ну разумеется."
    cs_narrator "Загадочные незнакомцы почему-то не выбирают светлые комнаты с телефоном."
    cs_narrator "Обязательно подвал."
    cs_narrator "Или тоннель."
    cs_narrator "Или что-нибудь ещё, куда даже страховой агент побоялся бы заглянуть."
    $ cs_director_scene("cs_d4_old_stairs")
    scene cs_d4_old_stairs
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Я подошла ближе."
    cs_narrator "Бетонная лестница уходила вниз. На ступенях крошилась штукатурка, перила покрывала ржавчина."
    cs_narrator "На стене сохранилась старая табличка."
    cs_narrator "Большинство букв осыпалось."
    cs_narrator "Но несколько ещё можно было прочесть."
    cs_narrator "«…БЕЖИ…»"
    cs_narrator "Я медленно провела пальцем по краю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Убежище."
    cs_narrator "Слово прозвучало слишком громко."
    cs_narrator "Я замолчала."
    cs_narrator "Убежище."
    cs_narrator "Значит, география действительно напоминает ту, которую я помнила по игре."
    cs_narrator "Вот только знание примерного расположения помещений пока не делало эту прогулку безопаснее."
    cs_narrator "Снизу донёсся металлический скрежет."
    cs_narrator "Я вздрогнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Эй! Здесь кто-нибудь есть?"
    cs_narrator "Мой голос отразился от бетонных стен и постепенно затих."
    cs_narrator "Ответа не последовало."
    cs_narrator "Затем снизу раздался короткий стук."
    cs_narrator "Будто кто-то коснулся металлической двери."
    cs_narrator "Я крепче сжала деревяшку."
    cs_narrator "Нет. Всё. Домой."
    cs_narrator "Нужно вернуться, рассказать Даше и Семёну, показать фотографии."
    cs_narrator "Можно будет прийти сюда вместе. С фонарями. Желательно днём."
    cs_narrator "Я уже сделала шаг назад, когда внизу на секунду мелькнул свет."
    cs_narrator "Холодный."
    cs_narrator "Белый."
    cs_narrator "Совсем не похожий на утреннее солнце."
    cs_narrator "Я застыла."
    cs_narrator "Электричество?"
    cs_narrator "В заброшенном корпусе?"
    cs_narrator "Может, кто-то действительно пользуется убежищем?"
    cs_narrator "Я осторожно ступила на первую ступеньку."
    cs_narrator "Потом на вторую."
    cs_narrator "Гул шагов неприятно расходился по лестничному пролёту."
    cs_narrator "Ты ведь понимаешь, что это плохая идея?"
    cs_narrator "Прекрасно понимаю."
    cs_narrator "Тогда зачем продолжаешь?"
    cs_narrator "Потому что хочу знать."
    cs_narrator "Я остановилась."
    cs_narrator "Впервые за всё утро этот ответ перестал казаться достаточно убедительным."
    cs_narrator "Но назад я так и не повернула."
    return
