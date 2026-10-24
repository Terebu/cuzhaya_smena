# -*- coding: utf-8 -*-
label cs_day03_85:
    $ save_name = "Чужая смена — День 3: Славя и первый советский сувенир"
    show cs_darya hair_touch pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья поправила волосы."
    cs_narrator "Я тем временем решила проверить, всё ли взяла."
    cs_narrator "Галстук."
    cs_narrator "Форма."
    cs_narrator "Повязка."
    cs_th "Вроде ничего не забыла."
    cs_narrator "Потом вспомнила утреннюю встречу."
    cs_ls "Кстати, я сегодня Славю встретила."
    cs_narrator "Дарья подняла взгляд."
    cs_da "Уже успела?"
    cs_narrator "Я кивнула."
    cs_ls "Разумеется. Пока остальные спали, она занималась хозяйственными делами."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Это на неё похоже."
    cs_ls "У меня возникает подозрение, что Славя просыпается раньше самого утра. Просто чтобы всё подготовить к его приходу."
    show cs_darya amused pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "И что вы обсуждали?"
    cs_narrator "Я немного подумала."
    cs_ls "Преимущественно трудовую этику, медицинские ограничения и некоторые недостатки советской тяжёлой промышленности."
    show cs_darya thinking pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья замолчала."
    cs_narrator "Потом медленно повернулась ко мне."
    cs_da "Лена."
    cs_narrator "Я совершенно серьёзно посмотрела на неё."
    cs_ls "Да?"
    cs_da "Ты снова говорила про танки?"
    cs_narrator "Я вздохнула."
    cs_ls "Всего один раз."
    cs_narrator "Она закрыла глаза."
    cs_narrator "И рассмеялась."
    cs_da "Бедная Славя."
    cs_narrator "Я указала на неё здоровой рукой."
    cs_ls "Никакая она не бедная. Сегодня уже сама начала издеваться над моей трудовой биографией."
    cs_da "И правильно сделала."
    cs_narrator "Я посмотрела на неё."
    cs_th "Вот ведь."
    cs_th "Два дня — и у меня уже сформировалась организованная оппозиция."
    cs_ls "Поразительно, с какой скоростью в этом лагере распространяется сарказм."
    show cs_darya shy_smile pioneer normal
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Ты же постоянно подаёшь пример."
    cs_ls "Придётся пересмотреть образовательную программу."
    if cs_sl_poster_saved_day3:
        call cs_day03_85a from cs_return_c94096320e6d7ce21731
    else:
        call cs_day03_85b from cs_return_26bba17531b32707abfa
    label cs_check_day03_85_poster_result:
    call cs_day03_85c from cs_return_06612e3ee7151b34401a
    return
