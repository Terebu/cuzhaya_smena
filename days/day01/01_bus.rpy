# -*- coding: utf-8 -*-
# Source: source/day01_staged.md.
label cs_day01_01:
    $ save_name = u"Чужая смена — День 1: Отклонение от маршрута"
    scene bg int_bus with Dissolve(1.2)
    window show dissolve
    $ renpy.music.set_volume(0.65, delay=1.0, channel="music")
    play music cs_day_music_think fadeout 2.0 fadein 3.0
    $ renpy.music.set_volume(0.35, delay=2.0, channel="ambience")
    play ambience cs_camp fadein 2.0
    label cs_check_day01_bus:
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_narrator "Я ещё секунд десять смотрела на вывеску."
    cs_narrator "{b}«СОВЁНОК».{/b}"
    cs_narrator "Затем перевела взгляд на летнее небо."
    cs_narrator "На Дарью."
    cs_narrator "И снова на вывеску."
    cs_ls "Ну… Кажется, четыреста десятый немного отклонился от маршрута."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "Насколько немного?"
    cs_narrator "Я расстегнула куртку."
    cs_narrator "Под ней был свитер. Под свитером — ещё один слой одежды."
    cs_narrator "Всё вполне оправданно."
    cs_narrator "Двадцать минут назад на улице стояла зима."
    cs_ls "Для начала я выехала за продуктами в январе. А приехала, судя по всему, в июль."
    pause 0.5
    cs_ls "Неплохая транспортная реформа."
    cs_narrator "Я высунула руку в открытое окно."
    cs_narrator "Жара была настоящей."
    cs_narrator "Не неисправное отопление."
    cs_narrator "Не остаточное ощущение после сна."
    cs_narrator "Тёплый воздух, запах нагретой земли, травы и хвои."
    cs_narrator "Я медленно убрала руку."
    cs_ls "Великолепно. Осталось выяснить, где принимают жалобы на перевозчика."
    cs_narrator "Дарья молчала."
    cs_narrator "Я повернулась к ней."
    cs_ls "Что?"
    cs_da "Просто пытаюсь понять, ты всегда настолько спокойно реагируешь на невозможное?"
    cs_ls "Нет. Обычно я хотя бы понимаю, что происходит."
    cs_narrator "Я стянула куртку с плеч."
    cs_ls "Сегодня решила разнообразить программу."
    pause 0.7
    cs_narrator "Автобус был пуст."
    cs_narrator "Совершенно."
    cs_narrator "Ни водителя, ни пассажиров."
    cs_narrator "Только мы вдвоём."
    cs_narrator "И вот это мне уже нравилось значительно меньше."
    cs_narrator "Я поднялась и прошла по салону к кабине."
    cs_ls "Эй?"
    pause 1.0
    cs_narrator "Тишина."
    cs_ls "Водитель?"
    cs_narrator "Никакого ответа."
    cs_narrator "Я подошла ближе."
    cs_narrator "Кабина оказалась пустой."
    cs_narrator "Ни ключей."
    cs_narrator "Ни сумки."
    cs_narrator "Ни каких-либо личных вещей."
    cs_narrator "Словно автобус самостоятельно доставил двух совершенно неподготовленных пассажирок к воротам советского пионерлагеря и решил, что его обязанности на сегодня выполнены."
    cs_narrator "Я посмотрела на приборную панель."
    cs_narrator "Затем через лобовое стекло."
    cs_narrator "Потом снова на приборную панель."
    cs_ls "Так."
    cs_narrator "Позади послышались шаги."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    cs_da "Что?"
    cs_ls "Кажется, поход за продуктами официально отменяется."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_da "Смелый вывод."
    cs_ls "Спасибо. Аналитический отдел сегодня особенно хорош."
    stop music fadeout 2.0
    return
