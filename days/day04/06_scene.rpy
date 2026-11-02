# -*- coding: utf-8 -*-
label cs_day04_06:
    $ save_name = "Чужая смена — День 4: У Ольги Дмитриевны"
    $ cs_director_scene("bg ext_house_of_mt_day")
    scene bg ext_house_of_mt_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    stop music fadeout 1.5
    cs_narrator "У домика вожатой мы остановились."
    cs_narrator "В приоткрытом окне шелестела бумага. Ольга Дмитриевна уже работала."
    cs_narrator "Сколько бумаги нужно одному лагерю, чтобы просто провести лето?"
    cs_narrator "А главное — как она вообще умудряется за всем следить?"
    cs_narrator "Я посмотрела на дверь."
    cs_narrator "Потом на Дашу и Семёна."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Так. Если начну говорить слишком много — остановите."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Хорошо."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Это может понадобиться довольно быстро."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спасибо за веру в меня, Сёмочка."
    cs_narrator "Я постучала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Войдите."
    $ cs_director_scene("bg int_house_of_mt_day")
    scene bg int_house_of_mt_day
    $ cs_d4_scene_cast = ['mt', 'cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы вошли."
    cs_narrator "Вожатая оторвалась от бумаг. Рядом с ней лежала раскрытая тетрадь."
    cs_narrator "Она оглядела нас троих и стала серьёзной."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Что случилось?"
    cs_narrator "Я закрыла дверь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нам нужно кое-что вам показать."
    cs_narrator "Вожатая отложила ручку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Надеюсь, на этот раз без приключений?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "С приключениями, боюсь, уже ничего не поделаешь. Они случились."
    cs_narrator "Семён вздохнул. Вожатая посмотрела на него, потом на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Садитесь."
    cs_narrator "Даша встала рядом со мной. Семён придвинул к столу свободный стул."
    cs_narrator "Я достала верхнюю фотографию."
    stop music fadeout 2.0
    cs_narrator "Осторожно положила её перед вожатой."
    cs_narrator "Сначала Ольга Дмитриевна рассматривала снимок совершенно спокойно."
    cs_narrator "Затем её взгляд изменился."
    cs_narrator "Едва заметно."
    cs_narrator "Она чуть наклонила голову и придвинула фотографию ближе."
    cs_narrator "Рисуя портреты, я привыкла замечать мелочи: напряжённые губы, движение бровей, перемену взгляда."
    cs_narrator "Поэтому я сразу обратила внимание."
    cs_narrator "Вожатая узнала что-то на фотографии."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Откуда это?"
    cs_narrator "Я посмотрела на Дашу."
    cs_narrator "Она тоже насторожилась."
    cs_narrator "Не «кто здесь изображён»."
    cs_narrator "Не «что за фотография»."
    cs_narrator "Именно «откуда»."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Из старого корпуса."
    cs_narrator "Ольга Дмитриевна резко подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Вы ходили туда?!"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я."
    cs_narrator "Даша добавила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Я нашла её уже там."
    cs_narrator "Вожатая закрыла глаза и устало провела ладонью по лицу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Лена…"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Знаю. Одна идти не должна была."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Это аварийное здание! Там может обвалиться перекрытие, провалиться пол…"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Теперь я знаю это не только теоретически."
    cs_narrator "Под её строгим взглядом шутить расхотелось."
    cs_narrator "Ольга Дмитриевна снова перевела взгляд на фотографию."
    cs_narrator "Я положила рядом второй снимок и список из архивной папки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А это лежало в документах за 1971 год."
    cs_narrator "Она замерла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "За какой?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Семьдесят первый."
    cs_narrator "Семён наклонился вперёд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Здесь наши имена."
    cs_narrator "Вожатая читала список: Славя, Женя, Тихонова, Семён… Всё сильнее сжимала лист, потом положила на стол."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Где именно вы это нашли?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "В подземной части корпуса."
    cs_narrator "Она посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "В убежище?"
    cs_narrator "Я замерла. Убежище."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вы знаете про убежище?"
    cs_narrator "Вожатая отвела взгляд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "О нём давно известно. Ничего удивительного."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тогда, возможно, вы знаете, почему там работает электричество?"
    cs_narrator "Она не ответила."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И почему в помещении, которое должно быть заброшено, кто-то регулярно бывает?"
    cs_narrator "Ольга Дмитриевна молча смотрела то на стол, то на Семёна, то на снимок."
    cs_narrator "Осторожнее, Соколова. Мы пришли за ответами, а не загонять человека в угол."
    if not cs_d4_choice_06_done:
        menu:
            "Спокойно попросить Ольгу Дмитриевну помочь разобраться":
                $ cs_d4_od_trust_approach = True
                cs_narrator "Я немного придвинулась к столу."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Ольга Дмитриевна, мы не пытаемся вас ни в чём обвинить."
                cs_narrator "Она подняла глаза."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Просто сегодня я испугалась сильнее, чем готова признать. А теперь держу в руках фотографии, которые совершенно не могу объяснить."
                cs_narrator "Я показала на список."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Мы не знаем, что это означает. И не знаем, безопасно ли вообще находиться в старом корпусе."
                cs_narrator "Даша добавила:"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "Поэтому и пришли к вам. Может быть, вы хотя бы знаете, с чего начать?"
                cs_narrator "Ольга Дмитриевна несколько секунд молчала."
                cs_narrator "Затем глубоко выдохнула."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mt "Ладно. Покажите всё ещё раз."
                cs_narrator "Я осторожно подвинула снимки ближе."
            "Прямо указать, что Ольга Дмитриевна что-то скрывает":
                $ cs_d4_od_direct_question = True
                cs_narrator "Я посмотрела ей прямо в глаза."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Вы сразу узнали убежище."
                cs_narrator "Ольга Дмитриевна нахмурилась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mt "И что?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "И почти не удивились самим документам. Зато удивились году."
                cs_narrator "Она положила лист на стол."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mt "Лена, ты делаешь слишком много выводов из моего выражения лица."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Возможно. Но лица — моя работа. А любопытство, к сожалению, моё самое дорогое хобби."
                cs_narrator "Семён негромко кашлянул."
                cs_narrator "Я не стала продолжать."
                cs_narrator "Ольга Дмитриевна некоторое время смотрела на меня, затем снова взяла снимок."
        $ cs_d4_choice_06_done = True
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Что ещё произошло?"
    cs_narrator "Я рассказала про пионерку и голос из темноты. Последние слова выговорила с трудом."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Она сказала, что я не должна была здесь проснуться."
    cs_narrator "Вожатая подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Именно так?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А когда мы уходили, она сказала: «До встречи, Лена»."
    cs_narrator "Ольга Дмитриевна медленно положила фотографию."
    cs_narrator "Семён смотрел на неё."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Вы что-то знаете?"
    cs_narrator "Она долго молчала."
    cs_narrator "Затем тихо ответила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Я не знаю, кто с вами говорил."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А о самом лагере?"
    cs_narrator "Она опустила взгляд."
    cs_narrator "Потом поднялась и подошла к окну."
    cs_narrator "За окном пионеры шли по дорожке, смеялись, переговаривались."
    cs_narrator "Ольга Дмитриевна смотрела на них так, словно увидела что-то совершенно чужое."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Иногда мне снится это место."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Этот лагерь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Только во сне всё иногда происходит иначе. Другие разговоры, другие поручения, другие ссоры."
    cs_narrator "Она повернулась к нам."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Иногда мне снятся целые дни."
    cs_narrator "Даша присела на край свободного стула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И вы их помните?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Очень хорошо."
    cs_narrator "Она провела ладонью по подоконнику."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Настолько хорошо, что иногда путаю их с тем, что действительно происходило."
    cs_narrator "Я почувствовала, как неприятно похолодели пальцы."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Например, могу помнить разговор с человеком, которого на самом деле не было. Или поручение, которое никому не давала."
    cs_narrator "Она посмотрела на собственные руки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Когда я впервые приехала в этот лагерь, я думала, что всё от усталости…"
    cs_narrator "Она осеклась."
    cs_narrator "Я сразу заметила."
    cs_narrator "Впервые."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Подождите."
    cs_narrator "Ольга Дмитриевна подняла глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вы сказали «впервые»?"
    cs_narrator "Она нахмурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Я не это имела в виду."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Имели."
    cs_narrator "Семён внимательно посмотрел на вожатую."
    cs_narrator "Я постаралась говорить спокойнее."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сколько раз вы здесь были?"
    cs_narrator "Ольга Дмитриевна открыла рот, но не ответила. Посмотрела в окно, потом на фотографии. Наконец произнесла:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Я не помню."
    cs_narrator "В комнате стало очень тихо."
    cs_narrator "Даже Семён перестал двигаться."
    cs_narrator "Даша медленно опустила взгляд."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я пыталась понять, что именно услышала."
    cs_narrator "Она не помнила, сколько раз была здесь?"
    cs_narrator "Или не могла отличить воспоминания от снов?"
    cs_narrator "Возможно, и то и другое."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Эти сны повторяются?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Иногда."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А люди в них?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вы видели меня раньше?"
    cs_narrator "Ольга Дмитриевна ответила не сразу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "По крайней мере, до этой смены."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А Дашу?"
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Тоже нет."
    cs_narrator "Мы с Дашей переглянулись. Семён подался вперёд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А меня?"
    cs_narrator "Ольга Дмитриевна посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Иногда."
    cs_narrator "Помолчав, он спросил:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "И что я делал?"
    cs_narrator "Вожатая едва заметно улыбнулась."
    cs_narrator "Но улыбка получилась печальной."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "По-разному."
    cs_narrator "Семён хотел спросить ещё, но не решился. Я его понимала: услышать ответ бывает страшнее."
    cs_narrator "Ольга Дмитриевна вернулась к столу и взяла фотографию."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Возможно, это просто сны."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Возможно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Но теперь у нас есть причины проверять и другие объяснения."
    cs_narrator "Ольга Дмитриевна тяжело вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Только не ходите больше в старый корпус."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сегодня точно не пойдём."
    cs_narrator "Вожатая прищурилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "А потом?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Если понадобится вернуться, сначала подготовимся. Возьмём фонари, предупредим вас и не станем ходить поодиночке."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Обещаешь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Обещаю."
    cs_narrator "Даша немедленно добавила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И одна она больше не пойдёт."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Это уже внесено в домашний устав. Красным карандашом."
    cs_narrator "Семён усмехнулся."
    cs_narrator "Но Ольга Дмитриевна не улыбнулась."
    cs_narrator "Она осторожно взяла самый старый снимок — тот, который я нашла в верхней комнате."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Можно я оставлю эту фотографию? Хочу рассмотреть внимательнее."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Хорошо. Только, пожалуйста, не потеряйте."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Верну."
    cs_narrator "Я аккуратно сложила оставшиеся документы."
    $ cs_d4_olga_has_undated_photo = True
    $ cs_d4_undated_photo_location = "olga"
    $ cs_d4_scene_cast = ['mt']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Мы поднялись."
    cs_narrator "Семён первым направился к двери."
    cs_narrator "Даша пошла следом."
    cs_narrator "Я задержалась, чтобы поправить листы."
    cs_narrator "И тут вожатая тихо окликнула меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Лена."
    cs_narrator "Я обернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да?"
    cs_narrator "Она несколько секунд смотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Мне не нравится, что ты туда ходила."
    cs_narrator "Я опустила взгляд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_mt "Но спасибо, что рассказала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пожалуйста."
    $ cs_director_scene("bg ext_house_of_mt_day")
    scene bg ext_house_of_mt_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Когда мы вышли, я ещё раз оглянулась."
    cs_narrator "Ольга Дмитриевна стояла возле стола, держа фотографию двумя руками."
    cs_narrator "Она даже не заметила, что дверь осталась приоткрытой."
    cs_narrator "И впервые мне показалось, что вожатая испугалась не меньше нас."
    return
