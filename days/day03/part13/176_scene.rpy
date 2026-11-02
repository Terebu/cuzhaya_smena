# -*- coding: utf-8 -*-
label cs_day03_176:
    $ save_name = "Чужая смена — День 3: Девушка, которая ждала"
    cs_narrator "Я спустилась с крыльца. Сделала несколько шагов."
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    cs_narrator "И услышала знакомый голос."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Ну наконец-то."
    cs_narrator "Я обернулась. На скамейке неподалёку сидела Даша."
    $ cs_da_waiting_outside_library_day3 = True
    $ cs_day03_darya_destination = "with_lena"
    cs_narrator "Она поднялась, когда я посмотрела в её сторону. Я немного удивилась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Даш?"
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Привет."
    cs_narrator "Я подошла ближе."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ты чего здесь?"
    cs_narrator "Она посмотрела на библиотеку, потом на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Тебя ждала."
    if cs_mz_evening_help_completed_day3:
        cs_narrator "Я вспомнила, как она вышла на улицу, пока я заканчивала роман."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "А я думала, ты уже пошла в домик."
        cs_narrator "Даша покачала головой."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Нет. Я же сказала, что немного посижу здесь."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Точно."
        cs_narrator "Она улыбнулась."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Только не думала, что твоё «совсем чуть-чуть» растянется ещё на несколько страниц."
        cs_narrator "Я вздохнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Сама не ожидала."
    else:
        cs_narrator "Я удивлённо посмотрела на неё."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "А ты разве не к Мику собиралась?"
        cs_narrator "Даша кивнула."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Сходила. Немного поговорили о завтрашних занятиях."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "И потом?"
        cs_narrator "Она посмотрела на освещённое окно библиотеки."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Шла к домику, увидела, что здесь ещё горит свет. Подумала, что ты, наверное, всё ещё читаешь."
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_ls "Очень смелая гипотеза."
        cs_narrator "Даша рассмеялась."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        if cs_reflective_shot:
            $ cs_pov_end()
            with cs_sprite_change
        cs_da "Ну вот. Решила немного подождать."
    cs_narrator "Я посмотрела на неё."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Давно сидишь?"
    cs_narrator "Она пожала плечами."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Нет, всего несколько минут. Не успела замёрзнуть."
    cs_narrator "Я помолчала. Потом улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Всё-таки могла зайти."
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Не хотела мешать."
    cs_narrator "Я посмотрела на неё."
    cs_th "Вот ведь. Она действительно не стала меня отвлекать. Не потому, что я попросила. Просто знала, что мне хочется дочитать."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Спасибо."
    cs_narrator "Даша слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Не за что."
    cs_narrator "Я посмотрела на её руки, потом на скамейку."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Не замёрзла?"
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Нет. Но домой уже хочется."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Тогда пойдём."
    cs_narrator "Она улыбнулась. Потом посмотрела на мои пустые руки."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "А книга?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Дочитана. Возвращена. Официально закрыта."
    cs_narrator "Даша подняла бровь."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Даже так?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да. Наш бурный роман с Иваном Александровичем завершился."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "И как ощущения?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Неожиданно хорошие."
    cs_narrator "Она улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Значит, стоило того?"
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Определённо."
    cs_narrator "Потом посмотрела на неё."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Ну что, теперь всё внимание снова твоё."
    cs_narrator "Даша усмехнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_da "Какая честь."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Пользуйся, пока не нашла следующего писателя."
    cs_narrator "Она рассмеялась. Я подошла ближе. Предложила ей здоровую руку. Даша взяла меня под руку."
    $ cs_da_waiting_outside_library_day3 = False
    cs_narrator "И мы направились по дорожке."
    return
