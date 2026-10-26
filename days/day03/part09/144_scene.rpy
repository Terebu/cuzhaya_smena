# -*- coding: utf-8 -*-
label cs_day03_144:
    $ save_name = "Чужая смена — День 3: Две Лены, два взгляда"
    if cs_un_sketch_completed_day3:
        return
    if cs_se_sketch_spot_day3:
        $ cs_director_scene("bg ext_musclub_day")
        scene bg ext_musclub_day
        $ cs_frame_focus([])
        with Dissolve(0.7)
    else:
        $ cs_director_scene("cs_camp_path_day")
        scene cs_camp_path_day
        $ cs_frame_focus([])
        with Dissolve(0.7)
    play music cs_day_music_home fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.10,delay=1.0,channel="music")
    cs_narrator "Я вышла из домика с блокнотом и карандашом."
    cs_narrator "Воздух оставался тёплым, но солнце уже постепенно клонилось ниже."
    cs_narrator "На дорожках появились длинные тени."
    cs_narrator "Вот теперь рисовать гораздо приятнее."
    cs_narrator "Никакого полуденного света, который пытается уничтожить зрение."
    cs_narrator "Никакой спешки."
    cs_narrator "Просто хороший вечер."
    if cs_se_sketch_spot_day3:
        cs_narrator "Я вспомнила слова Семёна."
        cs_narrator "Скамейка за музыкальным клубом."
        cs_narrator "Хороший вид на дорожку."
        cs_narrator "Достаточно тени."
        cs_narrator "Я решила сначала проверить именно это место."
        cs_narrator "Свернула за клуб."
        cs_narrator "И почти сразу увидела знакомую фигуру."
        $ cs_frame_focus(["un"])
        with cs_sprite_change
        cs_narrator "Тихонова шла от клуба с альбомом. Заметив меня, она замедлила шаг возле деревьев."
        cs_narrator "Я улыбнулась."
        cs_ls "Привет."
        cs_narrator "Она повернулась."
        cs_un "Привет."
        cs_narrator "Я огляделась."
        cs_ls "Смотри, какое место нашлось."
        cs_narrator "Она посмотрела на скамейку."
        cs_narrator "Потом на дорожку."
        cs_un "Красиво."
        cs_narrator "Я улыбнулась."
        cs_ls "Семён подсказал. Говорил, что здесь почти никто не мешает."
        cs_narrator "Она чуть улыбнулась."
        cs_un "Хорошо придумал."
    else:
        $ cs_frame_focus(["un"])
        with cs_sprite_change
        cs_narrator "Тихонову я встретила возле клубов."
        cs_narrator "Она стояла под деревом и что-то рассматривала в своём альбоме."
        cs_narrator "Я подошла."
        cs_ls "Привет."
        cs_narrator "Она подняла голову."
        cs_un "Привет. Я как раз тебя ждала."
        cs_narrator "Я улыбнулась."
        cs_ls "Тогда давай искать подходящее место."
        cs_narrator "Она кивнула."
        cs_narrator "Мы немного прошлись вдоль дорожки."
        cs_narrator "Наконец нашли скамейку, откуда были видны площадь, деревья и часть дорожки."
        cs_un "Здесь хорошо."
        cs_narrator "Я огляделась."
        cs_ls "Согласна."
    cs_narrator "Мы устроились рядом."
    cs_narrator "Я положила блокнот на колени."
    cs_narrator "Тихонова раскрыла альбом."
    cs_narrator "Несколько секунд обе просто смотрели на окружающий лагерь."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_narrator "Интересно."
    cs_narrator "Один и тот же вид."
    cs_narrator "Одни и те же деревья."
    cs_narrator "Одна и та же дорожка."
    cs_narrator "Но, подозреваю, через полчаса у нас будут совершенно разные рисунки."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Тихонова первой нарушила молчание."
    cs_un "А ты с чего обычно начинаешь?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "С того, что пытаюсь понять, что именно хочу показать."
    cs_narrator "Она кивнула."
    cs_un "А потом?"
    cs_narrator "Я улыбнулась."
    cs_ls "Потом делаю несколько быстрых линий и надеюсь, что они хотя бы приблизительно окажутся там, где нужно."
    cs_narrator "Тихонова тихо рассмеялась."
    cs_un "А я иногда сразу начинаю рисовать дерево."
    cs_narrator "Я посмотрела на неё."
    cs_ls "И потом выясняется, что для остальных деревьев уже нет места?"
    cs_narrator "Она улыбнулась."
    cs_un "Да."
    cs_narrator "Я кивнула."
    cs_ls "Очень знакомо."
    cs_narrator "Мы принялись рисовать."
    cs_narrator "Я сначала наметила дорожку."
    cs_narrator "Потом расположение деревьев."
    cs_narrator "Небольшую часть площади."
    cs_narrator "Скамейку на переднем плане."
    cs_narrator "Тихонова работала осторожнее."
    cs_narrator "Она долго выбирала расположение объектов."
    cs_narrator "Иногда останавливалась."
    cs_narrator "Смотрела вдаль."
    cs_narrator "Затем снова проводила карандашом по бумаге."
    cs_narrator "Надо же."
    cs_narrator "Мы действительно совершенно по-разному подходим к одной задаче."
    cs_narrator "Я улыбнулась."
    cs_narrator "Прошло несколько минут."
    cs_narrator "Потом ещё немного."
    $ cs_pov_begin()
    with cs_sprite_leave
    cs_narrator "Вокруг продолжалась обычная лагерная жизнь."
    cs_narrator "Иногда мимо проходили пионеры."
    cs_narrator "Кто-то разговаривал вдалеке."
    cs_narrator "Но нам никто не мешал."
    $ cs_pov_end()
    with cs_sprite_change
    cs_narrator "Тихонова вдруг посмотрела на мой блокнот."
    cs_un "Можно?"
    cs_narrator "Я кивнула."
    cs_ls "Конечно."
    cs_narrator "Она осторожно наклонилась ближе."
    cs_narrator "Несколько секунд рассматривала рисунок."
    cs_un "У тебя всё такое… свободное."
    cs_narrator "Я приподняла бровь."
    cs_ls "В каком смысле?"
    cs_narrator "Она немного задумалась."
    cs_un "Ты не стараешься сразу прорисовать каждую деталь. Но уже понятно, какая получится картинка."
    cs_narrator "Я улыбнулась."
    cs_ls "Это потому, что я пока пытаюсь не испортить композицию."
    if renpy.showing("un"):
        show un smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она тихо рассмеялась."
    cs_narrator "Я посмотрела на её альбом."
    cs_ls "А у тебя, наоборот, очень аккуратные линии."
    if renpy.showing("un"):
        show un shy pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Тихонова немного смутилась."
    cs_un "Мне кажется, иногда слишком аккуратные."
    cs_narrator "Я задумалась."
    cs_ls "Возможно. Но в этом есть свой характер."
    cs_narrator "Она посмотрела на меня."
    cs_un "Правда?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Мне нравится, как ты замечаешь мелочи. Я бы, например, не стала сразу так подробно рисовать кору дерева."
    if renpy.showing("un"):
        show un smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Тихонова чуть улыбнулась."
    cs_un "А мне нравится."
    cs_ls "Вот и прекрасно. Значит, не надо от этого отказываться."
    cs_narrator "Она задумалась."
    cs_narrator "Потом снова посмотрела на свой рисунок."
    cs_un "А я думала, что должна рисовать быстрее."
    cs_narrator "Я покачала головой."
    cs_ls "Кому должна?"
    cs_narrator "Тихонова ненадолго замолчала."
    cs_narrator "Затем пожала плечами."
    cs_un "Не знаю."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Тогда предлагаю считать вопрос закрытым."
    if renpy.showing("un"):
        show un smile pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Она тихо рассмеялась."
    if renpy.showing("un"):
        show un normal pioneer
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Мы вернулись к работе."
    if cs_friend_un >= 3:
        cs_narrator "Через некоторое время Тихонова неожиданно закрыла текущую страницу."
        cs_narrator "Посмотрела на меня."
        cs_un "Лена."
        cs_narrator "Я подняла голову."
        cs_ls "Да?"
        cs_narrator "Она немного помолчала."
        cs_narrator "Потом открыла альбом ближе к началу."
        cs_narrator "Там был другой рисунок."
        cs_narrator "Не концерт."
        cs_narrator "Не лагерная дорожка."
        cs_narrator "А небольшой портрет."
        cs_narrator "Я осторожно посмотрела."
        cs_narrator "Девушка сидела возле окна, опустив взгляд на книгу."
        cs_narrator "Лицо было прорисовано особенно внимательно."
        cs_narrator "Но, судя по нескольким оставленным линиям, Тихонова много раз исправляла отдельные детали."
        cs_un "Я его раньше никому не показывала."
        cs_narrator "Я повернулась к ней."
        cs_ls "Почему?"
        cs_narrator "Она немного смутилась."
        cs_un "Не знаю. Мне казалось, что получилось плохо."
        cs_narrator "Я снова посмотрела на рисунок."
        cs_narrator "Нет."
        cs_narrator "Он определённо не был плохим."
        cs_narrator "Немного неровным."
        cs_narrator "Местами незавершённым."
        cs_narrator "Но очень внимательным."
        cs_narrator "Я улыбнулась."
        cs_ls "Мне нравится."
        cs_narrator "Она посмотрела на меня."
        cs_un "Правда?"
        cs_narrator "Я кивнула."
        cs_ls "Да. Особенно выражение лица."
        cs_narrator "Она немного помолчала."
        cs_un "Я долго его исправляла."
        cs_narrator "Я улыбнулась."
        cs_ls "Заметно. Но не в плохом смысле."
        cs_narrator "Посмотрела на неё."
        cs_ls "Ты ведь хотела показать не просто человека у окна?"
        cs_narrator "Она чуть удивилась."
        cs_un "Да."
        cs_narrator "Я снова посмотрела на портрет."
        cs_ls "И у тебя получилось."
        cs_narrator "Тихонова немного помолчала."
        cs_narrator "Потом улыбнулась."
        cs_un "Спасибо."
        cs_narrator "Я кивнула."
        cs_ls "Не за что."
        cs_narrator "Она ещё немного смотрела на рисунок."
        cs_narrator "Затем осторожно перевернула страницу."
        cs_narrator "Надо же."
        cs_narrator "Она сама решила показать мне то, что раньше скрывала."
        cs_narrator "Кажется, сегодня мы действительно стали немного ближе."
        $ cs_un_private_drawing_shown_day3 = True
    else:
        cs_narrator "Тихонова продолжила работать над своим наброском."
        cs_narrator "Иногда поглядывала на мой."
        cs_narrator "Мы обменялись ещё несколькими замечаниями о композиции и свете."
        cs_narrator "Но к личным рисункам она не возвращалась."
        cs_narrator "Я не стала расспрашивать."
        cs_narrator "В конце концов, знакомство не обязано превращаться в обмен всеми секретами за один вечер."
    cs_narrator "К тому времени солнце опустилось ниже."
    cs_narrator "Тени стали длиннее."
    cs_narrator "Тихонова осторожно закрыла альбом."
    cs_un "Мне понравилось."
    cs_narrator "Я улыбнулась."
    cs_ls "Мне тоже."
    cs_narrator "Она посмотрела на мой блокнот."
    cs_un "Может, ещё как-нибудь порисуем вместе?"
    cs_narrator "Я кивнула."
    cs_ls "С удовольствием."
    cs_narrator "Она чуть улыбнулась."
    cs_narrator "Мы поднялись со скамейки."
    cs_narrator "Попрощались."
    $ cs_actor_exit(["un"])
    with cs_sprite_leave
    cs_narrator "И разошлись по дорожкам."
    $ cs_un_sketch_completed_day3 = True
    cs_narrator "Ну вот."
    cs_narrator "Ещё одно совершенно обычное занятие."
    cs_narrator "И ещё один человек, которого я теперь знаю немного лучше."
    cs_narrator "Пожалуй, именно из таких мелочей и складывается то, что потом называют дружбой."
    label cs_check_day03_144_completed:
    pass
    return
