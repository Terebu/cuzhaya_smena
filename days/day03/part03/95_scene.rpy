# -*- coding: utf-8 -*-
label cs_day03_95:
    $ save_name = "Чужая смена — День 3: Полная версия Соколовой"
    cs_narrator "Мы отнесли подносы."
    cs_narrator "Женя поправила книгу под мышкой."
    cs_mz "Ладно, мне пора."
    cs_narrator "Я кивнула."
    cs_ls "Хорошего дня."
    cs_narrator "Она посмотрела на меня."
    cs_narrator "И слегка улыбнулась."
    cs_mz "И тебе."
    cs_narrator "Дарья тоже попрощалась."
    $ cs_director_scene("bg ext_dining_hall_away_day")
    scene bg ext_dining_hall_away_day
    show cs_darya shy_smile pioneer normal at Transform(xpos=0.75, xanchor=0.5, ypos=1.60, yanchor=1.0)
    show cs_zhenya normal pioneer normal at Transform(xpos=0.25, xanchor=0.5, ypos=1.60, yanchor=1.0)
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы вышли из столовой."
    cs_narrator "Некоторое время шли вместе."
    cs_narrator "Потом возле развилки Женя остановилась."
    cs_mz "Мне сюда."
    cs_narrator "Я кивнула."
    cs_ls "До встречи."
    cs_mz "До встречи."
    $ cs_actor_exit(["cs_zhenya"])
    with cs_sprite_leave
    label cs_check_day03_95_zhenya_left:
    cs_narrator "Она направилась к библиотеке."
    return
