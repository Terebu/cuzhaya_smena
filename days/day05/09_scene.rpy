# -*- coding: utf-8 -*-
label cs_day05_09:
    $ cs_d5_scene = 9
    $ save_name = "Чужая смена — День 5: Десять минут без расследования"
    $ cs_bus_scene_enter(9)
    cs_narrator "Когда последняя книга оказалась на полке, я наконец выпрямилась."
    cs_narrator "Спина затекла."
    cs_narrator "Рука тоже напоминала о себе."
    cs_narrator "Женя заметила, как я осторожно размяла плечо."
    $ cs_d5_focus("mz")
    with cs_sprite_change
    # cs_page_anchor: 0c55a1dc19fab17011c7
    cs_mz "Всё, хватит."
    cs_mz "Иди отдохни."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Меня только что официально выгнали с работы?"
    $ cs_d5_focus("mz")
    with cs_sprite_change
    cs_mz "Отправили на перерыв."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Звучит благороднее."
    cs_narrator "Семён остался за столом."
    cs_narrator "Женя хотела уточнить у него ещё несколько деталей сна."
    cs_narrator "Даша посмотрела на меня."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Пойдём прогуляемся?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "С удовольствием."
    $ cs_d5_room("cs_camp_path_day")
    cs_narrator "Мы вышли из библиотеки и направились к спортплощадке."
    cs_narrator "На поле играли в футбол."
    cs_narrator "Двое мальчишек спорили, был ли гол."
    cs_narrator "Третий стоял возле ворот и выглядел так, словно ему надоело вообще всё происходящее."
    $ cs_d5_focus("d5_pioneer")
    with cs_sprite_change
    cs_d5_pioneer "Мяч прошёл мимо!"
    $ cs_d5_focus("d5_other_pioneer")
    with cs_sprite_change
    cs_d5_other_pioneer "Да ты даже не смотрел!"
    cs_narrator "Я остановилась."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Вот у людей проблемы."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "А тебе что, не нравятся?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: e62305780fce384f0465
    cs_ls "Наоборот."
    cs_ls "Очень завидую."
    cs_ls "Хотела бы и я сейчас переживать исключительно из-за мяча."
    cs_narrator "Мы сели на скамейку."
    cs_narrator "Даша вытянула ноги."
    $ cs_d5_room("bg ext_playground_day")
    cs_narrator "Я прислонилась к спинке."
    cs_narrator "Несколько минут просто смотрела на игру."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Ты умеешь отдыхать?"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Теоретически."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Тогда попробуй на практике."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "А если не получится?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Будем тренироваться."
    cs_narrator "Я повернулась к ней."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 277c66ee931f9d117823
    cs_ls "Жестокая женщина."
    cs_ls "Заставляет человека сидеть и ничего не делать."
    cs_narrator "Даша засмеялась."
    if cs_d5_shared_pace:
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Утром было хорошо."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Когда мы бегали?"
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Когда перестали бегать."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Вот уж не ожидала, что моя тренировка закончится такой оценкой."
        $ cs_d5_focus("da")
        with cs_sprite_change
        # cs_page_anchor: 6f4035731236c68b7b7d
        cs_da "Мне понравилось просто идти рядом."
        cs_da "Без спешки."
        cs_narrator "Я посмотрела на неё."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Тогда будем иногда повторять."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Договорились."
    else:
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "А я утром думала, что ты опять куда-нибудь убежишь."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Я же сказала, что сделаю один круг."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Ты часто говоришь одно, а потом находишь что-нибудь интересное по дороге."
        cs_narrator "Я задумалась."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Неприятно, когда тебя знают настолько хорошо."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Привыкай."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом я посмотрела на Дашу."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Ты хочешь домой?"
    cs_narrator "Она не ответила сразу."
    cs_narrator "Проследила взглядом за мячом, который пролетел мимо ворот."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: a7b180aa0da3cb4e47e2
    cs_da "Хочу."
    cs_da "Конечно."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Я кивнула."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: e1edbcda603549c41a9c
    cs_da "Там моя жизнь."
    cs_da "Люди, которых я знаю."
    cs_da "Наверное, они уже переживают."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "А здесь?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Здесь тоже есть кое-что хорошее."
    cs_narrator "Она повернулась ко мне."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Но это не значит, что мне не страшно."
    cs_narrator "Я опустила взгляд."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Мне тоже."
    cs_narrator "Даша немного помолчала."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "А больше всего я боюсь, что появится автобус, мы сядем, и окажется, что он везёт нас совершенно не туда."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Или скажет, что уехать может только кто-то один."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Нам ведь этого никто не говорил."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 1ef76cf743a97418b7ce
    cs_ls "Знаю."
    cs_ls "Просто предпочитаю заранее придумать худший вариант."
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Не самая полезная привычка."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Зато потом иногда приятно удивляешься."
    cs_narrator "Она посмотрела на меня с лёгкой укоризной."
    cs_narrator "Я улыбнулась."
    if cs_da_shared_bed_day3 and cs_da_love_confession_day3:
        cs_narrator "Я протянула руку."
        cs_narrator "Даша вложила в неё свою ладонь."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Только давай договоримся."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "О чём?"
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Если нам действительно предложат какой-нибудь выбор, не решай за меня."
        cs_narrator "Я посмотрела на неё."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Хорошо."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Даже если будешь уверена, что так лучше."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Тогда и ты за меня не решай."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Договорились."
        cs_narrator "Я чуть сжала её руку."
        cs_narrator "Некоторое время мы сидели рядом, не разговаривая."
    elif cs_friend_da >= 4:
        cs_narrator "Даша слегка толкнула меня плечом."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Если найдётся нормальный способ вернуться, будем разбираться вместе."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "А если ненормальный?"
        $ cs_d5_focus("da")
        with cs_sprite_change
        # cs_page_anchor: 993eafd533a5d8d2bd04
        cs_da "Тем более вместе."
        cs_da "Только не убегай проверять первой."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Ты сейчас окончательно разрушила мою репутацию бесстрашного исследователя."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Переживёшь."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Вероятно."
    else:
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Давай хотя бы рассказывать друг другу всё, что узнаём."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        cs_ls "Согласна."
        $ cs_d5_focus("da")
        with cs_sprite_change
        cs_da "Без попыток справиться со всем в одиночку."
        $ cs_d5_focus("ls")
        with cs_sprite_change
        # cs_page_anchor: 5e20d8e235df5201d50e
        cs_ls "Хорошо."
        cs_ls "Постараюсь."
    cs_narrator "С поля выкатился футбольный мяч."
    cs_narrator "Он остановился возле моей ноги."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_th "Я поднялась, подцепила его носком кеда и отправила обратно."
    $ cs_d5_focus("d5_pioneer")
    with cs_sprite_change
    cs_d5_pioneer "Спасибо!"
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Пожалуйста!"
    cs_narrator "Даша посмотрела на меня."
    $ cs_d5_focus("da")
    with cs_sprite_change
    # cs_page_anchor: ed1141e9954a5d35aa0e
    cs_da "Видишь?"
    cs_da "Уже поучаствовала в жизни лагеря."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    cs_ls "Можно считать, что общественная работа на сегодня выполнена?"
    $ cs_d5_focus("da")
    with cs_sprite_change
    cs_da "Попробуй объяснить это Ольге Дмитриевне."
    cs_narrator "Я вздохнула."
    $ cs_d5_focus("ls")
    with cs_sprite_change
    # cs_page_anchor: 82acbdd74149e3ebaf94
    cs_ls "Ладно."
    cs_ls "Пойдём обратно."
    cs_narrator "Мы поднялись со скамейки."
    cs_narrator "Десять минут действительно прошли спокойно."
    cs_narrator "И мне неожиданно захотелось, чтобы таких минут было побольше."
    return
