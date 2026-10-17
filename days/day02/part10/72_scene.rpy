# -*- coding: utf-8 -*-
label cs_day02_72:
    $ save_name = "Чужая смена — День 2: Не всем нужна одинаковая Лена"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    label cs_check_finale_72:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Дарья отложила книгу."
    cs_narrator "Посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ну что, как тебе разговор с Женей?"
    cs_narrator "Я задумалась."
    cs_ls "Хорошо."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Только хорошо?"
    cs_narrator "Я улыбнулась."
    cs_ls "Очень хорошо."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я немного помолчала."
    cs_narrator "Потом посмотрела на неё серьёзнее."
    cs_ls "Знаешь, я сегодня кое-что решила."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что именно?"
    cs_narrator "Я осторожно положила повреждённую руку на колени."
    cs_ls "С Женей буду вести себя немного иначе."
    cs_narrator "Дарья приподняла бровь."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Почему?"
    cs_narrator "Я задумалась."
    cs_th "Как лучше объяснить?"
    cs_ls "Потому что она действительно любит тишину."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это ты только сегодня заметила?"
    cs_narrator "Я улыбнулась."
    cs_ls "Нет. Просто раньше воспринимала её раздражение как повод пошутить ещё раз."
    cs_narrator "Немного помолчала."
    cs_ls "А сегодня поняла, что ей не обязательно должно быть весело от каждой моей шутки."
    cs_narrator "Дарья внимательно слушала."
    cs_ls "Если человеку хочется побыть одному, это ведь не означает, что его нужно срочно спасать от одиночества."
    cs_narrator "Она кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Согласна."
    cs_narrator "Я улыбнулась."
    cs_ls "К тому же выяснилось, что с Женей можно прекрасно разговаривать о книгах."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Даже не выводя её из себя?"
    cs_ls "Представь себе."
    cs_narrator "Она рассмеялась."
    cs_narrator "Я тоже улыбнулась."
    cs_narrator "Потом задумалась."
    cs_ls "И это не значит, что теперь я буду рядом с ней только молчать. Просто стану внимательнее к тому, когда она хочет разговаривать, а когда нет."
    cs_narrator "Дарья немного помолчала."
    cs_narrator "Затем произнесла:"
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне нравится эта мысль."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Правда?"
    cs_narrator "Она кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да. Ты ведь сама сегодня сказала, что не хочешь, чтобы тебя воспринимали только с одной стороны."
    cs_narrator "Я улыбнулась."
    cs_ls "Хорошо запоминаешь."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Стараюсь."
    cs_narrator "Несколько секунд мы молчали."
    cs_narrator "Потом я осторожно улеглась поперёк кровати."
    cs_narrator "Повернулась к Даше."
    cs_ls "Вообще, знаешь, с разными людьми я веду себя по-разному."
    cs_narrator "Она посмотрела на меня."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Например?"
    cs_narrator "Я задумалась."
    cs_ls "С Женей интересно обсуждать книги."
    cs_narrator "Дарья кивнула."
    cs_ls "Со Славей приятно просто работать. Она умеет организовать всё так, что даже я начинаю выглядеть полезным членом общества."
    cs_narrator "Дарья усмехнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Иногда ты им и являешься."
    cs_narrator "Я приложила здоровую руку к груди."
    cs_ls "Спасибо за высокую оценку."
    cs_narrator "Она рассмеялась."
    cs_ls "С Мику хочется говорить о музыке. Даже когда я не особенно понимаю, как она умудряется обсуждать пять тем одновременно."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А с Семёном?"
    cs_narrator "Я задумалась."
    cs_narrator "Очень серьёзно."
    cs_narrator "Потом улыбнулась."
    cs_ls "С Семёном у нас непрерывное соревнование по взаимному поддразниванию."
    cs_narrator "Дарья засмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это точно."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Но он хороший человек."
    cs_narrator "Она кивнула."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Согласна."
    cs_narrator "Я на секунду вспомнила дорогу."
    cs_narrator "Разговор перед исследованием."
    if cs_friend_se >= 2:
        cs_narrator "Семёна, который сам предложил помощь после концерта."
    else:
        cs_narrator "Семёна, который выслушал нас и прошёл с нами дорогу."
    cs_th "Да."
    cs_th "Хороший."
    cs_narrator "Потом посмотрела на Дарью."
    cs_ls "А с тобой…"
    cs_narrator "Она приподняла бровь."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что со мной?"
    cs_narrator "Я немного помолчала."
    cs_narrator "Улыбнулась."
    cs_ls "С тобой мне хочется быть собой. Без необходимости каждый раз объяснять, почему я сегодня разговорчивая, а завтра могу молчать несколько часов."
    cs_narrator "Дарья посмотрела на меня."
    cs_narrator "Несколько секунд ничего не говорила."
    cs_narrator "Потом тихо улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Мне это нравится."
    cs_narrator "Я почувствовала, что тоже улыбаюсь."
    cs_th "Вот ведь."
    cs_th "Снова удалось сказать что-то совершенно серьёзное."
    cs_th "И мир не рухнул."
    cs_narrator "Я слегка приподнялась."
    cs_ls "Хотя предупреждаю: это не означает, что от моих шуток ты теперь официально освобождена."
    cs_narrator "Дарья рассмеялась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Я и не рассчитывала."
    return
