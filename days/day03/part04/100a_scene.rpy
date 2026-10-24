# -*- coding: utf-8 -*-
label cs_day03_100a:
    $ save_name = "Чужая смена — День 3: Медицинская бухгалтерия"
    cs_narrator "Я посмотрела на список."
    cs_ls "Виола, а давайте мы поможем?"
    cs_narrator "Она подняла голову."
    cs_vi "Вы?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Полагаю, после всех моих посещений я уже должна медпункту несколько часов общественно полезного труда."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья тихо рассмеялась."
    cs_narrator "Виола посмотрела на повязку."
    cs_vi "Только никакой нагрузки на руку."
    cs_ls "Разумеется. Могу считать и делать серьёзное лицо."
    cs_da "А я запишу результаты."
    cs_narrator "Виола немного подумала."
    cs_narrator "Затем кивнула."
    cs_vi "Хорошо. Тогда помогите проверить запечатанные упаковки. Остальное я сама."
    cs_narrator "Мы согласились."
    cs_narrator "Дарья взяла карандаш."
    cs_narrator "Я устроилась возле стола."
    cs_narrator "Виола поставила перед нами несколько небольших коробок."
    cs_ls "Так. Бинты. Шесть упаковок."
    cs_da "Записала."
    cs_narrator "Я посмотрела в следующую коробку."
    cs_ls "Пластырь. Восемь."
    cs_narrator "Дарья сверилась со списком."
    cs_da "Здесь написано десять."
    cs_narrator "Я нахмурилась."
    cs_narrator "Посмотрела внимательнее."
    cs_th "Хм."
    cs_th "Вот это уже интересно."
    cs_ls "Подожди. Кажется, ещё две упаковки лежат сбоку."
    cs_narrator "Я осторожно сдвинула лёгкую коробочку здоровой рукой."
    cs_narrator "Действительно."
    cs_narrator "Под ней нашлись две запечатанные упаковки."
    cs_da "Тогда всё сходится."
    cs_narrator "Я торжественно кивнула."
    cs_ls "Медицинская система спасена от кризиса учёта."
    if renpy.showing("cs"):
        show cs custom amused medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола рассмеялась."
    cs_vi "Даже не представляю, что бы я без вас делала."
    cs_narrator "Я задумалась."
    cs_ls "Подозреваю, закончила бы на десять минут позже."
    cs_narrator "Она улыбнулась."
    cs_vi "Скорее всего."
    cs_narrator "Мы продолжили."
    $ cs_director_scene("cs_cg_lena_darya_medical_inventory_day")
    scene cs_cg_lena_darya_medical_inventory_day
    with Dissolve(0.8)
    label cs_check_day03_101_inventory_cg:
    cs_narrator "Работа оказалась совершенно обычной."
    cs_narrator "Несколько коробок."
    cs_narrator "Небольшой список."
    cs_narrator "Записи карандашом."
    cs_narrator "Ничего выдающегося."
    cs_narrator "Но мне почему-то нравилось."
    cs_th "За последние два дня я слишком часто пыталась найти объяснение вещам, которые не желали объясняться."
    cs_th "А здесь всё просто."
    cs_th "Десять упаковок — это десять упаковок."
    cs_th "Шесть бинтов — шесть бинтов."
    cs_th "И никакая пространственная аномалия пока не пытается заставить их появляться снова."
    $ cs_director_scene("bg int_aidpost_day")
    scene bg int_aidpost_day
    show cs custom warm_smile medical normal at cs_viola_normal_left
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    label cs_check_day03_101_inventory_return:
    cs_narrator "Наконец Дарья поставила последнюю отметку."
    cs_da "Готово."
    cs_narrator "Виола проверила лист."
    cs_narrator "Затем улыбнулась."
    cs_vi "Спасибо. Всё правильно."
    cs_narrator "Я выпрямилась."
    cs_ls "Прошу выдать справку о временной пригодности к административной работе."
    if renpy.showing("cs"):
        show cs custom amused medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Виола усмехнулась."
    cs_vi "Сначала выздоровей."
    cs_narrator "Я вздохнула."
    cs_ls "Опять кадровые ограничения."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Виола тоже улыбнулась."
    return
