# -*- coding: utf-8 -*-
label cs_day02_73:
    $ save_name = "Чужая смена — День 2: Неофициальные переговоры"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_73:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Я села ровнее."
    cs_narrator "Повернулась к Дарье."
    cs_ls "Кстати, раз уж мы обсуждаем межличностные отношения…"
    cs_narrator "Она слегка прищурилась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лена."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Я ещё ничего не предложила."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Именно поэтому и насторожилась."
    cs_narrator "Я улыбнулась."
    cs_ls "Несправедливо. У меня, между прочим, бывают вполне достойные предложения."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Например?"
    cs_narrator "Я задумалась."
    cs_ls "Например, завтра можно спокойно позавтракать, не отправляясь потом проверять геометрию окружающего мира."
    cs_narrator "Она рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Уже неплохо."
    cs_ls "А потом…"
    cs_narrator "Я сделала небольшую паузу."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что потом?"
    cs_narrator "Я улыбнулась."
    cs_ls "Можно снова провести немного времени вместе."
    cs_narrator "Она ненадолго замолчала."
    cs_narrator "Затем тоже улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы и так почти весь день вместе."
    cs_ls "Вот именно. А мне всё ещё не надоело."
    cs_narrator "Дарья рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Удивительное достижение."
    cs_narrator "Я задумалась."
    cs_ls "Знаешь, для меня — действительно немного удивительное."
    cs_narrator "Она посмотрела внимательнее."
    cs_narrator "Я немного помолчала."
    cs_ls "Обычно мне нужно немало личного пространства. Даже если человек мне нравится."
    cs_narrator "Дарья кивнула."
    cs_ls "А с тобой я почему-то вполне спокойно могу находиться рядом почти весь день."
    cs_narrator "Она улыбнулась мягче."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне тоже с тобой хорошо."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "И на секунду совершенно забыла, какую шутку собиралась произнести."
    cs_th "Вот так."
    cs_th "Одна короткая фраза."
    cs_th "А почему-то звучит важнее половины моих длинных признаний."
    cs_narrator "Дарья, кажется, заметила мою растерянность."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я улыбнулась."
    cs_ls "Ничего. Просто приятно слышать."
    cs_narrator "Она кивнула."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом я осторожно протянула ей здоровую руку."
    cs_ls "Можно?"
    cs_narrator "Дарья посмотрела на мою ладонь."
    cs_narrator "Затем на меня."
    cs_narrator "И улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Можно."
    cs_narrator "Она взяла меня за руку."
    cs_narrator "Я осторожно переплела наши пальцы."
    cs_narrator "Некоторое время мы просто сидели."
    cs_narrator "Молча."
    cs_narrator "И я вдруг почувствовала, что мне совершенно не хочется разрушать этот момент очередной шуткой."
    cs_th "Интересно."
    cs_th "Вчера я едва смогла признаться ей в своих чувствах."
    cs_th "Сегодня мы уже можем спокойно сидеть рядом и держаться за руки."
    cs_th "И при этом я всё ещё не знаю, что будет дальше."
    cs_narrator "Но почему-то именно сейчас неизвестность не казалась особенно страшной."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Лен?"
    cs_ls "Да?"
    cs_narrator "Она чуть улыбнулась."
    show cs_darya hands_on_hips pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только не начинай сейчас говорить, что мы подписали какой-нибудь договор."
    cs_narrator "Я замерла."
    cs_narrator "Потом медленно повернула голову."
    cs_ls "Ты только что уничтожила прекрасную шутку, которую я собиралась произнести."
    cs_narrator "Дарья рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я догадалась."
    cs_narrator "Я вздохнула."
    cs_ls "Безобразие. У меня отбирают профессиональный инструментарий."
    cs_narrator "Она улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Можешь придумать новую."
    cs_narrator "Я посмотрела на наши руки."
    cs_narrator "Потом на неё."
    cs_narrator "И тоже улыбнулась."
    cs_ls "Не сейчас."
    cs_narrator "Дарья немного удивилась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему?"
    cs_narrator "Я слегка пожала плечами."
    cs_ls "Потому что мне и так хорошо."
    cs_narrator "Она ничего не сказала."
    cs_narrator "Только чуть крепче сжала мою ладонь."
    cs_th "Пожалуй, впервые за сегодня я действительно не хотела добавить ничего остроумного."
    return
