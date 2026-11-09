# -*- coding: utf-8 -*-
label cs_day05_15:
    $ cs_d5_scene = 15
    $ save_name = "Чужая смена — День 5: Снаружи никого"
    $ cs_bus_scene_enter(15)
    cs_narrator "Никто не предложил броситься следом."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Удивительно разумное решение."
    cs_narrator "Особенно если вспомнить, что ещё вчера я сама наверняка побежала бы к двери первой."
    cs_narrator "Женя стояла возле стола."
    cs_narrator "Она смотрела на ручку."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Я никого не видела в окно."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Давайте проверим с другой стороны."
    cs_narrator "Даша осторожно подошла к окну."
    cs_narrator "Отодвинула занавеску."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "На дорожке никого нет."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А крыльцо видно?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 22e724b7cba4bcbad079
    cs_da "Нет."
    cs_da "Только ступеньки сбоку."
    cs_narrator "Я встала рядом с Женей."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Откроем вместе?"
    cs_narrator "Она посмотрела на меня."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Сначала послушаем."
    cs_narrator "Мы подождали."
    cs_narrator "За дверью было тихо."
    cs_narrator "Ни шагов, ни голосов."
    $ cs_bus_cue('calm')
    cs_narrator "С улицы снова доносилось пение птиц."
    cs_narrator "Обычный звук."
    cs_narrator "Но теперь я почему-то прислушивалась к нему так внимательно, словно от этого зависело всё происходящее."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: b7ac0a10b0bb3bf1cebb
    cs_da "Давайте."
    cs_da "Только осторожно."
    cs_narrator "Женя взялась за ручку."
    cs_narrator "Я встала рядом, оставляя ей достаточно места."
    $ cs_rev_sfx('sound/sfx/open_door_clubs.ogg',0.35)
    cs_narrator "Дверь медленно открылась."
    cs_narrator "Солнечное крыльцо."
    cs_narrator "Перила."
    cs_narrator "Край дорожки."
    cs_narrator "Никого."
    cs_narrator "Я выдохнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ну хотя бы дверь осталась дверью."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А что ты ожидала?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 13ba15889d6019faeddc
    cs_ls "После автобуса?"
    cs_ls "Уже не уверена."
    $ cs_d5_room("bg ext_library_day")
    cs_narrator "Мы вышли на крыльцо."
    cs_narrator "Женя остановилась возле косяка."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Подождите."
    cs_narrator "Я посмотрела туда же."
    cs_narrator "На дереве виднелись короткие белые линии."
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("│  │  │  │  │  │  ╳", "Отметки на дверном косяке")
    cs_narrator "Семь отметок."
    cs_narrator "Последняя была перечёркнута."
    hide screen cs_d5_insert
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Это было раньше?"
    cs_narrator "Женя покачала головой."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 72daec91480bff10b3e7
    cs_mz "Нет."
    cs_mz "Я здесь каждый день щётку ставлю."
    cs_mz "Заметила бы."
    cs_narrator "Семён подошёл ближе."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Семь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Уже начинаю ненавидеть это число."
    cs_narrator "Тихонова стояла у двери."
    cs_narrator "Она смотрела на отметки так внимательно, что я невольно повернулась к ней."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Лен?"
    cs_narrator "Тихонова вздрогнула."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Мне такие снились."
    cs_narrator "Все посмотрели на неё."
    cs_narrator "Она немного смутилась, но продолжила."
    $ cs_d5_focus("un")
    with cs_sprite_change
    # cs_page_anchor: da9b73a7dd79c53c191a
    cs_un "На стене возле двери."
    cs_un "Сначала семь линий."
    cs_un "Потом кто-то перечеркнул последнюю."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Ты помнишь, кто?"
    cs_narrator "Тихонова покачала головой."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Нет."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Не нужно заставлять себя вспоминать прямо сейчас."
    $ cs_d5_focus("un")
    with cs_sprite_change
    cs_un "Хорошо."
    cs_narrator "Женя достала тетрадь и аккуратно зарисовала отметки."
    cs_narrator "Я посмотрела на дорожку."
    cs_narrator "Мимо прошла девочка из младшего отряда."
    cs_narrator "Она остановилась возле крыльца."
    $ cs_d5_focus("d5_pioneer_girl")
    with cs_sprite_change
    cs_d5_pioneer_girl "А вы Ольгу Дмитриевну не видели?"
    cs_narrator "Я повернулась к ней."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 626e9910bbaa8e42903f
    cs_ls "Она скоро вернётся."
    cs_ls "Мы тоже её ждём."
    $ cs_d5_focus("d5_pioneer_girl")
    with cs_sprite_change
    cs_d5_pioneer_girl "Спасибо!"
    cs_narrator "Девочка убежала дальше."
    cs_narrator "Я проводила её взглядом."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Вот ведь."
    cs_narrator "Для кого-то сегодняшний день был совершенно обычным."
    cs_narrator "Пионеры бегали по лагерю, искали вожатую, спорили из-за мяча."
    cs_narrator "А мы стояли возле библиотеки и рассматривали странные отметки на двери."
    cs_narrator "Иногда хотелось оказаться на их месте."
    cs_narrator "Хотя бы ненадолго."
    if cs_friend_un >= 4:
        cs_narrator "Тихонова осторожно подошла ко мне."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Можно с тобой поговорить?"
        cs_narrator "Я кивнула."
        cs_narrator "Мы отошли к перилам."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Что такое?"
        cs_narrator "Она посмотрела на свои пальцы."
        $ cs_d5_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 93b0e2d4325aaffb4410
        cs_un "Во сне я видела руку."
        cs_un "Возле стены."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Чью?"
        $ cs_d5_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 37f2fe981d3ab17a578b
        cs_un "Не знаю."
        cs_un "Но на пальце была краска."
        cs_narrator "Она немного помолчала."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Такая же, какая бывает у меня после рисования."
        cs_narrator "Я посмотрела на неё."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Ты думаешь, это была твоя рука?"
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Не знаю."
        cs_narrator "Она опустила глаза."
        $ cs_d5_focus("un")
        with cs_sprite_change
        # cs_page_anchor: 03a5c76058191394ff28
        cs_un "Я поэтому не хотела говорить при всех."
        cs_un "Вдруг решат, что это я оставляю надписи."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Лен, у нас сейчас нет оснований так считать."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Правда?"
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: ef36768b3e81da16e123
        cs_ls "Правда."
        cs_ls "А на должность главного злодея ещё и собеседование не объявляли."
        cs_narrator "Она неожиданно рассмеялась."
        $ cs_d5_focus("un")
        with cs_sprite_change
        cs_un "Ты всё шутишь."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Не всегда."
        cs_narrator "Я чуть помолчала."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Спасибо, что доверилась."
        cs_narrator "Тихонова кивнула."
        $ cs_d5_lena_private_memory = True
    else:
        cs_narrator "Тихонова осталась возле Жени."
        cs_narrator "Она не сводила глаз с отметок."
        cs_narrator "Я не стала задавать дополнительных вопросов."
        cs_narrator "Если захочет, расскажет сама."
        cs_narrator "После сегодняшнего утра я уже достаточно хорошо понимала, как неприятно бывает, когда тебя заставляют объяснять то, чего ты сам не понимаешь."
        $ cs_d5_lena_private_memory = False
    cs_narrator "Женя закончила рисунок."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 8905906d1e6e42055d48
    cs_mz "Готово."
    cs_mz "Теперь хотя бы останется копия."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Стирать будем?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9def61b9ebd26b34e55e
    cs_ls "Пока нет."
    cs_ls "Пусть Ольга Дмитриевна посмотрит."
    cs_narrator "Даша проверила ручку двери."
    cs_narrator "Та закрывалась совершенно нормально."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Хоть здесь всё работает."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Не сглазь."
    $ cs_d5_room("bg int_library_day")
    $ cs_rev_sfx('sound/sfx/close_door_1.ogg',0.3)
    cs_narrator "Мы вернулись к столу."
    cs_narrator "Я записала последнее слово, произнесённое за дверью."
    cs_narrator "«Сегодня»."
    cs_narrator "Оно выглядело неприятно даже на бумаге."
    cs_narrator "Через несколько минут у крыльца послышались шаги."
    cs_narrator "На этот раз вполне обычные."
    cs_narrator "Ольга Дмитриевна вернулась вместе с Виолой."
    cs_narrator "Увидев нашу компанию, они сразу остановились."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Что произошло?"
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Потом на дверь."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У нас появилось ещё кое-что."
    cs_narrator "Вожатая нахмурилась."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Что именно?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Боюсь, вам не понравится."
    return
