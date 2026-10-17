# -*- coding: utf-8 -*-
label cs_day02_52:
    $ save_name = "Чужая смена — День 2: То, о чём не хочется шутить"
    $ cs_part06_live = False
    $ cs_part07_live = True
    $ cs_director_scene("bg ext_aidpost_day")
    scene bg ext_aidpost_day
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.13, channel="ambience", delay=1.0)
    if renpy.music.get_playing() != "sound/music/a_promise_from_distant_days.ogg":
        play music "sound/music/a_promise_from_distant_days.ogg" fadeout 2.0 fadein 2.5
    $ renpy.music.set_volume(0.15, channel="music", delay=1.0)
    label cs_check_part07_s52:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "На улице всё оставалось по-прежнему."
    cs_narrator "Солнце."
    cs_narrator "Деревья."
    cs_narrator "Обычная лагерная дорожка."
    cs_narrator "Ни одного признака того, что несколько минут назад я лежала на земле, пытаясь понять, насколько серьёзно повредила руку."
    $ cs_director_scene("cs_camp_path_day")
    scene cs_camp_path_day
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_semen
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide mt
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show cs_darya worried pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы медленно спустились с крыльца."
    cs_narrator "Я посмотрела на повязку."
    cs_narrator "Потом на Дарью."
    cs_narrator "Она держалась рядом, иногда поглядывая на мой локоть."
    cs_ls "Даш."
    show cs_darya ear_touch pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да?"
    cs_narrator "Я немного помолчала."
    cs_ls "Ты сильно испугалась?"
    cs_narrator "Она посмотрела на меня."
    cs_narrator "Не ответила сразу."
    cs_narrator "Затем кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да."
    cs_narrator "Я опустила взгляд."
    cs_ls "Из-за крови?"
    cs_da "Не только."
    cs_narrator "Мы продолжили идти."
    cs_narrator "Дарья некоторое время молчала."
    cs_narrator "Потом произнесла:"
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Когда ты упала, я сначала даже не поняла, что случилось. Только услышала удар и увидела, что ты лежишь."
    cs_narrator "Она посмотрела на меня."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А потом подошла и увидела кровь. Я ведь не знала, насколько сильно ты ударилась."
    cs_narrator "Я кивнула."
    cs_ls "Понимаю."
    cs_da "И ты сразу начала шутить."
    cs_narrator "Я невольно улыбнулась."
    cs_ls "Привычка."
    cs_da "Я уже заметила."
    cs_narrator "Я немного помолчала."
    cs_narrator "Потом остановилась."
    cs_narrator "Дарья сделала ещё шаг и повернулась ко мне."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_narrator "Я посмотрела на неё."
    cs_ls "Прости."
    cs_narrator "Она удивилась."
    cs_da "За что?"
    cs_ls "За то, что не сразу сказала нормально, как себя чувствую."
    cs_narrator "Дарья внимательно посмотрела на меня."
    cs_narrator "Я выдохнула."
    cs_ls "Просто когда больно или страшно, я начинаю говорить всякую ерунду. Наверное, мне так проще не думать о том, что происходит."
    cs_narrator "Она немного помолчала."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я понимаю."
    cs_narrator "Затем добавила:"
    cs_da "И я не против твоих шуток. Просто мне нужно знать, когда тебе действительно плохо."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо."
    cs_narrator "Она улыбнулась."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Договорились?"
    cs_ls "Договорились."
    cs_narrator "Мы снова пошли."
    cs_narrator "Несколько секунд я молчала."
    cs_narrator "Потом посмотрела на повязку."
    cs_th "Забавно."
    cs_narrator "В Москве я могла проводить часами за компьютером."
    cs_narrator "Работать над рисунком."
    cs_narrator "Отвечать на сообщения."
    cs_narrator "Общаться с людьми, которых никогда не видела лично."
    cs_narrator "Но при этом мне всегда было довольно сложно просто сказать кому-нибудь, что мне страшно."
    cs_narrator "Или больно."
    cs_narrator "Или что мне нужна помощь."
    cs_narrator "Наверное, потому что после таких слов нельзя было закрыть вкладку и сделать вид, будто разговор закончился."
    cs_narrator "А здесь всё происходило иначе."
    cs_narrator "Дарья не исчезала после того, как я сказала что-нибудь неловкое."
    cs_narrator "Не требовала, чтобы я немедленно стала веселее."
    cs_narrator "Просто оставалась рядом."
    cs_narrator "Я посмотрела на неё."
    cs_th "И ведь мы знакомы меньше двух дней."
    cs_th "Как же странно всё получилось."
    cs_da "Лен?"
    cs_narrator "Я повернулась."
    cs_ls "М?"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты опять задумалась."
    cs_narrator "Я слегка улыбнулась."
    cs_ls "Есть немного."
    cs_narrator "Она посмотрела на меня."
    cs_da "Только больше не начинай бежать, когда отвлечёшься."
    cs_narrator "Я рассмеялась."
    cs_ls "Договорились. Отныне размышления исключительно в положении стоя."
    cs_da "Или сидя."
    cs_ls "Желательно на скамейке, с которой ноги достают до земли."
    show cs_darya amused pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Дарья засмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part07_cast = ["cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это уже сложнее."
    cs_narrator "Я улыбнулась."
    cs_th "Ну вот."
    cs_th "Теперь хотя бы можно шутить без ощущения, что пытаюсь скрыть всё остальное."
    return
