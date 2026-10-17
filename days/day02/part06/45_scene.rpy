# -*- coding: utf-8 -*-
label cs_day02_45:
    $ save_name = "Чужая смена — День 2: Вопросы к вожатой"
    $ cs_part05_live = False
    $ cs_part06_live = True
    $ cs_director_scene("bg ext_camp_entrance_day")
    scene bg ext_camp_entrance_day
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen neutral pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    with Dissolve(0.8)
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/camp_center_day.ogg":
        play ambience "sound/ambiences/camp_center_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.15, channel="ambience", delay=1.0)
    stop music fadeout 2.0
    label cs_check_part06_s45:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_semen", "cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Мы едва успели пройти под вывеской, когда услышали знакомый голос."
    cs_mt "Лена! Семён! Дарья!"
    cs_narrator "Я остановилась."
    cs_th "Ну конечно."
    cs_th "Кто ещё мог появиться именно сейчас?"
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide mz
    # cs_presence_keep: hide un
    # cs_presence_keep: hide mi
    # cs_presence_keep: hide dv
    # cs_presence_keep: hide sl
    # cs_presence_keep: hide us
    # cs_presence_keep: hide sh
    # cs_presence_keep: hide el
    # cs_presence_keep: hide cs
    show mt angry pioneer far at cs_actor_far_left zorder 10
    show cs_semen neutral pioneer far at cs_semen_far_center
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part06_cast = ["mt", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part06_olga_arrived:
    cs_narrator "Ольга Дмитриевна шла по дорожке в нашу сторону."
    cs_narrator "Выражение лица у неё было далеко не приветливым."
    cs_mt "Где вы были?"
    cs_narrator "Я посмотрела на Дарью."
    cs_narrator "Потом на Семёна."
    cs_narrator "И решила, что выдумывать объяснение сейчас совершенно бессмысленно."
    cs_ls "За воротами. Проверяли дорогу."
    cs_narrator "Ольга Дмитриевна остановилась перед нами."
    cs_mt "Без разрешения?"
    cs_narrator "Я немного помолчала."
    cs_ls "Да."
    cs_narrator "Она тяжело вздохнула."
    cs_mt "Я понимаю, что вам интересно всё вокруг. Но здесь летний лагерь, а не туристическая база. Если куда-то уходите, хотя бы предупреждайте."
    cs_narrator "Семён шагнул чуть ближе."
    show cs_semen serious pioneer far at cs_semen_far_center
    $ cs_part06_cast = ["mt", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Мы были вместе и никуда с дороги не сворачивали."
    cs_mt "Это хорошо. Но я должна знать, где вы находитесь."
    cs_narrator "Дарья кивнула."
    cs_da "Вы правы. Нужно было предупредить."
    cs_narrator "Я посмотрела на неё."
    cs_narrator "Потом на Ольгу Дмитриевну."
    cs_th "Ну да."
    cs_th "В этой части она действительно права."
    cs_narrator "Мы исчезли из поля зрения лагеря, ничего толком не сказав."
    cs_narrator "И если бы случилось что-нибудь ещё более странное, искать нас было бы неизвестно где."
    cs_ls "Извините. В следующий раз предупредим."
    show mt normal pioneer far at cs_actor_far_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Ольга Дмитриевна немного смягчилась."
    cs_mt "Надеюсь."
    cs_narrator "Я посмотрела за её плечо."
    cs_narrator "На дорогу, исчезавшую между деревьями."
    cs_narrator "Потом снова на неё."
    cs_ls "Можно кое-что спросить?"
    cs_narrator "Она насторожилась."
    cs_mt "Что?"
    cs_ls "А куда ведёт эта дорога?"
    cs_narrator "Ольга Дмитриевна ответила не сразу."
    cs_mt "Из лагеря."
    cs_narrator "Я едва заметно улыбнулась."
    cs_ls "В этом я уже убедилась. А дальше?"
    cs_narrator "Она посмотрела на меня."
    cs_mt "Что значит «дальше»?"
    cs_ls "Мы шли по ней достаточно долго. И дважды вернулись к одной и той же отметке, хотя ни разу не разворачивались."
    cs_narrator "Пауза."
    cs_narrator "Взгляд Ольги Дмитриевны ненадолго задержался на мне."
    cs_narrator "Затем на Семёне."
    cs_mt "Что ещё за отметка?"
    cs_narrator "Дарья ответила прежде, чем я успела открыть рот."
    show cs_darya explaining pioneer far at cs_darya_far_right
    $ cs_part06_cast = ["mt", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мы оставили заметный ориентир у дороги. Резинку на кусте и стрелку на земле. Потом шли вперёд, а они снова оказались перед нами."
    cs_narrator "Ольга Дмитриевна молчала."
    cs_narrator "Я внимательно следила за её лицом."
    cs_narrator "Её взгляд на секунду изменился."
    cs_narrator "Но что именно это означало, понять было невозможно."
    cs_narrator "Удивление?"
    cs_narrator "Раздражение?"
    cs_narrator "Или просто усталость от трёх новеньких, которые уже второй день ведут себя совершенно непонятно?"
    cs_mt "Возможно, вы где-то ошиблись с направлением."
    cs_sy "Мы старались всё проверять."
    cs_mt "И всё-таки дорога — не место для подобных экспериментов."
    cs_narrator "Я посмотрела на неё."
    cs_ls "А вы сами когда-нибудь выходили по ней из лагеря?"
    cs_narrator "Она выдержала небольшую паузу."
    cs_mt "Лена, сейчас не время для очередного разговора о ваших загадках."
    cs_narrator "Я не ответила."
    cs_narrator "Она продолжила уже спокойнее:"
    cs_mt "Если хотите куда-нибудь сходить, сначала обсудите это со мной. А пока возвращайтесь к обычным делам. Вечером у нас мероприятие, к которому все готовятся."
    cs_narrator "Я кивнула."
    cs_ls "Хорошо."
    cs_narrator "Ольга Дмитриевна посмотрела на нас ещё раз."
    cs_mt "И больше не уходите за территорию без предупреждения."
    show cs_darya shrug pioneer far at cs_darya_far_right
    $ cs_part06_cast = ["mt", "cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Поняли."
    cs_sy "Да."
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
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
    show cs_semen serious pioneer normal at cs_semen_normal_left
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_part06_olga_left:
    cs_narrator "Она направилась обратно к площади."
    # cs_director_begin: Physical departure in the authored scene
    $ cs_actor_exit(["mt"])
    with cs_sprite_leave
    label cs_director_check_6f05e1023d:
    # cs_director_end
    cs_narrator "Мы некоторое время стояли молча."
    cs_narrator "Затем Семён тихо произнёс:"
    show cs_semen thinking pioneer normal at cs_semen_normal_left
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_sy "Ну что?"
    cs_narrator "Я проводила вожатую взглядом."
    cs_ls "У меня появилось ещё несколько вопросов."
    cs_narrator "Дарья посмотрела на меня."
    show cs_darya explaining pioneer normal at cs_darya_normal_right
    $ cs_part06_cast = ["cs_semen", "cs_darya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Потому что она не ответила?"
    cs_narrator "Я кивнула."
    cs_ls "Да. Но это пока ничего не доказывает."
    cs_narrator "Семён задумался."
    cs_sy "Может, она просто не поверила."
    cs_ls "Вполне возможно."
    # cs_director_begin: REFLECTIVE_SHOT: Road and unproven knowledge of the counsellor
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_6e6ed1e2e7:
    # cs_director_end
    cs_narrator "Я ещё раз посмотрела на дорогу."
    cs_th "Но почему Ольга Дмитриевна не смогла назвать ни одного места, куда она ведёт?"
    cs_th "Не знает?"
    cs_th "Не хочет говорить?"
    cs_th "Или я опять пытаюсь увидеть тайну там, где её нет?"
    cs_narrator "Вопрос оставался открытым."
    return
