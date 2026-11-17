# -*- coding: utf-8 -*-
label cs_day05_21:
    if cs_d5_missing_minute_done:
        return
    $ save_name = "Чужая смена — День 5: Пропавшая минута"
    $ cs_d5_scene = 20
    cs_narrator "Над столом коротко треснуло."
    $ cs_d5_room("bg int_house_of_mt_night")
    cs_narrator "Лампочка вспыхнула так ярко, что я зажмурилась."
    cs_narrator "Даша вздрогнула и ухватилась за мой рукав."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Вы включили?"
    cs_narrator "Она смотрела на Ольгу Дмитриевну."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Нет."
    cs_narrator "Вожатая перевела взгляд с лампы на выключатель у двери."
    cs_mt "Его никто не трогал. Сидите пока."
    cs_narrator "Семён сразу посмотрел на часы."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А эти так и стоят."
    cs_narrator "23:59. Ни одна стрелка не сдвинулась."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Женя, запиши. Свет вернулся, часы стоят."
    cs_narrator "Ольга Дмитриевна положила включённый фонарь на стол."
    cs_narrator "Гасить его никто не предложил."
    cs_narrator "Я разжала пальцы и только тогда заметила, как крепко держалась за край стула."
    cs_narrator "При свете лампы надпись на двери читалась ещё отчётливее."
    cs_narrator "За окном по-прежнему было тихо."
    $ cs_d5_clock = "23:59"
    show screen cs_d5_clock_face
    $ cs_d5_focus("mz")
    with cs_sprite_enter
    cs_narrator "Женя сделала пометку и попросила повторить, на чём мы остановились."
    cs_narrator "Я открыла рот и вдруг поняла, что забыла, о чём собиралась говорить."
    cs_narrator "Не слова — весь разговор на несколько секунд ушёл куда-то в сторону."
    cs_narrator "Я выпрямилась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Даш, тебе тоже спать хочется?"
    cs_narrator "Она потёрла глаза."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Только что накрыло."
    cs_narrator "Семён уронил карандаш."
    cs_narrator "Наклонился поднять, но остановился, держась за край кровати."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "Как-то резко."
    cs_narrator "Ольга подошла к нему и сама опёрлась на спинку стула."
    $ cs_d5_focus("mt")
    with cs_sprite_change
    cs_mt "Виола?"
    cs_narrator "Та смотрела на нас, явно пытаясь сосредоточиться."
    $ cs_d5_focus("vi")
    with cs_sprite_change
    cs_vi "Сядьте."
    cs_vi "Не ходите сейчас."
    cs_narrator "Я послушалась."
    cs_narrator "До соседнего стула было полшага, но колени вдруг стали ненадёжными."
    cs_narrator "Женя провела ладонью по лицу."
    cs_narrator "Тихонова положила альбом на колени и прислонилась к стене."
    if cs_d5_slavya_present:
        cs_narrator "Славя опустилась на свободный стул, так и не убрав плед."
    if cs_d5_alisa_present:
        cs_narrator "Алиса пыталась что-то сказать и закрыла глаза, опершись о стену."
    if cs_d5_miku_present:
        cs_narrator "Мику прижала ладонь ко лбу и попросила не вставать без неё."
    cs_narrator "Я посмотрела на часы."
    cs_narrator "Всё ещё 23:59."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ну нет."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Мы тут вообще-то заняты."
    cs_narrator "Прозвучало тихо."
    cs_narrator "Возмутиться как следует уже не хватило сил."
    $ cs_director_scene("cs_cg_day05_missing_minute")
    scene cs_cg_day05_missing_minute with Dissolve(0.7)
    cs_narrator "Даша придвинулась ближе и взяла меня за запястье."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Не вставай."
    cs_da "Я здесь."
    cs_narrator "Я хотела дотянуться до листа, но пальцы задели только край."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Записи…"
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "На столе."
    cs_narrator "Семён поднял голову."
    $ cs_d5_focus("sy")
    with cs_sprite_change
    cs_sy "А если забудем?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Тогда сравним, что осталось."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "У всех по отдельности."
    cs_narrator "Он что-то ответил."
    cs_narrator "Я уже не разобрала."
    cs_narrator "Даша всё ещё держала мою руку."
    cs_narrator "Я почувствовала, как она сама покачнулась, и попыталась сесть ровнее, чтобы не утащить её за собой."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Только не отпускай."
    cs_narrator "Она сжала пальцы."
    cs_narrator "На листе передо мной расплывались две строчки."
    cs_narrator "Я старалась прочитать их ещё раз, но глаза закрывались."
    cs_narrator "Последним запомнился свет фонаря на столе и Дашина ладонь у моего рукава."
    cs_narrator "Как мы вышли из домика, я не помнила."
    $ cs_d5_missing_minute_done = True
    hide screen cs_d5_clock_face
    hide screen cs_d5_notes
    hide screen cs_d5_insert
    $ cs_bus_cue("silence")
    window hide dissolve
    $ cs_director_scene("black")
    scene black with Dissolve(1.0)
    return
