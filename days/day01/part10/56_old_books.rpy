# -*- coding: utf-8 -*-
label cs_day01_56:
    $ save_name = "Чужая смена — День 1: Книги без будущего"
    label cs_check_day01_part10_join:
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/library_day.ogg":
        play ambience "sound/ambiences/library_day.ogg" fadeout 1.5 fadein 1.5
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    # cs_director_begin: REFLECTIVE_SHOT: Book dates and shelf focus
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_3ce72e702a:
    # cs_director_end
    cs_narrator "Я прошла вдоль полок. Потёртые обложки, пожелтевшие страницы, библиотечные штампы."
    cs_narrator "Проверила даты в трёх книгах: 1974, 1968, 1979."
    cs_narrator "Для местных — обычные книги. Для меня — издания, которым несколько десятилетий."
    # cs_director_begin: Return to direct interaction: Book dates and shelf focus
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_a3c480bd39:
    # cs_director_end
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Представляешь, всё это для нас уже антиквариат."
    cs_narrator "Она прочитала дату на одной из книг."
    cs_da "Странное чувство."
    cs_ls "Угу."
    cs_narrator "Я повернула страницу."
    cs_ls "В нашем времени за такие экземпляры коллекционеры иногда готовы платить вполне приличные деньги."
    cs_da "Только здесь они стоят на обычной полке."
    cs_ls "Вот именно."
    # cs_director_begin: Zhenya looks up and joins the book conversation
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    label cs_director_check_b16e3d0836:
    # cs_director_end
    cs_narrator "Женя подняла голову."
    # cs_speaker: present
    show cs_zhenya normal pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Что вас удивляет?"
    cs_narrator "Я показала ей книгу."
    cs_ls "Год издания."
    cs_narrator "Она посмотрела на обложку."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А что с ним?"
    cs_ls "Ничего. Просто непривычно."
    cs_narrator "Женя нахмурилась."
    # cs_speaker: present
    show cs_zhenya thinking pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вы какие-то странные."
    cs_ls "Нам сегодня это уже говорили."
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Не сомневаюсь."
    cs_narrator "Я снова стала серьёзной."
    cs_ls "Слушай, а у тебя есть свежие газеты?"
    # cs_speaker: present
    show cs_zhenya explaining pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Есть. Зачем?"
    cs_ls "Хочу посмотреть дату."
    cs_narrator "Женя молча достала несколько выпусков из стопки возле стола."
    # cs_director_begin: REFLECTIVE_SHOT: Checking publication dates
    $ cs_reflective_focus()
    with cs_sprite_change
    label cs_director_check_1bec142f87:
    # cs_director_end
    cs_narrator "В шапке верхней газеты стоял 1980-й. В следующей — тоже."
    cs_th "Согласуется. По крайней мере, внешне."
    # cs_darya_variety: reaction
    # cs_reflective_suppressed: show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    # cs_director_begin: Return to direct interaction: Checking publication dates
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    label cs_director_check_214c14521a:
    # cs_director_end
    cs_da "Ну что?"
    cs_narrator "Я показала ей газету."
    cs_ls "Здесь тоже восьмидесятый."
    cs_da "Получается, подтверждение?"
    cs_ls "Подтверждение того, что весь этот мир считает текущим именно этот год."
    # cs_director_begin: Librarian rejoins the conversation
    $ cs_frame_focus(["cs_darya", "cs_zhenya"])
    with cs_sprite_change
    label cs_director_check_47edd071d3:
    # cs_director_end
    cs_narrator "Женя подняла взгляд."
    # cs_speaker: present
    show cs_zhenya arms_crossed pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "А какой ещё?"
    cs_narrator "Я замолчала."
    cs_th "Вот теперь аккуратнее."
    cs_ls "Хороший вопрос."
    cs_narrator "Женя посмотрела на меня с явным недоверием."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Ты издеваешься?"
    cs_ls "Нет. Просто объяснить довольно сложно."
    # cs_speaker: present
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Попробуй."
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она покачала головой: с объяснениями мы уже однажды увлеклись."
    cs_th "И правильно. С Шуриком и Электроником хватило."
    cs_narrator "Я аккуратно положила газету обратно."
    cs_ls "Давай пока ограничимся тем, что мы не совсем понимаем, как сюда попали."
    cs_narrator "Женя скрестила руки."
    # cs_speaker: present
    show cs_zhenya glasses_touch pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Вы же приехали сегодня?"
    cs_ls "Да."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И не знаете, как?"
    cs_da "Помним поездку. Но не можем объяснить, почему оказались именно здесь."
    cs_narrator "Женя внимательно посмотрела на нас обеих."
    # cs_speaker: present
    show cs_zhenya angry pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Тогда вам лучше поговорить с Ольгой Дмитриевной."
    cs_narrator "Я тихо усмехнулась."
    cs_ls "Уже говорили."
    # cs_speaker: present
    show cs_zhenya shy pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "И?"
    cs_ls "Пока нас поселили в домик."
    cs_narrator "Женя немного помолчала."
    # cs_speaker: present
    show cs_zhenya shy pioneer normal at cs_darya_normal_left zorder 10
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_mz "Разумно. Не на улице же оставлять."
    cs_th "Первое решение вожатой, которое никто не оспаривает."
    return
