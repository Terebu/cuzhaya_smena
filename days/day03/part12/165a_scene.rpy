# -*- coding: utf-8 -*-
label cs_day03_165a:
    $ save_name = "Чужая смена — День 3: Соколова против канцелярии"
    $ cs_pov_end()
    with cs_sprite_change
    $ cs_frame_focus(["cs_semen", "sl"])
    with cs_sprite_change
    cs_narrator "Я посмотрела на листок."
    cs_ls "Слушайте, а что у вас там не сходится?"
    cs_narrator "Славя перевела взгляд на Семёна."
    cs_narrator "Потом на меня."
    cs_sl "Ольга Дмитриевна попросила уточнить, кто завтра помогает с инвентарём. Но в двух списках немного разные записи."
    cs_narrator "Семён показал на строчку."
    cs_sy "Вот здесь одно время, а здесь другое."
    cs_narrator "Я посмотрела внимательнее."
    cs_th "Хм."
    cs_th "Действительно."
    cs_th "В одном списке указан утренний сбор, а в другом — время, когда инвентарь нужно уже принести."
    cs_ls "А вы уверены, что это два времени одного и того же события?"
    cs_narrator "Славя задумалась."
    cs_sl "В смысле?"
    cs_narrator "Я показала на первую запись."
    cs_ls "Вот здесь написано, когда ответственные должны собраться."
    cs_narrator "Потом на вторую."
    cs_ls "А здесь — когда нужно сдать всё подготовленное."
    cs_narrator "Семён нахмурился."
    cs_narrator "Посмотрел внимательнее."
    cs_sy "Подожди."
    cs_narrator "Он снова перечитал обе строки."
    cs_sy "А ведь похоже."
    cs_narrator "Славя тоже посмотрела."
    cs_narrator "Потом улыбнулась."
    cs_sl "Точно! Здесь даже подписи разные."
    cs_narrator "Я кивнула."
    cs_ls "Значит, это не ошибка. Просто два разных этапа."
    cs_narrator "Семён посмотрел на меня."
    cs_sy "И как мы сами не заметили?"
    cs_narrator "Я задумалась."
    cs_ls "Возможно, вы слишком увлеклись тайными вечерними совещаниями."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он усмехнулся."
    if renpy.showing("sl"):
        show sl laugh pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя рассмеялась."
    cs_sl "Лена!"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Всё. Это была последняя."
    cs_narrator "Семён посмотрел на меня."
    cs_sy "Зафиксируем."
    cs_narrator "Я кивнула."
    cs_ls "Можешь составить протокол."
    cs_narrator "Славя ещё раз проверила список."
    cs_narrator "Потом аккуратно сложила бумаги."
    cs_sl "Спасибо. Теперь понятно, как всё распределить."
    cs_narrator "Я улыбнулась."
    cs_ls "Не за что."
    cs_narrator "Она посмотрела на меня."
    if cs_sl_friend_before_evening_choice >= 2:
        cs_sl "Знаешь, Лен, ты сегодня уже не первый раз выручаешь."
        cs_narrator "Я задумалась."
        cs_ls "Подозреваю, это опасная тенденция."
        if renpy.showing("sl"):
            show sl laugh pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Славя рассмеялась."
        cs_sl "Почему?"
        cs_ls "Ещё немного — и Ольга Дмитриевна начнёт воспринимать меня как полноценную рабочую единицу."
        cs_narrator "Семён усмехнулся."
        cs_sy "Поздно. Она уже воспринимает."
        cs_narrator "Я посмотрела на него."
        cs_ls "Тогда требую официального пересмотра условий трудоустройства."
        cs_narrator "Славя покачала головой."
        cs_sl "Ничего сложного завтра не планируется. Но если захочешь, можешь подойти после завтрака. Нужно будет помочь оформить объявление."
        cs_narrator "Я заинтересовалась."
        cs_ls "Оформить?"
        cs_narrator "Она кивнула."
        cs_sl "Да. Чтобы расписание было понятнее."
        cs_narrator "Я улыбнулась."
        cs_ls "С этим можно попробовать."
        cs_narrator "Славя обрадовалась."
        $ cs_sl_day4_notice_offer = True
        cs_sl "Тогда я спрошу тебя завтра, если будет время."
        cs_narrator "Я кивнула."
        cs_ls "Договорились. Только сначала посмотрю, как буду себя чувствовать."
        cs_narrator "Она перевела взгляд на повязку."
        cs_sl "Конечно. И никаких тяжёлых вещей."
        cs_narrator "Я вздохнула."
        cs_ls "Удивительно. Даже художественное оформление теперь проходит медицинское согласование."
        if renpy.showing("cs_semen"):
            show cs_semen smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Семён рассмеялся."
    else:
        if renpy.showing("sl"):
            show sl smile pioneer
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Славя улыбнулась."
        cs_sl "Всё равно спасибо. Очень помогла."
        cs_narrator "Я кивнула."
        cs_ls "Не за что."
        cs_narrator "Семён посмотрел на листок."
        cs_sy "Теперь хоть не придётся второй раз идти к Ольге Дмитриевне выяснять расписание."
        cs_narrator "Я улыбнулась."
        if not (cs_friend_se >= 2 and cs_se_day3_personal_talk):
            cs_ls "Видишь, а ты хотел меня прогнать. Потерял бы ценного консультанта."
        else:
            cs_ls "Вот видишь. У расследования обнаружилась практическая польза."
        if renpy.showing("cs_semen"):
            show cs_semen smile pioneer normal
            $ cs_presence_stage()
            with cs_sprite_change
        cs_narrator "Он усмехнулся."
        cs_sy "Даже боюсь представить размер твоего гонорара."
        cs_narrator "Я задумалась."
        cs_ls "Один нормальный ужин и право не таскать тяжёлые коробки."
        cs_narrator "Славя тихо рассмеялась."
    cs_narrator "Я посмотрела на часы."
    cs_th "О."
    cs_th "Кажется, моя пятиминутная прогулка уже начала превращаться в небольшое производственное совещание."
    cs_ls "Зайду в домик за книгой и вернусь в библиотеку."
    $ cs_sl_evening_destination_told_day3 = True
    cs_ls "Ладно, товарищи. Мне всё-таки пора."
    if renpy.showing("sl"):
        show sl smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Славя улыбнулась."
    cs_sl "Спасибо ещё раз."
    cs_ls "Пожалуйста."
    cs_narrator "Семён кивнул."
    if cs_sl_evening_destination_told_day3:
        cs_sy "Давай, Соколова. А то Женя начнёт думать, что тебя похитили."
    else:
        cs_sy "Давай, Соколова. У тебя ведь ещё дела."
    cs_narrator "Я задумалась."
    cs_ls "Ещё и эта версия появилась."
    if renpy.showing("cs_semen"):
        show cs_semen smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Он усмехнулся."
    cs_ls "Ладно. Не буду расширять расследование."
    cs_narrator "Я помахала им здоровой рукой."
    $ cs_director_scene("cs_camp_path_sunset")
    scene cs_camp_path_sunset
    $ cs_frame_focus([])
    with Dissolve(0.7)
    cs_narrator "И направилась к домику."
    $ cs_sl_evening_scene_done_day3 = True
    return
