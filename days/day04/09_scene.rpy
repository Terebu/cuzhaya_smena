# -*- coding: utf-8 -*-
label cs_day04_09:
    $ save_name = "Чужая смена — День 4: Свидетельства прошлого"
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Женя заметила нас ещё до того, как мы подошли."
    cs_narrator "Она подняла голову от листа, поправила очки и посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Привет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Привет. Что читаешь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Список книг, которые нужно проверить."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Опасное занятие."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Почему?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Есть риск обнаружить, что кто-то до сих пор не вернул второй том."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Между прочим, это действительно проблема."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот видишь. Пошутила, а получился социальный комментарий."
    if cs_friend_mz >= 3:
        cs_narrator "Женя внимательно посмотрела на меня."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Ты сегодня какая-то странная."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Это очень широкое определение."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Не в обычном смысле."
        cs_narrator "От Жени шутками не отделаешься. Она уже заметила, что со мной что-то не так."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Есть новости. Но лучше поговорить не здесь."
        cs_narrator "Женя сразу стала серьёзнее."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Что-то случилось?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Да."
    else:
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Слушай, после обеда можно будет зайти к тебе по делу?"
        cs_narrator "Она нахмурилась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "По какому?"
        cs_narrator "Я оглянулась на шумную столовую."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Лучше без лишних свидетелей."
        cs_narrator "Женя несколько секунд смотрела на меня."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Хорошо. Только объяснишь нормально."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Обязательно."
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы взяли еду и устроились у окна."
    cs_narrator "Женя села напротив, Даша — рядом. Вокруг звенели ложки и обсуждали вечерние дела."
    cs_narrator "Между листами картона лежали снимки. Я смотрела на тарелку, стараясь не начать разговор раньше времени."
    cs_narrator "Обычная бумага, без свечения и таинственных знаков. Но эти снимки пугали сильнее любой истории о привидениях: их можно было взять в руки и проверить."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "И они от этого не исчезали."
    cs_narrator "Женя поглядывала на меня, но не торопила. Пообещала рассказать потом — значит, потом."
    if cs_mz_hug_allowed_day3 == True:
        cs_narrator "Женя вдруг негромко произнесла:"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Кстати, ты не забыла, о чём мы вчера говорили?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "О чём именно?"
        cs_narrator "Она посмотрела поверх очков."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Что необязательно устраивать торжественное приветствие каждый раз, когда мы встречаемся."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Помню. Сегодня у меня сокращённая программа."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Очень надеюсь."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Без оркестра, фанфар и массового шествия."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Уже неплохо."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Доедайте. В библиотеке поговорим."
    cs_narrator "Доели и вышли вслед за Женей."
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "У выхода нас встретил Семён."
    cs_narrator "Он заметил, что мы идём втроём, и сразу насторожился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Куда?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тайное общество любителей архивов. Вход исключительно по приглашениям."
    cs_narrator "Он оглядел нашу компанию."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ты ей расскажешь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Хорошо. Только аккуратно."
    cs_narrator "Женя повернулась к нам."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Вы вообще можете говорить нормально?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Иногда."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Очень редко."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка, прошу не подрывать мою репутацию перед библиотечным руководством."
    cs_narrator "Женя тяжело вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "У меня уже сложилось собственное мнение."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот и прекрасно."
    $ cs_director_scene("bg ext_library_day")
    scene bg ext_library_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы попрощались с Семёном и направились в библиотеку."
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_zhenya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Знакомый запах старой бумаги после сырости убежища показался домашним."
    cs_narrator "Солнечный свет проникал через окна, освещая книжные полки. На столе лежал раскрытый журнал, рядом стояли чернильница и несколько карандашей."
    cs_narrator "Ещё недавно библиотека была для меня локацией из игры. Теперь я знала, за каким столом удобно читать и с кем можно поспорить о книге. Или просто помолчать."
    cs_narrator "Женя положила ключи на стол и повернулась к нам."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("arms_crossed pioneer normal".split()):
        show cs_zhenya arms_crossed pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Рассказывай."
    stop music fadeout 2.0
    cs_narrator "Я достала фотографию из папки за 1971 год."
    cs_narrator "Потом список."
    cs_narrator "Аккуратно разложила их на столе."
    cs_narrator "Женя наклонилась."
    cs_narrator "Сначала смотрела совершенно спокойно."
    cs_narrator "Потом чуть придвинула фотографию."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Славя."
    cs_narrator "Она перевела палец."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Лена."
    cs_narrator "Потом задержала палец возле одной из девушек. Сняла очки, протёрла и посмотрела снова."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Это я."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Очень похожа на тебя."
    cs_narrator "Она подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Соколова."
    cs_narrator "Я замолчала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("glasses_touch pioneer normal".split()):
        show cs_zhenya glasses_touch pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Я знаю, как выгляжу."
    cs_narrator "Но Женя уже смотрела на дату."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "1971 год."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она села."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "В семьдесят первом меня ещё на свете не было."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Женя держала фотографию перед собой."
    cs_narrator "Потом осторожно положила её на стол."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Объясни."
    cs_narrator "Мы с Дашей сели напротив."
    cs_narrator "Я рассказала, где нашла снимки и что было в архивных папках. Затем — о снах Ольги Дмитриевны и о том, что она не помнит, сколько раз бывала в лагере. О Виоле тоже. Старалась держаться фактов."
    cs_narrator "Женя слушала внимательно."
    cs_narrator "Ни разу не перебила."
    cs_narrator "Когда я закончила, она некоторое время рассматривала список."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Значит, и Ольга Дмитриевна, и Виола иногда помнят события, которых не было?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Они так говорят."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "А ты думаешь, что эти события происходили на самом деле?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Возможно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Но пока я не хочу делать вывод, который ничем не могу подтвердить."
    cs_narrator "Женя снова перевела взгляд на снимок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "А это?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Это уже предмет. Его можно изучить, сравнить с другими фотографиями, проверить дату."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Есть ещё что-нибудь?"
    cs_narrator "Мы с Дашей переглянулись."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Я вспомнила тёмную лестницу."
    cs_narrator "И внезапно почувствовала, как внутри снова всё неприятно сжалось."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Там кто-то говорил со мной."
    cs_narrator "Женя замерла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Кто?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не знаю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Что сказал?"
    cs_narrator "Я повторила почти шёпотом:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "«Ты не должна была проснуться здесь»."
    cs_narrator "Женя перестала двигаться."
    cs_narrator "Несколько секунд смотрела на меня."
    cs_narrator "Потом тихо спросила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Женский голос?"
    cs_narrator "Я замерла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она чуть подалась вперёд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Молодой?"
    cs_narrator "Я почувствовала, как по спине пробежал холод."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Женя отвела взгляд."
    cs_narrator "На лице появилось странное выражение."
    cs_narrator "Словно она пыталась вспомнить что-то очень далёкое."
    cs_narrator "Потом тихо произнесла:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_zhenya") and renpy.get_attributes("cs_zhenya") != tuple("thoughtful pioneer normal".split()):
        show cs_zhenya thoughtful pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_mz "Кажется, я его слышала."
    cs_narrator "В библиотеке стало тихо."
    if not cs_d4_choice_09_done:
        if cs_d4_mz_friend_before_choice is None:
            $ cs_d4_mz_friend_before_choice = cs_friend_mz
        menu:
            "Не торопить Женю и предложить ей самой рассказать, что помнит":
                $ cs_friend_mz += 1
                $ cs_d4_mz_gentle_dream_talk = True
                cs_narrator "Я посмотрела на неё."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Женя, если тяжело, можешь не рассказывать прямо сейчас."
                cs_narrator "Она подняла глаза."
                cs_narrator "Несколько секунд смотрела на меня."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mz "Нет. Я хочу понять."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Тогда давай спокойно. Что помнишь — то и говори. Остальное не нужно придумывать."
                cs_narrator "Она немного выдохнула."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mz "Хорошо."
            "Спросить, какие именно слова Женя слышала":
                $ cs_d4_mz_direct_dream_question = True
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Что именно ты слышала?"
                cs_narrator "Женя нахмурилась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mz "Подожди. Я пытаюсь вспомнить."
                cs_narrator "Я откинулась обратно."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Хорошо. Не тороплю."
                cs_narrator "Она закрыла глаза."
        $ cs_d4_choice_09_done = True
    cs_narrator "Помолчав, Женя заговорила."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Мне иногда снится коридор."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Какой?"
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Не знаю. Темно. Стены почти не видно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "И кто-то говорит."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что именно?"
    cs_narrator "Она всё сильнее хмурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Сегодня ночью я слышала…"
    cs_narrator "Женя умолкла и открыла глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "«Она пришла раньше»."
    cs_narrator "Я почувствовала неприятный холодок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Раньше?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Ты знаешь, кто «она»?"
    cs_narrator "Женя покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Нет."
    cs_narrator "Я перевела взгляд со снимка на Женю."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А ещё что-нибудь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Что-то про четвёртый день. Чей — не знаю."
    cs_narrator "Мы с Дашей переглянулись."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сегодня четвёртый. У нас с Дашей."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Я знаю."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Она пришла раньше."
    cs_narrator "Четвёртый день. Почему она слышала это до того, как мы рассказали о находках? И почему снова речь о времени?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тебе страшно?"
    cs_narrator "Женя не ответила сразу."
    cs_narrator "Потом медленно кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мне тоже."
    cs_narrator "Я слабо улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Просто я обычно выражаю страх через сомнительные шутки и ещё более сомнительные решения."
    cs_narrator "Даша негромко добавила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Особенно через решения."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спасибо, Даша. Очень поддержала."
    cs_narrator "Женя неожиданно тихо рассмеялась."
    cs_narrator "И напряжение стало чуть слабее."
    if cs_d4_mz_friend_before_choice >= 3 and cs_mz_hug_allowed_day3 == True:
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Можно?"
        cs_narrator "Она поняла."
        cs_narrator "Несколько секунд смотрела на меня."
        cs_narrator "Потом сама подошла ближе."
        cs_narrator "Я осторожно обняла её."
        $ cs_d4_mz_hug_09 = True
        cs_narrator "Не слишком крепко, стараясь не задеть локоть."
        cs_narrator "Женя ответила на объятие. Ненадолго, но теперь сама сделала шаг навстречу. Вчера разрешила — сегодня захотела."
    else:
        cs_narrator "Я не стала приближаться."
        cs_narrator "Вместо этого подвинула к ней стакан воды, стоявший на краю стола."
        cs_narrator "Женя посмотрела на него."
        cs_narrator "Потом на меня."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mz "Спасибо."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Не за что."
    cs_narrator "Женя села, посмотрела на фотографию и спросила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mz "И что теперь делать?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Для начала записать всё, что ты помнишь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Даже если какие-то слова кажутся бессмысленными. Не нужно пытаться сразу объяснить их."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И не подгонять воспоминания под нашу версию."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Женя достала лист. Подержала карандаш над бумагой и начала писать."
    cs_narrator "Я смотрела на знакомую девушку в очках на снимке 1971 года. Кто-то был здесь раньше нас. Может, не один раз."
    cs_narrator "Вслух я этого не сказала. Рано."
    $ cs_d4_mz_dream_record_written = True
    return
