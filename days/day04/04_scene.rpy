# -*- coding: utf-8 -*-
label cs_day04_04:
    $ save_name = "Чужая смена — День 4: Возвращение в нормальный «Совёнок»"
    $ cs_director_scene("bg ext_path_day")
    scene bg ext_path_day
    show cs_darya neutral sport normal at cs_darya_normal_center
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    $ day_time()
    $ persistent.sprite_time = "day"
    play music cs_day_music_daily fadein 3.0
    cs_narrator "Между деревьями показались знакомые корпуса, и я наконец выдохнула."
    cs_narrator "Дорожки, домики, знакомая советская действительность. Всё на месте."
    cs_narrator "Даже столовой с её вечными поручениями я была рада."
    cs_narrator "Но после подземелья даже эта перспектива казалась удивительно приятной."
    cs_narrator "Мы вышли из леса."
    cs_narrator "Солнце уже поднялось над деревьями. Лагерь постепенно просыпался: где-то открывали ставни, по дорожкам начали появляться первые пионеры."
    cs_narrator "Никаких заброшенных коридоров."
    cs_narrator "Никаких загадочных голосов."
    cs_narrator "Никого, кто сообщал бы мне, что я не должна была просыпаться."
    cs_narrator "Я глубоко вдохнула."
    cs_narrator "Никогда ещё запах влажной травы и далёкой лагерной кухни не казался настолько прекрасным."
    cs_narrator "Даша шла рядом и время от времени касалась моей здоровой руки."
    cs_narrator "Я заметила это, но ничего не сказала."
    cs_narrator "Возможно, она боялась, что я снова побегу исследовать какую-нибудь подозрительную развалину."
    cs_narrator "Не могу её осуждать."
    cs_narrator "Основания имеются."
    cs_narrator "Папку я прижала к боку. В здоровой руке всё ещё болталась ножка стула. Пожалуй, ей пора на пенсию."
    cs_narrator "Форма в пыли, кроссовки в грязи. Пучок на голове держался вопреки здравому смыслу."
    cs_narrator "Красавица."
    cs_narrator "Если сейчас выложить фотографию в Instagram, подписчики наверняка решат, что я снимаю какой-нибудь постапокалиптический фильм."
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    show cs_darya neutral sport normal at cs_darya_normal_right
    $ cs_d4_scene_cast = ['cs_darya', 'cs_semen']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы вышли на площадь."
    cs_narrator "И я увидела Семёна."
    cs_narrator "Он сидел на скамейке, немного ссутулившись, и смотрел куда-то в сторону столовой."
    cs_narrator "Обычный Семён."
    cs_narrator "Живой."
    cs_narrator "Здоровый."
    cs_narrator "С выражением лица «может, хоть сегодня обойдётся»."
    cs_narrator "Я остановилась."
    cs_narrator "И вдруг почувствовала такое облегчение, что сама себе удивилась."
    cs_narrator "Даша заметила перемену."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Лен?"
    cs_narrator "Я повернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "М?"
    cs_narrator "Она посмотрела на Семёна."
    cs_narrator "Потом на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Пожалуйста, без представлений."
    cs_narrator "Я задумалась."
    cs_narrator "Посмотрела на деревяшку."
    cs_narrator "Потом протянула её Даше."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Это зачем?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нельзя подходить к людям с оружием советского мебельного производства. Создаёт неправильное впечатление."
    cs_narrator "Даша взяла ножку стула и оставила её у мусорной урны, подальше от прохода."
    cs_narrator "Посмотрела на неё."
    cs_narrator "Затем на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А сейчас впечатление правильное?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вполне. Теперь я безоружна и исключительно дружелюбна."
    cs_narrator "И побежала к скамейке."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка!"
    cs_narrator "Семён поднял голову."
    cs_narrator "На его лице мгновенно появилось знакомое выражение."
    cs_narrator "Только не она."
    cs_narrator "Но затем он рассмотрел мою одежду."
    cs_narrator "Грязные кроссовки."
    cs_narrator "Пыльную футболку."
    cs_narrator "Документы в руке."
    cs_narrator "И выражение изменилось."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Соколова?.."
    cs_narrator "Я подбежала и схватила его за плечи."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сёмочка, слава богу. Ты существуешь!"
    cs_narrator "Он замер."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Чего?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нормальный. Живой. Недовольный."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты не представляешь, как я рада видеть твоё недовольное лицо."
    cs_narrator "Он медленно посмотрел на Дашу, которая подходила следом с деревянной ножкой."
    cs_narrator "Потом снова на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Мне сейчас будет страшно?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Возможно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что случилось?"
    cs_narrator "Улыбка стала заметно слабее."
    cs_narrator "Я отпустила его плечи и села рядом."
    cs_narrator "Семён внимательно наблюдал за мной."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я была в старом лагере."
    cs_narrator "Он перестал улыбаться."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Где?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "В заброшенном корпусе. Потом в убежище."
    cs_narrator "Он перевёл взгляд на Дашу."
    cs_narrator "Та молча кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Одна?!"
    cs_narrator "Я вздохнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Сначала да."
    cs_narrator "Семён несколько секунд просто смотрел на меня."
    cs_narrator "Потом медленно провёл ладонью по лицу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Ты же сама говорила, что там опасно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Говорила."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "И всё равно пошла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я последовательна в своей непоследовательности."
    cs_narrator "Он покачал головой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Удивительно, как ты вообще дожила до двадцати двух."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Везение. И редкие вспышки здравого смысла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Сегодня второго не наблюдалось."
    cs_narrator "Я посмотрела на неё."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Спасибо. Медицинская комиссия, как всегда, беспощадна."
    cs_narrator "Семён усмехнулся."
    cs_narrator "Но почти сразу стал серьёзным."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Лена, что случилось?"
    cs_narrator "Я достала фотографию."
    cs_narrator "Протянула ему."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Посмотри."
    cs_narrator "Он взял снимок, сначала почти равнодушно."
    cs_narrator "Потом нахмурился."
    cs_narrator "Поднёс ближе к лицу."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Подожди."
    cs_narrator "Показал на девушку в заднем ряду."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Славя?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Очень похожа."
    cs_narrator "Его палец переместился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Женя."
    cs_narrator "Ещё немного."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А это Лена."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Тихонова. По крайней мере, выглядит как она."
    cs_narrator "Семён поднял голову."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Когда это снято?"
    cs_narrator "Я достала второй снимок и список."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "У первого дата почти стёрлась. Второй лежал в папке за семьдесят первый год."
    cs_narrator "Семён замер."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Семьдесят первый?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ага."
    cs_narrator "Он взял список."
    cs_narrator "Пробежал глазами по строкам."
    cs_narrator "Остановился на собственном имени."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Но я тогда даже не родился."
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Вот именно."
    cs_narrator "Он медленно опустил лист."
    cs_narrator "Потом откинулся на спинку скамейки."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_semen") and renpy.get_attributes("cs_semen") != tuple("explaining pioneer normal".split()):
        show cs_semen explaining pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_sy "Рассказывай с самого начала."
    cs_narrator "И я рассказала."
    cs_narrator "Не торопясь."
    cs_narrator "О старом корпусе, фотографиях и папках за 1963 и 1971 годы. О работающем электричестве, следах чужого присутствия и девушке с двумя хвостиками."
    cs_narrator "Когда дошла до лестницы, голос невольно стал тише."
    cs_narrator "Я вспомнила, как погас свет."
    cs_narrator "Как пыталась нащупать перила."
    cs_narrator "Как стояла одна в темноте, совершенно не понимая, кто находится всего в нескольких метрах от меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "А потом она сказала, что я не должна была здесь проснуться."
    cs_narrator "Семён смотрел на меня очень внимательно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Именно так?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Именно."
    cs_narrator "Даша добавила:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А когда мы уходили, кто-то сказал: «До встречи, Лена». Это мы обе слышали."
    cs_narrator "Семён опустил взгляд на фотографию."
    cs_narrator "Несколько секунд молчал."
    cs_narrator "Потом неожиданно спросил:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Тебе было страшно?"
    cs_narrator "Я уже собиралась ответить чем-нибудь привычным."
    cs_narrator "Про диплом по подземным экспедициям и выдающийся талант к плохим решениям."
    cs_narrator "Но почему-то не смогла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Он поднял глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Серьёзно?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Очень."
    cs_narrator "Я посмотрела на собственные руки."
    cs_narrator "Они уже не дрожали."
    cs_narrator "Но ощущение темноты, наступившей сразу после щелчка выключателя, никуда не исчезло."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Особенно когда поняла, что кто-то знает моё имя и намеренно не хочет показываться."
    if not cs_d4_choice_04_done:
        menu:
            "Признаться Семёну, что действительно испугалась":
                $ cs_friend_se += 1
                $ cs_d4_se_honest_fear = True
                cs_narrator "Я посмотрела на него."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Знаешь, сегодня я впервые всерьёз подумала, что могу просто не вернуться."
                cs_narrator "Семён перестал двигаться."
                cs_narrator "Даже выражение лица изменилось."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Там было совершенно темно. Телефона нет, никто не знает, как глубоко я спустилась. Если бы кто-то закрыл дверь или обрушилась лестница…"
                cs_narrator "Я не закончила."
                cs_narrator "Семён посмотрел на документы у меня на коленях."
                cs_narrator "Потом на Дашу."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "Соколова."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "М?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                if renpy.showing("cs_semen") and renpy.get_attributes("cs_semen") != tuple("serious pioneer normal".split()):
                    show cs_semen serious pioneer normal
                    $ cs_presence_stage()
                    with cs_sprite_change
                cs_sy "В следующий раз говори заранее. Хотя бы одному из нас."
                cs_narrator "Я медленно кивнула."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Договорились."
                cs_narrator "Дарья тихо добавила:"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "И лучше не после того, как уже спустишься в подвал."
                cs_narrator "Я посмотрела на неё."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Справедливое замечание."
                cs_narrator "Семён выдохнул."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "Мне вообще не хочется выяснять, куда ты исчезла, по запискам из заброшенного бункера."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Согласна. Почта там работает отвратительно."
                cs_narrator "Он усмехнулся."
                cs_narrator "Несколько секунд мы сидели молча."
                cs_narrator "Потом я чуть толкнула его здоровым плечом."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Кстати."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "Что ещё?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Моё «слава богу, ты существуешь» было процентов на семьдесят издевательством."
                cs_narrator "Он поднял бровь."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "А на тридцать?"
                cs_narrator "Я посмотрела на него."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "На тридцать я действительно была очень рада увидеть знакомое лицо."
                cs_narrator "Он отвёл взгляд."
                cs_narrator "Но я заметила, что он улыбнулся."
            "Снизить напряжение привычной шуткой":
                $ cs_d4_se_joke_after_bunker = True
                cs_narrator "Я немного помолчала."
                cs_narrator "Потом кивнула в сторону урны, возле которой Даша оставила ножку стула."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Хотя, если честно, больше всего меня напугал один момент."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "Какой?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Когда поняла, что передо мной неизвестное подземелье, а в качестве оружия у меня ножка от стула."
                cs_narrator "Семён посмотрел на деревяшку."
                cs_narrator "Потом на меня."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "Хорошо хоть заметила."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Своевременная инвентаризация. Минут на десять позже, чем следовало."
                cs_narrator "Дарья покачала головой."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_da "В следующий раз идём вместе."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Безусловно."
                cs_narrator "Семён усмехнулся."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_sy "Зная тебя, в следующий раз ты хотя бы возьмёшь фонарь."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "И полный комплект мебели. На всякий случай."
                cs_narrator "Он рассмеялся."
                cs_narrator "Мне стало немного легче."
                cs_narrator "Но Семён то и дело косился на бумаги в моей руке."
        $ cs_d4_choice_04_done = True
    cs_narrator "Семён снова взял фотографию."
    cs_narrator "Долго рассматривал."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Значит, ты думаешь, всё это уже происходило?"
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Возможно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Циклы?"
    cs_narrator "Я задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Пока не знаю. Мы нашли старые документы с именами и лицами, которые напоминают нынешних пионеров. Но это ещё не доказывает, что время повторяется."
    cs_narrator "Он медленно кивнул."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "А в игре?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "В игре многое было иначе."
    cs_narrator "Я помолчала."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И знаешь, что самое неприятное? Я всё чаще понимаю, что мои знания могут оказаться бесполезными."
    cs_narrator "Он посмотрел на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Я могу помнить какую-нибудь сцену, характер или событие. Но здесь всё происходит не совсем так."
    cs_narrator "Я кивнула в сторону Даши."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нас с ней в оригинальной истории вообще не было."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "То есть мы изменили происходящее?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Может быть. А может, оно и без нас никогда не было таким, как я представляла."
    cs_narrator "Я посмотрела на него."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Но кое-что я уже поняла."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Что?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты не просто персонаж истории, в которую я случайно попала."
    cs_narrator "Он слегка нахмурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "У тебя своя жизнь. И удивительное терпение к моим шуточкам."
    cs_narrator "Он усмехнулся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И ты так же, как мы, не понимаешь, что происходит."
    cs_narrator "Несколько секунд Семён молчал."
    cs_narrator "Потом тихо произнёс:"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Спасибо."
    cs_narrator "Я улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Не за что. Хотя «Сёмочкой» ты всё равно останешься."
    cs_narrator "Он закрыл глаза."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Я так и думал."
    cs_narrator "Даша тихо рассмеялась."
    cs_narrator "Потом посмотрела на фотографии."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И что теперь?"
    cs_narrator "Я перевела взгляд на домики."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Теперь идём к Ольге Дмитриевне."
    cs_narrator "Семён нахмурился."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Прямо сейчас?"
    cs_narrator "Я посмотрела на свою одежду."
    cs_narrator "На грязные колени."
    cs_narrator "На рукав, испачканный пылью."
    cs_narrator "Потом на волосы, которые окончательно перестали напоминать пучок."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нет."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sy "Почему?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Потому что сначала мне нужно перестать выглядеть как экспонат, который только что достали с археологических раскопок."
    cs_narrator "Семён рассмеялся."
    cs_narrator "Даша тоже улыбнулась."
    cs_narrator "А я впервые за всё утро почувствовала, что снова нахожусь среди своих."
    return
