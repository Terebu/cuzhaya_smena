# -*- coding: utf-8 -*-
label cs_day03_159a:
    $ save_name = "Чужая смена — День 3: Временный заместитель библиотекаря"
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на Женю."
    cs_ls "Слушай, а тебе помощь нужна?"
    cs_narrator "Она подняла бровь."
    cs_mz "Какая?"
    cs_narrator "Я немного улыбнулась."
    cs_ls "Какая-нибудь, не требующая переноски шкафов. У меня пока медицинские ограничения."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "Представляешь, у нас не каждый день двигают шкафы."
    cs_narrator "Я кивнула."
    cs_ls "Прекрасная новость. Тогда мои шансы устроиться на работу значительно возрастают."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Женя посмотрела на меня."
    cs_mz "Ты серьёзно предлагаешь помочь?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Если тебе удобно."
    cs_narrator "Она немного задумалась."
    cs_mz "Нужно проверить несколько книг по списку и разложить карточки. Справишься?"
    cs_narrator "Я улыбнулась."
    cs_ls "Женя, я художница. Умею часами заниматься работой, которая со стороны выглядит как бессмысленное перекладывание предметов."
    cs_narrator "Она усмехнулась."
    cs_mz "Значит, подходящий опыт есть."
    cs_ls "Колоссальный."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "А мне можно помочь?"
    cs_narrator "Женя посмотрела на неё."
    cs_mz "Если хотите. Только аккуратно, чтобы ничего не перепутать."
    cs_narrator "Дарья кивнула."
    cs_da "Конечно."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я посмотрела на Женю."
    cs_ls "Тогда после ужина зайдём?"
    cs_narrator "Она немного подумала."
    cs_mz "Да. Только ненадолго. Мне самой ещё нужно закончить журнал."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    if cs_mz_dinner_friend_on_arrival >= 3:
        cs_narrator "Женя чуть улыбнулась."
        cs_mz "Только предупреждаю: если начнёшь называть себя заместителем заведующей, я передумаю."
        cs_narrator "Я замерла."
        cs_narrator "Посмотрела на неё."
        cs_narrator "Потом медленно улыбнулась."
        cs_ls "Женя, как ты могла подумать, что я собиралась произнести именно это?"
        cs_narrator "Она подняла бровь."
        cs_mz "Потому что ты уже открыла рот."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
        cs_narrator "Я покачала головой."
        cs_ls "Удивительно. Меня начинают понимать раньше, чем я сама успеваю сформулировать мысль."
        if renpy.showing("cs_zhenya"):
            show cs_zhenya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя усмехнулась."
        cs_mz "Это несложно."
    else:
        if renpy.showing("cs_zhenya"):
            show cs_zhenya glasses_touch pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Женя поправила очки."
        cs_mz "И, пожалуйста, не перекладывай карточки без спроса."
        cs_narrator "Я кивнула."
        cs_ls "Конечно. Сначала объяснишь, что куда."
        cs_mz "Вот и хорошо."
    cs_narrator "Я улыбнулась."
    cs_th "Ну вот."
    cs_th "Ещё одно добровольное общественно полезное мероприятие."
    cs_th "Кажется, на третий день я окончательно превращаюсь в человека, которого можно эксплуатировать на благо лагеря."
    cs_th "Ольга Дмитриевна была бы довольна."
    return
