# -*- coding: utf-8 -*-
# Source: source/prologue.md. Dialogue is preserved verbatim.
label cs_scene_06:
    $ save_name = u"Чужая смена — Последняя остановка"
    show cs_bus_winter at cs_bus_ride zorder -10 with Dissolve(1.5)
    stop music fadeout 2.0
    cs_narrator "Автобус качнуло на повороте."
    cs_narrator "За стеклом промелькнул дорожный знак."
    cs_narrator "Я попыталась прочитать надпись."
    cs_narrator "Не успела."
    cs_narrator "Деревья становились всё плотнее."
    cs_narrator "Дорога — уже."
    cs_narrator "Странно."
    cs_narrator "Очень странно."
    cs_narrator "Почему-то мне даже показалось, что по этой дороге мы уже проезжали."
    cs_narrator "Хотя отличить один заснеженный участок леса от другого было практически невозможно."
    cs_narrator "Я посмотрела вперёд."
    cs_narrator "Водитель сидел неподвижно."
    cs_narrator "Только руки на руле немного двигались."
    cs_narrator "Всё выглядело совершенно обыденно."
    cs_narrator "И всё-таки что-то было не так."
    cs_narrator "Я не могла объяснить что именно."
    cs_narrator "Наверное, просто устала."
    cs_th "Нужно было вчера лечь спать раньше."
    cs_narrator "Я зевнула."
    cs_narrator "Рядом Дарья тоже чуть откинулась на спинку сиденья."
    label cs_check_sleep_winter:
    cs_narrator "Я заметила, как она прикрыла глаза."
    cs_ls "Спать хочешь? — спросила я."
    cs_narrator "Она чуть повернула голову."
    # cs_darya_variety: reaction
    show cs_dasha_winter shy normal at cs_darya_normal_center
    cs_da "Немного."
    cs_ls "Аналогично."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    cs_da "Долго ещё ехать?"
    cs_narrator "Я посмотрела на зимний лес."
    cs_ls "Понятия не имею."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    cs_da "Обнадёживает."
    cs_ls "Я стараюсь."
    cs_narrator "Мы обе ненадолго замолчали."
    cs_narrator "Я снова прислонилась к окну."
    cs_narrator "От отопителя клонило в сон всё сильнее."
    cs_narrator "Веки постепенно тяжелели."
    cs_th "Может, буквально на минутку?"
    cs_th "Ничего ведь не случится."
    cs_narrator "Я прикрыла глаза."
    cs_narrator "Автобус мягко покачивался."
    cs_narrator "Колёса негромко шуршали по дороге."
    cs_narrator "Где-то впереди что-то звякнуло."
    cs_narrator "Потом всё снова стало тихо."
    stop music fadeout 6.0
    cs_narrator "Я слышала собственное дыхание."
    cs_narrator "Ровное."
    cs_narrator "Медленное."
    cs_narrator "Рядом сидела Дарья."
    scene cs_sleep_winter with Dissolve(1.5)
    label cs_check_cg_winter:
    cs_narrator "За окном был зимний лес."
    cs_narrator "Ничего необычного."
    cs_narrator "Ничего страшного."
    cs_narrator "Просто автобус."
    cs_narrator "Просто дорога."
    cs_narrator "Просто очень неудачная поездка в супермаркет."
    cs_narrator "Звуки постепенно становились тише."
    stop ambience fadeout 5.0
    cs_narrator "Всё дальше."
    cs_narrator "Будто я медленно погружалась под воду."
    cs_narrator "Я попыталась открыть глаза."
    cs_narrator "Не получилось."
    cs_narrator "Или просто не захотелось."
    cs_th "Надо будет спросить у водителя..."
    cs_th "...где мы вообще..."
    window hide dissolve
    scene black with Dissolve(3.0)
    stop ambience fadeout 3.0
    pause 3.0
    window hide dissolve
    pause 3.0
    return
