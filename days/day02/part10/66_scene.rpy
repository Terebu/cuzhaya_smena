# -*- coding: utf-8 -*-
label cs_day02_66:
    $ save_name = "Чужая смена — День 2: Ещё одна маленькая просьба"
    $ cs_part09_live = False
    $ cs_reading_live = False
    $ cs_part10_live = True
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ cs_director_scene("bg ext_dining_hall_near_sunset")
    scene bg ext_dining_hall_near_sunset
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    play music "sound/music/my_daily_life.ogg" fadeout 2.0 fadein 2.0
    $ renpy.music.set_volume(0.12, channel="music")
    label cs_check_finale_66:
    # cs_director_begin: entry frame; explicit scene plan
    $ cs_frame_focus(["cs_darya"])
    with cs_sprite_change
    # cs_director_end
    cs_narrator "После ужина я действительно собиралась отправиться на площадь."
    cs_narrator "Более того, уже успела мысленно выбрать место, откуда будет хорошо видно выступление Мику и Алисы."
    cs_narrator "Оставалось только дойти."
    cs_narrator "Задача, казалось бы, элементарная."
    cs_narrator "Особенно после того, как Дарья несколько раз напомнила мне, что сегодня больше не нужно никуда бежать."
    cs_narrator "Но почти у самой дорожки к клубам я остановилась."
    cs_th "Книга."
    cs_th "Точно."
    cs_narrator "Утром я бы наверняка развернула из этого целую трагедию. Рассказала о забывчивости, жестокости мироздания и том, как тяжело жить без электронных напоминаний."
    cs_narrator "Сейчас же просто посмотрела на Дарью."
    cs_ls "Даш, можно на несколько минут задержаться?"
    cs_narrator "Она повернулась ко мне."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Что случилось?"
    cs_ls "Хочу забрать книгу из домика и вернуть Жене. Мне там совсем немного осталось дочитать."
    cs_narrator "Дарья посмотрела в сторону площади."
    cs_narrator "Издалека доносились голоса и звуки настройки инструментов."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "А концерт?"
    cs_ls "Ещё не начался. Но если не успеем, оставлю книгу до завтра."
    cs_narrator "Она немного подумала."
    show cs_darya smile pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Хорошо. Только давай действительно ненадолго."
    cs_narrator "Я кивнула."
    cs_ls "Договорились."
    cs_narrator "Мы направились к домику."
    $ cs_director_scene("cs_house_lena_darya_int_day")
    scene cs_house_lena_darya_int_day at cs_house_full_frame
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Внутри я сразу подошла к тумбочке."
    cs_narrator "Книга лежала там, где я её оставила перед ужином."
    cs_narrator "Рядом лежала книга Дарьи."
    cs_narrator "Я взяла свой экземпляр, проверила закладку и осторожно прижала его к боку здоровой рукой."
    $ cs_reading_book_location = "lena_hand"
    cs_th "Не так уж много страниц."
    cs_th "За вечер вполне можно закончить."
    cs_narrator "Дарья стояла возле двери."
    show cs_darya thinking pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Всё?"
    cs_ls "Угу."
    cs_narrator "Я посмотрела на неё."
    cs_ls "Спасибо, что согласилась зайти."
    cs_narrator "Она улыбнулась."
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    # cs_global_transition
    with cs_sprite_change
    cs_da "Не за что. Только постарайся не растягивать прощание с Женей на полчаса."
    cs_narrator "Я усмехнулась."
    cs_ls "Никаких торжественных церемоний."
    $ cs_director_scene("cs_house_lena_darya_ext_day")
    scene cs_house_lena_darya_ext_day
    show cs_darya shrug pioneer normal at cs_darya_normal_right
    $ cs_presence_stage()
    with Dissolve(0.8)
    cs_narrator "Мы вышли."
    cs_th "Вот ведь."
    cs_th "Ещё вчера мне казалось невероятно забавным само существование Жени."
    cs_th "А теперь я просто хочу вернуть человеку книгу и сказать, что она мне понравилась."
    cs_th "Наверное, это и называется нормальным знакомством."
    return
