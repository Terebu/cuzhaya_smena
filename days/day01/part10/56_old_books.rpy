# -*- coding: utf-8 -*-
label cs_day01_56:
    $ save_name = "Чужая смена — День 1: Книги без будущего"
    label cs_check_day01_part10_join:
    $ renpy.music.set_volume(0.24,delay=1.0,channel="ambience")
    if renpy.music.get_playing(channel="ambience") != "sound/ambiences/library_day.ogg":
        play ambience "sound/ambiences/library_day.ogg" fadeout 1.5 fadein 1.5
    cs_narrator "Я медленно прошла вдоль книжных полок."
    cs_narrator "Книги выглядели совершенно обычными."
    cs_narrator "Потёртые обложки."
    cs_narrator "Пожелтевшие страницы."
    cs_narrator "Старые библиотечные штампы."
    cs_narrator "Я осторожно вытащила одну."
    cs_narrator "Открыла."
    cs_narrator "Год издания — 1974."
    cs_narrator "Другую."
    cs_narrator "1968."
    cs_narrator "Третью."
    cs_narrator "1979."
    cs_narrator "Я провела пальцем по дате."
    cs_th "Интересно."
    cs_narrator "Для местных жителей это были обычные книги."
    cs_narrator "Для меня — издания, которым уже несколько десятилетий."
    cs_narrator "Я посмотрела на Дарью."
    cs_ls "Представляешь, всё это для нас уже антиквариат."
    cs_narrator "Она взяла одну из книг."
    cs_narrator "Прочитала дату."
    cs_da "Странное чувство."
    cs_ls "Угу."
    cs_narrator "Я повернула страницу."
    cs_ls "В нашем времени за такие экземпляры коллекционеры иногда готовы платить вполне приличные деньги."
    cs_da "Только здесь они стоят на обычной полке."
    cs_ls "Вот именно."
    cs_narrator "Женя подняла голову."
    show mz normal glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Что вас удивляет?"
    cs_narrator "Я показала ей книгу."
    cs_ls "Год издания."
    cs_narrator "Она посмотрела на обложку."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "А что с ним?"
    cs_ls "Ничего. Просто непривычно."
    cs_narrator "Женя нахмурилась."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Вы какие-то странные."
    cs_narrator "Я кивнула."
    cs_ls "Нам сегодня это уже говорили."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Не сомневаюсь."
    cs_narrator "Я улыбнулась."
    cs_narrator "Но потом снова стала серьёзной."
    cs_ls "Слушай, а у тебя есть свежие газеты?"
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Есть. Зачем?"
    cs_ls "Хочу посмотреть дату."
    cs_narrator "Женя молча достала несколько выпусков из стопки возле стола."
    cs_narrator "Я взяла верхний."
    cs_narrator "Посмотрела на шапку."
    cs_narrator "1980 год."
    cs_narrator "Ещё один номер."
    cs_narrator "То же самое."
    cs_narrator "Я медленно выдохнула."
    cs_th "Значит, всё действительно согласуется."
    cs_th "По крайней мере, внешне."
    # cs_darya_variety: reaction
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    cs_da "Ну что?"
    cs_narrator "Я показала ей газету."
    cs_ls "Здесь тоже восьмидесятый."
    cs_narrator "Она кивнула."
    cs_da "Получается, подтверждение?"
    cs_ls "Подтверждение того, что весь этот мир считает текущим именно этот год."
    cs_narrator "Женя подняла взгляд."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "А какой ещё?"
    cs_narrator "Я замолчала."
    cs_th "Вот теперь аккуратнее."
    cs_ls "Хороший вопрос."
    cs_narrator "Женя посмотрела на меня с явным недоверием."
    show mz angry glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz angry glasses pioneer at cs_actor_left zorder 10
    cs_mz "Ты издеваешься?"
    cs_ls "Нет. Просто объяснить довольно сложно."
    show mz normal glasses pioneer at cs_actor_left zorder 10
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Попробуй."
    cs_narrator "Я посмотрела на Дарью."
    # cs_darya_variety: reaction
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    cs_narrator "Она чуть заметно покачала головой."
    cs_narrator "Не запрещая."
    cs_narrator "Скорее напоминая, что мы уже однажды слишком увлеклись объяснениями."
    cs_th "И правильно."
    cs_th "С Шуриком и Электроником хватило."
    cs_narrator "Я аккуратно положила газету обратно."
    cs_ls "Давай пока ограничимся тем, что мы не совсем понимаем, как сюда попали."
    cs_narrator "Женя скрестила руки."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Вы же приехали сегодня?"
    cs_ls "Да."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И не знаете, как?"
    cs_da "Помним поездку. Но не можем объяснить, почему оказались именно здесь."
    cs_narrator "Женя внимательно посмотрела на нас обеих."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Тогда вам лучше поговорить с Ольгой Дмитриевной."
    cs_narrator "Я тихо усмехнулась."
    cs_ls "Уже говорили."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "И?"
    cs_ls "Пока нас поселили в домик."
    cs_narrator "Женя немного помолчала."
    # cs_speaker: present
    show mz normal glasses pioneer at cs_actor_left zorder 10
    cs_mz "Разумно. Не на улице же оставлять."
    cs_narrator "Я кивнула."
    cs_th "Надо же."
    cs_th "Первое решение Ольги Дмитриевны, которое никто не пытается оспорить."
    return
