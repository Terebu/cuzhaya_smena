# -*- coding: utf-8 -*-
label cs_day03_103:
    $ save_name = "Чужая смена — День 3: Медицинская комиссия завершила работу"
    label cs_check_day03_103_outside:
    play music "sound/music/my_daily_life.ogg" fadein 2.0
    $ renpy.music.set_volume(0.15,delay=1.0,channel="music")
    cs_narrator "Мы спустились с крыльца."
    cs_narrator "Я посмотрела на свежую повязку."
    cs_narrator "Потом в сторону двери."
    cs_th "Интересное утро."
    cs_th "Оказывается, вчерашний концерт имеет последствия не только в виде хороших воспоминаний."
    cs_th "Некоторые продолжают расплачиваться пальцами."
    cs_narrator "Дарья посмотрела на меня."
    cs_da "О чём задумалась?"
    cs_narrator "Я улыбнулась."
    cs_ls "О том, что у каждого творческого занятия свои профессиональные травмы."
    cs_narrator "Она приподняла бровь."
    cs_da "Например?"
    cs_narrator "Я подняла здоровую руку."
    cs_ls "У музыкантов страдают пальцы."
    cs_narrator "Посмотрела на повязку."
    cs_ls "У художников иногда страдает здравый смысл."
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "А локоть тут при чём?"
    cs_narrator "Я задумалась."
    cs_ls "Это уже самостоятельное направление исследований."
    cs_narrator "Она покачала головой."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    show cs_darya shy_smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы пошли по дорожке."
    cs_narrator "Несколько минут молчали."
    $ cs_pov_begin()
    with cs_sprite_leave
    label cs_check_day03_103_reflection:
    cs_narrator "Я смотрела на деревья."
    cs_narrator "На знакомые корпуса."
    cs_narrator "На пионеров, которые спешили по своим делам."
    cs_th "За эти два дня я успела узнать здесь довольно много людей."
    cs_th "Но, кажется, только теперь начинаю по-настоящему с ними знакомиться."
    cs_th "Раньше мне казалось, что я знаю их заранее."
    cs_th "Алиса — дерзкая гитаристка."
    cs_th "Женя — строгая библиотекарша."
    cs_th "Славя — образцовая помощница вожатой."
    cs_th "Виола — медсестра с подозрительно хорошим чувством юмора."
    cs_th "Удобные короткие описания."
    cs_th "Только сами люди, как выяснилось, значительно сложнее."
    $ cs_pov_end()
    with cs_sprite_change
    label cs_check_day03_103_dialogue:
    cs_narrator "Я немного улыбнулась."
    cs_da "Лен."
    cs_narrator "Я повернулась."
    cs_ls "М?"
    cs_da "Ты сегодня действительно как-то спокойнее."
    cs_narrator "Я задумалась."
    cs_ls "Неужели?"
    cs_narrator "Она кивнула."
    cs_da "Да. Даже с Алисой почти не спорила."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Даша, мне начинает казаться, что ты очень сильно переоцениваешь мою потребность конфликтовать."
    cs_narrator "Она улыбнулась."
    cs_da "А я ничего не говорила про конфликты."
    cs_narrator "Я остановилась."
    cs_narrator "Посмотрела на неё."
    cs_narrator "Пауза."
    cs_ls "Так. Поймала."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я тоже."
    cs_narrator "Потом осторожно поправила рукав."
    cs_ls "Знаешь, кажется, я просто привыкла."
    cs_da "К чему?"
    cs_narrator "Я посмотрела на лагерь."
    cs_ls "К тому, что здесь можно жить обычной жизнью. Несмотря на всё странное."
    cs_narrator "Она немного помолчала."
    cs_da "Понимаю."
    cs_narrator "Я кивнула."
    cs_ls "Мы всё ещё не знаем, как вернуться домой. И дорога по-прежнему никуда нас не выпускает."
    cs_narrator "Посмотрела на неё."
    cs_ls "Но это не значит, что каждую минуту нужно вести себя так, будто мир сейчас закончится."
    if renpy.showing("cs_darya"):
        show cs_darya shy_smile pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья улыбнулась."
    cs_da "Согласна."
    cs_narrator "Я выпрямилась."
    cs_ls "Вот и прекрасно. Тогда предлагаю продолжить знакомство с советским образом жизни."
    cs_da "И куда теперь?"
    cs_narrator "Я посмотрела на часы."
    cs_narrator "Потом в сторону домиков."
    cs_ls "К Ольге Дмитриевне. Предложим помощь."
    cs_narrator "Дарья остановилась."
    cs_narrator "Посмотрела на меня."
    cs_da "Ты серьёзно?"
    cs_narrator "Я кивнула."
    cs_ls "Да."
    cs_narrator "Она улыбнулась."
    cs_da "Даже добровольно?"
    cs_narrator "Я приложила здоровую ладонь к груди."
    cs_ls "Почему сегодня все так удивляются моему трудолюбию?"
    if renpy.showing("cs_darya"):
        show cs_darya amused pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_narrator "Дарья рассмеялась."
    cs_da "Потому что ты обычно сначала шутишь, а потом работаешь."
    cs_narrator "Я задумалась."
    cs_ls "Тогда сегодня попробуем наоборот."
    cs_narrator "Она улыбнулась."
    cs_da "Хороший план."
    cs_narrator "Мы свернули к домикам."
    cs_th "Что ж."
    cs_th "Медицинская часть дня завершена."
    cs_th "Пациент выпущен на свободу."
    cs_th "Общественная опасность пока не установлена."
    cs_narrator "Я улыбнулась."
    cs_th "Соколова, третий день."
    cs_th "Постарайся хотя бы сегодня ничего себе не сломать."
    $ cs_day03_medpoint_revision_done = True
    return
