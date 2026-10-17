# -*- coding: utf-8 -*-
# Source: source/prologue.md. Dialogue is preserved verbatim.
label cs_scene_05:
    $ save_name = u"Чужая смена — Не туда"
    show cs_bus_city at cs_bus_ride zorder -10 with dissolve
    stop ambience fadeout 2.0
    play music cs_music_410 fadeout 2.0 fadein 3.0
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "Прошло ещё несколько минут."
    cs_narrator "Или десять."
    cs_narrator "Или двадцать."
    cs_narrator "Определить было трудно."
    # cs_director_begin: Long road/window viewpoint
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_b0c436238c:
    # cs_director_end
    cs_narrator "Я смотрела в окно, иногда переводя взгляд на пустые сиденья."
    cs_narrator "Автобус постепенно опустел."
    cs_narrator "Город сменился окраиной."
    show cs_bus_winter at cs_bus_ride zorder -10 with Dissolve(2.0)
    cs_narrator "Окраина — редкими домами."
    cs_narrator "Потом появились деревья."
    cs_narrator "Много деревьев."
    cs_narrator "Я выпрямилась."
    cs_th "Подозрительно."
    cs_narrator "За окном тянулся заснеженный лес."
    label cs_check_winter:
    cs_narrator "Сугробы по краям дороги становились всё выше, а фонарей почти не осталось."
    cs_narrator "Я несколько секунд смотрела на происходящее."
    cs_narrator "Потом негромко произнесла:"
    cs_ls "Какой интересный супермаркет."
    # cs_director_begin: Return to shared conversation
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_b9e621bd8a:
    # cs_director_end
    cs_narrator "Девушка рядом повернулась к окну."
    cs_narrator "Посмотрела на деревья."
    cs_narrator "Потом на меня."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Ты не знаешь, куда едет этот автобус?"
    cs_ls "Согласно моему великолепному планированию — к магазину."
    cs_narrator "Она снова посмотрела в окно."
    cs_da "Уверена?"
    cs_ls "Уже нет."
    pause 1.0
    cs_da "Может, спросишь у водителя?"
    cs_narrator "Я посмотрела вперёд."
    cs_narrator "Потом на неё."
    cs_narrator "Потом снова на лес."
    cs_ls "Это было бы слишком разумно."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Понятно."
    cs_ls "К тому же здесь тепло."
    # cs_darya_stage: present in story
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Это аргумент?"
    cs_ls "Очень весомый."
    cs_narrator "Она тихо рассмеялась."
    cs_narrator "Не громко."
    cs_narrator "Даже как-то осторожно, словно не хотела нарушать тишину."
    # cs_director_begin: Independent reflection during the bus ride
    $ cs_frame_focus([])
    with cs_sprite_change
    label cs_director_check_bbd8b52c96:
    # cs_director_end
    cs_narrator "Я снова отвернулась к окну."
    stop music fadeout 3.0
    cs_narrator "В принципе, ситуация была довольно идиотской."
    cs_narrator "Я села неизвестно куда."
    cs_narrator "Проехала нужную остановку."
    cs_narrator "Разрядила телефон."
    cs_narrator "И теперь ехала через лес в компании совершенно незнакомой девушки."
    cs_narrator "Нормальный человек давно бы начал беспокоиться."
    cs_narrator "Но почему-то тревоги не было."
    cs_narrator "Совсем."
    cs_narrator "В салоне стояло приятное тепло."
    show cs_snow at cs_snow_drift with dissolve
    cs_narrator "За окном медленно падал снег."
    cs_narrator "Двигатель монотонно гудел."
    cs_narrator "Автобус покачивался на неровностях дороги."
    cs_narrator "А вставать совершенно не хотелось."
    cs_narrator "Я прислонилась виском к стеклу."
    cs_narrator "Холодному."
    cs_narrator "Приятному."
    # cs_director_begin: Darya becomes the subject of attention again
    $ cs_frame_focus(["cs_dasha_winter"])
    with cs_sprite_change
    label cs_director_check_b43e26ff23:
    # cs_director_end
    cs_narrator "Мой взгляд снова остановился на девушке рядом."
    cs_narrator "Она сидела, сложив руки на коленях, и смотрела куда-то вперёд."
    cs_narrator "Кажется, тоже немного устала."
    cs_narrator "Я помолчала."
    cs_narrator "Потом всё-таки заговорила."
    cs_ls "Кстати..."
    # cs_darya_variety: reaction
    show cs_dasha_winter shy normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Да?"
    cs_ls "Лена."
    # cs_darya_variety: reaction
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_narrator "Она моргнула."
    # cs_darya_stage: present in story
    show cs_dasha_winter explaining normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что?"
    cs_ls "Меня Лена зовут."
    # cs_darya_stage: present in story
    show cs_dasha_winter shrug normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А..."
    cs_narrator "Девушка немного выпрямилась."
    $ cs_darya_known = True
    cs_da "Дарья."
    cs_ls "Дарья?"
    cs_da "Угу."
    cs_ls "Красиво."
    # cs_darya_variety: reaction
    show cs_dasha_winter smile normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Спасибо."
    label cs_check_introduced:
    cs_narrator "Я кивнула."
    cs_narrator "Разговор можно было считать завершённым."
    cs_narrator "Хотя теперь хотя бы стало известно, с кем именно я еду в неизвестность."
    cs_th "Лена и Дарья."
    cs_th "Две взрослые, самостоятельные девушки."
    cs_th "Одна не умеет смотреть маршруты, вторая почему-то всё ещё сидит рядом."
    cs_th "Отличная команда."
    cs_narrator "Я усмехнулась собственным мыслям."
    cs_narrator "Дарья покосилась на меня."
    # cs_darya_variety: reaction
    show cs_dasha_winter thinking normal at cs_darya_normal_center
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что-то смешное?"
    cs_ls "Да так. Вспомнила кое-что."
    cs_da "Понятно."
    cs_narrator "Она не стала расспрашивать."
    cs_narrator "За это я уже была готова поставить ей мысленные десять баллов."
    return
