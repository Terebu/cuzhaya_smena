# -*- coding: utf-8 -*-
label cs_day04_08:
    $ save_name = "Чужая смена — День 4: Мистика мистикой, а обед по расписанию"
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_d4_scene_cast = []
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    play music cs_day_music_daily fadein 2.0
    cs_narrator "После медпункта я решила заняться чем-нибудь нормальным. Для начала — найти Дашу и никуда больше не проваливаться."
    cs_narrator "Я шла по подсохшим дорожкам. У площадки таскали инвентарь, у столовой спорили о хлебе."
    cs_narrator "Мимо пронеслась Ульяна с чужой панамкой. За ней — возмущённый владелец. Местная преступность не дремлет."
    $ cs_director_scene("bg ext_musclub_day")
    scene bg ext_musclub_day
    $ cs_d4_scene_cast = ['sl', 'cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Возле музыкального клуба стояли Славя и Даша."
    cs_narrator "Они что-то обсуждали, время от времени поглядывая на раскрытую дверь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Нашла."
    cs_narrator "Даша повернулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    if renpy.showing("cs_darya") and renpy.get_attributes("cs_darya") != tuple("shrug pioneer normal".split()):
        show cs_darya shrug pioneer normal
        $ cs_presence_stage()
        with cs_sprite_change
    cs_da "Я не терялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Это не мешает мне гордиться результатом поисков."
    cs_narrator "Славя рассмеялась."
    cs_narrator "Потом посмотрела на мой локоть."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sl "Ты уже была у Виолы?"
    cs_narrator "Я продемонстрировала руку."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Да. Повязка отправлена на заслуженный отдых."
    cs_narrator "Даша внимательно посмотрела."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И что сказала?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Что всё заживает. Но от здравого смысла меня не освободили."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_sl "Хорошо, что хоть руку проверили."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Справедливо. Некоторые мои проблемы современной медицине пока неподвластны."
    if cs_sl_day4_notice_offer == True:
        cs_narrator "Славя вдруг что-то вспомнила."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sl "Кстати, Лен. Ты вчера говорила, что можешь помочь с объявлением."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sl "Если будет время, загляни после обеда. Нужно аккуратно оформить расписание."
        cs_narrator "После обеда мы собирались к Жене. Ещё одно обещание — и придётся заводить очередь."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Сегодня, боюсь, не успею. Можно завтра утром?"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_sl "Конечно. Это не срочно."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Тогда договорились. Буквы у меня ровные, характер — нет, но для расписания хватит."
        cs_narrator "Славя рассмеялась."
    cs_narrator "Из музыкального клуба донеслись голоса."
    cs_narrator "Мику оживлённо что-то объясняла."
    cs_narrator "Алиса пыталась вставить слово, но, судя по всему, пока безуспешно."
    cs_narrator "Даже приятно слушать, как люди ругаются из-за четырёх тактов."
    if cs_mi_followup_invitation_day3 == True:
        $ cs_d4_scene_cast = ['sl', 'mi', 'cs_darya']
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
        cs_narrator "Мику заметила нас через открытую дверь."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mi "Лена! Даша! Вы как раз вовремя! Мы тут обсуждаем вчерашнее вступление, и Алиса говорит, что его нужно немного сократить, но мне кажется, тогда пропадёт настроение, потому что я хотела сначала сделать небольшую паузу, а потом…"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_dv "Мику! Четыре такта! Я предлагаю убрать всего четыре такта!"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Вижу, творческий процесс развивается успешно."
        cs_narrator "Мику подошла ближе."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_mi "Заглянете позже? Мы хотели показать вам оба варианта!"
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Сегодня не обещаю: нужно разобраться с нашими делами. Давайте завтра, чтобы не заставлять вас ждать."
        cs_narrator "Мику просияла."
    if cs_dv_followup_invitation_day3 == True:
        $ cs_d4_scene_cast = ['sl', 'dv', 'cs_darya']
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
        cs_narrator "Алиса появилась в дверях следом."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_dv "Соколова! И про гитару не забудь."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Помню. Давай завтра, если тебе удобно? Сегодня боюсь снова не успеть."
        cs_narrator "Алиса усмехнулась."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_dv "Смотри не зазнайся."
        if cs_reflective_shot:
            $ cs_frame_focus(cs_d4_scene_cast)
            with cs_sprite_change
        cs_ls "Поздно. Я художница. Это профессиональное заболевание."
        cs_narrator "Алиса фыркнула и скрылась обратно в клубе."
    $ cs_d4_scene_cast = ['sl', 'cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Некоторое время мы с Дашей стояли рядом со Славей."
    cs_narrator "Разговор перешёл на уборку и объявления. Из клуба всё ещё доносился спор о вступлении."
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я слушала и неожиданно почувствовала себя почти нормально."
    cs_narrator "Славя прикидывала, кому ещё нужна помощь, а из клуба доносилось возмущённое «Мику, ну дай договорить!». Я уже знала, чем это закончится, и всё равно улыбалась."
    cs_narrator "Славя вскоре ушла заниматься поручениями."
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Мы с Дашей остались вдвоём."
    cs_narrator "Она внимательно посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Устала?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Немного."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Может, посидим?"
    cs_narrator "Я подняла бровь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ты предлагаешь мне добровольно отдохнуть?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Да."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Смелое решение. Но сегодня я готова попробовать."
    $ cs_director_scene("bg ext_square_day")
    scene bg ext_square_day
    $ cs_d4_scene_cast = ["cs_darya"]
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы нашли свободную скамейку под деревом."
    cs_narrator "Оттуда хорошо просматривалась площадь. Солнечные пятна медленно двигались по дорожке, а ветер шевелил листья над головой."
    cs_narrator "Даша устроилась рядом."
    cs_narrator "Некоторое время мы просто наблюдали за лагерем."
    cs_narrator "Потом она заговорила о музыке."
    cs_narrator "Рассказала, что Мику снова пыталась уговорить её сыграть на пианино, а Алиса интересовалась, какие композиции ей нравятся."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "И ты, конечно, снова сказала, что ничего особенного не умеешь?"
    cs_narrator "Даша улыбнулась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Возможно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мику тебя уже слышала. Теперь придётся придумать отговорку получше."
    cs_narrator "Она рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Я просто давно не занималась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Конечно. А я просто иногда рисую."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "У тебя ведь огромная аудитория."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Незначительная подробность."
    cs_narrator "Мы обе засмеялись."
    cs_narrator "Заговорили про Москву: любимую музыку, знакомые улицы, зимнюю слякоть. Здесь, на солнце, всё это казалось ужасно далёким."
    cs_narrator "Я невольно посмотрела на солнечную площадь."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Интересно, какая сейчас погода дома?"
    cs_narrator "Даша задумалась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Наверное, холодно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Снег, грязь, серое небо?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Возможно."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Никогда бы не подумала, что буду скучать по московской слякоти."
    cs_narrator "Она посмотрела на меня."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "А я иногда скучаю."
    cs_narrator "Даша смотрела на деревья."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Не по грязи, конечно. Просто по знакомым вещам."
    cs_narrator "Я подвинулась к ней ближе. Дома у нас осталось слишком много вещей, о которых пока тяжело было говорить."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Зато здесь кормят по расписанию."
    cs_narrator "Даша рассмеялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "И ты считаешь это преимуществом?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "После сегодняшнего утра — безусловно."
    cs_narrator "В этот момент над лагерем раздался горн."
    play sound sfx_dinner_horn_processed
    cs_narrator "Мы повернулись к столовой."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ну что ж."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я торжественно поднялась."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Мистика мистикой, а обед по расписанию."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Звучит как девиз лагеря."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Предлагаю вышить на флаге."
    $ cs_director_scene("bg ext_dining_hall_near_day")
    scene bg ext_dining_hall_near_day
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with Dissolve(0.7)
    cs_narrator "Мы направились к столовой."
    $ cs_d4_scene_cast = ['mi', 'dv', 'cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_enter
    cs_narrator "У дверей нас догнали Алиса и Мику. Спор, как выяснилось, тоже шёл обедать."
    cs_narrator "Алиса держала несколько нотных листов. Один тут же оказался перед моим носом."
    cs_dv "Соколова! Ты же художница. Иногда лучше убрать лишнее, да?"
    cs_ls "Смотря что. Мой обед, например, трогать не советую."
    cs_mi "Она про вступление! Хочет убрать четыре такта, а без них мелодия…"
    cs_dv "Быстрее начнётся."
    cs_mi "Не так начнётся!"
    cs_narrator "Обе посмотрели на меня. Я перевела взгляд на ноты."
    cs_narrator "Прекрасно. Я ещё не поела, а уже член худсовета."
    if not cs_d4_choice_08_done:
        menu:
            "Выслушать обеих и помочь найти компромисс":
                $ cs_friend_dv += 1
                $ cs_d4_dv_mi_compromise = True
                cs_narrator "Я взяла лист."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Для начала дайте обоим вариантам по одной попытке."
                cs_narrator "Алиса нахмурилась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_dv "Зачем?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Чтобы спорить о том, что услышали, а не о том, кто кого перекричит."
                cs_narrator "Мику рассмеялась."
                cs_narrator "Я посмотрела на записи."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "А если оба варианта не подойдут — попробуйте что-нибудь между ними. Ноты ведь не высечены в камне."
                cs_narrator "Алиса задумалась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_dv "Ладно. Это уже похоже на разговор."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mi "Можно попробовать! А ещё можно сначала сыграть медленно, потом чуть быстрее, чтобы понять…"
                cs_narrator "Алиса вздохнула, уже улыбаясь. Я вернула лист."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Вот. Искусство переговоров."
            "Предложить девушкам самим решить музыкальный спор":
                $ cs_d4_dv_mi_self_decide = True
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Девушки, я, конечно, великий эксперт по чужим спорам…"
                cs_narrator "Алиса прищурилась."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_dv "Но?"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Но по нотам я могу оценить только почерк. Сыграйте оба варианта — сами услышите."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_mi "А ведь правда! Мы можем сыграть оба варианта и сравнить!"
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_dv "Вот этим и займёмся."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Прекрасно. Конфликт разрешён без вмешательства третьих сторон."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_dv "Ты ведь и есть третья сторона."
                if cs_reflective_shot:
                    $ cs_frame_focus(cs_d4_scene_cast)
                    with cs_sprite_change
                cs_ls "Прошу не разрушать мою теорию."
        $ cs_d4_choice_08_done = True
    cs_narrator "Девушки вошли в столовую, договорившись продолжить работу после обеда."
    $ cs_d4_scene_cast = ['cs_darya']
    $ cs_frame_focus(cs_d4_scene_cast)
    with cs_sprite_change
    cs_narrator "Мы с Дашей остались у столовой."
    cs_narrator "Я уже взялась за дверь, когда заметила Женю. Та читала какой-то листок в стороне от очереди. Обед, видимо, мог подождать."
    cs_narrator "Даша заметила мой взгляд."
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_da "Женя?"
    if cs_reflective_shot:
        $ cs_frame_focus(cs_d4_scene_cast)
        with cs_sprite_change
    cs_ls "Ага. Пойдём поздороваемся."
    if cs_mi_followup_invitation_day3:
        $ cs_mi_followup_target_day = 5
    if cs_dv_followup_invitation_day3:
        $ cs_dv_followup_target_day = 5
    if cs_sl_day4_notice_offer:
        $ cs_d4_sl_notice_deferred = True
    return
