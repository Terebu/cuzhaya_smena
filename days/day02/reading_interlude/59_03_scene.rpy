# -*- coding: utf-8 -*-
label cs_day02_reading_03:
    $ save_name = "Чужая смена — Тишина на троих: Очень подозрительная тишина"
    $ cs_part08_live = False
    $ cs_reading_live = True
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_zhenya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    $ cs_reading_cast = []
    label cs_check_reading_03:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Прошло какое-то время. Я не следила за часами. Просто читала. Когда дверь библиотеки открылась, я услышала это краем уха."
    cs_narrator "Затем раздались шаги. По комнате кто-то прошёл. На стол легла стопка бумаг. Зашуршали страницы."
    cs_th "Женя вернулась."
    cs_narrator "Я даже не подняла головы. Дочитала абзац. Перевернула страницу. Потом ещё одну."
    cs_narrator "И только когда шаги приблизились к моему столу, оторвалась от книги."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_reading_zhenya_approached:
    cs_narrator "Женя стояла напротив. Смотрела на меня поверх очков, затем на книгу. Потом снова на меня."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Соколова?"
    cs_narrator "Я подняла голову."
    cs_ls "Привет."
    cs_narrator "Она немного помолчала."
    cs_mz "Ты давно здесь?"
    cs_ls "Не очень. Минут десять, наверное."
    cs_narrator "Женя посмотрела в сторону входа. Затем снова на меня."
    cs_mz "А зачем пришла?"
    cs_narrator "Я чуть приподняла книгу."
    cs_ls "Почитать."
    cs_narrator "Пауза."
    cs_narrator "Женя нахмурилась. Не сердито. Скорее озадаченно."
    cs_mz "Просто почитать?"
    cs_ls "Угу."
    cs_narrator "Она посмотрела на стол. На мои руки. На книгу. И снова на меня."
    cs_th "Кажется, девушка ожидала чего угодно. Очередного рассказа о будущем. Вопросов о лагерных документах. Или хотя бы попытки немедленно завести разговор."
    cs_th "Но я действительно пришла только читать."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Понятно."
    cs_narrator "Я кивнула. И вернулась к странице. Она не уходила ещё несколько секунд. Потом спросила:"
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А с рукой что?"
    cs_narrator "Я слегка повернула перевязанный локоть."
    cs_ls "Упала. Виола уже обработала."
    cs_narrator "Женя вздохнула."
    # cs_presence_keep: hide cs_darya
    # cs_presence_keep: hide cs_semen
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
    # cs_presence_keep: hide cs_dasha_winter
    # cs_presence_keep: hide cs_dasha_pioneer
    show cs_zhenya normal pioneer normal at cs_darya_normal_left
    $ cs_reading_cast = ["cs_zhenya"]
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Осторожнее надо."
    cs_ls "Согласна."
    cs_narrator "Ещё одна пауза. Она явно собиралась что-то добавить. Но я снова опустила глаза к книге."
    $ cs_mz_quiet_visit_seen = True
    cs_narrator "Никакой специальной демонстрации молчаливости. Мне просто хотелось узнать, что произойдёт дальше в истории."
    return
