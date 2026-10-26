# -*- coding: utf-8 -*-
label cs_day03_166:
    $ save_name = "Чужая смена — День 3: Возвращение за пропавшим литературным интересом"
    $ cs_director_scene("cs_house_lena_darya_ext_sunset")
    scene cs_house_lena_darya_ext_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "До домика я добралась уже без остановок."
    cs_th "Надо же."
    cs_th "Действительно без приключений."
    cs_th "Это начинает выглядеть подозрительно."
    cs_narrator "Я поднялась на крыльцо."
    cs_narrator "Открыла дверь."
    $ cs_director_scene("cs_house_lena_darya_int_sunset")
    scene cs_house_lena_darya_int_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "Внутри было тихо."
    cs_narrator "Вечерний свет проникал через окно."
    cs_narrator "На столе лежали мои наброски."
    cs_narrator "Рядом — аккуратно сложенные вещи."
    if cs_sl_poster_collected_day3:
        cs_narrator "На столе лежала папка с концертным плакатом, которую мы оставили здесь раньше."
        cs_th "Вот и хорошо."
        cs_th "Хотя бы одно художественное произведение сегодня не требует спасательной операции."
    cs_narrator "Я подошла к столу."
    cs_narrator "Книга лежала там, где я её оставила."
    label cs_check_day03_166_book_taken:
    $ cs_day03_reading_book_location = "with_lena"
    cs_narrator "Взяла её здоровой рукой."
    cs_narrator "Посмотрела на обложку."
    cs_ls "Так. Товарищ Гончаров на месте."
    cs_narrator "Осторожно открыла роман на закладке."
    cs_narrator "Проверила страницу."
    cs_th "Всё правильно."
    cs_th "Никто не перепутал главы."
    cs_th "Никто не вырвал страницы."
    cs_th "Великая литература пережила моё отсутствие."
    cs_narrator "Я закрыла книгу."
    cs_narrator "И на секунду задержалась."
    cs_narrator "В комнате было приятно."
    cs_narrator "Тихо."
    cs_narrator "Спокойно."
    cs_narrator "Можно было бы просто остаться здесь."
    cs_narrator "Сесть на кровать."
    cs_narrator "Продолжить читать."
    cs_th "Вообще-то это даже проще."
    cs_th "Не нужно никуда возвращаться."
    cs_th "Не нужно снова проходить через площадь."
    cs_narrator "Но я вспомнила Женю."
    cs_narrator "Она уже согласилась, что я могу прийти."
    if cs_mz_evening_help_day3:
        cs_th "И мы ещё обещали помочь ей с библиотечными записями."
        cs_th "Даша уже должна быть там."
        cs_th "Задерживаться точно не стоит."
    else:
        cs_th "А ещё мне хотелось хотя бы ненадолго вернуться туда."
        cs_th "Не потому, что в домике нельзя читать."
        cs_th "Просто там мне тоже хорошо."
    cs_narrator "Я посмотрела на повязку."
    cs_narrator "Осторожно поправила рукав."
    cs_th "Локоть в порядке."
    cs_th "Книга в руках."
    cs_th "План предельно понятен."
    cs_th "Теперь нужно всего лишь вернуться."
    cs_narrator "Я направилась к двери."
    cs_narrator "Потом остановилась."
    cs_narrator "Посмотрела на блокнот."
    cs_th "Так."
    cs_th "Может, ещё карандаш взять?"
    cs_narrator "Пауза."
    cs_th "Нет."
    cs_th "Соколова, ты идёшь читать."
    cs_th "Не открывать филиал художественной школы."
    cs_narrator "Я усмехнулась."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "И вышла."
    $ cs_day03_evening_book_retrieved = True
    return
