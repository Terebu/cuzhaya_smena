# -*- coding: utf-8 -*-
label cs_day05_05:
    $ cs_d5_scene = 5
    $ save_name = "Чужая смена — День 5: Остановка"
    $ cs_bus_scene_enter(5)
    $ cs_d5_room("bg ext_square_day")
    with Dissolve(0.7)
    stop music fadeout 1.0
    cs_narrator "К воротам мы пошли через площадь."
    cs_narrator "Возле клумбы Ульяна спорила с каким-то мальчишкой из младшего отряда."
    cs_narrator "В руках у неё была лейка, которой она размахивала с таким видом, словно собиралась использовать её совсем не по назначению."
    $ cs_d5_focus("d5_ulyana")
    with cs_sprite_change
    cs_d5_ulyana "А почему опять я должна поливать?!"
    $ cs_d5_focus("d5_pioneer")
    with cs_sprite_change
    cs_d5_pioneer "Потому что ты вчера обещала!"
    $ cs_d5_focus("d5_ulyana")
    with cs_sprite_change
    cs_d5_ulyana "Я вчера много чего обещала!"
    cs_narrator "Я чуть не остановилась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Слушайте, а у них, кажется, интереснее."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Ты хотела проверить остановку."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Да, но здесь хотя бы конфликт понятный."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "У тебя ещё будет возможность посмотреть, чем закончится история с лейкой."
    $ cs_d5_room("cs_camp_path_day")
    cs_narrator "Мы пошли дальше."
    cs_narrator "Чем ближе становились ворота, тем меньше хотелось разговаривать."
    cs_narrator "На первый взгляд, ничего не изменилось."
    cs_narrator "Те же деревья, та же ограда, знакомая дорожка."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Я вспомнила свой первый день."
    # cs_page_anchor: ccbc4c6ee809bf9913ed
    cs_narrator "Тогда всё вокруг казалось чужим."
    cs_narrator "Даже обычная автобусная остановка выглядела неправильно, хотя я не могла объяснить почему."
    $ cs_d5_room("bg ext_no_bus")
    cs_narrator "Теперь я знала расположение почти всех главных зданий лагеря."
    cs_narrator "Могла найти столовую, библиотеку, музыкальный клуб."
    cs_narrator "Даже начала запоминать, кто где обычно бывает."
    cs_narrator "И только эта дорога оставалась для меня неприятным исключением."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Ты притихла."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Думаю, не открыть ли здесь туристическое агентство."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Серьёзно?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 4ddaa4d7035e3dfb8991
    cs_ls "Конечно."
    cs_ls "Экскурсия «Как приехать в Совёнок и не понять, где ты находишься»."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Очень востребованное направление."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У нас уже трое клиентов."
    cs_narrator "Женя посмотрела на нас."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Может, сначала посмотрим, ради чего пришли?"
    cs_narrator "Я кивнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Разумно."
    cs_narrator "Мы остановились возле ворот."
    cs_narrator "Автобуса не было."
    cs_narrator "Дорога уходила за поворот, где деревья почти полностью закрывали обзор."
    cs_narrator "Я подошла к остановке."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: ab9f0c42f91c5ddd9269
    cs_ls "Так."
    cs_ls "Что проверяем?"
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Следы, табличку и всё, что выглядит новым."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А если ничего не найдём?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 103f361d599573b6b3fc
    cs_ls "Вернёмся."
    cs_ls "Мне такой результат тоже нравится."
    cs_narrator "Даша уже рассматривала землю возле обочины."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Смотрите сюда."
    cs_narrator "Мы подошли."
    cs_narrator "На рыхлом участке грунта виднелись две широкие полосы."
    cs_narrator "Следы шин."
    cs_narrator "Я присела и посмотрела на них."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Автобус?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Возможно."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Они доходят почти до остановки."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 2d7f7d40da12b2c26bb2
    cs_mz "А дальше асфальт."
    cs_mz "Поэтому мы не знаем, куда он поехал."
    cs_narrator "Я осторожно провела пальцем рядом с отпечатком."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: d9ee361928cc99bab55b
    cs_ls "Пыль могла бы оставить нам объяснительную."
    cs_ls "Но, к сожалению, отказалась."
    cs_narrator "Семён выпрямился."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "В любом случае здесь кто-то проезжал."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1e6630981d0c704964d6
    cs_ls "Да."
    cs_ls "И это уже больше, чем у нас было утром."
    cs_narrator "Мы осмотрели лавку."
    cs_narrator "Под ней нашлись сухие листья, бумажка от какой-то конфеты и потерянный карандаш."
    cs_narrator "Карандаш Даша подняла."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: 2b547caa7a77ac7494a7
    cs_da "Вот."
    cs_da "Первая улика."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Надеюсь, не придётся выяснять судьбу его владельца."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Скорее всего, кто-то из пионеров потерял."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "В таком случае загадка почти раскрыта."
    cs_narrator "Женя отошла к стойке с расписанием."
    cs_narrator "Через несколько секунд она позвала нас."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Здесь кое-что написано."
    cs_narrator "Я подошла ближе."
    cs_narrator "На обратной стороне стойки белели буквы, выведенные мелом."
    $ cs_pov_begin()
    with cs_sprite_leave
    show screen cs_d5_insert("НЕ ОГЛЯДЫВАЙСЯ", "Надпись на остановке")
    $ cs_bus_cue('warning')
    cs_narrator "НЕ ОГЛЯДЫВАЙСЯ."
    cs_narrator "Несколько секунд я просто смотрела на надпись."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Это было здесь раньше?"
    hide screen cs_d5_insert
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 94a6e3d3edbbd295615b
    cs_mz "Не знаю."
    cs_mz "Мы ведь с обратной стороны не смотрели."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Может, кто-то пошутил."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 4d88dbb22d5051378516
    cs_ls "Возможно."
    cs_ls "Но чувство юмора у человека довольно своеобразное."
    cs_narrator "Женя достала карандаш."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Я зарисую."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 9ddc377445a59ce650d6
    cs_ls "Хорошо."
    cs_ls "Только не стирай."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Я и не собиралась."
    cs_narrator "Я отошла на шаг."
    cs_narrator "Слова были написаны совершенно обычным почерком."
    # cs_page_anchor: f5b772c119d5aafd80d1
    cs_narrator "Никаких странных символов."
    cs_narrator "Никаких загадочных рисунков."
    cs_narrator "Просто надпись мелом."
    cs_narrator "Наверное, именно это раздражало больше всего."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Мы теперь должны стоять и смотреть только вперёд?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 794dfdef0c0f08cd406e
    cs_ls "Пока нет."
    cs_ls "Не хочу подчиняться каждой надписи, которую кто-то оставил на улице."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Но запомнить стоит."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Согласна."
    cs_narrator "Семён сел на лавку."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    # cs_page_anchor: 9d21cd5751248b4c69b4
    cs_sy "Давайте ещё минуту посидим и пойдём обратно."
    cs_sy "Ольга Дмитриевна просила не задерживаться."
    cs_narrator "Я посмотрела на дорогу."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Хорошая идея."
    cs_narrator "За деревьями было тихо."
    $ cs_bus_cue('approach')
    cs_narrator "Потом откуда-то издалека донёсся звук двигателя."
    cs_narrator "Я повернула голову."
    cs_narrator "Семён тоже услышал."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Машина?"
    cs_narrator "Даша встала рядом со мной."
    $ cs_bus_cue('near')
    cs_narrator "Звук приближался."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Лучше отойти к воротам."
    cs_narrator "Никто не возражал."
    cs_narrator "Мы отошли от остановки."
    $ cs_d5_room("cs_bus410_closed_day", duration=1.6, force=True)
    cs_narrator "И через несколько секунд из-за поворота показался автобус."
    cs_narrator "Светлый кузов."
    cs_narrator "Красная полоса."
    cs_narrator "Номер маршрута — четыреста десятый."
    cs_narrator "Я почувствовала, как всё внутри неприятно сжалось."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ну конечно."
    cs_narrator "Автобус медленно подъехал к остановке."
    cs_narrator "Я посмотрела на лобовое стекло."
    cs_narrator "Водительского места было достаточно хорошо видно."
    $ cs_bus_cue('uncanny')
    cs_narrator "Оно было пустым."
    return
