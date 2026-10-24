# -*- coding: utf-8 -*-
label cs_day03_78b:
    $ save_name = "Чужая смена — День 3: Вчерашнее объявление"
    cs_narrator "Славя немного поправила содержимое коробки."
    cs_narrator "Я заметила несколько листов картона."
    cs_narrator "Среди них мелькнул знакомый рисунок."
    cs_ls "Подожди, а это не наше вчерашнее объявление?"
    cs_narrator "Славя посмотрела внутрь."
    cs_sl "Да. После концерта всё снимали с доски."
    cs_narrator "Я кивнула."
    cs_ls "Понятно."
    cs_narrator "Немного помолчала."
    cs_ls "Жалко, конечно. Я уже почти привыкла видеть результаты своего художественного гения в общественных местах."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_sl "Оно ведь выполнило свою задачу. Все узнали о концерте."
    cs_narrator "Я улыбнулась."
    cs_ls "Тоже верно."
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Славя закрыла коробку."
    cs_sl "Ладно, мне ещё нужно всё отнести."
    cs_narrator "Я кивнула."
    cs_ls "Не буду задерживать."
    return
