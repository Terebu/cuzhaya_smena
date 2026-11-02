# -*- coding: utf-8 -*-
label cs_day04_07:
    $ save_name = "Чужая смена — День 4: Седьмой день не за горами"
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    play music cs_day_music_daily fadein 2.0
    cs_narrator "Потеплело, лагерь проснулся. По дорожкам шли пионеры, кто-то спорил из-за уборки. Возле столовой Славя раздавала поручения."
    cs_narrator "Лагерь не поддавался объяснению, зато уборка шла по графику."
    cs_narrator "Мы пошли к столовой."
    cs_narrator "«Когда я впервые приехала…» Оговорка Ольги Дмитриевны всё не шла из головы. Сколько же раз она сюда приезжала?"
    cs_narrator "Я посмотрела на Семёна и остановилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что?"
    cs_narrator "Я подняла палец."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Подожди. Арифметика."
    cs_narrator "Он нахмурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Какая ещё арифметика?"
    cs_narrator "Даша тоже повернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "У нас сегодня четвёртый день."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А Семён приехал на день раньше."
    cs_narrator "Семён задумался."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Значит, у меня пятый."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Завтра шестой. А послезавтра — седьмой."
    cs_narrator "Даша перестала улыбаться."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Последний день смены?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "По обычному расписанию — да."
    cs_narrator "Семён несколько секунд смотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "И что это значит?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не знаю."
    cs_narrator "Его лицо стало серьёзнее."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно поэтому мне и не нравится эта арифметика."
    cs_narrator "Семён невесело усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Отлично. Значит, у меня теперь есть срок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "У тебя есть дата, когда смена может закончиться. Это разные вещи."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А если всё произойдёт как в игре?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тогда будем разбираться. Но пока никто не знает, что случится именно здесь."
    cs_narrator "Он опустил взгляд."
    cs_narrator "Я чуть улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И вообще, у тебя теперь появилась очень назойливая служба безопасности."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Из двух человек."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Очень обнадёживает."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Работаем без выходных. Жалобы не принимаются."
    cs_narrator "Семён наконец рассмеялся. Хоть с этим справились."
    $ cs_director_scene("bg int_dining_hall_people_day")
    scene bg int_dining_hall_people_day
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы вошли в столовую."
    cs_narrator "Внутри пахло кашей, свежим хлебом и горячим чаем."
    cs_narrator "Оказалось, я зверски голодна. Мистика аппетит не испортила."
    cs_narrator "Мы взяли еду и устроились за свободным столом."
    cs_narrator "Семён сел напротив."
    cs_narrator "Даша рядом со мной."
    cs_narrator "Несколько минут мы просто ели."
    cs_narrator "Вокруг продолжалась обычная лагерная жизнь."
    cs_narrator "Кто-то жаловался на слишком горячий чай. За соседним столом спорили о предстоящем концерте. Возле раздачи мелькнула Ульяна, которая, кажется, пыталась убедить повариху, что одной порции ей категорически недостаточно."
    cs_narrator "Я слушала столовский шум и ела. Здесь никого не волновали старые фотографии, и пока меня это устраивало."
    cs_narrator "Семён показал ложкой на мой локоть."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что дальше?"
    cs_narrator "Я посмотрела на повязку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Медпункт."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Правильное решение."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Удивительно, насколько быстро все начали хвалить меня за элементарные поступки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "У нас было сложное утро."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не могу спорить."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "После завтрака Семён отправился по своим делам."
    cs_narrator "Условились с Семёном встретиться к вечеру и обсудить документы. Даша пошла к Славе, я — в медпункт."
    $ cs_director_scene("bg int_aidpost_day")
    scene bg int_aidpost_day
    $ cs_d4_scene_cast = ['cs']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "В прохладном медпункте пахло лекарствами. После сырости старого корпуса это успокаивало. Я постучала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Входи."
    cs_narrator "Виола оторвалась от журнала. Осмотрела меня, грязные кроссовки и повязку — на ней задержалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Доброе утро, Лена. Что на этот раз?"
    cs_narrator "Я приложила здоровую руку к груди."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Почему обязательно должно что-то случиться?"
    cs_narrator "Она подняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Потому что ты пришла с грязной повязкой."
    cs_narrator "Я посмотрела на повязку. С медиками спорить бесполезно: у них улики на руках. Причём на моих."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ладно. Есть небольшие обстоятельства."
    cs_narrator "Виола указала на кушетку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs") and renpy.get_attributes("cs") != tuple("custom explaining medical normal".split()):
        show cs custom explaining medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_vi "Садись."
    cs_narrator "Я подчинилась."
    cs_narrator "Она осторожно сняла повязку, осмотрела локоть и проверила, не появились ли новые ссадины."
    cs_narrator "Несколько секунд внимательно изучала заживающую кожу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Всё неплохо. Рана заживает."
    cs_narrator "Я облегчённо выдохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Правда, хотелось бы узнать, где ты успела так испачкать бинт."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Боюсь, объяснение будет слишком длинным для медицинской карты."
    cs_narrator "Виола усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Значит, снова приключения?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "К сожалению, моя биография развивается довольно динамично."
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Если не будешь снова лазить по грязи, можно оставить локоть без повязки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Значит, я свободна?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "От повязки. Не от здравого смысла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Второе, боюсь, пока не лечится."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Я заметила."
    cs_narrator "Она улыбнулась и выбросила старый бинт."
    cs_narrator "Я посмотрела на локоть."
    cs_narrator "Странно."
    cs_narrator "За несколько дней настолько привыкла к повязке, что отсутствие белой ткани казалось непривычным."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Даже жалко."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Чего?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Повязка придавала мне образ женщины с непростым прошлым."
    cs_narrator "Она усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Теперь придётся рассчитывать на характер."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот это действительно плохая новость."
    $ cs_d4_elbow_bandage_removed = True
    $ cs_lena_elbow_bandaged = False
    cs_narrator "Я собиралась встать, но вспомнила оговорку вожатой, фотографии, седьмой день Семёна. Виола заметила, что я задержалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Что-то ещё?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Можно задать вопрос?"
    cs_narrator "Она кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Конечно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сколько здесь обычно длится смена?"
    cs_narrator "Виола удивилась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Семь дней. А что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А потом?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Потом дети разъезжаются."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вы это помните?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Что именно?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Как они уезжают."
    cs_narrator "Улыбка исчезла с её лица."
    cs_narrator "Виола некоторое время смотрела на меня."
    cs_narrator "Потом перевела взгляд на окно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Иногда."
    cs_narrator "Я почувствовала неприятный холодок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Иногда?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Почему ты спрашиваешь?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сегодня утром мы были у Ольги Дмитриевны."
    cs_narrator "Виола отложила ручку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Она рассказала, что иногда помнит события, которых не было."
    cs_narrator "Несколько секунд Виола молчала."
    cs_narrator "Потом медленно села за стол."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs") and renpy.get_attributes("cs") != tuple("custom thoughtful medical normal".split()):
        show cs custom thoughtful medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_vi "Что вы нашли, Лена?"
    cs_narrator "Виола явно не собиралась довольствоваться словом «обстоятельства»."
    if not cs_d4_choice_07_done:
        menu:
            "Рассказать Виоле обо всём, не скрывая собственной ошибки":
                $ cs_friend_viola += 1
                $ cs_d4_viola_full_trust = True
                cs_narrator "Я глубоко вдохнула."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Сегодня утром я отправилась в старый лагерь."
                cs_narrator "Виола внимательно посмотрела на меня."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Одна."
                cs_narrator "Она закрыла глаза."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_vi "Конечно."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Да. Не самое выдающееся решение в моей жизни."
                cs_narrator "Она жестом предложила продолжать."
                cs_narrator "Я коротко рассказала про корпус, фотографии и документы. Про голос — тоже. Не пыталась выставить себя героиней. Виола выслушала, не перебивая."
            "Рассказать только о фотографиях и спросить о старом лагере":
                $ cs_d4_viola_partial_disclosure = True
                cs_narrator "Я решила пока ограничиться тем, что можно подтвердить."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "В старом корпусе сохранились документы разных лет. На фотографиях люди, очень похожие на нынешних пионеров."
                cs_narrator "Виола нахмурилась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_vi "Ты сама это видела?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Да."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_vi "А в убежище заходила?"
                cs_narrator "Врать медику, который только что держал твой локоть, — так себе стратегия."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Да."
                cs_narrator "Виола тяжело вздохнула."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_vi "Понятно."
        $ cs_d4_choice_07_done = True
    cs_narrator "После паузы она спросила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Ольга Дмитриевна знает?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Уже да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "А остальные?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пока только Даша и Семён."
    cs_narrator "Она посмотрела в окно."
    cs_narrator "Ветер слегка шевелил занавеску."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Я тоже иногда помню странные вещи."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Какие?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Другие дни. Разговоры, которых не было. Иногда помню людей, которых давно не видела."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "А иногда — как заканчивается смена."
    cs_narrator "Я осторожно спросила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Автобусы?"
    cs_narrator "Виола кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Иногда."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А в остальные разы?"
    cs_narrator "Она долго молчала."
    cs_narrator "Потом тихо произнесла:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Иногда я помню утро после того, как все должны были уехать."
    cs_narrator "Я почувствовала, как неприятно сжалось в груди."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "С теми же людьми?"
    cs_narrator "Она не ответила сразу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Иногда."
    cs_narrator "Ещё один человек, чья память не сходится с календарём. И ни одного объяснения."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Виола."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вы знаете, что произойдёт на седьмой день Семёна?"
    cs_narrator "Она покачала головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спасибо."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "За что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "За честное «нет». Сегодня это довольно редкий ответ."
    cs_narrator "Виола посмотрела на меня внимательнее."
    cs_narrator "Затем улыбнулась."
    cs_narrator "Но почти сразу стала серьёзной."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Только прошу об одном."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "О чём?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Не превращай его в эксперимент."
    cs_narrator "Я сразу подняла голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не собираюсь."
    cs_narrator "Под её взглядом я добавила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Серьёзно. Для меня он уже не просто человек, о котором я что-то знаю из игры."
    cs_narrator "Я вспомнила, как Семён сидел утром на скамейке."
    cs_narrator "Как слушал рассказ."
    cs_narrator "Как перестал улыбаться, когда понял, насколько сильно я испугалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Он мой друг."
    cs_narrator "Виола медленно кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs") and renpy.get_attributes("cs") != tuple("custom warm_smile medical normal".split()):
        show cs custom warm_smile medical normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_vi "Вот и хорошо."
    cs_narrator "Я поднялась с кушетки."
    cs_narrator "Поправила рукав."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спасибо за осмотр."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Постарайся сегодня больше ничего не повредить."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Очень амбициозная задача."
    $ cs_d4_scene_cast = ['cs']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Я подошла к двери."
    cs_narrator "Но перед выходом обернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И, кстати…"
    cs_narrator "Виола немедленно подняла палец."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "Если это очередная шутка про Семёна — не надо."
    cs_narrator "Я замерла."
    cs_narrator "Посмотрела на неё."
    cs_narrator "Потом медленно улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Потрясающе. Меня начинают понимать ещё до того, как я открою рот."
    cs_narrator "Виола усмехнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_vi "До свидания, Лена."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "До свидания."
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "На улице оказалось заметно теплее."
    cs_narrator "На крыльце я оглядела площадь. У Семёна пятый день. Завтра шестой, послезавтра седьмой."
    cs_narrator "Теперь мы хотя бы знали, о чём спрашивать. Осталось найти ответы."
    return
