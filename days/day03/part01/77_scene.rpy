# -*- coding: utf-8 -*-
label cs_day03_77:
    $ save_name = "Чужая смена — День 3: Главный специалист по всему"
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    $ cs_frame_focus(["sl"])
    label cs_check_day03_77:
    cs_narrator "Славя заметила меня почти одновременно."
    cs_narrator "И сразу улыбнулась."
    cs_sl "Доброе утро, Лена!"
    cs_narrator "Я остановилась."
    cs_ls "Доброе."
    cs_narrator "Посмотрела на коробку."
    cs_narrator "Потом на Славю."
    cs_narrator "Затем снова на коробку."
    cs_ls "Знаешь, я начинаю подозревать, что ты вообще не ложишься спать."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_sl "Почему?"
    cs_narrator "Я указала на коробку."
    cs_ls "Потому что нормальные люди сейчас досматривают сны. А ты уже переносишь имущество лагеря из пункта А в пункт Б."
    cs_sl "Мне просто нужно убрать оставшиеся после вчерашнего вечера вещи."
    cs_narrator "Я кивнула."
    cs_ls "Разумеется. Вчера концерт закончился, а хозяйственная часть решила не прекращать работу ни на минуту."
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_sl "Ты сама опять с утра гуляешь."
    cs_ls "Я занимаюсь восстановлением здоровья."
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Славя посмотрела на мой локоть."
    cs_sl "В спортивной форме?"
    cs_narrator "Я задумалась."
    cs_ls "Хорошее замечание. Начинаю подозревать, что ты умеешь проводить расследования."
    cs_sl "Просто вижу."
    cs_narrator "Я вздохнула."
    cs_ls "А я так надеялась на презумпцию невиновности."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_narrator "Я немного приблизилась."
    cs_ls "Слушай, Славя, а у вас здесь вообще предусмотрен отдых для людей, которые постоянно всем помогают?"
    cs_sl "Конечно."
    cs_ls "Даже для тебя?"
    cs_narrator "Она приподняла бровь."
    cs_sl "И для меня."
    cs_narrator "Я посмотрела на неё с демонстративным недоверием."
    cs_ls "Любопытно. Пока свидетельств не обнаружено."
    cs_narrator "Славя поставила коробку на ближайшую скамейку."
    show sl normal pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "И скрестила руки."
    cs_sl "Лена, ты сейчас хочешь сказать, что мне нужно меньше работать?"
    cs_narrator "Я кивнула."
    cs_ls "Именно."
    cs_sl "А сама вчера успела побегать, помочь с объявлением, сходить за ворота и дважды попасть к Виоле."
    cs_narrator "Я открыла рот."
    cs_narrator "Закрыла."
    cs_narrator "Посмотрела на неё."
    cs_th "О."
    cs_th "Неплохо."
    cs_ls "Славя, это очень нечестный приём."
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_sl "Какой?"
    cs_ls "Использовать реальные факты против моей красивой теории."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она рассмеялась."
    cs_sl "Просто мне кажется, что ты сама не особенно умеешь отдыхать."
    cs_narrator "Я задумалась."
    cs_th "А ведь вчера в библиотеке очень даже умела."
    cs_th "Пожалуй, есть чем возразить."
    cs_ls "Между прочим, после обеда я несколько часов читала."
    cs_sl "Вот видишь. Значит, можешь."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Только что мои же показания снова использовали против меня."
    cs_sl "Получается, да."
    cs_narrator "Я покачала головой."
    cs_ls "Всё. Вы тут за два дня освоили сарказм быстрее, чем я успела научиться правильно завязывать пионерский галстук."
    show sl smile pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она улыбнулась."
    cs_sl "У тебя теперь почти всегда получается."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Спасибо. Моя квалификация растёт."
    cs_narrator "Некоторое время мы молчали."
    cs_narrator "Потом я снова посмотрела на коробку."
    cs_ls "И всё-таки. Что несёшь?"
    cs_sl "Остатки украшений и кое-что после концерта. Надо вернуть на склад."
    cs_narrator "Я заглянула внутрь."
    cs_narrator "Сверху лежали свёрнутые цветные ленты."
    cs_narrator "Какие-то крепления."
    cs_narrator "Несколько листов картона."
    cs_narrator "И небольшая папка."
    cs_ls "Ага. Вчерашняя культурная жизнь отправляется на заслуженный отдых."
    cs_sl "Примерно так."
    cs_narrator "Я кивнула."
    cs_ls "А сама организатор этого отдыха опять работает."
    cs_narrator "Славя улыбнулась."
    cs_sl "Сейчас отнесу и тоже немного посижу до завтрака."
    cs_narrator "Я подняла здоровую руку."
    cs_ls "Запомнила. Есть свидетель."
    show sl laugh pioneer at cs_actor_left
    $ cs_presence_stage()
    with cs_sprite_change
    cs_narrator "Она рассмеялась."
    return
