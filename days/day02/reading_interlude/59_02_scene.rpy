# -*- coding: utf-8 -*-
label cs_day02_reading_02:
    $ save_name = "Чужая смена — Тишина на троих: Два экземпляра"
    $ cs_part08_live = False
    $ cs_reading_live = True
    $ cs_director_scene("bg int_library_day")
    scene bg int_library_day
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
    with Dissolve(0.8)
    stop music fadeout 2.0
    play ambience "sound/ambiences/library_day.ogg" fadeout 1.0 fadein 1.5
    $ renpy.music.set_volume(0.055, channel="ambience", delay=1.0)
    label cs_check_reading_02:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus([])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "В библиотеке было тихо."
    cs_narrator "Настолько тихо, что после площади я невольно замедлила шаг."
    cs_narrator "Сквозь окна проникал тёплый дневной свет."
    cs_narrator "В нём медленно кружились пылинки."
    cs_narrator "На столах лежали аккуратные стопки книг."
    cs_narrator "Вдоль стен тянулись шкафы с потёртыми деревянными полками."
    cs_narrator "Пахло бумагой."
    cs_narrator "Деревом."
    cs_narrator "И чем-то ещё — тем самым запахом старых библиотек, который невозможно воспроизвести ни в одном электронном приложении для чтения."
    cs_narrator "Я прикрыла за собой дверь."
    cs_narrator "Огляделась."
    cs_narrator "Жени не было."
    cs_th "Отлично."
    cs_th "Не придётся объяснять, что я снова пришла не ради того, чтобы вывести её из себя."
    cs_narrator "Я прошла между стеллажами."
    cs_narrator "Вчера, когда мы разговаривали, Женя держала в руках книгу."
    cs_narrator "Мне запомнилась её обложка."
    cs_narrator "Не название целиком."
    cs_narrator "Скорее цвет, оформление и характерный рисунок возле корешка."
    cs_narrator "Я остановилась перед нужной полкой."
    cs_narrator "Провела взглядом по книгам."
    cs_narrator "Одна."
    cs_narrator "Другая."
    cs_narrator "Третья."
    cs_th "Где же ты?"
    cs_narrator "Через минуту нашла."
    cs_narrator "И удивлённо моргнула."
    cs_narrator "На полке стояли два экземпляра."
    cs_narrator "У одного обложка выглядела заметно новее."
    cs_narrator "Другой был потёртым, с немного пожелтевшими страницами."
    $ cs_reading_book_id = "zhenya_second_copy"
    $ cs_reading_book_location = "reading_room"
    cs_narrator "Я осторожно достала второй."
    cs_narrator "Между страницами лежала бумажная полоска. Я оставила её для закладки."
    cs_narrator "Посмотрела на титульный лист."
    cs_narrator "Затем на полку."
    cs_th "Ну вот."
    cs_th "Никаких сложных технологий."
    cs_th "Никакого поиска по электронной библиотеке."
    cs_th "Просто стоишь и читаешь корешки."
    cs_narrator "И, что удивительно, мне это нравилось."
    cs_narrator "Я прошла к дальнему столу."
    cs_narrator "Выбрала место, где свет падал слева, не прямо в глаза."
    cs_narrator "Осторожно села."
    cs_narrator "Устроила повреждённую руку так, чтобы не давить на повязку."
    cs_narrator "Положила книгу перед собой."
    cs_narrator "Открыла."
    cs_narrator "Первые несколько строк потребовали неожиданно много внимания."
    cs_narrator "Я всё ещё думала о дороге."
    cs_narrator "О яркой резинке на кусте."
    cs_narrator "Об Ольге Дмитриевне."
    cs_narrator "О разговоре с Семёном."
    cs_narrator "Но затем начала втягиваться."
    cs_narrator "Один абзац."
    cs_narrator "Другой."
    cs_narrator "Третий."
    cs_narrator "Постепенно всё остальное отступило."
    cs_narrator "И вместо «Совёнка» передо мной возник мир совершенно другой истории."
    cs_th "Как же давно я нормально не читала бумажные книги."
    cs_narrator "В Москве я чаще пользовалась телефоном."
    cs_narrator "Иногда читала с компьютера."
    cs_narrator "Могла открыть сразу несколько вкладок, отвлечься на сообщение, проверить уведомления и вернуться к тексту через полчаса."
    cs_narrator "А здесь отвлекаться оказалось не на что."
    cs_narrator "Телефон мёртв."
    cs_narrator "Компьютера нет."
    cs_narrator "Интернета тоже."
    cs_narrator "Есть только книга."
    cs_narrator "И, пожалуй, впервые за последние два дня меня это совершенно устраивало."
    return
