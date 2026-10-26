# -*- coding: utf-8 -*-
label cs_day03_136:
    $ save_name = "Чужая смена — День 3: Хорошие новости требуют свидетелей"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_frame_focus([])
    with Dissolve(0.7)
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.12,delay=1.0,channel="music")
    cs_narrator "Я сделала несколько шагов."
    cs_narrator "Потом остановилась."
    cs_narrator "Посмотрела на книгу."
    cs_narrator "Ну что ж."
    cs_narrator "Прекрасно."
    cs_narrator "Действительно прекрасный день."
    if cs_mz_open_library_invitation_day3:
        cs_narrator "Женя сама предложила мне приходить."
        cs_narrator "Даже без книги."
        cs_narrator "Надо же."
        cs_narrator "Пожалуй, это можно считать очень серьёзным достижением."
        cs_narrator "Я прижала роман к груди здоровой рукой."
        cs_narrator "Широко улыбнулась."
        cs_ls "Товарищ Соколова, поздравляю. Вас официально допустили в общество людей, умеющих молчать."
        cs_narrator "Я тихо рассмеялась."
    elif cs_mz_friend_on_arrival_day3 >= 2:
        if cs_mz_friend_on_arrival_day3 >= 2:
            cs_narrator "Женя выбрала для меня книгу."
        else:
            cs_narrator "Женя помогла мне выбрать книгу."
        cs_narrator "Причём не случайную."
        cs_narrator "Она действительно запомнила, что я рассказывала."
        cs_narrator "Я посмотрела на обложку."
        cs_ls "Великолепно. Осталось не разочаровать библиотекаря собственной литературной неграмотностью."
        cs_narrator "Я улыбнулась."
    else:
        cs_narrator "Что ж."
        cs_narrator "Библиотека действительно оказалась хорошим местом."
        cs_narrator "Даже если наши отношения с Женей пока ограничиваются выдачей книг и короткими разговорами."
        cs_narrator "Я посмотрела на роман."
        cs_ls "Ну что, товарищ Гончаров, продолжим знакомство вечером."
    cs_narrator "Я направилась к площади."
    cs_narrator "Впереди уже слышались знакомые голоса."
    cs_narrator "Похоже, музыкальный клуб тоже закончил очередную репетицию."
    cs_narrator "Интересно, как там Даша?"
    cs_narrator "Наверняка Мику успела предложить ещё несколько вариантов мелодии."
    cs_narrator "А Алиса — объяснить, почему хотя бы половину из них нужно немедленно выбросить."
    cs_narrator "Я улыбнулась."
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    cs_narrator "И почти сразу увидела Дашу."
    cs_narrator "Она шла со стороны клубов."
    cs_narrator "Увидев меня, помахала рукой."
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    if renpy.showing("cs_darya"):
        show cs_darya wave pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_da "Лен!"
    cs_narrator "Я улыбнулась."
    cs_ls "О, музыкальная общественность вернулась."
    cs_narrator "Она рассмеялась."
    cs_da "А литературная?"
    cs_narrator "Я подняла книгу."
    cs_ls "С богатыми трофеями."
    cs_narrator "Дарья посмотрела на обложку."
    cs_da "Гончаров?"
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_da "Нравится?"
    cs_ls "Пока очень."
    cs_narrator "Она улыбнулась."
    cs_da "А Женя?"
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Задумалась."
    cs_narrator "Потом довольно улыбнулась."
    if cs_mz_open_library_invitation_day3:
        cs_ls "Даша."
        cs_narrator "Она насторожилась."
        cs_da "Что?"
        cs_narrator "Я выпрямилась."
        cs_ls "Должна сообщить тебе чрезвычайно важную новость."
        cs_narrator "Она рассмеялась."
        cs_da "Какую?"
        cs_narrator "Я подняла палец."
        cs_ls "Женя сама сказала, что я могу приходить в библиотеку, даже когда не собираюсь брать книги."
        cs_narrator "Дарья на секунду удивилась."
        cs_narrator "Потом улыбнулась."
        cs_da "Правда?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Это, между прочим, высшая форма доверия в отдельно взятом культурном учреждении."
        cs_narrator "Она рассмеялась."
        cs_da "Поздравляю."
        cs_narrator "Я улыбнулась."
        cs_ls "Спасибо. Прошу считать сегодняшнюю дипломатическую миссию успешно завершённой."
        cs_da "И сколько же разговоров тебе для этого понадобилось?"
        cs_narrator "Я задумалась."
        cs_ls "Меньше, чем я первоначально планировала. Подозрительно эффективный метод."
        if renpy.showing("cs_darya"):
            show cs_darya shrug pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья покачала головой."
    else:
        cs_ls "Нормально поговорили. Она даже спросила, что я думаю о книге."
        if renpy.showing("cs_darya"):
            show cs_darya shy_smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья улыбнулась."
        cs_da "Значит, подружились?"
        cs_narrator "Я немного подумала."
        cs_ls "Думаю, постепенно."
        cs_narrator "Она кивнула."
        cs_da "Хорошо."
    cs_narrator "Мы пошли рядом."
    cs_narrator "Я посмотрела на Дашу."
    cs_ls "А у тебя как прошло?"
    cs_narrator "Она улыбнулась."
    cs_da "Хорошо. Мику показала ещё одно вступление. Потом мы немного поиграли."
    cs_narrator "Я приподняла бровь."
    cs_ls "«Немного» — это сколько?"
    cs_narrator "Она задумалась."
    cs_da "Минут двадцать, наверное."
    cs_narrator "Я кивнула."
    cs_ls "То есть ещё пара посещений, и можно будет продавать билеты."
    cs_narrator "Дарья засмеялась."
    cs_da "Лена."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Всё. Молчу. Не вмешиваюсь в коммерческую деятельность музыкантов."
    cs_narrator "Она покачала головой."
    cs_da "У тебя любая тема превращается в какую-то организацию."
    cs_narrator "Я задумалась."
    cs_ls "Возможно, я просто слишком долго жила среди людей, которые на каждую идею сначала составляют план."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    if cs_mi_followup_invitation_day3:
        cs_narrator "Дарья вдруг вспомнила:"
        cs_da "Кстати, Мику просила передать, что всё ещё хочет показать тебе окончательный вариант вступления."
        cs_narrator "Я заинтересовалась."
        cs_ls "Того самого?"
        cs_narrator "Она кивнула."
        cs_da "Да. Говорит, твоё замечание про плавное начало ей помогло."
        cs_narrator "Я улыбнулась."
        cs_ls "Тогда заглянем. Не прямо сейчас, но немного позже."
    if cs_dv_followup_invitation_day3:
        cs_narrator "Дарья улыбнулась чуть шире."
        cs_da "И Алиса тоже спрашивала, где ты пропала."
        cs_narrator "Я удивилась."
        cs_ls "Вот как?"
        cs_narrator "Она кивнула."
        cs_da "Сказала, что хотела показать тебе один новый переход на гитаре."
        cs_narrator "Я задумалась."
        cs_ls "Надо же. Меня начинают использовать как независимого эксперта по художественным вопросам."
        cs_da "Она сказала примерно то же самое. Только менее вежливо."
        cs_narrator "Я рассмеялась."
        cs_ls "Тогда точно Алиса."
    if cs_un_sketch_time_agreed_day3:
        cs_narrator "Я вспомнила ещё кое-что."
        cs_ls "Кстати, мне надо будет встретиться с Тихоновой."
        cs_narrator "Дарья посмотрела на меня."
        cs_da "Порисовать?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Договорились ближе к вечеру."
        cs_narrator "Она улыбнулась."
        cs_da "Тогда тебе нужно успеть."
        cs_narrator "Я посмотрела на часы."
        cs_ls "Успею. Главное — не начинать ещё одну полуторачасовую дискуссию о Гончарове."
        if renpy.showing("cs_darya"):
            show cs_darya amused pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Дарья рассмеялась."
    cs_narrator "Мы миновали библиотеку."
    cs_narrator "Свернули к площади."
    cs_narrator "И я вдруг поняла, что совсем не чувствую себя человеком, которому необходимо срочно найти новое занятие."
    cs_narrator "Впервые за эти дни у меня уже было достаточно дел."
    cs_narrator "Причём не навязанных."
    cs_narrator "Желаемых."
    cs_narrator "Интересная разница."
    if cs_sl_poster_collected_day3 and cs_day03_poster_location == "darya_folder":
        cs_narrator "Папку с плакатом Даша несла под мышкой: из клуба она забрала её с собой."
    return
