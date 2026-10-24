# -*- coding: utf-8 -*-
label cs_day03_124:
    $ save_name = "Чужая смена — День 3: Одна задержавшаяся девушка"
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Я как раз собиралась допить чай, когда услышала знакомый голос."
    $ cs_frame_focus(["cs_zhenya", "cs_darya"])
    with cs_sprite_change
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_da "Можно к вам?"
    cs_narrator "Я подняла голову."
    cs_narrator "Даша стояла рядом с нашим столом."
    cs_narrator "С подносом."
    cs_narrator "И слегка виноватой улыбкой."
    cs_ls "Конечно."
    cs_narrator "Женя кивнула на свободный стул."
    cs_mz "Садись."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Спасибо."
    cs_narrator "Она поставила поднос."
    cs_narrator "Аккуратно устроилась рядом."
    if cs_sl_poster_collected_day3 and cs_day03_poster_location in ("darya_folder", "dining_chair"):
        $ cs_day03_poster_location = "dining_chair"
        cs_narrator "Папку с вчерашним плакатом она положила на свободный край стула, подальше от еды."
        cs_narrator "Я заметила это."
        cs_th "Молодец."
        cs_th "Кажется, сохранность художественных произведений теперь находится под надёжным контролем."
    cs_da "Извините, что задержалась."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Ольга Дмитриевна?"
    cs_narrator "Она удивилась."
    cs_da "Ты видела?"
    cs_narrator "Я покачала головой."
    cs_ls "Нет. Просто предположила."
    cs_narrator "Дарья кивнула."
    cs_da "Да. Она спросила, как твоя рука после перевязки."
    cs_narrator "Я посмотрела на Женю."
    cs_ls "Всё. Теперь мой локоть официально стал объектом межведомственного взаимодействия."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_narrator "Дарья тоже улыбнулась."
    cs_da "Ещё просила передать, чтобы ты сегодня не устраивала пробежек."
    cs_narrator "Я кивнула."
    cs_ls "Передано. Принято к исполнению."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "Даже спорить не будешь?"
    cs_ls "Нет."
    cs_narrator "Она замолчала."
    cs_narrator "Посмотрела на Женю."
    cs_narrator "Женя — на неё."
    cs_narrator "Обе снова повернулись ко мне."
    cs_narrator "Я подняла бровь."
    cs_ls "Что?"
    cs_da "Ничего. Просто ожидала немного другой реакции."
    cs_narrator "Я задумалась."
    cs_ls "Могу для порядка написать жалобу на ограничение спортивных свобод."
    cs_narrator "Женя тихо рассмеялась."
    cs_da "Не нужно."
    cs_narrator "Я кивнула."
    cs_ls "Тогда считаем вопрос закрытым."
    cs_narrator "Дарья начала есть."
    cs_narrator "Мы некоторое время сидели втроём."
    cs_narrator "Женя читала надпись на обложке своей книги."
    cs_narrator "Я смотрела в окно."
    cs_narrator "Дарья спокойно обедала."
    cs_narrator "И всем, кажется, было хорошо."
    cs_narrator "Спустя некоторое время она повернулась ко мне."
    cs_da "А ты почему не стала ждать меня с едой?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Потому что проголодалась."
    cs_narrator "Дарья моргнула."
    cs_narrator "Потом рассмеялась."
    cs_da "И всё?"
    cs_narrator "Я кивнула."
    cs_ls "Ну да."
    cs_da "Даже никаких обвинений в предательстве?"
    cs_narrator "Я задумалась."
    cs_ls "Пока нет."
    cs_narrator "Она улыбнулась."
    cs_da "«Пока»?"
    cs_narrator "Я посмотрела на Женю."
    cs_narrator "Та уже наблюдала за нами поверх очков."
    cs_narrator "Я совершенно спокойно ответила:"
    cs_ls "Сегодня обед проходит в рамках культурной программы."
    if renpy.showing("cs_zhenya"):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Женя усмехнулась."
    cs_mz "И неплохо проходит."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Поняла."
    cs_narrator "Потом посмотрела на Женю."
    cs_da "Она весь обед такая?"
    cs_mz "В основном."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Прошу не обсуждать меня как отсутствующего человека. Я тут вообще-то сижу."
    cs_narrator "Женя посмотрела на меня."
    cs_mz "Тогда не подслушивай."
    cs_narrator "Я замолчала."
    cs_narrator "Потом медленно повернулась к Дарье."
    cs_ls "Даша. Библиотекарь вышла на новый уровень."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_narrator "Женя едва заметно улыбнулась."
    cs_th "Ну вот."
    cs_th "Теперь уже точно всё нормально."
    return
