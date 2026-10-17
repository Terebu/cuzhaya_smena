# -*- coding: utf-8 -*-
label cs_day02_68c:
    $ save_name = "Чужая смена — День 2: Честный финал"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_68c:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Женя отложила ручку."
    cs_narrator "Посмотрела на книгу."
    cs_narrator "Затем снова на меня."
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А как ты относишься к последнему решению главного героя?"
    cs_narrator "Я задумалась."
    cs_ls "Думаю, оно было правильным. Но слишком поздним."
    cs_narrator "Она кивнула."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вот именно."
    cs_narrator "Потом немного помолчала."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Меня раздражало, что он почти всю книгу избегал разговора, который мог многое изменить."
    cs_narrator "Я улыбнулась."
    cs_ls "А мне понравилось, что автор не стал оправдывать его только потому, что он главный герой."
    cs_narrator "Женя посмотрела на меня."
    cs_narrator "И негромко рассмеялась."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Соколова, удивительно, но в литературе мы с тобой иногда вполне можем договориться."
    cs_narrator "Я положила здоровую руку на край стола."
    cs_ls "Звучит как большой прогресс."
    cs_narrator "Она поправила очки."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только не делай из этого событие исторического масштаба."
    cs_narrator "Я улыбнулась."
    cs_ls "Не буду."
    cs_narrator "Женя открыла журнал выдачи."
    cs_narrator "Поставила отметку."
    cs_narrator "Потом немного подумала."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Знаешь, у меня есть ещё одна книга, которая тебе может понравиться."
    cs_narrator "Я заинтересованно посмотрела на неё."
    cs_ls "Какая?"
    cs_narrator "Она назвала произведение и указала, в каком разделе его можно найти."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Там тоже многое строится на характерах. Только автор подходит к этому немного иначе."
    cs_narrator "Я кивнула."
    cs_ls "Тогда в следующий раз возьму."
    cs_narrator "Женя слегка улыбнулась."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Хорошо."
    cs_narrator "Она убрала возвращённую книгу в стопку."
    cs_narrator "Потом неожиданно добавила:"
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И вообще, можешь приходить читать. Даже если тебе ничего не нужно."
    cs_narrator "Я посмотрела на неё."
    cs_th "Вот теперь это было действительно приятно."
    cs_ls "Спасибо, Женя."
    cs_narrator "Она немного смутилась."
    cs_narrator "И тут же поправила очки."
    show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Только не превращай библиотеку в место постоянных собраний."
    cs_narrator "Я тихо рассмеялась."
    cs_ls "Договорились."
    if cs_mz_map_lead:
        cs_narrator "Женя уже собиралась вернуться к бумагам, но вспомнила ещё кое-что."
        show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "И насчёт завтрашнего поиска."
        cs_narrator "Я подняла голову."
        cs_ls "Да?"
        show cs_zhenya explaining pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Приходи после завтрака, как договаривались. Я посмотрю, в каком шкафу лежат старые каталоги."
        cs_ls "Хорошо."
        show cs_zhenya thoughtful pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "И, пожалуйста, не приводи весь лагерь."
        cs_narrator "Я улыбнулась."
        cs_ls "Постараюсь ограничить состав исследовательской группы."
        cs_narrator "Она вздохнула."
        show cs_zhenya thinking pioneer normal at cs_darya_normal_left
        $ cs_presence_stage()
        # cs_global_transition
        with cs_sprite_change
        cs_mz "Почему меня это не успокаивает?"
        cs_narrator "Дарья тихо рассмеялась."
        cs_narrator "Я тоже улыбнулась."
    $ cs_reading_book_borrowed = False
    $ cs_lena_book_returned = True
    $ cs_reading_book_location = "library_shelf"
    label cs_check_finale_returned_c:
    return
