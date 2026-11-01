# -*- coding: utf-8 -*-
label cs_day04_10:
    $ save_name = "Чужая смена — День 4: Тишина библиотеки"
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    play music "sound/music/a_promise_from_distant_days.ogg" fadein 3.0
    stop music fadeout 1.5
    cs_narrator "Когда Женя закончила записывать воспоминания, она некоторое время рассматривала лист."
    cs_narrator "На листе осталось несколько фраз — без имён, подробностей и ответов."
    cs_narrator "Она медленно положила карандаш."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("normal pioneer normal".split()):
        show cs_zhenya normal pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Пока больше ничего не помню."
    cs_narrator "Я посмотрела на записи."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ничего страшного. Главное, что теперь они не потеряются."
    cs_narrator "Женя кивнула."
    cs_narrator "Осторожно придвинула лист к краю стола, где лежали остальные бумаги."
    cs_narrator "Даша сидела рядом, рассматривая найденный список."
    cs_narrator "Я наблюдала за ними и пыталась решить, что делать дальше."
    cs_narrator "Утром я отправилась в старый лагерь, надеясь найти хоть какое-нибудь объяснение происходящему."
    cs_narrator "Теперь у нас было ещё больше вопросов."
    cs_narrator "Кто изображён на фотографиях?"
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Почему одни и те же имена встречаются в документах разных лет?"
    cs_narrator "Кто разговаривал со мной в убежище?"
    cs_narrator "И самое неприятное — почему этот кто-то знал, что я здесь проснулась?"
    cs_narrator "Я потёрла переносицу."
    cs_narrator "Хватит. Ещё немного — начну искать тайные послания на обоях."
    cs_narrator "Я подняла голову."
    cs_narrator "Посмотрела на книжные полки."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "А потом на Женю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Слушай."
    cs_narrator "Она повернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Что?"
    cs_narrator "Я показала на полки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты вчера говорила, что подберёшь мне следующую книгу. Если предложение ещё в силе, я бы попробовала."
    cs_narrator "Женя несколько секунд смотрела на меня."
    cs_narrator "Потом медленно сняла очки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Соколова."
    cs_narrator "Я подняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "М?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Мы только что обсуждали фотографии, которых не должно существовать. Неизвестный голос. Странные сны."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Она посмотрела на книжные полки."
    cs_narrator "Потом снова на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "И ты хочешь читать?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Очень."
    cs_narrator "Даша закрыла лицо ладонью."
    cs_narrator "Женя неожиданно рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Ты невозможная."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мистика мистикой, а библиотека должна работать."
    cs_narrator "Она покачала головой."
    cs_narrator "Но поднялась."
    cs_narrator "Прошла между стеллажами, несколько секунд изучала корешки книг и сняла с верхней полки небольшой том."
    cs_narrator "Потом вернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Попробуй это."
    cs_narrator "Я взяла книгу."
    cs_narrator "На обложке значилось: Иван Тургенев, «Ася»."
    cs_narrator "Обложка была немного потёртой, но страницы сохранились хорошо."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Почему именно эту?"
    cs_narrator "Женя чуть улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("explaining pioneer normal".split()):
        show cs_zhenya explaining pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Мне интересно, что ты скажешь о героях."
    cs_narrator "Я подняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ещё один эксперимент над читателем."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Можешь отказаться."
    cs_narrator "Я прижала книгу к груди."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ни за что. Теперь мне самой интересно."
    cs_narrator "Она усмехнулась."
    cs_narrator "Прежде чем открыть книгу, я вспомнила о документах."
    cs_narrator "Фотография 1971 года и список всё ещё лежали на столе."
    cs_narrator "Я осторожно придвинула их к Жене."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И ещё кое-что."
    cs_narrator "Она посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Можно оставить это у тебя на хранение?"
    cs_narrator "Женя перевела взгляд на снимки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Почему?"
    cs_narrator "Я немного подумала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Потому что у нас в домике они рано или поздно окажутся под чьей-нибудь кружкой. Причём, скорее всего, под моей."
    cs_narrator "Женя улыбнулась."
    cs_narrator "Но затем стала серьёзнее."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Ты понимаешь, что это могут быть важные документы?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно поэтому и предлагаю оставить их здесь."
    cs_narrator "Я показала на картотеку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "У тебя хотя бы имеется место, где бумаги не исчезают в неизвестном направлении."
    cs_narrator "Женя посмотрела на фотографии."
    cs_narrator "Потом на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Хорошо."
    cs_narrator "Она достала плотную папку."
    cs_narrator "Осторожно поместила внутрь снимок и список, разделив их листом бумаги."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Но это не значит, что теперь они мои."
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Конечно. Это значит, что они в безопасности."
    cs_narrator "Она закрыла папку."
    cs_narrator "Убрала в ящик."
    cs_narrator "Повернула ключ."
    cs_narrator "Я почувствовала неожиданное облегчение."
    cs_narrator "Хотя бы один вопрос на сегодня удалось решить."
    $ cs_d4_mz_has_1971_photo = True
    $ cs_d4_photo1971_location = cs_d4_roster_location = "library_locked_drawer"
    cs_narrator "Я устроилась за свободным столом у окна и открыла книгу."
    cs_narrator "Даша выбрала что-то с соседней полки и села неподалёку."
    cs_narrator "Женя вернулась к своим записям."
    cs_narrator "В библиотеке снова стало тихо. Я всё ещё прислушивалась, как в убежище, но слышала только страницы и скрип Жениного стула. Постепенно отпустило."
    cs_narrator "Я перевернула страницу."
    cs_narrator "Первые несколько минут чтение давалось трудно."
    cs_narrator "Мысли постоянно возвращались к фотографиям."
    cs_narrator "Стоило встретить описание незнакомого места, как память услужливо подсовывала заброшенный коридор."
    cs_narrator "Стоило прочитать чью-нибудь реплику, и я вспоминала голос из темноты."
    cs_narrator "Я раздражённо выдохнула."
    cs_narrator "Соколова, это Тургенев. Не инструкция по выходу из временной петли."
    cs_narrator "Я заставила себя сосредоточиться."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Постепенно строки начали складываться в образы."
    cs_narrator "Персонажи обрели голоса."
    cs_narrator "Описания перестали казаться просто словами на бумаге."
    cs_narrator "Я наконец увлеклась книгой. На несколько страниц даже забыла, где нахожусь. Как дома, когда чтение ещё не требовало таких усилий."
    cs_narrator "Со стороны рабочего стола раздался тихий стук."
    cs_narrator "Я подняла голову."
    cs_narrator "Женя поставила передо мной чашку чая."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Держи."
    cs_narrator "Я удивилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спасибо."
    cs_narrator "Она показала на книгу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Только не пролей."
    cs_narrator "Я прищурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Неужели ты мне настолько не доверяешь?"
    cs_narrator "Она посмотрела на мой локоть."
    cs_narrator "Потом на чашку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("shrug pioneer normal".split()):
        show cs_zhenya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Я просто знаю, на что ты способна."
    cs_narrator "Я задумалась."
    cs_narrator "Возразить оказалось нечем."
    cs_narrator "Молча подвинула чашку подальше от книги."
    cs_narrator "Женя удовлетворённо кивнула."
    cs_narrator "Вернулась к столу."
    cs_narrator "Я улыбнулась."
    cs_narrator "Вот за что люблю библиотеку."
    cs_narrator "Здесь даже забота о человеке выражается через заботу о книгах."
    cs_narrator "Через некоторое время Даша отложила свой том."
    cs_narrator "Она потянулась и посмотрела в окно."
    $ cs_director_scene("cs_library_interior_evening")
    scene cs_library_interior_evening
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Свет постепенно менялся. Солнечные лучи уже падали под другим углом, освещая дальние стеллажи."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Лен."
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "М?"
    cs_narrator "Она слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты сегодня впервые за долгое время сидишь спокойно."
    cs_narrator "Я посмотрела на себя."
    cs_narrator "Потом на книгу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Значит, эксперимент удался."
    cs_narrator "Даша рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Какой?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Проверка гипотезы, что я способна хотя бы час не искать приключений."
    cs_narrator "Женя, услышав наш разговор, подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Результаты пока обнадёживают."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Прошу занести в личное дело."
    cs_narrator "Она покачала головой."
    cs_narrator "И вернулась к журналу."
    cs_narrator "Мы ещё немного почитали."
    cs_narrator "Потом Даша предложила обсудить музыку."
    cs_narrator "Оказалось, она успела вспомнить несколько композиций, которые играла раньше, и теперь размышляла, можно ли подобрать что-нибудь похожее на лагерном пианино."
    cs_narrator "Я слушала и улыбалась. Для человека, который «давно не занимался», Даша подозрительно увлечённо объясняла, как нужно играть."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Даш."
    cs_narrator "Она остановилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты сейчас минут пять объясняла мне, как правильно расставлять акценты."
    cs_narrator "Она чуть покраснела."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И?"
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ничего. Просто приятно наблюдать за человеком, который совершенно не умеет играть на пианино."
    cs_narrator "Даша рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Лена!"
    cs_narrator "Я подняла руки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Всё. Молчу."
    cs_narrator "Женя посмотрела на нас поверх очков."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Очень надеюсь."
    cs_narrator "И я действительно замолчала."
    cs_narrator "По крайней мере, на несколько минут."
    cs_narrator "Ближе к вечеру я отложила книгу."
    cs_narrator "Свет за окнами стал золотистым."
    cs_narrator "Где-то далеко раздавались голоса пионеров, возвращавшихся с занятий."
    cs_narrator "Я посмотрела на часы."
    cs_narrator "День почти закончился."
    cs_narrator "А мы так и не узнали, что означают фотографии."
    cs_narrator "Но, пожалуй, это нормально."
    cs_narrator "Не каждую загадку можно решить за один день."
    cs_narrator "И не каждый вопрос обязательно требует немедленного ответа."
    cs_narrator "Я перевела взгляд на Дашу."
    cs_narrator "Она сидела у окна, рассеянно перелистывая книгу."
    cs_narrator "Заметила мой взгляд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ничего. Просто хорошо, что мы сегодня вместе."
    cs_narrator "Она немного помолчала."
    cs_narrator "Потом улыбнулась в ответ."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Мне тоже."
    cs_narrator "Над лагерем прозвучал горн."
    play sound sfx_dinner_horn_processed
    cs_narrator "Я подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Уже?"
    cs_narrator "Женя посмотрела на часы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Ужин."
    cs_narrator "Я медленно закрыла книгу."
    cs_narrator "Вот ведь."
    cs_narrator "Весь день пытались разобраться со временем."
    cs_narrator "И опять совершенно незаметно его потеряли."
    cs_narrator "Я поднялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Предлагаю временно отложить исследование реальности."
    cs_narrator "Даша улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ради ужина?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "У каждого учёного должны быть приоритеты."
    cs_narrator "Женя усмехнулась."
    cs_narrator "Проверила, что ящик с папкой заперт."
    cs_narrator "И мы начали собираться."
    $ cs_d4_new_book_location = "library_reading_table"
    return
