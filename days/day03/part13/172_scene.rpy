# -*- coding: utf-8 -*-
label cs_day03_172:
    $ save_name = "Чужая смена — День 3: Взросление по Гончарову"
    if not cs_reflective_shot:
        $ cs_pov_begin()
        with cs_sprite_leave
    cs_narrator "Я продолжила читать."
    cs_narrator "Александр Адуев, с которым я познакомилась на первых страницах, к концу книги изменился настолько, что временами хотелось проверить, точно ли это тот же самый человек."
    cs_narrator "Когда-то он приехал в Петербург с целой коллекцией возвышенных представлений о будущем."
    cs_narrator "Теперь передо мной был вполне успешный человек."
    cs_narrator "Карьера."
    cs_narrator "Деньги."
    cs_narrator "Расчётливая женитьба."
    cs_narrator "Всё, чему раньше учил его дядя."
    cs_th "Ну поздравляю, товарищ Адуев."
    cs_th "Ты добился успеха."
    cs_th "Осталось выяснить, кто именно должен этому радоваться."
    cs_narrator "Я перевернула страницу."
    cs_narrator "И неожиданно для себя задержалась на Петре Ивановиче."
    cs_narrator "В начале истории он производил впечатление человека, у которого на всё есть правильный ответ."
    cs_narrator "Чувства?"
    cs_narrator "Не будь наивным."
    cs_narrator "Мечты?"
    cs_narrator "Займись делом."
    cs_narrator "Любовь?"
    cs_narrator "Подходи разумно."
    cs_narrator "А теперь этот же человек был готов отказаться от карьеры ради жены."
    cs_narrator "Причём будто слишком поздно понял, сколько всего упустил."
    cs_th "Вот ведь."
    cs_th "Дядя всю жизнь учил племянника не быть таким, каким был он сам в молодости."
    cs_th "А в результате племянник стал похож на него прежнего, пока сам дядя наконец задумался, не слишком ли дорого ему обошлась собственная правота."
    cs_narrator "Я немного помолчала."
    cs_narrator "Снова перечитала несколько строк."
    cs_th "Интересная штука."
    cs_th "Один человек вроде бы вырос, но растерял то, что когда-то делало его живым."
    cs_th "Другой слишком поздно вспомнил, что жизнь состоит не только из правильных решений."
    cs_narrator "Я чуть усмехнулась."
    cs_th "И ни один из них не может просто взять и откатить сохранение."
    cs_narrator "Мысль заставила меня на секунду остановиться."
    cs_th "А вот это уже неприятно знакомо."
    cs_narrator "Я посмотрела в окно."
    cs_narrator "За ним темнели деревья."
    cs_narrator "Те самые, которые ещё недавно казались мне совершенно чужими."
    cs_th "Мы тоже сели в автобус, не зная, что будет дальше."
    cs_th "И теперь живём здесь."
    cs_th "Не потому, что всё решили."
    cs_th "А потому, что пока не можем ничего изменить."
    cs_narrator "Я снова опустила взгляд."
    cs_th "Но у нас, в отличие от Адуева, ещё есть возможность не забыть, кем мы были."
    cs_th "Надеюсь."
    cs_narrator "Перевернула последнюю страницу."
    cs_narrator "Прочитала финальные строки."
    $ cs_mz_book_finished_day3 = True
    label cs_check_day03_172_book_finished:
    cs_narrator "И остановилась."
    cs_narrator "Просто сидела несколько секунд."
    cs_narrator "Потом медленно закрыла книгу."
    cs_narrator "Провела здоровой ладонью по обложке."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Всё."
    cs_narrator "За рабочим столом кто-то слегка пошевелился."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    $ cs_frame_focus(["cs_zhenya"])
    with cs_sprite_change
    cs_narrator "Женя подняла голову."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Дочитала?"
    cs_narrator "Я кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Да."
    cs_narrator "Она посмотрела на книгу."
    cs_narrator "Потом на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Ну?"
    cs_narrator "Я задумалась."
    cs_th "Вот ведь."
    cs_th "За сегодняшний день она уже столько раз спрашивала, что я думаю, а сейчас ответить оказалось неожиданно трудно."
    cs_narrator "Я посмотрела на обложку."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Концовка лучше, чем я ожидала."
    cs_narrator "Женя слегка улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Почему?"
    cs_narrator "Я не ответила сразу."
    cs_th "Как объяснить?"
    cs_th "Понравилась — не то слово."
    cs_th "Счастливой её тоже не назовёшь."
    cs_th "Но правильной для этой истории…"
    cs_th "Пожалуй."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Потому что автор не стал делать вид, будто взросление автоматически превращает человека в хорошую версию самого себя."
    cs_narrator "Женя посмотрела на меня внимательнее."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Александр стал успешным. Только я не уверена, что мне хочется поздравлять его с тем, каким человеком он стал."
    cs_narrator "Она кивнула."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "А его дядя?"
    cs_narrator "Я немного подумала."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "А дядя хотя бы заметил, что из-за дел почти перестал видеть собственную жену."
    cs_narrator "Пауза."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Жаль, что так поздно. И всё-таки в самом конце он снова радуется чужому богатству — будто ещё не решил, что для него важнее."
    cs_narrator "Женя опустила взгляд на книгу."
    cs_narrator "Потом чуть улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Значит, заметила."
    cs_narrator "Я приподняла бровь."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "А я должна была?"
    cs_narrator "Она усмехнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Не обязательно."
    cs_narrator "Я покачала головой."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Женя, у меня возникает ощущение, что меня только что проверили."
    cs_narrator "Она посмотрела на меня."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_mz "Может быть."
    cs_narrator "Я замерла."
    cs_narrator "Потом медленно улыбнулась."
    if cs_reflective_shot:
        $ cs_pov_end()
        with cs_sprite_change
    cs_ls "Великолепно. Пришла за художественной литературой, а попала на внеплановую аттестацию."
    cs_narrator "Женя рассмеялась."
    cs_narrator "Не особенно громко."
    cs_narrator "Но совершенно искренне."
    cs_th "Ну вот."
    cs_th "Кажется, экзамен всё-таки сдан."
    return
